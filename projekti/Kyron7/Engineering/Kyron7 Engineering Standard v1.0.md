# Kyron7 Engineering Standard v1.0

**Status:** Adopted  
**Date:** 2026-07-16  
**Owner:** Robert Srdič Senčar, Founder  
**Applies to:** All Kyron7 software projects  

---

## 1. Git Workflow

All production repositories use the standard pull request workflow:

- Branch from `main` for every change.
- One logical change per pull request.
- Squash merge to `main`.
- Delete the feature branch after merge.
- `main` is always deployable.

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): summary

body (optional)

footer (optional)
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `security`, `ci`.

For experimental repositories or personal prototypes, the Founder may explicitly approve a simplified workflow. All production repositories continue to require the standard pull request workflow.

---

## 2. AI Agent Responsibilities

When an AI agent (Claude, Hermes, ChatGPT, or other) is engaged on a Kyron7 project:

- The agent works only from the current task specification.
- The agent does not introduce unsolicited scope changes.
- The agent does not modify unrelated files, services, or repositories.
- The agent does not push to `main` directly.
- The agent does not create or delete Git tags without explicit Founder approval.
- The agent flags security concerns immediately and halts if a destructive or irreversible action is contemplated.
- The agent never prints, logs, or commits secrets.
- The agent verifies its own work before reporting completion.
- The agent distinguishes between what it has actually done and what it plans to do.

If multiple technically valid approaches exist and none is clearly superior, the AI agent must explain the trade-offs and request a decision instead of selecting one silently.

---

## 3. Release Checklist

A release is not published until every checkbox is verified:

- [ ] All PRs merged
- [ ] CI green
- [ ] Independent review completed
- [ ] Secret scan completed
- [ ] Changelog updated
- [ ] Rollback documented
- [ ] ODS Vault updated
- [ ] Release tag created
- [ ] Production verification completed
- [ ] Freeze confirmed

No release proceeds with an unchecked box unless the Founder grants a documented exception.

---

## 4. GitHub Governance

### Repository Categories

| Category | Path pattern | Purpose | Examples |
|---|---|---|---|
| `product/` | `Kyron7/<product>` | Product-specific application code | `northstar-artifact-gateway` |
| `infra/` | `Kyron7/<infra>` | Infrastructure, deployment, ops tooling | Terraform, Dockerfiles, CI templates |
| `platform/` | `Kyron7/<platform>` | Cross-cutting platform services | Auth, logging, monitoring |
| `docs/` | `Kyron7/<docs>` | Engineering documentation (if not in ODS Vault) | API specs, architecture diagrams |
| `shared/` | `Kyron7/<shared>` | Shared libraries, SDKs, reusable packages and components | UI kit, design tokens, utility libraries |

### Visibility Rules

- All product and infrastructure repositories are **private** by default.
- A repository may be made public only with explicit Founder approval.
- Documentation repositories may be public if they contain no proprietary architecture details.

### Branch Protection

- `main` branches have protection rules enabled.
- Force pushes to `main` are prohibited.
- Branch deletion of `main` is prohibited.
- At least one approval is required for production repositories (Founder or designated reviewer).

---

## 5. Security Change Policy

### Credential Management

- No secrets, tokens, or credentials are committed to Git repositories.
- Secrets are stored in environment files (`.env`) that are gitignored.
- `.env.example` files contain only placeholder values.
- Secret scanning is performed before every push and every release.
- Every production credential must have a documented owner, purpose, scope and rotation procedure.

### Dependency Management

- Dependencies are reviewed before addition.
- `package-lock.json` or equivalent lockfile is committed.
- Security advisories are monitored.
- Dependencies are updated promptly when security patches are available.

### Access Control

- GitHub organization roles follow least-privilege principles.
- Deploy keys are scoped to a single repository.
- No personal SSH keys are used for automated operations.
- OAuth tokens are scoped to the minimum required permissions.

---

## 6. Documentation Policy

### Single Source of Truth

- The ODS Vault (`projekti/` in `ods-vault` repository) is the **only** documentation source for Kyron7.
- GitHub repositories contain **only** source code.
- Documentation is not migrated to GitHub wikis, Notion, or other platforms.

### What Goes Where

| Content | Location |
|---|---|
| Project specs, product decisions, roadmaps | ODS Vault: `projekti/<project>/01 Product/` |
| Architecture, engineering notes, security records | ODS Vault: `projekti/<project>/03 Engineering/` |
| Design deliverables (HTML, PDF, reviews) | ODS Vault: `projekti/<project>/04 Design Deliverables/` |
| Source code, tests, build config | GitHub: `Kyron7/<repo>` |
| Engineering standards (this document) | ODS Vault: `projekti/Kyron7/Engineering/` |

### Architecture Decision Records

Architecture Decision Records (ADR) are stored in the ODS Vault and referenced from repositories when appropriate.

### Commit Documentation Rule

When documentation is updated in the ODS Vault, the commit message follows the conventional commit format:

```
docs(scope): description
```

When code is committed to a GitHub repository, documentation in the ODS Vault is updated in a separate commit (not mixed into the code commit).

---

## 7. Sprint and Freeze Protocol

### Sprint Lifecycle

1. **Assess** — inspect current state, identify risks.
2. **Plan** — produce a written plan, get Founder approval.
3. **Implement** — make changes in feature branches.
4. **Verify** — run tests, security scans, regression suites.
5. **Freeze** — no further changes after verification.
6. **Document** — update ODS Vault with completion record.
7. **Tag** — create a Git tag marking the frozen state.

### Freeze Rules

- A frozen sprint is not modified.
- Bug fixes go in a new sprint.
- The freeze commit hash is recorded in the ODS Vault completion record.
- Rollback is always documented before the next sprint begins.

---

## 8. Review and Revision

This standard is reviewed and revised by the Founder. Revisions are tracked in the ODS Vault commit history. The current version supersedes all prior drafts and informal practices.

### Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-07-16 | Initial adoption. Git workflow, AI agent responsibilities, release checklist, GitHub governance, security policy, documentation policy, sprint protocol. |
