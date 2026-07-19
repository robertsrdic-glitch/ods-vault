# Kyron7 Deployment Agent — Operationalization Plan

**Type:** Operationalization Plan
**Status:** Draft — Pending CTO/Founder Review
**Date:** 2026-07-19
**Precondition:** `WP-14-Design-Acceptance.md` ("Kyron7 Deployment Agent MVP — Design Complete"); `Project-Closure-Report.md` (Design & Build phase closed, WP-00 through WP-14 all APPROVED)
**Basis:** Deployment Agent MVP Architecture Specification §7 (Deployment Flow), §8 (Trust Model), §9 (Constraints); Deployment Policy Engine Specification; Deployment Execution Engine Specification; ADR-002 (Founder Console Replaces Telegram Approval); ADR-005 (Fresh Repository Baseline); ADR-008 (MVP Deployment Execution Outcome); ADR-011 (Independent Rollback Decision Model); ADR-012 (Verification Ownership Model); `WP-14-Design-Acceptance.md` §4 (Outstanding Items) and §6 (Next Phase); `Pilot-Deployment-Validation-Plan.md`
**Revision:** CTO-directed refinement pass, 2026-07-19 — work-package granularity, an added governance gate, an expanded Production Acceptance outcome set, and an Operational Principles section. No architecture, ADR, or scope change.

This is a planning document only. It introduces no new architecture, port, contract, or business logic, and changes no ADR. It organizes the Operationalization phase into a sequenced roadmap and states the measurable conditions under which that phase ends and a Production Acceptance decision becomes possible. Where a plan already exists for part of this phase (`Pilot-Deployment-Validation-Plan.md`), this document references it rather than restating or altering it.

---

## 1. Purpose

### 1.1 Status of Prior Phases (explicit statement)

**Architecture is complete and frozen.** The Architecture Specification, Deployment Policy Engine Specification, and Deployment Execution Engine Specification are each Approved and unchanged since original approval. No architectural change is proposed, required, or in scope anywhere in this document.

**Design & Build is complete and closed.** Per `Project-Closure-Report.md`: all fifteen top-level work packages (WP-00 through WP-14, including WP-12A/B/C and WP-13A) reached APPROVED; all thirteen ADRs (ADR-001 through ADR-013) carry a terminal Accepted/Approved status; 184 automated tests pass; `WP-14-Design-Acceptance.md` certifies "Kyron7 Deployment Agent MVP — Design Complete." This Operationalization Plan does not reopen, revalidate, or add to that closed phase.

### 1.2 Objectives

Operationalization exists to produce the one category of evidence Design Acceptance explicitly could not produce (`WP-14-Design-Acceptance.md` §1, §6): proof that the already-approved design behaves correctly against real infrastructure, not test doubles. Concretely, this phase must:

1. Build minimal, thin live adapters for the boundaries `WP-14-Design-Acceptance.md` §4 lists as outstanding — the live GitHub adapter, live Founder Console channel, real deployment execution, real rollback execution, real verification, and real audit persistence — implementing the already-approved port interfaces exactly as specified, with no interface change. Per this revision, this work is executed as six separate, individually-completable work packages (Section 4, OP-01–OP-06) rather than one combined package, matching the granularity already proven across WP-00–WP-14.
2. Pass a mandatory Operational Readiness Review (Section 4, OP-07) confirming every adapter from step 1 is complete, interface-compliant, and CTO-reviewed, before any live pilot begins.
3. Execute the pilot defined in `Pilot-Deployment-Validation-Plan.md` against those live adapters, only after the Operational Readiness Review has passed.
4. Compile the pilot evidence report that document's own Exit Criteria (§7) calls for, and present it for CTO and Founder review.
5. Reach an explicit Production Acceptance decision — Accept, Conditional Acceptance, Reject, or Defer (Section 6) — a decision this document does not itself make, per the Design Acceptance / Production Acceptance split established at `WP-14-Design-Acceptance.md` §1, §6.

### 1.3 Scope

**In scope:** live adapters for the six port boundaries already defined in the approved architecture and already enumerated in `Pilot-Deployment-Validation-Plan.md` §4 (`GitHubIntegrationPort`, `DeploymentExecutionPort`, `RollbackExecutionPort`, `FounderConsolePort`, `VerificationPort`, `AuditTrailPort`); the Operational Readiness Review gate; execution of the pilot scenarios in `Pilot-Deployment-Validation-Plan.md` §5 against the single initial target product already scoped for this MVP; evidence collection and compilation; the Production Acceptance decision point itself (not its outcome).

**Out of scope, per `Pilot-Deployment-Validation-Plan.md` §3 and the Architecture Specification's own Non-Goals, restated here without expansion:** any additional Kyron7 product; any Founder Console capability beyond deployment approval; any change to Policy Engine classification or rollback rules; any new port, contract, or component; performance/load/scale testing; multi-environment, multi-region, or multi-cloud orchestration; any interface for authoring Policy Engine rules; any code, contract, or architecture change discovered during this phase (to be documented and deferred to a superseding ADR, never implemented silently).

---

## 2. Operational Principles

Governance guidance for this phase. These principles clarify how existing rules (Implementation Plan §6 Review Gates, ADR-002, ADR-011, ADR-012, the Architecture Specification's frozen status) apply under live-system conditions. They introduce no new requirement beyond what Sections 1, 3, 4, and 6 already state.

- **Architecture remains frozen.** Nothing discovered during Operationalization changes the Architecture Specification, the Policy Engine Specification, the Execution Specification, or any ADR directly — a change requires a superseding ADR, per the same rule already governing Design & Build (Implementation Plan §2).
- **Evidence before opinion.** Every claim about live behavior is backed by the evidence formats already defined in `Pilot-Deployment-Validation-Plan.md` §6, not by expectation or assumption.
- **Governance before speed.** The Operational Readiness Review (OP-07) and the Implementation Plan §6 Review Gate sequence are not to be shortened or bypassed under pilot time pressure.
- **No emergency architecture changes during pilot.** A design gap discovered mid-pilot is documented and deferred to a superseding ADR (Section 5, Governance Risks) — it is never patched directly in a running live adapter.
- **Every failure is documented.** Adapter failures, rollback events, and verification mismatches are recorded as evidence (`Pilot-Deployment-Validation-Plan.md` §6), not treated as noise.
- **Rollback before workaround.** Where a live deployment fails, the already-approved rollback path (ADR-011) is used; no ad hoc manual correction substitutes for it.
- **Every operational change remains traceable.** Each OP work package's output (adapter, review record, evidence report, decision record) is filed in the vault and carries an unambiguous approval status from the point it is created — this plan's own traceability failure around ADR-006/ADR-007 (`Kyron7 Project Health.md`) is not to be repeated.
- **Production Acceptance is earned through evidence, never assumed.** Reaching the end of the OP work-package sequence makes a Production Acceptance decision possible; it does not itself constitute or imply acceptance (Section 6).

---

## 3. Success Criteria

Operationalization succeeds when all of the following hold:

- Every live adapter in Section 1.2 (OP-01 through OP-06) exists, implements its already-approved port interface with no interface deviation, and has been exercised by at least one real invocation.
- The Operational Readiness Review (OP-07) has passed with CTO sign-off.
- Every success criterion in `Pilot-Deployment-Validation-Plan.md` §2 is met, without restatement here — that document's criteria govern the pilot itself.
- Every scenario in `Pilot-Deployment-Validation-Plan.md` §5 has direct evidence, or an explicit, justified deferral — none may be silently skipped.
- A pilot evidence report has been compiled per `Pilot-Deployment-Validation-Plan.md` §6–§7 and presented to the CTO and Founder.
- No defect, safety issue, or architectural deviation has been discovered that was not already known and accepted at Design Acceptance (`WP-14-Design-Acceptance.md` §4); any that is discovered is documented and routed through a superseding ADR, not resolved ad hoc.

### Conditions required before Production Acceptance may be decided

Production Acceptance is a separate, future decision (`WP-14-Design-Acceptance.md` §1, §6; `Project-Closure-Report.md`, Remaining Objective). This plan does not grant it. It only defines when the decision becomes possible to make. That point is reached when, and only when:

- All Operationalization Success Criteria above are met.
- The pilot evidence report exists and has been reviewed by both CTO and Founder.
- Every open item from `Pilot-Deployment-Validation-Plan.md` §7 (Exit Criteria) is closed.
- No unresolved governance question remains open (see Section 5, Governance Risks).

---

## 4. Work Package Roadmap

Proposed sequence. Numbering is independent of the closed WP-00–WP-14 series to avoid collision; these are Operationalization-phase packages (`OP-`), not Design & Build work packages. Per this revision, adapter build-out is split into six individually-completable packages (OP-01–OP-06), followed by a governance gate (OP-07) before pilot execution (OP-08) and the acceptance decision point (OP-09). No adapter beyond the six already-approved architecture ports is introduced.

### OP-01 — GitHub Integration Adapter

- **Objective:** Implement a real, read-only adapter for `GitHubIntegrationPort`, exactly against its existing, already-approved interface — no interface change.
- **Expected deliverables:** a real adapter identifying a candidate deployable artifact from GitHub, per Architecture Specification §6, §7 step 1; must not originate, store, version, or modify artifacts, per `Pilot-Deployment-Validation-Plan.md` §4.
- **Completion criteria:** adapter exists, compiles against the existing `GitHubIntegrationPort` interface with zero modification to that interface, and has been exercised by at least one real (non-test-double) invocation against a live GitHub repository.
- **Dependencies:** none beyond the closed Design & Build phase (WP-06 established this boundary).

### OP-02 — Founder Console Adapter

**Status: Architecture approved; implementation not yet started (2026-07-19).** The transport and trust-boundary blocker identified during initial implementation attempts is resolved: `ADR-014-Founder-Approval-Transport-and-Trust-Boundary.md` (Accepted) and `Founder-Console-Integration-Contract.md` (Approved), both in `projekti/Kyron7/Architecture/`, now govern this adapter. No adapter code has been written yet. This status note does not change the objective/deliverables/completion criteria/dependencies below, which remain as originally planned.

- **Objective:** Implement a real, Cloudflare Access-authenticated `FounderConsolePort` channel, checked against the Founder allowlist, per ADR-002 — no interface change, and consistent with ADR-002's requirement that no AI agent expose or consume this mechanism.
- **Expected deliverables:** a real approval channel through which a high-risk candidate is raised to the Founder Console and an approve/reject decision is received back, matching the existing WP-07 boundary.
- **Completion criteria:** adapter exists, compiles against the existing `FounderConsolePort` interface with zero modification, and has been exercised by at least one real, Founder-identity-authenticated approve or reject decision.
- **Dependencies:** none beyond the closed Design & Build phase (WP-07 established this boundary).

### OP-03 — Deployment Execution Adapter

- **Objective:** Implement a real, minimal adapter for `DeploymentExecutionPort` against the pilot's actual target, per Architecture Specification §6, §7 step 4 — no interface change.
- **Expected deliverables:** an execution adapter capable of carrying out a low-risk automatic deployment and a Founder-approved high-risk deployment, against the single initial target product already scoped for this MVP.
- **Completion criteria:** adapter exists, compiles against the existing `DeploymentExecutionPort` interface with zero modification, and has been exercised by at least one real deployment.
- **Dependencies:** none beyond the closed Design & Build phase (WP-08/WP-09 established this boundary). A real invocation is most easily exercised once OP-01 can supply a real candidate, but building the adapter itself does not require OP-01 to be complete first.

### OP-04 — Rollback Execution Adapter

- **Objective:** Implement a real, minimal adapter for `RollbackExecutionPort` capable of reversing a pilot deployment, per ADR-011's two independently-bounded rollback questions (execution-failure and verification-failure) — no interface change.
- **Expected deliverables:** a rollback adapter capable of reversing the specific deployment OP-03's adapter can perform.
- **Completion criteria:** adapter exists, compiles against the existing `RollbackExecutionPort` interface with zero modification, and has been exercised by at least one real, deliberately-engineered rollback.
- **Dependencies:** OP-03 — a rollback adapter reverses a real deployment and cannot be meaningfully exercised until a real deployment execution exists to reverse.

### OP-05 — Verification Adapter

- **Objective:** Implement a real, even if minimal, independent `VerificationPort` mechanism, consistent with ADR-012's verification-ownership model — no interface change.
- **Expected deliverables:** a verification mechanism that determines Verified status for a real Reported outcome, without the Deployment Agent making that determination itself, per Architecture Specification §8.
- **Completion criteria:** adapter exists, compiles against the existing `VerificationPort` interface with zero modification, and has been exercised by at least one real verification of a real Reported outcome.
- **Dependencies:** OP-03 — mirroring the original Implementation Plan's dependency pattern for this boundary (WP-11 depended on WP-08/WP-09), a real Reported outcome must exist before this adapter's real invocation can occur; the port's own interface remains source-agnostic per ADR-008.

### OP-06 — Audit Trail Adapter

- **Objective:** Implement a real, durable `AuditTrailPort` backend — explicitly not an in-memory or mock store, per `Pilot-Deployment-Validation-Plan.md` §4 — no interface change.
- **Expected deliverables:** a durable persistence backend recording every decision point and action, per Architecture Specification §9.
- **Completion criteria:** adapter exists, compiles against the existing `AuditTrailPort` interface with zero modification, and has been exercised by at least one real, durably-persisted audit entry retrievable after the fact.
- **Dependencies:** none beyond the closed Design & Build phase for the backend to exist and accept a real entry. Full audit coverage naturally depends on OP-01 through OP-05 also being live, mirroring the original Audit Trail Foundation's own dependency pattern (WP-03 depended on WP-02 and WP-04 through WP-11 collectively, since it records every decision point across the whole flow).

### OP-07 — Operational Readiness Review

**Purpose:** confirm that every operational adapter is complete and CTO-reviewed before any live pilot begins. This is a mandatory governance gate, not an implementation package — it builds nothing new.

- **Objective:** Verify, for each of OP-01 through OP-06: implementation complete; interface compliance (no deviation from the already-approved port interface); logging present; auditability confirmed (the adapter's actions are visible in OP-06's real audit trail); rollback capability confirmed where applicable; verification capability confirmed where applicable; no unresolved architecture deviation.
- **Expected deliverables:** a single review record covering all six adapters against the checklist above, signed off by the CTO.
- **Completion criteria:** the review record exists, is CTO-signed, and finds zero unresolved architecture deviations across all six adapters; any deviation found is either resolved or explicitly deferred with CTO/Founder visibility before this gate is considered passed.
- **Dependencies:** OP-01, OP-02, OP-03, OP-04, OP-05, and OP-06 all complete. **Pilot Deployment Validation (OP-08) may not begin until this gate is passed** — no exception.

### OP-08 — Pilot Deployment Validation

- **Objective:** Execute `Pilot-Deployment-Validation-Plan.md` in full against the OP-01–OP-06 live adapters, only after OP-07 has passed. This work package's deliverables and completion criteria are that document's own Section 2 (Success Criteria) and Section 5 (Pilot Scenarios) — referenced here, not restated or altered.
- **Expected deliverables:** the evidence set defined in `Pilot-Deployment-Validation-Plan.md` §6 for every scenario in its §5.
- **Completion criteria:** every criterion in `Pilot-Deployment-Validation-Plan.md` §2 met; every scenario in its §5 evidenced or explicitly, justifiably deferred with CTO/Founder visibility.
- **Dependencies:** OP-07 passed (Operational Readiness Review).

### OP-09 — Pilot Evidence Report and Production Acceptance Decision Point

- **Objective:** Compile the pilot evidence report called for in `Pilot-Deployment-Validation-Plan.md` §7, present it to the CTO and Founder, and reach an explicit Production Acceptance decision — Accept, Conditional Acceptance, Reject, or Defer (Section 6) — mirroring the Design Acceptance / Production Acceptance split established at `WP-14-Design-Acceptance.md`.
- **Expected deliverables:** a single evidence report consolidating OP-08's results against every Pilot Plan §2 criterion and §5 scenario; a formal decision record (in the same acceptance-document style as `WP-14-Design-Acceptance.md`) stating the outcome and, if Conditional Acceptance, the follow-up actions and agreed completion dates.
- **Completion criteria:** the report is filed; the CTO and Founder have both reviewed it; a decision record exists with one explicit outcome from the four defined in Section 6 — this work package does not complete on "report filed" alone, it completes on "decision recorded."
- **Dependencies:** OP-08 complete.

---

## 5. Risks

### Operational Risks

- A live adapter's real-world failure mode (network partition, target-system outage, credential expiry) is untested by the 184-test unit suite, which validates logic against test doubles only (`WP-14-Design-Acceptance.md` §1) — the pilot may surface behavior the design-level evidence could not.
- The audit trail's persistence is documented as "best-effort" (`Deployment-Agent-MVP-Implementation-Plan.md`, WP-03 status note) — real deployment load may expose gaps OP-06 and the pilot's Objective 5 (`Pilot-Deployment-Validation-Plan.md` §1) are specifically designed to test, but the outcome of that test is not yet known.
- The Founder Console channel (OP-02) has never been exercised outside test doubles; a real Cloudflare Access misconfiguration could block or falsely permit an approval decision.

### Validation Risks

- A verification-failure rollback (`Pilot-Deployment-Validation-Plan.md` §5) may not occur naturally within a small pilot and may be difficult to safely engineer; the Pilot Plan already requires this be explicitly recorded as deferred rather than silently skipped if it cannot be safely forced — this plan carries that same requirement forward without relaxing it.
- Evidence collected against a single initial target product (the only target in scope) may not generalize to a different future target; this plan does not claim it does, and no such claim should be inferred from Operationalization's completion.
- Splitting adapter work into OP-01–OP-06 creates a risk of each being individually "complete" while an integration gap exists between them; OP-07 (Operational Readiness Review) exists specifically to catch this before OP-08 begins.

### Governance Risks

- Discovering a design gap during a live pilot creates pressure to patch it directly in the running system rather than routing it through a superseding ADR; Section 1.3 (Scope) and `Pilot-Deployment-Validation-Plan.md` §3 both explicitly forbid this — any such discovery must be documented and deferred, not implemented mid-pilot.
- This project's standing review-gate workflow (Implementation Plan §6: Developer completion → CTO Review → APPROVED → Commit) has, to date, applied cleanly to code work packages; Operationalization work involves real external systems and real Founder-identity-authenticated approvals, which raises the stakes of any gate being skipped under pilot time pressure — OP-07 exists to formalize this gate, but the risk of it being weakened in practice under real time pressure remains.
- As documented in `Kyron7 Project Health.md`, ADR-006 and ADR-007 required an explicit, separately-tracked Founder approval pass after being treated as binding without formal ADR-level sign-off; this plan's own OP work-package outputs (adapters, review record, evidence report, decision record) should not repeat that pattern — each should carry unambiguous approval status from the point it is created, not retroactively.

---

## 6. Exit Criteria

### Exact conditions for completing Operationalization

Operationalization is complete when, and only when:

- OP-01 through OP-09 have each individually reached a completed state per their own completion criteria in Section 4, in dependency order — including OP-07 (Operational Readiness Review) having passed with CTO sign-off before OP-08 began.
- Every Success Criterion in Section 3 (Operationalization) is met.
- Every Success Criterion in `Pilot-Deployment-Validation-Plan.md` §2 is met, without exception or unexplained deferral.
- Every scenario in `Pilot-Deployment-Validation-Plan.md` §5 is evidenced or explicitly, justifiably deferred with CTO/Founder visibility — none silently skipped.
- The pilot evidence report (OP-09) has been filed and reviewed by both CTO and Founder.
- No unresolved finding remains open (mirroring `Pilot-Deployment-Validation-Plan.md` §7's own exit condition).

### Readiness gate for Production Acceptance

Meeting the conditions above makes a Production Acceptance decision **possible**, not automatic. Consistent with `WP-14-Design-Acceptance.md` §1 and §6 and `Project-Closure-Report.md`'s Remaining Objective: Production Acceptance is a distinct, separate decision, made by the CTO and Founder against the OP-09 decision record, and is not implied, pre-committed, or defaulted to by Operationalization's completion. This document does not make that decision and does not begin Production Acceptance work of any kind.

The decision record produced at OP-09 states exactly one of the following four outcomes:

- **Accept** — the system is accepted for production with no outstanding condition.
- **Conditional Acceptance** — the system is accepted for production with explicitly documented non-blocking follow-up actions and agreed completion dates.
- **Reject** — the system is not accepted for production; the reasons and required remediation are documented.
- **Defer** — no decision is made at this time; the reasons and the conditions for revisiting the decision are documented.

---

## 7. Traceability

**Architecture (unchanged, frozen):**
- Deployment Agent MVP — Architecture Specification (Approved) §6, §7, §8, §9
- Deployment Policy Engine Specification (Approved)
- Deployment Execution Engine Specification (Approved)

**ADRs referenced (unchanged, no ADR modified by this document):**
- ADR-002 — Founder Console Replaces Telegram Approval (Accepted) — governs the OP-02 `FounderConsolePort` live adapter
- ADR-005 — Fresh Repository Baseline for Deployment Agent MVP (Accepted) — governs where OP-01–OP-06 adapter code is built
- ADR-006 — Technology Stack Selection for Deployment Agent MVP (Accepted) — governs the tooling OP-01–OP-06 adapters are built with
- ADR-007 — Deployment Risk Classification Rules (Accepted) — governs classification inputs any live GitHub/execution adapter must supply
- ADR-008 — MVP Deployment Execution Outcome (Approved) — defines the source-agnostic Reported outcome shape OP-05's verification adapter operates on
- ADR-011 — Independent Rollback Decision Model (Approved) — governs the OP-04 `RollbackExecutionPort` adapter and the OP-08 rollback pilot scenarios
- ADR-012 — Verification Ownership Model (Approved) — governs the OP-05 `VerificationPort` adapter

**Closure and acceptance records (unchanged, no historical record altered by this document):**
- `Project-Closure-Report.md` — Design & Build phase closure; source of the "Remaining Objective Before Production Acceptance" this plan operationalizes
- `WP-14-Design-Acceptance.md` — source of the Outstanding Items (§4) this plan's OP-01–OP-06 address, and the Design Acceptance / Production Acceptance split (§1, §6) this plan's OP-09 and Section 6 preserve

**Operationalization-phase planning:**
- `Pilot-Deployment-Validation-Plan.md` — the existing, approved-scope plan this document sequences as OP-08; referenced throughout, not restated or altered
