# Contributing

Thank you for helping make swiyu work for the whole ecosystem. This document
describes how change request proposals are written, reviewed and handed over
to the swiyu team.

## Principles

- **Ecosystem first.** Every proposal explains who is affected (issuers,
  verifiers, wallets, relying parties, holders, integrators) and why the
  current state is a problem for them.
- **Evidence over opinion.** Link to the exact spec section, code, standard or
  implementation experience that motivates the change.
- **Constructive and concrete.** Propose a specific change, list alternatives,
  and be honest about drawbacks.
- **Consensus before submission.** Proposals go to the swiyu team on behalf of
  DIDAS only after review here.
- **Consistent terminology.** Use the terms defined in the
  [DIDAS glossary](https://github.com/DIDAS-swiss/didas-glossary).

## Workflow

### 1. Discuss in an issue

Open an issue with the **Change request** or **Feasibility concern** template.
Keep it short: the problem, who it affects, and a first idea for a solution.
Use the issue to gather input and find co-authors.

### 2. Write the proposal

When the idea is mature enough:

1. Copy `proposals/0000-template.md` to
   `proposals/NNNN-short-title.md`, using the next free number.
2. Fill in every section (write "n/a" rather than deleting one).
3. Add a row to the index in `proposals/README.md`.
4. Open a pull request that references the issue (`Closes #123`).

### 3. Review

- Anyone may review; at least **two DIDAS members from different
  organisations** should approve before merge.
- Open questions are resolved in the PR or listed under *Open questions*.
- On merge, the status becomes **Ready for submission**.

### 4. Submit upstream

A maintainer submits the proposal to the swiyu team (by default as an issue or
discussion in [swiyu-admin-ch/community](https://github.com/swiyu-admin-ch/community),
or in the relevant component repository) and updates the proposal with the
upstream link and status **Submitted**.

### 5. Track the outcome

When swiyu responds, update the proposal's *Status* and *Upstream* fields and
the index. Summarise the swiyu response under *Outcome*.

## Proposal statuses

| Status | Meaning |
| --- | --- |
| Draft | Being written; PR open |
| Ready for submission | Reviewed and merged; not yet sent upstream |
| Submitted | Sent to the swiyu team; awaiting response |
| Accepted | swiyu has agreed to make the change (fully or partly) |
| Implemented | The change is live in a swiyu spec or release |
| Declined | swiyu has decided not to make the change |
| Withdrawn | Withdrawn by the authors or superseded |

## Labels

| Label | Use |
| --- | --- |
| `change-request` | Proposed change to a spec, API or framework |
| `feasibility` | Ecosystem feasibility concern |
| `documentation` | Gap or ambiguity in the swiyu documentation |
| `status: discussion` | Being discussed, no proposal yet |
| `status: draft` | Proposal PR open |
| `status: ready` | Proposal merged, ready to submit |
| `status: submitted` | Sent to swiyu |
| `status: closed-upstream` | swiyu has responded (see proposal) |
| `area: issuance` | OID4VCI, swiyu-issuer |
| `area: verification` | OID4VP, swiyu-verifier |
| `area: wallet` | swiyu wallet apps, holder experience |
| `area: trust` | Trust registry, trust statements, governance |
| `area: identifiers` | DIDs, did:tdw/did:webvh, DID resolution |
| `area: status` | Status lists, revocation |
| `area: credential-format` | SD-JWT VC, OCA, schemas |
| `area: security` | Cryptography, key management, attestation |

## Style

- Write in English (proposals may include German/French/Italian quotes from
  official sources).
- One proposal per file; one topic per proposal.
- Use normative keywords (MUST, SHOULD, MAY) only when quoting or proposing
  normative text.
