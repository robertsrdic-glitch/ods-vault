# Request for Change (RFC) Process

Version: 1.0
Status: Draft
Owner: Founder
Related Documents:
- [[AI Product OS Constitution]]
- [[Operating Model]]
- [[Organization Charter]]
- [[Repository Standard]]

---

# Purpose

Defines the official process for proposing, evaluating, deciding on, and recording any architectural change to the AI Product OS itself. This process exists so that the operating system evolves deliberately and traceably, never through informal or silent edits.

---

# Scope

This process applies to any change to a Foundation Document — a document that a governing document has designated as requiring an approved RFC before modification. It applies regardless of who or what proposes the change, and regardless of how small the change appears. It does not apply to ordinary product-level artifacts (specifications, design deliverables, implementation work), which are governed instead by the Operating Model and Repository Standard.

---

# RFC Lifecycle

## Proposal

Any role may propose a change to a Foundation Document. The proposal states: the document affected, the specific change requested, and the reasoning for it. A proposal is recorded in the repository before any discussion of its merits proceeds.

## Review

The Quality Guardian reviews the proposal for consistency with every other governing document, and identifies any conflicts, ambiguities, or downstream impacts the proposal would introduce. Review produces findings, not a decision.

## Decision

The Founder decides whether to accept, reject, or request revision of the proposal, per the Decision Model in the Operating Model. A decision is not valid until it is recorded.

## Implementation

Once accepted, the change is made to the affected Foundation Document by, or with the explicit involvement of, that document's owning role.

## Validation

The Quality Guardian confirms the implemented change matches the accepted proposal and introduces no new conflicts across the repository.

## Closure

The RFC is marked closed once validation confirms the change is correctly and consistently applied. Closed RFCs are retained as a permanent decision record; they are never deleted.

---

# Approval Authority

Only the Founder may approve an RFC affecting a Foundation Document. This authority may not be delegated silently — any delegation must itself be recorded as a governance decision.

---

# Repository Rules

- Every RFC is recorded in the repository at proposal time, before a decision is made.
- No Foundation Document is modified outside an approved RFC.
- An RFC's full lifecycle — proposal, review findings, decision, implementation, validation, closure — remains traceable from the repository alone.
- Superseded document versions move to Archive; nothing is deleted.

---

# Emergency Changes

Where a defect in a Foundation Document blocks ongoing work and waiting for the full lifecycle would cause disproportionate harm, the Founder may approve an expedited change. An expedited change still requires a recorded proposal and a recorded Founder decision — only the Review stage may be shortened, and a full Review and Validation must still follow retroactively before the RFC is closed.

---

# Decision Records

Every RFC decision — accepted, rejected, or revised — is recorded with its reasoning, regardless of outcome. Rejected and revised proposals remain part of the permanent record; they are not discarded.

---

# Definition of Success

This process succeeds when every change to a Foundation Document can be traced, from the repository alone, to a specific proposal, a recorded decision, and a validated implementation — with no Foundation Document ever having been modified outside this process.
