# Kyron7 Deployment Agent MVP — Implementation Plan

## 1. Document Control

- **Type:** Implementation Plan
- **Status:** Draft — Pending CTO Review
- **Date:** 2026-07-18
- **Dependencies:**
  - Kyron7 Deployment Agent MVP — Architecture Specification (Approved)
  - Kyron7 Deployment Policy Engine Specification (Approved)
  - Kyron7 Deployment Execution Engine Specification (Approved)
  - ADR-001 — Separate Product and Platform (Accepted)
  - ADR-002 — Founder Console Replaces Telegram Approval (Accepted)
  - ADR-003 — AI Engineering Workflow v2 (Accepted)
  - ADR-004 — Kyron7 Deployment Agent Priority (Accepted)
  - ADR-005 — Fresh Repository Baseline for Deployment Agent MVP (Accepted)
  - ADR-010 — Deployment Agent Owns Lifecycle, Policy Engine Owns Policies (Approved)
  - ADR-011 — Independent Rollback Decision Model (Approved)
- **Target Repository:** New Kyron7 Deployment Agent MVP repository (not yet created; the old `kyron7-operations-agent` repository is historical reference only, per ADR-005)

## 2. Purpose

This document defines the ordered implementation work required to build the already-approved Kyron7 Deployment Agent MVP architecture. It converts the Architecture Specification, the Policy Engine Specification, and the Execution Specification into a sequenced set of implementation work packages.

**Architecture is frozen.** This plan does not change architecture or scope. Every requirement referenced below traces to a section of an already-approved document. **Implementation follows architecture** — where this plan is silent or ambiguous relative to the approved documents, the approved documents govern, not this plan.

## 3. MVP Implementation Boundary

Restated from the approved Architecture Specification (§2, §4) only — not expanded:

- Deployment Agent orchestration of the deployment flow.
- Policy Engine classification of a candidate deployment as low-risk or high-risk, and policy-driven determination of rollback.
- Automatic execution for low-risk deployments, with no manual deployment command and no user interaction.
- Founder Console approval as a prerequisite for any high-risk deployment before execution.
- Execution and rollback carried out by the Deployment Agent according to the Policy Engine's determinations, not hardcoded into the Deployment Agent.
- Deployment outcomes reported as Reported at the time an action completes.
- Independent verification determining whether a Reported outcome becomes Verified.
- Audit trail recording of every decision point and action, as an architectural requirement of the platform.
- Integration points with GitHub (authoritative source of deployable artifacts) and ODS Vault (authoritative source of architecture and deployment policy documentation), as described in the Architecture Specification and Policy Engine Specification.

## 4. Repository Bootstrap

The MVP implementation begins in a new, empty repository, per ADR-005. This section describes only the repository's initial shape — no code, no implementation logic.

- **Purpose:** house the Deployment Agent MVP implementation exclusively — the Deployment Agent's orchestration and execution responsibility, and the Policy Engine — as scoped by the approved architecture. It carries no code, types, or identifiers inherited from the old `kyron7-operations-agent` repository.
- **High-level directory structure (conceptual only):**
  - An area for the Deployment Agent's orchestration and execution responsibility (Architecture Specification §6; Execution Specification).
  - An area for the Policy Engine's classification and Deployment Policy logic (Policy Engine Specification).
  - An area for the integration points with GitHub and the Founder Console (boundary/interface only — this repository does not implement GitHub or the Founder Console themselves).
  - An area for audit trail recording.
  - A documentation area that references the approved ODS Vault documents by pointer, in the same spirit as the corrected form recommended in the Repository Reconciliation Report — not a restatement of them.
- **Documentation location:** the repository's own documentation states that architecture is authoritative in ODS Vault (Architecture Specification, Policy Engine Specification, Execution Specification, ADR-001–005), consistent with the Repository Reconciliation Report's finding that dangling, unverifiable authority citations must not recur.
- **Configuration principles:** no deployment policy or risk-classification logic is hardcoded into the Deployment Agent's area, per the Architecture Specification's constraint that decisions are policy-driven; the repository's structure is generic per ADR-001, not coupled to a specific product; no component beyond the five approved components (Deployment Agent, Policy Engine, Founder Console, GitHub, ODS Vault) is represented in the structure.
- **Governance:**
  - *Official repository name:* `Kyron7/deployment-agent`, consistent with the existing Kyron7 organization's repository naming pattern (e.g. `Kyron7/northstar-artifact-gateway`).
  - *Default branch strategy:* a single default branch (`main`), trunk-based; no long-lived branches beyond a work package's implementation branch, which merges into the default branch only after that work package reaches APPROVED (Section 6).
  - *Versioning strategy:* Semantic Versioning; the repository remains in the pre-release (`0.x`) series throughout implementation and does not reach a `1.0` release before MVP Acceptance (Section 5) is issued.
  - *Coding standards:* enforced through automated formatting, linting, and type-checking established in Development Environment Bootstrap (Section 5); the standards themselves are documented and maintained in the repository, not restated in this plan.
  - *Documentation conventions:* repository documentation is code-adjacent only — it references the authoritative ODS Vault documents (Architecture Specification, Policy Engine Specification, Execution Specification, ADR-001–005) by pointer rather than restating them, correcting the pattern the Repository Reconciliation Report identified as a conflict in the old repository (citing a non-existent "TS-003" as authoritative).

No files or the repository itself are created by this document.

## 5. Ordered Implementation Work Packages

**WP-00 — Development Environment Bootstrap**
- *Objective:* Prepare the development environment only — repository initialization, tooling, formatter, linting, CI skeleton, and documentation bootstrap.
- *Architectural requirement implemented:* ADR-005 (fresh repository baseline); the governance conventions in Section 4 (official repository name, branch strategy, versioning strategy, coding standards, documentation conventions).
- *Dependencies:* None.
- *Expected deliverables:* An initialized repository under the official name established in Section 4, with formatting and linting configuration, a CI skeleton, and a documentation bootstrap that points to the authoritative ODS Vault documents.
- *CTO acceptance criteria:* Confirmed no business logic, deployment logic, Policy Engine, or Deployment Agent content exists in this package — environment and tooling only.
- *Excluded work:* Repository directory structure aligned to the five approved components (WP-01); any Deployment Agent, Policy Engine, GitHub/Founder Console integration, execution, rollback, trust-model, or audit trail logic.

**WP-01 — Repository Bootstrap**
- *Objective:* Establish the new repository's initial structure per Section 4.
- *Architectural requirement implemented:* ADR-005 (fresh repository baseline); ADR-001 (generic, platform-appropriate structure).
- *Dependencies:* WP-00.
- *Expected deliverables:* An initialized repository matching the structure described in Section 4.
- *CTO acceptance criteria:* Repository structure reviewed and confirmed to introduce no component beyond the five approved components; no inherited code, types, or identifiers from the old repository.
- *Excluded work:* Any Deployment Agent, Policy Engine, or integration logic.

**WP-02 — Deployment Agent Orchestration Skeleton**
- *Objective:* Establish the Deployment Agent's role as orchestrator of the deployment flow.
- *Architectural requirement implemented:* Architecture Specification §5 (High-Level Architecture), §6 (Deployment Agent responsibilities), §7 (Deployment Flow, steps 1–2).
- *Dependencies:* WP-01.
- *Expected deliverables:* The structural basis for the Deployment Agent to identify a candidate deployment and request a classification, with no execution or approval logic yet attached.
- *CTO acceptance criteria:* Confirmed that no classification, approval, or execution decision logic exists in this package — orchestration only, per Architecture Specification §6.
- *Excluded work:* Classification, approval handling, execution, rollback.

**WP-04 — Policy Engine: Risk Classification**
- *Objective:* Implement the Policy Engine's classification of a candidate deployment as low-risk or high-risk.
- *Architectural requirement implemented:* Policy Engine Specification §1, §2, §4 (binary classification output); Architecture Specification §6 ("sole source of the automatic-vs-manual-approval decision").
- *Dependencies:* WP-01.
- *Expected deliverables:* A Policy Engine capability that returns exactly one of two classification values for a candidate deployment.
- *CTO acceptance criteria:* Confirmed the classification output is strictly binary (low-risk / high-risk), with no additional or graded risk levels, per Policy Engine Specification §4.
- *Excluded work:* Concrete policy rules defining what makes a deployment low-risk or high-risk (per Policy Engine Specification §3, individual rules are out of scope of the specification itself, and therefore of this work package).

**WP-05 — Policy Engine: Deployment Policy for Rollback**
- *Objective:* Implement the Policy Engine's determination of whether and how rollback applies to a given execution or verification outcome.
- *Architectural requirement implemented:* Policy Engine Specification §2 ("Holds the Deployment Policy that governs risk classification and rollback behavior"), §4 (rollback determination output).
- *Dependencies:* WP-04.
- *CTO acceptance criteria:* Confirmed rollback determination is produced by the Policy Engine and only executed by the Deployment Agent, per Policy Engine Specification §2 and Execution Specification §2.
- *Expected deliverables:* A Policy Engine capability that returns a rollback determination for a failed or unverified deployment outcome.
- *Excluded work:* Execution of rollback itself (Deployment Agent's responsibility, see WP-10).

**WP-06 — GitHub Integration Point**
- *Objective:* Establish how the Deployment Agent identifies a candidate deployable artifact from GitHub.
- *Architectural requirement implemented:* Architecture Specification §6 ("GitHub... is the authoritative source of deployable artifacts"), §7 (Deployment Flow, step 1).
- *Dependencies:* WP-01.
- *Expected deliverables:* An integration point through which the Deployment Agent becomes aware of a candidate deployable artifact in GitHub.
- *CTO acceptance criteria:* Confirmed this package only reads from GitHub as the artifact's authoritative source and does not originate, store, or modify artifacts, per Architecture Specification §6.
- *Excluded work:* Any artifact storage, versioning, or modification capability.

**WP-07 — Founder Console Approval Gate**
- *Objective:* Establish the integration point through which the Deployment Agent requests, and receives, a Founder approval decision for a high-risk deployment.
- *Architectural requirement implemented:* Architecture Specification §6, §7 (steps 5–7); ADR-002 (Cloudflare Access-authenticated identity, Founder allowlist, no AI agent exposing or consuming the approval mechanism).
- *Dependencies:* WP-01.
- *Expected deliverables:* An integration point through which a high-risk candidate is raised to the Founder Console and an approve/reject decision is received back.
- *CTO acceptance criteria:* Confirmed the Deployment Agent does not expose or consume the approval mechanism itself, and that approval identity verification remains the Founder Console's responsibility, per ADR-002.
- *Excluded work:* Any Founder Console UI or capability beyond deployment approval (per Architecture Specification §3 Non-Goals).

**WP-08 — Automatic Execution Path (Low-Risk)**
- *Objective:* Implement execution of a low-risk deployment with no manual command and no user interaction.
- *Architectural requirement implemented:* Architecture Specification §2, §6, §7 (step 4).
- *Dependencies:* WP-02, WP-04, WP-06.
- *Expected deliverables:* An execution path that proceeds automatically once the Policy Engine returns a low-risk classification, producing the recordable action and Reported outcome that WP-03 (Audit Trail Foundation) later captures.
- *CTO acceptance criteria:* Confirmed execution proceeds only from a Policy Engine low-risk classification, with no manual trigger and no additional decision made by the Deployment Agent, per Architecture Specification §6.
- *Excluded work:* High-risk / approval-gated execution (WP-09); rollback (WP-10).

**WP-09 — Manual-Approval Execution Path (High-Risk)**
- *Objective:* Implement execution of a high-risk deployment that proceeds only after Founder approval.
- *Architectural requirement implemented:* Architecture Specification §6, §7 (steps 5–7).
- *Dependencies:* WP-02, WP-04, WP-06, WP-07.
- *Expected deliverables:* An execution path that halts on a high-risk classification, awaits the Founder's decision via WP-07, and proceeds only on approval, producing the recordable decision and outcome that WP-03 (Audit Trail Foundation) later captures.
- *CTO acceptance criteria:* Confirmed execution does not proceed on a high-risk classification without a recorded Founder approval; confirmed a rejection halts the deployment and is recorded in the audit trail, per Architecture Specification §7.
- *Excluded work:* Automatic execution (WP-08); rollback (WP-10).

**WP-10 — Rollback Execution**
- *Objective:* Implement the Deployment Agent's execution of rollback according to the Policy Engine's Deployment Policy.
- *Architectural requirement implemented:* Architecture Specification §6, §7 (step 9), §8, §9; Execution Specification §2; ADR-011 (rollback determination modeled as two independently bounded Policy Engine questions — execution-failure and verification-failure — rather than a single combined determination).
- *Dependencies:* WP-02, WP-05 (sufficient for the execution-failure rollback question); WP-11 Core (the generic verification mechanism only — not WP-11 Integration) additionally required for the verification-failure rollback question, per ADR-011.
- *Expected deliverables:* A rollback execution path triggered by either of two independently evaluated Policy Engine questions — rollback-on-execution-failure and rollback-on-verification-failure, per ADR-011 — producing the recordable action that WP-03 (Audit Trail Foundation) later captures.
- *CTO acceptance criteria:* Confirmed rollback is executed only per a Policy Engine determination and is not a hardcoded Deployment Agent behavior, per Architecture Specification §9 and Execution Specification §5.
- *Excluded work:* The rollback determination itself (WP-05, Policy Engine's responsibility); WP-11 Integration (rollback-outcome verification wiring — that capability depends on this package's own rollback action existing first, see WP-11).

**WP-11 — Trust Model: Reported / Verified Outcome Handling**
- *Objective:* Implement outcome reporting as Reported, and the independent verification path that determines whether an outcome becomes Verified. This package comprises two internally sequenceable capabilities — a generic verification mechanism (**WP-11 Core**) and its integration into rollback's own outcome reporting (**WP-11 Integration**), per Dependencies and Expected deliverables below. Both remain part of this single work package; this distinction does not create a new work package.
- *Architectural requirement implemented:* Architecture Specification §8 (Trust Model); Execution Specification §2, §4.
- *Dependencies:* WP-08, WP-09 (sufficient for WP-11 Core — the generic verification mechanism operates on any Reported outcome regardless of source, per ADR-008's source-agnostic `ReportedOutcome` shape); WP-10 additionally required for WP-11 Integration only (wiring verification into rollback's own outcome reporting requires a rollback action to exist first).
- *Expected deliverables:* **WP-11 Core:** an independent verification mechanism that determines Verified status for a Reported outcome, without the Deployment Agent making that determination itself — usable as soon as WP-08/WP-09 exist. **WP-11 Integration:** wiring that same mechanism into rollback's own outcome reporting once WP-10 exists, completing outcome reporting and verification for every execution and rollback action.
- *CTO acceptance criteria:* Confirmed the Deployment Agent only reports outcomes as Reported and does not itself assign Verified status, per Architecture Specification §8; confirmed no additional trust state beyond Reported and Verified is introduced; confirmed WP-11 Core is usable by WP-10's verification-failure rollback question (per ADR-011) without requiring WP-11 Integration to be complete.
- *Excluded work:* Any trust state beyond Reported and Verified.

**WP-03 — Audit Trail Foundation**
- *Objective:* Implement audit trail recording covering every decision point and action established by WP-02 and WP-04 through WP-11.
- *Architectural requirement implemented:* Architecture Specification §2, §5, §6, §7, §9 ("audit trail... as an architectural requirement of the platform").
- *Dependencies:* WP-02, WP-04, WP-05, WP-06, WP-07, WP-08, WP-09, WP-10, WP-11.
- *Expected deliverables:* Audit trail entries recorded for every decision point and action produced across the flow — classification, approval request and decision, automatic execution, manual-approval execution, rollback, and outcome reporting.
- *CTO acceptance criteria:* Confirmed the audit trail is described and structured as a platform-level requirement, not an application feature, per the approved Architecture Specification's framing; confirmed it captures every decision point and action from WP-02 and WP-04 through WP-11 with no gaps.
- *Excluded work:* Any decision point or action not already established by WP-02 or WP-04 through WP-11.

**WP-12 — Integration**
- *Objective:* Integrate WP-00, WP-01, WP-02, WP-04 through WP-11, and WP-03 into the single deployment flow described in Architecture Specification §7.
- *Architectural requirement implemented:* Architecture Specification §5, §7 in full.
- *Dependencies:* WP-00, WP-01, WP-02, WP-04, WP-05, WP-06, WP-07, WP-08, WP-09, WP-10, WP-11, WP-03.
- *Expected deliverables:* A single integrated instance of the deployment flow covering both the low-risk automatic path and the high-risk Founder-approval path, including a rollback case, both a Reported and a Verified outcome, and audit trail entries across the whole flow.
- *CTO acceptance criteria:* Confirmed the integrated flow matches Architecture Specification §7 step-for-step, with no deviation, omission, or addition.
- *Excluded work:* Validation of the integrated flow against MVP Completion Criteria (WP-13); formal acceptance (WP-14).

**WP-13 — System Validation**
- *Objective:* Validate the integrated flow from WP-12 against every MVP Completion Criterion (Section 8).
- *Architectural requirement implemented:* Architecture Specification §7 (full flow), §8 (Trust Model), §9 (Constraints) — validation confirms these hold end-to-end.
- *Dependencies:* WP-12.
- *Expected deliverables:* Validation evidence demonstrating that each criterion in Section 8 is met by the integrated flow.
- *CTO acceptance criteria:* Confirmed each Section 8 criterion has CTO Verification (Section 7) evidence; no criterion left Developer-Evidence-only.
- *Excluded work:* Any new functionality or scope beyond what WP-00 through WP-12 already deliver — this package validates, it does not build.

**WP-14 — MVP Acceptance**
- *Objective:* Formal CTO acceptance of the Kyron7 Deployment Agent MVP as complete, per Section 8.
- *Architectural requirement implemented:* Section 8 (MVP Completion Criteria), derived in full from the approved architecture documents.
- *Dependencies:* WP-13.
- *Expected deliverables:* A formal MVP Acceptance record confirming all Section 8 criteria are met.
- *CTO acceptance criteria:* CTO issues MVP Acceptance only once WP-13's validation evidence confirms every Section 8 criterion.
- *Excluded work:* Any implementation, deployment, or scope addition — this package is a governance sign-off stage only.

## 6. Review Gates

Every work package passes through the same gate sequence before it may be committed:

```
Developer completion
      ↓
CTO Review
      ↓
APPROVED
      ↓
Commit
      ↓
Deployment Policy
      ↓
Deployment
```

- **Developer completion:** the work package's deliverables and acceptance criteria (Section 5) are met and evidence (Section 7) is assembled.
- **CTO Review:** the CTO reviews the work package's deliverables and evidence against its stated architectural requirement.
- **APPROVED:** required before any commit. No work package's code may be committed without an explicit CTO APPROVED, consistent with ADR-003's review stage and this project's standing workflow.
- **Commit:** the approved work package is committed to the new repository.
- **Deployment Policy:** any deployment of committed work — as distinct from committing the work package's code — is itself subject to the Policy Engine's classification and, where high-risk, Founder Console approval, per the approved architecture. This applies to deploying the Deployment Agent MVP's own implementation, not only to deployments the finished MVP will later manage.
- **Deployment:** occurs only after the Deployment Policy gate above is satisfied. No deployment occurs during implementation planning or during the implementation work packages themselves.

## 7. Evidence Required

For every work package, the following evidence stages must accompany the CTO Review step (Section 6). These are implementation governance stages, distinct from the product's own Trust Model (Architecture Specification §8), which remains Reported and Verified only and is not altered by this section.

```
Developer Evidence
      ↓
CTO Verification
      ↓
Ready for Commit
```

- **Developer Evidence:** a description, provided by the implementer, of what was built and how it satisfies the work package's acceptance criteria. Available immediately, not independently confirmed.
- **CTO Verification:** confirmation, independent of the implementer's own report, that the deliverable meets its acceptance criteria — the CTO's own review of the delivered work against the cited architectural requirement.
- **Ready for Commit:** the state a work package reaches once CTO Verification is complete and APPROVED (Section 6) has been given. A work package may not be marked Ready for Commit while any of its acceptance criteria have not undergone CTO Verification.

## 8. MVP Completion Criteria

The Kyron7 Deployment Agent MVP implementation is complete when, and only when:

- WP-00 through WP-14 have each individually reached APPROVED per Section 6.
- The end-to-end flow integrated in WP-12 and validated in WP-13 matches Architecture Specification §7 in full, with no deviation.
- A low-risk deployment has been demonstrated proceeding automatically, with no manual command and no user interaction.
- A high-risk deployment has been demonstrated halting for, and proceeding only after, Founder Console approval.
- A rollback has been demonstrated occurring according to a Policy Engine determination, not as hardcoded Deployment Agent behavior.
- Both a Reported outcome and a Verified outcome have been demonstrated, with the Deployment Agent itself never assigning Verified status.
- An audit trail entry has been demonstrated for every decision point and action in the flow.
- All implementation work resides in the new repository established under ADR-005, with no dependency on the old `kyron7-operations-agent` repository's code, types, or identifiers.
- WP-14 (MVP Acceptance) has been issued, confirming all criteria in this section are met.

## 9. Out of Scope

Restated from the approved architecture documents; not expanded:

- Additional products beyond the initial target (Architecture Specification §10).
- Founder Console capabilities beyond deployment approval (Architecture Specification §3, §10).
- Any interface for authoring or editing Policy Engine rules (Architecture Specification §10; Policy Engine Specification §7).
- Multi-environment, multi-region, or multi-cloud deployment orchestration (Architecture Specification §10).
- Integration with monitoring, incident-management, or alerting systems (Architecture Specification §10).
- Any trust state beyond Reported and Verified (Architecture Specification §8, §10; Policy Engine Specification §7; Execution Specification §7).
- Broader Kyron7 OS platform rollout beyond the Deployment Agent module itself (Architecture Specification §10).
- Any component beyond the five approved components — Deployment Agent, Policy Engine, Founder Console, GitHub, ODS Vault.
- Creation of the new repository itself, and any code, commit, push, or deployment — all excluded from this planning document.
