# WP-04 — Encrypted SQLite Bootstrap and Key Management

Document status: Approved

**Recorded WP status: Implemented and statically validated, including two post-review security remediation rounds; committed, pushed and verified; Android Runtime Validation Pending.**

Date: 2026-07-21 (implementation); 2026-07-22 (commit)
Risk: **High** (security-critical infrastructure)
Mode: High
Commit: `99e9d9c52865d0d736af765702f514637133caed` — "feat: add encrypted SQLite bootstrap foundation"

This is the highest-risk work-package checkpoint implemented to date. WP-04 must never be described as Completed, runtime validated, production ready, or Android validated. The status phrase above is exact and must be reused verbatim elsewhere in this vault.

## Objective

Establish an encrypted local-first SQLite foundation using SQLCipher, with a fail-closed bootstrap state machine and a securely stored 256-bit database key. Infrastructure only — no schema, no product tables, no repositories, no business logic.

## Threat model

- **Data at rest:** the database is opened only through SQLCipher with a 256-bit key, unreadable without the key even if device storage is extracted.
- **Key at rest:** generated with `expo-crypto` native randomness, stored exclusively via `expo-secure-store` (`requireAuthentication: false`); never written to a normal file, logged, placed in an error, returned to UI code, or held in React state.
- **Fail-closed over fail-open:** every ambiguous or failed state resolves to locked/unavailable or recoverable-error. No path silently creates a new key next to an existing encrypted database; no path deletes or overwrites existing state to "recover."
- **Blast radius of a compromised UI layer:** presentation code only ever receives a sanitized `DatabaseBootstrapResult`; native error text, file paths and SQL are never exposed publicly.
- **Backup exfiltration:** `android.allowBackup: false` and `expo-secure-store`'s Android backup-rule injection disabled (`configureAndroidBackup: false`).

## Security remediation — round 1 (4 findings, all fixed)

1. **Bootstrap could reject into presentation** — `run()` had no top-level exception handling. Fixed via a `runSafely()` wrapper; `bootstrap()` can no longer reject; a failed attempt is never cached as ready; `AppBootstrapProvider` gained a defense-in-depth `.catch()`.
2. **File-state failure didn't take strict precedence** — the key store was consulted before the file-state branch. Fixed: file-state is now checked immediately, and `check-failed` returns `database-file-state-failed` before the key store is ever asked to act.
3. **SecureStore writes could overwrite an existing key** — nothing at the adapter level prevented overwrite. Fixed via a new independently unit-tested `write-key-if-absent.ts` adapter: reads before writing; refuses to write over an existing entry (`already-exists`); `DatabaseKeyService` re-reads and safely reuses/rejects whatever won the race, never returning its own unwritten candidate.
4. **Diagnostic cleanup wasn't fail-safe or verified** — deletion ran only after every diagnostic step succeeded, and `cleanupPassed` was set without verifying the file was gone. Fixed via `diagnostic-cleanup.ts`: pre-diagnostic best-effort removal of any stale file, cleanup in a `finally` block, `cleanupPassed: true` only after a post-delete existence check confirms absence, plus `assertIsDiagnosticDatabaseName()` guarding every deletion so the active database can never be targeted.

## Security remediation — round 2 (3 findings, all fixed)

1. **Cleanup verification had a false-positive path** — `diagnosticDatabaseFileExists()` returned `false` ("does not exist") whenever the database directory was simply unavailable. Fixed: it now throws instead, and every fail-closed check already treats a thrown existence check as "cannot verify," never "confirmed absent."
2. **The diagnostic could open a database before clean state was verified** — stale-database removal was best-effort only. Fixed via a new `verifyCleanDiagnosticState()` gate that deletes and positively verifies absence before any `openDatabaseAsync()` call; a `'blocked'` gate result skips opening entirely.
3. **`writeKeyIfAbsent()` had a real, not theoretical, read/write race** — the installed `expo-secure-store` SDK 57 API was directly inspected (`SecureStore.d.ts`) and confirmed to expose no atomic create-only or compare-and-set primitive. Fixed via process-wide FIFO serialization (Option B) of every `writeKeyIfAbsent()` call, plus post-write read-back verification that only reports `'stored'` on an exact match. This is an honest **process-local** guarantee, not native atomicity — sufficient because Care Circle is currently a single-process JS runtime with no other writer of this entry; a future multi-process/background-service architecture would need re-evaluation.

## Dependencies

Runtime (via `npx expo install`, no `--force`/`--legacy-peer-deps`): `expo-sqlite@~57.0.1`, `expo-secure-store@~57.0.1`, `expo-crypto@~57.0.1`, `expo-file-system@~57.0.1`.
Dev only: `vitest@^4.1.10` — no test runner existed in the project before WP-04.

## Native configuration

```json
"android": { "allowBackup": false },
"plugins": [
  "expo-router", "expo-font", "expo-localization",
  ["expo-sqlite", { "useSQLCipher": true }],
  ["expo-secure-store", { "faceIDPermission": false, "configureAndroidBackup": false }]
]
```

Each setting was confirmed directly against installed plugin source (`withSQLite.ts`, `AllowBackup.js`, `withSecureStore.js`), not assumed. `requireAuthentication` is never set to `true` anywhere in `src/` (validator-enforced).

## Key lifecycle

- Format: exactly 32 cryptographically random bytes (`expo-crypto` `getRandomBytesAsync`), represented as 64 lowercase/uppercase hex characters, validated with `/^[0-9a-fA-F]{64}$/` before use.
- Storage: `SecureKeyStorePort` via `ExpoSecureKeyStore`, under fixed key name `care_circle_database_key_v1`.
- `generateAndPersistKey()` always re-checks for an existing key first. No key rotation, reset, or deletion path anywhere in WP-04.

## Four-state fail-closed matrix

| Database file | Key | Action |
| --- | --- | --- |
| absent | absent | generate + persist a new key, then create and open |
| absent | present | use the existing key, create and open |
| present | present | use the existing key, open and verify |
| present | absent | **locked/unavailable** — no key generated, no database opened, nothing deleted |

Two additional fail-closed cases evaluated first: file-state check failed (`database-file-state-failed`) and SecureStore unavailable (`database-unavailable`/`secure-store-unavailable`).

## SQLCipher opening order

1. Apply the validated raw key as the first operation.
2. Force a real read from `sqlite_master` to prove the key works.
3. Query `PRAGMA cipher_version`; fail if empty.
4. Enable and verify `foreign_keys = ON`, `journal_mode = WAL`, `busy_timeout = 5000` — each asserted by value.
5. Run `PRAGMA quick_check`; require exactly `"ok"`.
6. Handle closed on every failure path; left open only on full success; never exposed through React context, state or props.

## Architecture boundaries

Application ports/services import nothing from Expo/React Native (validator-enforced). Infrastructure owns every native touchpoint. Presentation imports no native persistence/security module directly — only the sanitized `DatabaseBootstrapPort.bootstrap()` contract. Domain remains untouched. Route files contain no SQL and no persistence imports. No raw SQLite handle is exposed through React context, state or props. No domain repository or product table exists.

## Public error behavior

`DatabaseBootstrapResult`: closed union `initializing` / `ready` / `recoverable-error { reasonCode }` / `database-unavailable { reasonCode }`, where `reasonCode` ∈ `secure-store-unavailable`, `database-file-state-failed`, `database-key-missing`, `invalid-stored-key`, `sqlcipher-unavailable`, `database-key-rejected`, `database-integrity-failed`, `database-configuration-failed`, `unsupported-platform`, `unknown-bootstrap-failure`. No file path, SQL text, key or native stack trace ever appears in this type or in any bootstrap-path log.

## Diagnostic separation

`sqlcipher-runtime-diagnostic.ts` runs only when `__DEV__` is true, uses a completely separate database name (`care_circle_wp04_diagnostic.db`, asserted distinct from the active database), generates its own ephemeral in-memory key, never touches the active database or key, and logs only sanitized boolean fields under `CARE_CIRCLE_WP04_DIAGNOSTIC`.

## Tests

77 tests across 5 files, all passing, 0 skipped (up from 37 across 3 files originally, 63 across 4 files after round 1):

- `determine-database-bootstrap-action.test.ts` — all four file/key combinations, file-state-failure priority, SecureStore-unavailable priority.
- `database-key-service.test.ts` — hex-key validation, key conversion, invalid-key rejection, existing-key reuse, write-time race handling.
- `write-key-if-absent.test.ts` (new in round 2) — single-call behavior, plus process-wide concurrency serialization (2–3 concurrent calls, exactly one write occurs).
- `encrypted-database-bootstrap.test.ts` — SQLCipher-verification layer and end-to-end bootstrap, all four state combinations, unexpected-dependency-exception suite.
- `diagnostic-cleanup.test.ts` (new in round 1, expanded in round 2) — cleanup and `verifyCleanDiagnosticState` fail-closed behavior; active-database name can never enter the deletion step.

## Static validation results

`npm run typecheck` PASS; `npm run lint` PASS (scope widened to `src scripts tests vitest.config.ts` in round 1); validator PASS (WP-02/WP-03/WP-04 banners); `npm run test:unit` PASS (5 files, 77 tests); `npm run check` PASS; `npx expo install --check` PASS; `npx expo-doctor` PASS 20/20; `npx expo config --type public` confirmed `allowBackup: false` and both plugin configs; Android JS bundle export PASS; secret/prohibited-file scan clean; UTF-8-without-BOM confirmed on all new/modified files including both remediation rounds.

## Native build result — not attempted

Read-only environment inspection found no Java, no `ANDROID_HOME`/Android SDK, no `adb`, and no Gradle, and `app.json` has no `android.package`/`ios.bundleIdentifier` configured. Per the mandatory rules, either condition alone requires stopping before the native/prebuild stage — no tooling was installed and no application identifier was invented. The `android/` directory does not exist and was not generated.

## Android runtime evidence — not available

No device or emulator was used; nothing was force-stopped, cleared or wiped. The active-database/no-key fail-closed case is proven entirely through unit tests, not through destructive manipulation of a real SecureStore key.

## Limitations

- SQLCipher's actual native presence and behavior is unverified on-device.
- The composition root and dev-only diagnostic are not unit tested by design (they wire or exercise real native modules).
- No iOS-specific runtime validation was performed.
- The `writeKeyIfAbsent()` non-overwrite guarantee is process-local serialization, not native atomicity.

## Explicit exclusions

Drizzle ORM/Kit, application migrations, schema versioning, domain tables, repositories, CRUD, Medication Events, reminders, notifications, PIN, biometrics, App Lock, backup, restore, photos, cloud sync, analytics, crash reporting, database reset, key deletion, key rotation, rekeying, plaintext-to-encrypted migration, production signing, store deployment.

## Committed files

34 files changed, 4780 insertions(+), 86 deletions(-), including: `src/application/ports/*` (3 files), `src/application/services/determine-database-bootstrap-action.ts`, `src/infrastructure/persistence/*` (9 files), `src/infrastructure/security/*` (3 files), `src/presentation/components/app-bootstrap-status.tsx`, `src/presentation/providers/app-bootstrap-provider.tsx`, `tests/unit/*` (5 files), `vitest.config.ts`, `scripts/validate-bootstrap.mjs`, `src/app/_layout.tsx`, `src/i18n/translations/{en,hr,sl}.ts`.

## Commit and push state

Committed and pushed to `origin/main` as `99e9d9c52865d0d736af765702f514637133caed`, verified via `git ls-remote` against the live remote during this consolidation. Approval workflow: CTO review → Founder commit approval → local commit → post-commit verification → Founder push approval → push → independent live-remote verification. See [[Care Circle Collaboration and Approval Workflow]].

**Android native runtime validation remains pending as the next controlled step.** See [[../00 Dashboard/Care Circle Dashboard|Care Circle Dashboard]].

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/releases/WP-04-Encrypted-SQLite-Bootstrap-and-Key-Management.md; PROJECT-STATUS.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Approved (recorded WP status: Implemented and statically validated; committed, pushed and verified; Android Runtime Validation Pending)
**Notes:** Structured consolidation of the full WP-04 release document (the longest and most detailed source in the repository) and PROJECT-STATUS.md's WP-04 sections. All security findings, remediation rounds, and limitations preserved in full. The release document's closing line ("No commit or push has occurred") is a stale pre-commit statement superseded by the verified Git baseline supplied for this consolidation (HEAD/origin/main/live-remote all match `99e9d9c52865d0d736af765702f514637133caed`). No claim of Android runtime validation, production readiness, or completion is made anywhere in this document.
