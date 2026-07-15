# Operating Model

Version: 1.0
Status: Draft
Owner: Founder
Related Documents:
- [[AI Product OS Constitution]]
- [[Organization Charter]]
- [[Workflow Overview]]
- [[Repository Standard]]

---

# Purpose

The Operating Model exists to describe how work actually flows through the organization — from an initial idea to a released, learned-from outcome. Where the Constitution defines why the organization exists and the Organization Charter defines who holds which role, this document defines how those roles interact in sequence. It is independent of any specific technology and remains valid even as tools change, because it describes behavior, not implementation.

---

# Guiding Principle

Work moves through clearly defined stages, never skipped and never informally shortcut. Every artifact has exactly one owner at every point in its life. Reviews exist to improve work before it is approved, not to gatekeep for its own sake. The repository is the source of truth — a decision that is not recorded in it did not happen, organizationally speaking.

---

# Organizational Lifecycle

## Idea

**Purpose:** Capture a new possibility before it becomes a commitment.
**Primary Owner Role:** Founder.
**Primary Outputs:** A recorded idea, with enough context to be evaluated.
**Exit Criteria:** The idea is judged worth formal strategic validation, or explicitly set aside.

## Strategic Validation

**Purpose:** Confirm the idea aligns with vision, strategy, and current priorities before resources are committed.
**Primary Owner Role:** Founder.
**Primary Outputs:** A validated strategic direction, or a documented reason for rejection.
**Exit Criteria:** The Strategy Gate is passed.

## Product Definition

**Purpose:** Translate a validated direction into concrete product scope.
**Primary Owner Role:** Product Architect.
**Primary Outputs:** Product specifications and defined scope.
**Exit Criteria:** The Product Gate is passed.

## Design

**Purpose:** Translate product specifications into experience and design principles.
**Primary Owner Role:** Design Lead.
**Primary Outputs:** Design specifications and design deliverables.
**Exit Criteria:** The Design Gate is passed.

## Implementation

**Purpose:** Build the product according to approved product and design specifications.
**Primary Owner Role:** Engineering Lead.
**Primary Outputs:** Implemented work ready for review.
**Exit Criteria:** The Engineering Gate is passed.

## Review

**Purpose:** Verify consistency, quality, and adherence to every governing document before anything is approved.
**Primary Owner Role:** Quality Guardian.
**Primary Outputs:** A review report — findings, not decisions.
**Exit Criteria:** The Quality Gate is passed, or findings are returned to the owning role for rework.

## Approval

**Purpose:** Formally accept work as correct and ready to enter the repository as current.
**Primary Owner Role:** The artifact's owning role, or the Founder where cross-domain authority is required.
**Primary Outputs:** An Approved artifact.
**Exit Criteria:** Approval is recorded against the artifact.

## Repository

**Purpose:** Record the approved work as the current source of truth.
**Primary Owner Role:** Founder, as steward of the Repository Standard; individual artifacts retain their own owners within it.
**Primary Outputs:** An updated, traceable repository state.
**Exit Criteria:** The artifact is correctly filed, owned, and versioned per the Repository Standard.

## Release

**Purpose:** Make approved work the active version used going forward.
**Primary Owner Role:** Founder.
**Primary Outputs:** A released, current product state.
**Exit Criteria:** The Release Gate is passed.

## Learning

**Purpose:** Convert what happened into improvements to the organization itself.
**Primary Owner Role:** Quality Guardian, feeding into Founder-owned governance decisions.
**Primary Outputs:** Retrospective findings and recommended improvements.
**Exit Criteria:** Findings are recorded and, where accepted, applied to templates, workflow, repository practice, or governance.

---

# Decision Gates

## Strategy Gate

**Purpose:** Confirm strategic alignment before product work begins.
**Owner:** Founder.
**Required Inputs:** A recorded idea and its strategic context.
**Approval Criteria:** Alignment with vision, mission, and current priorities.
**Outputs:** A validated strategic direction.

## Product Gate

**Purpose:** Confirm product scope is well-defined and ready for design.
**Owner:** Product Architect.
**Required Inputs:** Validated strategic direction.
**Approval Criteria:** Specifications are complete, unambiguous, and consistent with governing documents.
**Outputs:** Approved product specifications.

## Design Gate

**Purpose:** Confirm design direction is ready for implementation.
**Owner:** Design Lead.
**Required Inputs:** Approved product specifications.
**Approval Criteria:** Design work satisfies product requirements and design principles.
**Outputs:** Approved design specifications.

## Engineering Gate

**Purpose:** Confirm implementation is complete and matches approved specifications.
**Owner:** Engineering Lead.
**Required Inputs:** Approved design and product specifications.
**Approval Criteria:** Implementation satisfies both specifications without unapproved deviation.
**Outputs:** Implementation ready for review.

## Quality Gate

**Purpose:** Confirm consistency and integrity across product, design, and engineering artifacts.
**Owner:** Quality Guardian.
**Required Inputs:** Completed implementation and all upstream specifications.
**Approval Criteria:** No unresolved conflicts, duplications, or deviations from governing documents.
**Outputs:** A review report clearing the work for approval, or returning it for rework.

## Release Gate

**Purpose:** Confirm approved work is ready to become the active version.
**Owner:** Founder.
**Required Inputs:** An Approved artifact that has passed the Quality Gate.
**Approval Criteria:** All upstream gates are passed and recorded.
**Outputs:** A released product state.

---

# Artifact Flow

Every artifact moves through the same sequence regardless of type:

- **Creation** — an owning role produces a draft artifact.
- **Ownership** — the artifact is assigned exactly one owner at all times; this never changes silently.
- **Review** — the Quality Guardian, or another role where the Organization Charter specifies, checks the artifact against governing documents.
- **Approval** — the owning role, or the Founder where required, marks the artifact Approved.
- **Repository** — the artifact is recorded as current, per the Repository Standard.
- **Versioning** — changes to an Approved artifact create a new version; history is never overwritten.
- **Archive** — superseded versions move to Archive; nothing is deleted.

No artifact skips a stage in this sequence. No artifact ever has more than one owner at a time.

---

# Repository Model

The repository is the source of truth: if a decision, specification, or approval is not recorded there, it does not organizationally exist. Every artifact carries version and status metadata, so its current state is always known without needing external memory.

The repository holds several categories of material, each following the same ownership and review rules: documentation, design deliverables, specifications, and review records. All of it is historically traceable — prior versions remain available in Archive rather than being discarded, so any past decision can be reconstructed from the repository alone.

---

# Review Model

Reviews exist to improve work before it is approved, not to slow work down for its own sake. The Quality Guardian performs cross-domain consistency review; owning roles perform review within their own domain as part of reaching their own Gate.

No artifact bypasses review on its way to Approval — this holds regardless of urgency or seniority of the role proposing it. Review and approval are distinct: review produces findings, which may include a recommendation, but only the owning role or the Founder can convert a reviewed artifact into an Approved one.

---

# Decision Model

- **Decides:** the role with documented Authority over that domain, per its Agent Contract.
- **Recommends:** any role may recommend outside its own Authority; a recommendation is not a decision.
- **Approves:** the artifact's owning role, or the Founder where cross-domain or constitutional authority is required.
- **Escalates:** any role facing a condition listed in its own Escalation Rules must stop and raise it rather than deciding alone.
- **Records:** every decision is recorded in the repository at the point it is made — an undocumented decision has no standing.

---

# Learning Loop

Every completed project is expected to improve the AI Product OS itself, not just produce its own output.

- **Retrospectives** — held at the close of Learning, reviewing what happened against what was planned.
- **Lessons Learned** — recorded findings, kept even when no immediate change follows from them.
- **Template Improvements** — proposed changes to templates such as the Agent Contract Template.
- **Workflow Improvements** — proposed changes to the Organizational Lifecycle or Decision Gates.
- **Repository Improvements** — proposed changes to the Repository Standard.
- **Governance Improvements** — proposed changes to the Constitution or Organization Charter, subject to the amendment process.

Findings from the Learning stage do not self-apply — they are proposals, reviewed and approved through the same Decision Model as any other change.

---

# Operating Principles

- Small approved iterations over large unreviewed ones.
- One owner per artifact, always.
- Repository over memory.
- Transparency over automation.
- Automation supports governance; it never replaces it.
- Reviews strengthen quality; they are not a formality to route around.
- Roles outlive tools.

---

# Definition of Success

The organization is operating successfully when every artifact can be traced to a single owner, every decision can be reconstructed from the repository alone, no work reaches release without passing its Gates, and each completed project leaves the AI Product OS measurably better defined than it found it.
