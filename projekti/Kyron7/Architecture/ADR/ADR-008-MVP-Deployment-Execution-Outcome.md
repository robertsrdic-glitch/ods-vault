# ADR-008: MVP Deployment Execution Outcome

**Status:** Approved
**Date:** 2026-07-18

## 1. Purpose

WP-08 (Automatic Execution Path, Low-Risk) requires an actual execution boundary — not merely a value to relabel — through which the Deployment Agent invokes execution and receives its result, plus a minimal, binary representation of that result. The Execution Specification governs execution but explicitly declines to define either: §4 states "No implementation, format, or mechanism for producing these outputs is defined here," and §7 (Non-Goals) excludes "any implementation, code, or pseudocode describing how execution... is carried out." This ADR supplies exactly the minimum boundary architecture WP-08 needs to implement a real automatic execution path.

## 2. Motivation

Architecture Specification §7 step 9 treats "if execution fails" as a real branch in the deployment flow. WP-05's rollback determination already consumes an opaque `executionFailed: boolean` as an input — but no approved document defines what produces that signal, or through what boundary the Deployment Agent actually invokes execution. A prior draft of this ADR proposed treating the execution result as an externally-supplied signal with no invocation boundary; CTO review rejected that as not implementing an automatic execution path at all. This revision defines the missing boundary: `DeploymentExecutionPort`.

## 3. Scope

This ADR governs the Deployment Agent's low-risk automatic execution path (WP-08): the `DeploymentExecutionPort` boundary contract, the `ReportedOutcome` type it returns, ownership, timing, allowed values, and WP-08's execution semantics. It does not govern high-risk execution (WP-09), rollback execution (WP-10), the Verified side of the Trust Model (WP-11), or audit trail persistence (WP-03) — though it is written to remain consistent with all of them. It does not define any concrete execution infrastructure.

## 4. Definition of ReportedOutcome

```
ReportedOutcome {
  status: "succeeded" | "failed"
}
```

Deliberately minimal — no timestamp, message, or candidate reference. It carries exactly what the Architecture Specification's Trust Model requires: a claim about whether the action completed successfully, stated by the Deployment Agent, prior to any independent verification.

**Semantics:**
- `"succeeded"` means the execution implementation behind `DeploymentExecutionPort` reports that the requested deployment action completed successfully.
- `"failed"` means the execution implementation behind `DeploymentExecutionPort` reports that the requested deployment action did not complete successfully.

No infrastructure-specific rules — shell exit codes, Docker behavior, HTTP status codes, Hostinger-specific commands, health-check algorithms, or any other concrete mechanism — are defined here. Those belong to a future concrete adapter implementing `DeploymentExecutionPort`, outside WP-08's scope.

## 5. DeploymentExecutionPort

```
export interface DeploymentExecutionRequest {
  candidate: CandidateDeployment;
}

export interface DeploymentExecutionPort {
  execute(request: DeploymentExecutionRequest): ReportedOutcome;
}
```

Responsibility:
- Receive the deployment candidate to execute (`request.candidate`).
- Invoke an execution capability through an implementation-neutral boundary — the `execute` method itself is that boundary; it specifies no mechanism for how execution happens.
- Return the technical result of that execution as a `ReportedOutcome`.

**On the request DTO:** every existing `PolicyEnginePort` and `FounderConsolePort` method that accepts a payload wraps it in a dedicated request DTO — `PolicyClassificationRequest`, `RollbackPolicyRequest`, `FounderApprovalRequest` — including `FounderApprovalRequest`, which, like this case, wraps nothing more than a single `CandidateDeployment` field. `DeploymentExecutionRequest` follows that same established contract discipline rather than passing `CandidateDeployment` directly, for consistency across every port in this repository.

No concrete infrastructure implementation of this port is defined here.

## 6. Ownership

- `DeploymentExecutionPort` is a boundary contract owned and invoked by the Deployment Agent — defined in `deployment-agent/contracts/`, mirroring `GitHubIntegrationPort` and `FounderConsolePort`.
- A concrete execution adapter implementing this port produces the technical execution result. No such adapter is defined by this ADR or implemented in WP-08.
- The Deployment Agent treats whatever `DeploymentExecutionPort.execute()` returns as the Reported outcome — its own claim, sourced from the port's result, per Architecture Specification §8.
- The Policy Engine does not execute deployments and does not produce `ReportedOutcome`. Its role remains limited to classification (WP-04) and rollback determination (WP-05), operating on its own internal `DeploymentOutcomeSignal` — a distinct type serving a distinct, internal purpose (see Section 10).

## 7. When It Is Produced

When `DeploymentExecutionPort.execute()` returns, immediately following the execution action it represents — per Architecture Specification §7 step 8: "Following execution, the Deployment Agent reports the outcome as Reported."

## 8. Allowed Outcome Values

Strictly binary — `"succeeded"` or `"failed"` — no score, no confidence value, no third state. Matches the closed-set discipline already established for `RiskClassification`, `RollbackDetermination`, and `FounderApprovalDecision`.

## 9. WP-08 Execution Semantics

WP-08 implements the low-risk automatic execution path as:

1. Receiving or operating on a candidate already classified as low-risk (via the Policy Engine's classification, WP-04).
2. Bypassing Founder approval entirely — no `FounderConsolePort` call occurs on this path, per Architecture Specification §7 step 4 ("no manual command or user interaction").
3. Invoking `DeploymentExecutionPort.execute()` with the candidate.
4. Returning the resulting `ReportedOutcome` as WP-08's output.

WP-08 must not:
- Implement real infrastructure execution behind `DeploymentExecutionPort` — that is separate, future work, outside WP-08's scope and outside this ADR.
- Implement the high-risk approval flow (WP-09).
- Execute rollback (WP-10).
- Perform Verified trust-state checks (WP-11).
- Implement audit persistence — not required by WP-08's approved deliverable (that is WP-03's territory).
- Implement WP-09 or any later work package.

## 10. Relationship to Rollback Determination (WP-05)

- `ReportedOutcome` is the public execution result — the boundary type returned by `DeploymentExecutionPort` and consumed by the Deployment Agent.
- `DeploymentOutcomeSignal` (WP-05) remains an internal Policy Engine input type — private to `policy-engine/`, never exposed through any public port.
- These are not competing authoritative representations: `ReportedOutcome` is authoritative for what execution reported; `DeploymentOutcomeSignal` is authoritative for what the Policy Engine's rollback rule evaluates. A deterministic conceptual correspondence exists between them:

```
ReportedOutcome.status === "failed"
  → DeploymentOutcomeSignal.executionFailed === true
```

- This ADR records that correspondence for future reference only. WP-08 does not implement this mapping or any rollback wiring — that remains out of scope unless a later, explicit work package requires it (not WP-08).

## 11. Non-Goals

This ADR explicitly does not:

- Define concrete execution infrastructure — shell commands, Docker behavior, HTTP status codes, Hostinger-specific commands, health-check algorithms, or any other real mechanism. That belongs to a future concrete adapter implementing `DeploymentExecutionPort`, outside WP-08's scope.
- Define how or when an outcome becomes Verified (Architecture Specification §8; WP-11's territory).
- Wire `ReportedOutcome` into rollback determination (WP-10 / later integration work).
- Define audit trail persistence format or mechanism (WP-03's territory) — not required by WP-08.
- Define high-risk execution semantics (WP-09).
- Introduce any new architectural component. `DeploymentExecutionPort` and `ReportedOutcome` are a boundary contract and a data type owned and consumed by the Deployment Agent, not a sixth component alongside Deployment Agent, Policy Engine, Founder Console, GitHub, and ODS Vault.

## 12. Consequences

- WP-08 implements a deterministic orchestration path: receive a low-risk candidate, invoke `DeploymentExecutionPort.execute()`, return the resulting `ReportedOutcome` — no approval gate, no invented success/failure logic.
- `DeploymentExecutionPort` is defined and consumed as a boundary contract in WP-08; a concrete adapter implementing it is separate, future work, outside WP-08's scope — the same relationship WP-06 and WP-07 already established for `GitHubIntegrationPort` and `FounderConsolePort`. Future adapters may be introduced behind this boundary without changing the orchestration contract.
- `ReportedOutcome` becomes the shared vocabulary type for the Reported side of the Trust Model; WP-09 (high-risk execution) should reuse it rather than defining a competing type.
- The `ReportedOutcome` ↔ `DeploymentOutcomeSignal.executionFailed` correspondence is documented but not implemented; a future work package is responsible for that wiring, not WP-08.

## 13. Alternatives Considered

- **Treating execution outcome as an externally-supplied opaque signal, with no invocation boundary (the original ADR-008 draft):** rejected in CTO review — this does not implement an automatic execution path; it only relabels an already-given value, leaving WP-08 without any real orchestration responsibility for invoking execution.
- **Hardcoding execution as always-successful for the MVP:** rejected — fabricates a guarantee no approved document makes and renders `"failed"` unreachable and untestable.
- **A graded or multi-value outcome:** rejected — conflicts with the binary discipline established for `RiskClassification`, `RollbackDetermination`, and `FounderApprovalDecision`.
- **Defining concrete execution mechanics now (shell/Docker/HTTP specifics):** rejected — infrastructure-specific rules belong to a future concrete adapter, not to this ADR or to WP-08's boundary-definition scope, mirroring how `GitHubIntegrationPort` and `FounderConsolePort` never defined their real integration mechanisms either.
- **Passing `CandidateDeployment` directly to `execute()` without a request DTO:** considered, per the suggested conceptual shape, but a wrapping `DeploymentExecutionRequest` was chosen instead for consistency with the established contract discipline (every existing port with a payload wraps it in a dedicated request DTO, including single-field cases).
- **A richer `ReportedOutcome`** (timestamp, message, candidate reference): rejected for the MVP as unnecessary scope beyond WP-08's requirement, consistent with `RollbackDetermination` and `FounderApprovalDecision`'s own bare closed-set shapes.
