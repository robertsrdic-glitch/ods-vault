# ADR-004: Kyron7 Deployment Agent Priority

**Status:** Accepted
**Date:** 2026-07-16

## Context

Deployment automation has the highest return on investment among candidate platform initiatives because it directly reduces recurring Hermes operating costs — manual, Hermes-mediated deployment work is a recurring expense that a dedicated deployment agent would eliminate or substantially reduce.

## Decision

Immediately after the current gateway security work (Security Sprint 1C / 1C.1) is complete, the highest infrastructure priority becomes the **Kyron7 Deployment Agent MVP**.

## Consequences

- The Deployment Agent becomes the first reusable Kyron7 platform module, preceding broader Kyron7 OS work, and should be designed from the outset per ADR-001 as a platform capability rather than a NorthStar-specific tool.
- Sequencing is explicit: gateway security work is not deprioritized or interrupted by this decision — the Deployment Agent MVP begins only once that work is complete.
- Because the current gateway security work (Sprint 1C/1C.1) is design-only as of this record and not yet implemented, deployed, or tested, this ADR establishes intended sequencing rather than an immediately actionable start date.
