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

```
Idea ──► Issue (discussion) ──► Proposal PR ──► DIDAS review ──► Submitted upstream ──► Outcome
                                (proposals/)    (consensus)      (link to swiyu)       accepted / declined / withdrawn
```

1. **Open an issue** using the *Change request* or *Feasibility concern* template
   to check interest and collect input.
2. **Write a proposal** once there is enough substance: copy
   [`proposals/0000-template.md`](proposals/0000-template.md) and open a pull request.
3. **Review**: DIDAS members review the PR. A proposal is merged once there is
   rough consensus that it is ready for the swiyu team.
4. **Submit upstream**: a maintainer forwards the proposal to the swiyu team
   (typically via [swiyu-admin-ch/community](https://github.com/swiyu-admin-ch/community))
   and records the link in the proposal.
5. **Track the outcome**: the proposal's status and the [index](proposals/README.md)
   are updated when swiyu responds.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details, statuses and labels.

## Proposals

The list of all proposals and their status is kept in
[`proposals/README.md`](proposals/README.md).

## Licence

[MIT](LICENSE)
