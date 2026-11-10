---
title: "CR-DIDAS-0001: Sectoral governing authorities managing authorized issuers per credential type"
cr: CR-DIDAS-0001
status: Draft
sectors: [cross-sector, health]
steward: TBD
updated: 2026-11-10
---

# CR-DIDAS-0001: Sectoral governing authorities managing authorized issuers per credential type

| Field | Value |
| --- | --- |
| Authors | Daniel Säuberli (DIDAS) |
| Created | 2026-11-10 |
| Area | trust |
| Sectors affected | Cross-sector: every sector with credential types that a sectoral body should govern. First evidence from health. |
| Affected swiyu artefacts | Trust Protocol 2.0 (protected issuance, piaTS, piTLS, trust registry API); swiss-profile-trust 1.0 (root trust anchors); swiyu-registry-trust-data-service; swiyu Wallet; swiyu-verifier. See [Sources](#sources). |
| Discussion | [Issue 1](https://github.com/DIDAS-swiss/swiyu-change-requests/issues/1) |
| Upstream | — |

## Governance

| Item | Value |
| --- | --- |
| Steward | TBD (DIDAS provisional, see [STEWARDS.md](../STEWARDS.md)) |
| Working group(s) consulted | TBD; at least Health. Proposed: all sectoral working groups, as the change is cross-sector. |
| Consultation period | TBD |
| Council(s) | TBD |
| Council decision(s) | pending |
| Cross-sector consolidation | pending, by DIDAS as orchestrator |
| Steering Circle | Proposed: inform, since the question who governs a sector is strategic for the ecosystem. |
| Early notice | Requested. Trust Protocol 2.0 and swiss-profile-trust 1.0 are both still drafts, so the problem should reach swiyu while the trust model can still change. |

## Summary

In swiyu today, one federal trust statement issuer decides which issuers are
authorized for which credential types. Sectoral governing authorities, such as
cantonal or federal authorities, professional bodies or industry schemes, have
no technical means to maintain the list of issuers authorized for the credential
types they are responsible for. The wallet and the generic verifier are
configured with exactly one trusted signer for these statements, so no other
body can take on this role without a change to swiyu. We ask swiyu to give
governing authorities a scoped, auditable way to manage authorized issuers for
their credential types, so that governance sits where the legal and domain
responsibility lies.

## Problem

All references are listed with versions and commits under [Sources](#sources).

### 1. Only one signer can authorize issuers

Trust Protocol 2.0 describes trust statements as statements that "require a
manual verification process by a governing body" and trust list statements as
"actively managed by a governing body" ([TP L26–L31][tp-types]).

For issuance, a credential type is protected "if and only if its `vct` claim is
listed in the `vct_values` claim of an active Protected Issuance Trust List
Statement" (piTLS), and an issuer of such a credential **MUST** have a Protected
Issuance Authorization Trust Statement (piaTS) ([TP L67–L73][tp-protected]).
Both statement types **MUST** be issued by "an trust statement issuer
identified in the swiss-profile-trust" ([TP L706–L741][tp-piats]). The piaTS is
described as the issuer's "proof of state authorization to issue protected VCs"
([TP L708][tp-piats]).

[swiss-profile-trust 1.0][spt-anchors] lists exactly one root trust anchor of
type *Trust statement issuer* (L61–L66).

The reference implementations confirm this:

- The **swiyu Android wallet** accepts each statement type, including piTLS
  and piaTS, only from one hard-coded DID per environment
  ([wallet L68–L69, L83–L100][wallet-dids]). A new signer needs a new app
  release.
- The **swiyu generic verifier** takes a single `trustIssuerDid`, "the DID
  trusted to issue Trust Statements" ([verifier properties L24–L27][verifier-props]),
  and checks issuers against it ([validator L99–L102][verifier-validator]).

There is no statement type, claim or registry API through which that signer can
delegate authority over a set of credential types to another body.

### 2. Every change goes through the federal operator

Because only one signer exists, every addition, renewal or withdrawal of an
issuer's authorization for any protected credential type is an act of the
federal trust statement issuer. The trust registry renews statements
automatically, and that renewal can be terminated when an issuer or verifier is
no longer eligible ([swiss-profile-trust L89–L93][spt-validity]). Whether an issuer is still
eligible, however, is decided by the sector (for example a withdrawn
authorisation to practise), so the federal operator has to rely on information
it does not hold.

### 3. Protection is all or nothing

A credential type is either on the federal piTLS or not protected at all
([TP L67–L73][tp-protected]). There is no state for "governed by sectoral
authority X" for credential types that are not state matters but still need a
body that says who may issue them, such as professional qualifications,
diplomas or scheme memberships.

### 4. Authorizations cannot be looked up by credential type

The trust registry lists piaTS with paging and an active filter
([TP L512–L543][tp-registry]) and fetches a single piaTS by `jti`
([TP L434–L503][tp-registry-jti]). The registry
implementation additionally supports a `sub` filter, which the spec does not
document ([registry L200–L223][registry-pias]). Neither offers a filter by
`vct`: a governing authority, verifier or auditor cannot ask "which issuers are
currently authorized for this credential type?".

### 5. Who authorized an issuer is not stated

A piaTS carries `can_issue.vct`, `vct_name` and an optional free-text `reason`
([TP L718–L726][tp-piats-object]), but no claim for the responsible governing
authority or its legal basis. A wallet or verifier cannot show who stands
behind an issuer's authorization.

### The workaround does not scale

Without an authorization, deployments fall back to listing trusted issuers per
verification: the generic verifier accepts `accepted_issuer_dids`, "dids from
issuers whose credentials are accepted for this verification"
([verifier DTO L21–L30][verifier-dto]). Every verifier then maintains its own
allow-list for every sector, which is the fragmentation a trust infrastructure
is meant to avoid.

## Ecosystem impact

- [x] **Issuers**: depend on a central process to be authorized; no contact
  point in their own sector.
- [x] **Verifiers / relying parties**: cannot rely on swiyu to tell them which
  issuers a sector recognises; maintain their own `accepted_issuer_dids`.
- [x] **Wallet providers**: cannot show the user which authority stands behind
  an issuer's authorization.
- [x] **Holders**: weaker protection against look-alike credentials outside the
  federally protected types.
- [x] **Integrators / solution vendors**: build per-sector allow-lists outside
  swiyu.
- [x] **Governing authorities**: cannot exercise their legal or scheme
  responsibility technically within swiyu.
- [x] **Trust infrastructure operators**: the federal operator carries the
  operational burden of sector decisions.

## Evidence from use cases and trust flows

| Kind | Link | How it is affected |
| --- | --- | --- |
| Trust flow | [Health F-01: Becoming an actor in the health trust domain][tf-f01] (status `partial`) | Of the four onboarding layers, only *entitlement*, an authorisation statement that a DID may issue a given credential type in health, is unavailable, because "no health-domain governing authority exists to publish it". The pilot runs on explicitly listed `accepted_issuer_dids`, "which does not scale past a pilot". Tracked as [Trust-Flow-Diagram-Repository issue 3](https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository/issues/3). |
| Credential | [Immunization record][uc-immunization] (stage `signal`) | "No governing authority yet grants the vaccinator role on the trust infrastructure." |
| Use case | [Vaccination record candidate](https://github.com/DIDAS-swiss/use-case-repository/issues/122) | Needs the immunization record above. |

F-01 also sets requirements that any solution must meet: authorization
decisions must be checkable against existing registers (cantonal authorisation
to practise, MedReg, GLN, BAG number), issuing and verifying authorizations stay
separate (piaTS vs pvaTS), and withdrawal must propagate to the published
statement ([F-01 L104–L144][tf-f01-constraints]).

## Proposed change

We ask swiyu to support **scoped delegation of issuer authorization to
governing authorities**. These building blocks are for the consultation to
weigh; it should decide which to recommend.

### A. Governing authority role and scope

Define a *governing authority* in swiss-profile-trust. The root trust statement
issuer publishes a new statement for the authority's DID (draft name
**Governing Authority Delegation Trust Statement**) with:

- `sub`: the authority's DID;
- `governed_vct_values`: the credential types, or a `vct` namespace, the
  authority governs;
- `legal_basis` (optional, localizable): the law, ordinance or scheme rules
  that give the authority its role;
- `status` and `exp`, as for other trust statements, so delegation can be
  revoked.

### B. Authorizations published by the governing authority

Allow a piaTS, or an equivalent new statement, to be signed by a governing
authority when its `can_issue.vct` falls within the authority's delegated
scope. Wallets and verifiers then validate a chain of fixed length:

```
Root trust statement issuer ──delegation──► Governing authority ──authorization──► Issuer
```

Add an `authorized_by` claim (authority DID and display name) so that wallets
and verifiers can show who authorized the issuer.

### C. Governed credential types

Allow the trust list to mark a `vct` as governed by a named authority,
separately from the federal protected list. For an issuer of a governed `vct`,
the same rule as for protected types applies: without a valid authorization
from that type's authority, the governed use case authorization marker cannot
be derived, and the actor declines
([swiss-profile-trust L78][spt-requirements]).

### D. Registry support

- A management interface, or onboarding process, through which governing
  authorities publish, renew and withdraw their authorizations.
- Documented query parameters for authorizations by credential type and by
  issuer, for example
  `GET /api/v2/protected-issuance-authorization-trust-statement/?vct=<vct>` and
  `?sub=<issuer DID>`. The `sub` filter already exists in the implementation
  and only needs to be specified.

### Possible phasing

1. **Short term, no wallet change:** governing authorities manage
   authorizations through the registry while the root still signs; specify
   `sub` and add `vct` queries; name the authority in `reason` until a claim
   exists.
2. **Medium term:** delegation statement and authority-signed authorizations
   (A, B), validated by wallets and verifiers. Requires a wallet and verifier
   release, since both pin a single signer today.
3. **Then:** governed credential types (C).

## Alternatives considered

- **Do nothing: the federal operator acts for all sectors.** Keeps one trust
  anchor, but makes the federal operator responsible for sector decisions it
  cannot check itself, and does not scale.
- **Each sector keeps its own allow-list outside swiyu**, or every verifier
  uses `accepted_issuer_dids`. Works today, but fragments the ecosystem and
  gives holders no consistent signal.
- **Several root trust anchors**, one per authority, in swiss-profile-trust.
  Simpler validation, but without scope: any root could authorize any `vct`,
  and every new authority needs a profile change and an app release.
- **OpenID Federation trust marks.** A close conceptual fit (trust mark owners
  and issuers delegated by a trust anchor), but a larger departure from Trust
  Protocol 2.0. Worth considering for the long term.

## Drawbacks and risks

- **More complex validation** for wallets and verifiers; mitigated by a fixed
  chain length of two.
- **Key management at governing authorities**: they need secure key handling
  and withdrawal processes, which onboarding must require.
- **Overlapping scopes**: two authorities claiming the same `vct`; delegation
  must prevent overlaps.
- **Privacy**: no holder data is involved; registry queries concern issuers
  only.

## Alignment with standards

- **OpenID Federation 1.0**: trust anchors, trust mark owners and trust mark
  issuers model the same delegation.
- **EBSI Trusted Issuers Registry**: hierarchical accreditation scoped to
  credential types.
- **eIDAS 2.0 / EUDI Architecture and Reference Framework**: attestation
  providers registered for specific attestation types; trusted lists. A scoped
  model in swiyu eases later mutual recognition.
- **ETSI TS 119 612** trusted lists: per-scheme operators and service types.

## Migration and backwards compatibility

- Existing piTLS and piaTS issued by the root remain valid.
- Phase 1 changes the registry and its API only.
- Phases 2 and 3 add statement types and claims under a new `profile_version`,
  introduced Expand–Migrate–Contract as swiyu did for Trust Protocol 2.0
  ([CD-006][cd-006]).

## Sources

Checked on 2026-11-10.

| Document / component | Version and status (as stated) | Commit checked |
| --- | --- | --- |
| [Trust Protocol](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/trust-protocol-v2-0.md) | 2.0, "draft - content is under review and may still change", last edited 2026-10-30 | `01d9824` |
| [swiss-profile-trust](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/swiss-profile-trust.md) | 1.0, "draft - technically complete, but might to be reformulated", last edited 2026-10-26 | `01d9824` |
| [CD-006 Trust Protocol 2.0](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_change-dossiers/CD-006-Trust-Protocol-2.0.md) | Released, effective 19.08.2026 | `01d9824` |
| [swiyu-registry-trust-data-service](https://github.com/swiyu-admin-ch/swiyu-registry-trust-data-service/tree/a34aef41909f87d627d5f41c12abd4edb9d87b96) | main | `a34aef4` |
| [eidch-android-wallet](https://github.com/swiyu-admin-ch/eidch-android-wallet/tree/c29a6f3af51f14c47cf23ab88933522ffa1fbef0) | main | `c29a6f3` |
| [swiyu-verifier](https://github.com/swiyu-admin-ch/swiyu-verifier/tree/0bf4cdc149ef7e0651c1ee82b1f5b2ce35518496) | main | `0bf4cdc` |
| [Trust Flow Diagram Repository](https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository/tree/6c11036ca35039739849a0349121317c756a1752), health F-01 | status `partial` | `6c11036` |
| [Use Case Repository](https://github.com/DIDAS-swiss/use-case-repository/tree/86273c6642144f9ca204ce7ecfb78a66e4dd3f63), immunization record | stage `signal` | `86273c6` |

Discrepancies found:

- **Registry query parameters**: the spec's piaTS list endpoint documents only
  `filterActive`, `page` and `size` ([TP L512–L543][tp-registry]); the
  implementation also accepts `sub` ([registry L216–L217][registry-pias]).
- **Endpoint headings**: in Trust Protocol 2.0 the endpoint tables under
  *Retrieving Protected Issuance Authorization Trust Statements* (L434) and
  *Retrieving Protected Issuance Trust List Statements* (L504) list each
  other's list endpoints.
- **Root anchors are given for one environment**: the trust statement issuer
  listed in swiss-profile-trust is on `swiyu-int`
  ([L61–L66][spt-anchors]); the wallet pins a different DID for production
  ([wallet L68–L69][wallet-dids]). Both are single signers.
- **Production date**: swiyu's documentation states both 2026
  ([roadmap](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_pages/roadmap.md#L10))
  and 2027
  ([open source components](https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_pages/open-source-components.md#L10))
  for the production go-live. This proposal does not depend on either date.

## Open questions

- Which bodies qualify as governing authorities, and who decides: a legal
  basis, a recognised scheme, or both? Raised for health in
  [F-01, open question 1][tf-f01].
- Should delegation be scoped by exact `vct` values, by namespace, or both?
- Should the same mechanism cover protected **verification** (pvaTS), so that
  sectors also govern who may request their credentials?
- Should governing authorities be able to flag non-compliant actors in their
  sector (ncTLS)?
- Will the root delegate to private-law schemes, or only to public authorities?
- What is the appeal path when an authorization is refused or withdrawn
  ([F-01, open question 3][tf-f01])?

## Community input

Pending consultation.

| Working group / council / participant | Position | Main points |
| --- | --- | --- |
| | | |

## Outcome

Pending.

[tp-types]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/trust-protocol-v2-0.md#L26-L31
[tp-protected]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/trust-protocol-v2-0.md#L67-L73
[tp-registry]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/trust-protocol-v2-0.md#L512-L543
[tp-registry-jti]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/trust-protocol-v2-0.md#L434-L503
[tp-piats-object]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/trust-protocol-v2-0.md#L718-L726
[tp-piats]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/trust-protocol-v2-0.md#L706-L741
[spt-anchors]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/swiss-profile-trust.md#L61-L66
[spt-requirements]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/swiss-profile-trust.md#L78
[spt-validity]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_specifications/swiss-profile-trust.md#L89-L93
[cd-006]: https://github.com/swiyu-admin-ch/swiyu-admin-ch.github.io/blob/01d9824ef29217d9a4dbfba5bb89556a54404b14/_change-dossiers/CD-006-Trust-Protocol-2.0.md
[registry-pias]: https://github.com/swiyu-admin-ch/swiyu-registry-trust-data-service/blob/a34aef41909f87d627d5f41c12abd4edb9d87b96/src/main/java/ch/admin/bj/swiyu/registry/trust/data/infrastructure/web/controller/StatementV2Controller.java#L200-L223
[wallet-dids]: https://github.com/swiyu-admin-ch/eidch-android-wallet/blob/c29a6f3af51f14c47cf23ab88933522ffa1fbef0/app/src/main/java/ch/admin/foitt/wallet/platform/environmentSetup/data/MainEnvironmentSetupRepositoryImpl.kt#L68-L100
[verifier-props]: https://github.com/swiyu-admin-ch/swiyu-verifier/blob/0bf4cdc149ef7e0651c1ee82b1f5b2ce35518496/verifier-service/src/main/java/ch/admin/bj/swiyu/verifier/common/config/TrustRegistryProperties.java#L24-L27
[verifier-validator]: https://github.com/swiyu-admin-ch/swiyu-verifier/blob/0bf4cdc149ef7e0651c1ee82b1f5b2ce35518496/verifier-service/src/main/java/ch/admin/bj/swiyu/verifier/service/trust/TrustProtocol2Validator.java#L99-L102
[verifier-dto]: https://github.com/swiyu-admin-ch/swiyu-verifier/blob/0bf4cdc149ef7e0651c1ee82b1f5b2ce35518496/verifier-service/src/main/java/ch/admin/bj/swiyu/verifier/dto/management/CreateVerificationManagementDto.java#L21-L30
[tf-f01]: https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository/blob/6c11036ca35039739849a0349121317c756a1752/health/flows/F-01-actor-onboarding.md
[tf-f01-constraints]: https://github.com/DIDAS-swiss/Trust-Flow-Diagram-Repository/blob/6c11036ca35039739849a0349121317c756a1752/health/flows/F-01-actor-onboarding.md#L104-L144
[uc-immunization]: https://github.com/DIDAS-swiss/use-case-repository/blob/86273c6642144f9ca204ce7ecfb78a66e4dd3f63/credentials/immunization-record.md#L30-L36
