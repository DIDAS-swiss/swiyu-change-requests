# swiyu change requests

Change request proposals from the [DIDAS](https://didas.swiss) community for the
[swiyu](https://github.com/swiyu-admin-ch) team to consider.

swiyu is the Swiss e-ID trust infrastructure. Its specifications and reference
components are developed by the Federal Administration in the
[swiyu-admin-ch](https://github.com/swiyu-admin-ch) GitHub organisation. This
repository is where DIDAS members **draft, discuss and consolidate** proposed
changes before they are handed to the swiyu team, so that the ecosystem
(issuers, verifiers, wallets, integrators) can actually implement and operate
the infrastructure.

## What belongs here

- Proposed changes to swiyu specifications, profiles, APIs or trust frameworks
- Ecosystem feasibility concerns: things that are hard, costly or impossible
  for participants to implement as currently specified
- Gaps or ambiguities in the documentation that block implementation

What does **not** belong here:

- Bugs in a specific swiyu component: report them directly in that component's
  repository (e.g. [swiyu-issuer](https://github.com/swiyu-admin-ch/swiyu-issuer),
  [swiyu-verifier](https://github.com/swiyu-admin-ch/swiyu-verifier))
- Security vulnerabilities: follow the swiyu responsible disclosure process,
  never post them publicly here

## How it works

Every proposal is sent to swiyu on behalf of DIDAS, so it always needs input
from the community: a **steward** guides it, **working groups** are consulted,
and a **council** endorses it before submission.

```
Issue ──► Draft PR ──► Consultation ──► Council decision ──► Submitted ──► Outcome
          steward      working groups   endorse / return /   upstream      accepted / declined /
          assigned     ≥ 14 days        reject               link          implemented / withdrawn
```

1. **Open an issue** using the *Change request* or *Feasibility concern* template.
   A steward is assigned.
2. **Write a proposal**: copy [`proposals/0000-template.md`](proposals/0000-template.md)
   and open a draft pull request.
3. **Consultation**: the steward opens the proposal to the responsible working
   group(s) and the community for at least 14 days and summarises the input.
4. **Council decision**: the council endorses, returns or rejects the proposal.
   Only endorsed proposals are merged.
5. **Submit upstream**: the steward submits the proposal to the swiyu team
   (typically via [swiyu-admin-ch/community](https://github.com/swiyu-admin-ch/community))
   and records the link.
6. **Track the outcome** in the proposal and the [index](proposals/README.md).

Time-critical topics can reach swiyu earlier through a council-authorised
**early notice**.

- [GOVERNANCE.md](GOVERNANCE.md): roles, gates, early notice, transparency
- [CONTRIBUTING.md](CONTRIBUTING.md): step-by-step workflow, statuses, labels

## Proposals

The list of all proposals and their status is kept in
[`proposals/README.md`](proposals/README.md).

## Licence

[MIT](LICENSE)
