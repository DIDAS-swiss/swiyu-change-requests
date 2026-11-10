# swiyu Change Requests

**Website: <https://didas-swiss.github.io/swiyu-change-requests/>**

Change requests from the [DIDAS](https://www.didas.swiss) community for the
swiyu team to consider. swiyu is the Swiss e-ID trust infrastructure; its
specifications and reference components are developed by the Federal
Administration in [swiyu-admin-ch](https://github.com/swiyu-admin-ch). Here,
DIDAS members raise, consult and consolidate the changes the ecosystem needs so
that issuers, verifiers, wallets and sectors can actually build on swiyu. DIDAS
submits them to the swiyu team in its role as swiyu orchestrator.

<p class="gh-only"><a href="https://github.com/DIDAS-swiss/swiyu-change-requests/issues/new?template=change-request.yml"><b>+ Raise a change request</b></a> · <a href="https://github.com/DIDAS-swiss/swiyu-change-requests/issues/new?template=feasibility-concern.yml">Report a feasibility concern</a> · <a href="https://didas-swiss.github.io/swiyu-change-requests/">Open the website</a></p>

## Change requests

| CR | Title | Sectors | Status |
| --- | --- | --- | --- |
| [CR-0001](proposals/0001-sectoral-issuer-authorization.md) | Sectoral governing authorities managing authorized issuers per credential type | cross-sector, health | Draft |

The full list with stewards and upstream links is in the
[index](proposals/README.md).

## How it works

Every change request is submitted on behalf of DIDAS, so it always needs input
from the community: a **steward** guides it, the **sectoral working groups**
are consulted, and the **sectoral councils** endorse it. Cross-sector conflicts
and strategic questions go to the swiyu **Steering Circle**.

```
Issue ──► Draft PR ──► Consultation ──► Council decision ──► Submitted ──► Outcome
          steward,     sectoral WGs,    sectoral council(s);  by DIDAS as    accepted /
          spec         ≥ 14 days        cross-sector:          orchestrator   declined /
          verified                      consolidated, or                      implemented /
                                        Steering Circle                       withdrawn
```

1. **Open an issue** with the *Change request* or *Feasibility concern* form.
   A steward is assigned and the affected sectors are named.
2. **Write a proposal** from [`proposals/0000-template.md`](proposals/0000-template.md)
   in a draft pull request. Every claim about swiyu is verified against the
   current specification and referenced with a commit-pinned link.
3. **Consultation** with the working groups of the affected sectors for at
   least 14 days. The steward summarises the input, including dissent.
4. **Council decision** by the sectoral council(s). Only endorsed change
   requests are merged.
5. **Submission** to the swiyu team by DIDAS as orchestrator, typically in
   [swiyu-admin-ch/community](https://github.com/swiyu-admin-ch/community).
6. **Outcome** recorded in the proposal, the index and the changelog, and
   reported to the Steering Circle.

Time-critical topics can reach swiyu earlier through an authorised **early
notice** that describes the problem only.

- [GOVERNANCE.md](GOVERNANCE.md): ecosystem governance, roles, gates, escalation
- [CONTRIBUTING.md](CONTRIBUTING.md): step-by-step workflow, spec verification, statuses, labels
- [STEWARDS.md](STEWARDS.md): stewards and sectoral councils
- [Changelog](changelog/README.md)

## What belongs here

- Proposed changes to swiyu specifications, profiles, APIs or trust frameworks
- Ecosystem feasibility concerns: things that are hard, costly or impossible to
  implement or operate as currently specified
- Gaps or ambiguities in the swiyu documentation that block implementation

Not here:

- Bugs in a single swiyu component: report them in that component's
  repository, e.g. [swiyu-issuer](https://github.com/swiyu-admin-ch/swiyu-issuer)
  or [swiyu-verifier](https://github.com/swiyu-admin-ch/swiyu-verifier)
- Security vulnerabilities: follow the swiyu responsible disclosure process,
  never post them publicly

## Related DIDAS repositories

- [DIDAS Glossary](https://didas-swiss.github.io/didas-glossary/): the common vocabulary
- [Use Case Repository](https://didas-swiss.github.io/use-case-repository/): the use cases that run into the problems raised here
- [Trust Flow Diagram Repository](https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository): the trust flows that show where swiyu falls short

## Licence

[MIT](LICENSE)
