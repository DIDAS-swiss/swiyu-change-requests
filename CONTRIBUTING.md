---
title: Contributing
---

# Contributing

Thank you for helping make swiyu work for the whole ecosystem. This guide
describes how change requests are written and reviewed. Who decides what, and
when, is set out in [GOVERNANCE.md](GOVERNANCE.md): every change request needs
input from the sectoral working groups and councils concerned, guided by a
steward, before DIDAS submits it to the swiyu team.

## Principles

- **Ecosystem first.** Every change request explains who is affected (issuers,
  verifiers, wallets, holders, integrators, governing authorities) and why the
  current state is a problem for them.
- **Verified against the spec, always.** Every statement about swiyu is checked
  against the current specifications and code in
  [swiyu-admin-ch](https://github.com/swiyu-admin-ch) and referenced. See
  [Verifying and referencing the spec](#verifying-and-referencing-the-spec).
- **Grounded in real use.** Link the use cases in the
  [Use Case Repository](https://github.com/DIDAS-swiss/use-case-repository) and
  the trust flows in the
  [Trust Flow Diagram Repository](https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository)
  that run into the problem.
- **Constructive and concrete.** Propose a specific change, list alternatives,
  and be honest about drawbacks.
- **Community before submission.** Change requests go to the swiyu team on
  behalf of DIDAS only after consultation and endorsement.
- **Consistent terminology.** Use the terms of the
  [DIDAS Glossary](https://github.com/DIDAS-swiss/didas-glossary).

## Workflow

### 1. Discussion (issue)

Open an issue with the **Change request** or **Feasibility concern** form.
Keep it short: the problem, the sectors it affects, and a first idea. A
maintainer adds `sector:` labels and asks for a **steward** (label
`needs-steward`).

### 2. Draft (pull request)

Once a steward is assigned:

1. Copy `proposals/0000-template.md` to `proposals/CR-DIDAS-NNNN-short-title.md`, using
   the next free number.
2. Fill in the front matter and every section (write "n/a" rather than
   deleting one). Verify and reference every claim about swiyu.
3. Add a row to the index in `proposals/README.md` and an entry in
   `changelog/`.
4. Open a **draft pull request** that references the issue.

### 3. Consultation

The steward marks the pull request ready for review, labels it
`status: consultation`, names the working group(s) of the affected sectors in
the *Governance* table and announces the consultation to them.

- The consultation lasts **at least 14 days**.
- Anyone may comment; each consulted working group states its position
  (support, support with changes, object, abstain).
- Authors update the proposal in the same pull request.
- At the end, the steward writes the *Community input* summary, including
  dissenting views.

### 4. Council decision

The steward brings the change request to the council(s) of the affected sectors
and labels it `status: council`. Each council endorses, returns or rejects it.
For a cross-sector change request, DIDAS as orchestrator consolidates the
positions and escalates to the Steering Circle where they conflict or the
question is strategic (see
[GOVERNANCE.md](GOVERNANCE.md#single-sector-and-cross-sector-change-requests)).
Decisions, dates and links to minutes go into the *Governance* table.

A maintainer **merges the pull request only after endorsement**. Merged change
requests have status *Endorsed*.

### 5. Submission upstream

The steward, for DIDAS as orchestrator, submits the change request to the swiyu
team, by default in
[swiyu-admin-ch/community](https://github.com/swiyu-admin-ch/community) or in
the relevant component repository, and records the link. Status becomes
*Submitted*.

### 6. Outcome

When swiyu responds, the steward updates the status, *Upstream* and *Outcome*
in the proposal, the index and the changelog, in a small follow-up pull
request.

### Early notice

If a topic needs to reach swiyu before the full process completes, the steward
can ask for an early notice. See [GOVERNANCE.md](GOVERNANCE.md#early-notice).

## Verifying and referencing the spec

The swiyu specifications are published in
[swiyu-admin-ch/swiyu-admin-ch.github.io](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io)
(`_specifications/`, rendered at <https://swiyu-admin-ch.github.io/specifications/>);
the reference components are the other repositories in
[swiyu-admin-ch](https://github.com/swiyu-admin-ch). A change request that
misrepresents the spec costs DIDAS credibility, so:

1. **Check every input.** Every claim about how swiyu works, including claims
   from issues, comments or meetings, is checked against the current spec
   before it goes into a proposal. Where the spec is silent or ambiguous, check
   the reference implementation as well and say which one you relied on.
2. **Reference every claim.** Each claim links to its source with a
   **commit-pinned permalink** (`/blob/<commit-sha>/path#L10-L20`), not a link
   to a branch that can change. Quote the normative text where it matters.
3. **Record the spec version.** The proposal's *Sources* section lists every
   document used with its version, status and "last edited" date as shown in
   the document, and the commit checked.
4. **Note discrepancies.** If the spec and the implementation differ, or the
   swiyu documentation contradicts itself, say so rather than choosing
   silently.
5. **Re-verify before each gate.** The steward re-checks the *Sources* against
   the latest spec before consultation, before the council decision and before
   submission, and updates commits and wording if the spec has changed.

## Numbering

Change requests are numbered `CR-DIDAS-NNNN`, four digits, in the order their
proposal pull requests are opened (`CR-DIDAS-0001`, `CR-DIDAS-0002`, …). The
`DIDAS` part keeps them apart from swiyu's own numbering, such as its change
dossiers (`CD-NNN`), when they are discussed upstream. Use the full number in
the file name, the title, the issue and the upstream submission.

## Proposal front matter

Each proposal starts with front matter that the site shows as a facts panel:

```yaml
---
title: "CR-DIDAS-0001: Short title"
cr: CR-DIDAS-0001
status: Draft            # see statuses below
sectors: [health, education]   # ids from the DIDAS working groups
steward: TBD
updated: 2026-11-10
---
```

## Statuses

| Status | Meaning |
| --- | --- |
| Draft | Being written |
| In consultation | Open for working group and community input |
| Awaiting council | Consultation closed; awaiting council decision (or Steering Circle) |
| Endorsed | Endorsed; ready to submit |
| Submitted | Sent to the swiyu team; awaiting response |
| Accepted | swiyu has agreed to make the change (fully or partly) |
| Implemented | The change is live in a swiyu spec or release |
| Declined | swiyu has decided not to make the change |
| Withdrawn | Withdrawn by the authors, rejected by a council, or superseded |

## Labels

| Label | Use |
| --- | --- |
| `change-request` | Proposed change to a spec, API or framework |
| `feasibility` | Ecosystem feasibility concern |
| `documentation` | Gap or ambiguity in the swiyu documentation |
| `needs-steward` | Waiting for a steward |
| `cross-sector` | Affects more than one sector |
| `escalated` | Brought to the Steering Circle |
| `status: discussion` | Being discussed, no proposal yet |
| `status: draft` | Proposal PR open, being written |
| `status: consultation` | Open for working group and community input |
| `status: council` | Awaiting council decision |
| `status: endorsed` | Endorsed, ready to submit |
| `status: early-notice` | Early notice to swiyu authorised |
| `status: submitted` | Sent to swiyu |
| `status: closed-upstream` | swiyu has responded |
| `sector: <id>` | Affected sector, one per DIDAS working group (e.g. `sector: health`) |
| `area: issuance` | OID4VCI, swiyu-issuer |
| `area: verification` | OID4VP, swiyu-verifier |
| `area: wallet` | swiyu wallet apps, holder experience |
| `area: trust` | Trust registry, trust statements, trust protocol |
| `area: identifiers` | DIDs, did:webvh, DID resolution |
| `area: status` | Status lists, revocation |
| `area: credential-format` | SD-JWT VC, OCA, schemas |
| `area: security` | Cryptography, key management, attestation |

## Changelog

Every pull request that changes a rule, adds a proposal or changes a proposal's
status adds a file to [`changelog/`](changelog/README.md) named
`YYYY-MM-DD-short-title.md`.

## Style

- Write in English (proposals may quote German, French or Italian sources).
- One topic per change request.
- Use normative keywords (MUST, SHOULD, MAY) only when quoting or proposing
  normative text.
- Disclose relevant interests (see
  [GOVERNANCE.md](GOVERNANCE.md#conflicts-of-interest)).
