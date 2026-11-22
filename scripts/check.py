"""Consistency checks for the repository, run by .github/workflows/check.yml.

Checks internal links and the changelog index. Checks the front matter of every
change request against both indexes. Checks that aspects, statuses and sectors
agree across ASPECTS.md, CONTRIBUTING.md, the intake form and the label
workflow. Checks the writing rules that can be checked mechanically.

Run locally with: python3 scripts/check.py
"""

import glob
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

problems = []


def report(message):
    problems.append(message)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def front_matter(path):
    m = re.match(r"---\n(.*?)\n---\n", read(path), re.S)
    return yaml.safe_load(m.group(1)) if m else None


def slug(heading):
    h = heading.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


files = subprocess.check_output(["git", "ls-files"], text=True).split()
markdown = [f for f in files if f.endswith(".md")]
anchors = {f: {slug(h) for h in re.findall(r"^#+\s+(.*)$", read(f), re.M)} for f in markdown}

# Internal links and anchors
for f in markdown:
    text = re.sub(r"```.*?```", "", read(f), flags=re.S)
    for m in re.finditer(r"\]\(([^)\s]+)\)", text):
        url = m.group(1)
        if re.match(r"(https?:|mailto:)", url):
            continue
        path, _, anchor = url.partition("#")
        target = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if path and not os.path.exists(target):
            report(f"{f}: broken link {url}")
            continue
        if path and os.path.basename(target) == "LICENSE":
            report(f"{f}: LICENSE is not published on the website, link to GitHub instead")
        if anchor and target.endswith(".md") and anchor not in anchors.get(target, set()):
            report(f"{f}: missing anchor {url}")

# Changelog index
entries = sorted(os.path.basename(p) for p in glob.glob("changelog/2*.md"))
index = read("changelog/README.md")
listed = re.findall(r"\]\((2[^)]+\.md)\)", index)
for e in entries:
    if e not in listed:
        report(f"changelog/README.md: {e} is not listed")
for e in listed:
    if e not in entries:
        report(f"changelog/README.md: lists {e}, which does not exist")
dates = [e[:10] for e in listed]
if dates != sorted(dates, reverse=True):
    report("changelog/README.md: entries are not newest first")
for e in entries:
    first = read("changelog/" + e).splitlines()[0]
    if not first.startswith("# " + e[:10]):
        report(f"changelog/{e}: heading does not start with the date of the file name")

# Vocabularies
aspects_md = read("ASPECTS.md")
aspect_ids = re.findall(r"`aspect: ([a-z-]+)`", aspects_md)
aspect_names = re.findall(r"^\| ([A-Z][^|]+?) \| `aspect:", aspects_md, re.M)
contributing = read("CONTRIBUTING.md")
statuses = re.findall(r"^\| ([A-Z][a-z ]+) \| [A-Z]", contributing.split("## Statuses", 1)[1].split("##", 1)[0], re.M)
workflow = read(".github/workflows/sync-labels.yml")
labels = set(re.findall(r"\['([^']+)',", workflow))
sector_labels = re.findall(r"'sector: ([a-z-]+)'", workflow)
form = yaml.safe_load(read(".github/ISSUE_TEMPLATE/change-request.yml"))
fields = {b.get("id"): b for b in form["body"]}

if sorted(re.findall(r"'aspect: ([a-z-]+)'", workflow)) != sorted(aspect_ids):
    report("aspect labels in sync-labels.yml differ from ASPECTS.md")
primary = [o.split(":")[0] for o in fields["aspect"]["attributes"]["options"]]
if primary != aspect_names:
    report("primary aspects in the intake form differ from ASPECTS.md")
if fields["secondary-aspects"]["attributes"]["options"] != aspect_names:
    report("secondary aspects in the intake form differ from ASPECTS.md")
if len(fields["sectors"]["attributes"]["options"]) != len(sector_labels) + 1:
    report("sectors in the intake form differ from the sector labels")
if sorted(set(re.findall(r"`status: ([a-z-]+)`", contributing))) != sorted(re.findall(r"'status: ([a-z-]+)'", workflow)):
    report("status labels in CONTRIBUTING.md differ from sync-labels.yml")
for label in form["labels"]:
    if label not in labels:
        report(f"intake form label {label} is not in sync-labels.yml")
for f in markdown:
    for label in re.findall(r"`((?:status|aspect|sector): [a-z-]+|needs-steward|cross-sector|escalated|change-request)`", read(f)):
        if label not in labels:
            report(f"{f}: label {label} is not in sync-labels.yml")

# Change requests
project_index = read("proposals/README.md")
readme = read("README.md")
for path in sorted(glob.glob("proposals/CR-DIDAS-*.md")):
    name = os.path.basename(path)
    m = re.match(r"(CR-DIDAS-\d{4})-[a-z0-9-]+\.md$", name)
    if not m:
        report(f"{path}: file name does not follow CR-DIDAS-NNNN-short-title.md")
        continue
    number = m.group(1)
    fm = front_matter(path)
    if not fm:
        report(f"{path}: no front matter")
        continue
    for key in ("title", "cr", "status", "aspects", "sectors", "steward", "updated"):
        if key not in fm:
            report(f"{path}: front matter lacks {key}")
    if fm.get("cr") != number:
        report(f"{path}: cr is {fm.get('cr')}, file name says {number}")
    title = fm.get("title", "")
    if not title.startswith(number + ": "):
        report(f"{path}: title does not start with {number}")
    h1 = re.search(r"^# (.*)$", read(path), re.M)
    if not h1 or h1.group(1) != title:
        report(f"{path}: first heading differs from the title")
    if fm.get("status") not in statuses:
        report(f"{path}: unknown status {fm.get('status')}")
    for a in fm.get("aspects", []):
        if a not in aspect_ids:
            report(f"{path}: unknown aspect {a}")
    for s in fm.get("sectors", []):
        if s not in sector_labels + ["cross-sector"]:
            report(f"{path}: unknown sector {s}")
    short = title.split(": ", 1)[-1]
    for index_name, text in (("proposals/README.md", project_index), ("README.md", readme)):
        rows = [line for line in text.splitlines() if f"[{number}]" in line]
        if not rows:
            report(f"{index_name}: {number} is missing")
            continue
        row = rows[0]
        for label, value in (("title", short), ("status", fm.get("status", "")),
                             ("aspects", ", ".join(fm.get("aspects", []))),
                             ("sectors", ", ".join(fm.get("sectors", [])))):
            if value not in row:
                report(f"{index_name}: {label} of {number} differs from the change request")
    text = read(path)
    for ref in set(re.findall(r"\]\[([a-z0-9-]+)\]", text)):
        if not re.search(r"^\[" + re.escape(ref) + r"\]:", text, re.M):
            report(f"{path}: reference [{ref}] is not defined")
    for ref in re.findall(r"^\[([a-z0-9-]+)\]:", text, re.M):
        if not re.search(r"\]\[" + re.escape(ref) + r"\]", text):
            report(f"{path}: reference [{ref}] is defined but not used")
    for url in re.findall(r"https://github\.com/swiyu-admin-ch/[^\s)>]+/blob/([^/]+)/", text):
        if not re.fullmatch(r"[0-9a-f]{40}", url):
            report(f"{path}: link to swiyu-admin-ch is not pinned to a commit ({url})")
for line in project_index.splitlines() + readme.splitlines():
    for number in re.findall(r"\[(CR-DIDAS-\d{4})\]", line):
        if not glob.glob(f"proposals/{number}-*.md"):
            report(f"index lists {number}, which has no file")

# Writing rules that can be checked mechanically
rules = [
    (r",\s+and\b", "comma before 'and'"),
    ("—", "em dash"),
    (r"\bnot only\b", "'not only'"),
    (r"\b(crucial|essential|holistic|seamless(ly)?|leverag\w*|robust|empower\w*|unlock\w*)\b", "filler word"),
]
for f in files:
    if not f.endswith((".md", ".yml", ".html")) or f.startswith("assets/"):
        continue
    text = read(f)
    for pattern, what in rules:
        for m in re.finditer(pattern, text, re.I):
            line = text[: m.start()].count("\n") + 1
            report(f"{f}:{line}: {what}: '{m.group(0).strip()}'")

if problems:
    print("\n".join(problems))
    sys.exit(1)
print("All checks passed.")
