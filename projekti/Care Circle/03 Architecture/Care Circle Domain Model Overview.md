# Care Circle Domain Model Overview

Document status: Approved
Source decision status: Approved

Full copy of DM-001 — Final Domain Model Specification.

## Core entities

### Person

Represents the human whose medication is organized.

Key fields: id, name, optional photo and date of birth, relationship, management mode (SELF_MANAGED or CAREGIVER_MANAGED), notes, display order, status (ACTIVE or ARCHIVED), timestamps.

A Person is not an account.

### Medicine

Represents the medicine itself.

Key fields: id, name, optional structured strength and display strength, form, optional photo, notes, status, timestamps.

Medicine contains no schedule, dose history or inventory.

### Therapy

Answers: How does one Person use one Medicine?

Key fields: personId, medicineId, dose, schedule, duration, reminders, optional inventory, notes, lifecycle status.

Statuses: DRAFT, ACTIVE, PAUSED, COMPLETED, ARCHIVED.

### Dose

Value object: numeric amount where available, unit, display text.

Custom non-numeric dose text is allowed, but may require manual inventory.

### Schedule

Types: DAILY, SELECTED_WEEKDAYS, EVERY_X_HOURS, AS_NEEDED.

A Schedule is a rule. It is not history.

### MedicationEvent

Represents one concrete scheduled or logged occurrence.

Stored statuses: PENDING, SNOOZED, TAKEN, SKIPPED, MISSED, COMPLETED_LATE, CANCELLED.

Each event preserves: original planned instant; local planned date and time; snapshots of person, medicine and dose; actual taken and confirmation times; confirmation actor and optional method; notes and status timestamps.

Snapshots preserve historical integrity after later edits.

### ReminderSettings

Domain preferences for how a Therapy should remind. Not the same as a scheduled operating-system notification.

### ReminderInstance

Technical representation of one planned reminder associated with an event or occurrence.

Possible types: PRE_REMINDER, PRIMARY, REPEAT, SNOOZE, MISSED_NOTICE, LOW_STOCK.

### Inventory

Belongs to exactly one Therapy.

Modes: DISABLED, AUTOMATIC, MANUAL.

### InventoryTransaction

Every stock change has a reason: INITIAL_STOCK, DOSE_TAKEN, DOSE_CORRECTION, STOCK_ADDED, MANUAL_CORRECTION.

### TherapyChange

Preserves effective-dated changes to dose, schedule, duration, reminders and lifecycle.

### AuditRecord

Records important corrections and destructive or history-affecting actions.

### BackupManifest

Contains format version, app version, creation time, record counts, checksum and encryption metadata.

## Main relations

```text
Person 1 ── * Therapy
Medicine 1 ── * Therapy
Therapy 1 ── 1 Schedule
Therapy 1 ── * MedicationEvent
Therapy 1 ── 0..1 ReminderSettings
Therapy 1 ── 0..1 Inventory
MedicationEvent 1 ── * ReminderInstance
Inventory 1 ── * InventoryTransaction
Therapy 1 ── * TherapyChange
```

## Invariants

1. A Therapy belongs to one Person and one Medicine.
2. Active Therapy requires a valid dose and schedule.
3. Draft creates no events or reminders.
4. MedicationEvent preserves original planned time.
5. Snooze does not create another event.
6. Later Therapy edits never rewrite past events.
7. Inventory belongs to Therapy.
8. Skipped and Missed do not consume inventory.
9. Taken and Completed Late consume inventory only in automatic mode.
10. Archiving preserves history.
11. Notification is not proof of ingestion.
12. Care Circle never changes medical instructions automatically.
13. Core behavior works offline.

## Implementation status

No domain tables, schema, repository or business logic exist in the codebase as of WP-04. This document describes the approved model that WP-05 (Proposed/Next) is expected to implement via Drizzle ORM/Kit. See [[Care Circle Work Package Register]].

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/architecture/DM-001-Final-Domain-Model.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Approved (source decision status: Approved)
**Notes:** Full copy of DM-001 (Approved 2026-07-21). Implementation-status note added to make clear this is an approved design, not yet implemented; no decision content altered.
