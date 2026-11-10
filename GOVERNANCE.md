# Governance

Every change request in this repository is submitted to the swiyu team **on
behalf of the DIDAS community**. A proposal therefore never goes upstream on
the strength of its authors alone: it always needs input from the community
and an explicit endorsement before submission.

## Roles

| Role | Who | Responsibilities |
| --- | --- | --- |
| **Author** | Any DIDAS member or community participant | Raises the issue, writes and revises the proposal, responds to review. |
| **Steward** | A DIDAS steward assigned to the proposal | Owns the proposal through its lifecycle: checks scope and quality, picks the working group(s) to consult, runs the consultation, summarises the input, brings the proposal to the council and acts as contact person towards the swiyu team. |
| **Working group(s)** | The DIDAS working group(s) responsible for the subject matter | Provide expert review during consultation; state their position (support, support with changes, object, abstain) on the record. |
| **Council** | The DIDAS council responsible for the topic | Decides whether DIDAS endorses the proposal and submits it upstream; may authorise an early notice; decides on withdrawal. |
| **Maintainers** | Repository maintainers | Keep the repository, labels and index in order; merge pull requests once the gates below are met; record upstream links. |

A person can hold more than one role, but the **steward should not be the sole
author** of the proposal they steward.

## Lifecycle and gates

```
 ┌────────────┐   ┌─────────┐   ┌──────────────┐   ┌──────────────────┐   ┌───────────┐   ┌─────────┐
 │ Discussion │──►│  Draft  │──►│ Consultation │──►│ Council decision │──►│ Submitted │──►│ Outcome │
 └────────────┘   └─────────┘   └──────────────┘   └──────────────────┘   └───────────┘   └─────────┘
   issue           proposal PR    working groups,     endorse / return /     upstream link    accepted /
   steward         steward OK     open comment        reject                 recorded         implemented /
   assigned                       period                                                      declined /
                                                                                              withdrawn
              (optional) Early notice to swiyu — only with council authorisation, see below
```

| Gate | Condition to pass | Recorded in |
| --- | --- | --- |
| Discussion → Draft | A steward is assigned and agrees the topic is in scope. | Issue (assignee + `status: draft` label) |
| Draft → Consultation | Steward confirms the proposal is complete enough for review and names the working group(s) to consult. | Proposal *Governance* table |
| Consultation → Council decision | Consultation period has ended (at least **14 days**); every consulted working group has stated a position; the steward has summarised the input, including dissenting views. | Proposal *Community input* section |
| Council decision → Submitted | Council has **endorsed** the proposal. | Proposal *Governance* table (date, decision, link to minutes) |
| Submitted → Outcome | swiyu has responded or the proposal is withdrawn. | Proposal *Outcome* section and index |

If the council **returns** the proposal, it goes back to Draft or Consultation
with the council's requests recorded. If the council **rejects** it, the
proposal is set to *Withdrawn* with the reason recorded.

## Early notice

Some issues need to reach the swiyu team before a full proposal is ready, for
example when a specification is about to be finalised. For these cases the
council (or its chair, if the council has delegated this) may authorise an
**early notice**:

- it describes the **problem and its ecosystem impact only**, not a DIDAS
  position on the solution;
- it states clearly that the topic is still in DIDAS community consultation;
- it links to the proposal in this repository;
- the authorisation is recorded in the proposal's *Governance* table.

An early notice does not replace consultation or endorsement of the full
proposal.

## Transparency

- All discussion happens in issues and pull requests in this repository, or is
  summarised there when it happens in working group or council meetings.
- Working group positions and council decisions are recorded in the proposal
  itself, with links to minutes where they exist.
- Dissenting views are kept in the proposal, not removed.

## Conflicts of interest

Participants disclose relevant commercial or organisational interests in the
issue or pull request (e.g. "my organisation builds an issuer product affected
by this"). Disclosure does not exclude anyone from the discussion; the steward
takes it into account when summarising input.
