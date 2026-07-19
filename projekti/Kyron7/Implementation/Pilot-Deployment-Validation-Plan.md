# Pilot Deployment Validation Plan

**Type:** Planning document — Operationalization phase entry point
**Status:** Planned — not yet executed
**Date:** 2026-07-19
**Precondition:** WP-14 Design Acceptance ("Kyron7 Deployment Agent MVP — Design Complete")
**Basis:** Architecture Specification §7 (Deployment Flow), §8 (Trust Model), §9 (Constraints); ADR-002 (Founder Console); WP-14-Design-Acceptance.md §6; the five port boundaries already defined in the repository

This document plans the first phase of Operationalization. It introduces no new architecture, port, contract, or business logic — it defines how already-approved boundaries get their first live adapters and how that is validated.

## 1. Pilot Objectives

1. Prove a low-risk deployment executes automatically against a real target, with no manual command and no human in the loop.
2. Prove a high-risk deployment halts for, and proceeds only after, an actual Founder decision through a real, Cloudflare Access-authenticated Founder Console channel.
3. Prove a Founder rejection actually prevents execution against real infrastructure.
4. Prove rollback executes according to a live Policy Engine determination for both independently-bounded rollback questions (execution-failure and verification-failure, per ADR-011).
5. Test whether the audit trail's best-effort persistence guarantee is acceptable once real deployments depend on it.
6. Confirm no behavior contradicts what the 184-test unit suite already established — the pilot confirms already-proven logic under real conditions, it does not search for new logic.

## 2. Success Criteria

- At least one low-risk deployment executed fully automatically with a confirmed Verified outcome.
- At least one high-risk deployment approved through the real Founder Console and executed only after that approval.
- At least one high-risk deployment rejected through the real Founder Console, with execution confirmed never to have occurred.
- Zero instances of a high-risk deployment executing without a recorded Founder approval.
- Zero instances of a manual override of Policy Engine classification.
- At least one rollback observed (deliberately engineered), confirmed triggered by a Policy Engine determination.
- 100% of pilot deployment actions present and retrievable in real audit persistence afterward.
- Zero unexplained discrepancies between the audit trail and independently-observed pilot evidence.
- No defect, safety issue, or architectural deviation discovered that was not already known and accepted at Design Acceptance.

## 3. Pilot Scope

**Included:** a small, bounded set of real deployments against the single initial target product already scoped for this MVP; minimal, thin live adapters for the five boundaries in Section 4, implementing the already-approved port interfaces exactly as specified; evidence collection throughout.

**Excluded:** any additional Kyron7 product; any Founder Console capability beyond deployment approval; any change to Policy Engine classification or rollback rules; performance/load/scale testing; multi-environment/region/cloud orchestration; any interface for authoring Policy Engine rules; any code, contract, or architecture change discovered mid-pilot (documented and deferred, not implemented mid-pilot).

## 4. Required Components

- **GitHub integration** (`GitHubIntegrationPort`): a real, read-only adapter — must not originate, store, version, or modify artifacts.
- **Deployment execution** (`DeploymentExecutionPort`): a real, minimal adapter for the pilot's actual target.
- **Rollback execution** (`RollbackExecutionPort`): a real, minimal adapter capable of reversing a pilot deployment.
- **Founder approval** (`FounderConsolePort`): a real, Cloudflare Access-authenticated channel, checked against the Founder allowlist, per ADR-002 — not simulatable, per that ADR's own requirement that no AI agent expose or consume this mechanism.
- **Verification** (`VerificationPort`): a real, even if minimal, independent verification mechanism.
- **Audit persistence** (`AuditTrailPort`): a real, durable backend — an in-memory or mock store would defeat Objective 5 above.

## 5. Pilot Scenarios

- Successful low-risk deployment.
- Successful high-risk deployment (approved).
- Rejected high-risk deployment.
- Execution failure and rollback (deliberately engineered, safe/reversible).
- Verification failure and rollback (deliberately engineered, since natural occurrence within a small pilot is unlikely; if it cannot be safely engineered, this must be explicitly recorded as deferred, not silently skipped).

## 6. Evidence Collection

For every pilot deployment: candidate identity and classification result with characteristics; for high-risk candidates, the approval request/decision with real Founder identity and timestamps; execution outcome; verification result where applicable; rollback determination and, where triggered, rollback execution outcome; the complete audit trail retrieved from real persistence, cross-checked against the independently-observed sequence; any exception or unexpected behavior; explicit confirmation no manual override was used.

## 7. Exit Criteria

The pilot is complete, and the project may proceed to a Production Acceptance decision, when: every scenario in Section 5 has evidence (or an explicit, justified deferral); every Section 2 criterion is met; no unresolved finding remains open; a pilot evidence report has been compiled (the real-world counterpart to WP-13's validation record) for CTO and Founder review. This exit does **not** itself constitute Production Acceptance — it produces the evidence that decision would be made on, mirroring the Design Acceptance / Production Acceptance split established at WP-14.
