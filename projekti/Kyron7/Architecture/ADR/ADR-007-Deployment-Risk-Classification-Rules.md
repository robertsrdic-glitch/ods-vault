# ADR-007: Deployment Risk Classification Rules

**Status:** Accepted
**Date:** 2026-07-18
**Approved:** 2026-07-19 (Founder)

## Context

WP-04 (Policy Engine Classification) requires deterministic rules to classify a candidate deployment as low-risk or high-risk. The Deployment Policy Engine Specification establishes the binary output contract (§4) but explicitly defers the rules themselves: §3 states "individual policy rules are out of scope here," and §7 (Non-Goals) explicitly excludes "defining concrete policy rules or the criteria that make a deployment low-risk or high-risk." No classification criteria existed anywhere in ODS Vault before this ADR.

A first draft of this ADR proposed a single signal (target environment only). CTO review rejected that as insufficient: a staging or development deployment can still be high-risk when it involves database changes, secrets, authentication, infrastructure, destructive operations, unclear rollback, or incomplete metadata. This ADR replaces that draft with a conservative, multi-signal MVP policy.

This is a governance and safety decision, not an implementation detail. WP-04 must implement these rules exactly as defined here. Any future change to the classification policy — adding, removing, or altering a signal or a rule — requires a superseding ADR or another explicitly approved policy decision; it may not be changed silently during implementation.

## Decision

The Policy Engine classifies a candidate deployment using multiple explicit signals evaluated in a fixed precedence order (see Decision Precedence). The output remains strictly binary — low-risk or high-risk — with no score, confidence value, graded level, or third state. Low-risk is permitted only when every required low-risk condition is explicitly satisfied. High-risk is mandatory whenever any high-risk condition is present, or whenever valid deployment metadata is uncertain, incomplete, contradictory, unsupported, or unverifiable. The system never defaults to low-risk.

## Classification Input Model

| Signal | Type / Values | Required signal it covers |
|---|---|---|
| `environment` | `production` \| `staging` \| `development` | target environment |
| `changeType` | `documentation-only` \| `test-only` \| `application-code-only` \| `database-migration` \| `infrastructure` \| `dependency-or-runtime` \| `external-api-contract` \| `other` | change category; supported/unsupported change type; documentation-only; test-only; ordinary application-code-only |
| `touchesDatabaseOrSchema` | boolean | database/schema/data migration impact |
| `touchesSecretsOrCredentials` | boolean | secrets, keys, credentials, or sensitive environment configuration |
| `touchesAuthenticationOrAuthorization` | boolean | authentication or authorization impact |
| `touchesInfrastructure` | boolean | Docker, VPS, networking, reverse-proxy, or production infrastructure impact |
| `includesDestructiveOperation` | boolean | destructive or irreversible operations |
| `touchesDependenciesOrRuntime` | boolean | dependency or runtime changes |
| `touchesExternalApiOrContract` | boolean | externally visible API or contract changes |
| `rollbackAvailable` | boolean | rollback availability |
| `rollbackClear` | boolean | rollback clarity |
| `rollbackVerifiable` | boolean | rollback verifiability |
| `metadataComplete` | boolean | metadata completeness |
| `metadataConsistent` | boolean | metadata consistency |

`changeType = "other"` is a valid, schema-conforming value representing a change that does not fit any recognized category — it is not a validation failure, but it is never eligible for low-risk (see Validation and Uncertainty Handling).

All fourteen signals are required on every classification request. A request missing any signal, or supplying a value outside a signal's defined type/values, fails schema validation (see Decision Precedence, step 1–2) rather than being classified.

## Low-Risk Rules

Low-risk is a conjunctive allow-list. Every one of the following must hold, with no exception:

- `environment` is `staging` or `development` (never `production` — see High-Risk Rules).
- `changeType` is one of `documentation-only`, `test-only`, or `application-code-only`.
- `touchesDatabaseOrSchema` is `false`.
- `touchesSecretsOrCredentials` is `false`.
- `touchesAuthenticationOrAuthorization` is `false`.
- `touchesInfrastructure` is `false`.
- `includesDestructiveOperation` is `false`.
- `touchesDependenciesOrRuntime` is `false`.
- `touchesExternalApiOrContract` is `false`.
- `rollbackAvailable` is `true`.
- `rollbackClear` is `true`.
- `rollbackVerifiable` is `true`.
- `metadataComplete` is `true`.
- `metadataConsistent` is `true`.

If any one condition fails, the candidate is not low-risk. There is no partial or weighted credit.

## High-Risk Rules

At least one of the following, if present, mandates high-risk:

- `environment` is `production`. No safe routine-production exception is defined in this ADR. No approved project governance currently justifies one; inventing one here would not be grounded in anything approved. **All production deployments are high-risk for the MVP, without exception.**
- `touchesDatabaseOrSchema` is `true`.
- `touchesSecretsOrCredentials` is `true`.
- `touchesAuthenticationOrAuthorization` is `true`.
- `touchesInfrastructure` is `true`.
- `includesDestructiveOperation` is `true`.
- `rollbackAvailable` is `false`, `rollbackClear` is `false`, or `rollbackVerifiable` is `false` (rollback absent, unclear, or unverifiable).
- `changeType` is `other` (unsupported change category).
- `metadataComplete` is `false` or `metadataConsistent` is `false` (incomplete, contradictory, or otherwise unverifiable metadata).
- Any candidate that does not satisfy every condition in Low-Risk Rules — i.e., impact outside the explicitly approved low-risk boundary — is high-risk by construction, whether or not a specific rule above was matched. The classification is strictly binary; failing to qualify for low-risk is itself sufficient for high-risk.

## Validation and Uncertainty Handling

Two distinct outcomes exist, and they must not be conflated:

1. **Validation error** — the input does not conform to the Classification Input Model (a required signal is missing, or a value falls outside its defined type/closed set, e.g. an `environment` value that is not `production`/`staging`/`development`). This is not a classification; the Policy Engine must reject the request explicitly, before any classification rule is evaluated.
2. **High-risk classification** — the input conforms to the Classification Input Model (passes validation) but represents an unsupported, incomplete, contradictory, or otherwise unverifiable change (`changeType = "other"`, `metadataComplete = false`, `metadataConsistent = false`). This is a real classification outcome, not an error, and it is always high-risk, never low-risk.

The Policy Engine must never silently default uncertain, incomplete, or unrecognized input to low-risk, and must never silently coerce a validation failure into either classification value.

## Decision Precedence

Classification proceeds in exactly this order:

1. Validate the transport/schema shape of the input against the Classification Input Model.
2. If the schema is malformed or any value is not a valid typed input, fail explicitly with a validation error. Stop — no classification is produced.
3. If the schema is valid but the metadata is incomplete, contradictory, unsupported (`changeType = "other"`), uncertain, or unverifiable, classify high-risk. Stop.
4. If any High-Risk Rule matches, classify high-risk. Stop.
5. Classify low-risk only if every Low-Risk Rule condition is satisfied.
6. Never default to low-risk. If step 5 does not affirmatively hold in full, the result is high-risk.

## Examples

**Low-risk:**
- `environment: staging`, `changeType: documentation-only`, all impact flags `false`, rollback flags all `true`, metadata flags all `true` → low-risk.
- `environment: development`, `changeType: test-only`, all impact flags `false`, rollback flags all `true`, metadata flags all `true` → low-risk.
- `environment: staging`, `changeType: application-code-only`, all impact flags `false`, rollback flags all `true`, metadata flags all `true` → low-risk.

**High-risk:**
- `environment: production`, `changeType: application-code-only`, all impact flags `false`, rollback and metadata all satisfied → high-risk (production is always high-risk for the MVP).
- `environment: staging`, `changeType: database-migration` → high-risk (`touchesDatabaseOrSchema` is necessarily relevant; database-migration is not among the low-risk change types).
- `environment: staging`, `changeType: application-code-only`, `touchesSecretsOrCredentials: true` → high-risk, even though environment and change type would otherwise qualify.
- `environment: development`, `changeType: test-only`, all impact flags `false`, but `rollbackAvailable: false` → high-risk.
- `environment: staging`, `changeType: other` → high-risk (unsupported change type).
- `environment: staging`, `changeType: application-code-only`, all impact flags `false`, rollback flags all `true`, `metadataComplete: false` → high-risk.

**Validation error (not a classification):**
- `environment: "prod"` (not one of the three exact defined values) → validation error.
- A request missing `rollbackVerifiable` entirely → validation error.

## Consequences

- WP-04 implements classification strictly against this policy: the fourteen-signal input model, the conjunctive low-risk allow-list, the mandatory high-risk conditions, and the exact precedence order in this ADR.
- The `CandidateDeployment` contract defined in WP-02 (`deployment-agent/contracts/candidate-deployment.ts`) does not currently carry any of these fourteen signals. WP-04 must extend the Policy Engine's own input model to carry them, without duplicating that model into `deployment-agent/`, per WP-04's architectural boundary. Any resulting adjustment must be clearly reported when WP-04 executes.
- Classification policy is a governance and safety decision. It is not implementation detail, and it is not to be altered, narrowed, or extended by any implementation work package. Any future change — including adding a routine-production exception, adding or removing a signal, or changing a rule — requires a superseding ADR or another explicitly approved policy decision.
- This ADR does not define rollback execution policy, Founder approval workflow, audit trail behavior, or GitHub integration. It defines classification inputs and rules only.

## Alternatives Considered

- **Single-signal classification (environment only):** rejected. This was the first draft of this ADR and was rejected in CTO review — a staging or development deployment can still be high-risk via database, secrets, authentication, infrastructure, destructive-operation, or rollback-quality concerns that a single environment signal cannot detect.
- **Numeric or weighted risk scoring:** rejected. The Policy Engine Specification requires a strictly binary output; a scored or weighted input model risks reintroducing a graded internal risk scale — the exact defect the Repository Reconciliation Report flagged in the old repository's `maxRiskLevel: string`. A conjunctive allow-list with mandatory disqualifying conditions avoids this without sacrificing multi-signal coverage.
- **A broad automatic-production exception (e.g., "documentation-only changes to production are low-risk"):** rejected. No approved project governance currently defines or justifies any such exception. Inventing one here would not be grounded in anything approved, so all production deployments remain high-risk for the MVP without exception.
- **Defaulting incomplete or unsupported metadata to low-risk:** rejected. Explicitly forbidden by this ADR's own uncertainty-handling rule and by WP-04's instructions; uncertainty must resolve to high-risk, never low-risk.
- **Treating unsupported change type as a validation error rather than a high-risk classification:** rejected. `changeType = "other"` is a schema-valid value — the request is well-formed — but represents a change the policy cannot vouch for. Conflating it with a structural validation failure would blur the distinction between "the input is malformed" and "the input is valid but risky," which this ADR keeps separate (see Validation and Uncertainty Handling).
