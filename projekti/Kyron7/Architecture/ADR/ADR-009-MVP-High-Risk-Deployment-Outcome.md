# ADR-009: MVP High-Risk Deployment Outcome

**Status:** Approved
**Date:** 2026-07-18

## 1. Context

WP-09 (Manual-Approval Execution Path, High-Risk) requires the Deployment Agent
to orchestrate a high-risk candidate through Founder approval and, only on
approval, through execution. The WP-09 preflight review identified that no
approved document defines what the Deployment Agent's high-risk orchestration
method returns when the Founder **rejects** a candidate.

`ReportedOutcome` (ADR-008 §4) is strictly `"succeeded" | "failed"` and is
defined as the result of invoking `DeploymentExecutionPort` (ADR-008 §5–§6).
The Deployment Execution Engine Specification §2 states execution
responsibility begins only "once Founder approval has been given" — meaning a
rejected candidate never reaches `DeploymentExecutionPort` at all. ADR-008 §12
directs WP-09 to reuse `ReportedOutcome` "rather than defining a competing
type," but does not address the case where no execution occurs.

## 2. Problem

Architecture Specification §7 step 7 states: "On approval, the Deployment
Agent executes accordingly. On rejection, the deployment does not proceed,
and this outcome is recorded in the audit trail." It does not define a type
or value for that outcome.

Without an explicit decision, WP-09 cannot be implemented without one of the
following defects:
- Misrepresenting a rejection as `ReportedOutcome.status === "failed"`,
  falsely implying `DeploymentExecutionPort.execute()` was invoked and
  reported failure, when no execution occurred at all.
- Treating rejection as an exceptional/error condition, when Architecture
  Specification §7 step 6–7 describes it as a normal, expected branch of the
  deployment flow ("The Founder reviews and approves or rejects").
- Leaving the orchestration method's return behavior on rejection undefined,
  which is not implementable without inventing architecture.

## 3. Decision

Founder rejection is not an execution failure and must not be represented as
one. A rejected high-risk candidate:

- must not invoke `DeploymentExecutionPort`
- must not produce a `ReportedOutcome`
- must not be represented as `ReportedOutcome.status === "failed"`
- must not cause the orchestration method to throw merely because the
  Founder rejected it — rejection is expected business behavior, not an
  exceptional condition

`ReportedOutcome` (ADR-008 §4) is unchanged and continues to mean exactly
what ADR-008 defines: the result of an actual invocation of
`DeploymentExecutionPort`.

A new orchestration-level result type, `HighRiskDeploymentOutcome`, is
introduced to represent the outcome of the complete high-risk orchestration
path — approval decision plus, where applicable, execution result — as a
single closed-set return value for WP-09's orchestration method.

## 4. Public Contract

```typescript
export type HighRiskDeploymentOutcome =
  | {
      status: "rejected";
    }
  | {
      status: "reported";
      outcome: ReportedOutcome;
    };
```

This type represents the result of the orchestration process, not the
deployment execution itself.

Strictly binary at the outer discriminant (`"rejected" | "reported"`),
consistent with the closed-set discipline already established for
`RiskClassification`, `RollbackDetermination`, `FounderApprovalDecision`, and
`ReportedOutcome`. No third state, no score, no optional/nullable fields.

## 5. Rejection-Path Semantics

When `FounderConsolePort.submitCandidateForApproval()` returns
`FounderApprovalDecision === "rejected"`:

1. The Deployment Agent halts the high-risk path immediately.
2. `DeploymentExecutionPort` is not invoked under any circumstance.
3. No `ReportedOutcome` is produced or fabricated.
4. The orchestration method returns `{ status: "rejected" }`.
5. This return is a normal, successful return of the orchestration method —
   not a thrown exception, not an error state.

## 6. Approval-and-Execution Semantics

When `FounderConsolePort.submitCandidateForApproval()` returns
`FounderApprovalDecision === "approved"`:

1. The Deployment Agent invokes `DeploymentExecutionPort.execute()` with the
   candidate, per ADR-008 §5.
2. The resulting `ReportedOutcome` is received unchanged, per ADR-008 §4 and
   §8 semantics.
3. The orchestration method returns
   `{ status: "reported", outcome: reportedOutcome }`.

## 7. Ownership and Boundaries

- `HighRiskDeploymentOutcome` is owned by the Deployment Agent API boundary.
- It is produced only through the Deployment Agent's high-risk orchestration
  path (WP-09) — no other component produces or consumes it.
- It introduces no new architectural component. The Architecture
  Specification's five approved components (Deployment Agent, Policy Engine,
  Founder Console, GitHub, ODS Vault) are unchanged.

## 8. Relationship to Existing Contracts

- **`FounderApprovalDecision`** (`"approved" | "rejected"`) — unchanged. It
  is the Founder Console's authorization decision, consumed as an input to
  the high-risk orchestration method. It is not itself returned to the
  orchestration method's caller.
- **`ReportedOutcome`** (`"succeeded" | "failed"`) — unchanged, per ADR-008.
  It can exist only after `DeploymentExecutionPort.execute()` has actually
  been invoked. It appears nested inside `HighRiskDeploymentOutcome` only in
  the `"reported"` branch.
- **`DeploymentExecutionPort`** — unchanged, per ADR-008 §5. Invoked by the
  high-risk orchestration method only on approval, exactly as it is already
  invoked by WP-08's low-risk path.
- **`FounderConsolePort`** — unchanged, per WP-07. Its
  `submitCandidateForApproval()` method is the sole source of the approval
  decision the high-risk orchestration method branches on.
- **`DeploymentAgent`** — gains `FounderConsolePort` as a second constructor
  dependency (alongside the existing `PolicyEnginePort` and
  `DeploymentExecutionPort`), and a new orchestration method that consumes
  it. No existing `DeploymentAgent` method (`requestClassification`,
  `executeLowRiskDeployment`) changes behavior or signature.

## 9. Alternatives Considered

- **Map rejection to `ReportedOutcome.status === "failed"`:** rejected —
  falsely represents "the Founder declined, execution never ran" as "the
  execution implementation reported failure," conflating a pre-execution
  authorization decision with a post-execution technical result. This would
  also make `ReportedOutcome.status === "failed"` ambiguous between two
  materially different situations (execution attempted and failed, vs.
  execution never attempted).
- **Throw an exception on Founder rejection:** rejected — Architecture
  Specification §7 step 6 describes rejection as one of two ordinary
  branches of Founder review ("approves or rejects"), not an exceptional or
  error condition. Modeling expected business behavior as a thrown exception
  would also make the rejection path harder to test and reason about than a
  typed return value.
- **Return `FounderApprovalDecision | ReportedOutcome` directly (a union of
  the two existing types, no new type):** rejected — the two types are not
  substitutable at the same position in every case; a naive union would let
  a caller mistake an approval decision for an execution result (or vice
  versa) without a discriminant tying them together as a single
  orchestration outcome. A dedicated discriminated union expresses the
  actual relationship (rejection **or** approval-plus-execution-result)
  precisely.
- **Make the orchestration method return `void` on rejection (or overall):**
  rejected — gives the caller no way to determine, from the method's return
  value alone, whether the candidate was rejected or approved-and-executed,
  which the Architecture Specification's flow (§7 steps 6–8) requires be
  distinguishable at this boundary.
- **Return `ReportedOutcome | undefined`:** rejected. It forces callers to
  interpret the absence of a value, rather than receiving an explicit
  business outcome. Founder rejection is expected business behavior and
  therefore deserves an explicit typed result, not an implicit `undefined`
  that a caller must remember to check for and correctly interpret as
  "rejected" rather than, say, "not yet resolved" or a bug.

## 10. Consequences

- WP-09 implements a deterministic orchestration path: request Founder
  approval; on rejection, return `{ status: "rejected" }` without touching
  `DeploymentExecutionPort`; on approval, invoke execution and return
  `{ status: "reported", outcome: ReportedOutcome }`.
- `DeploymentAgent` gains a `FounderConsolePort` dependency, mirroring how
  `DeploymentExecutionPort` was added for WP-08.
- `HighRiskDeploymentOutcome` becomes the shared vocabulary type for the
  outcome of the high-risk orchestration path; later work packages (WP-12
  integration, in particular) should reuse it rather than defining a
  competing type.
- `HighRiskDeploymentOutcome` is not intended for low-risk deployments.
  Low-risk deployments continue to return `ReportedOutcome` directly, as
  defined by ADR-008. This separation is intentional and must remain
  unchanged.
- `ReportedOutcome` remains scoped exactly as ADR-008 defined it — the
  result of an actual execution invocation, low-risk or high-risk — and this
  ADR does not reopen or alter that definition.

## 11. Explicit MVP Exclusions

This ADR, and WP-09's use of it, do not:

- Implement audit-trail persistence for the approval decision or the
  high-risk outcome (WP-03's territory).
- Implement rollback behavior for a `"reported"` outcome with
  `status: "failed"` (WP-10's territory).
- Implement or touch Verified trust-state handling (WP-11's territory,
  Architecture Specification §8).
- Introduce a concrete Founder Console implementation or a concrete
  execution adapter — both remain boundary contracts only, per WP-07 and
  ADR-008.
- Implement WP-10, WP-11, or any later integration work (WP-12 and beyond).

## 12. WP-09 Implementation Guidance

- Add `FounderConsolePort` as a third constructor dependency on
  `DeploymentAgent`, alongside the existing `PolicyEnginePort` and
  `DeploymentExecutionPort`.
- Add a new orchestration method (e.g. `executeHighRiskDeployment`) that:
  operates on a candidate already classified high-risk (mirroring how
  `executeLowRiskDeployment` operates on a candidate already classified
  low-risk, per ADR-008 §9) — WP-09 does not itself perform classification;
  calls `FounderConsolePort.submitCandidateForApproval()`; branches on the
  returned `FounderApprovalDecision` exactly per Sections 5–6 above; returns
  `HighRiskDeploymentOutcome`.
- Define `HighRiskDeploymentOutcome` in
  `deployment-agent/contracts/high-risk-deployment-outcome.ts`, following the
  existing contract file/naming convention in that directory.
- Do not modify `FounderApprovalDecision`, `ReportedOutcome`,
  `FounderConsolePort`, or `DeploymentExecutionPort`.

## 13. References

- Kyron7 Deployment Agent MVP — Architecture Specification (Approved), §6,
  §7 steps 5–7
- Kyron7 Deployment Execution Engine Specification (Approved), §2, §6
- ADR-002 — Founder Console Replaces Telegram Approval (Accepted)
- ADR-007 — Deployment Risk Classification Rules (Proposed)
- ADR-008 — MVP Deployment Execution Outcome (Approved)
- Kyron7 Deployment Agent MVP — Implementation Plan (Draft — Pending CTO
  Review), WP-07, WP-08, WP-09
