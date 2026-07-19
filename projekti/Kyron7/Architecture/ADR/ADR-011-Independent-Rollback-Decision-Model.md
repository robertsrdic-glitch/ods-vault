# ADR-011 — Independent Rollback Decision Model

**Status:** Approved
**Date:** 2026-07-19

## 1. Context

The WP-10 (Rollback Execution) architectural preflight found that rollback
determination, as currently modeled, requires a single combined fact set —
`DeploymentOutcomeSignal { executionFailed: boolean; verified: boolean }` —
before the Policy Engine can be asked whether rollback is required. That
preflight identified two blocking gaps: no legitimate source yet exists for
the `verified` fact, and no boundary exists for actually executing
rollback. The CTO-approved response introduced ADR-010, establishing that
the Deployment Agent alone owns lifecycle sequencing and transitions, and
that the Policy Engine's role is limited to answering bounded policy
questions — never initiating action, never holding lifecycle state.

A subsequent Rollback Architecture Review, conducted under ADR-010's
principles, asked whether the combined signal model still represented the
correct boundary. That review found that the approved rollback rule
(`executionFailed || !verified`) is a pure disjunction of two independent
facts, with no rule in the approved architecture that depends on their
interaction — and that the Architecture Specification itself already
describes execution failure and verification failure as two distinct
lifecycle moments (Architecture Specification §7 step 9: "if execution
fails, **or** a Reported outcome cannot be confirmed as Verified"), not one
combined moment.

A follow-on Rollback Decision Model Comparison evaluated the combined model
("Model A") against an independent-questions model ("Model B") across
twelve architectural criteria and recommended Model B. That recommendation
was CTO-approved and is the direct basis for this ADR.

## 2. Problem Statement

The combined rollback signal forces the Deployment Agent to hold two facts
from two different lifecycle phases — execution completion and independent
verification — before it may ask the Policy Engine anything about
rollback. This creates a structural dependency that does not reflect the
underlying policy logic (a pure OR with no joint term), forces the
execution-failure rollback trigger to wait on a verification mechanism that
may be irrelevant to it, and creates a fabrication risk: whenever
execution has already failed and verification correspondingly never runs,
some value for `verified` must still be supplied to satisfy the combined
signal's unconditional validation — inventing one would violate the
standing rule (ADR-009, ADR-010) that facts feeding a policy decision must
never be fabricated.

## 3. Decision

The combined rollback decision model is replaced with two independent
bounded policy questions:

- Rollback after execution failure is evaluated independently.
- Rollback after verification failure is evaluated independently.

Each policy question is evaluated only when its own required objective
facts exist — never before, and never with a fabricated or inferred
substitute for a fact that does not yet exist. The Deployment Agent decides
when each policy question is asked, consistent with its exclusive
ownership of lifecycle sequencing under ADR-010. The Policy Engine answers
each question independently, deterministically, and without reference to
the other question's fact or timing. This decision model follows ADR-010's
bounded-question principle directly: each question is scoped to exactly
the fact it needs, nothing more.

## 4. Decision Model

Two independently-askable rollback questions exist, corresponding to the
two triggers already described in Architecture Specification §7 step 9:

1. **Execution-failure rollback question** — askable once the Deployment
   Agent holds a Reported outcome from execution. This question requires
   only the fact of whether execution reported failure. It does not
   require, wait for, or reference any verification fact.
2. **Verification-failure rollback question** — askable once the
   Deployment Agent holds a legitimately produced verification report for
   a previously Reported outcome. This question requires only the fact of
   whether that outcome was confirmed Verified. It does not require, wait
   for, or reference the execution-failure fact.

Each question is bounded to a single fact, asked at the lifecycle point
where that fact becomes legitimately available, and answered by the Policy
Engine without knowledge of the other question's existence, timing, or
answer.

## 5. Responsibility Boundaries

- **Deployment Agent:** decides when each question is askable (i.e., when
  its required fact legitimately exists), asks each question
  independently at its own lifecycle point, and decides what to do with
  each answer. This is a sequencing responsibility, not a fact-gathering
  or fact-accumulation responsibility — no cross-phase state needs to be
  held or merged.
- **Policy Engine:** answers each bounded question deterministically from
  the single fact it is given. It does not initiate either question, does
  not hold lifecycle state between them, and does not need to know whether
  or when the other question will be, or was, asked.
- **Fact legitimacy:** no fabricated, defaulted, or inferred value may ever
  stand in for a fact a question requires. If the required fact does not
  yet exist, the corresponding question is simply not askable yet — this
  is a valid, expected lifecycle state, not an error condition to work
  around.

## 6. Architectural Consequences

- The execution-failure rollback question no longer has any dependency on
  a verification-reporting mechanism, and can be evaluated using facts
  already available since WP-08/WP-09 (a `ReportedOutcome`).
- The verification-failure rollback question remains dependent on a
  legitimate verification-reporting mechanism existing — that dependency
  is unchanged by this ADR, but it is now scoped to only one of the two
  rollback triggers rather than blocking both.
- Each rollback trigger's policy rule is independently testable,
  independently maintainable, and independently extensible, without risk
  of accidental coupling between them.
- Future policy domains named under ADR-010 (retry, maintenance windows,
  emergency stop, and others not yet anticipated) can each follow this
  same shape — one bounded question per lifecycle-relevant fact pattern —
  rather than requiring a bespoke combined-signal shape each time.
- Any future AI-assisted policy evaluator operating behind either question
  is scoped to reasoning about one bounded fact, not two facts from two
  lifecycle phases at once, consistent with ADR-010's determinism and
  governance requirements for such evaluators.

## 7. Relationship to ADR-010

This ADR does not modify ADR-010. It applies ADR-010's bounded-question and
sequencing-ownership principles to the specific rollback domain, resolving
one of the items ADR-010 explicitly deferred (its Section 9, "Explicit
Non-Decisions," named "rollback execution boundaries, verification signal
modeling, and WP-10/WP-11 sequencing" as outside its own scope). ADR-010
remains the authoritative source for the general responsibility boundary
between the Deployment Agent and the Policy Engine; this ADR is a
domain-specific application of that boundary, not a revision of it.

## 8. Relationship to Existing Architecture

This ADR does not amend the Architecture Specification. Architecture
Specification §7 step 9 already describes execution failure and
verification failure as two independently sufficient rollback triggers
("if execution fails, **or** a Reported outcome cannot be confirmed as
Verified"). This ADR aligns the internal decision model with that existing
description rather than changing it — the combined-signal model was an
implementation-shape choice made in WP-05, prior to ADR-010's clarification
of the bounded-question principle, not a requirement the Architecture
Specification itself ever imposed. Architecture Specification §8 (Trust
Model) and §9 (Constraints) are likewise unaffected: this ADR changes how
the rollback question is asked, not what the Trust Model states about
Reported and Verified outcomes.

## 9. Migration from the Combined Rollback Model

**Why the previous `DeploymentOutcomeSignal` model is being retired:** the
combined model was built to answer one question with two facts, on the
implicit assumption that both facts would always be simultaneously
available and jointly relevant. The Rollback Architecture Review found
neither assumption holds: the approved policy rule is a pure disjunction
with no joint term, and the two facts are produced at two genuinely
different lifecycle moments — one of which (verification) may never occur
at all for a deployment whose execution already failed. A model built on
an assumption the domain does not actually satisfy is the correct thing to
retire, regardless of how long it has existed.

**Why this is an architectural evolution rather than a correction:** the
combined model was not incorrect at the time it was defined (WP-05) — it
was a reasonable shape chosen before ADR-010 existed to state the
bounded-question principle explicitly, and before the WP-10 preflight
surfaced the sequencing cost of combining facts from two lifecycle phases.
This ADR does not conclude that WP-05's original design was a defect; it
concludes that applying a principle established afterward (ADR-010) to
this specific domain implies a different, better-fitting shape. That is
evolution in light of a newly settled architectural principle, not
correction of a prior mistake.

**How this removes the artificial WP-11 dependency:** the combined model's
unconditional requirement for both `executionFailed` and `verified` was the
direct and sole cause of the earlier WP-11-before-WP-10 sequencing
conclusion — not any inherent property of rollback as a domain concept.
Once the execution-failure and verification-failure triggers are modeled
as independent questions, the execution-failure question depends only on
facts already available since WP-08/WP-09, and no longer needs to wait on
WP-11 at all. Only the verification-failure question retains a dependency
on WP-11 — a narrower, accurate dependency, rather than the previous
model's artificial coupling of both triggers to the slower-arriving fact.

## 10. Alternatives Considered

- **Retain the combined `DeploymentOutcomeSignal` model unchanged:**
  rejected, per the Rollback Decision Model Comparison — it forces an
  artificial sequencing coupling the underlying policy rule does not
  require, and reintroduces the fabrication risk this ADR is meant to
  eliminate.
- **Make `verified` optional/nullable on the existing combined signal, to
  allow partial evaluation:** rejected. This would implicitly encode a
  three-state model (verified true / false / not-yet-known) into what
  ADR-007 through ADR-009 have consistently kept strictly binary, and would
  require the Policy Engine to interpret an absent fact — effectively
  reintroducing inference or default behavior at the Policy Engine
  boundary, which ADR-010 and this ADR both forbid.
- **Split the combined signal into two optional fields evaluated by one
  question that branches internally:** rejected. This preserves a single
  entry point but pushes the same sequencing ambiguity into the Policy
  Engine's own logic, making the Policy Engine responsible for detecting
  which fact is "the one that matters right now" — a sequencing-adjacent
  judgment that ADR-010 assigns exclusively to the Deployment Agent.

## 11. Explicit Non-Decisions

This ADR does not decide, and explicitly defers to later work packages:

- The interface, contract, or type definitions for either rollback
  question's request or response shape.
- The interface, contract, or type definition for any rollback-execution
  boundary (including any future `RollbackExecutionPort`-shaped
  contract) — rollback execution itself remains entirely out of this
  ADR's scope.
- The concrete source and reporting mechanism for the verification
  (`Verified`) signal — still WP-11's territory.
- Any change to the Implementation Plan's stated ordering or dependencies
  for WP-10 and WP-11; a documentation update reflecting this ADR's
  narrower WP-11 dependency (verification-failure question only) is
  expected but is separate work, not performed by this ADR.
- Any amendment to the Architecture Specification or to ADR-010.

## Architectural impact

The rollback-determination boundary is no longer a single combined
question but two independently bounded ones, each following ADR-010's
bounded-question principle directly. The Policy Engine's responsibility is
unchanged in kind (evaluate a bounded question, return a deterministic
answer) but is now expressed as two smaller, single-purpose
responsibilities instead of one wider one. The Deployment Agent's
sequencing responsibility is clarified rather than expanded: it asks each
question independently at the point its fact becomes legitimate, with no
new fact-accumulation duty.

## Implementation impact

WP-10 may now be scoped, planned, and sequenced around two independent
rollback triggers rather than one combined precondition. The
execution-failure trigger's implementation no longer requires WP-11 to
exist first; the verification-failure trigger's implementation still does.
No contracts, interfaces, or execution mechanisms are defined by this ADR —
those remain for the work packages that implement this decision model.

## Future ADR dependencies

- A future ADR (or the deferred rollback-execution boundary work) must
  define the interfaces/contracts for the two independent rollback
  questions and for rollback execution itself, consistent with this ADR's
  decision model and with ADR-010's responsibility boundaries.
- WP-11 must still define the source and semantics of the verification
  signal before the verification-failure rollback question can be
  implemented; this ADR narrows but does not eliminate that dependency.
- Any future Implementation Plan update reflecting this ADR's narrower
  WP-11 dependency is a separate, later documentation action, not covered
  here.
