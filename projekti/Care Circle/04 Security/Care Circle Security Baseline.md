# Care Circle Security Baseline

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Previous revision status: Approved (2026-07-22)
Source decision status (SEC-001 baseline): Approved
Recorded WP-04 status: Implemented and statically validated; committed, pushed and verified; Android Runtime Validation Pending

## SEC-001 baseline (approved, derived from TA-001)

This baseline does not introduce new product scope. It records mandatory security constraints already approved in [[../03 Architecture/Care Circle Architecture Overview|Care Circle Architecture Overview]] (TA-001).

- medication data stays local in the MVP;
- SQLite database is encrypted at rest;
- database key is protected by the platform key store;
- PIN is never stored in plaintext;
- biometrics use the operating-system prompt;
- backup is encrypted before leaving the app sandbox;
- backup password cannot be recovered by Care Circle;
- restore uses staging and atomic replacement;
- photographs remain inside the encrypted data boundary;
- logs exclude secrets and unnecessary medication details;
- no advertising or analytics SDK;
- no cloud upload;
- destructive actions require explicit confirmation.

## WP-04 implementation: encrypted SQLite bootstrap and key management

**Status: Implemented and statically validated, committed, pushed and verified; Android Runtime Validation Pending.**

Commit: `99e9d9c52865d0d736af765702f514637133caed`. Risk classification: High (security-critical infrastructure). See [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management|WP-04 work package record]] for full implementation detail, remediation history and test coverage.

### Implemented security properties

- SQLCipher-enabled SQLite foundation (`expo-sqlite` + `useSQLCipher: true`);
- 256-bit database key, generated with `expo-crypto` native randomness;
- key stored exclusively via `expo-secure-store`, `requireAuthentication: false` (no biometric gate in WP-04);
- `android.allowBackup: false`, and `expo-secure-store`'s Android backup-rule injection disabled (`configureAndroidBackup: false`);
- fail-closed bootstrap state machine across all four database-file/key combinations, plus SecureStore-unavailable and file-state-check-failed cases;
- SQLCipher key applied before the first database read;
- `sqlite_master` proof read (a wrong key fails here);
- `cipher_version` verification;
- `foreign_keys = ON`, `journal_mode = WAL`, `busy_timeout = 5000`, each asserted by value;
- `PRAGMA quick_check` required to return exactly `"ok"`;
- active database deletion is structurally prohibited in the diagnostic cleanup path;
- sanitized startup and error behavior — `DatabaseBootstrapResult` is a closed union with no file path, SQL text, key or native stack trace ever exposed;
- process-local serialized SecureStore key writes (`writeKeyIfAbsent`), with post-write verification — an honest process-local guarantee, not native atomicity;
- no reset, key deletion, key rotation, rekeying or plaintext-to-encrypted migration path exists anywhere in WP-04.

### Security remediation history

Two CTO security-remediation rounds were completed before this checkpoint, both within the same uncommitted WP-04 change set at the time:

**Round 1 (4 findings, all fixed):**
1. Bootstrap could reject into presentation — fixed via a `runSafely()` wrapper; `bootstrap()` can no longer reject.
2. File-state failure didn't take strict precedence — fixed by checking file-state before ever consulting the key store.
3. SecureStore writes could overwrite an existing key — fixed via a new read-before-write `write-key-if-absent.ts` adapter.
4. Diagnostic cleanup wasn't fail-safe or verified — fixed via a `finally`-block, verified-cleanup `diagnostic-cleanup.ts` module.

**Round 2 (3 findings, all fixed):**
1. Cleanup verification had a false-positive path — `diagnosticDatabaseFileExists()` now throws instead of returning a false "does not exist".
2. The diagnostic could open a database before clean state was verified — fixed via a new `verifyCleanDiagnosticState()` gate.
3. `writeKeyIfAbsent()` had a real (not theoretical) read/write race — fixed via process-wide FIFO serialization plus post-write verification, after directly inspecting the installed `expo-secure-store` SDK 57 API and confirming no atomic create-only primitive exists.

### Validation evidence

- 77 passing Vitest unit tests across 5 files (up from 37 in the original implementation, 63 after round 1);
- `npm run check` (typecheck + lint + validator + unit tests): PASS;
- `npx expo-doctor`: PASS, 20 of 20 checks;
- `npx expo config --type public`: confirmed `android.allowBackup: false` and both native plugin configs;
- Android JavaScript bundle export: PASS;
- secret and prohibited-file scan: no secrets, no `.env` files, no hardcoded 64-character hex literal;
- UTF-8-without-BOM verified on all new/modified files.

### Android runtime validation — pending, not yet performed

**Historical environment record — 2026-07-21:** Android native build and runtime validation had not occurred. The computer inspected at that checkpoint had no Java installation, no Android SDK (`ANDROID_HOME`), no `adb` and no Gradle, and `app.json` had no `android.package`/`ios.bundleIdentifier` configured. Per the WP-04 rules, the native/prebuild stage stopped rather than inventing an identifier or installing tooling. This paragraph is preserved as evidence of the 2026-07-21 environment and is no longer the current home x64 tooling state.

**Current-state update — 2026-07-24:** Eclipse Temurin JDK 17.0.19 is installed, and `JAVA_HOME` points to that verified JDK 17 installation. The pre-existing JDK 25 remains installed. Android Studio stable 2026.1.2 is installed, and `ANDROID_HOME` points to `C:\Users\Robert\AppData\Local\Android\Sdk`. Android Platform 36.1, Build-Tools 36.0.0, Platform-Tools 37.0.0, Command-line Tools 22.0 and Emulator 36.6.11 are installed; WHPX is available and usable; and the required user `Path` entries are correctly persisted.

No Android Virtual Device or Android system image exists yet. No project dependency installation, Expo prebuild, `android/` generation, native build, APK installation or SQLCipher Android runtime validation has occurred. No application identifier has been invented. Tooling readiness is not Android runtime validation.

**WP-04 remains: Implemented and statically validated; committed, pushed and verified; Android Runtime Validation Pending.**

SQLCipher's actual on-device behavior is therefore **unverified beyond static and unit-test evidence**. This includes:

- SQLCipher's actual native presence and runtime behavior (as opposed to the config-plugin build flag and TypeScript-level verification pipeline);
- the composition root and dev-only diagnostic, which are not unit tested by design and depend on real native modules;
- any iOS-specific runtime behavior (`NSFaceIDUsageDescription` handling was disabled but not runtime-validated).

**WP-04 must not be documented, described, or treated as fully completed, runtime validated, production ready, or Android validated anywhere in this vault.** The correct status phrase is always: *Implemented and statically validated; committed, pushed and verified; Android Runtime Validation Pending.*

### WP-04 explicit exclusions

Not implemented in WP-04: Drizzle ORM/Kit, application migrations, schema versioning, domain tables, repositories, CRUD, Medication Events, reminders, notifications, PIN, biometrics, App Lock, backup, restore, photos, cloud sync, analytics, crash reporting, database reset, key deletion, key rotation, rekeying, plaintext-to-encrypted migration, production signing, store deployment.

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/security/SEC-001-Security-Baseline.md; docs/releases/WP-04-Encrypted-SQLite-Bootstrap-and-Key-Management.md; PROJECT-STATUS.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22; current-state Draft update prepared 2026-07-24
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (previous revision Approved; source decision status, SEC-001 baseline, remains Approved; recorded WP-04 status remains: Implemented and statically validated; committed, pushed and verified; Android Runtime Validation Pending)
**Notes:** SEC-001 was copied in full in the previous Approved revision. The WP-04 section is a structured consolidation of the WP-04 release document and PROJECT-STATUS.md. The 2026-07-24 Draft update preserves the earlier environment statement as dated historical evidence and adds only the verified current home x64 tooling state; it changes no security architecture, database design, key-management rule or WP scope.
