# DP-00 Design Baseline and Asset Audit

Version: 1.0
Status: Draft
Category: Design
Owner: Founder
Related Documents:
- [[Design Phase Kickoff]]
- [[Design Bible]]
- [[NorthStar Design Context Pack]]
- [[NorthStar Design Context Pack v2]]
- [[NorthStar Brand DNA]]
- [[Design Foundation Specification]]
- [[Constitution Amendment 001]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]

---

## 1. Purpose

This document formalizes the completed DP-00 — Design Baseline and Asset Audit work package (per [[Design Phase Kickoff]] §16) and records the Founder-approved canonical design-folder ownership model.

This document does not:

- approve a visual direction;
- approve Direction A+;
- begin DP-01;
- create screens, wireframes, prototypes, or design-system content;
- change product scope.

---

## 2. Governing Authority

For DP-00 purposes, authority is established in this order:

1. Approved Founder decisions (including the folder-ownership ruling recorded in Section 9 of this document).
2. The Approved [[Design Phase Kickoff]] (Version 1.0, Status Approved).
3. Approved product documents — [[Decision Register]], [[MVP]], [[Features]], the three Approved product specifications, [[Product Bible]], [[User Journey Specification]], [[NorthStar Constitution]], [[NorthStar OS Specification]].
4. Draft design references — [[Design Bible]], [[NorthStar Brand DNA]], [[Design Foundation Specification]], both NorthStar Design Context Packs, the Claude Design edition context pack.
5. Historical or exploratory artifacts — the Brand Exploration HTML/PDF pair, `04 Design Deliverables/Reviews/` records, `04 Design Deliverables/Archive/Session Summary.md`, [[Constitution Amendment 001]], `01 Product/Decision Log.md`, the historical `01 Product/User Flow Specification.md`.

Explicitly:

- **Draft polish does not confer authority.** A well-produced Draft document (e.g. the Brand Exploration PDF) carries no more authority than a plain-text Draft note.
- **File location does not confer authority.** A file's presence in `02 Design/` or `04 Design Deliverables/` does not by itself make it Approved.
- **Visual similarity to an Approved concept does not confer authority.** The Brand Exploration artifacts visually reference "Concept A"/"Calm Intelligence" language without being an Approved rendering of anything.

---

## 3. Audit Scope and Method

DP-00 audited:

- `02 Design/` (all seven stub documents, [[Design Bible]], [[Design Phase Kickoff]]);
- `04 Design Deliverables/` (`Foundation/`, `Reviews/`, `Archive/` subfolders, including the HTML and PDF artifacts);
- `AI Context Packs/`;
- root-level NorthStar design-adjacent documents ([[NorthStar Design Context Pack]], [[NorthStar Design Context Pack v2]], [[NorthStar Brand DNA]], [[Design Foundation Specification]], [[Constitution Amendment 001]]);
- `01 Product/Decision Log.md` and `01 Product/User Flow Specification.md`, for historical design-relevant content.

Method used:

- **HTML bundle inspection:** `NorthStar Brand Exploration v0.1.html` was identified as a self-extracting Claude Design canvas bundle (`__bundler/manifest`, `__bundler/template` script tags), not literal static HTML. The gzip+base64 payloads were decoded read-only (outside the repository) to inspect actual visible copy and structure.
- **PDF visual inspection:** `NorthStar Brand Exploration v0.1.pdf` was rendered and read page-by-page (5 pages total), not inferred from filename or sibling files.
- **Exact stub inspection:** all seven `02 Design/` stub files were read in full, line by line.
- **Design-relevant wikilink audit:** `[[...]]` links were extracted from a defined 21-file design-relevant corpus and resolved against `projekti/NorthStar/` filenames.

Verified wikilink-audit figures:

- 21 design-relevant Markdown files checked;
- 140 raw wikilinks found;
- 17 unique targets;
- 0 unresolved targets;
- 0 ambiguous targets, within `projekti/NorthStar/`.

**Scope limitation:** the wikilink audit was scoped to the 21-file design-relevant corpus within `projekti/NorthStar/` only. The vault (`C:/Users/rober/Documents/ods-vault`) contains other unrelated projects (e.g. `AI Product OS`, `Kyron7`, `TestProj`, `celje-skarpa-hisa`, plus non-project folders) that were not searched for filename collisions. No vault-wide wikilink claim is made.

---

## 4. Design Artifact Inventory

| Path | Type | Version/Status | Authority Classification | Safe Use | Prohibited Authority Use | Landing Compatibility | Recommended Handling |
|---|---|---|---|---|---|---|---|
| `02 Design/Design Phase Kickoff.md` | md | 1.0 / Approved | **Approved authority** | Governs the entire design phase | N/A | Sole authoritative written record of the exact landing copy (§3.1) | No action |
| `02 Design/Design Bible.md` | md | 1.0 / Draft | Draft reference | Calmness, whitespace, typography, color-as-meaning, accessibility, component-consistency principles | AI-first/conversation-primary navigation framing | Partial (tone only) | Leave unchanged |
| `02 Design/Approved Screens.md` | md | none / Draft | Empty stub | Future index of Founder-approved screens | Nothing currently | N/A | Remains stub; populate at DP-08 |
| `02 Design/Wireframes.md` | md | none / Draft | Empty stub | Future wireframe index | Nothing currently | N/A | Remains stub |
| `02 Design/Design System.md` | md | none / Draft | Empty stub | Future design-token/component index | Nothing currently | N/A | Remains stub |
| `02 Design/UX Principles.md` | md | none / Draft | Empty stub | Future UX-rule index | Nothing currently | N/A | Remains stub |
| `02 Design/HTML Prototypes.md` | md | none / Draft | Empty stub | Future index pointing to `04 Design Deliverables` HTML artifacts | Nothing currently | N/A | Remains stub; becomes an index per Section 9 |
| `02 Design/Reviews.md` | md | none / Draft | Empty stub | Future index of design review notes | Nothing currently | N/A | Remains stub |
| `02 Design/Assets.md` | md | none / Draft | Empty stub | Future index of design assets | Nothing currently | N/A | Remains stub |
| `04 Design Deliverables/Foundation/NorthStar Brand Exploration v0.1.html` | html (Claude Design bundle) | none declared | Exploratory | Candidate color/type/motion reference, only once separately Founder-approved | Any current authority; landing-screen reference | No — contains none of the approved landing copy | Retain; index from `02 Design/HTML Prototypes.md` per Section 9 |
| `04 Design Deliverables/Foundation/NorthStar Brand Exploration v0.1.pdf` | pdf | none declared | Exploratory | Same as HTML — confirmed print-equivalent by direct visual inspection | Same | Same — confirmed via 5-page visual read: explicitly states "No screens, no components." | Retain; index from `02 Design/Assets.md` or `HTML Prototypes.md` |
| `04 Design Deliverables/Reviews/Design Decisions.md` | md | none / none | Historical | Cross-reference for the Brand Exploration sprint's design tokens | Product/design authority | No | Retain in place (historical, per Section 9 item 5) |
| `04 Design Deliverables/Reviews/Recommendation.md` | md | none / none | Historical | Rationale record for Direction 1a | Product/design authority | No | Retain in place |
| `04 Design Deliverables/Reviews/Self Critique.md` | md | none / none | Historical | Self-flagged risk record (incl. Design Tokens gap) | Product/design authority | No | Retain in place |
| `04 Design Deliverables/Archive/Session Summary.md` | md | none / none | Historical | Sprint sequence log | File-location claims (references filenames not present in the repo) | N/A | Retain; filename mismatch flagged in Section 12 |
| `NorthStar Design Context Pack.md` (v1) | md | 1.0 / Draft | **Superseded** (by its own successor's text) | Historical trace only | Anything current | No | Retain as historical record per its own "not deleted" note |
| `NorthStar Design Context Pack v2.md` | md | 2.0 / Draft | Draft reference; no superseding document identified in the audited corpus | Non-conflicting typography/color/layout/accessibility bullets | AI-primary navigation framing (§10) | No | Leave unchanged |
| `AI Context Packs/NorthStar Design Context Pack - Claude Design.md` | md | **none declared** | Draft reference (no frontmatter) | Same non-conflicting bullets as v2 (near-duplicate) | Same AI-primary navigation framing | No | Leave unchanged; missing-metadata flagged in Section 12 |
| `NorthStar Brand DNA.md` | md | 1.0 / Draft | Draft reference | Tone/personality/voice guidance | Product scope decisions | Partial (tone only) | Leave unchanged |
| `Design Foundation Specification.md` | md | 1.0 / Draft | Draft reference | Decision-priority checklist framing | Product scope | No | Leave unchanged |
| `Constitution Amendment 001.md` | md | 1.0 / Draft (unapproved) | Historical/exploratory proposal | Context on the (separately resolved) Trust-vs-Understanding ordering | Anything — explicitly "not approved, not rejected" | N/A | Leave unchanged |
| `01 Product/Decision Log.md` | md | none / Draft | Historical/legacy | Low-detail confirmation trail | Detailed product/design claims | Confirms Concept A generally, not exact copy | Leave unchanged |
| `01 Product/User Flow Specification.md` | md | 1.0 / Approved, self-flagged `Historical Status: Pre-DR-002 — Non-authoritative` | **Superseded** (by its own header) | Nothing for current scope | Everything current — explicitly disclaimed | No | Leave unchanged |

No Draft, unversioned, historical, or exploratory item above is classified as Approved.

---

## 5. Approved Landing Compatibility

**[[Design Phase Kickoff]] §3.1 is the sole authoritative source** for the exact Slovenian landing copy, the four-tile order, the release behavior, and the `Zakaj NorthStar?` benefits. This DP-00 document does not reproduce that foundation as a second canonical record — doing so would create a second source of truth and risk drifting out of sync with the authoritative original.

DP-00's audit findings, at the summary level only:

- No existing visual artifact — HTML, PDF, or otherwise — represents the Approved landing screen.
- The authoritative foundation includes exact copy (title, subtitle, entry label), four ordered tiles, defined release behavior per tile, and the `Zakaj NorthStar?` benefits.
- For the literal wording and exact structure, refer to [[Design Phase Kickoff]] §3.1 — not to this document.

This audit does not own or redefine the landing foundation. Any future change to it must be made through the governing Founder-decision workflow and reflected first in [[Design Phase Kickoff]] §3.1. The summary above must not be used as a substitute for that authoritative source.

---

## 6. Design Bible and Context-Pack Findings

- [[Design Bible]] is **Version 1.0, Status Draft.**
- [[NorthStar Design Context Pack]] (v1) is **Draft**, and is superseded by v2 per v2's own text ("Supersedes: [[NorthStar Design Context Pack]]").
- [[NorthStar Design Context Pack v2]] is **Draft**.
- The Claude Design edition (`AI Context Packs/NorthStar Design Context Pack - Claude Design.md`) has **no `Version:` or `Status:` metadata at all**.
- All of the above contain **AI-primary / navigation-secondary** framing ("AI is the primary guide. Navigation is secondary." / "AI is the interface... Primary guide; navigation is secondary.") that **conflicts** with the Approved four-tile, no-AI-chat first public MVP scope.
- Safe, non-conflicting principles that may still be used as inspiration: calmness, whitespace, typography hierarchy, color as meaning (not decoration), component consistency, and accessibility intent.
- AI-first navigation language from any of these four documents **must not govern Stage A**.

These documents are not declared retired by this document. Whether their AI-first framing is retired, revised, or scoped to a future release is recorded as an open governance action in Section 15, pending a separate Founder decision.

---

## 7. Brand Exploration Findings

- The HTML bundle (`NorthStar Brand Exploration v0.1.html`) was decoded and inspected this audit.
- The PDF (`NorthStar Brand Exploration v0.1.pdf`) was visually inspected across all 5 pages.
- The artifact's own page-1 subtitle explicitly states: **"No screens, no components."**
- It contains brand directions **1a (Calm Intelligence), 1b (Human Finance), 1c (Premium Guidance)**, a comparison/recommendation of 1a, and **Direction A+** (the evolved signature identity: Northlight, Certainty Arc, single-sharp-corner rule, and three smaller refinements).
- It contains **none** of the Approved landing copy or product tiles.
- It is **exploratory**, not an Approved landing reference of any kind.
- **Direction A+ remains `PROPOSED ONLY`** per [[Decision Register]] DR-008 and is not endorsed by this document.

---

## 8. Stub Status

All seven `02 Design/` stub files were re-verified:

- `Approved Screens.md`, `Wireframes.md`, `Design System.md`, `UX Principles.md`, `HTML Prototypes.md`, `Reviews.md`, `Assets.md`.
- Each contains exactly **5 lines**.
- Each has **no `Version:` line**.
- Each contains `Status: Draft` as **ordinary Markdown body text**, not YAML frontmatter (no `---` delimiters anywhere in any of the seven files).
- None contains substantive design content beyond a title and a one-sentence description.
- None currently provides authority of any kind.

---

## 9. Founder-Approved Canonical Folder Ownership

The Founder has explicitly approved the following canonical model:

### `02 Design/`

Authoritative for:

- Markdown design documentation;
- design governance;
- information architecture;
- UX rules;
- design indexes;
- Approved-screen records;
- design-system specifications.

### `04 Design Deliverables/`

Physical location for:

- generated/exported HTML;
- PDFs;
- images;
- screenshots;
- visual prototypes;
- historical sprint exports.

### Cross-reference rule

- Current visual deliverables relevant to governed work must be indexed or referenced from an appropriate authoritative document in `02 Design/`.
- Location inside `04 Design Deliverables/` does not create authority or Approved status.
- Historical Markdown records already located in `04 Design Deliverables/` (`Design Decisions.md`, `Recommendation.md`, `Self Critique.md`, `Session Summary.md`) remain in place for now and are treated as historical.
- This decision does not authorize moving or rewriting any historical file. No file was moved, renamed, or rewritten as part of recording this decision.

---

## 10. Safe-to-Use Reference List

- **[[Design Phase Kickoff]]** — full authority for the design phase.
- **[[Design Bible]]** — calmness, whitespace, typography-hierarchy, color-as-meaning, component-consistency, and accessibility sections only (excluding "AI-First Design").
- **[[NorthStar Brand DNA]]** — tone/personality/voice guidance only.
- **Brand Exploration HTML/PDF, `Design Decisions.md`, `Recommendation.md`, `Self Critique.md`** — as *candidate*, strictly non-binding color/type/motion direction, usable only once any Direction A+ element receives its own separate Founder approval (none currently approved).
- **[[Design Foundation Specification]]** — process/checklist framing, excluding any AI-navigation-model implication.
- **[[Decision Register]], [[MVP]], [[Features]], and the three Approved product specifications** — full authority for product scope.

---

## 11. Do-Not-Use-as-Authority List

- Design Bible's "AI-First Design" / "AI Interface Principles" sections, as a literal interface/navigation requirement.
- Both NorthStar Design Context Packs and the Claude Design edition file, for anything touching navigation model or product architecture.
- The historical `01 Product/User Flow Specification.md` — self-flagged non-authoritative (pre-DR-002 PDF/Ask-AI concept).
- The unapproved [[Constitution Amendment 001]] — decides nothing.
- The Brand Exploration HTML/PDF and their companion Markdown deliverables, as any form of landing-screen authority.
- Any of the seven `02 Design/` stubs — currently contain no substantive content to cite.

---

## 12. Governance Risk Register

| Risk | Severity | Evidence | Impact | Blocking (DP-01)? | Future Owner/Action |
|---|---|---|---|---|---|
| Draft artifacts (Design Bible, both Context Packs) mistaken for Approved authority | High | All carry `Status: Draft` or no status, yet contain confident prescriptive language | Could misdirect DP-02's navigation model | No — routed around by Kickoff §2/§18 | Founder ruling on AI-first framing (Section 15) |
| Duplicate/near-duplicate Context Packs | Medium | v1 superseded, v2 current, Claude Design edition a near-duplicate of v2 | Wastes review time; edit-one-miss-others risk | No | Founder decision to consolidate (Section 15) |
| Unversioned Claude Design context pack | Medium | No `Version:`/`Status:` line present | Cannot be cited with a precise authority claim | No | Add frontmatter (Section 15) |
| AI-first navigation conflict | High | 4 documents state AI is "primary guide, navigation secondary" | Direct tension with the approved static four-tile landing | No — Kickoff §2/§18 already governs | Founder/CTO ruling (Section 15) |
| Missing design-token authority | Medium | Self-flagged in `Self Critique.md`, `Session Summary.md`, Context Pack v2 §14 | Blocks Stage C, not Stage A/B | No | Founder decision once component work begins |
| Historical filename mismatch in Session Summary | Low-Medium | References `.dc.html` filenames not present in the repo; actual files are `NorthStar Brand Exploration v0.1.html`/`.pdf` | Minor historical-record inaccuracy | No | Correct or annotate (Section 15) |
| Approved landing copy recorded only in the Kickoff | Medium | Verified: zero other artifacts contain the literal strings | No independent backup of the exact copy | No | Consider indexing into `Approved Screens.md` at DP-08, not before |
| Future indexing requirement for `04 Design Deliverables` | Medium | `02 Design/HTML Prototypes.md`, `Assets.md`, `Reviews.md` are currently empty stubs, not yet indexing anything | Duplicate-source-of-truth risk persists until stubs are populated | No | Populate indexes at the appropriate later DP, per Section 9 |

No risk above is resolved beyond the Founder-approved folder model recorded in Section 9.

---

## 13. DP-01 Readiness

**Analytical readiness:** DP-01 read-only analytical work is ready to begin.

**Write readiness:** Markdown IA output may be written under `02 Design/`, consistent with the Founder-approved ownership model in Section 9. Exported or visual artifacts, if any are later produced, belong under `04 Design Deliverables/` and must be indexed from `02 Design/`.

This document does not start DP-01. No IA diagram, wireframe, screen, or design-system content was created as part of recording this audit.

---

## 14. DP-00 Completion Statement

- DP-00 evidence is complete.
- DP-00 received ChatGPT CTO approval (`DP-00 — Design Baseline and Asset Audit: CTO APPROVED`).
- The canonical folder-ownership model (Section 9) received explicit Founder approval.
- This document remains `Status: Draft` until the full NorthStar approval workflow ([[Design Phase Kickoff]] §17) is completed.

---

## 15. Open Follow-Up Actions

The following are listed, not executed:

- decide whether Design Bible's AI-first framing is retired, revised, or scoped to a future release;
- consolidate or formally relate the Context Packs (v1, v2, Claude Design edition);
- add `Version:`/`Status:` metadata to the Claude Design edition context pack;
- later index governed visual artifacts from `02 Design/` (per Section 9's cross-reference rule);
- decide whether the stale filenames in `Session Summary.md` should be corrected or annotated;
- evaluate Direction A+ only through a separate Founder decision;
- define design tokens before Stage C.

---

## 16. Related Documents

- [[Design Phase Kickoff]]
- [[Design Bible]]
- [[NorthStar Design Context Pack]]
- [[NorthStar Design Context Pack v2]]
- [[NorthStar Brand DNA]]
- [[Design Foundation Specification]]
- [[Constitution Amendment 001]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
