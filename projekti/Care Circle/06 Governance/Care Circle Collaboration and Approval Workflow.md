# Care Circle Collaboration and Approval Workflow

Document status: Approved
Recorded workflow status: Approved (in active use)

## Approval sequence

Every Care Circle work package follows the same controlled sequence before it reaches the remote repository:

1. **ChatGPT CTO review** — the implementation is reviewed for architecture, security and scope compliance before anything is committed.
2. **Founder commit approval** — the Founder explicitly approves creating a local commit; no commit happens automatically after CTO review alone.
3. **Local commit** — the approved change is committed to the local `main` branch.
4. **Post-commit verification** — the resulting commit is checked (SHA, subject, file list) before proceeding.
5. **Separate Founder push approval** — pushing to the remote is a distinct approval from the commit approval; the two are never bundled.
6. **Push** — the commit is pushed to `origin/main`.
7. **Independent live-remote verification** — the live remote is checked directly (e.g. `git ls-remote`) to confirm the push landed as expected, rather than trusting local state alone.

This sequence was applied to WP-01, WP-02, WP-03 and WP-04. See [[../05 Work Packages/Care Circle Work Package Register|Care Circle Work Package Register]].

## Risk-mode discipline

Work packages are classified by risk (Low, Low-to-medium, High) and reviewed at a matching mode (Medium, High). WP-04 — encrypted database key management — was classified High risk and reviewed in High mode, resulting in two full CTO security-remediation rounds before the static checkpoint was reached. See [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management|WP-04 work package record]].

## Roadmap discipline

New ideas are recorded for a future phase and are not inserted into the current scope unless the roadmap is formally changed. See [[../03 Architecture/Care Circle Architecture Decision Register|ADR-010 Roadmap Discipline]].

## Native/prebuild stopping rule

If a work package would require Android/iOS native build tooling that is not present in the local environment (Java, Android SDK, `adb`, Gradle) or would require inventing an application identifier (`android.package`/`ios.bundleIdentifier`) that has not been explicitly approved, the work package stops before the native/prebuild stage rather than installing tooling or inventing an identifier. This rule produced the current Android runtime validation blocker on WP-04. See [[Care Circle Source of Truth and Repository Map]].

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** PROJECT-STATUS.md; docs/releases/WP-01 through WP-04 (commit/push-state sections)
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Approved (recorded workflow status: Approved, in active use)
**Notes:** Structured consolidation of the approval workflow as consistently described across all four WP release documents and PROJECT-STATUS.md. No separate standalone "collaboration rules" document exists in the Care Circle repository (unlike NorthStar's Collaboration Rules) — this document reconstructs the workflow from its consistent application across all four work packages.
