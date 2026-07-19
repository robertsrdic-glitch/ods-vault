# ADR-012 — Verification Ownership Model

**Status:** Approved
**Date:** 2026-07-19

## 1. Status

Approved.

## 2. Context

The WP-11 Verification Ownership Consistency Check established, from the approved architecture alone, that no component currently owns independent verification. Specifically, and only:

- Architecture Specification §6 excludes the Deployment Agent from determining Verified status but names no replacement.
- Deployment Execution Engine Specification §2 and Deployment Policy Engine Specification §2 each exclude verification from their own component while breaking their own otherwise-consistent practice of attributing every other exclusion to a named component.
- Architecture Specification §7 step 8 is normative as to sequence ("Verification then determines whether the outcome becomes Verified" must occur after reporting) but silent as to actor.
- ADR-011 §11 (Explicit Non-Decisions) explicitly states the verification signal's source and mechanism remain "still WP-11's territory" — the architecture's own most recent statement confirms the gap rather than resolving it.

This is the entire, proven problem this ADR exists to resolve: who owns independent verification, conceptually, within the already-approved five-component architecture.

## 3. Decision

**Ownership of independent verification** is split between two distinct responsibilities, neither of which introduces a new component:

- **Lifecycle responsibility** for verification belongs to the Deployment Agent. This is not a new assignment; it is the direct application of ADR-010's already-settled principle that the Deployment Agent is "the sole authoritative owner of lifecycle sequencing and transitions... in every phase, present and future" to the one phase that principle had not yet been explicitly applied to.
- **The verification determination itself** — the independent confirmation that produces the Verified/not-yet-Verified fact — is not performed by the Deployment Agent, the Policy Engine, or any of the other three named components in their existing responsibilities. It is produced by an independent verification mechanism that is conceptually external to the responsibilities of the five architectural components, while remaining part of the overall deployment architecture, in the same relationship the already-approved architecture already establishes between the Deployment Agent and the undefined mechanism behind its existing execution-type boundaries (ADR-008 §12: "the same relationship WP-06 and WP-07 already established"). This mechanism is not a sixth architectural component — it occupies the same conceptual position as the undefined infrastructure behind any of this architecture's existing boundaries: unnamed, unspecified, and outside the set of five components with named responsibilities in the deployment flow.

**Initiation responsibility** belongs to the Deployment Agent. Verification cannot be an independently self-initiated process outside Deployment Agent sequencing, because that would require some actor other than the Deployment Agent to advance the lifecycle — directly contradicting ADR-010 §5's binding statement that "lifecycle transitions belong exclusively to the Deployment Agent, in every phase, present and future" and that other components "may observe or report lifecycle state, but they do not own or advance it." The Deployment Agent decides when a Reported outcome is checked and what happens with the result; it does not decide, and does not fabricate, what the result is.

**Relationship to the Deployment Agent:** the Deployment Agent consults the independent verification mechanism and acts on what it returns — sequencing, not determining. This preserves Architecture Specification §6 and §8's exclusion of the Deployment Agent from assigning Verified status itself.

**Relationship to the Policy Engine:** unchanged and unaffected. The Policy Engine remains entirely uninvolved in verification, consistent with Deployment Policy Engine Specification §2/§7 and ADR-010's general principle that the Policy Engine never orchestrates and holds no lifecycle state. This ADR does not create any path by which the Policy Engine becomes aware of, or participates in, verification.

**Relationship to the Trust Model:** unchanged. Reported and Verified remain the only two trust states (Architecture Specification §8). This ADR clarifies who is involved in producing the Reported→Verified transition; it does not redefine either state, does not introduce a third, and does not alter the existing rule that a Reported outcome failing to reach Verified is treated as a failure under Deployment Policy.

## 4. Consequences

- The pull-versus-push ambiguity identified in the WP-11 Core preflight is resolved: verification is Deployment-Agent-sequenced (pull), because any independently-initiated (push) alternative would conflict with ADR-010's already-binding sequencing-ownership language.
- WP-11 Core can now be scoped as a Deployment-Agent-owned boundary, following the same conceptual relationship already established for execution and rollback, without further ownership ambiguity blocking it.
- WP-10's already-implemented rollback-consideration capability for the verification-failure question — which already treats the verified fact as something supplied to it from outside its own logic — remains fully consistent with this decision and requires no rework.
- The independent verification mechanism, being conceptually external to the five components' responsibilities, has no architecturally-defined internal responsibilities of its own under this ADR — it remains conceptually equivalent to the undefined mechanism behind every other existing boundary in this architecture.
- No future policy domain named in ADR-010 (retry, maintenance windows, emergency stop) is affected by this decision.
- This ADR resolves ownership only. All implementation contracts remain the responsibility of future Work Packages.

## 5. Alternatives Considered

- **Verification as an independently-initiated process, outside Deployment Agent sequencing:** rejected. Directly conflicts with ADR-010 §5's explicit, unqualified statement that lifecycle transitions belong exclusively to the Deployment Agent "in every phase, present and future."
- **Policy Engine performs or triggers verification:** rejected. Directly contradicts Deployment Policy Engine Specification §2 and §7's explicit exclusion of verification from the Policy Engine's responsibility, and ADR-010's general principle that the Policy Engine never orchestrates.
- **A sixth architectural component dedicated to verification:** rejected. Violates the five-component constraint every prior ADR in this project (ADR-008, ADR-009, ADR-010, ADR-011) has maintained without exception, and is unnecessary — the existing boundary-pattern precedent (ADR-008 §12) already demonstrates that an undefined external mechanism can sit behind an owned boundary without becoming a new component.
- **The Deployment Agent both initiates and performs the verification determination itself:** rejected. Directly contradicts Architecture Specification §8 ("Verified... separate from the Deployment Agent's own report... Verification, not the Deployment Agent, determines") and Execution Specification §2's explicit exclusion of this determination from the Deployment Agent's responsibility.

## 6. Non-Goals

This ADR explicitly does not define:

- Any implementation.
- Any contract, interface, or DTO.
- Any port.
- Any concrete adapter.
- Any scheduling or polling behavior.
- Any infrastructure or monitoring mechanism.
- Any retry behavior.

All of the above remain future, separate work, entirely out of this ADR's scope.

## 7. Impact

- **WP-11 Core:** directly affected — this ADR removes the ownership ambiguity that was blocking its preflight-to-implementation transition. It does not itself authorize implementation to begin.
- **WP-11 Integration:** indirectly affected — depends on WP-11 Core, whose ownership model is now settled.
- **WP-12 (Integration):** indirectly affected — the full deployment flow it assembles now has a settled conceptual answer for who owns the verification phase.
- **WP-03 (Audit Trail Foundation):** indirectly affected — verification remains a Deployment-Agent-sequenced decision point, consistent with what WP-03 is already scoped to record.
- **WP-08, WP-09, WP-10:** unaffected — none require rework under this decision.
