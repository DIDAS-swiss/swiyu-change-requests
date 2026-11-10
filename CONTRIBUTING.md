# Contributing

Thank you for helping make swiyu work for the whole ecosystem. This document
describes how change request proposals are written and reviewed. Who decides
what, and when, is set out in [GOVERNANCE.md](GOVERNANCE.md): every proposal
needs input from DIDAS stewards, working groups and councils before it is sent
to the swiyu team.

## Principles

- **Ecosystem first.** Every proposal explains who is affected (issuers,
  verifiers, wallets, relying parties, holders, integrators, governing
  authorities) and why the current state is a problem for them.
- **Evidence over opinion.** Link to the exact spec section, code, standard or
  implementation experience that motivates the change.
- **Constructive and concrete.** Propose a specific change, list alternatives,
  and be honest about drawbacks.
- **Community before submission.** Proposals go to the swiyu team on behalf of
  DIDAS only after working group consultation and council endorsement.
- **Consistent terminology.** Use the terms defined in the
  [DIDAS glossary](https://github.com/DIDAS-swiss/didas-glossary).

## Workflow

### 1. Discussion (issue)

Open an issue with the **Change request** or **Feasibility concern** template.
Keep it short: the problem, who it affects, and a first idea for a solution.
A maintainer labels it and asks for a **steward** to be assigned.

### 2. Draft (pull request)

Once a steward is assigned:

1. Copy `proposals/0000-template.md` to `proposals/NNNN-short-title.md`, using
   the next free number.
2. Fill in every section (write "n/a" rather than deleting one) and the
   *Governance* table as far as known.
3. Add a row to the index in `proposals/README.md`.
4. Open a pull request that references the issue. Keep it as a **draft pull
   request** until the steward starts consultation.

### 3. Consultation

The steward marks the pull request ready for review, labels it
`status: consultation`, names the working group(s) in the *Governance* table
and announces the consultation to them.

- The consultation lasts **at least 14 days**.
- Anyone may comment; each consulted working group states its position
  (support, support with changes, object, abstain).
- Authors update the proposal in the same pull request.
- At the end, the steward writes the *Community input* summary, including
  dissenting views.

### 4. Council decision

The steward brings the proposal to the council and labels it
`status: council`. The council endorses, returns or rejects it. The decision,
date and a link to minutes go into the *Governance* table.

A maintainer **merges the pull request only after endorsement**. Merged
proposals have status *Endorsed*.

### 5. Submission upstream

The steward (or a maintainer on their behalf) submits the proposal to the swiyu
team, by default in
[swiyu-admin-ch/community](https://github.com/swiyu-admin-ch/community) or in
the relevant component repository, and records the link in the proposal.
Status becomes *Submitted*.

### 6. Outcome

When swiyu responds, the steward updates *Status*, *Upstream* and *Outcome* in
the proposal and the index, in a small follow-up pull request.

### Early notice

If a topic needs to reach swiyu before the full process completes, the steward
can ask the council for an early notice. See
[GOVERNANCE.md](GOVERNANCE.md#early-notice).

## Proposal statuses

| Status | Meaning |
| --- | --- |
| Draft | Being written; no steward review yet |
| In consultation | Open for working group and community input |
| Awaiting council | Consultation closed; awaiting council decision |
| Endorsed | Endorsed by the council; ready to submit |
| Submitted | Sent to the swiyu team; awaiting response |
| Accepted | swiyu has agreed to make the change (fully or partly) |
| Implemented | The change is live in a swiyu spec or release |
| Declined | swiyu has decided not to make the change |
| Withdrawn | Withdrawn by the authors, rejected by the council, or superseded |

## Labels

| Label | Use |
| --- | --- |
| `change-request` | Proposed change to a spec, API or framework |
| `feasibility` | Ecosystem feasibility concern |
| `documentation` | Gap or ambiguity in the swiyu documentation |
| `needs-steward` | Waiting for a steward to be assigned |
| `status: discussion` | Being discussed, no proposal yet |
| `status: draft` | Proposal PR open, being written |
| `status: consultation` | Open for working group and community input |
| `status: council` | Awaiting council decision |
| `status: endorsed` | Endorsed, ready to submit |
| `status: early-notice` | Council authorised an early notice to swiyu |
| `status: submitted` | Sent to swiyu |
| `status: closed-upstream` | swiyu has responded (see proposal) |
| `area: issuance` | OID4VCI, swiyu-issuer |
| `area: verification` | OID4VP, swiyu-verifier |
| `area: wallet` | swiyu wallet apps, holder experience |
| `area: trust` | Trust registry, trust statements, governance |
| `area: identifiers` | DIDs, did:webvh, DID resolution |
| `area: status` | Status lists, revocation |
| `area: credential-format` | SD-JWT VC, OCA, schemas |
| `area: security` | Cryptography, key management, attestation |

## Style

- Write in English (proposals may include German/French/Italian quotes from
  official sources).
- One proposal per file; one topic per proposal.
- Use normative keywords (MUST, SHOULD, MAY) only when quoting or proposing
  normative text.
- Disclose relevant interests (see [GOVERNANCE.md](GOVERNANCE.md#conflicts-of-interest)).
