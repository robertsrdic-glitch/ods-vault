# Care Circle Source Register

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Previous revision status: Approved (2026-07-22)
Recorded register status: Approved

Maps every relevant Care Circle source document found in the application repository (at commit `99e9d9c52865d0d736af765702f514637133caed`) to its canonical ODS destination. No relevant source document was silently omitted.

**Source-document count:** 36 documentation-source rows (README.md + PROJECT-STATUS.md = 2; ADR-001–ADR-010 = 10; architecture documents (DM-001, TA-001) = 2; design documents (DS-001) = 1; product documents (PRODUCT-001, MVP-001) = 2; security documents (SEC-001) = 1; UX-001–UX-012 plus UX-P04 = 13; REL-000 plus WP-01–WP-04 = 5) **plus 6 supporting-source rows** (Git history; app.json; four verified 2026-07-24 home x64 evidence files) **= 42 total data rows** in the table below. The 14 Full-copy rows are unchanged. This preserves the previous correction of an earlier miscount of 33 that appeared only in the now-superseded first-pass evidence file and final report.

| Source repository | Source path | Source commit | Source title | Source type | Canonical ODS document | Treatment | Status |
|---|---|---|---|---|---|---|---|
| care-circle | README.md | 99e9d9c | Care Circle | README | [[../01 Product/Care Circle Product Foundation]] | Structured consolidation | Canonical |
| care-circle | PROJECT-STATUS.md | 99e9d9c | Project Status | Status report | [[../06 Governance/Care Circle Project Status]] | Structured consolidation | Canonical |
| care-circle | docs/product/PRODUCT-001-Product-Definition.md | 99e9d9c | Product Definition | Product | [[../01 Product/Care Circle Product Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/product/MVP-001-MVP-Scope.md | 99e9d9c | MVP Scope | Product | [[../01 Product/Care Circle MVP Scope]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-001-Medication-Event-Centered-Architecture.md | 99e9d9c | ADR-001 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-002-Local-First.md | 99e9d9c | ADR-002 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-003-Reliability-Before-Features.md | 99e9d9c | ADR-003 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-004-Family-and-Caregiver-First.md | 99e9d9c | ADR-004 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-005-Apple-Like-Simplicity.md | 99e9d9c | ADR-005 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-006-Two-Tap-Rule.md | 99e9d9c | ADR-006 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-007-Human-Confirmation.md | 99e9d9c | ADR-007 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-008-Calm-Design.md | 99e9d9c | ADR-008 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-009-Therapy-Terminology.md | 99e9d9c | ADR-009 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/adr/ADR-010-Roadmap-Discipline.md | 99e9d9c | ADR-010 | ADR | [[../03 Architecture/Care Circle Architecture Decision Register]] | Full copy | Canonical |
| care-circle | docs/architecture/DM-001-Final-Domain-Model.md | 99e9d9c | Final Domain Model | Architecture | [[../03 Architecture/Care Circle Domain Model Overview]] | Full copy | Canonical |
| care-circle | docs/architecture/TA-001-Technical-Architecture.md | 99e9d9c | Technical Architecture | Architecture | [[../03 Architecture/Care Circle Architecture Overview]] | Full copy | Canonical |
| care-circle | docs/design/DS-001-Final-Design-System.md | 99e9d9c | Final Design System | Design | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/security/SEC-001-Security-Baseline.md | 99e9d9c | Security Baseline | Security | [[../04 Security/Care Circle Security Baseline]] | Full copy | Canonical |
| care-circle | docs/ux/UX-001-Onboarding.md | 99e9d9c | Onboarding | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-002-Today.md | 99e9d9c | Today | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-003-People.md | 99e9d9c | People | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-004-Medicines.md | 99e9d9c | Medicines | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-005-Settings.md | 99e9d9c | Settings | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-006-Add-Therapy.md | 99e9d9c | Add Therapy | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-007-Therapy-Details-and-Editing.md | 99e9d9c | Therapy Details and Editing | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-008-Medication-Event-Actions.md | 99e9d9c | Medication Event Actions | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-009-Notifications-and-Reminders.md | 99e9d9c | Notifications and Reminder Experience | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-010-Inventory.md | 99e9d9c | Inventory | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-011-Search-Empty-and-Error-States.md | 99e9d9c | Search, Empty States and Error States | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-012-Navigation-and-Global-Interaction.md | 99e9d9c | Navigation and Global Interaction Rules | UX | [[../02 UX and Design/Care Circle UX and Design Foundation]] and [[../02 UX and Design/Navigation Accessibility and Simplicity]] | Structured consolidation | Canonical |
| care-circle | docs/ux/UX-P04-Simplicity-First.md | 99e9d9c | Simplicity First | UX / permanent rule | [[../02 UX and Design/Navigation Accessibility and Simplicity]] | Structured consolidation | Canonical |
| care-circle | docs/releases/REL-000-Bootstrap.md | 99e9d9c | Controlled Bootstrap | Release | [[../06 Governance/Care Circle Source of Truth and Repository Map]] (referenced, foundation history) | Indexed reference | Superseded by WP-01 |
| care-circle | docs/releases/WP-01-Controlled-Expo-Application-Bootstrap.md | 0de98ff | WP-01 | Work package | [[../05 Work Packages/WP-01 Controlled Expo Application Bootstrap]] | Structured consolidation (bullet lists condensed to prose; committed-file list added; pre-commit conditional language replaced with actual commit/push state) | Canonical |
| care-circle | docs/releases/WP-02-Application-Shell-and-Navigation-Foundation.md | f711dc6 | WP-02 | Work package | [[../05 Work Packages/WP-02 Application Shell and Navigation Foundation]] | Structured consolidation (bullet lists condensed to prose; committed-file list added; pre-commit conditional language replaced with actual commit/push state) | Canonical |
| care-circle | docs/releases/WP-03-Localization-Foundation.md | ae7a7f0 | WP-03 | Work package | [[../05 Work Packages/WP-03 Localization Foundation]] | Structured consolidation (bullet lists condensed to prose; committed-file list added; closing commit/push line retained as sourced, flagged stale in provenance notes) | Canonical |
| care-circle | docs/releases/WP-04-Encrypted-SQLite-Bootstrap-and-Key-Management.md | 99e9d9c | WP-04 | Work package | [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management]] | Structured consolidation (full technical content preserved) | Canonical |
| care-circle | git log / git show --stat (WP-01..WP-04 commits) | 0de98ff .. 99e9d9c | Commit history and file lists | Git history | [[../05 Work Packages/Care Circle Work Package Register]] and individual WP documents | Indexed reference | Canonical |
| care-circle | app.json (inspected, not copied) | 99e9d9c | Native configuration | Config | [[../04 Security/Care Circle Security Baseline]] and [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management]] | Summary (non-secret config values only) | Canonical |
| Care Circle Evidence (home x64) | `C:\Users\Robert\Desktop\Care Circle Evidence\Care-Circle-Home-X64-Clone-Evidence.txt` | 2026-07-24; 11,755 bytes; SHA-256 `f87406705ce74da41b28fa127a3ae77f07bc5583eb04a2f382b71c9d0f679ddf` | Home x64 clone and synchronization evidence | Supporting evidence | [[../00 Dashboard/Care Circle Dashboard]], [[../06 Governance/Care Circle Project Status]] and [[../06 Governance/Care Circle Source of Truth and Repository Map]] | Supporting evidence (indexed, not copied); authoritative state consolidated into ODS/Git | Verified |
| Care Circle Evidence (home x64) | `C:\Users\Robert\Desktop\Care Circle Evidence\Care-Circle-Home-X64-Android-Environment-Assessment-Evidence.txt` | 2026-07-24; 16,464 bytes; SHA-256 `eb5121459a0a5038f141b60cee0ebc80bf2c05b17dbd155888c7b05a23095585` | Android environment assessment evidence | Supporting evidence | [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management]], [[../06 Governance/Care Circle Project Status]] and [[../06 Governance/Care Circle Source of Truth and Repository Map]] | Supporting evidence (indexed, not copied); authoritative state consolidated into ODS/Git | Verified |
| Care Circle Evidence (home x64) | `C:\Users\Robert\Desktop\Care Circle Evidence\Care-Circle-Home-X64-Android-Installer-Preparation-Evidence.txt` | 2026-07-24; 12,598 bytes; SHA-256 `18340c4688559bf3c026cef515e85543ed4baa3c2f6d1f7fd28358436a87d279` | Android installer preparation evidence | Supporting evidence | [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management]], [[../06 Governance/Care Circle Project Status]] and [[../06 Governance/Care Circle Source of Truth and Repository Map]] | Supporting evidence (indexed, not copied); authoritative state consolidated into ODS/Git | Verified |
| Care Circle Evidence (home x64) | `C:\Users\Robert\Desktop\Care Circle Evidence\Care-Circle-Home-X64-Android-Tooling-Post-Install-Verification-Evidence.txt` | 2026-07-24; 19,506 bytes; SHA-256 `400204e9dd55fc31d0ad151c849035f4b94ce9d15a2ce277a98122465308f495` | Android tooling post-install verification and controlled Codex pilot evidence | Supporting evidence | [[../00 Dashboard/Care Circle Dashboard]], [[../05 Work Packages/WP-04 Encrypted SQLite Bootstrap and Key Management]], [[../06 Governance/Care Circle Collaboration and Approval Workflow]] and [[../06 Governance/Care Circle Project Status]] | Supporting evidence (indexed, not copied); authoritative state consolidated into ODS/Git | Verified |

## Notes on treatment categories

- **Full copy** — the source document's substantive content is reproduced with no shortening, condensation or merging beyond title/status normalization, added Obsidian links, a provenance footer, or a clearly separated current-status clarification.
- **Structured consolidation** — content from one or more sources has been reorganized, merged with another source, or had its wording/layout condensed (e.g. lists rewritten as prose) into a target document, without loss of the underlying material decisions or constraints.
- **Summary** — only the technically relevant, non-secret subset of a configuration source is recorded.
- **Indexed reference** — the source is acknowledged and pointed to but not reproduced, because it is either superseded (REL-000, by WP-01) or is procedural git metadata already reflected in the work-package documents.
- **Supporting evidence** — an external, hash-verified record is indexed but not copied into ODS. Its verified facts are consolidated into canonical ODS/Git state; the evidence file does not become a parallel documentation source of truth.

**2026-07-22 remediation note:** every row previously marked "Full copy" was re-audited against its actual target document. PRODUCT-001, DS-001, all 13 UX sources (UX-001–UX-012, UX-P04), and WP-01/WP-02/WP-03 were reclassified to "Structured consolidation" because their target documents condense list formatting into prose, merge multiple sources, and/or replace pre-commit conditional language with the actual commit/push state. ADR-001–ADR-010, DM-001, TA-001, MVP-001, and the SEC-001 portion of the Security Baseline remain "Full copy" — verified to contain no shortening or rewriting beyond the allowed exceptions above.

## Completeness statement

Every Markdown file under `docs/` in the Care Circle repository at commit `99e9d9c52865d0d736af765702f514637133caed`, plus `README.md` and `PROJECT-STATUS.md`, appears in this register. No `.md` or `.txt` documentation file in the repository was found outside the paths listed above (verified via a recursive file search excluding `node_modules` and `.git`).

The four 2026-07-24 home x64 evidence files are indexed as Supporting evidence with verified byte sizes and SHA-256 hashes. They are not Full copies and do not alter the count of 36 documentation sources or 14 Full-copy rows.

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** entire `docs/` tree, README.md, PROJECT-STATUS.md
**Source commit or commit range:** 0de98ffae03f5303dc3866ae5cf079d3625acbf6 .. 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22; current-state Draft update prepared 2026-07-24
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (previous revision Approved; recorded register status remains Approved)
**Notes:** This register remains the completeness proof for the 36 application documentation sources. The Draft update adds four independently hash-verified Supporting evidence rows, bringing supporting sources to 6 and total table rows to 42 without changing the 14 Full-copy rows.
