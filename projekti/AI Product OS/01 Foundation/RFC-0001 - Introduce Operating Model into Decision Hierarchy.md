# RFC-0001 — Introduce Operating Model into Decision Hierarchy

RFC Number: RFC-0001
Title: Introduce Operating Model into Decision Hierarchy
Status: Approved
Author: Founder
Date: 2026-07-15
Related Documents:
- [[AI Product OS Constitution]]
- [[Operating Model]]
- [[Workflow Overview]]
- [[Request for Change (RFC) Process]]

---

# Problem Statement

The AI Product OS Constitution's Decision Hierarchy does not list Operating Model at all, while it still lists Workflow Overview at position 3. Operating Model is the document that actually defines how the organization operates; Workflow Overview no longer does. The Constitution is therefore internally inconsistent with the current state of the repository.

---

# Background

The Architecture Consolidation Sprint (v1.0) refactored Workflow Overview from a document that described lifecycle stages into a workflow index, and confirmed Operating Model as the sole document describing organizational operation. That sprint's validation pass surfaced this Decision Hierarchy inconsistency and reported it as open governance debt rather than silently correcting a Foundation Document. This RFC is the formal proposal to resolve it.

---

# Proposed Change

In `AI Product OS Constitution.md`, Decision Hierarchy section:

- Insert Operating Model into the hierarchy, positioned immediately below Organization Charter, as the authoritative document for how the organization operates.
- Retain Workflow Overview in the hierarchy, repositioned below Operating Model, with its role clarified as a supporting navigation document rather than an operational authority.
- No other section of the Constitution is affected.

Resulting order:
1. AI Product OS Constitution
2. Organization Charter
3. Operating Model
4. Workflow Overview
5. Repository Standard
6. Individual product specifications

---

# Benefits

- Restores internal consistency between the Constitution and the current, intentional state of the repository.
- Makes explicit, at the constitutional level, that Operating Model is the operational authority — matching what Operating Model, Workflow Overview, and the RFC Process already state.
- Removes ambiguity for any future role reading the Decision Hierarchy about which document governs operational conflicts.

---

# Risks

- None identified to product-level artifacts; this change is scoped entirely to governance documentation.
- Minimal risk of the hierarchy needing further adjustment if additional Foundation Documents are introduced later — accepted as normal governance evolution, to be handled by future RFCs.

---

# Impact Assessment

- No product-level (NorthStar) documents are affected.
- No role definitions, ownership assignments, or approval authorities change.
- Only the ordering and membership of the Decision Hierarchy list changes.

---

# Affected Documents

- `01 Foundation/AI Product OS Constitution.md` (Decision Hierarchy section only).

---

# Approval

Approved by: Founder
Date: 2026-07-15
Decision: Accepted as proposed, per direct Founder instruction to assume approval and implement.

---

# Implementation Plan

Modify only the Decision Hierarchy section of `AI Product OS Constitution.md` to insert Operating Model and reposition Workflow Overview, as specified in Proposed Change. No other constitutional content is touched.

---

# Validation Plan

After implementation, confirm: the Decision Hierarchy lists Operating Model above Workflow Overview; no other Constitution content changed; Operating Model remains the sole document describing organizational operation; Workflow Overview does not duplicate that authority; all wikilinks resolve; no new governance conflicts are introduced.

---

# Closure

RFC-0001 is closed once the Implementation and Validation steps above are confirmed complete and recorded in the sprint report.
