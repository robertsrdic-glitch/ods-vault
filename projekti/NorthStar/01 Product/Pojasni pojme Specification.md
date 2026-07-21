# Pojasni pojme Specification

Version: 1.0
Status: Approved
Category: Product
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
- [[Design Bible]]

---

## 1. Purpose

Pojasni pojme helps users understand important financial concepts in plain language, before or during a financial decision.

It is educational, favors clarity before complexity, does not persuade the user toward any conclusion, and does not recommend a specific bank, lender, or financial product. Full trust boundaries are stated in [Section 15](#15-trust-and-product-boundaries) (DR-017, Product Bible §§1–2, §6).

---

## 2. Product Role

Pojasni pojme is one of NorthStar's four standalone first-phase products (DR-013).

It is one of the two core products of the first public MVP release (DR-014).

Term explanations may be reused by Stanovanjski kredit, and in time by Affordability, Leasing, and future products, through the shared Financial Terms capability — but this technical reuse does not reduce the standalone product status of Pojasni pojme (DR-012, DR-013, DR-017).

Detailed release scope is owned by [[MVP]]. Approved architecture and decisions are owned by [[Decision Register]] and [[Product Bible]].

---

## 3. MVP Country Scope

The first public MVP is limited to Slovenia. Pojasni pojme uses the authoritative content unit:

`Slovenia Country Content Pack`

The pack is expected to contain approximately 30–50 curated key financial terms. The exact list is not decided in this document (DR-017).

No other country pack launches in the first public MVP release. The system architecture may be built to support future country packs, but that architectural readiness does not by itself expand current MVP scope (DR-017, Product Bible §11).

A country pack is not merely a translation bundle. It contains locally validated content, terminology, sources, examples, and review history specific to that country. Content for a new country must not be created by automatic translation of an existing pack alone (DR-017, Product Bible §11).

---

## 4. Target User and User Goal

Pojasni pojme is for users who:

- encounter unfamiliar terminology in bank, loan, leasing, affordability, or other financial-decision contexts;
- need a plain explanation without pressure;
- want to understand why a term matters to their situation;
- want to explore connected concepts.

No specific age group, income level, or demographic segment is defined; the audience is described by the situation a person is in, not by who they are (Product Bible §3).

The user goal is understanding, not obtaining a recommendation or a decision (DR-017, Product Bible §2).

---

## 5. MVP Discovery Model

The MVP includes:

- a search field;
- simple categories;
- access to an individual term's explanation;
- related-term navigation (DR-017).

Search helps locate curated, published terms. Categories organize the pack simply. Related terms support learning paths. The final taxonomy, category names, and detailed search behavior are not decided in this document (see [Section 19](#19-open-decisions-before-implementation)).

The MVP does not include AI chat, user accounts, saving favorite terms, personalized explanations, or user-generated content (DR-017).

---

## 6. Term Content Model

Each published term must contain four required user-facing parts (DR-017).

### 6.1 Plain-language explanation

- Understandable without specialist knowledge.
- Concise enough for an ordinary user.
- Free of unnecessary jargon; jargon may be used only when immediately explained.
- Must not create false certainty.

### 6.2 Simple example

- Concrete and realistic.
- Educational.
- Understandable without a calculator, unless the term itself requires a numeric example.
- Not presented as a bank offer, an official calculation, or personalized advice.
- Locally relevant where jurisdiction matters.

### 6.3 Why it matters

- Explains how misunderstanding the term could affect a financial decision.
- Focuses on practical consequences.
- Does not use fear or pressure.
- Does not recommend a lender or product.

### 6.4 Related terms

- Links only to curated terms in the active country pack, unless a deliberate placeholder rule is separately approved.
- Supports exploration without creating an endless dependency graph.
- Relationship type or ranking between related terms is not decided in this document.

This four-part structure is the confirmed content model. It is not replaced by a generic dictionary-style definition (DR-017).

---

## 7. Term Metadata and Editorial Record

The following record elements are directly confirmed by DR-017 as the minimum a term record must support, without defining a technical schema:

- canonical concept ID;
- country pack;
- language;
- local term name;
- verified source or sources;
- last validation date;
- review or approval status;
- the four content fields defined in [Section 6](#6-term-content-model) (plain-language explanation, example, why it matters, related terms), which remain part of each term record.

Category also exists as a record element, consistent with the confirmed category discovery model in [Section 5](#5-mvp-discovery-model); the exact category taxonomy is unresolved (see [Section 19](#19-open-decisions-before-implementation)).

Not all internal editorial metadata needs to appear in the public user interface.

Whether the record model also needs aliases, synonyms, version history, source excerpts, risk classifications, or source publication/access dates is not decided by any authoritative source. These are not added as mandatory MVP metadata here; see [Section 19](#19-open-decisions-before-implementation).

---

## 8. Country Content Pack Model

The Slovenia Country Content Pack is a governed editorial unit. It must contain:

- selected terms;
- localized explanations;
- locally relevant examples;
- verified sources;
- review and approval records;
- last-validation dates;
- category and relationship structure (DR-017).

Another country requires its own separate content pack, with its own sources and approval history. Country packs may share product structure, but do not automatically share authoritative content (see [Section 3](#3-mvp-country-scope) for the translation and localization boundary) (DR-017, Product Bible §11).

This document does not define a database model or deployment architecture for country packs.

---

## 9. Source Requirements

- Primary, official, regulatory, public-institution, or otherwise authoritative sources are preferred (DR-017).
- Enough source information must be recorded to allow later verification.
- Source-backed facts must be distinguishable from NorthStar's plain-language editorial explanation.
- Unattributed AI output must not be relied on as a source.
- If authoritative sources conflict or differ by context, that uncertainty must remain visible, and the content must be reviewed rather than silently resolved.
- No unsupported current rule may be published from AI model memory alone.

This document does not define a final approved source hierarchy. Source-hierarchy governance is listed as an open decision (see [Section 19](#19-open-decisions-before-implementation)).

---

## 10. AI-Assisted Editorial Workflow

AI may assist with:

- research;
- candidate-source discovery and comparison;
- preparation of drafts;
- rewriting for clarity;
- preparation of examples;
- identifying possible local or contextual differences that need human attention (DR-017).

AI must not:

- automatically publish content;
- independently confirm legal or financial correctness;
- replace human editorial review;
- generate live, on-the-fly explanations presented to users as authoritative term content (DR-017).

All AI-assisted output remains Draft until the human editorial gate described in [Section 11](#11-human-editorial-and-publishing-gate) is completed. This document does not specify a particular AI provider or model.

---

## 11. Human Editorial and Publishing Gate

A term may become Published only after:

1. research;
2. source recording;
3. source verification;
4. content or editorial review;
5. explicit approval;
6. recording of the last-validation date (DR-017).

- Exact editorial roles, separation of duties, and responsibility assignments are unresolved and require Founder approval.
- The required sources, review or approval status, and last-validation date must be recorded before publication.
- No automatic publication is allowed.
- Material changes to published content require renewed review, approval, and validation before the updated content is treated as current.
- Expired or uncertain content must not remain silently represented as current.

This document does not define a complete staffing model.

---

## 12. Publication Status Model

DR-017 requires that each term record carry a review or approval status. Exact status names, lifecycle stages, and transitions are not decided by any authoritative source and belong in [Section 19](#19-open-decisions-before-implementation). This document does not define or imply any particular status model, and it does not build a workflow engine.

---

## 13. Validation and Maintenance

- Every published term has a last-validation date (DR-017).
- Stale or changed content requires a revalidation policy.
- Legal, regulatory, banking, or country-specific changes may trigger revalidation.
- The revalidation policy must define whether and when unchanged content is reviewed again.
- Publication must not imply perpetual validity.

Validation cadence, trigger events, ownership, and stale-content behavior are not decided in this document; they are consolidated into a single open decision (DR-017, [[MVP]] §8; see [Section 19](#19-open-decisions-before-implementation)).

---

## 14. High-Level User Experience

A safe high-level structure:

1. User enters the standalone product.
2. User searches or browses a category.
3. User opens a curated term.
4. User reads the explanation, example, and why it matters.
5. User may open a related term.
6. User returns to the financial decision with clearer understanding.

This sequence may be adapted during design and does not define final screens. Public users do not edit authoritative content. Live Ask AI is not part of this product's first-public-MVP scope (DR-017).

---

## 15. Trust and Product Boundaries

- NorthStar is not a bank, lender, broker, or financial adviser.
- This is educational content, not individualized advice.
- It is not a substitute for professional legal, tax, accounting, banking, or financial guidance.
- Explanations may simplify a more complex underlying rule.
- Locally sensitive content depends on verified country-specific sources.
- Uncertainty and limitations must remain visible.
- Published content must be traceable to verified sources and editorial approval.
- NorthStar must not use explanations to steer users toward a commercial product.
- The user remains responsible for the final decision (Product Bible §§1, 6, 13; NorthStar Constitution).

---

## 16. Explicitly Excluded from the First Public MVP

Confirmed exclusions (DR-017, [[MVP]] §4.2):

- AI chat;
- automatic generation of answers or explanations for users;
- automatic publication of AI content;
- user accounts;
- saving favorite terms;
- personalized explanations;
- user-generated content;
- country packs outside Slovenia;
- automatic translation as a substitute for local research and validation.

These are current-release exclusions. They are not framed as permanent product non-goals, and none of them is confirmed for a future release without a new Founder-approved decision. The pack itself remains limited to approximately 30–50 curated terms ([Section 3](#3-mvp-country-scope)); this is a scope statement, not a separate confirmed exclusion.

---

## 17. Edge Cases and Content Safety Principles

Without inventing final workflow rules, the product must account for:

- ambiguous term names;
- synonyms;
- terms with different meanings across countries and, where verified evidence shows it, across institutions;
- terms whose meaning changes over time;
- conflicting sources;
- an unavailable official source;
- a related term not yet published;
- an incomplete editorial record;
- expired validation;
- withdrawn or superseded terms;
- misleadingly simple examples.

Principles:

- the product must not fabricate a definitive explanation;
- uncertainty must remain visible;
- publication should stop if verification is inadequate;
- local context must be made explicit where material;
- older content must not silently override newer validated content.

---

## 18. Success Criteria

- Users understand a previously unfamiliar term.
- Users can explain why the term matters.
- Users can connect it to related concepts.
- Content feels clear rather than promotional.
- Users can recognize that an explanation is educational and locally scoped.
- Every published term has verified sourcing, review, approval, and last-validation evidence.
- No term is automatically published from AI output.
- Users are not falsely reassured by oversimplification.

No numeric KPIs are defined in this document ([[MVP]] §7).

---

## 19. Open Decisions Before Implementation

First-pass design may proceed using a small demonstrative subset of terms and placeholder editorial states. Final content-ready and implementation-ready design require the decisions below.

| # | Decision | Why it matters | Blocks first-pass design? | Blocks final content-ready design? | Blocks implementation? | Who must approve |
|---|---|---|---|---|---|---|
| 1 | Exact list of the initial ~30–50 curated terms | Determines the actual MVP content pack | No | Yes | Yes | Founder / content owner, with verified sources |
| 2 | Prioritization criteria for selecting the initial term set | Needed to produce a defensible, non-arbitrary list | No | Yes | Yes | Founder |
| 3 | Concrete category taxonomy and names | Drives navigation and the discovery model | No | Yes | Yes | Founder, with Design owner input |
| 4 | Source hierarchy governance (which source types take precedence, how conflicts are resolved) | Needed for consistent, defensible sourcing | No | Yes | Yes | Founder, with verified official sources |
| 5 | Exact editorial roles, separation of duties, and responsibility assignments (e.g., whether review and approval are the same person or different people) | Affects editorial integrity and staffing | No | Yes | Yes | Founder |
| 6 | Publication-status names and transitions | Needed for a workable editorial lifecycle | No | No | Yes | Founder or delegated technical owner |
| 7 | Revalidation cadence, trigger events, and stale-content behavior | Needed to prevent silently stale content and to define how stale content is treated | No | Yes (for public stale-content treatment) | Yes | Founder or delegated content owner |
| 8 | Alias and synonym model | Affects discoverability and search quality | No | No | Yes | Founder or delegated technical owner |
| 9 | Related-term relationship model or ranking | Affects the learning-path experience | No | No | Yes | Founder or delegated technical owner |
| 10 | Whether and how institution-specific variations are represented, when verified sources show meaningful differences | Needed for accuracy where a single country-level definition is insufficient | No | Yes | Yes | Founder, with verified sources |
| 11 | Whether verified source links are shown publicly | Affects transparency and UX design | No | Yes | Yes | Founder, with Design owner input |
| 12 | Whether the last-validation date is shown publicly | Affects transparency and UX design | No | Yes | Yes | Founder, with Design owner input |
| 13 | Content version history requirement | Current scope does not require it unless Founder expands it | No | No | Only if the Founder chooses to add it | Founder |
| 14 | Editorial audit evidence / record-keeping format | Needed to prove the publishing gate occurred | No | No | Yes | Founder or delegated technical owner |
| 15 | Localization and approval workflow for future country packs | Needed before any country beyond Slovenia can launch | No | No (does not block Slovenia pack) | Yes, for any future country pack | Founder, with verified local sources |
| 16 | Technical country-pack format | Needed for implementation, not for design | No | No | Yes | Founder or delegated technical owner |
| 17 | Accessibility requirements beyond general principles | Detailed accessibility spec not yet written | No | Yes | Yes | Founder, with Design owner recommendation |
| 18 | Search behavior and tolerance for spelling variants | Affects discoverability | No | No | Yes | Founder or delegated technical owner |
| 19 | Whether source publication or access dates are recorded as additional editorial metadata | Not required by DR-017; only relevant if the Founder chooses to expand the metadata model | No | No | Only if the Founder adds it | Founder |

---

## 20. Document Boundaries

- [[Decision Register]] owns approved product and governance decisions.
- [[MVP]] owns current release scope.
- [[Features]] owns the product and feature catalog.
- [[Product Bible]] owns durable product architecture and philosophy.
- [[User Journey Specification]] owns the cross-product journey framework.
- [[Design Bible]] owns visual and interaction principles.
- This specification owns product-level content structure, editorial behavior, country-pack boundaries, trust rules, and publishing requirements for Pojasni pojme.
- The actual Slovenia Country Content Pack requires separate curated content work and approval.
- Technical schema and CMS workflow require later technical specifications.

---

## 21. Related Documents

- [[NorthStar Constitution]]
- [[NorthStar OS Specification]]
- [[Product Bible]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
- [[User Journey Specification]]
- [[Housing Loans Specification]]
- [[Affordability Specification]]
- [[Design Bible]]
