# User Journey Specification

Version: 1.0
Status: Draft
Category: Product
Owner: Founder
Related Documents:
- [[NorthStar Constitution]]
- [[NorthStar OS Specification]]
- [[Product Bible]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
- [[Housing Loans Specification]]
- [[Design Bible]]

---

## 1. Purpose

This document defines a flexible journey framework for NorthStar.

It describes the broad user experience: the user's progression from uncertainty toward understanding, the trust and clarity principles shared across products, and common journey phases that individual products may adapt.

This document does not define one identical flow for every product. NorthStar has four standalone products with different user purposes and primary entry points; each may express these phases differently, or skip phases that don't apply.

---

## 2. Journey Versus Flow

### User Journey

The broader experience, including:

- user motivation;
- the uncertainty or decision context the user starts from;
- the understanding gained;
- confidence and clarity reached;
- movement between relevant standalone products;
- completion without pressure.

### User Flow

A concrete sequence of screens, actions, decisions, states, errors, and transitions for a specific product or use case.

Product-specific flows must be documented separately and may differ from one another.

---

## 3. Product Context

NorthStar has four standalone first-phase products (DR-013):

- Stanovanjski kredit;
- Leasing;
- Koliko kredita si lahko privoščim;
- Pojasni pojme.

Each product has its own primary entry point and serves a different user purpose. Shared capabilities (such as Affordability or Financial Terms) support some of these products technically, but do not reduce their standalone status (DR-011, DR-012, DR-013).

The current first public MVP release activates different levels of functionality per product (DR-014):

- Koliko kredita si lahko privoščim and Pojasni pojme are core products of the first public MVP release;
- Stanovanjski kredit is present as a limited initial version (DR-015);
- Leasing is visible on the first screen but inactive, labeled `Kmalu`, and deferred to a later release within the first phase.

Detailed per-product scope is not duplicated here — see [[MVP]], [[Features]], and each product's own specification.

---

## 4. Common Journey Principles

- clarity before complexity;
- education before recommendation;
- trust before persuasion;
- privacy first;
- a calm, non-judgmental experience;
- no hidden selling;
- no false precision;
- assumptions and limitations kept visible;
- the user remains in control;
- completion is defined by understanding, not by engagement time.

These principles are grounded in [[NorthStar Constitution]], [[NorthStar OS Specification]], [[Product Bible]], and [[Design Bible]].

---

## 5. Flexible Journey Framework

The following phases describe a common shape that products may adapt. Not every product needs to express every phase, and not every phase needs to be a separate screen or step.

### 5.1 Arrive

The user enters through a product-specific entry point with a question, uncertainty, or learning goal.

### 5.2 Orient

The product quickly explains what it can help with, what it cannot do, what information or action may be needed, and its important trust boundaries.

### 5.3 Understand

The user receives plain-language context, concepts, examples, or framing appropriate to the selected product.

### 5.4 Explore

The user may interact with the product's confirmed current capabilities.

The interaction model depends on the selected product and must remain within its confirmed current scope.

### 5.5 Clarify

The user sees the assumptions, uncertainty, limitations, relevant distinctions, and questions worth considering behind what they were shown.

### 5.6 Continue or Conclude

The user may finish with improved understanding, continue within the same product, follow an intentional link to another standalone NorthStar product, or return later without pressure.

---

## 6. Cross-Product Movement

Cross-links between standalone products should be intentional and contextually relevant, and should help the user understand why another product may help them.

Cross-links must not imply that one product owns another. Users should not be funneled through all four products, and product switching must not feel like an upsell. A shared capability may support multiple products in the background without implying that any one product owns another.

Stanovanjski kredit's links to Koliko kredita si lahko privoščim and Pojasni pojme (DR-015) are one approved example of this pattern — this section is not a Stanovanjski kredit-specific flow, and its detailed behavior remains owned by [[Housing Loans Specification]].

---

## 7. Current MVP Journey Constraints

At a high level, the current first public MVP release does not assume:

- a universal user account requirement;
- a saved-history requirement;
- Ask AI;
- document upload or PDF analysis;
- offer comparison.

Additionally:

- Stanovanjski kredit's current scope is limited to Learn and Monthly Payment Examples (DR-015);
- Koliko kredita si lahko privoščim and Pojasni pojme each have their own standalone journeys, not defined here.

Detailed functionality, calculations, content schemas, and release acceptance criteria are not duplicated in this document — see [[MVP]] and [[Features]].

---

## 8. Trust and Safety Across the Journey

Every journey must:

- distinguish education from recommendation;
- show uncertainty honestly;
- avoid predicting bank approval;
- avoid presenting estimates as offers or guarantees;
- avoid hidden persuasion;
- preserve privacy;
- make limitations clear;
- avoid invented facts;
- support user understanding before action.

This document does not introduce legal claims or compliance guarantees.

---

## 9. Journey Success Criteria

- the user knows where they are and what the product can do;
- the user understands the relevant topic more clearly;
- assumptions and limitations are understood;
- the user can identify useful next questions;
- movement to another product is understandable and optional;
- the user does not feel pressured;
- the product can conclude successfully without maximizing time or clicks.

---

## 10. Document Boundaries

- [[Product Bible]] owns durable product philosophy and architecture.
- [[Decision Register]] owns approved decisions and their supersession history.
- [[MVP]] owns current release scope.
- [[Features]] owns the product and feature catalog.
- Product specifications (e.g. [[Housing Loans Specification]]) own detailed product behavior.
- [[Design Bible]] owns visual and interaction principles.
- Detailed screen-by-screen flows belong in separate product- or use-case-specific flow specifications.

This document must not be used to infer a feature that is not approved elsewhere.

---

## 11. Related Documents

- [[NorthStar Constitution]]
- [[NorthStar OS Specification]]
- [[Product Bible]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
- [[Housing Loans Specification]]
- [[Design Bible]]
