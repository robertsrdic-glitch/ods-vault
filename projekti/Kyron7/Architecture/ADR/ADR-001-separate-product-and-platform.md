# ADR-001: Separate Product and Platform

**Status:** Accepted
**Date:** 2026-07-16

## Context

Infrastructure components — deployment, approvals, monitoring, security — should not live inside individual products. Building these capabilities directly into NorthStar would couple platform-level concerns to a single product's codebase and release cycle, making them harder to reuse as Kyron7 grows beyond one product.

## Decision

NorthStar remains a **product**.

Kyron7 OS becomes the internal **platform** for reusable engineering capabilities (deployment, approval workflows, monitoring, security tooling, and similar cross-cutting infrastructure).

## Consequences

- Future Kyron7 products reuse Kyron7 OS modules rather than reimplementing platform-level capabilities per product.
- Platform components must be designed generically enough to serve more than one product from the outset, not retrofitted later.
- NorthStar's own repository and release cycle stay scoped to product functionality; platform-level infrastructure work is tracked and versioned separately under Kyron7 OS.
