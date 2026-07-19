# Kyron7 Deployment Execution Engine Specification

**Type:** Specification
**Status:** Approved
**Date:** 2026-07-18
**Depends on:** Kyron7 Deployment Agent MVP — Architecture Specification; Kyron7 Deployment Policy Engine Specification; ADR-001; ADR-002; ADR-003; ADR-004

**Scope note:** This document elaborates the execution responsibility already assigned to the Deployment Agent in the approved Architecture Specification. "Execution Engine" here refers to that execution responsibility, not a separate architectural component alongside the Deployment Agent. The Architecture Specification recognizes exactly five components — Deployment Agent, Policy Engine, Founder Console, GitHub, ODS Vault — and this document does not add a sixth.

---

## 1. Purpose

Execution exists because the Deployment Agent must carry out a deployment — and, when required, its rollback — according to determinations made outside itself: the classification produced by the Policy Engine, and, for high-risk deployments, the Founder's approval given through the Founder Console. This document exists to describe that execution responsibility in more depth than the Architecture Specification's high-level summary, without introducing a new component to hold it.

## 2. Responsibility

The Deployment Agent's execution responsibility covers:

- Carrying out a deployment once the Policy Engine has classified it as low-risk, or once Founder approval has been given for a high-risk deployment.
- Carrying out rollback according to Deployment Policy when execution fails or an outcome fails to reach Verified.
- Reporting the outcome of an execution or rollback action as Reported, without determining Verified status itself.
- Producing the record of each execution and rollback action required for the audit trail.

It does **not** cover:

- Classifying a deployment as low-risk or high-risk — that is the Policy Engine's responsibility.
- Determining whether a deployment requires Founder approval — also the Policy Engine's classification.
- Providing the Founder approval interface — that is the Founder Console's responsibility.
- Originating, storing, or tracking deployable artifacts — that is GitHub's responsibility.
- Authoring or maintaining architecture or deployment policy documentation — that is ODS Vault's responsibility.
- Determining whether a Reported outcome becomes Verified — per the Trust Model, that determination is made through verification, independent of the Deployment Agent.
- Making the automatic-vs-manual-approval decision — that remains the Policy Engine's sole responsibility.

## 3. Inputs

Conceptually, before execution proceeds, it depends on:

- The candidate deployable artifact, sourced from GitHub.
- The classification already produced by the Policy Engine (low-risk or high-risk).
- For high-risk deployments, the Founder's approval decision, given through the Founder Console.
- The applicable Deployment Policy governing rollback behavior, as held by the Policy Engine.

No implementation detail about how these inputs are obtained or represented is defined here.

## 4. Outputs

Conceptually, execution produces:

- A Reported outcome following a deployment action.
- A Reported outcome following a rollback action, when rollback is triggered.
- The information recorded in the audit trail for each action performed.

No implementation, format, or mechanism for producing these outputs is defined here.

## 5. Architectural Constraints

The following constraints, already established by the approved Architecture Specification, the approved Deployment Policy Engine Specification, and ADR-001 through ADR-004, apply to execution:

- **From the Architecture Specification:** The Deployment Agent executes low-risk deployments automatically, with no manual command and no user interaction. It executes high-risk deployments only after Founder approval through the Founder Console. It executes rollback according to Deployment Policy on failure or failed verification. It reports outcomes as Reported and does not itself determine whether an outcome becomes Verified. It records audit trail entries for every action.
- **From the Deployment Policy Engine Specification:** The Policy Engine is the sole source of classification and of the Deployment Policy governing rollback; execution follows those determinations rather than originating them.
- **From ADR-001:** Execution, as part of the Deployment Agent's platform module, must be designed generically enough to be reused by future Kyron7 products, not retrofitted later.
- **From ADR-002:** No AI agent may expose or consume the high-risk approval mechanism; execution of a high-risk deployment must wait on Founder Console approval rather than proceeding independently.
- **From ADR-003:** Hermes's role remains limited to deployment execution and production verification, not architecture, implementation, or review.
- **From ADR-004:** The Deployment Agent MVP, including its execution responsibility, is designed as a platform capability, not a product-specific tool.

## 6. Relationship to Other Components

Execution, as described in this document, is carried out by the Deployment Agent itself — the Architecture Specification's sole executing component. This section describes how that execution responsibility relates to the other approved components.

**Policy Engine** — supplies the classification and the Deployment Policy that execution acts on. Execution does not classify deployments or determine policy itself; it carries out what the Policy Engine has already determined.

**Founder Console** — for high-risk deployments, execution does not proceed until Founder approval has been given through the Founder Console. The Founder Console's approval decision is a precondition for execution, not something execution participates in.

**GitHub** — is the authoritative source of the deployable artifact that execution acts on. Execution does not originate, store, or modify artifacts in GitHub.

**ODS Vault** — is not consulted directly during execution. Execution follows the Deployment Policy the Policy Engine derives from the architecture and deployment policy documentation recorded in ODS Vault.

## 7. Non-Goals

This specification explicitly excludes:

- Introducing a new architectural component distinct from the Deployment Agent.
- Any implementation, code, or pseudocode describing how execution or rollback is carried out.
- Classifying deployments or determining approval requirements.
- Providing any Founder-facing interface.
- Determining whether an outcome becomes Verified.
- Originating, storing, or tracking deployable artifacts.
- Authoring or maintaining architecture or deployment policy documentation.
