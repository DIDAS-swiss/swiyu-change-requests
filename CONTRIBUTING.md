---
title: Contributing
---

# Contributing

Status: proposal. The process, the governance, the aspects and the templates
in this repository are a DIDAS proposal for discussion with the stewards,
working groups and councils and with the swiyu ecosystem governance.

This guide describes how a change request is written and reviewed. Roles,
decisions and escalation are set out in [GOVERNANCE.md](GOVERNANCE.md).

## What a change request is

A change request names an obstacle that keeps actors from using swiyu, shows
who runs into it and states what should become possible. It is the input to a
pipeline: DIDAS consults and endorses it, submits it to the swiyu team and the
swiyu team decides how to respond. A change request stays at a high level and
typically does not propose code, data formats or API changes. Each one is
assigned to the [aspects](ASPECTS.md) it concerns.

A good change request:

- describes the problem from the perspective of the actors affected;
- supports statements about swiyu with references to the specification or code;
- shows the problem in a use case, trust flow or deployment;
- states the requested outcome without prescribing the solution;
- separates facts from assessments and names open questions and trade-offs.

## Workflow

### 1. Issue

Open an issue with the **Change request** form. A
maintainer adds the `aspect:` and `sector:` labels and the label
`needs-steward`.

### 2. Draft

Once a steward is assigned, copy `proposals/0000-template.md` to
`proposals/CR-DIDAS-NNNN-short-title.md` with the next free number, fill it in,
add a row to `proposals/README.md` and a file in `changelog/` and open a pull
request that references the issue.

When the steward confirms that the change request follows the template and that
its statements about swiyu are checked and referenced, a maintainer merges it
with the status *Draft*. Merging publishes the change request; it does not
mean that DIDAS endorses it. Every later step is a pull request that changes
the status, the *Governance* table, the index and the changelog.

### 3. Consultation

The steward sets the status to *In consultation*, labels the issue
`status: consultation` and notifies the working groups of the affected sectors.
The consultation runs in the discussion issue and lasts at least 14 days. Each
consulted working group states its position: support, support with changes,
object or abstain. The steward summarises the input, including dissent, under
*Community input*.

### 4. Council decision

The steward brings the change request to the councils of the affected sectors
and labels it `status: council`. For a change request that affects several
sectors, DIDAS consolidates the positions as orchestrator and brings conflicts
or strategic questions to the Steering Circle (see
[GOVERNANCE.md](GOVERNANCE.md#single-sector-and-cross-sector-change-requests)).
When the councils have decided, the steward records the decisions and sets the
status to *Endorsed* or, after a rejection, to *Withdrawn*.

### 5. Submission and outcome

The steward submits the change request to the swiyu team, by default in
[swiyu-admin-ch/community](https://github.com/swiyu-admin-ch/community) and
records the link. When swiyu responds, the steward updates the status, the
outcome, the index and the changelog.

If a topic has to reach swiyu before the process is complete, the steward can
request an [early notice](GOVERNANCE.md#early-notice).

## Verifying and referencing the spec

The swiyu specifications are in
[swiyu-admin-ch/swiyu-admin-ch.github.io](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io)
(`_specifications/`, published at <https://swiyu-admin-ch.github.io/specifications/>).
The reference components are the other repositories in
[swiyu-admin-ch](https://github.com/swiyu-admin-ch).

1. Every statement about how swiyu works is checked against the current
   specification before it goes into a change request, including statements
   taken from issues, comments or meetings. Where the specification is silent,
   check the reference implementation and say which source you relied on.
2. Every statement links to its source with a commit-pinned permalink
   (`/blob/<commit>/path#L10-L20`).
3. The *Sources* table lists each document with its version, its status as
   stated in the document, the commit checked and the date.
4. Contradictions between specification and implementation, or within the
   documentation, are stated.
5. The steward re-checks the sources before the consultation, before the
   council decision and before submission.

The requested outcome stays general. The description of the current state must
be exact.

## Numbering

Change requests are numbered `CR-DIDAS-NNNN` in the order their pull requests
are opened. The prefix separates them from swiyu's own numbering, such as its
change dossiers (`CD-NNN`). Use the full number in the file name, the title,
the issue and the submission.

## Front matter

```yaml
---
title: "CR-DIDAS-0001: Short title"
cr: CR-DIDAS-0001
status: Draft
aspects: [governance, costs]     # primary aspect first
sectors: [health]                # ids of the DIDAS working groups
steward: TBD
updated: 2026-11-22
---
```

## Statuses

| Status | Meaning |
| --- | --- |
| Draft | Being written |
| In consultation | Open for working group and community input |
| Awaiting council | Consultation closed, decision pending |
| Endorsed | Endorsed, ready to submit |
| Submitted | Submitted to the swiyu team |
| Accepted | swiyu has agreed to act on it, fully or in part |
| Implemented | The change is in a swiyu specification, release or legal text |
| Declined | swiyu has decided not to act on it |
| Withdrawn | Withdrawn by the authors, rejected by a council or superseded |

## Labels

| Label | Use |
| --- | --- |
| `change-request` | Change request |
| `needs-steward` | No steward assigned yet |
| `cross-sector` | Affects more than one sector |
| `escalated` | Brought to the Steering Circle |
| `aspect: <id>` | Aspect, see [ASPECTS.md](ASPECTS.md) |
| `sector: <id>` | Affected sector, one per DIDAS working group |
| `status: discussion`, `status: draft`, `status: consultation`, `status: council`, `status: endorsed`, `status: early-notice`, `status: submitted`, `status: closed-upstream` | Position in the workflow |

The workflow *Sync labels* (`.github/workflows/sync-labels.yml`) creates and
updates these labels. It runs when the workflow file changes on `main` and can
be started from the Actions tab. Change the list there.

## Changelog

Every pull request that changes a rule, adds a change request or changes its
status adds a file `changelog/YYYY-MM-DD-short-title.md`.

## Style

Write in English, in plain and precise sentences. Avoid promotional language
and filler. One topic per change request. Use the terms of the
[DIDAS Glossary](https://github.com/DIDAS-swiss/didas-glossary). Disclose
relevant interests (see [GOVERNANCE.md](GOVERNANCE.md#conflicts-of-interest)).
