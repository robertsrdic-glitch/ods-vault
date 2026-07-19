# Kyron7 Deployment Agent — Dashboard

Status: Current
Date: 2026-07-19

Central entry point into the Kyron7 Deployment Agent knowledge base. Links to every Architecture, Engineering, and Implementation document for this project.

---

## 00 Dashboard

- [[Kyron7 Project Health]]
- [[Kyron7 Quick Links]]

## Architecture

- [[Deployment-Agent-MVP-Architecture-Specification|Deployment Agent MVP — Architecture Specification]]
- [[Deployment-Execution-Engine-Specification|Deployment Execution Engine Specification]]
- [[Deployment-Policy-Engine-Specification|Deployment Policy Engine Specification]]
- [[Repository-Reconciliation-Report|Repository Reconciliation Report]] — Superseded by ADR-005; findings retained as historical record

### Architecture Decision Records (ADR-001 – ADR-013)

- [[ADR-001-separate-product-and-platform|ADR-001 — Separate Product and Platform]]
- [[ADR-002-founder-console-replaces-telegram-approval|ADR-002 — Founder Console Replaces Telegram Approval]]
- [[ADR-003-ai-engineering-workflow-v2|ADR-003 — AI Engineering Workflow v2]]
- [[ADR-004-kyron7-deployment-agent-priority|ADR-004 — Kyron7 Deployment Agent Priority]]
- [[ADR-005-fresh-repository-baseline|ADR-005 — Fresh Repository Baseline]]
- [[ADR-006-Technology-Stack-Selection|ADR-006 — Technology Stack Selection]] — **Proposed, not yet Approved** (see [[Kyron7 Project Health|Project Health]])
- [[ADR-007-Deployment-Risk-Classification-Rules|ADR-007 — Deployment Risk Classification Rules]] — **Proposed, not yet Approved** (see [[Kyron7 Project Health|Project Health]])
- [[ADR-008-MVP-Deployment-Execution-Outcome|ADR-008 — MVP Deployment Execution Outcome]]
- [[ADR-009-MVP-High-Risk-Deployment-Outcome|ADR-009 — MVP High-Risk Deployment Outcome]]
- [[ADR-010-Deployment-Agent-Owns-Lifecycle-Policy-Engine-Owns-Policies|ADR-010 — Deployment Agent Owns Lifecycle, Policy Engine Owns Policies]]
- [[ADR-011-Independent-Rollback-Decision-Model|ADR-011 — Independent Rollback Decision Model]]
- [[ADR-012-Verification-Ownership-Model|ADR-012 — Verification Ownership Model]]
- [[ADR-013-Deployment-Lifecycle-Outcome-Represents-Complete-Lifecycle|ADR-013 — Deployment Lifecycle Outcome Represents Complete Lifecycle]]

## Engineering

- [[Kyron7 Engineering Standard v1.0]]

## Implementation

- [[Deployment-Agent-MVP-Implementation-Plan|Deployment Agent MVP — Implementation Plan]] — governs WP-00 through WP-14. WP-01 through WP-11 (excluding WP-12/13/14) are documented inline in this plan's §5 and have no separate files — intentional, not a gap.
- [[Project-Closure-Report|Project Closure Report — Design & Build Phase]]
- [[WP-00-Development-Environment-Bootstrap|WP-00 — Development Environment Bootstrap]]
- [[WP-12A-DeploymentLifecycleOutcome-Refactoring|WP-12A — DeploymentLifecycleOutcome Refactoring]]
- [[WP-12B-DeploymentLifecycleOutcome-Implementation|WP-12B — DeploymentLifecycleOutcome Implementation]] — superseded by WP-12C
- [[WP-12C-Contract-Compliance-Correction|WP-12C — Contract Compliance Correction]] — final WP-12 implementation
- [[WP-13-System-Validation|WP-13 — System Validation]]
- [[WP-14-Design-Acceptance|WP-14 — Design Acceptance]]
- [[Pilot-Deployment-Validation-Plan|Pilot Deployment Validation Plan]] — Operationalization phase entry point, planned, not yet executed

## Implementation Repository

- Repository: `Kyron7/deployment-agent` (local: `C:\Users\rober\Projects\deployment-agent`)
- HEAD at closure: `a26c410` (WP-13A)
- No GitHub remote configured yet — nothing pushed

## 99 Archive

Empty. Superseded material is moved here, never deleted.
