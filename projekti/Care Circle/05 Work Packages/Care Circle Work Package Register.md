# Care Circle Work Package Register

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Recorded project status: In Progress

Tracks every Care Circle implementation work package in the controlled, CTO-reviewed, Founder-approved sequence defined by [[Care Circle Collaboration and Approval Workflow]] and [[../03 Architecture/Care Circle Architecture Decision Register|ADR-010 Roadmap Discipline]].

## Status table

| WP | Title | Status | Commit SHA |
|---|---|---|---|
| WP-01 | Controlled Expo Application Bootstrap | Completed, committed, pushed and verified | `0de98ffae03f5303dc3866ae5cf079d3625acbf6` |
| WP-02 | Application Shell and Navigation Foundation | Completed, committed, pushed and verified | `f711dc67bab8a1e36c01c9ca1e37c11c5a9a8982` |
| WP-03 | Localization Foundation | Completed, committed, pushed and verified | `ae7a7f0cefe6972daa118ab703611d3feeed8a19` |
| WP-04 | Encrypted SQLite Bootstrap and Key Management | Implemented and statically validated; committed, pushed and verified; **Android Runtime Validation Pending** | `99e9d9c52865d0d736af765702f514637133caed` |
| WP-05 | Drizzle schema and migration foundation | Proposed / Next — not started | — |

WP-04 is **never** to be described as Completed, runtime validated, production ready, or Android validated. See [[../04 Security/Care Circle Security Baseline|Care Circle Security Baseline]].

## WP-01 — Controlled Expo Application Bootstrap

- **Objective:** Create the smallest controlled Expo/React Native application foundation without implementing Care Circle product functionality.
- **Scope:** Expo SDK 57 baseline, React Native, strict TypeScript, Expo Router under `src/app`, Expo Development Client, minimal technical bootstrap screen, layered directory structure (Presentation/Application/Domain/Infrastructure/Shared), test directories, ESLint, bootstrap/architecture validation script, Android JS bundle validation.
- **Validation:** `npm run typecheck`; ESLint; bootstrap validation; architecture import validation; `npx expo install --check`; Expo Doctor; Android JavaScript bundle export; secret-file detection; forbidden dependency detection.
- **Commit:** `0de98ffae03f5303dc3866ae5cf079d3625acbf6` — "chore: bootstrap Care Circle Expo application"
- **Status:** Completed, committed, pushed and verified.

Full record: [[WP-01 Controlled Expo Application Bootstrap]].

## WP-02 — Application Shell and Navigation Foundation

- **Objective:** Establish the approved Care Circle application shell and primary navigation without implementing business functionality.
- **Scope:** Stable Expo Router JavaScript tabs; exactly four destinations (Today, People, Medicines, Settings) with Today as the initial route; safe-area-aware screen wrapper; automatic light/dark appearance; minimal semantic theme tokens; accessible navigation labels.
- **Validation:** TypeScript checking; ESLint (no warnings); navigation structure/tab-count/tab-order validation; dependency validation; route/domain-boundary validation; Expo Doctor 20/20; Android JS bundle export.
- **Commit:** `f711dc67bab8a1e36c01c9ca1e37c11c5a9a8982` — "feat: add Care Circle application shell and navigation"
- **Status:** Completed, committed, pushed and verified.

Full record: [[WP-02 Application Shell and Navigation Foundation]].

## WP-03 — Localization Foundation

- **Objective:** Establish the localization foundation for Slovenian, Croatian and English, and replace hardcoded navigation/placeholder text with centralized translations.
- **Scope:** Centralized i18n module at `src/i18n/`; typed translation resolver (Approach B, no external i18n library); device-locale resolution with English fallback; localized navigation and placeholder text on all four routes; translation-key parity validation.
- **Validation:** TypeScript, ESLint, validator (WP-02 + WP-03 checks), `npm run check`, Expo Doctor 20/20, Android JS bundle export, secret scan, UTF-8-without-BOM.
- **Commit:** `ae7a7f0cefe6972daa118ab703611d3feeed8a19` — "feat: add Care Circle localization foundation"
- **Status:** Completed, committed, pushed and verified.

Full record: [[WP-03 Localization Foundation]].

## WP-04 — Encrypted SQLite Bootstrap and Key Management

- **Risk classification:** High (security-critical infrastructure).
- **Objective:** Establish an encrypted local-first SQLite foundation using SQLCipher, with a fail-closed bootstrap state machine and a securely stored 256-bit database key. Infrastructure only — no schema, no product tables, no repositories, no business logic.
- **Implementation scope:** SQLCipher-enabled `expo-sqlite`; 256-bit key via `expo-crypto`; storage via `expo-secure-store`; fail-closed four-state bootstrap matrix; SQLCipher opening/verification pipeline; calm `AppBootstrapProvider` startup gate; dev-only diagnostic on a fully separate database/key; `android.allowBackup: false`.
- **Security remediation:** Two CTO security-remediation rounds (4 findings + 3 findings, all fixed). See [[../04 Security/Care Circle Security Baseline|Care Circle Security Baseline]] for the full list.
- **Static validation:** 77 unit tests across 5 files; TypeScript, ESLint, validator, `npm run check`, Expo Doctor 20/20, `expo config --type public`, Android JS bundle export, secret scan, UTF-8-without-BOM — all PASS.
- **Commit:** `99e9d9c52865d0d736af765702f514637133caed` — "feat: add encrypted SQLite bootstrap foundation" — committed, pushed and GitHub-verified (origin/main and live remote match).
- **Android runtime blocker:** No Java, Android SDK, `adb` or Gradle in the local environment; no `android.package`/`ios.bundleIdentifier` configured. Native/prebuild stage was stopped per the mandatory rules rather than inventing an identifier or installing tooling.
- **Status:** Static checkpoint implemented, CTO approved, committed, pushed and verified; Android runtime validation pending.

Full record: [[WP-04 Encrypted SQLite Bootstrap and Key Management]].

## WP-05 — Drizzle schema and migration foundation (Proposed / Next)

- **Status:** Proposed. Not started. No commit exists.
- **Expected scope:** Drizzle ORM/Kit schema and migration foundation, per [[../03 Architecture/Care Circle Architecture Overview|Care Circle Architecture Overview]]. Must not be described as implemented until a corresponding work-package record and commit exist.

## Approval workflow (applies to every work package)

1. ChatGPT CTO review of the implementation.
2. Founder commit approval.
3. Local commit.
4. Post-commit verification.
5. Separate Founder push approval.
6. Push.
7. Independent live-remote verification (`git ls-remote`).

See [[Care Circle Collaboration and Approval Workflow]] for the full governance record of this process.

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/releases/WP-01 through WP-04; PROJECT-STATUS.md; git log (commit metadata)
**Source commit or commit range:** 0de98ffae03f5303dc3866ae5cf079d3625acbf6 .. 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (recorded project status: In Progress; see per-WP status above)
**Notes:** Commit SHAs cross-checked against `git log`/`git cat-file` in the live Care Circle repository during this consolidation; all four exist as stated. WP-04 status language matches the exact required phrasing and is never rendered as "Completed" anywhere in this register.
