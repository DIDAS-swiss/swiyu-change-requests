# swiyu Change Requests

**Website: <https://didas-swiss.github.io/swiyu-change-requests/>**

Status: proposal. The process, the governance, the aspects and the templates
in this repository are a DIDAS proposal for discussion with the stewards,
working groups and councils, and with the swiyu ecosystem governance.

DIDAS collects here the obstacles that keep actors from using swiyu, the Swiss
e-ID trust infrastructure, and submits them to the swiyu team as change
requests. DIDAS acts as swiyu orchestrator; the specifications and reference
components of swiyu are maintained by the Federal Administration in
[swiyu-admin-ch](https://github.com/swiyu-admin-ch).

A change request is the input to a pipeline. It describes the obstacle, the
actors affected and the outcome they need, and stays at a high level. It
typically does not prescribe a technical solution: the swiyu team decides whether a specification, a component, the
infrastructure, an ordinance or a later revision of the law is the right place
to respond. Each change request is assigned to one or more [aspects](ASPECTS.md),
for example costs for actors, constraints of use, technological or
organisational hurdles, governance, defects, infrastructure or law.

<p class="gh-only"><a href="https://github.com/DIDAS-swiss/swiyu-change-requests/issues/new?template=change-request.yml"><b>+ Raise a change request</b></a> · <a href="https://didas-swiss.github.io/swiyu-change-requests/">Open the website</a></p>

## Change requests

| CR | Title | Aspects | Sectors | Status |
| --- | --- | --- | --- | --- |
| none yet | | | | |

The [index](proposals/README.md) also lists stewards and upstream links.

## Process

A steward guides each change request. The working groups of the affected
sectors are consulted for at least 14 days, and the sectoral councils decide.
DIDAS consolidates positions across sectors, submits endorsed change requests
to the swiyu team and reports to the swiyu Steering Circle, which decides on
conflicts and strategic questions.

```
Issue ──► Draft ──► Consultation ──► Council decision ──► Submitted ──► Outcome
```

Statements about swiyu in a change request are checked against the current
specification and referenced with commit-pinned links. A topic that has to
reach swiyu before the process is complete can be sent as an early notice that
describes the problem only.

- [ASPECTS.md](ASPECTS.md): the aspects of a change request
- [GOVERNANCE.md](GOVERNANCE.md): roles, decisions, escalation
- [CONTRIBUTING.md](CONTRIBUTING.md): workflow, verification, statuses, labels
- [STEWARDS.md](STEWARDS.md): stewards and sectoral councils
- [Changelog](changelog/README.md)

Defects in a single swiyu component that need no consultation go to that
component's repository in [swiyu-admin-ch](https://github.com/swiyu-admin-ch).
Security vulnerabilities follow the swiyu responsible disclosure process and are
never posted here.

## Related DIDAS repositories

- [DIDAS Glossary](https://didas-swiss.github.io/didas-glossary/): vocabulary
- [Use Case Repository](https://didas-swiss.github.io/use-case-repository/): use cases
- [Trust Flow Diagram Repository](https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository): trust flows

## Licence

[MIT](LICENSE)
