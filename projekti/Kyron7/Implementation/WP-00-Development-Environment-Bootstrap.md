# WP-00 — Development Environment Bootstrap

**Type:** Work Package Execution Plan
**Status:** Approved — Implemented (commit `2844a85`)
**Date:** 2026-07-18
**Parent document:** Kyron7 Deployment Agent MVP — Implementation Plan, Section 5, WP-00
**Depends on:** ADR-005 (Fresh Repository Baseline); Implementation Plan §4 (Repository Bootstrap — Governance)

This document is the execution plan for WP-00 only. It does not change architecture, scope, or any approved document.

---

## 1. Objectives

- Prepare the development environment for the Kyron7 Deployment Agent MVP repository, per Implementation Plan WP-00.
- Establish tooling, formatting, linting, a CI skeleton, and a documentation bootstrap before any architecture-aligned repository structure (WP-01) or business logic (WP-02 onward) is created.
- Apply the governance decisions already recorded in Implementation Plan §4 (official repository name, default branch strategy, versioning strategy, coding standards, documentation conventions) — this document does not redecide them.

## 2. Scope

In scope for WP-00, per the Implementation Plan:

- Repository initialization at the tooling/configuration level only.
- Selection and configuration of development tooling, a formatter, and a linter.
- A CI skeleton that enforces formatting, linting, and type-checking.
- A documentation bootstrap that points to the authoritative ODS Vault documents.

Out of scope is addressed in full in Section 11.

## 3. Deliverables

- An initialized repository under the official name established in Implementation Plan §4 (`Kyron7/deployment-agent`), on a single default branch (`main`).
- Formatter and linter configuration, enforced consistently across the repository.
- A CI skeleton that runs formatting, linting, and type-checking on every push and pull request.
- A documentation bootstrap (README and pointer documentation) stating that architecture is authoritative in ODS Vault, not restated in the repository.

## 4. Acceptance Criteria

- Confirmed no business logic, deployment logic, Policy Engine, or Deployment Agent content exists in this package — environment and tooling only, per Implementation Plan WP-00.
- Confirmed the repository is initialized under the official name and branch strategy in Implementation Plan §4, with no directory structure aligned to the five approved components yet (that is WP-01).
- Confirmed formatting and linting are enforced automatically, not left to individual contributor discretion.
- Confirmed the CI skeleton runs on every push and pull request and contains no deployment step.
- Confirmed the documentation bootstrap references ODS Vault by pointer only, with no restatement of architecture content, correcting the pattern the Repository Reconciliation Report identified as a conflict in the old repository.
- This work package follows the evidence and review process defined in Implementation Plan §6 (Review Gates) and §7 (Evidence Required): Developer Evidence, then CTO Verification, before it may be marked Ready for Commit.

## 5. Repository Initialization Approach

The repository `Kyron7/deployment-agent` is initialized fresh, per ADR-005, with no code, types, or identifiers carried over from the old `kyron7-operations-agent` repository. Initialization at this stage consists of: the repository shell itself, a single default branch (`main`) per Implementation Plan §4's branch strategy, and the tooling/configuration described in Sections 6–9 below. No directory structure aligned to the Deployment Agent, Policy Engine, or integration points is created here — that structure is WP-01's responsibility.

## 6. Development Tooling

WP-00 prepares the development environment independently of the final implementation technology. The runtime, implementation language, package management, formatter, linter, and testing framework will follow the technology stack selected through the project's approved architecture decision process — none of these are selected by WP-00.

- **Runtime/language:** not selected by WP-00; determined by the approved technology stack.
- **Package management:** will follow the approved technology stack.
- **Testing framework:** a testing framework placeholder may be prepared, but no framework is selected by WP-00; no test suites are written at this stage, since no business logic exists yet to test (Policy Engine and Deployment Agent logic begin at WP-02 and WP-04).

## 7. Formatting Strategy

A single, repository-wide automated formatter configuration is established and applied consistently across all files. Formatting is checked in CI (Section 9) as a blocking check, so no manually-formatted or inconsistently-formatted contribution can be merged. No per-contributor or per-directory formatting variation is permitted.

## 8. Linting Strategy

A linter appropriate to the approved technology stack is configured to catch structural and, where the stack supports it, type-level issues, consistent with the coding standards recorded in Implementation Plan §4. The specific linter is not selected by WP-00. Linting is enforced in CI (Section 9) as a blocking check. No lint rule encodes deployment policy, risk classification, or any other business logic — the linter's scope is code quality only.

## 9. CI Skeleton

A CI pipeline (consistent with GitHub as the architecture's authoritative source of deployable artifacts, per Architecture Specification §6) runs on every push and pull request:

- Formatting check (Section 7).
- Linting check (Section 8).
- Type-check, where the approved technology stack includes static typing.

The CI skeleton established here contains no deployment step and no test execution beyond the empty scaffold in Section 6. Deployment remains gated by Implementation Plan §6 (Review Gates) and the approved architecture's Deployment Policy, and is out of scope for WP-00 in every respect (see Section 11).

## 10. Documentation Bootstrap

The repository's initial documentation consists of:

- A README stating that architecture, specifications, and ADRs are authoritative in ODS Vault (Architecture Specification, Policy Engine Specification, Execution Specification, ADR-001 through ADR-005, and the Implementation Plan) and are not restated in this repository.
- A documentation pointer area (established structurally here; populated with real pointers as later work packages land) that references the ODS Vault documents by path rather than duplicating their content.

This directly corrects the conflict the Repository Reconciliation Report identified in the old repository, where `docs/contracts/execution-plan.md` and `README.md` cited an architectural authority ("TS-003") that did not exist in the vault.

## 11. Out of Scope

Restated from Implementation Plan WP-00's excluded work; not expanded:

- Repository directory structure aligned to the five approved components (Deployment Agent, Policy Engine, Founder Console, GitHub, ODS Vault) — that is WP-01.
- Any Deployment Agent logic or orchestration behavior.
- Any Policy Engine logic, including risk classification or Deployment Policy content.
- Any GitHub or Founder Console integration logic.
- Any execution, rollback, trust-model (Reported/Verified), or audit trail logic.
- Any application code of any kind.
- Creation of the repository itself — this document is planning only; the repository is not created by it.
- Any commit, push, or deployment.
