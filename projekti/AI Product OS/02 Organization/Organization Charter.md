# Organization Charter

Version: 1.0
Status: Approved
Governance State: Frozen — modification requires an approved RFC. See [[Request for Change (RFC) Process]].
Owner: Founder

---

# Purpose

Defines the organizational structure, roles, responsibilities, ownership, and approval model shared by every product built on the AI Product OS.

---

# Organizational Structure

The organization is role-based, not tool-based. Each role owns a defined domain of the repository. Roles persist across products; the individuals or tools performing them may change.

---

# Roles

**Founder**
Final decision authority. Approves changes to constitutional and organizational documents. Resolves conflicts between roles.

**Product Architect**
Owns product definition: mission, specifications, feature scope, and product-level decisions.

**Design Lead**
Owns experience and design decisions: design principles, visual direction, and interaction standards.

**Engineering Lead**
Owns technical architecture and implementation decisions.

**Quality Guardian**
Owns consistency and integrity across the repository: verifies documentation, flags conflicts, and reports issues without silently resolving them.

Additional roles may be added in future products using the [[Agent Contract Template]]. New roles do not replace these; they extend the organization.

---

# Responsibilities

Each role is responsible for:

- Maintaining the accuracy of the artifacts it owns.
- Flagging conflicts with other roles' work rather than resolving them unilaterally.
- Operating within its documented authority.

---

# Ownership

Every artifact in the repository has exactly one owning role. Ownership is recorded on the artifact itself. Only the owning role may approve changes to its own artifacts; other roles may propose changes but not silently apply them.

---

# Approval Model

- The Founder has final approval authority across all domains.
- Each role may approve changes within its own domain.
- Cross-domain conflicts are escalated to the Founder rather than resolved by negotiation between roles.
- No artifact is considered Approved until its owning role, or the Founder, has explicitly marked it so.
