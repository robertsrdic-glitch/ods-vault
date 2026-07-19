# Kyron7 Deployment Agent MVP — Architecture Specification

**Type:** Architecture Specification
**Status:** Approved
**Date:** 2026-07-18
**Depends on:** ADR-001, ADR-002, ADR-003, ADR-004

---

## 1. Purpose

The Kyron7 Deployment Agent exists to automate the routine orchestration of deployments that are currently performed manually and mediated by Hermes. Per ADR-004, this manual, Hermes-mediated deployment work is a recurring operating expense; the Deployment Agent's purpose is to eliminate or substantially reduce that recurring cost.

Within Kyron7, the Deployment Agent's responsibility is to orchestrate the deployment flow for a given candidate deployment — executing according to the classification produced by the Policy Engine, and according to the Founder's decision when Founder Console approval is required — and to ensure every deployment outcome is handled according to Deployment Policy. It is a cross-cutting infrastructure capability, not a feature of any single product.

## 2. Goals

The MVP's goals are limited to:

- Execute low-risk deployments automatically, with no manual deployment command and no user interaction required.
- Require explicit manual Founder approval, via the Founder Console, before any high-risk deployment proceeds.
- Apply rollback according to Deployment Policy when a deployment fails, rather than as hardcoded Deployment Agent behavior.
- Maintain an audit trail of deployment actions and outcomes, as an architectural requirement of the platform.
- Ensure every low-risk/high-risk classification is produced by the Policy Engine according to policy, not hardcoded into the Deployment Agent.
- Be designed as the first reusable Kyron7 platform module (ADR-001), not as a NorthStar-specific tool, even though its MVP execution scope is limited to a single initial product.

## 3. Non-Goals

The MVP explicitly does not attempt to:

- Be a general-purpose CI/CD platform.
- Provide a user interface for authoring, editing, or managing policy rules.
- Replace GitHub as the authoritative source of deployable artifacts.
- Replace ODS Vault as the authoritative source of architecture and deployment policy documentation.
- Take on production-verification responsibilities beyond what Deployment Policy requires for a deployment's outcome to become Verified.
- Support more than one product's deployments in its initial execution scope, even though its design must remain generic enough to be reused by future products.
- Introduce any Founder-facing capability beyond high-risk deployment approval.

## 4. Scope

The MVP covers:

- Deployment automation for the initial target product (the system currently receiving manual, Hermes-mediated deployments).
- Policy-driven classification of a candidate deployment as low-risk or high-risk.
- An automatic execution path for low-risk deployments.
- A manual approval path for high-risk deployments, routed through the Founder Console.
- Rollback on deployment failure, applied according to Deployment Policy.
- Audit trail recording of deployment actions and outcomes, required at the platform level.
- Conceptual integration points with GitHub (authoritative source of deployable artifacts) and ODS Vault (authoritative source of architecture and deployment policy documentation the Policy Engine enforces).

Everything not listed above is out of scope for this MVP (see Section 10).

## 5. High-Level Architecture

The Deployment Agent is a platform-level orchestrator positioned between the source of a candidate change and the running product infrastructure it deploys to.

For every candidate deployment, the Deployment Agent consults the Policy Engine to obtain a risk classification. Low-risk deployments proceed through the automatic execution path without human involvement. High-risk deployments are held pending Founder approval through the Founder Console rather than proceeding automatically. In both cases, the Deployment Agent executes according to the Policy Engine's classification and, where required, the Founder's approval decision.

Deployment outcomes are recorded in two stages, consistent with the project's trust model: the Deployment Agent reports an outcome as Reported at the time an action completes, and verification independently determines whether that outcome becomes Verified. A failed execution, or a Reported outcome that fails to reach Verified, triggers rollback according to Deployment Policy.

Every decision point and action — classification, execution, approval request, approval decision, rollback, and final outcome — produces an audit trail entry, as an architectural requirement of the platform. Policy rules enforced by the Policy Engine are grounded in the architecture and deployment policy documentation recorded in ODS Vault, rather than being embedded ad hoc in the Deployment Agent.

## 6. Responsibilities

**Deployment Agent**
- Orchestrates the end-to-end deployment flow for a candidate change.
- Requests a risk classification from the Policy Engine before acting.
- Executes deployments according to the Policy Engine's classification — automatically for low-risk deployments.
- Halts and awaits Founder approval through the Founder Console for high-risk deployments; does not proceed until that approval is given.
- Executes rollback according to Deployment Policy on failure or failed verification.
- Records audit trail entries for every action.
- Reports deployment outcomes as Reported; does not itself determine whether an outcome becomes Verified — that determination is made through verification, independent of the Deployment Agent.

**Policy Engine**
- Holds the Deployment Policy that governs risk classification and rollback behavior.
- Classifies each candidate deployment as low-risk or high-risk.
- Is the sole source of the automatic-vs-manual-approval decision; the Deployment Agent does not make this determination itself.
- Derives its rules from the architecture and deployment policy documentation recorded in ODS Vault.

**Founder Console**
- Serves as the approval channel for high-risk deployments, per ADR-002.
- Is Cloudflare Access-protected and checks the Founder's identity against the Founder allowlist.
- Is where the Founder's approve or reject decision on a high-risk deployment is made. No AI agent exposes or consumes this approval mechanism, consistent with ADR-002.
- Does not participate in deployment decision logic; it provides only the Founder approval interface.

**GitHub**
- Is the authoritative source of deployable artifacts.
- Is where the deployable change originates and is tracked.

**ODS Vault**
- Is the authoritative source of architecture and deployment policy documentation that inform the Policy Engine's rules.
- Is not a runtime execution component of the deployment flow.

## 7. Deployment Flow

1. A candidate deployable artifact becomes available in GitHub.
2. The Deployment Agent identifies the candidate deployment and requests a classification from the Policy Engine.
3. The Policy Engine classifies the candidate as low-risk or high-risk based on Deployment Policy grounded in ODS Vault's architecture and deployment policy documentation.
4. If low-risk: the Deployment Agent executes automatically, according to the Policy Engine's classification, with no manual command or user interaction.
5. If high-risk: the Deployment Agent halts and raises the candidate for Founder approval through the Founder Console.
6. The Founder reviews and approves or rejects the candidate in the Founder Console.
7. On approval, the Deployment Agent executes accordingly. On rejection, the deployment does not proceed, and this outcome is recorded in the audit trail.
8. Following execution, the Deployment Agent reports the outcome as Reported. Verification then determines whether the outcome becomes Verified.
9. If execution fails, or a Reported outcome cannot be confirmed as Verified, rollback is triggered according to Deployment Policy.
10. Every step above — classification, execution, approval request, approval decision, rollback, and final outcome — is recorded in the audit trail.

## 8. Trust Model

The MVP recognizes exactly two trust states for a deployment outcome:

- **Reported** — the outcome as stated by the Deployment Agent at the time an action completed. The Deployment Agent reports outcomes; it does not assign trust states.
- **Verified** — the outcome after independent confirmation, separate from the Deployment Agent's own report. Verification, not the Deployment Agent, determines whether an outcome becomes Verified.

A deployment is not considered successfully complete until its outcome reaches Verified. A Reported outcome that cannot be confirmed as Verified is treated as a failure and rollback is triggered according to Deployment Policy. No additional trust states are defined for the MVP.

## 9. Constraints

The following constraints carry forward from existing ADRs and from approved deployment policy, and govern this architecture:

- **From ADR-001:** The Deployment Agent must be designed generically enough to be reused by future Kyron7 products, as the first reusable Kyron7 platform module, not retrofitted later. The initial product's own repository and release cycle remain scoped to product functionality; the Deployment Agent's work is tracked separately as platform infrastructure.
- **From ADR-002:** No AI agent may expose or consume the high-risk approval mechanism. Approval identity must be Cloudflare Access-authenticated and checked against the Founder allowlist. Routine approval operation must not depend on Hermes.
- **From ADR-003:** Hermes's role is limited to deployment execution and production verification, not architecture, implementation, or review. This specification is itself the Architecture-stage output in that workflow.
- **From ADR-004:** The Deployment Agent MVP is designed as a platform capability per ADR-001, not a product-specific tool. Its sequencing precondition — completion of the gateway security work (Security Sprint 1C / 1C.1) — is treated as satisfied per current CTO direction, with the Production Validation Baseline (commit `8efcc42e1c9b09466590b4735bbb2cb70b0e1851`) as the completed milestone.
- **From approved deployment policy:** Deployment classifications and approval requirements are policy-driven, not hardcoded into the Deployment Agent. Low-risk deployments execute automatically with no user interaction and no manual deployment command. High-risk changes require manual Founder approval, through the Founder Console, before deployment. Rollback on failure occurs according to Deployment Policy. An audit trail is required as an architectural requirement of the platform.

## 10. Out of Scope

The following belong to future phases, not this MVP:

- Extending the Deployment Agent's execution scope to additional Kyron7 products beyond the initial target.
- The Founder Console's broader control-center capabilities (products, agents, incidents, analytics, administrative actions) beyond deployment approval.
- Any interface for authoring or editing Policy Engine rules.
- Multi-environment, multi-region, or multi-cloud deployment orchestration.
- Integration with monitoring, incident-management, or alerting systems.
- Any trust state beyond Verified and Reported.
- Broader Kyron7 OS platform rollout beyond the Deployment Agent module itself.
