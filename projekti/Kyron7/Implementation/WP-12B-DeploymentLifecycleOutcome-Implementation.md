# WP-12B — DeploymentLifecycleOutcome Implementation

**Type:** Work Package Implementation Record
**Status:** Superseded by WP-12C
**Date:** 2026-07-19
**Parent document:** WP-12A (DeploymentLifecycleOutcome Refactoring); ADR-013
**Implementation commit:** `026c20a` (superseded — not the authoritative implementation)

**This document is NOT the authoritative implementation of ADR-013 or WP-12A. Do not treat commit `026c20a` or this document's contract shape as current. See WP-12C for the authoritative implementation.**

## 1. Purpose

First implementation attempt realizing WP-12A's approved plan: redefine `DeploymentLifecycleOutcome` and `DeploymentAgent.runDeploymentLifecycle()`'s return construction so the outcome represents a complete lifecycle rather than the last sub-operation's result.

## 2. Implementation Summary (as committed)

- `DeploymentLifecycleOutcome` became a two-variant union: `{status:"rejected"}` or a `"completed"` variant carrying `candidate`, `classification`, `approvalDecision`, `executionOutcome`, `verificationResult`, and `rollback` — with `approvalDecision` and `verificationResult` typed as their real value **or the literal `"not-applicable"`**.
- The implementation mechanism selected (per WP-12A's deliberately-left-open Section 3): on the succeeded branch, `runDeploymentLifecycle()` calls `verifyReportedOutcomeWithAudit()` and `considerRollbackOnVerificationFailureWithAudit()` directly, instead of the combined `verifyAndConsiderRollbackWithAudit()`, to make `VerificationResult` observable. This mechanism was retained unchanged through WP-12C.
- 11 new tests added; 175 tests passing; format/lint/typecheck clean at commit time.

## 3. Review History

**WP-12B CTO Review:** CONDITIONALLY APPROVED. Implementation quality assessed as good; approval conditioned on a follow-up Focused Contract-Conformance Review.

**WP-12B Focused Contract-Conformance Review** — evidence-based review against WP-12A's exact wording. Findings:

- **Confirmed deviation:** the `"completed"` variant did not achieve structural absence for `approvalDecision` or `verificationResult` — both keys were present on every `"completed"` instance regardless of applicability; inapplicability was represented by the value `"not-applicable"`, not by the key's absence. This deviates from WP-12A Approach 2's literal wording: "no field exists on a variant where the corresponding step never ran." (The outer `"rejected"` vs. `"completed"` split did achieve genuine structural absence — the deviation was confined to the two `"not-applicable"` fields inside `"completed"`.)
- **Secondary, judgment-dependent finding:** `approvalDecision`'s `"approved"`/`"rejected"` values were reconstructed at the return site (from `HighRiskDeploymentOutcome`'s own discriminant) rather than copied directly from `FounderConsolePort`'s return value — in tension with, though not clearly prohibited by, the requirement that every field originate directly from a port call. This has direct precedent in the already-approved WP-03 audit-recording code's identical technique. True direct preservation would require modifying `executeHighRiskDeployment`'s contract (an already-approved WP-09 method), which was out of scope. This finding was **not** required to be corrected by WP-12C and remains carried forward as a disclosed, scope-bounded characteristic of the current (WP-12C) implementation.

**Verdict:** IMPLEMENTATION DEVIATES FROM WP-12A. Smallest compliant correction identified: split the `"completed"` variant into narrower variants keyed on `classification` and `executionOutcome.status`, each declaring only the keys applicable to it.

## 4. Final Disposition

**Superseded by WP-12C**, which implements the corrective structure identified in the Contract-Conformance Review's own recommendation. Commit `026c20a` remains in git history as WP-12C's parent commit but must not be treated as the current or authoritative implementation of ADR-013.
