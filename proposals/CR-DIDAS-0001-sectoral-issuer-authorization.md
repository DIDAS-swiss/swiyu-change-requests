---
title: "CR-DIDAS-0001: Non-governmental sector bodies cannot decide which issuers may issue their credential types"
cr: CR-DIDAS-0001
status: Draft
aspects: [governance, law, costs, infrastructure]
sectors: [cross-sector]
steward: TBD
updated: 2026-11-22
---

# CR-DIDAS-0001: Non-governmental sector bodies cannot decide which issuers may issue their credential types

| Field | Value |
| --- | --- |
| Authors | Daniel Säuberli (DIDAS) |
| Created | 2026-11-10, revised 2026-11-22 |
| Primary aspect | Governance and trust framework |
| Secondary aspects | Law and ordinances; costs for actors; infrastructure |
| Sectors affected | Cross-sector |
| Discussion | [Issue 1](https://github.com/DIDAS-swiss/swiyu-change-requests/issues/1) |
| Upstream | none yet |

## Governance

| Item | Value |
| --- | --- |
| Steward | TBD, DIDAS provisional (see [STEWARDS.md](../STEWARDS.md)) |
| Working groups consulted | TBD |
| Consultation period | TBD |
| Councils | TBD |
| Council decisions | pending |
| Cross-sector consolidation | pending |
| Steering Circle | To be informed: who governs a sector within swiyu is a strategic question. |
| Early notice | Requested, because the trust specifications are still drafts. |

## Summary

For credential types that only authorised issuers may issue, swiyu provides a
single body that grants the authorisation: the federal trust statement issuer.
Some credential types are governed outside government, by associations,
self-regulatory organisations (SROs) or industry schemes that decide which
organisations may issue them. These bodies cannot take that decision within
swiyu. We ask swiyu to give non-governmental sector bodies a defined role in
the trust framework, so that they can grant and withdraw these authorisations
themselves within a scope set by the federal authorities.

## Problem

Facts, with sources listed below:

- Trust Protocol 2.0 lets a credential type be declared protected. An issuer of
  a protected type must hold an authorisation statement and both the list of
  protected types and the authorisations are issued by the trust statement
  issuer named in the Swiss Profile Trust
  ([Trust Protocol, L67-L73][tp-protected], [L706-L741][tp-piats]). The
  specification describes the authorisation as "proof of state authorization"
  ([L708][tp-piats]).
- The Swiss Profile Trust names one trust statement issuer
  ([L61-L66][spt-anchors]).
- The swiyu wallet and the generic verifier accept these statements from one
  configured signer only ([wallet][wallet], [verifier][verifier-props]).
- The specification and the profile contain no role or mechanism through which
  another body could grant authorisations for a defined set of credential
  types.
- A credential type is either on the federal list of protected types or not
  protected at all ([L67-L73][tp-protected]).

Assessment: where an association or a self-regulatory organisation decides
which organisations may issue a credential type, swiyu leaves it two options.
It can ask the federal operator to declare the type protected and to issue and
withdraw each authorisation on its behalf, relying on information the operator
does not hold. Or the type stays unprotected and the body has no say within
swiyu. Since the specification describes the authorisation as proof of state
authorisation, it is open whether the federal trust statement issuer would
issue it for a credential type that is not a state matter.

Example: a student credential confirming enrolment at a higher education
institution. Whether an organisation may issue it is a question for the
education sector, for example for bodies such as swissuniversities or educa.
Whether these bodies would take such a role has not been discussed with them.
Under the current specifications there are two options. Either
the federal trust statement issuer declares the credential type protected and
authorises each institution itself, or the type stays unprotected and any
issuer can issue a credential of that type. The sector has no way to decide
within swiyu which institutions may issue it.

## Who is affected

Associations, self-regulatory organisations and scheme operators cannot
exercise their responsibility within swiyu. Issuers have no authorisation path through the body responsible
for them. Verifiers that need to know which issuers a sector recognises
maintain their own lists of accepted issuers; the generic verifier provides a
per-verification list for this purpose ([verifier][verifier-dto]). Holders cannot
see which body authorised an issuer. The federal operator carries
decisions that belong to other bodies.

## Evidence

None linked yet. Use cases, trust flows or deployments that show the problem
are collected during the consultation.

## Requested outcome

A non-governmental sector body, such as an association or a self-regulatory
organisation, can grant and withdraw the authorisation to issue the credential
types it governs within swiyu. The federal authorities define which bodies take
this role and for which credential types. Wallets and verifiers can tell which
body authorised an issuer.

## Where the change may land

Assessment, for the swiyu team to decide:

- Trust framework and governance: which bodies may take the role, on what
  basis and how disputes and appeals are handled.
- Specifications: Trust Protocol and Swiss Profile Trust.
- Infrastructure and reference components: trust registry, wallet, generic
  verifier. Both the wallet and the verifier currently pin a single signer.
- Ordinance or law: whether the E-ID Act and its ordinances allow the federal
  authorities to delegate this role to private-law bodies. This has not been
  checked.

## Trade-offs and open questions

- A single federal signer is easier to operate and audit. More signing bodies
  increase the attack surface and the coordination effort.
- Overlapping responsibilities, for example between competing associations in
  one sector, have to be resolved before a credential type can be assigned to
  one body.
- Open: which non-governmental bodies qualify and on what basis, for example
  their statutes or recognition by an authority; whether the same applies to the authorisation to verify
  protected data; how withdrawal reaches issuers and verifiers in time; which
  appeal path an issuer has when an authorisation is refused or withdrawn.

## Sources

Checked on 2026-11-22.

| Document or component | Version and status as stated | Commit checked | Date checked |
| --- | --- | --- | --- |
| [Trust Protocol](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/403ddf2ba49b0bbdb537044a9898246217d4b207/_specifications/trust-protocol-v2-0.md) | 2.0, draft, last edited 2026-10-30 | `403ddf2` | 2026-11-22 |
| [Swiss Profile Trust](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/403ddf2ba49b0bbdb537044a9898246217d4b207/_specifications/swiss-profile-trust.md) | 1.0, draft, last edited 2026-10-26 | `403ddf2` | 2026-11-22 |
| [swiyu Android wallet](https://github.com/swiyu-admin-ch/eidch-android-wallet/tree/c29a6f3af51f14c47cf23ab88933522ffa1fbef0) | main | `c29a6f3` | 2026-11-22 |
| [swiyu generic verifier](https://github.com/swiyu-admin-ch/swiyu-verifier/tree/5e1fd27fa9ee037169e7449bd01bfe5ac6944725) | main | `5e1fd27` | 2026-11-22 |

## Community input

Pending.

| Working group, council or participant | Position | Main points |
| --- | --- | --- |
| | | |

## Outcome

Pending.

[tp-protected]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/403ddf2ba49b0bbdb537044a9898246217d4b207/_specifications/trust-protocol-v2-0.md#L67-L73
[tp-piats]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/403ddf2ba49b0bbdb537044a9898246217d4b207/_specifications/trust-protocol-v2-0.md#L706-L741
[spt-anchors]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/403ddf2ba49b0bbdb537044a9898246217d4b207/_specifications/swiss-profile-trust.md#L61-L66
[wallet]: https://github.com/swiyu-admin-ch/eidch-android-wallet/blob/c29a6f3af51f14c47cf23ab88933522ffa1fbef0/app/src/main/java/ch/admin/foitt/wallet/platform/environmentSetup/data/MainEnvironmentSetupRepositoryImpl.kt#L68-L100
[verifier-props]: https://github.com/swiyu-admin-ch/swiyu-verifier/blob/5e1fd27fa9ee037169e7449bd01bfe5ac6944725/verifier-service/src/main/java/ch/admin/bj/swiyu/verifier/common/config/TrustRegistryProperties.java#L24-L27
[verifier-dto]: https://github.com/swiyu-admin-ch/swiyu-verifier/blob/5e1fd27fa9ee037169e7449bd01bfe5ac6944725/verifier-service/src/main/java/ch/admin/bj/swiyu/verifier/dto/management/CreateVerificationManagementDto.java#L21-L30
