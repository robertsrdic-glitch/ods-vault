# Features

Status: Draft

Catalog of NorthStar's four first-phase products, their confirmed product and UX status, the shared capabilities that support them at a technical level, candidate features still awaiting MVP confirmation, and historically superseded or unresolved scope.

Related Documents:
- [[Decision Register]]
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

DR-013 determines the product status of all four first-phase products. DR-011 and DR-012 determine the technical, architectural reuse of the capabilities that support two of them. A shared capability does not reduce the status of a standalone product.

Where an older document (e.g. [[Housing Loans Specification]], [[User Journey Specification]], [[Design Bible]]) states something that conflicts with these Founder-approved decisions, the Decision Register takes precedence.

---

## First-Phase Products

Per [[Decision Register]] DR-013, NorthStar has exactly four first-phase products:

### Stanovanjski kredit

- Standalone first-phase product.
- Has a detailed specification: [[Housing Loans Specification]].
- Its final MVP feature scope has not yet been formally confirmed.

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

## Housing Loans — Candidate Features Pending MVP Confirmation

The following features originate from the earlier [[Housing Loans Specification]] and describe how the Stanovanjski kredit product might use existing capabilities and content. Learn, Monthly Payment Examples, and Ask AI have not yet been formally confirmed as final MVP or first-phase feature scope; this document retains them as candidates pending the upcoming MVP review. The absence of a conflict with the Decision Register does not mean automatic Founder approval.

- **Learn** — educational content covering the mortgage process, fixed vs. variable interest, APR, down payment, loan duration, early repayment, and refinancing. Candidate pending MVP confirmation.
- **Monthly Payment Examples** — interactive educational examples using loan amount, interest rate, and duration; explicitly not a banking calculator. Candidate pending MVP confirmation.
- **Affordability** — the standalone product **Koliko kredita si lahko privoščim** is already confirmed, and the Affordability capability is already confirmed (DR-011, DR-013). What is not yet confirmed is exactly how, and to what extent, Stanovanjski kredit will use this capability.
- **Financial Terms** — the standalone product **Pojasni pojme** is already confirmed, and the Financial Terms capability is already confirmed (DR-012, DR-013). What is not yet confirmed is exactly how, and to what extent, Stanovanjski kredit will use this capability.
- **Ask AI** — natural-language question answering about a user's mortgage situation. Candidate pending MVP confirmation.

`PDF Offer Explanation` is not included in this list — see "Superseded or Unresolved Historical Scope" below.

---

## Leasing — Current Status

- Leasing is confirmed as a standalone first-phase product and primary UX entry point.
- A detailed Leasing specification does not yet exist.
- This document does not invent Leasing features.

---

## Koliko kredita si lahko privoščim — Current Status

- The product is confirmed as a standalone first-phase product.
- Its basic user purpose is estimating a safe monthly payment / affordability.
- A detailed product or feature specification has not yet been formalized.
- This document does not invent additional features.

---

## Pojasni pojme — Current Status

- The product is confirmed as a standalone first-phase product.
- Its basic purpose is simple, jargon-free explanations of financial terms.
- It is supported by the shared Financial Terms capability.
- A detailed product or feature specification has not yet been formalized.
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
