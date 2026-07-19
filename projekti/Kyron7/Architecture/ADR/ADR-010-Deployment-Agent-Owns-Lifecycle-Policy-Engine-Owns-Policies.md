# ADR-010: Deployment Agent Owns Lifecycle, Policy Engine Owns Policies

**Status:** Approved
**Date:** 2026-07-19

## 1. Context

Earlier architecture reviews — most recently during the rollback and
verification design review that preceded WP-10 — surfaced a recurring
ambiguity at the boundary between two distinct kinds of responsibility:
orchestrating the deployment lifecycle, and evaluating policy to produce a
decision consumed within that lifecycle.

The ambiguity did not appear as a single, isolated question. It recurred
each time a new lifecycle phase was designed: once for execution, once for
approval, and again for rollback and verification. In each case the same
underlying question resurfaced — does the Policy Engine merely answer a
question the Deployment Agent asks, or does it participate in deciding what
happens next in the flow? The rollback and verification design review made
this ambiguity explicit for the first time, because rollback and
verification both depend on sequencing decisions (when to check, when to
act, when to wait) that are easy to mistake for policy decisions but are
not.

This ADR exists to state, as a single durable principle rather than a
recurring per-phase judgment call, where that boundary lies — so that every
future lifecycle phase can be designed against one settled answer instead of
re-litigating the same ambiguity each time. It formalizes and makes durable
a separation already implicit in the Approved Architecture Specification
(see Section 8, "Relationship to Existing Architecture"); it does not amend
that specification.

## 2. Decision

- The Deployment Agent owns the deployment lifecycle.
- The Policy Engine evaluates bounded policy questions and returns
  decisions.
- The Policy Engine never owns workflow progression.
- The Policy Engine never initiates or orchestrates lifecycle transitions.
- The Deployment Agent is the sole authoritative owner of lifecycle
  sequencing and transitions.
- Other components may observe or report lifecycle state, but they do not
  own or advance it.
- Policy decisions inform orchestration but never imply orchestration
  ownership.

Rollback execution boundaries, verification signal modeling, and WP-10 /
WP-11 sequencing are explicitly outside this ADR's scope and will be
handled separately in ADR-011 or later decisions.

## 3. Deployment Agent Responsibilities

The Deployment Agent is responsible for:

- Owning the deployment lifecycle end to end, for every phase — current and
  future.
- Determining the order in which lifecycle phases occur.
- Deciding when to consult the Policy Engine, and what to do with the
  Policy Engine's answer.
- Initiating execution, verification, rollback, and approval requests.
- Being the sole place where "what happens next" is decided.
- Carrying the lifecycle's current position and history — no other
  component holds this.
- Advancing the lifecycle from one state to the next; this authority is
  exclusive to the Deployment Agent.

## 4. Policy Engine Responsibilities

The Policy Engine is responsible only for evaluating bounded policy
questions, including:

- Risk classification.
- Approval requirements.
- Rollback policy.
- Retry policy.
- Maintenance windows.
- Emergency stop policies.
- Any future policy domain.

The Policy Engine's responsibility begins and ends at answering a policy
question from the input it is given. It does not initiate action, does not
sequence phases, does not hold or advance lifecycle state, and is not aware
of its own decision's place within a larger sequence. It may be observed or
consulted at any point in the lifecycle without its behavior depending on
that context.

## 5. Architectural Boundary

The boundary between the two components is exact and does not vary by
lifecycle phase or policy domain:

- The Policy Engine answers questions.
- The Deployment Agent decides what happens next.
- A policy decision never implies orchestration ownership over the
  lifecycle phase it informs.
- Lifecycle transitions belong exclusively to the Deployment Agent, in
  every phase, present and future.
- Any component other than the Deployment Agent — including the Policy
  Engine — may observe or report on lifecycle state, but none may own or
  advance it.

A future capability that appears to require the Policy Engine to initiate
an action, hold lifecycle state, or determine sequencing is, by this
boundary, either a Deployment Agent capability or a sign that the
capability has been misclassified — not a basis for extending the Policy
Engine's role.

**On future AI-assisted policy evaluation:** a future AI-assisted evaluator
operating behind the Policy Engine boundary is not inherently
deterministic, and this ADR does not claim otherwise. Such an evaluator may
provide evidence, scoring, or recommendations as part of producing a
decision. However the authoritative policy decision returned across the
boundary must still conform to validated contracts, explicit governance
rules, and whatever determinism requirements apply to that specific policy
domain. Introducing an AI-assisted evaluator does not relax those
requirements, and does not grant the Policy Engine any orchestration
authority it does not otherwise have under this ADR.

## 6. Consequences

- **Simpler responsibility boundaries.** Every future design question of
  the form "does this belong to the Deployment Agent or the Policy Engine"
  reduces to one test: is this a decision, or a sequencing action?
- **Easier future retry policies.** A retry policy is naturally expressed
  as a Policy Engine decision ("should this be retried?") consumed by
  Deployment Agent sequencing ("retry now"), without either side acquiring
  responsibility for the other's concern.
- **Maintenance windows.** Whether a deployment is permitted to proceed
  during a given window is a policy question; when and whether to actually
  hold, delay, or resume the lifecycle around that answer remains the
  Deployment Agent's.
- **Progressive rollout.** Staged rollout decisions (proceed to the next
  stage, halt, or reverse) can be added as new Policy Engine answers
  without requiring the Policy Engine to track or drive rollout
  progression itself.
- **Approval policies.** Any future approval policy beyond the current
  Founder approval model fits the same shape already established: the
  Policy Engine decides whether approval is required; the Deployment Agent
  owns requesting it and acting on the result.
- **Emergency stop policies.** An emergency stop is a policy decision
  ("must this halt?") the Deployment Agent can consult at any sequencing
  point, without needing the Policy Engine to understand or hold lifecycle
  state to answer it.
- **Future AI-assisted policy evaluation.** Because the Policy Engine's
  contribution is bounded to producing a decision from given input, a
  future AI-assisted or learned evaluator can be introduced behind that
  boundary — subject to the same contracts, governance rules, and
  determinism requirements described in Section 5 — without expanding the
  Policy Engine's responsibility into lifecycle orchestration.
- **Deterministic, reusable decisions.** Because the Policy Engine never
  holds lifecycle state, its answers remain a function of the input it is
  given, regardless of when or how many times it is consulted within a
  single deployment's lifecycle.
- **Long-term architectural consistency.** Every future lifecycle phase or
  policy domain inherits an already-settled answer to "who owns this,"
  rather than reopening the boundary question each time the architecture
  grows.

## 7. Alternatives Considered

- **Policy Engine orchestrates lifecycle decisions:** rejected. Under this
  alternative, the Policy Engine would not merely answer "is this
  low-risk" or "is rollback required," but would also decide *when* to ask
  those questions, *what* should happen next given its own answer, or
  otherwise hold and advance lifecycle state. This was rejected because it
  would make the Policy Engine's behavior depend on lifecycle context it
  has no principled reason to hold, blurring the boundary that keeps its
  decisions deterministic and reusable across every lifecycle phase; it
  would duplicate lifecycle ownership across two components instead of
  one, reintroducing exactly the ambiguity this ADR exists to resolve; and
  it would make every future lifecycle phase (retry, progressive rollout,
  emergency stop) re-raise the same "who decides sequencing here" question
  this ADR settles permanently, rather than inheriting a single,
  already-answered boundary.
- **Allowing other components to advance lifecycle state directly, when
  convenient:** rejected. Permitting any component other than the
  Deployment Agent to advance — rather than merely observe or report —
  lifecycle state would reintroduce distributed, ambiguous ownership of
  the same kind this ADR exists to eliminate, even if that component is
  never intended to become a full orchestrator.
- **Treating a future AI-assisted evaluator as inherently deterministic,
  and therefore exempt from the governance and contract requirements
  applied to other policy decisions:** rejected. Determinism is a property
  that must be established for a given policy domain's authoritative
  decision, not assumed because the underlying evaluator is AI-assisted;
  exempting such an evaluator from validated contracts, governance rules,
  or domain-specific determinism requirements would weaken the same
  boundary this ADR is meant to keep durable.

## 8. Relationship to Existing Architecture

ADR-010 clarifies and makes durable the responsibility separation already
implicit in the Approved Architecture Specification — specifically Section
6 ("Responsibilities"), which already assigns lifecycle orchestration to
the Deployment Agent and classification/rollback-determination decisions to
the Policy Engine, and Section 9 ("Constraints"), which already states that
classifications and approval requirements are policy-driven rather than
hardcoded into the Deployment Agent. ADR-010 does not introduce a new
division of responsibility; it states explicitly, as a standing principle,
a boundary the specification already establishes case by case.

ADR-010 does not directly amend or replace the frozen Architecture
Specification. It does not add, remove, or alter any section of that
document. It exists as a separate, durable clarification that future ADRs
and work packages can rely on without re-deriving the boundary from the
specification's individual responsibility statements each time.

## 9. Explicit Non-Decisions

This ADR does not decide, and explicitly defers:

- The rollback execution boundary (the contract through which the
  Deployment Agent invokes and receives the result of a rollback action) —
  deferred to ADR-011 or a later decision.
- The source, sequencing, and semantics of the verification (`Verified`)
  signal — deferred to ADR-011 or a later decision.
- The relative ordering of WP-10 and WP-11 in the Implementation Plan —
  deferred to ADR-011 or a later decision.
- Any concrete infrastructure, adapter, or implementation mechanism for
  execution, rollback, verification, or any other lifecycle phase.
- Any amendment to the Architecture Specification, any existing ADR, or the
  Implementation Plan.
