# Features

Status: Approved

Catalog of NorthStar's four first-phase products, their confirmed product and UX status, the shared capabilities that support them at a technical level, confirmed first-public-MVP scope per DR-014 through DR-017 and approved [[MVP]] v0.1, and historically superseded or unresolved scope.

Related Documents:
- [[Decision Register]]
- [[MVP]]
- [[User Journey Specification]]
- [[Housing Loans Specification]]
- [[Design Bible]]

---

## Purpose

This document summarizes the currently valid product structure. Where an older specification conflicts with a later Founder-approved decision, the Decision Register governs. This document does not introduce any new feature or decision of its own — every entry below either traces to an existing source document or to the Decision Register.

---

## Authoritative Decision Source

Product architecture in this catalog follows [[Decision Register]], specifically:

- **DR-001** — first-screen structure (four primary entry points).
- **DR-002** — PDF / bank-offer scope (superseded, first-phase exclusion).
- **DR-011** — Affordability architecture (shared capability, clarified by DR-013).
- **DR-012** — Financial Terms architecture (shared educational capability, clarified by DR-013).
- **DR-013** — the four first-phase products and the separation between a product and a shared capability.
- **DR-014** — first public MVP release structure (which products, and in what depth, enter the first release).
- **DR-015** — limited Housing Loans MVP scope for the first public release.
- **DR-016** — Affordability MVP scope for Koliko kredita si lahko privoščim.
- **DR-017** — Financial Terms / Pojasni pojme MVP scope and the Slovenia Country Content Pack model.

DR-013 determines the product status of all four first-phase products. DR-011 and DR-012 determine the technical, architectural reuse of the capabilities that support two of them. A shared capability does not reduce the status of a standalone product. DR-014 through DR-017 determine first-public-MVP-release depth and scope; the approved [[MVP]] v0.1 is the operative document for that detailed MVP scope.

Where an older document (e.g. [[Housing Loans Specification]], [[User Journey Specification]], [[Design Bible]]) states something that conflicts with these Founder-approved decisions, the Decision Register takes precedence.

---

## First-Phase Products

Per [[Decision Register]] DR-013, NorthStar has exactly four first-phase products:

### Stanovanjski kredit

- Standalone first-phase product.
- Has a detailed specification: [[Housing Loans Specification]].
- Its limited first-public-MVP-release feature scope is confirmed (DR-015; see [[MVP]] §4.3).

### Leasing

- Standalone first-phase product.
- Primary UX entry point.
- No detailed specification exists yet.
- This document does not invent Leasing features.

### Koliko kredita si lahko privoščim

- Standalone first-phase product.
- Has its own primary UX entry point.
- Has its own, standalone user purpose.
- Supported by the shared Affordability capability.
- The same affordability logic can also be used by other products.

References: DR-003, DR-011, DR-013.

### Pojasni pojme

- Standalone first-phase product.
- Has its own primary UX entry point.
- Has its own, standalone user purpose.
- Supported by the shared Financial Terms capability.
- The same source of financial term explanations can also be used by other products.

References: DR-004, DR-012, DR-013.

---

## First-Screen UX Entry Points

Per [[Decision Register]] DR-001 and DR-013, the first screen has exactly four primary entry points, and all four represent standalone first-phase products:

1. **Stanovanjski kredit**
2. **Leasing**
3. **Koliko kredita si lahko privoščim**
4. **Pojasni pojme**

For the last two, a shared technical capability exists (see below), separate from their product status — the shared capability is a technical/architectural fact, not a reduction of their status as standalone first-phase products.

In the first public MVP release (DR-014), the Leasing entry point remains visible on the first screen, carries a `Kmalu` label, and is clearly visually and behaviorally inactive rather than a broken or partially working control. This does not remove Leasing from the first phase — it is deferred to the next release within the first phase, pending a dedicated Leasing specification.

---

## Shared Capabilities Supporting First-Phase Products

This section describes technical/architectural reuse — it does not classify products. A product and a shared capability are separate concepts: a product has its own UX entry point and user purpose; a shared capability describes reusable logic, data models, or content sources that one or more products can draw on.

### Affordability capability

- Product: **Koliko kredita si lahko privoščim**.
- Capability: Affordability.
- The Affordability capability supports this standalone product.
- The same capability can also be used by Stanovanjski kredit, Leasing, and future products.

### Financial Terms capability

- Product: **Pojasni pojme**.
- Capability: Financial Terms.
- The Financial Terms capability supports this standalone product.
- The same shared source of explanations can also be used by other products.
- Content should not be duplicated unnecessarily across products when the shared source can be used instead.

---

## Housing Loans — Confirmed First Public MVP Scope

The limited first-public-MVP-release scope for Stanovanjski kredit is confirmed (DR-015; see [[MVP]] §4.3), superseding the earlier candidate-pending-confirmation framing of these items from [[Housing Loans Specification]].

**Included:**

- **Learn** — short, structured, understandable content on the basics of housing loans. Confirmed included (DR-015).
- **Monthly Payment Examples** — simple educational monthly-payment examples. Confirmed included (DR-015). Must remain described as educational and approximate; not a bank calculation, not a bank offer, and not personal financial advice.
- A link to the standalone product **Koliko kredita si lahko privoščim** — the Affordability capability is used through this link, not duplicated inside Stanovanjski kredit (DR-011, DR-013, DR-015).
- A link to the standalone product **Pojasni pojme** / shared Financial Terms capability — used through this link, not duplicated inside Stanovanjski kredit (DR-012, DR-013, DR-015).

**Explicitly excluded from the first public MVP release (DR-015):**

- Ask AI;
- PDF Offer Explanation;
- offer comparison;
- personalized learning;
- bank-meeting preparation;
- advanced simulations;
- user accounts;
- saved history.

`PDF Offer Explanation` is addressed further under "Superseded or Unresolved Historical Scope" below.

---

## Leasing — Current Status

- Leasing is confirmed as a standalone first-phase product and primary UX entry point.
- A detailed Leasing specification does not yet exist.
- This document does not invent Leasing features.

---

## Koliko kredita si lahko privoščim — Current Status

- The product is confirmed as a standalone first-phase product.
- Its basic user purpose is estimating a safe monthly payment / affordability.
- DR-016 and approved [[MVP]] §4.1 define the first public MVP scope: confirmed user inputs; a NorthStar-proposed minimum living-cost estimate that the user can adjust; recurring contractual obligations; a range-based main result (not a single falsely precise figure); risk classifications (bolj varno / napeto / previsoko tveganje); a required dual visualization (safe-range chart and monthly money allocation); and trust boundaries (not a bank approval, not a formal creditworthiness assessment, not personal financial advice).
- Still open per DR-016 and approved [[MVP]] §8: the exact formula; concrete safety thresholds; the minimum living-cost methodology; Slovenian localization of that methodology; validation and test data; detailed visualization UX; and accessibility requirements.
- This document does not invent additional features.

---

## Pojasni pojme — Current Status

- The product is confirmed as a standalone first-phase product.
- Its basic purpose is simple, jargon-free explanations of financial terms.
- It is supported by the shared Financial Terms capability.
- DR-017 and approved [[MVP]] §4.2 define the first public MVP scope: Slovenia-only support via the `Slovenia Country Content Pack`; approximately 30–50 curated concepts; core functionality (search, simple categories, individual concept explanations, related-concept links); a required four-part explanation structure (short plain-language explanation, concrete example, why it matters, related concepts); AI limited to research and drafting assistance, never automatic publishing, never independent legal/financial validation, never a replacement for editorial review, and never live generative user-facing explanations; a mandatory source-recording, verification, editorial-review, approval, and last-validation-date gate before publication; future country-pack architecture without including any country beyond Slovenia in the current MVP; and reuse of the same curated collection as the shared Financial Terms capability inside Stanovanjski kredit without changing Pojasni pojme's standalone-product status.
- Still open per DR-017 and approved [[MVP]] §4.2: the exact list of ~30–50 concepts; concrete categories; prioritization criteria; official sources per concept; the editorial/review process; final approval ownership; search and navigation UX; the technical country-pack format; accessibility requirements; and the revalidation cadence for potentially outdated content.
- This document does not invent additional features.

---

## Housing Loans — Historical Future Candidates from Earlier Specification

Source: [[Housing Loans Specification]] §"Future Versions." This list originates from the earlier Housing Loans Specification. It is not active first-phase scope, and it is not a formally approved Roadmap or deferred backlog. Individual items must not be treated as confirmed future features. Their status will be decided only through the Roadmap process, which is not yet formalized.

- Compare multiple mortgage offers
- Personalized learning
- Mortgage timeline
- AI preparation for bank meetings
- Advanced repayment simulations

---

## Superseded or Unresolved Historical Scope

### PDF Offer Explanation

- The earlier [[Housing Loans Specification]] tagged PDF Offer Explanation as MVP.
- [[Decision Register]] DR-002 later determined that the **Razloži ponudbo banke** card is not part of the first screen and is not part of the first phase.
- As a result, PDF Offer Explanation is not an active first-phase feature.
- Its possible future status has not yet been determined.
- It must not be treated as a confirmed deferred or roadmap feature without a new Founder decision.

### Document Analysis

- Older documents used the term `Document Analysis`.
- The Decision Register does not confirm it as a first-phase product.
- Its possible future role has not been determined.
- This document therefore does not classify it as either an active or a confirmed future product.

---

## Out of Scope for This Document

This document does not define:

- the full MVP definition,
- roadmap sequencing,
- the technical implementation of shared capabilities,
- the detailed Leasing feature scope,
- the future status of PDF or Document Analysis features,
- the final Housing Loans MVP feature scope,
- a confirmed deferred backlog,
- the final feature scope of the Koliko kredita si lahko privoščim product,
- the final feature scope of the Pojasni pojme product.

These topics require separate approved documents or Founder decisions.
