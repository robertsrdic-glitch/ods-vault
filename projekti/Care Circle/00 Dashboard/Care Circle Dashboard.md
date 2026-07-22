# Care Circle Dashboard

Document status: Approved
Recorded project status: In Progress

## Product purpose

Care Circle is a calm, privacy-first, local-first medication organizer for individuals, families and caregivers. It organizes medications — it is not medical advice and not proof that medication was actually taken. See [[../01 Product/Care Circle Product Foundation]].

## Current phase

**Implementation** — current work package: WP-04 (Encrypted SQLite Bootstrap and Key Management).

## Current authoritative code state

- Repository: https://github.com/robertsrdic-glitch/care-circle.git
- Branch: `main`
- Current authoritative code SHA (HEAD = origin/main = live remote, verified during this consolidation): `99e9d9c52865d0d736af765702f514637133caed`
- Commit subject: "feat: add encrypted SQLite bootstrap foundation"
- Working tree: clean; staging: empty

## ODS source-of-truth statement

GitHub `care-circle` is authoritative for application code. This ODS Vault is authoritative for Care Circle project documentation, product decisions, architecture, security, governance and work-package history. Obsidian is only the local interface over the Git-tracked ODS Vault. See [[../06 Governance/Care Circle Source of Truth and Repository Map]].

## Work package status

| WP | Title | Status |
|---|---|---|
| WP-01 | Controlled Expo Application Bootstrap | Completed, committed, pushed and verified |
| WP-02 | Application Shell and Navigation Foundation | Completed, committed, pushed and verified |
| WP-03 | Localization Foundation | Completed, committed, pushed and verified |
| WP-04 | Encrypted SQLite Bootstrap and Key Management | Implemented and statically validated; committed, pushed and verified; **Android Runtime Validation Pending** |

Full detail: [[../05 Work Packages/Care Circle Work Package Register]].

> ⚠ **WP-04 is not runtime validated.** SQLCipher's actual on-device behavior is unverified beyond static and unit-test evidence (77 passing tests, full static validation suite). WP-04 must not be treated as Completed, production ready, or Android validated until native Android build and runtime evidence are captured and approved. See [[../04 Security/Care Circle Security Baseline]].

## Current blocker

**Android native environment and runtime validation.** No Java, Android SDK, `adb` or Gradle in the local environment; no `android.package`/`ios.bundleIdentifier` configured yet.

## Current next controlled step

The Care Circle ODS project foundation is published and independently verified on the live remote. This final lifecycle-approval commit exists locally only.

1. Obtain separate explicit Founder approval for pushing the Care Circle ODS final lifecycle commit.
2. Push that commit and independently verify local HEAD, origin/main and the live remote.
3. On the home x64 computer, synchronize both `care-circle` and `ods-vault`.
4. Perform a read-only Android development-environment assessment.
5. Obtain a separate explicit Founder decision for the permanent Android application ID.
6. Install or repair only required Android tooling through a separately approved task.
7. Perform WP-04 native Android build and SQLCipher runtime validation.
8. Complete the final WP-04 runtime CTO review and follow-up ODS/code commit and push workflow.
9. Define WP-05 before any WP-05 implementation begins.

WP-05 remains Proposed/Next and has not been started.

Full sequence: [[../06 Governance/Care Circle Project Status]].

## Canonical documents

**01 Product**
- [[../01 Product/Care Circle Product Foundation]]
- [[../01 Product/Care Circle MVP Scope]]

**02 UX and Design**
- [[../02 UX and Design/Care Circle UX and Design Foundation]]
- [[../02 UX and Design/Navigation Accessibility and Simplicity]]

**03 Architecture**
- [[../03 Architecture/Care Circle Architecture Overview]]
- [[../03 Architecture/Care Circle Architecture Decision Register]]
- [[../03 Architecture/Care Circle Domain Model Overview]]

**04 Security**
- [[../04 Security/Care Circle Security Baseline]]

**05 Work Packages**
- [[../05 Work Packages/Care Circle Work Package Register]]
- [[../05 Work Packages/WP-01 Controlled Expo Application Bootstrap]]
- [[../05 Work Packages/WP-02 Application Shell and Navigation Foundation]]
- [[../05 Work Packages/WP-03 Localization Foundation]]
- [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management]]

**06 Governance**
- [[../06 Governance/Care Circle Collaboration and Approval Workflow]]
- [[../06 Governance/Care Circle Source of Truth and Repository Map]]
- [[../06 Governance/Care Circle Project Status]]

**99 Source Register**
- [[../99 Source Register/Care Circle Source Register]]

## Last consolidation

2026-07-22 — controlled, comprehensive Care Circle ODS Vault consolidation from the Care Circle application repository at commit `99e9d9c52865d0d736af765702f514637133caed`. Read-only against the application repository; no code repository changes; no ODS commit or push performed as part of this consolidation.

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** PROJECT-STATUS.md; README.md; full docs/ tree
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Approved (recorded project status: In Progress)
**Notes:** Dashboard synthesizes all canonical Care Circle ODS documents created in this consolidation; it introduces no new facts beyond what is recorded and sourced in those documents.
