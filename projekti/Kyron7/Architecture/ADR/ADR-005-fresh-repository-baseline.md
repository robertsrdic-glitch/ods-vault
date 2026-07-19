# ADR-005: Fresh Repository Baseline for Deployment Agent MVP

**Status:** Accepted
**Date:** 2026-07-18

## Context

The Repository Reconciliation Report (`Repository-Reconciliation-Report.md`) compared the existing `kyron7-operations-agent` repository against the approved Deployment Agent MVP Architecture Specification, Policy Engine Specification, and Execution Specification. The report's Final Recommendation was **BLOCKED**.

The repository's only substantial existing work — the `ExecutionPlan` contract (commit `7582f14`, "IMP-001: Execution Plan contract (TS-003)") — depends on components with no approved equivalent (a Capability Registry, a Plan Store), models risk as an open-ended scale rather than the approved binary low-risk/high-risk classification, models approval without any tie to the Founder Console or Cloudflare Access identity required by ADR-002, and treats execution as a distinct forward-referenced module rather than the Deployment Agent's own responsibility as established by the approved Execution Specification. The repository's own documentation (`docs/contracts/execution-plan.md`, `README.md`) cites an architectural authority, "TS-003," that does not exist anywhere in ODS Vault.

Reconciling the existing repository in place would require, at minimum, a High-impact rework of its core contract (per the report's Migration Impact table), alongside multiple Medium- and Low-impact corrections, before it could serve as a trustworthy implementation baseline.

## Decision

Kyron7 Deployment Agent MVP implementation proceeds in a **new, clean repository**, established solely from the approved architecture: the Deployment Agent MVP Architecture Specification, the Deployment Policy Engine Specification, the Deployment Execution Engine Specification, and ADR-001 through ADR-004.

The existing `kyron7-operations-agent` repository is retained only as historical reference. It does not influence architecture or implementation planning going forward.

## Consequences

- The Repository Reconciliation Report's cleanup plan (Section 5) is superseded; no further reconciliation work is required against `kyron7-operations-agent`.
- All new implementation work for the Deployment Agent MVP occurs in a new repository, built fresh from the approved architecture rather than carrying forward the old repository's existing code, types, component references (Capability Registry, Plan Store), lifecycle states, or TS-/ECR-/IMP-series identifiers.
- The old repository's history and documentation remain available for reference but carry no architectural authority. Any future reuse of concepts from it must be re-derived from and validated against the approved architecture, not assumed compatible.
- Implementation planning (Sprint 4) may proceed against a fresh-repository baseline rather than the repository blocked by the Reconciliation Report.
