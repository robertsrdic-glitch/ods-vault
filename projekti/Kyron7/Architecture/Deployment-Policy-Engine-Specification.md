# Kyron7 Deployment Policy Engine Specification

**Type:** Specification
**Status:** Approved
**Date:** 2026-07-18
**Depends on:** Kyron7 Deployment Agent MVP — Architecture Specification; ADR-001; ADR-002; ADR-003; ADR-004

---

## 1. Purpose

The Policy Engine exists so that deployment classification and rollback determinations are policy-driven rather than hardcoded into the Deployment Agent. Per the Architecture Specification, the Deployment Agent orchestrates and executes but does not itself decide whether a deployment is low-risk or high-risk, or whether a failed outcome calls for rollback — those determinations belong to the Policy Engine. The Policy Engine is what allows the Deployment Agent to remain a pure orchestrator and executor.

## 2. Responsibility

The Policy Engine is responsible for:

- Holding the Deployment Policy that governs risk classification and rollback behavior.
- Classifying each candidate deployment as low-risk or high-risk.
- Being the sole source of the automatic-vs-manual-approval determination.
- Deriving its rules from the architecture and deployment policy documentation recorded in ODS Vault.

The Policy Engine is **not** responsible for:

- Orchestrating or executing any deployment — that is the Deployment Agent's responsibility.
- Executing rollback — the Deployment Agent executes rollback according to the Deployment Policy the Policy Engine holds; the Policy Engine does not carry it out.
- Providing the Founder approval interface — that is the Founder Console's responsibility.
- Originating, storing, or tracking deployable artifacts — that is GitHub's responsibility.
- Authoring or maintaining architecture or deployment policy documentation — that is ODS Vault's responsibility; the Policy Engine consumes that documentation, it does not produce it.
- Determining whether a deployment outcome becomes Verified — per the Trust Model, that determination is made through verification, independent of the Deployment Agent, and is likewise outside the Policy Engine's responsibility.

## 3. Inputs

Conceptually, the Policy Engine evaluates:

- The characteristics of a candidate deployment relevant to determining its risk, traceable back to the deployable artifact in GitHub.
- The applicable Deployment Policy, as derived from the architecture and deployment policy documentation recorded in ODS Vault.
- For rollback determinations, information about a deployment's execution or verification outcome.

This specification does not define what those characteristics or policy rules are; individual policy rules are out of scope here.

## 4. Outputs

Conceptually, the Policy Engine returns:

- A risk classification for a candidate deployment (low-risk or high-risk), which determines whether the Deployment Agent proceeds automatically or must await Founder approval.
- A rollback determination, per Deployment Policy, for a failed or unverified deployment outcome, which the Deployment Agent then executes.

No implementation, format, or mechanism for returning these outcomes is defined here.

## 5. Architectural Constraints

The following constraints, already established by the approved Architecture Specification and ADR-001 through ADR-004, apply to the Policy Engine:

- **From the Architecture Specification:** The Policy Engine is the sole source of the automatic-vs-manual-approval decision; the Deployment Agent does not make this determination itself. Deployment classifications and approval requirements are policy-driven, not hardcoded into the Deployment Agent. The Policy Engine derives its rules from the architecture and deployment policy documentation recorded in ODS Vault, rather than embedding them ad hoc.
- **From ADR-001:** As part of the Deployment Agent's platform module, the Policy Engine must be designed generically enough to be reused by future Kyron7 products, not retrofitted later.
- **From ADR-002:** No AI agent may expose or consume the high-risk approval mechanism. The Policy Engine's classification determines whether Founder Console approval is required, but the Policy Engine does not itself expose or consume that approval mechanism.
- **From ADR-003:** Hermes's role remains limited to deployment execution and production verification, not architecture, implementation, or review.
- **From ADR-004:** The Policy Engine, as part of the Deployment Agent MVP, is designed as a platform capability, not a product-specific tool.

## 6. Relationship to Other Components

**Deployment Agent** — requests a risk classification from the Policy Engine before acting, and executes according to that classification. For failure or unverified outcomes, the Deployment Agent consults the Policy Engine's Deployment Policy to determine rollback and then executes it. The Policy Engine does not orchestrate or execute; the Deployment Agent does.

**Founder Console** — is not consulted or invoked by the Policy Engine directly. A high-risk classification from the Policy Engine is what causes the Deployment Agent to route a candidate deployment to the Founder Console for approval. The Founder's approval decision itself is made in the Founder Console, not the Policy Engine.

**GitHub** — is the authoritative source of the deployable artifact that constitutes a candidate deployment. The Policy Engine evaluates characteristics of that candidate deployment but does not originate, store, or modify artifacts in GitHub.

**ODS Vault** — is the authoritative source of the architecture and deployment policy documentation the Policy Engine derives its rules from. The Policy Engine consumes this documentation; it is not itself a store of architectural decisions, and ODS Vault is not a runtime component the Policy Engine executes against.

## 7. Non-Goals

The Policy Engine specification explicitly excludes:

- Defining concrete policy rules or the criteria that make a deployment low-risk or high-risk.
- Any implementation, code, or pseudocode describing how classification or rollback determination is carried out.
- Executing deployments or rollbacks.
- Providing any Founder-facing interface or approval mechanism.
- Originating, storing, or tracking deployable artifacts.
- Authoring or maintaining architecture or deployment policy documentation.
- Determining Verified/Reported trust states for deployment outcomes.
- Introducing any architectural component beyond the Deployment Agent, Founder Console, GitHub, ODS Vault, and the Policy Engine itself, as established by the approved Architecture Specification.
