# Care Circle Architecture Overview

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Source decision status: Approved

Full copy of TA-001 — Technical Architecture Specification.

## Architectural objective

Build an encrypted, local-first React Native application with a domain-driven Medication Event engine and replaceable native notification adapters.

## Technology direction

- React Native
- TypeScript
- Expo Development Build
- Expo Router
- React Native New Architecture
- SQLite through expo-sqlite
- SQLCipher
- Drizzle ORM and migrations

The current stable compatible versions are pinned only when implementation begins.

## Layers

```text
Presentation
    ↓
Application
    ↓
Domain
    ↑
Infrastructure adapters
    ↓
Native platform
```

### Dependency rules

Allowed:
- Presentation → Application
- Application → Domain
- Infrastructure → Application ports and Domain types

Forbidden:
- Domain → Expo or React Native
- Domain → SQLite
- Screen → raw SQL
- Screen → notification library
- UI component → SecureStore

## Ports

Examples: NotificationSchedulerPort, MedicationEventRepository, TherapyRepository, InventoryRepository, SecureKeyStorePort, BiometricAuthenticationPort, BackupCryptoPort, FileExportPort, ClockPort, TransactionPort.

## Database

SQLite is the only persistent source of truth once the schema layer is introduced ([[Care Circle Domain Model Overview]]). No domain tables were introduced through WP-04 ([[../05 Work Packages/Care Circle Work Package Register|Work Package Register]]).

Configuration includes: foreign keys; WAL journal mode; busy timeout; prepared statements; transactional use cases; versioned migrations; encrypted database through SQLCipher.

## Time model

A central ScheduleEvaluator and TimeService own time calculations.

Concrete events store: UTC planned instant; local date and time; time-zone context; rule revision; actual and confirmation times.

Daily and selected-weekday schedules follow local wall time. Every-X-hours follows elapsed time from its anchor.

## Schedule revisions

Dose, schedule and duration changes create effective-dated revisions. Past Medication Events remain unchanged.

## Event generation

Medication Events are generated deterministically within a controlled horizon or when needed.

A unique occurrence key combines: therapy; rule revision; scheduled instant. This prevents duplicate events.

## Reminder architecture

```text
ScheduleEvaluator
OccurrenceMaterializer
ReminderPlanner
ReminderOutbox
NotificationSchedulerPort
ReminderReconciler
```

The Outbox records desired schedule or cancellation actions before invoking the operating system. Reconciliation compares desired local state with platform-scheduled reminders and repairs mismatches.

## Android

Use the user-granted exact-alarm path where exact alarms are required. The application checks actual permission, explains it plainly, and never claims reminders are active when the platform blocks them.

Android reminders must be restored after device reboot and reconciled after permission, time or time-zone changes.

## iOS

Use local UserNotifications with repeating calendar triggers for stable recurring schedules and one-time requests for snooze, finite therapies and special events. Use a controlled rolling horizon for non-repeating requests.

## Notification actions

Where supported: Taken, Snooze, Open. Skip remains in-app.

All callbacks are idempotent. Duplicate callbacks may create only one status transition and one inventory transaction.

## Security (architecture-level)

- encrypted SQLite database;
- random database key stored in Android Keystore or iOS Keychain through a secure adapter;
- PIN stored only as a salted slow hash;
- optional system biometrics;
- App Lock is separate from database encryption;
- photos stored inside the encrypted data boundary;
- no analytics or advertising SDK in MVP.

See [[../04 Security/Care Circle Security Baseline|Care Circle Security Baseline]] for the full security record, including the WP-04 implementation.

## Backup

A backup is one encrypted `.carecircle` file containing: manifest; encrypted consistent database snapshot; format and app versions; checksum; cryptographic parameters.

Restore uses: manifest validation; integrity verification; decryption to staging; migration on staging; database integrity check; atomic replacement; reminder reconciliation.

Failure never overwrites the current valid database.

## Migrations

- sequential and immutable after release;
- committed to the repository;
- tested against old database fixtures;
- transactional where supported;
- no ad hoc schema changes in UI code.

WP-05 is expected to establish the Drizzle schema and migration foundation, but remains Proposed/Next — not implemented as of this consolidation.

## Diagnostics

No server and no automatic upload.

A small local diagnostic log may contain technical event categories and timestamps, but no PIN, keys, backup password or unnecessary medication content.

## Testing

Required layers: domain unit tests; repository integration tests; notification adapter contract tests; migration tests; backup/restore tests; real-device reminder tests; accessibility tests; end-to-end critical flows.

## Release reliability gate

Release is blocked unless verified on real devices:

1. locked-phone reminder;
2. closed-app reminder;
3. Android reboot recovery;
4. exact-alarm permission change handling;
5. iOS local-notification persistence;
6. old reminder cancellation after therapy change;
7. snooze without duplicate event;
8. duplicate Taken without duplicate inventory change;
9. safe failed restore;
10. safe failed migration;
11. complete offline operation;
12. honest permission and reliability status.

## Official technical references

- React Native TypeScript documentation: https://reactnative.dev/docs/typescript
- Expo Router: https://docs.expo.dev/router/introduction/
- Expo SQLite: https://docs.expo.dev/versions/latest/sdk/sqlite/
- Expo Notifications: https://docs.expo.dev/versions/latest/sdk/notifications/
- Expo SecureStore: https://docs.expo.dev/versions/latest/sdk/securestore/
- Expo LocalAuthentication: https://docs.expo.dev/versions/latest/sdk/local-authentication/
- Android exact alarms: https://developer.android.com/develop/background-work/services/alarms
- Apple UserNotifications: https://developer.apple.com/documentation/usernotifications

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/architecture/TA-001-Technical-Architecture.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (source decision status: Approved)
**Notes:** Full copy of TA-001 (Approved 2026-07-21). One clarifying cross-reference added noting WP-05/Drizzle status is Proposed/Next, consistent with [[Care Circle Architecture Decision Register]] and current PROJECT-STATUS.md. No approved decision altered.
