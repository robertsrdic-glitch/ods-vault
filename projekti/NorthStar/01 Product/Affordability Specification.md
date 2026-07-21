# Affordability Specification

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
- [[User Journey Specification]]
- [[Housing Loans Specification]]
- [[Design Bible]]

---

## 1. Purpose

Koliko kredita si lahko privoščim helps users understand what monthly credit obligation may be sustainable within their household finances.

It is educational. It helps users reason before approaching a bank or accepting an obligation. It does not determine bank approval, and it does not recommend a lender or product. The final decision always remains with the user (DR-016).

---

## 2. Product Role

Koliko kredita si lahko privoščim is one of NorthStar's four standalone first-phase products (DR-013).

It is one of the two core products of the first public MVP release (DR-014).

Affordability may be reused as a shared capability by other products — first Stanovanjski kredit, later Leasing and future products — but this technical reuse does not reduce the standalone product status of Koliko kredita si lahko privoščim (DR-011, DR-013).

Detailed release scope is owned by [[MVP]]. Approved architecture and decisions are owned by [[Decision Register]] and [[Product Bible]].

---

## 3. User Goal

Users should be able to better understand:

- how much monthly room may remain after living costs and existing obligations;
- how a tested monthly payment affects household resilience;
- when a tested amount appears comfortable, tight, or high risk;
- which assumptions materially affect the result;
- which questions to consider before proceeding.

The product does not tell the user the objectively correct maximum loan. The result is a considered, transparent estimate — not a determination.

---

## 4. Inputs

The following inputs are confirmed by DR-016 and approved [[MVP]] §4.1.

### 4.1 Household monthly net income

The household's relevant recurring monthly net income.

Exact income definitions, eligible income types, and treatment of irregular income are not yet defined in any authoritative source and are not invented here (see [Section 16](#16-open-decisions-before-implementation)).

### 4.2 Household size

Household size is a confirmed input, used to propose safe minimum living costs (DR-016).

No household equivalence scale or country-specific value is invented in this document.

### 4.3 Safe minimum living costs

- NorthStar proposes an initial safe minimum-living-cost amount based on household size.
- The user can adjust this proposed amount.
- The original suggestion and the user's adjustment must both remain understandable to the user.
- The assumptions behind the proposal must remain visible.
- The proposed value is educational. It is not presented as an official legal, bank, or regulatory minimum, and must not be presented as an unquestionable fact (DR-016).

The concrete numeric values and the methodology behind them are not defined in this document — see [Section 16](#16-open-decisions-before-implementation).

### 4.4 Existing monthly obligations

Confirmed to include, at minimum (DR-016):

- existing loan instalments;
- leasing instalments;
- relevant monthly card or credit-limit burdens;
- alimony or maintenance payments;
- other contractual monthly debts or obligations.

This list must not be silently narrowed to bank loans only. A recommended user-facing label for this input group is: "Existing loans, leasing, and other regular monthly obligations."

These obligations reduce the household's available monthly capacity.

### 4.5 Desired or maximum loan term

A confirmed input (DR-016): the user's desired or maximum loan repayment period.

### 4.6 Indicative interest rate

A confirmed input (DR-016): an indicative interest rate, or a clearly displayed default educational example where the user does not provide one.

### 4.7 Tested monthly amount

The user may test a proposed monthly credit or financing payment.

This is an exploratory amount for the purpose of understanding, not a bank offer, and not a submitted application.

### 4.8 Unresolved or additional inputs

The following are not confirmed as first-public-MVP inputs by any authoritative source and are not added here:

- regular essential expenses beyond the safe-minimum-living-cost proposal;
- a savings buffer;
- number or age of dependants beyond household size;
- income volatility or irregularity factors beyond what household income already covers.

Any of these would require a separate Founder-approved decision before being added as confirmed scope (see [Section 16](#16-open-decisions-before-implementation)).

---

## 5. Core Calculation Model — Conceptual Only

The result conceptually relates:

- household monthly net income;
- safe minimum living costs (proposed and/or user-adjusted);
- existing monthly obligations;
- the tested monthly amount;
- the remaining monthly buffer.

The safe monthly-payment range and the indicative loan-value range are both derived from this same conceptual relationship. The loan-value range additionally relates the safe monthly-payment range to the desired or maximum loan term and the indicative interest rate or disclosed default educational example, so that a possible loan value can be shown as a range alongside the payment range.

The exact formula, rounding rules, frequency conversion, treatment of irregular income, and handling of missing values are not defined in this document and require separate approval before implementation (DR-016, MVP.md §8).

The result is an educational affordability view. It is not an underwriting outcome, and it is not a formal calculation performed on behalf of a bank.

No code, equation, numeric threshold, or bank-specific debt-service formula is included in this document.

---

## 6. Result and Interpretation

The user should receive:

- an understandable summary;
- the tested monthly amount;
- an indicative loan-value range;
- the remaining monthly room or buffer;
- a qualitative interpretation: bolj varno (more safe) / napeto (tight) / previsoko tveganje (too high risk) (DR-016);
- the key assumptions behind the result;
- useful next questions to consider.

The indicative loan-value range is educational, depends on the disclosed loan term, interest-rate assumption, and unresolved calculation methodology, and must be presented as a range rather than a single amount. It is not a loan offer, bank approval, or guaranteed borrowing amount.

The result is a range; a single falsely precise amount is not permitted as the main result (DR-016).

Absolute or unqualified language such as "approved," "safe for everyone," or "you can afford this" must not be used.

---

## 7. Mandatory Visualization

DR-016 requires two mandatory visual elements, together forming the required visualization of the result. Neither is a new methodology or a separate calculation — both visually present the same confirmed result described in [Section 6](#6-result-and-interpretation).

### 7.1 Safe-range graph

Must show, at minimum:

- the safe range of the monthly payment;
- the user's selected or tested monthly payment;
- the boundary or zone where the result becomes tight;
- the zone of excessive risk.

The user must be able to immediately understand where their tested payment falls. The visualization must clearly distinguish between bolj varno / napeto / previsoko tveganje, and must not create an impression of mathematical or banking certainty (DR-016).

### 7.2 Monthly money allocation

A second mandatory visual element, or a further part of the same result display, showing:

- household monthly net income;
- living costs;
- existing loans, leasing, and other obligations;
- the proposed new monthly payment;
- the remaining amount or safety reserve.

### 7.3 Shared visualization principles

- The visualization must stay very simple: no complex curves, financial jargon, or excessive data.
- Its purpose is understanding, not decoration.
- It must be understandable to a user without financial knowledge.
- Accessibility must not depend on color alone.
- No final chart type, colors, dimensions, thresholds, or interactions are decided in this document — these require a separate UX and methodological specification (DR-016).

---

## 8. Affordability Ratio

DR-016 confirms the affordability ratio as a required educational output.

At the product level, the ratio must:

- support user understanding of their situation, not replace it;
- show the assumptions it relies on;
- never be presented as a universal banking rule;
- never imply approval or rejection;
- never use an invented official threshold.

The exact numerator, denominator, and any interpretation bands are not yet formally decided by any authoritative source and are marked as an unresolved decision rather than guessed.

---

## 9. Bank Stress-Test Reference

DR-016 confirms the bank stress-test reference as a required educational output.

At the product level, this reference must:

- help users understand that banks may test affordability under less favorable conditions than the ones NorthStar illustrates;
- never be presented as NorthStar performing an official bank assessment;
- never be presented as a guarantee of approval or rejection;
- acknowledge that bank methodologies vary between institutions;
- rely only on verified official sources and separate approval for any country-specific methodology or rate uplift — no such rule is hard-coded from memory in this document.

No stress-test percentage, uplift value, or bank rule is invented here.

---

## 10. User Control and Transparency

- The user can review and edit relevant inputs.
- NorthStar-proposed values (e.g. the safe minimum living-cost suggestion) are visibly distinguished from user-entered or user-adjusted values.
- Changing an input updates the educational result.
- Assumptions behind the result remain visible.
- The product explains why an input matters.
- The user is not pressured toward a higher or lower loan amount.
- False precision is avoided throughout.

---

## 11. High-Level User Experience

A safe high-level structure:

1. User enters the standalone product.
2. User provides household and obligation information.
3. NorthStar proposes safe minimum living costs.
4. User reviews or adjusts assumptions.
5. User tests a monthly amount.
6. NorthStar shows the summary, including the indicative loan-value range, the mandatory visualization, the affordability ratio, and the stress-test reference.
7. User can revise assumptions or conclude with clearer questions.

This sequence may be adapted during design and does not define final screens.

This document does not introduce account creation, saved history, Ask AI, PDF upload, or lender offers.

---

## 12. Trust and Product Boundaries

- NorthStar is not a bank, lender, broker, or financial adviser.
- This is educational, not personal financial advice.
- There is no bank-approval prediction.
- There is no official creditworthiness assessment.
- There is no guarantee that a payment is sustainable.
- There is no guarantee that a bank will accept the application.
- Proposed living costs are not official minimums.
- Estimates and zones depend on stated assumptions.
- Uncertainty must remain visible.
- The user remains responsible for the final decision.
- The used interest rate, term, costs, obligations, and safety reserve must be disclosed (DR-016).

---

## 13. Explicitly Excluded from the First Public MVP

Confirmed exclusions (DR-016):

- connecting to banks;
- actual verification of creditworthiness;
- automatic import of bank data;
- user accounts;
- saving calculations;
- Ask AI / AI chat;
- recommending a specific bank or loan;
- prediction of approval.

These are current-release exclusions. They are not framed as permanent product non-goals, and none of them is confirmed for a future release without a new Founder-approved decision.

---

## 14. Edge Cases and Error Principles

Without inventing final handling rules, the product must account for the following situations:

- incomplete inputs;
- zero or negative values;
- obligations greater than income;
- unusually high or low user-adjusted living costs;
- inconsistent frequencies (e.g. weekly vs. monthly figures);
- uncertain or irregular income;
- inability to calculate a meaningful result.

Principles:

- the product must not fabricate a result;
- invalid or uncertain inputs must be explained to the user, not silently guessed;
- the user should be told what needs correction;
- high-risk situations must be communicated calmly and clearly, without alarm;
- exact validation and calculation rules remain an implementation decision requiring separate approval.

---

## 15. Success Criteria

- Users understand which inputs drive affordability.
- Users understand the difference between income, obligations, living costs, tested payment, and remaining buffer.
- Users understand the result is educational.
- Users can interpret the visualization without relying on color alone.
- Users understand the affordability ratio and stress-test reference at a basic level.
- Users understand the difference between the safe monthly-payment range and the indicative loan-value range, and that the loan-value range depends on the stated term and interest-rate assumptions.
- Users can identify useful questions before speaking to a bank or adviser.
- Users do not feel pressured or falsely reassured.

No numeric KPIs are defined in this document.

---

## 16. Open Decisions Before Implementation

First-pass design may proceed using clearly labeled placeholder or demonstration values. Final content-ready and implementation-ready design require the methodology decisions below.

| # | Decision | Why it matters | Blocks first-pass design? | Blocks final content-ready design? | Blocks implementation? | Who must approve |
|---|---|---|---|---|---|---|
| 1 | Exact calculation formula for the safe monthly-payment range and the indicative loan-value range | Determines what the result actually represents | No | Yes | Yes | Founder, via a separate methodology specification |
| 2 | Concrete safety thresholds (what counts as bolj varno / napeto / previsoko tveganje) | Directly drives the visualization and the qualitative result | No | Yes | Yes | Founder |
| 3 | Slovenia-specific safe minimum living-cost values, methodology, verified sources, and maintenance process | Needed to make the household-size proposal real, defensible, and correctly localized | No | Yes | Yes | Founder, with verified local/official sources |
| 4 | Household-size methodology (equivalence scale, treatment of children/dependants) | Affects the living-cost proposal's fairness and accuracy | No | Yes | Yes | Founder |
| 5 | Affordability-ratio numerator, denominator, and interpretation bands | The ratio is confirmed as required (DR-016) but has no defined content yet | No | Yes | Yes | Founder |
| 6 | Bank stress-test source, representation, and any rate uplift | The reference is confirmed as required (DR-016) but has no defined methodology yet; must come from verified official sources | No | Yes | Yes | Founder, with verified official sources |
| 7 | Frequency conversions (e.g. weekly/annual to monthly) | Needed for consistent calculation | No | No | Yes | Founder or delegated technical owner |
| 8 | Rounding rules | Affects displayed figures and perceived precision | No | No | Yes | Founder or delegated technical owner |
| 9 | Handling of negative or missing values | Needed for a robust, non-fabricating product | No — placeholder error states are sufficient | No | Yes | Founder or delegated technical owner |
| 10 | Whether the MVP input/output model expands beyond DR-016 to include additional expenses or a separate savings-buffer concept | Current DR-016 scope remains unchanged unless the Founder expands it | No | No | Only if the Founder chooses to expand scope | Founder |
| 11 | Slovenia-specific content validation and last-reviewed-date requirements for any published figures | Needed for trust and content governance | No | Yes | Yes | Founder / content owner |
| 12 | Accessibility requirements beyond "not color alone" | Detailed accessibility spec not yet written | No | Yes | Yes | Founder, with Design owner recommendation |
| 13 | Validation and test data for the eventual calculation model | Needed before implementation can be verified | No | No | Yes | Founder or delegated technical owner |

---

## 17. Document Boundaries

- [[Decision Register]] owns approved decisions and their supersession history.
- [[MVP]] owns current release scope.
- [[Features]] owns the product and feature catalog.
- [[Product Bible]] owns durable architecture and philosophy.
- [[User Journey Specification]] owns the cross-product journey framework.
- [[Design Bible]] owns visual and interaction principles.
- This specification owns product-level behavior and trust boundaries for Koliko kredita si lahko privoščim.

---

## 18. Related Documents

- [[NorthStar Constitution]]
- [[NorthStar OS Specification]]
- [[Product Bible]]
- [[Decision Register]]
- [[MVP]]
- [[Features]]
- [[User Journey Specification]]
- [[Housing Loans Specification]]
- [[Design Bible]]
