# ADR-006: Technology Stack Selection for Deployment Agent MVP

**Status:** Accepted
**Date:** 2026-07-18
**Approved:** 2026-07-19 (Founder)

## Context

The Kyron7 Deployment Agent MVP — Implementation Plan defines WP-00 (Development Environment Bootstrap) as technology-neutral by design: it explicitly defers the implementation language/runtime, package management, formatter, linter, and testing framework to "the technology stack selected through the project's approved architecture decision process." No such decision has been recorded anywhere in ODS Vault. Attempting to execute WP-00 surfaced this directly: a formatter and a linter (both required WP-00 deliverables) cannot be meaningfully configured without first knowing what language/runtime they apply to.

This ADR is that decision. It selects the technology stack for the Deployment Agent MVP, so that WP-00 — already approved — can be executed against a concrete, architecturally-justified stack rather than an assumed one.

Per ADR-005, the old `kyron7-operations-agent` repository carries no architectural authority and its code, types, and identifiers are not inherited. Its verified tooling choices (Node.js, TypeScript, npm, ESLint, Vitest, `tsc`) are cited below only as organizational precedent to weigh, not as a binding decision — this ADR evaluates the stack on its own merits against the approved architecture.

## Decision

The Kyron7 Deployment Agent MVP is implemented using:

- **Implementation language/runtime:** TypeScript on Node.js (LTS).
- **Package management:** npm.
- **Formatting:** Prettier.
- **Linting:** ESLint, configured for TypeScript.
- **Testing framework:** Vitest.
- **CI platform:** GitHub Actions.

## Rationale

- **Binary and two-state model enforcement (Architecture Specification §8; Policy Engine Specification §4):** the approved architecture requires exactly two risk classifications (low-risk/high-risk) and exactly two trust states (Reported/Verified), with no additional or graded states. TypeScript's literal and union types can enforce these as closed sets at compile time. The Repository Reconciliation Report identified the old repository's `PolicyResult.maxRiskLevel: string` — an open-ended string where the approved architecture requires a binary value — as a direct conflict; a statically-typed language capable of expressing closed unions directly prevents that class of defect from recurring.
- **GitHub as authoritative artifact source (Architecture Specification §6):** GitHub Actions runs CI colocated with the repository and artifact source already established as authoritative, without introducing an additional external CI service or its associated credential/access surface.
- **Platform-generic design (ADR-001):** TypeScript's interface-based typing supports defining the Deployment Agent, Policy Engine, and integration-point contracts in a form other future Kyron7 platform modules could depend on without being coupled to a single product, consistent with the Deployment Agent's role as the first reusable Kyron7 platform module (ADR-004).
- **Operational cost (ADR-004):** ADR-004 identifies reducing recurring operating cost as the Deployment Agent's core rationale. Reusing a verified, already-working tooling family from within the Kyron7 organization (Node.js/TypeScript/npm/ESLint/Vitest, as directly observed in `kyron7-operations-agent`) avoids introducing a second language ecosystem and its associated learning, maintenance, and tooling overhead, without violating ADR-005 — tooling-family consistency is a separate decision from code or component reuse, and no code, types, or identifiers are carried over.
- **Minimal surface area (ADR-001, ADR-002):** none of the selected tools introduce a new architectural component; they are implementation tooling only, consistent with the approved architecture's five components (Deployment Agent, Policy Engine, Founder Console, GitHub, ODS Vault).

## Consequences

- WP-00 (Development Environment Bootstrap), already approved as technology-neutral, can now be executed concretely against this stack: repository initialization, default branch, Prettier configuration, ESLint configuration, a Vitest scaffold, and a GitHub Actions CI skeleton.
- Work packages defining the Policy Engine's classification output, the rollback determination, and the Reported/Verified trust states (WP-04, WP-05, WP-11) should express those values as closed TypeScript union/literal types, directly enforcing the binary and two-state constraints from the Architecture Specification and Policy Engine Specification at compile time.
- No code, types, contracts, or identifiers are carried over from the old `kyron7-operations-agent` repository; this ADR selects a tooling family only, per ADR-005.
- Any future Kyron7 platform module may choose to adopt the same stack for consistency, but this ADR governs the Deployment Agent MVP specifically and does not itself mandate reuse elsewhere.

## Alternatives Considered

- **Python (Poetry/pip, Black, Ruff, pytest, GitHub Actions):** rejected. No verified organizational precedent within Kyron7 repositories; would introduce a second language ecosystem across the platform without a corresponding architectural benefit, and Python's type hints are not enforced at runtime as strictly as TypeScript's compiler, weakening the closed-set enforcement this ADR's Rationale relies on.
- **Go (Go modules, gofmt, golangci-lint, `go test`, GitHub Actions):** rejected. No organizational precedent; strong performance characteristics are not a stated requirement of the approved architecture (which is a policy/orchestration system, not a high-throughput data path), and introducing a new language for a single platform module conflicts with the operational-cost rationale in ADR-004.
- **Plain JavaScript (no static typing):** rejected. Directly reintroduces the risk the Repository Reconciliation Report flagged — an open, unconstrained representation of values the approved architecture defines as closed binary/two-state sets — with no compile-time protection against drift.
- **A non-GitHub-Actions CI platform (e.g., a third-party SaaS CI provider):** rejected. Adds an external service and its own credential/access management overhead for no benefit over GitHub Actions, given GitHub is already the architecture's authoritative artifact source; conflicts with ADR-001's preference for a minimal, generic platform surface.
