# Care Circle UX and Design Foundation

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Source decision status: Approved

Structured consolidation of the approved UX and design sources. All material decisions and constraints are represented, while wording and layout have been condensed for canonical ODS use — for example, DS-001's Core Components bullet list is reproduced here as a comma-separated paragraph, and the 13 UX specifications are merged into one document instead of remaining standalone files.

## Design system character

Care Circle is calm, warm, private, dependable and contemporary. It avoids clinical dashboards, visual noise and alarmist language.

### Design principles

- Calm before Attention
- One Primary Action
- Content before Decoration
- Large and Clear
- Consistency
- Progressive Disclosure
- Accessibility by Default
- Simplicity First

### Foundation

- system fonts;
- light, dark and system appearance;
- warm neutral backgrounds;
- white or gently separated surfaces;
- dark neutral primary text;
- one mature blue accent;
- soft green, amber and red status colors;
- 8-point spacing system;
- approximately 16-unit card radius;
- subtle borders and shadows;
- 150–250 ms purposeful motion;
- Reduce Motion support.

### Accessibility

- scalable text;
- large touch targets;
- readable contrast;
- text plus icon for status;
- screen-reader labels;
- logical focus;
- no hidden critical gestures;
- buttons use concrete action labels, not Yes/No;
- cards expand vertically when text grows.

### Core components

AppHeader, ScreenTitle, SectionHeader, PrimaryButton, SecondaryButton, TextButton, DestructiveButton, BottomNavigation, FloatingActionButton, PersonCard, MedicineCard, TherapyCard, EventCard, StatusBadge, SearchField, FormField, SelectionRow, SettingsRow, EmptyState, ErrorState, SuccessToast, ConfirmationDialog, BottomSheet, Avatar, Timeline, InlineWarning, AppLockScreen.

### Elderly-friendly rules

1. Key information is never tiny.
2. Buttons are large and separated.
3. Icons are supported by text.
4. Each screen has one obvious main action.
5. Status is written in words.
6. Forms are divided into short steps.
7. Errors explain recovery.
8. Navigation remains predictable.

See [[Navigation Accessibility and Simplicity]] for the permanent simplicity rule derived from these principles and from UX-P04.

## UX-001 — Onboarding

Flow:
1. Splash
2. Welcome
3. Privacy explanation
4. Notification explanation and system permission
5. Optional PIN or biometrics
6. Create first Person
7. Empty Today with Add Therapy

Onboarding introduces complexity progressively. Every screen has a clear next action. A Person can be Myself or Someone I care for, with self-managed or caregiver-managed mode.

## UX-002 — Today

Today answers: "What needs attention today?"

It shows a chronological timeline of Medication Events with person, time, medicine, strength, dose and status. Pending events expose Taken, Snooze and Skip. Completed events remain visible but visually quiet. Today does not edit therapies.

The screen is usable in under five seconds and with one hand.

## UX-003 — People

People lists active profiles. A card shows photo or initials, name, management mode and active therapy count.

Person Profile shows active, paused, completed and archived therapies plus a link to medication history. A caregiver confirmation may optionally record how it was verified.

Archiving preserves history and warns about active therapies.

## UX-004 — Medicines

Medicines is a simple local library containing name, strength, form, optional photo and notes.

It does not contain schedules, dose history or shared inventory. Medicine Details shows which persons and therapies use the medicine. Search is alphabetical and immediate. Similar entries are warned about but never merged automatically.

## UX-005 — Settings

Sections: Notifications, Security, Language, Appearance, Accessibility link, Backup, Archived Items, About.

Settings uses good defaults and minimal options. It clearly distinguishes app reminder settings from operating-system permission. Delete All Data is protected and not prominent.

## UX-006 — Add Therapy

Seven short steps:
1. Person
2. Medicine
3. Dose
4. Schedule
5. Duration
6. Reminders
7. Review

Known context is preselected. Inventory is optional. Drafts create no events or reminders. Caregiver-managed profiles clearly state that reminders appear on the caregiver's device.

## UX-007 — Therapy Details and Editing

Therapy Details shows person, medicine, dose, schedule, duration, reminders, next event, optional inventory, notes and recent history.

Editing is section-based. Changes to dose or schedule have an effective date and never rewrite past events. Person and Medicine cannot be casually reassigned on an active therapy. Lifecycle: Draft, Active, Paused, Completed, Archived.

## UX-008 — Medication Event Actions

Pending actions: Taken, Snooze, Skip.

Taken is one tap and offers short Undo. Skip requires confirmation. Snooze keeps the original scheduled time. Missed may later become Completed Late with actual time. PRN therapies use Log a dose.

Inventory decreases only for Taken, Completed Late and logged PRN doses.

## UX-009 — Notifications and Reminder Experience

Every notification identifies the Person, Medicine, Dose and planned time. Supported actions are Taken, Snooze and Open where the platform allows. Skip remains in-app.

The system limits repetition, distinguishes blocked permission from disabled reminders, restores reminders after reboot where required, and never claims delivery reliability it cannot verify.

## UX-010 — Inventory

Inventory is optional and belongs to Therapy.

It supports automatic or manual tracking, current amount, unit and low-stock threshold. Changes are transaction-based. Incorrect inventory never blocks recording a Medication Event. Low-stock messaging is visible but calm and not repetitive.

## UX-011 — Search, Empty States and Error States

Search is contextual, not global. Empty states explain the situation and show one useful next action. Errors state what failed, whether data is safe and what the user can do.

User input is preserved. Offline operation is normal, not an error. Technical codes are not shown to ordinary users.

## UX-012 — Navigation and Global Interaction Rules

Bottom navigation: Today, People, Medicines, Settings.

No hamburger menu. Back behavior follows platform conventions. Unsaved work is protected. Important actions are never available only through hidden gestures. Cards have large clickable areas. Primary actions are placed within easy reach.

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/ux/UX-001-Onboarding.md through docs/ux/UX-012-Navigation-and-Global-Interaction.md; docs/design/DS-001-Final-Design-System.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (source decision status: Approved)
**Notes:** Structured consolidation of 13 UX specifications (UX-001–UX-012 plus UX-P04, cross-referenced from [[Navigation Accessibility and Simplicity]]) plus DS-001, all Approved. Most individual UX sections closely track their one-paragraph sources; DS-001's Core Components list was reformatted from a bullet list into a comma-separated paragraph. No material decision or constraint was dropped, but wording and layout were condensed — this is Structured consolidation, not a verbatim/full copy.
