# Governance

This document defines how change requests for swiyu are raised, consulted,
endorsed and submitted. Every change request is submitted to the swiyu team
**on behalf of the DIDAS community**, so none goes upstream on the strength of
its authors alone: it always needs input from the sectoral working groups and
councils concerned, guided by a steward.

It follows the intake model of the
[DIDAS Glossary](https://github.com/DIDAS-swiss/didas-glossary/blob/main/GOVERNANCE.md)
and the [DIDAS Use Case Repository](https://github.com/DIDAS-swiss/use-case-repository/blob/main/GOVERNANCE.md),
and maps onto the swiyu ecosystem governance below.

## Ecosystem governance

The swiyu ecosystem governance is a **working draft**. As currently drafted it
has three levels:

| Level | Who | In relation to change requests |
| --- | --- | --- |
| **Steering Circle** | Public sector (BJ, Fachbereich e-ID; fedpol; …), the swiyu orchestrators (DVS, DIDAS), swiyu ambassadors (digitalswitzerland; …), and AN3 ecosystem stewards and councils | Receives reporting, needs and strategic questions from the orchestrators. Gives sponsoring and resources, goals, advice and priorities, and handles conflict management. |
| **swiyu Orchestrators** | Digitale Verwaltung Schweiz (DVS) and DIDAS | Collect industry and domain knowledge, pain points, use cases and needs from the sectors. Give advice, technical support, methodology, tools and network back. DIDAS runs this repository as its orchestrator methodology for change requests. |
| **Sectoral councils and working groups** | Education, Banking, eCommerce & Retail, Health, … | Bring industry and domain knowledge, pain points, use cases, needs and questions. DIDAS members contribute through them. |

```
                ┌───────────────────────── Steering Circle ─────────────────────────┐
                │  Public sector · swiyu orchestrators · ambassadors · AN3 stewards  │
                └────────────────────────────────────────────────────────────────────┘
     reporting, needs, strategic questions ▲            │ sponsoring, goals, advice,
                                           │            ▼ priorities, conflict management
                ┌──────────────────── swiyu Orchestrators: DVS · DIDAS ──────────────┐
                └────────────────────────────────────────────────────────────────────┘
  domain knowledge, pain points, use cases ▲            │ advice, tech support,
                                           │            ▼ methodology, tools, network
                ┌──────────────── Sectoral councils & working groups ────────────────┐
                │      Education · Banking · eCommerce & Retail · Health · …          │
                └────────────────────────────────────────────────────────────────────┘
```

A change request is a pain point or need that travels **up** this structure:
it starts in a sector, is consulted and endorsed by the sector, carried by DIDAS
as orchestrator to the swiyu team, and reported to the Steering Circle.

## Principles

1. **Issues are intake, the pull request is the governance artifact, merge to
   `main` is endorsement.** Every decision is recorded in issue and PR history.
2. **Sectors decide what they need.** A change request is endorsed by the
   sectoral council(s) it affects, after their working groups were consulted.
3. **Verified against the spec, always.** Every statement about swiyu is
   checked against the current specifications and code in
   [swiyu-admin-ch](https://github.com/swiyu-admin-ch) and referenced with
   commit-pinned links. See
   [CONTRIBUTING.md](CONTRIBUTING.md#verifying-and-referencing-the-spec).
4. **Reference, don't duplicate.** Use cases, trust flows and terms stay in the
   [Use Case Repository](https://github.com/DIDAS-swiss/use-case-repository),
   the [Trust Flow Diagram Repository](https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository)
   and the [DIDAS Glossary](https://github.com/DIDAS-swiss/didas-glossary).
   A change request links to them as evidence.
5. **Escalate, don't stall.** Cross-sector conflicts and strategic questions go
   to the Steering Circle.

## Roles

| Role | In this repository | Ecosystem governance |
| --- | --- | --- |
| **Community participant** | Anyone with a GitHub account. Opens issues, comments, adds 👍 to show that others are affected. | — |
| **Author** | Raises the issue and writes the proposal, on behalf of an identified organisation where possible. | DIDAS member |
| **Sectoral working group** | Consulted on every change request that affects its sector. States a position on the record: support, support with changes, object, abstain. The groups are listed in the [Use Case Repository](https://github.com/DIDAS-swiss/use-case-repository/blob/main/_data/working-groups.csv). | Sectoral working group |
| **Sectoral council** | Endorses, returns or rejects a change request for its sector. | Sectoral council |
| **Steward** | Named per change request in [STEWARDS.md](STEWARDS.md) and the proposal. Owns it through its lifecycle: checks scope and quality, verifies the spec references, picks the sectors to consult, runs the consultation, summarises the input, brings it to the council(s), and is the contact for the swiyu team. | Ecosystem steward |
| **Orchestrator (DIDAS)** | Consolidates the positions of several sectors on a cross-sector change request, submits endorsed change requests to the swiyu team, reports to the Steering Circle, and coordinates with DVS where the public sector is affected. | swiyu Orchestrator |
| **Steering Circle** | Decides on escalations: conflicts between sectors, strategic questions and priorities. | Steering Circle |
| **Maintainers** | Repository administration, labels, index, changelog, site. Merge once the gates are met. | — |

A person can hold more than one role, but the **steward should not be the sole
author** of the change request they steward.

## Lifecycle and gates

```
 Discussion ──► Draft ──► Consultation ──► Council decision ──► Submitted ──► Outcome
 issue,         PR,       sectoral WGs,     sectoral           by DIDAS as    accepted /
 steward        spec      ≥ 14 days         council(s);        orchestrator;  implemented /
 assigned       verified                    cross-sector:      reported to    declined /
                                            consolidated by    Steering       withdrawn
                                            the orchestrator   Circle
```

| Gate | Condition to pass | Recorded in |
| --- | --- | --- |
| Discussion → Draft | A steward is assigned and agrees the topic is in scope; the affected sectors are named. | Issue (assignee, `sector:` labels, `status: draft`) |
| Draft → Consultation | Every claim is verified against the current swiyu spec and referenced (*Sources*); the steward names the working group(s) to consult. | Proposal *Governance* and *Sources* tables |
| Consultation → Council decision | At least **14 days** have passed; every consulted working group has stated a position; the steward has summarised the input, including dissent. | Proposal *Community input* section |
| Council decision → Submitted | The sectoral council(s) concerned have **endorsed** it (cross-sector: see below); the steward has re-verified the *Sources* against the latest spec. | Proposal *Governance* table (date, decision, link to minutes) |
| Submitted → Outcome | swiyu has responded, or the change request is withdrawn. | Proposal *Outcome* section, index, changelog |

If a council **returns** the change request, it goes back to Draft or
Consultation with the council's requests recorded. If it **rejects** it, the
status becomes *Withdrawn* with the reason.

### Single-sector and cross-sector change requests

- **Single sector**: the council of that sector decides.
- **Cross-sector**: the council of every sector named in the proposal is asked.
  DIDAS as orchestrator consolidates their positions. If they agree, the change
  request is endorsed. If they disagree, or the change request raises a
  strategic question for the ecosystem, the orchestrator brings it to the
  **Steering Circle**, whose decision is recorded in the proposal.
- **No council yet**: where a sector has no council, its working group's
  position stands in, and the orchestrator records that it did.

## Early notice

Some issues need to reach the swiyu team before a full change request is ready,
for example while a specification is still a draft. For these the council(s)
concerned, or DIDAS as orchestrator for a cross-sector topic, may authorise an
**early notice**:

- it describes the **problem and its ecosystem impact only**, not a DIDAS
  position on the solution;
- it states that the topic is in DIDAS community consultation;
- it links to the proposal in this repository;
- the authorisation is recorded in the proposal and reported to the Steering
  Circle.

An early notice does not replace consultation or endorsement.

## Reporting

DIDAS as orchestrator reports the change requests and their status to the
Steering Circle. The [published site](https://didas-swiss.github.io/swiyu-change-requests/)
and the [index](proposals/README.md) are the basis for that report.

## Transparency

- All discussion happens in issues and pull requests in this repository, or is
  summarised there when it happens in working group, council or Steering Circle
  meetings.
- Working group positions, council decisions and escalations are recorded in
  the proposal, with links to minutes where they exist.
- Dissenting views stay in the proposal.
- Every change to the repository's rules or to a proposal's status gets a
  [changelog](changelog/README.md) entry in the same pull request.

## Conflicts of interest

Participants disclose relevant commercial or organisational interests in the
issue or pull request. Disclosure does not exclude anyone from the discussion;
the steward takes it into account when summarising input.

## Status of this document

The swiyu ecosystem governance above is a working draft. When it changes, this
document is updated in a pull request with a changelog entry.
