# Design Phase Kickoff

Version: 1.0
Status: Draft
Category: Design
Owner: Founder
Related Documents:
- [[NorthStar Constitution]]
- [[NorthStar OS Specification]]
- [[Product Bible]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
- [[User Journey Specification]]
- [[Housing Loans Specification]]
- [[Affordability Specification]]
- [[Pojasni pojme Specification]]
- [[Design Bible]]

---

## 1. Purpose

This document defines the controlled transition from NorthStar's Approved product architecture into the design phase. It does not itself perform design work, and it does not approve any screen — it sequences and gates the work that follows.

- Design operationalizes already-Approved product decisions ([[Decision Register]], [[MVP]], [[Features]], and the three Approved product specifications). It does not silently redefine product scope.
- Where a product or methodology decision has not yet been made (see the Affordability and Pojasni pojme "Open Decisions" tables in their respective specifications), this document leaves it visibly unresolved. It does not guess, and it does not invent a threshold, formula, category list, or content set to make a screen look more finished than the product actually is.
- First-pass design (Stage A) may use clearly labeled placeholder or demonstrative values so that screen hierarchy, navigation, and interaction models can be established before every content and methodology question is answered (see [Section 15](#15-design-stage-definitions) for the full Stage A / Stage B / Stage C definitions).
- Design approval and implementation approval are separate gates. A design being visually complete, or even Founder-approved as a design artifact, does not by itself authorize implementation — [[MVP]] §9 ("MVP Definition of Done") and the per-product "Open Decisions" tables still govern whether a feature may be built.

---

## 2. Design Authority and Source Hierarchy

Per [[Decision Register]] DR-010, and applied here specifically for design decisions:

1. The latest direct Founder decision (including instructions delivered directly by the Founder in a working session, such as the approved landing foundation restated in [Section 3](#3-approved-design-foundation)).
2. The Approved [[Decision Register]] (DR-001 through DR-017).
3. The three Approved product specifications: [[Housing Loans Specification]], [[Affordability Specification]], [[Pojasni pojme Specification]].
4. Approved [[MVP]], [[Features]], [[Product Bible]], and [[User Journey Specification]].
5. Approved design decisions (none yet formally logged as Approved in `02 Design/` — see [Section "Existing Design-Material Audit"] in the accompanying report).
6. [[Design Bible]] — according to its actual current status, which is **Draft**, not Approved (see [Section 21](#21-document-boundaries) and the audit findings). Draft design material is a candidate philosophy statement, not settled authority.
7. Historical or exploratory artifacts (e.g. `04 Design Deliverables/`, the NorthStar Design Context Pack series, [[Constitution Amendment 001]]) — useful as context, never as a source of product or design authority.

Draft design material cannot override Approved product decisions. Where a Draft design document (including [[Design Bible]]) states something in tension with an Approved product decision, the Approved product decision governs, and the tension is recorded as an open item rather than silently resolved in either direction (see [Section 18](#18-open-design-decisions-and-external-dependencies)).

---

## 3. Approved Design Foundation

The following was communicated directly by the Founder as the current landing foundation ("Concept A, refined to v2") and is treated, per [Section 2](#2-design-authority-and-source-hierarchy) item 1, as the highest-authority design source currently available. It is structurally consistent with [[Decision Register]] DR-001, DR-006, and DR-014 (four entry tiles, Concept A as visual basis, Leasing inactive and labeled `Kmalu`). The literal Slovenian copy strings below (title, subtitle, entry label, benefit labels) do not yet appear verbatim in any existing vault artifact — `02 Design/Approved Screens.md` is currently an empty stub — so this section is this kickoff's first written record of that exact copy, not a re-statement of a pre-existing saved document.

### 3.1 Fixed approved elements

- **Title:** "Razumite finančne odločitve."
- **Subtitle:** "Brez zapletenega jezika. Brez pritiska. Samo jasne razlage."
- **Entry label:** "Kje želite začeti?"
- **Four entry tiles**, in this order:
  1. Stanovanjski kredit
  2. Leasing
  3. Koliko kredita si lahko privoščim
  4. Pojasni pojme
- **Release behavior per tile:**
  - Koliko kredita si lahko privoščim — active.
  - Pojasni pojme — active.
  - Stanovanjski kredit — active, limited in scope (per DR-015).
  - Leasing — visible, disabled, labeled `Kmalu`.
- **"Zakaj NorthStar?" section**, with three benefits: Neodvisno / Jasno / Zasebno.

### 3.2 Safe scope constraints (binding)

These constraints are binding on all design work, regardless of which visual direction is later chosen:

- Leasing must remain visibly present on the landing screen and must honestly communicate `Kmalu` — it must never appear removed, broken, or non-functional by accident.
- The four approved products and their approved order (Section 3.1) must remain intact in any design produced under this kickoff.
- The "Zakaj NorthStar?" section must support, not replace or obscure, the primary entry points (title, subtitle, entry label, and the four tiles).

### 3.3 Non-binding design hypotheses

The following are candidate visual-design ideas only. They are **not** Approved design decisions, they do **not** override Section 3.1 or Section 3.2, and none of them may be treated as a binding rule until explored during DP-02 and reviewed by ChatGPT and the Founder:

- Whether the four tiles should be visually equivalent in size and prominence, or some other treatment, is a candidate direction, not a requirement.
- Whether "Zakaj NorthStar?" sits in an exact secondary position beneath the tiles, or is placed elsewhere, is a candidate direction, not a requirement.
- Whether Neodvisno / Jasno / Zasebno are presented as three short equally weighted statements, a feature-grid, or another treatment is not decided or prohibited here — any of these may be proposed and evaluated during DP-02.

### 3.4 Unresolved visual detail

The following are explicitly not decided by this section and remain open (see [Section 18](#18-open-design-decisions-and-external-dependencies)):

- exact tile layout and responsive presentation mechanism across breakpoints (Section 3.2's tile-order constraint still applies — see [Section 9](#9-responsive-design-scope));
- exact typography, color, and spacing values (no Design Tokens system exists in any source document — flagged, not invented, per the NorthStar Design Context Pack v2 §14);
- whether "Direction A+" elements (Northlight color, Certainty Arc, sharp-corner rule, decimal-underline treatment, linear loading indicator, underline confirmation) apply to the landing screen — these remain `PROPOSED ONLY` per DR-008 and must not be used without a separate Founder decision;
- exact interaction behavior of the Leasing `Kmalu` tile (tap/click behavior, any tooltip or explanatory microcopy) — this is not decided anywhere in this document.

Do not redesign or overturn the fixed foundation in Section 3.1 or the binding constraints in Section 3.2 without a new Founder decision.

---

## 4. Current Release Design Scope

| Product | Public-MVP role | First-pass design scope | Final-content-ready dependencies | Explicitly excluded design work |
|---|---|---|---|---|
| **Landing** | Global entry point; four standalone products (DR-001, DR-013) | Default landing state; Leasing `Kmalu` state; navigation to each product | Final typography/color/token decisions; final tile interaction spec | Any redesign of the approved foundation (Section 3) without Founder approval |
| **Affordability** (Koliko kredita si lahko privoščim) | Core MVP product (DR-014, DR-016) | Input, incomplete-input, validation-error, result, assumptions-disclosure, and both mandatory visualization states, using placeholder values | Real methodology, thresholds, living-cost values, affordability-ratio and stress-test content ([[Affordability Specification]] §16) | Any screen implying a finished formula or bank-grade precision |
| **Pojasni pojme** | Core MVP product (DR-014, DR-017) | Search/browse, category-browsing, term-detail, no-result, unavailable-related-term, and trust/source-area states, using a small demonstrative term subset | Real term list, categories, sources, validation dates, editorial status ([[Pojasni pojme Specification]] §19) | AI chat; live generative explanations; automatic publication UI |
| **Housing Loans** (Stanovanjski kredit) | Limited first version (DR-015) | Learn overview; Monthly Payment Examples; links to Affordability and Pojasni pojme | Final example content and copy | PDF upload/analysis, Ask AI, offer comparison, advanced simulations, approval prediction — none of these may be designed |
| **Leasing** | Standalone first-phase product, not in first public MVP release (DR-013, DR-014) | Landing tile disabled/`Kmalu` state only | Not applicable — no Leasing specification exists yet | A full Leasing product flow of any kind |

---

## 5. Primary User Journeys

Per [[User Journey Specification]] and the confirmed cross-product links (DR-015, [[Housing Loans Specification]] §4.3), the first-pass design covers only:

- Landing → Affordability
- Landing → Pojasni pojme
- Landing → Housing Loans
- Landing → Leasing disabled/`Kmalu` interaction state — no Leasing product journey or internal Leasing screens are in scope; the exact click/tap behavior, and any tooltip or explanatory microcopy, remain unresolved (see [Section 3.4](#34-unresolved-visual-detail) and [Section 18.A](#18a-open-design-decisions-design-owned))
- Housing Loans → Affordability
- Housing Loans → Pojasni pojme
- Pojasni pojme → Related term

Not included, per confirmed exclusions (DR-002, DR-015, DR-016, DR-017): Ask AI, PDF/document analysis, bank-offer comparison, approval prediction, or a complete Leasing journey.

---

## 6. Information Architecture

First-pass hierarchy, following [[Design Bible]]'s "Information Priority" question set (what am I looking at / why does it matter / what can I do next) where that principle does not conflict with Approved product scope:

- **Global landing:** Title/subtitle → entry label → four product tiles (in the approved order, Section 3.1) → "Zakaj NorthStar?" (supporting layer, Section 3.2).
- **Affordability:** Entry/orientation → inputs (income, household size, living costs, obligations, term, rate) → result (range + interpretation) → mandatory visualizations → assumptions/methodology disclosure.
- **Pojasni pojme:** Entry/orientation → search + categories → term detail (four-part structure) → related terms → source/validation trust area.
- **Housing Loans:** Entry/orientation → Learn content → Monthly Payment Examples → links out to Affordability and Pojasni pojme.
- **Leasing:** Tile only, no internal hierarchy — disabled entry point with `Kmalu` label; no internal Leasing screens.

This section does not decide final detailed copy or visual style beyond what is already Approved in Section 3.

---

## 7. Required First-Pass Screens

### Landing
- Default landing state.
- Leasing `Kmalu` behavior (disabled tile treatment; exact interaction behavior unresolved, Section 3.4).

### Affordability
- Input state.
- Incomplete-input state.
- Validation-error state.
- Result state.
- Assumptions/methodology disclosure.
- Safe-range visualization (placeholder values).
- Monthly-allocation visualization (placeholder values).

### Pojasni pojme
- Search and browse state.
- Category-browsing behavior.
- Term-detail state.
- No-result state.
- Unavailable/unpublished related-term behavior.
- Source and validation trust area, with placeholders where visibility is unresolved.

### Housing Loans
- Learning overview.
- Monthly-payment examples.
- Link to Affordability.
- Link to Pojasni pojme.

No screen beyond this list is in scope for the first-pass design stage. No internal Leasing screen is in scope (Section 4, Section 5).

---

## 8. Interaction and State Inventory

| State | First-pass design | Final content-ready | Implementation only |
|---|---|---|---|
| Default | Required | — | — |
| Loading | Required (generic pattern) | — | Final timing/animation behavior |
| Empty | Required | — | — |
| Incomplete (input) | Required | — | Exact validation trigger rules |
| Validation error | Required (generic pattern) | Final message wording | Exact validation rules |
| No search result | Required | Final empty-state copy | Search-matching logic |
| Unavailable content | Required (placeholder pattern) | Real unpublished/withdrawn-term copy | — |
| Stale/revalidation placeholder | Required (placeholder pattern) | Real revalidation policy (open, [[Pojasni pojme Specification]] §19 item 7 — see [Section 18.B](#18b-external-unresolved-productcontentgovernance-dependencies)) | Revalidation automation |
| Disabled / `Kmalu` | Required (Leasing tile; exact tap/click behavior unresolved, Section 3.4) | — | — |
| Source or validation info | Required (placeholder pattern) | Public visibility decision (Section 18.B) | — |
| Mobile navigation | Required (intent only) | Final breakpoint spec | Final component behavior |
| Keyboard focus | Required (intent only) | Final focus-order spec | Final implementation |

This inventory does not invent backend behavior; it only classifies which states a first-pass screen set must visually represent.

---

## 9. Responsive Design Scope

Covered at intent level only for Stage A:

- Mobile-first considerations for the landing tiles, search, and category navigation.
- Desktop layout intent for a four-tile landing and for result/visualization screens.
- Tablet behavior as an intermediate case between the two, not a separately designed target.
- Touch targets sized for comfortable tapping on the four landing tiles and search/category controls.
- Content density: Slovenian strings run longer than English equivalents (e.g. "Obstoječi krediti, leasingi in druge redne mesečne obveznosti") — layouts must tolerate this without truncation as a first-pass principle.
- Charts (safe-range, monthly-allocation) must remain legible on narrow screens without inventing a final chart type (open per [[Affordability Specification]] §16 item 12 / §7.3).
- Tile stacking behavior on narrow viewports must preserve the Founder-approved product order (Section 3.1): **Stanovanjski kredit, Leasing, Koliko kredita si lahko privoščim, Pojasni pojme.** Stacking, scrolling, wrapping, or pagination mechanics are open for design to decide (Section 18.A); reordering the four tiles is not open, and requires a new Founder decision.
- Search and category navigation behavior on mobile.
- Term-detail readability on mobile, given four required content parts per term.

Exact breakpoints, and the exact responsive presentation mechanism (subject to the order constraint above), are explicitly not defined here and remain an open design decision (Section 18.A).

---

## 10. Accessibility Scope

At product-design level:

- Color must not be the only information carrier (Design Bible "Accessibility," Affordability Spec §7.3).
- Readable typography and sufficient contrast.
- Keyboard-navigation intent for all interactive elements.
- Visible focus states.
- Clear, plain-language labels.
- Understandable validation messages (no fabricated results, per Affordability Spec §14).
- Chart information must also be available in non-visual (text) form.
- Touch-target sizing considerations.
- Plain-language content throughout, consistent with Design Bible's Accessibility & Inclusive Design section.

This is a set of general principles for Stage A, not a final accessibility specification or implementation acceptance criteria — those require a dedicated accessibility pass (DP-07, Section 16) and Founder-approved requirements (open per both product specifications' "Open Decisions" tables, and see Section 18.B). No WCAG or other legal compliance level is claimed here or implied elsewhere in this document.

---

## 11. Content and Trust Design

First-pass design must visibly support:

- Educational-not-advice framing on every product (Constitution, Product Bible §13, all three product specifications' Trust and Product Boundaries sections).
- Visible assumptions wherever an estimate or example is shown.
- Visible uncertainty — ranges, not falsely precise single figures (DR-016).
- A place for sources, shown with placeholders where public visibility is unresolved (Section 18.B).
- A place for last-validation date, shown with placeholders where public visibility is unresolved (Section 18.B).
- Country-specific context (Slovenia-only scope) made legible to the user.
- No automatic AI authority — no AI chat, no live generative explanation surfaces anywhere in this release's first-pass screens.
- No persuasive or sales-style framing anywhere, consistent with Product Bible §6 ("Trust before Profit").
- Privacy and no-account expectations reflected in the design (no login/account UI to design).
- An honest `Kmalu` state for Leasing that reads as "coming later," not as a broken control.

Public source-link visibility and public last-validation-date visibility are not decided here (Section 18.B).

---

## 12. Affordability Design Dependencies

| Category | Item |
|---|---|
| **Resolved product requirements** | Confirmed inputs (income, household size, obligations, term, rate); range-based result; qualitative interpretation (bolj varno / napeto / previsoko tveganje); mandatory dual visualization; affordability ratio and stress-test reference as required educational outputs (DR-016, [[Affordability Specification]] §§4, 6–9) |
| **Unresolved methodology** | Exact calculation formula; concrete safety thresholds; Slovenia living-cost values and methodology; household-size equivalence methodology; affordability-ratio numerator/denominator/bands; stress-test source and representation ([[Affordability Specification]] §16 items 1–6) |
| **First-pass placeholders** | Demonstrative income/obligation/result figures clearly labeled as illustrative; placeholder safe-range boundaries for wireframe purposes only |
| **Final-content-ready blockers** | Items 1–6 and 11–12 of [[Affordability Specification]] §16 (methodology, thresholds, living costs, ratio, stress test, content validation, accessibility spec) |
| **Implementation blockers** | All items in [[Affordability Specification]] §16, including frequency conversion, rounding, missing-value handling, and validation/test data (items 7–10, 13) |

This table does not re-decide any formula, threshold, or content item owned by [[Affordability Specification]] §16 — it only maps those same open items onto design-stage readiness.

---

## 13. Pojasni pojme Design Dependencies

| Category | Item |
|---|---|
| **Resolved product requirements** | Confirmed discovery model (search, categories, term detail, related terms); four-part term structure; required metadata fields; human editorial publishing gate; AI limited to research/drafting only ([[Pojasni pojme Specification]] §§5–11) |
| **Unresolved methodology** | Exact initial term list; prioritization criteria; category taxonomy; source hierarchy governance; editorial roles; publication-status names/transitions; revalidation cadence ([[Pojasni pojme Specification]] §19 items 1–7) |
| **First-pass placeholders** | Small demonstrative term subset; placeholder categories; placeholder source records; placeholder validation dates; placeholder editorial status labels |
| **Final-content-ready blockers** | Items 1–5, 7, 10–12, 17 of [[Pojasni pojme Specification]] §19 (term list, prioritization, taxonomy, sourcing, editorial roles, revalidation, institution-specific variation, public source/date visibility, accessibility spec) |
| **Implementation blockers** | All items in [[Pojasni pojme Specification]] §19, including alias model, related-term ranking, technical country-pack format, and search/spelling tolerance (items 6, 8–9, 13–19) |

Institution-specific variation, public source visibility, and public validation-date visibility are called out explicitly because they materially change what the term-detail and trust-area screens must show; they are not decided here (Section 18.B).

---

## 14. Housing Loans Design Dependencies

Current design is limited to:

- educational overview (Learn content);
- monthly-payment examples;
- links to Affordability;
- links to Pojasni pojme.

Excluded from any current design work: PDF uploads, live analysis, AI chat, bank-offer comparison, advanced simulations (DR-015, [[Housing Loans Specification]] §5).

---

## 15. Design Stage Definitions

These three stages are used consistently throughout this document, and every section above and below should be read against these exact meanings.

### Stage A — First-pass design

**Purpose:** establish hierarchy, journeys, minimum screens, interaction concepts, responsive intent, trust placement, and major states.

**Allowed:**
- clearly labeled placeholder and demonstrative data;
- unresolved methodology or content represented visibly as open, never invented or guessed.

**Does not mean:**
- final content;
- final methodology;
- implementation-ready design;
- implementation authorization.

### Stage B — Final content-ready design

**Purpose:** replace relevant placeholders with Founder-approved or formally validated content and methodology-dependent presentation.

**Requires:**
- the necessary Affordability methodology decisions (Section 12; [[Affordability Specification]] §16);
- the necessary Pojasni pojme content, editorial, source, category, and visibility decisions (Section 13; [[Pojasni pojme Specification]] §19);
- final user-facing wording required by the screens.

**Does not mean:**
- a technical implementation specification;
- implementation authorization.

### Stage C — Implementation-ready design

**Purpose:** provide sufficiently exact interaction, responsive, component, state, accessibility, content, and handoff detail for a separate implementation-specification phase.

**Requires:**
- resolved design decisions (Section 18.A);
- final screen/state behavior;
- design-system or token decisions required for consistent implementation;
- formal design approval (Section 17).

**Does not mean:**
- that code has been authorized or that implementation has begun.

Moving from Stage C into implementation requires a separate, controlled technical planning and approval process. This document does not perform, authorize, or substitute for that process.

---

## 16. Design Work Packages

| ID | Objective | Inputs | Outputs | Blockers | Review gate | Explicit exclusions |
|---|---|---|---|---|---|---|
| **DP-00** — Design Baseline and Asset Audit | Establish a single, verified inventory of existing design material and its status | This document; vault search audit | Confirmed audit record (no duplicate source of truth) | None | Claude self-critique | Creating new screens |
| **DP-01** — Information Architecture | Define first-pass hierarchy for all in-scope products | Section 6; approved product specs | IA diagrams/outlines per product | None | Claude self-critique + ChatGPT review | Final navigation component design |
| **DP-02** — Landing and Global Navigation | Produce first-pass landing screens matching Section 3.1–3.2 exactly, and explore the non-binding hypotheses in Section 3.3 as candidate directions | Section 3, 7 | Default landing wireframe; Leasing `Kmalu` wireframe | Unresolved visual detail (Section 3.4) does not block Stage A | Claude self-critique + ChatGPT review + Founder review | Redesigning the fixed foundation (Section 3.1) or the binding constraints (Section 3.2) |
| **DP-03** — Affordability First-Pass UX | Produce required Affordability screens with placeholders | Section 7, 12; [[Affordability Specification]] | Input/error/result/visualization wireframes | Methodology remains open — does not block Stage A | Claude self-critique + ChatGPT review + Founder review | Real formulas, thresholds, or final content |
| **DP-04** — Pojasni pojme First-Pass UX | Produce required Pojasni pojme screens with a demonstrative term subset | Section 7, 13; [[Pojasni pojme Specification]] | Search/browse/term-detail/no-result wireframes | Content and editorial decisions remain open — does not block Stage A | Claude self-critique + ChatGPT review + Founder review | AI chat, real term list, real sourcing |
| **DP-05** — Housing Loans Limited UX | Produce Learn + Monthly Payment Example + cross-links | Section 7, 14; [[Housing Loans Specification]] | Learn overview and example wireframes | None | Claude self-critique + ChatGPT review + Founder review | PDF/AI/comparison features |
| **DP-06** — Shared States and Trust Patterns | Define reusable states (loading, empty, error, disabled, trust/source area) once, for reuse across products | Section 8, 11 | Shared state pattern set | Public source/date visibility open — placeholders only (Section 18.B) | Claude self-critique + ChatGPT review | Final trust wording |
| **DP-07** — Responsive and Accessibility Review | Verify Stage A screens against Section 9–10 intent | DP-02 through DP-06 outputs | Responsive/accessibility findings and adjustments | Final breakpoints and accessibility spec remain open | Claude self-critique + ChatGPT review | Legal compliance claims |
| **DP-08** — First-Pass Design Acceptance | Confirm Stage A completeness against Section 20 (Exit Criteria) | All DP-01–DP-07 outputs | Stage A design-output acceptance record | All Stage A exit criteria must be met | Founder review + ODS commit/push/verify (Section 17) | Declaring Stage B or Stage C readiness; declaring formal document approval |
| **DP-09** — Content-Ready Design Preparation | Identify what Stage B (final content-ready design) will require | Stage A outputs; Sections 12–13 | Stage B readiness checklist | Requires resolved methodology/content per Sections 12–13 | Founder review | Performing Stage B work itself |

No implementation work package is defined in this document.

---

## 17. Design Review Gates

1. Claude self-critique.
2. ChatGPT CTO/Product review.
3. Founder design review.
4. Approved artifact saved to ODS.
5. Controlled commit and push.
6. Direct remote verification.
7. Separate approval-only status commit and subsequent remote verification.

Being visually polished does not automatically mean Approved. Scope correctness, trust framing, and accessibility intent are acceptance criteria alongside visual quality.

For governed NorthStar design documents and formal design-acceptance records, **gate 7 is mandatory, not optional.** No document or acceptance record produced under this kickoff may be marked `Status: Approved` without it.

To remove any ambiguity, the full sequence distinguishes six distinct steps:

1. **Substantive Founder approval** — the Founder's actual decision that the design artifact is acceptable (gate 3).
2. **Controlled content commit and push while the document remains `Status: Draft`** — the artifact's content is saved and pushed, but its frontmatter status is not yet changed (gates 4–5).
3. **Remote verification of that content commit** (gate 6).
4. **A separate approval-only status change** — a dedicated commit that changes only `Status: Draft` to `Status: Approved` (or the equivalent frontmatter field), with no simultaneous content edits (part of gate 7).
5. **Second commit and push** of that approval-only status change (part of gate 7).
6. **Final remote verification** of the approval-only commit (part of gate 7).

Founder review alone, or the first content commit alone, does **not** change a document's status to Approved — steps 4–6 above must also occur. Implementation cannot begin from a design artifact that has not passed all seven gates above — including the mandatory approval-only status commit and its final remote verification — and does not separately satisfy [[MVP]] §9 ("MVP Definition of Done").

---

## 18. Open Design Decisions and External Dependencies

This section separates decisions genuinely owned by design (18.A) from unresolved product/content/governance dependencies owned by an Approved product specification (18.B). It does not duplicate formula, threshold, content-selection, or editorial-methodology decisions already owned by [[Affordability Specification]] §16 or [[Pojasni pojme Specification]] §19 — those are referenced, not repeated.

### 18.A Open design decisions (design-owned)

| Decision | Source | Why it matters | Blocks Stage A? | Blocks Stage B? | Blocks Stage C? | Approver |
|---|---|---|---|---|---|---|
| Exact responsive breakpoints | Section 9 | Needed for a concrete responsive spec | No | No | Yes | Founder / Design owner |
| Responsive presentation mechanism (stacking, scrolling, wrapping, or pagination) while preserving the approved tile order | Section 9 | Affects mobile landing usability; must not reorder the four approved tiles (Section 3.1) | No | No | Yes | Founder / Design owner |
| Interaction feedback (hover/press feedback, tap targets) | Section 3.3 (non-binding hypotheses) | Affects landing feel and consistency with Design Bible's "predictable behaviour" | No | No | Yes | Founder / Design owner |
| Leasing disabled-state presentation and optional informational behavior (exact tap/click behavior, any tooltip or explanatory microcopy) | Section 3.4 | Must read as "coming later," not broken; does not open a Leasing product journey | No | No | Yes | Founder / Design owner |
| No-result presentation (copy, suggested next action) | Section 7 | Affects trust and calm-experience framing | No | No | Yes | Founder / Design owner |
| Long-content expansion or collapse (Learn content, term explanations) | Section 9 | Affects density and mobile readability | No | No | Yes | Founder / Design owner |
| Chart interaction model (hover, tap-to-inspect, static-only) | [[Affordability Specification]] §7.3 | Chart is mandatory; interaction model is not yet decided | No | No | Yes | Founder, with Design owner input |
| Methodology-disclosure placement (inline vs. expandable) | [[Affordability Specification]] §16 item 12 | Affects how "assumptions must remain visible" is satisfied visually | No | Yes | Yes | Founder / Design owner |
| Visual stale-content treatment, once the underlying stale-content policy exists | Policy owned by [[Pojasni pojme Specification]] §19 item 7 (see 18.B); visual treatment is design-owned | Needed so stale content is never silently presented as current | No | Yes | Yes | Founder / content owner + Design owner |
| Design-token system | NorthStar Design Context Pack v2 §14; Design Decisions.md "Known gap" | No token architecture exists in any source document | No | No | Yes | Founder, once component work begins |
| Final typography | [[Design Bible]] "Typography Philosophy" (principles only, no scale defined) | Needed for a concrete type system | No | No | Yes | Founder / Design owner |
| Visual treatment of trust notices (e.g. "educational, not a bank offer" disclaimers) | Product Bible §6; all three product specs' Trust sections | Must be visible without reading as alarming or as legal boilerplate | No | Yes | Yes | Founder / Design owner |
| Visual accessibility acceptance criteria, derived from subsequently approved requirements | Requirement owned by both specs' "Open Decisions" tables (see 18.B); visual criteria are design-owned once the requirement exists | Needed before Stage C sign-off | No | Yes | Yes | Founder, with Design owner recommendation |

### 18.B External unresolved product/content/governance dependencies

None of the items below are decided by this document. Each is owned by an Approved product specification; this table only shows how it constrains design work.

| Dependency | Owning specification | How it affects design | Blocks Stage A? | Blocks Stage B? | Blocks Stage C? |
|---|---|---|---|---|---|
| Pojasni pojme category taxonomy | [[Pojasni pojme Specification]] §19 item 3 | Drives navigation and discovery design | No | Yes | Yes |
| Whether verified sources are publicly visible | [[Pojasni pojme Specification]] §19 item 11; [[Affordability Specification]] §9 | Changes what the trust area must render | No | Yes | Yes |
| Whether last-validation dates are publicly visible | [[Pojasni pojme Specification]] §19 item 12 | Changes what the term-detail trust area must render | No | Yes | Yes |
| Underlying revalidation policy (cadence, trigger events, the stale-content rule itself) | [[Pojasni pojme Specification]] §19 item 7 | Determines when the design's stale-content treatment (18.A) must appear | No | Yes | Yes |
| Final product-level accessibility requirements, where still owned by the product specifications | [[Affordability Specification]] §16 item 12; [[Pojasni pojme Specification]] §19 item 17 | Sets the requirement that Section 10 and 18.A's visual criteria must satisfy | No | Yes | Yes |

This document does not duplicate formulas, thresholds, term-selection methodology, sourcing governance, or editorial ownership decisions — those remain owned exclusively by [[Affordability Specification]] §16 and [[Pojasni pojme Specification]] §19.

---

## 19. Design Phase Entry Criteria

Complete and available today:

- Core product architecture (DR-013: four standalone first-phase products, shared-capability model).
- Release scope for the first public MVP (DR-014 through DR-017; [[MVP]] v0.1, Approved).
- Three Approved product specifications: [[Housing Loans Specification]], [[Affordability Specification]], [[Pojasni pojme Specification]].
- Approved landing foundation (Section 3), communicated directly by the Founder and structurally consistent with DR-001/DR-006/DR-014.
- Key trust boundaries (educational, not advice; no bank approval prediction; no hidden persuasion) — stated consistently across the Constitution, Product Bible, and all three product specifications.

Not required before first-pass design can begin:

- Final Affordability formulas, thresholds, or living-cost methodology.
- The final 30–50 Pojasni pojme terms, categories, or sources.
- A final editorial workflow or staffing model.
- Any technical implementation.

First-pass design can begin safely because Stage A (Section 15) is explicitly permitted to use placeholder and demonstrative values (per both product specifications' "Open Decisions" tables), and because the screen hierarchy, navigation, and interaction model it establishes do not depend on which exact formula or term list is eventually approved.

---

## 20. Design Phase Exit Criteria

Two distinct things are assessed here, and they must not be conflated:

- **Stage A design-output acceptance** — whether the actual screens, journeys, and states described in Sections 5–11 have been produced and reviewed.
- **Formal document approval** — whether this kickoff document, or a Stage A acceptance record derived from it, has actually been moved from `Status: Draft` to `Status: Approved` via the mandatory approval-only commit sequence in Section 17.

Stage A design-output acceptance is complete only when:

- the required screens in Section 7 exist;
- the primary journeys in Section 5 are represented;
- the core states in Section 8 are represented;
- mobile and desktop intent (Section 9) are documented, including the tile-order preservation constraint;
- trust boundaries (Section 11) are visible on every relevant screen;
- placeholders are clearly marked as placeholders, not presented as final content or methodology;
- the exclusions in Sections 4–5, 13–14 are respected (no Ask AI, no PDF flow, no bank comparison, no approval prediction, no complete Leasing flow, no internal Leasing screen);
- Claude self-critique is complete;
- ChatGPT CTO/Product review is complete;
- Founder approval is recorded;
- artifacts are saved, committed, pushed, and remote-verified (Section 17, gates 4–6).

Stage A design-output acceptance being complete does **not**, by itself, make this document or any derived acceptance record formally Approved. Formal approval additionally requires the separate approval-only status commit, its own commit and push, and final remote verification (Section 17, steps 4–6). Until all of that has occurred, the document — and any Stage A acceptance record derived from it — remains `Status: Draft`, regardless of how complete the Stage A content is.

Completion of Stage A does not imply Stage B (final content-ready) or Stage C (implementation-ready) readiness (see Section 15 for the exact Stage definitions). Those require the additional dependencies listed in Sections 12, 13, and 18, and in each product specification's "Open Decisions" table.

---

## 21. Document Boundaries

- Product documents ([[Product Bible]], [[MVP]], [[Features]], the three Approved product specifications) own product scope.
- [[Design Bible]] owns design principles according to its actual current status — **Draft**, not Approved. It informs but does not by itself authorize design decisions that conflict with Approved product scope.
- This kickoff document owns design-phase sequencing, scope boundaries, minimum journey coverage, minimum screen/state coverage, dependencies, and review gates. It does not own final screen composition, final visual design, final component specifications, design tokens, or technical realization.
- Wireframes (to be produced under DP-02 through DP-05) and later approved design-system artifacts own final screen composition, final visual design, and component details.
- Design-system documents (`02 Design/Design System.md`, currently an empty Draft stub) own reusable visual rules and design tokens.
- Implementation specifications (not yet created) own technical realization.

---

## 22. Related Documents

- [[NorthStar Constitution]]
- [[NorthStar OS Specification]]
- [[Product Bible]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
- [[User Journey Specification]]
- [[Housing Loans Specification]]
- [[Affordability Specification]]
- [[Pojasni pojme Specification]]
- [[Design Bible]]
