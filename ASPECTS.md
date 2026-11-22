# Aspects of a change request

Status: proposal for discussion with the stewards, working groups and councils.

A DIDAS change request is the first step of a pipeline. It names an obstacle
that keeps actors from using swiyu, shows who runs into it and what should
become possible. How swiyu removes the obstacle is for the swiyu team to decide:
in a specification, a reference component, the infrastructure, its operation,
an ordinance or a later revision of the law. A change request therefore stays
at the level of the need and the expected result. It typically does not
propose code, data formats or API changes.

Each change request names one primary aspect and any secondary ones. The
aspects sort the requests for the consultation, show the swiyu team which kind
of change is asked for, and let DIDAS report to the Steering Circle where the
obstacles concentrate.

## The aspects

| Aspect | Label | Covers | Typical question |
| --- | --- | --- | --- |
| Costs for actors | `aspect: costs` | Fees, integration and operating effort, effort caused by manual processes, duplicated effort across actors | Which actor pays or works for what, and does that keep actors out? |
| Constraints of use | `aspect: constraints` | Rules and technical limits on how swiyu may be used: who may take part, which environments, credential types, identifiers, algorithms or interactions are allowed | Which legitimate use case is excluded by a rule or limit? |
| Technological hurdles | `aspect: tech-hurdles` | Implementation is hard or impossible for some actors: missing libraries or platforms, complexity, dependencies on specific components | What blocks an actor from building on swiyu with reasonable effort? |
| Organisational hurdles | `aspect: org-hurdles` | Onboarding, manual verification, lead times, support, missing contact points, unclear responsibilities | Which process step stops or delays actors? |
| Governance and trust framework | `aspect: governance` | Who decides about participation, roles, authorisations and withdrawal; how sectors take part in these decisions | Who is responsible for a decision, and can that body take it within swiyu? |
| Technological improvements | `aspect: tech-improvement` | Capabilities swiyu lacks that the ecosystem needs, such as new interaction patterns or credential features | What can actors not do today that they need for a use case? |
| Defects | `aspect: defects` | Errors and contradictions in specifications or reference components that affect several actors | Which defect makes implementations diverge or fail? |
| Infrastructure | `aspect: infrastructure` | Base registry, trust registry, status lists, environments, availability, operation | Which property of the infrastructure limits use, scale or reliability? |
| Law and ordinances | `aspect: law` | Provisions in the E-ID Act (BGEID) and its ordinances that constrain the ecosystem, collected for later revisions | Which legal provision stands in the way, and is that intended? |
| Interoperability | `aspect: interoperability` | Alignment with international standards and other ecosystems, in particular the EU Digital Identity framework | Where does swiyu diverge in a way that blocks cross-border or cross-ecosystem use? |
| Documentation | `aspect: documentation` | Gaps, ambiguities and contradictions in the swiyu documentation | Where can actors not tell from the documentation how swiyu behaves? |

## Delimitation

Some aspects overlap. A missing authorisation mechanism is a governance
question, but it also causes costs and may need a legal basis. The primary
aspect is the one the requested result addresses; the others are secondary.

Defects and documentation gaps that affect a single component and need no
consultation belong in the issue tracker of that component in
[swiyu-admin-ch](https://github.com/swiyu-admin-ch). They become a change
request when several actors are affected or the correct behaviour is disputed.

Security vulnerabilities are never raised here. They follow the swiyu
responsible disclosure process.

## Open points for the consultation

- Whether the list is complete. Candidates that are not listed: privacy and
  data minimisation, accessibility for holders, and market concentration
  around single wallets or vendors. They may fit under existing aspects or
  need their own.
- Whether `law` should collect provisions continuously, independent of
  individual change requests, so that DIDAS has a consolidated list ready
  when the E-ID Act or its ordinances are revised.
- How DIDAS weighs change requests across aspects when it reports to the
  Steering Circle.
