# Care Circle Source of Truth and Repository Map

Document status: Approved
Previous revision status: Approved (2026-07-22)
Recorded governance status: Approved

## Authoritative locations

- **Care Circle application repository (code):** home x64 path `C:\Users\Robert\Projects\care-circle`; other-device path recorded by the previous revision `C:\Users\rober\Projects\care-circle`; GitHub: https://github.com/robertsrdic-glitch/care-circle.git — authoritative for application code.
- **ODS Vault (this vault):** home x64 path `C:\Users\Robert\Documents\ods-vault`; other-device path recorded by the previous revision `C:\Users\rober\Documents\ods-vault`; target folder `projekti/Care Circle` — ODS/GitHub is authoritative for Care Circle project documentation, product decisions, architecture, security, governance and work-package history.
- **Supporting evidence directory:** `C:\Users\Robert\Desktop\Care Circle Evidence` — holds independently verifiable supporting records; indexed evidence supports but does not replace the canonical state consolidated into ODS/Git.
- **Obsidian** is only the local interface over the Git-tracked ODS Vault; it holds no authority of its own.
- **Conversation history:** ChatGPT and Claude conversations are working context only and are not authoritative project-state sources.

## Current verified code baseline

- Branch: `main`
- HEAD / origin/main / live remote (all matching at time of this consolidation): `99e9d9c52865d0d736af765702f514637133caed`
- Commit subject: "feat: add encrypted SQLite bootstrap foundation"
- Working tree: clean; staging: empty

The home x64 ODS Vault is on `main` at `ebb46c05e5c47baec3c9935e864cc5207068257a`, matching `origin/main` and live GitHub with a clean working tree and empty staging at the start of the 2026-07-24 Draft consolidation.

## Repository contents (Care Circle app repo, `docs/`)

| Category | Path prefix |
|---|---|
| Project status | `PROJECT-STATUS.md`, `README.md` |
| Architecture Decision Records | `docs/adr/ADR-001` .. `ADR-010` |
| Domain and technical architecture | `docs/architecture/DM-001`, `docs/architecture/TA-001` |
| Design system | `docs/design/DS-001` |
| Product | `docs/product/PRODUCT-001`, `docs/product/MVP-001` |
| Security | `docs/security/SEC-001` |
| UX flows | `docs/ux/UX-001` .. `UX-012`, `docs/ux/UX-P04` |
| Release / work-package records | `docs/releases/REL-000`, `docs/releases/WP-01` .. `WP-04` |

See [[../99 Source Register/Care Circle Source Register|Care Circle Source Register]] for the complete mapping of every source document to its ODS destination.

## Native/prebuild stopping rule

See [[Care Circle Collaboration and Approval Workflow]].

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** repository root structure; PROJECT-STATUS.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22; current-state Draft update prepared 2026-07-24
**Canonical ODS status:** Approved (previous revision Approved; recorded governance status remains Approved)
**Notes:** Baseline SHAs and branch/remote state were verified directly against both live repositories (`git rev-parse`, `git ls-remote`). The 2026-07-24 update adds device-specific home x64 paths, the verified evidence directory and the explicit exclusion of conversation history from authoritative project state.
