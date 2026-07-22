# WP-02 — Application Shell and Navigation Foundation

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Recorded WP status: Completed, committed, pushed and verified
Date: 2026-07-21
Risk: Low to medium
Mode: Medium
Commit: `f711dc67bab8a1e36c01c9ca1e37c11c5a9a8982`

## Objective

Establish the approved Care Circle application shell and primary navigation without implementing business functionality.

## Implemented

- stable Expo Router JavaScript tabs;
- exactly four bottom-navigation destinations: Today, People, Medicines, Settings, in this order;
- Today as the initial route;
- text labels and icons;
- safe-area-aware screen wrapper;
- automatic light and dark appearance;
- minimal semantic theme tokens;
- accessible navigation labels;
- Expo Font support required by the icon dependency;
- thin route files;
- expanded architecture and route validation.

## Dependencies added

`@expo/vector-icons`, `expo-font`, `expo-system-ui`.

## Excluded

Floating Action Button; Add Person, Add Therapy and Add Medicine actions; Medication Events; database and persistence; SQLCipher and migrations; notifications and reminders; PIN and biometrics; backup and restore; product forms; localization; complete design-system implementation; business state and domain behavior.

## Architecture safeguards

- route files remain thin;
- navigation imports no infrastructure or persistence modules;
- domain imports no Expo or React Native modules;
- no global business-state store was introduced;
- no unstable native-tabs API is used.

## Validation

TypeScript checking; ESLint without warnings; navigation structure validation; exact tab-count validation; tab-order validation; required/forbidden dependency validation; route-boundary validation; domain-boundary validation; Expo dependency compatibility validation; Expo Doctor 20/20; Android JavaScript bundle export — all PASS.

## Committed files

`PROJECT-STATUS.md`, `app.json`, `docs/releases/WP-02-Application-Shell-and-Navigation-Foundation.md`, `package-lock.json`, `package.json`, `scripts/validate-bootstrap.mjs`, `src/app/(tabs)/_layout.tsx`, `src/app/(tabs)/index.tsx`, `src/app/(tabs)/medicines.tsx`, `src/app/(tabs)/people.tsx`, `src/app/(tabs)/settings.tsx`, `src/app/_layout.tsx`, `src/app/index.tsx`, `src/design-system/tokens.ts`, `src/presentation/components/route-placeholder.tsx`, `src/presentation/components/screen.tsx`, `src/presentation/hooks/use-app-theme.ts` — 17 files changed, 12539 insertions(+), 11952 deletions(-).

## Commit and push state

Completed, committed, pushed and verified via the same CTO/Founder approval workflow as WP-01. See [[Care Circle Collaboration and Approval Workflow]].

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/releases/WP-02-Application-Shell-and-Navigation-Foundation.md
**Source commit or commit range:** f711dc67bab8a1e36c01c9ca1e37c11c5a9a8982
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (recorded WP status: Completed, committed, pushed and verified)
**Notes:** Structured consolidation of the WP-02 release document: bullet lists condensed into semicolon-joined prose, a committed-file list added from `git show --stat`, and the source's pre-commit conditional commit/push language replaced with the actual commit/push state now that the commit is verified. No decision, scope item, or validation result was dropped or reinterpreted.
