# ADR-013 — Deployment Lifecycle Outcome Represents Complete Lifecycle

**Status:** Accepted
**Date:** 2026-07-19
**Supersedes:** none
**Related Work Package:** WP-12 (Integration) — realized through WP-12A (plan), WP-12B (superseded implementation), WP-12C (final implementation)

## 1. Status

Accepted.

## 2. Context

WP-12's objective, per the Implementation Plan, was to integrate WP-00, WP-01, WP-02, WP-04 through WP-11, and WP-03 into the single deployment flow described in Architecture Specification §7 — composing the already-approved `...WithAudit` methods into one end-to-end orchestration entry point, `DeploymentAgent.runDeploymentLifecycle()`, without introducing new business logic, new ports, or new trust states.

That objective was met in the initial WP-12 implementation: the resulting orchestration composed seven already-approved methods unmodified and matched Architecture Specification §7 steps 1–9 step-for-step. Its return type, `DeploymentLifecycleOutcome`, was defined as a pure union of two already-approved shapes — the rejected case from `HighRiskDeploymentOutcome` and `RollbackConsiderationOutcome` in full — so that no new contract shape, beyond a bare union of existing ones, would need review.

This is where the limitation surfaced. `RollbackConsiderationOutcome` was designed under WP-10/WP-11 to describe the result of a single rollback-consideration sub-call — it was never intended to describe an entire lifecycle, because until WP-12 existed, nothing in the repository called more than one or two of these methods in sequence as part of a single externally-visible operation. Reusing that type as the return value of the new top-level lifecycle method caused every fact known earlier in the run — the candidate identity, the risk classification, the Founder approval decision, the original execution outcome, the verification result — to be silently dropped by the time the method returns, because none of those facts were ever part of what `RollbackConsiderationOutcome` was built to carry.

This was not an implementation defect. The composition itself was correct: every branch faithfully delegated to an already-approved method, no method body was modified, and the seven-event audit model remained exactly as approved. The limitation was that the *result-type reuse* — a deliberate, constraint-compliant choice at the time — was made without an explicit architectural decision about what the lifecycle-level result type is responsible for representing. That question did not exist, and could not have been evaluated, before a lifecycle-level orchestration method existed at all. WP-12 was the first work package to need a result type that spans the entire flow, and this was the first point at which the gap became visible.

## 3. Decision

`DeploymentLifecycleOutcome` shall conceptually represent the terminal state of one complete deployment lifecycle, not merely the outcome of the last sub-operation `runDeploymentLifecycle()` happened to call.

This decision is explicitly scoped as follows:

- No new business decisions are introduced. Every fact the lifecycle outcome carries is produced by an existing, previously-approved port (`PolicyEnginePort`, `DeploymentExecutionPort`, `FounderConsolePort`, `VerificationPort`, `RollbackExecutionPort`, `GitHubIntegrationPort`) and is already observed by `runDeploymentLifecycle()` in the course of its existing, approved composition.
- No new trust states are introduced. Reported and Verified (Architecture Specification §8) remain the only two trust states.
- No Policy Engine responsibilities move. Classification and both rollback determinations remain exclusively the Policy Engine's.
- No Founder Console responsibilities move. Approval remains exclusively the Founder Console's.
- No Audit responsibilities move. The audit trail's role as a best-effort, passive record is unchanged; `AuditTrailPort` and the seven-event `AuditableAction` set are untouched.

This decision concerns preservation of already-known information only — it does not authorize any new decision-making logic, any new port, or any new architectural component. `DeploymentAgent` already possesses every fact at the moment `runDeploymentLifecycle()` returns; the initial implementation discarded most of them on the way out. This decision reverses that discarding.

**Structural requirement:** applicability of each fact must be enforced by the type itself, not by a sentinel value a consumer must interpret. No field may exist on a variant where the corresponding lifecycle step never ran. (This structural requirement was not fully met by the first realization of this decision — see WP-12B/WP-12C below — and required a corrective implementation, WP-12C, before this ADR could be considered fully realized.)

## 4. Consequences

- Callers of `runDeploymentLifecycle()` can determine the deployment's actual outcome, verification status, rollback rationale, and candidate identity directly from the return value, without relying on the audit trail's best-effort persistence.
- The result type's name (`DeploymentLifecycleOutcome`) accurately describes what it returns.
- `DeploymentLifecycleOutcome` became a five-variant discriminated union (`rejected`, `low-risk-succeeded`, `low-risk-failed`, `high-risk-succeeded`, `high-risk-failed`), each declaring only the fields applicable to that stage.
- `runDeploymentLifecycle()`'s internal composition changed on its succeeded branch: instead of calling the single combined `verifyAndConsiderRollbackWithAudit()`, it calls `verifyReportedOutcomeWithAudit()` and `considerRollbackOnVerificationFailureWithAudit()` directly — the same two already-approved calls that method already performs internally — because the combined method does not itself return the `VerificationResult` it obtains, and that fact must be preserved on the lifecycle outcome. Neither method's body changed; `verifyAndConsiderRollbackWithAudit()` remains independently callable and unmodified.
- Establishes a lifecycle-complete outcome as the natural foundation for WP-13's validation evidence and any future reporting consumer.

## 5. Alternatives Considered

- **Keep the existing (WP-12 initial) contract unchanged:** rejected. Left the fifteen-lifecycles-into-four-values collapse unresolved and left consumers dependent on the audit trail's best-effort persistence for facts the audit trail is not guaranteed to retain.
- **Use the Audit Trail as the lifecycle source of truth:** rejected. Would require the audit trail's recording to become durable/guaranteed rather than best-effort, directly conflicting with the already-approved WP-03 corrective design, which this ADR does not reopen.
- **A flat structure with all facts present and inapplicable facts left unset by convention:** rejected. The first departure from this codebase's established discipline (every other outcome-shaped type in this repository is a closed, discriminated union, never an object with optional fields left unset by convention).
- **A single "completed" variant using an explicit `"not-applicable"` sentinel value for inapplicable facts:** this was the first realization of this decision (WP-12B). It was found, on CTO review, not to satisfy this ADR's structural requirement — the field still existed on the variant, only its value was explicit. Corrected by WP-12C to a fully staged discriminated union with genuine structural absence.

## 6. Non-Goals

This ADR does not define:

- Exact TypeScript interfaces or concrete field names (settled at the implementation level, WP-12A/WP-12C).
- Any new port, contract boundary, or architectural component.
- Any change to the audit trail's persistence guarantees.
- A migration strategy for existing tests.

## 7. Impact

- **WP-12 (Integration):** directly affected — this ADR governs the shape of `runDeploymentLifecycle()`'s return value, realized through WP-12A (plan), WP-12B (initial, superseded implementation), and WP-12C (final, conforming implementation).
- **WP-13 (System Validation):** indirectly affected — the lifecycle-complete outcome this ADR establishes is available as validation evidence.
- **WP-03 (Audit Trail Foundation), WP-08, WP-09, WP-10, WP-11:** unaffected — no port, method body, or audit event introduced by this decision. `verifyAndConsiderRollbackWithAudit()` in particular remains unmodified and independently callable.
