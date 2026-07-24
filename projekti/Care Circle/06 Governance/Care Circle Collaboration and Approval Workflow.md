# Care Circle Collaboration and Approval Workflow

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Previous revision status: Approved (2026-07-22)
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

## Controlled division of work — 2026-07-24

- **ChatGPT** remains the CTO, architect, reviewer and approval-gate controller.
- **ChatGPT Business/Codex** is the preferred local implementation and verification environment where its capabilities and safety boundaries permit, operating only under controlled permissions.
- **Claude Code** remains a backup execution, test and verification worker.
- **Founder** remains the final approver for scope, application identity, execution choices, commits, pushes and deployment.

This division changes no approval gate. No worker is authorized to commit, push, deploy, access secrets, perform a destructive action, or run an uncontrolled loop automatically. Codex sandbox escape or unrestricted external-tool execution always requires explicit user approval. Critical security, database and native-runtime changes require heightened CTO review and explicit Founder gates.

## Risk-mode discipline

Work packages are classified by risk (Low, Low-to-medium, High) and reviewed at a matching mode (Medium, High). WP-04 — encrypted database key management — was classified High risk and reviewed in High mode, resulting in two full CTO security-remediation rounds before the static checkpoint was reached. See [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management|WP-04 work package record]].

## Roadmap discipline

New ideas are recorded for a future phase and are not inserted into the current scope unless the roadmap is formally changed. See [[../03 Architecture/Care Circle Architecture Decision Register|ADR-010 Roadmap Discipline]].

## Native/prebuild stopping rule

If a work package would require missing Android/iOS native build tooling or would require inventing an application identifier (`android.package`/`ios.bundleIdentifier`) that has not been explicitly approved, the work package stops before the native/prebuild stage rather than installing tooling or inventing an identifier. The home x64 Android toolchain is now verified, but WP-04 remains stopped before native generation because the permanent application ID, dependency installation and device/emulator sequence require separate Founder decisions and controlled execution. See [[Care Circle Source of Truth and Repository Map]].

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** PROJECT-STATUS.md; docs/releases/WP-01 through WP-04 (commit/push-state sections)
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22; current-state Draft update prepared 2026-07-24
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (previous revision Approved; recorded workflow remains Approved, in active use)
**Notes:** The prior Approved revision reconstructs the workflow consistently applied across WP-01 through WP-04. The 2026-07-24 Draft update records the controlled ChatGPT/Codex/Claude division of work without changing any Founder approval, commit, push, deployment or heightened-review gate.
