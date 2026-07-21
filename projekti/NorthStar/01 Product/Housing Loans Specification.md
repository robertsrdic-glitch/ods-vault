# Housing Loans Specification

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
- [[Design Bible]]

---

## 1. Purpose

Stanovanjski kredit helps users understand housing-loan concepts and the monthly-payment implications of a housing loan before making one of the biggest financial decisions of their lives.

NorthStar educates. NorthStar explains. NorthStar does not recommend banks or financial products, and does not sell.

The final decision always belongs to the user.

---

## 2. Product Role

Stanovanjski kredit is one of NorthStar's four standalone first-phase products (DR-013).

The first public MVP release contains Stanovanjski kredit as a limited initial version, per DR-015.

For the full first-phase product structure, see [[Decision Register]]. For current release scope, see [[MVP]]. For the product and feature catalog, see [[Features]].

---

## 3. User Goal

Users should be able to better understand, at an educational level:

- how housing loans work;
- fixed versus variable interest;
- interest rate, effective cost, down payment, repayment period, early repayment, and refinancing;
- how loan amount, interest rate, and repayment period affect an illustrative monthly payment;
- what questions and assumptions matter before they continue toward a decision.

This document does not presume an uploaded offer, paragraph-by-paragraph document interpretation, live AI conversation, offer comparison, or personalized analysis — see [Section 5](#5-explicitly-excluded-from-the-first-public-mvp).

---

## 4. Confirmed First Public MVP Scope

The confirmed scope of Stanovanjski kredit in the first public MVP release is defined by DR-015 and approved [[MVP]].

### 4.1 Learn

Short, structured, plain-language educational content covering:

- the housing-loan process;
- fixed vs. variable interest;
- interest rate and effective cost;
- down payment;
- repayment period (loan duration);
- early repayment;
- refinancing.

This is not a complete curriculum specification, and it does not include legal or regulatory claims.

### 4.2 Monthly Payment Examples

Simple educational examples illustrating the relationship between loan amount, interest rate, repayment period, and an approximate monthly payment.

Trust boundaries:

- educational and approximate;
- not a banking calculator;
- not a bank calculation;
- not a bank offer;
- not a guarantee;
- not personal financial advice;
- assumptions must be visible to the user.

This document does not define a formula, thresholds, amortization rules, or implementation details for these examples.

### 4.3 Links to Other Standalone Products

Stanovanjski kredit links to two other standalone NorthStar products:

- **Koliko kredita si lahko privoščim**
- **Pojasni pojme**

Affordability is a shared capability supporting the standalone product Koliko kredita si lahko privoščim. Financial Terms is a shared capability supporting the standalone product Pojasni pojme. Stanovanjski kredit does not duplicate either capability — it links to both standalone products instead. This reuse does not reduce the standalone status of either product (DR-011, DR-012, DR-013, DR-015).

The detailed behavior of Koliko kredita si lahko privoščim and Pojasni pojme is not defined in this document.

---

## 5. Explicitly Excluded from the First Public MVP

The following are excluded from the current release of Stanovanjski kredit (DR-015):

- Ask AI;
- PDF Offer Explanation / bank PDF analysis;
- offer comparison;
- personalized learning;
- bank-meeting preparation;
- advanced simulations;
- user accounts;
- saved history.

These are current release exclusions, not permanent product non-goals. None of them is confirmed for a later release; any future inclusion requires a new Founder-approved decision (see [Section 10](#10-future-scope-and-document-boundaries)).

---

## 6. User Experience Principles

The experience should feel:

- calm;
- clear;
- educational;
- transparent;
- non-judgmental;
- free of hidden persuasion;
- free of false precision;
- open about its assumptions and limitations;
- understandable without specialist financial knowledge.

---

## 7. High-Level User Experience

1. User enters Stanovanjski kredit.
2. User chooses to view Learn content or a Monthly Payment Example.
3. User receives clear educational content or an approximate example, with assumptions shown.
4. User can continue to Koliko kredita si lahko privoščim or Pojasni pojme.
5. User leaves with better understanding and clearer questions.

This is a high-level description, not a screen-by-screen flow. It does not include document upload, document processing, document analysis, live AI, or offer-specific interpretation.

---

## 8. Trust and Product Boundaries

- NorthStar is not a bank, lender, broker, or financial adviser.
- Content is educational.
- Estimates are not bank offers and not official creditworthiness assessments.
- Stanovanjski kredit does not predict bank approval.
- The final decision always belongs to the user.
- Uncertainty must not be presented as certainty.

---

## 9. Success Criteria

- Users understand key housing-loan concepts more clearly.
- Users understand the assumptions behind the examples shown to them.
- Users can identify useful questions to ask before speaking to a bank or adviser.
- Users recognize the limits of educational examples.
- The experience produces understanding rather than pressure.

---

## 10. Future Scope and Document Boundaries

This document does not enumerate future candidate features. Future candidates and unresolved historical scope are tracked in [[Features]]. Current release scope is owned by [[MVP]]. Approved decisions and their supersession history are owned by [[Decision Register]].

Future inclusion of any currently excluded item requires a new Founder-approved decision.

---

## 11. Related Documents

- [[NorthStar Constitution]]
- [[NorthStar OS Specification]]
- [[Product Bible]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
- [[Design Bible]]
