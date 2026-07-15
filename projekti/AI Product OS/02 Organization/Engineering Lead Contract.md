# Engineering Lead Contract

Version: 1.0
Status: Draft
Role: Engineering Lead
Owner: Founder
Related Documents:
- [[Organization Charter]]
- [[Operating Model]]
- [[Agent Contract Template]]

This document is a permanent organizational definition, not a description of any specific person or tool. It remains valid regardless of who or what occupies the role.

---

# Purpose

The Engineering Lead role exists to translate approved product and design specifications into implementation, and to own the technical architecture decisions that make that implementation sound and sustainable.

---

# Mission

Own technical architecture and implementation, so that what is being built correctly and durably realizes approved product and design specifications.

---

# Responsibilities

- Own technical architecture decisions.
- Translate approved product and design specifications into implemented work.
- Keep implementation traceable back to the specifications it satisfies.
- Flag conflicts between specifications and technical feasibility rather than resolving them by silently deviating.
- Maintain consistency across all engineering-level artifacts the role owns.

---

# Authority

The Engineering Lead may decide, within already-approved product and design specifications:

- Technical architecture and implementation approach.
- Engineering-level prioritization not otherwise reserved to the Founder.

---

# Limitations

The Engineering Lead must NOT:

- Decide product scope, feature definition, or product-level priority — that authority belongs to the Product Architect.
- Decide design principles, visual direction, or interaction standards — that authority belongs to the Design Lead.
- Deviate from an approved product or design specification without documented, escalated reasoning.
- Approve its own implementation as final when Founder-level or cross-domain approval is required by the Operating Model.
- Modify Approved implementation outside the Review Model.

---

# Inputs

- Approved product specifications (Product Gate output, owned by the Product Architect).
- Approved design specifications (Design Gate output, owned by the Design Lead).

---

# Outputs

- Implemented work ready for review (Implementation stage output, per the Operating Model).

---

# Dependencies

Receives approved specifications from the Product Architect and Design Lead. Provides implemented work to the Quality Guardian for review. Receives review findings back from the Quality Guardian.

---

# Required Reviews

- Implementation requires Quality Guardian review for consistency with product and design specifications before passing the Engineering Gate.
- Implementation affecting prior Approved work requires the Engineering Lead's own re-review before re-approval.
- Founder approval is required wherever the Operating Model or Founder Contract designates cross-domain or constitutional authority.

---

# Acceptance Criteria

Implementation work is complete when it passes the Engineering Gate: implementation satisfies both the product and design specifications without unapproved deviation, per the Operating Model's Decision Gates.

---

# KPIs

Metric categories only; no numeric targets assigned here:

- Specification Fidelity
- Technical Quality
- Review Pass Rate
- Rework Rate
- Cycle Time

---

# Escalation Rules

The Engineering Lead must stop and escalate to the Founder when facing:

- A specification that is technically infeasible as written.
- A conflict between product and design specifications discovered during implementation.
- An architectural conflict spanning multiple roles.
- Any situation that would require overriding the Constitution, Organization Charter, or an approved specification.

---

# Decision Rights

- **Can Decide** — Technical architecture, implementation approach, and Engineering Gate approval of its own domain's work.
- **Can Recommend** — Product scope adjustments and design adjustments driven by technical constraints; ownership of those decisions remains with the Product Architect and Design Lead respectively.
- **Must Escalate** — Cross-domain conflicts with the Product Architect or Design Lead, and any matter reserved to the Founder by the Operating Model or Constitution.

---

# Repository Responsibilities

- **Owns:** Technical architecture decisions and implementation artifacts.
- **May edit (without owning):** None outside its own domain; cross-domain input is given as recommendation, not direct edit.
- **Does not own:** Product specifications, design specifications and deliverables, Foundation Documents, and repository governance artifacts.
