---
title: "CR-DIDAS-0001: Sectoral authorities cannot decide which issuers may issue their credential types"
cr: CR-DIDAS-0001
status: Draft
aspects: [governance, law, costs, infrastructure]
sectors: [cross-sector, health]
steward: TBD
updated: 2026-11-22
---

# CR-DIDAS-0001: Sectoral authorities cannot decide which issuers may issue their credential types

| Field | Value |
| --- | --- |
| Authors | Daniel Säuberli (DIDAS) |
| Created | 2026-11-10, revised 2026-11-22 |
| Primary aspect | Governance and trust framework |
| Secondary aspects | Law and ordinances; costs for actors; infrastructure |
| Sectors affected | Cross-sector. First evidence from health. |
| Discussion | [Issue 1](https://github.com/DIDAS-swiss/swiyu-change-requests/issues/1) |
| Upstream | none yet |

## Governance

| Item | Value |
| --- | --- |
| Steward | TBD, DIDAS provisional (see [STEWARDS.md](../STEWARDS.md)) |
| Working groups consulted | TBD. Health at least; all working groups if the change request is treated as cross-sector. |
| Consultation period | TBD |
| Councils | TBD |
| Council decisions | pending |
| Cross-sector consolidation | pending |
| Steering Circle | To be informed: who governs a sector within swiyu is a strategic question. |
| Early notice | Requested, because the trust specifications are still drafts. |

## Summary

For credential types that only authorised issuers may issue, swiyu provides a
single body that grants the authorisation: the federal trust statement issuer.
Bodies responsible for a sector, such as cantonal health authorities,
professional associations or industry schemes, cannot decide within swiyu
which issuers are authorised for the credential types of their sector. We ask
swiyu to give such bodies a defined role in the trust framework, so that they
can grant and withdraw these authorisations themselves within a scope set by
the federal authorities.

## Problem

Facts, with sources listed below:

- Trust Protocol 2.0 lets a credential type be declared protected. An issuer of
  a protected type must hold an authorisation statement, and both the list of
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

Assessment: whether a health professional may practise is decided by cantonal
authorities, and the health trust flow F-01 expects authorisations to be
checked against such registers. In swiyu, the federal operator would have to issue and
withdraw these authorisations on their behalf, relying on information it does
not hold. For credential types that are not state matters, swiyu has no way to
express that a sector body governs them.

## Who is affected

Sectoral authorities and scheme operators cannot exercise their responsibility
within swiyu. Issuers have no authorisation path through the body responsible
for them. Verifiers that need to know which issuers a sector recognises
maintain their own lists of accepted issuers; the generic verifier provides a
per-verification list for this purpose ([verifier][verifier-dto]). Holders cannot
see which body authorised an issuer. The federal operator carries
decisions that belong to other bodies.

## Evidence

| Kind | Link | What it shows |
| --- | --- | --- |
| Trust flow | [Health F-01: Becoming an actor in the health trust domain][tf-f01] | Organisation, identity and transparency can be set up today. The authorisation to issue health credential types cannot, because no health-domain body exists in swiyu to grant it. The pilot uses a fixed list of accepted issuers, which the flow judges not to scale beyond a pilot. |
| Credential | [Immunization record][uc-immunization] | No body grants the vaccinator role on the trust infrastructure. |
| Use case | [Vaccination record](https://github.com/DIDAS-swiss/use-case-repository/issues/122) | Depends on the immunization record. |

## Requested outcome

A body responsible for a sector can grant and withdraw the authorisation to
issue the credential types of that sector within swiyu. The federal
authorities define which bodies take this role and for which credential types.
Wallets and verifiers can tell which body authorised an issuer. Credential types
that are not state matters can also be placed under a sector body.

## Where the change may land

Assessment, for the swiyu team to decide:

- Trust framework and governance: which bodies may take the role, on what
  basis, and how disputes and appeals are handled.
- Specifications: Trust Protocol and Swiss Profile Trust.
- Infrastructure and reference components: trust registry, wallet, generic
  verifier. Both the wallet and the verifier currently pin a single signer.
- Ordinance or law: whether the E-ID Act and its ordinances allow the federal
  authorities to delegate this role. This has not been checked.

## Trade-offs and open questions

- A single federal signer is easier to operate and audit. More signing bodies
  increase the attack surface and the coordination effort.
- Overlapping responsibilities between bodies, or between cantons, have to be
  resolved before a credential type can be assigned to one body.
- Open: whether private-law schemes can take the role or only public
  authorities; whether the same applies to the authorisation to verify
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
| [Trust Flow Diagram Repository, health F-01](https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository/tree/6c11036ca35039739849a0349121317c756a1752) | status `partial` | `6c11036` | 2026-11-10 |
| [Use Case Repository, immunization record](https://github.com/DIDAS-swiss/use-case-repository/tree/86273c6642144f9ca204ce7ecfb78a66e4dd3f63) | stage `signal` | `86273c6` | 2026-11-10 |

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
[tf-f01]: https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository/blob/6c11036ca35039739849a0349121317c756a1752/health/flows/F-01-actor-onboarding.md
[uc-immunization]: https://github.com/DIDAS-swiss/use-case-repository/blob/86273c6642144f9ca204ce7ecfb78a66e4dd3f63/credentials/immunization-record.md#L30-L36
