# WP-03 — Localization Foundation

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Recorded WP status: Completed, committed, pushed and verified
Date: 2026-07-21
Risk: Low
Mode: Medium
Commit: `ae7a7f0cefe6972daa118ab703611d3feeed8a19`

## Objective

Establish the localization foundation for Slovenian, Croatian and English, and replace hardcoded user-facing navigation and placeholder text in the application shell with centralized translations. Localization infrastructure only — no manual language selection, no persistence, no product functionality.

## Implemented scope

- centralized i18n module at `src/i18n/`;
- translation resources for English, Slovenian and Croatian;
- locale normalization and supported-locale selection;
- English fallback for missing or unsupported locales;
- localized navigation labels (Today, People, Medicines, Settings);
- localized placeholder screen titles and messages on all four routes;
- translation-key parity validation across all three locales;
- validation that route/tab-layout files contain no hardcoded navigation or placeholder text and do not import `expo-localization` directly.

## Language-selection rules

Device locale only: `sl`/`sl-*` → Slovenian; `hr`/`hr-*` → Croatian; any other/unsupported locale → English (safe fallback). Manual language selection and persistence of language choice are explicitly out of scope.

## Dependencies added

`expo-localization` (`~57.0.1`), registered as an Expo config plugin in `app.json`.

## Translation-layer approach

**Approach B — a tiny internal typed translation resolver** was chosen over an external library (e.g. `i18n-js`), because the scope was eight flat translation keys across three locales with no pluralization, interpolation or dynamic loading. A typed `Record<SupportedLocale, Translations>` resolver gives compile-time key-parity enforcement without a runtime dependency.

## Translation structure

```
src/i18n/
  index.ts               # resolveLocale(), getTranslations(), useTranslation()
  locale.ts               # SupportedLocale, normalizeLocale(), DEFAULT_LOCALE
  translations/
    en.ts / sl.ts / hr.ts
```

Keys: `nav.today`, `nav.people`, `nav.medicines`, `nav.settings`, `placeholder.today`, `placeholder.people`, `placeholder.medicines`, `placeholder.settings`.

## Architecture boundaries preserved

Route files call `useTranslation()` only, no direct `expo-localization` import; only `src/i18n/index.ts` imports `expo-localization`; domain layer imports no localization/Expo/React Native modules; tab count remains exactly four in the same order.

## Explicit exclusions

Manual language selection; a Settings language screen; persistence of language choice; SQLite/AppSettings/SQLCipher/Drizzle; notifications/reminders; PIN/biometrics; backup/restore; date/time or dose formatting; pluralization beyond current strings; RTL support; remote/dynamic/AI translation; medical terminology content; new screens/onboarding/FAB behavior.

## Validation results

TypeScript PASS; ESLint PASS (no warnings); validator PASS (WP-02 + WP-03 banners); `npm run check` PASS; `npx expo install --check` PASS; Expo Doctor 20/20; Android JS bundle export PASS; secret/prohibited-file scan clean; UTF-8-without-BOM verified.

## Committed files

`PROJECT-STATUS.md`, `app.json`, `docs/releases/WP-03-Localization-Foundation.md`, `package-lock.json`, `package.json`, `scripts/validate-bootstrap.mjs`, `src/app/(tabs)/_layout.tsx`, `src/app/(tabs)/index.tsx`, `src/app/(tabs)/medicines.tsx`, `src/app/(tabs)/people.tsx`, `src/app/(tabs)/settings.tsx`, `src/i18n/index.ts`, `src/i18n/locale.ts`, `src/i18n/translations/en.ts`, `src/i18n/translations/hr.ts`, `src/i18n/translations/sl.ts` — 16 files changed, 614 insertions(+), 50 deletions(-).

## Commit and push state

Completed, committed, pushed and verified via the same CTO/Founder approval workflow as WP-01 and WP-02. See [[Care Circle Collaboration and Approval Workflow]].

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/releases/WP-03-Localization-Foundation.md
**Source commit or commit range:** ae7a7f0cefe6972daa118ab703611d3feeed8a19
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (recorded WP status: Completed, committed, pushed and verified)
**Notes:** Structured consolidation of the WP-03 release document: bullet lists condensed into semicolon-joined prose, a committed-file list added from `git show --stat`. The source document's own closing line ("No commit or push has occurred...") reflects its pre-commit authoring moment; the verified Git history confirms this WP is committed and pushed, and the ODS "Commit and push state" section reflects that, not the stale source wording. No decision, scope item, or validation result was dropped or reinterpreted.
