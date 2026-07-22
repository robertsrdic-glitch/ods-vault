# Care Circle Architecture Decision Register

Document status: Approved
Source decision status: Approved

Every source ADR (ADR-001 through ADR-010) is one short decision paragraph in the source repository, with no separate Rationale/Consequences sections. Where the source does not contain enough detail for a field, that field is marked "Not specified in source" rather than invented.

## ADR-001 — Medication Event-Centered Architecture

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** Care Circle is organized around concrete Medication Events. A Therapy is a rule; a Medication Event is one scheduled or logged occurrence. Today, history, snooze, missed doses and confirmation all operate on Medication Events.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Not specified in source. In practice this shapes [[Care Circle Domain Model Overview]] (MedicationEvent as the central entity) and [[../02 UX and Design/Care Circle UX and Design Foundation|UX-002 Today]].
- **Source path:** docs/adr/ADR-001-Medication-Event-Centered-Architecture.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** WP-05 (Proposed/Next, domain schema)

## ADR-002 — Local First

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** The MVP has no account, server or cloud dependency. Core use, reminders, history, inventory, security and backup work offline. SQLite is the local source of truth.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Underpins [[Care Circle Architecture Overview]] ("SQLite is the only persistent source of truth") and [[Care Circle Security Baseline]].
- **Source path:** docs/adr/ADR-002-Local-First.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** WP-04 (encrypted SQLite bootstrap)

## ADR-003 — Reliability before Features

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** Dependable reminders, correct history and safe data handling take priority over new capabilities. A feature is not accepted if it weakens reminder reliability.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Reflected in the Release Reliability Gate in [[Care Circle Architecture Overview]].
- **Source path:** docs/adr/ADR-003-Reliability-Before-Features.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** Not specified in source

## ADR-004 — Family and Caregiver First

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** Multiple people are supported from the first version. A profile is not an account and may be managed entirely by a caregiver using one local device.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Reflected in the Person/caregiver model in [[Care Circle Product Foundation]] and [[Care Circle Domain Model Overview]].
- **Source path:** docs/adr/ADR-004-Family-and-Caregiver-First.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** Not specified in source

## ADR-005 — Apple-like Simplicity

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** The product uses calm, spacious, familiar mobile patterns. It is inspired by clarity and restraint, not by copying Apple assets or interfaces.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Reflected in [[../02 UX and Design/Care Circle UX and Design Foundation|Care Circle UX and Design Foundation]] design character and principles.
- **Source path:** docs/adr/ADR-005-Apple-Like-Simplicity.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** Not specified in source

## ADR-006 — Two-Tap Rule

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** Common actions should require no more than two taps where practical. Confirming a pending dose from Today requires one tap.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Reflected in UX-008 Medication Event Actions (Taken is one tap) within [[../02 UX and Design/Care Circle UX and Design Foundation|Care Circle UX and Design Foundation]].
- **Source path:** docs/adr/ADR-006-Two-Tap-Rule.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** Not specified in source

## ADR-007 — Human Confirmation

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** Care Circle records a user's confirmation. It never claims independent proof of ingestion and never changes dosage or therapy automatically.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** This is the source of the permanent "not proof medication was taken" product boundary stated in [[Care Circle Product Foundation]] and invariant 11 in [[Care Circle Domain Model Overview]].
- **Source path:** docs/adr/ADR-007-Human-Confirmation.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** Not specified in source

## ADR-008 — Calm Design

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** The interface avoids alarmist language, visual clutter and unnecessary urgency. Attention colors are reserved for information that genuinely needs attention.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Reflected in the "Calm before Attention" design principle in [[../02 UX and Design/Care Circle UX and Design Foundation|Care Circle UX and Design Foundation]].
- **Source path:** docs/adr/ADR-008-Calm-Design.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** Not specified in source

## ADR-009 — Therapy Terminology

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** The domain term is Therapy, not Medication Plan. A Therapy connects one Person, one Medicine, one Dose, one Schedule, reminders, inventory and lifecycle.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** Fixes the terminology used throughout [[Care Circle Domain Model Overview]] and all UX-006/UX-007 specifications.
- **Source path:** docs/adr/ADR-009-Therapy-Terminology.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** Not specified in source

## ADR-010 — Roadmap Discipline

- **Status:** Approved
- **Date:** Not specified in source
- **Decision:** The project follows the approved sequence. New ideas are recorded for a future phase and are not inserted into the current scope unless the roadmap is formally changed.
- **Rationale:** Not specified in source beyond the decision statement.
- **Consequences:** This is the governing principle behind the controlled, sequential Work Package model in [[Care Circle Work Package Register]] and MVP discipline in [[../01 Product/Care Circle MVP Scope|Care Circle MVP Scope]].
- **Source path:** docs/adr/ADR-010-Roadmap-Discipline.md
- **Source commit:** 99e9d9c52865d0d736af765702f514637133caed
- **Related work packages:** All (governs sequencing of WP-01 through WP-04 and beyond)

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/adr/ADR-001 through docs/adr/ADR-010
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Approved (source decision status: Approved)
**Notes:** All 10 ADRs referenced in PROJECT-STATUS.md as "ADR-001 through ADR-010" were located and are preserved in full. No ADR number was invented; none was missing. Source ADRs contain no explicit date, rationale, or consequences fields — those fields are marked "Not specified in source" rather than fabricated, with consequences inferred only where directly traceable to another approved document (noted inline).
