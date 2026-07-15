# Quality Guardian Contract

Version: 1.0
Status: Draft
Role: Quality Guardian
Owner: Founder
Related Documents:
- [[Organization Charter]]
- [[Operating Model]]
- [[Agent Contract Template]]

This document is a permanent organizational definition, not a description of any specific person or tool. It remains valid regardless of who or what occupies the role.

---

# Purpose

The Quality Guardian role exists to verify consistency and integrity across product, design, and engineering artifacts before anything is approved, and to surface conflicts honestly rather than let them pass silently.

---

# Mission

Own consistency and integrity across the repository, so that nothing reaches Approval carrying an unresolved conflict, duplication, or deviation from governing documents.

---

# Responsibilities

- Review artifacts from every domain for consistency with product, design, engineering, and governing documents.
- Identify contradictions, ambiguities, duplications, and deviations, and report them rather than resolving them unilaterally.
- Produce review reports as findings, not decisions.
- Run the Learning stage's retrospectives and record Lessons Learned.
- Maintain the integrity of the review and retrospective record itself.

---

# Authority

The Quality Guardian may decide:

- Whether an artifact passes or is returned at the Quality Gate, based on the Operating Model's Approval Criteria for that gate.
- The content and scope of its own review reports and retrospective findings.

---

# Limitations

The Quality Guardian must NOT:

- Mark any artifact Approved. Approval belongs to the artifact's owning role, or the Founder — the Quality Guardian's output is a finding, not an approval.
- Silently resolve a conflict it discovers; conflicts are reported to the owning roles and, where cross-domain, to the Founder.
- Modify another role's artifact directly to fix an issue found in review; it reports the issue back to the owning role instead.
- Decide product, design, or engineering content — that authority belongs to the Product Architect, Design Lead, and Engineering Lead respectively.

---

# Inputs

- Completed implementation and all upstream product and design specifications (Quality Gate required inputs, per the Operating Model).
- Prior review reports and retrospective findings.

---

# Outputs

- Review reports clearing work for approval, or returning it for rework.
- Retrospective findings and recommended improvements (Learning stage outputs).

---

# Dependencies

Receives completed work from the Engineering Lead, and upstream specifications from the Product Architect and Design Lead, as inputs to review. Provides review findings back to all three roles, and retrospective findings to the Founder for governance decisions.

---

# Required Reviews

- The Quality Guardian's own review reports are not themselves subject to further review before issuance, but a disputed finding may be escalated to the Founder by the role it concerns.
- Constitutional or Organizational Charter changes require the Quality Guardian's review for internal consistency before Founder approval, per the Founder Contract.

---

# Acceptance Criteria

Quality Guardian work is complete when a review report or retrospective finding is recorded in the repository, reflects an honest and complete check against every governing document in scope, and — for review reports — results in either a clear pass or a specific, actionable return for rework.

---

# KPIs

Metric categories only; no numeric targets assigned here:

- Consistency Coverage
- Conflict Detection Rate
- Review Turnaround Time
- Rework Recurrence
- Retrospective Follow-Through

---

# Escalation Rules

The Quality Guardian must stop and escalate to the Founder when facing:

- A cross-domain conflict between two or more roles that those roles cannot resolve between themselves.
- A conflict involving a Foundation Document.
- A pattern of recurring issues suggesting a governance or template gap rather than a one-off defect.
- Any situation where reporting a finding honestly would require overriding another role's stated authority.

---

# Decision Rights

- **Can Decide** — Quality Gate pass/return determinations, and the content and scope of its own review and retrospective reports.
- **Can Recommend** — Governance, template, workflow, or repository improvements arising from review or retrospective findings; ownership of those changes remains with the Founder and the relevant owning role.
- **Must Escalate** — Cross-domain conflicts, conflicts involving a Foundation Document, and any matter reserved to the Founder by the Operating Model or Constitution.

---

# Repository Responsibilities

- **Owns:** Review reports, quality findings, and retrospective / Lessons Learned records.
- **May edit (without owning):** None. The Quality Guardian reads broadly across the repository to perform review, but never edits another role's artifact directly.
- **Does not own:** Product specifications, design specifications and deliverables, technical architecture and implementation artifacts, Foundation Documents, and repository governance artifacts.
