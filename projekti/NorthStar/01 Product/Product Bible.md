 # Product Bible

Status: Draft

Version: 0.1

Started: 13.07.2026

Founder:
Robert Srdič Šenčar

Project:
NorthStar

Development Status:
Active Development

---

## 1. Product Identity

NorthStar is an independent AI-supported platform that helps people understand important financial decisions before they commit to them.

NorthStar is not a bank, not a broker, not a lender, and not a financial adviser. It does not make decisions on a user's behalf — it helps the user understand their own situation clearly enough to decide for themselves.

---

## 2. Purpose and Promise

NorthStar exists to replace complexity with understanding, not to persuade.

Financial decisions affect people's lives, and clarity is what allows someone to face one with confidence rather than pressure.

NorthStar's promise: it helps people understand before they decide. The final decision always belongs to the user.

---

## 3. Who NorthStar Is For

NorthStar is for people who are making, or preparing to make, an important financial decision, and who want clarity before committing to it.

This includes people who may not have specialist financial knowledge, and who want the assumptions, risks, and trade-offs behind a decision explained in plain language rather than jargon.

No specific age group, income level, employment category, buyer persona, or demographic segment is defined for NorthStar. The audience is described by the situation a person is in, not by who they are.

---

## 4. The Problem NorthStar Solves

Important financial decisions are often complex. The language used, the assumptions behind an offer, and the risks and trade-offs involved can be difficult for someone without specialist knowledge to evaluate on their own.

People can end up committing to a financial decision without fully understanding what they are agreeing to, what it will cost them, or what could go wrong. Complexity, jargon, and sales pressure all work against informed decision-making.

NorthStar exists to reduce that gap between what a person is asked to decide and what they actually understand about the decision.

---

## 5. Desired User Outcomes

Success for NorthStar is a user who, after using it, thinks:

> "Končno razumem."
>
> "Zaradi tega sem se izognil dragi napaki."

Translated into stable outcome principles, NorthStar aims to give users:

- greater understanding of their own financial situation and the decision in front of them;
- better questions to ask before they commit;
- a clearer awareness of the assumptions and risks behind any estimate or explanation they are given;
- more confident, more independent decisions.

NorthStar does not claim or guarantee any specific saving, or that using it will always prevent a costly mistake. It aims to improve understanding, not to promise an outcome.

---

## 6. Trust Principles

NorthStar is governed by a small set of durable trust principles:

- **Trust before Profit** — no element of the product should function as sales or monetization pressure at the expense of user trust.
- **Clarity before Complexity** — every result, explanation, or visualization should be understandable without financial expertise.
- **Education before Recommendation** — NorthStar explains and estimates; it does not recommend specific banks, lenders, or financial products.
- **Privacy First** — user data is handled with restraint by default; see [Privacy Principle](#12-privacy-principle).
- **Independence** — NorthStar optimizes for the user's understanding, not for a sale.
- **Transparent assumptions** — whenever NorthStar produces an estimate or explanation, the assumptions behind it are shown, not hidden.
- **No hidden persuasion** — NorthStar does not use pressure, urgency, or manipulation to move a user toward a particular choice.

---

## 7. What Makes NorthStar Different

NorthStar is built around a small number of principle-level distinctions:

- it aims for understanding rather than persuasion;
- it offers independent explanation rather than selling a product;
- it prefers plain language over unnecessary financial jargon;
- it presents ranges and transparent assumptions rather than false precision;
- where AI assists with sensitive financial content, human or editorial judgment remains in control of what is ultimately published or presented as authoritative.

This section intentionally does not compare NorthStar to named competitors, and makes no "only," "best," or market-leading claims. Any such claims would require separate Founder-approved substantiation.

---

## 8. First-Phase Product Structure

NorthStar's first phase is built around four standalone products (DR-013):

1. Stanovanjski kredit
2. Leasing
3. Koliko kredita si lahko privoščim
4. Pojasni pojme

Each of these is a standalone, user-facing product with its own primary entry point and its own user purpose.

Separately, some products are supported in the background by a shared technical or content capability — for example, Affordability supports Koliko kredita si lahko privoščim, and Financial Terms supports Pojasni pojme, and either capability may in time also be reused by other products. A shared capability is a technical/architectural fact; it does not reduce the standalone product status of Koliko kredita si lahko privoščim or Pojasni pojme, or of any other product that draws on it (DR-011, DR-012, DR-013).

For the current feature-level detail of each product, see [[Features]].

---

## 9. Release Philosophy

NorthStar's first phase is broader than any single release. Products may enter the first phase across multiple releases rather than all at once (DR-014).

Being visible on the first screen does not necessarily mean a product is fully active in the current release — a product can be present and clearly signposted as coming later, without being removed from the first phase.

Release scope is deliberately kept limited at each stage, in order to protect trust, clarity, and quality rather than to maximize the number of features shipped at once.

For the current public release's exact scope, see [[MVP]] and [[Decision Register]].

---

## 10. AI Role and Human Control

AI is used within NorthStar to assist, not to decide.

AI may assist with research, drafting, simplification of explanations, preparation of examples, and identifying possible local or contextual differences that need human attention.

AI output is not automatically treated as authoritative. AI does not independently validate legal or financial correctness, and it does not automatically publish curated financial content — editorial review and approval remain required wherever they are defined for a given type of content.

This follows the Constitution's principle that AI proposes and the Founder, or another authorized human decision-maker, decides. AI supports a user's understanding; it does not replace human judgment, and it does not make the user's decision for them.

---

## 11. Localization Philosophy

NorthStar's content is organized by country, and a new country is never added simply by translating an existing one.

Legal, regulatory, tax, banking, and consumer context can all differ by country, so each country requires its own local research and validation before its content can be trusted.

The product's architecture is designed to support future countries over time, but that architectural readiness does not by itself place any additional country inside the current MVP scope.

Slovenia is the country supported by the first public MVP release — this reflects where NorthStar starts, not a permanent geographic limit on the product. No country expansion roadmap or timeline is defined here; see [[Decision Register]] (DR-017) for the current approved country-content model.

---

## 12. Privacy Principle

Users should remain in control of their own information.

NorthStar's default approach is to minimize what data it collects and retains, and to design for privacy from the outset rather than add it afterward.

Any product claim about privacy must not exceed what is actually implemented and documented in NorthStar's technical architecture.

This document does not state retention periods, encryption guarantees, third-party data-sharing policies, hosting arrangements, regulatory compliance guarantees, or any other specific technical security control — those belong to a separate, dedicated privacy and engineering specification.

---

## 13. Product Boundaries

NorthStar operates within durable boundaries that hold regardless of release:

- NorthStar is not a bank.
- NorthStar is not a lender or a broker.
- Nothing NorthStar provides is personal financial advice.
- NorthStar does not make decisions for users — the final decision always belongs to the user.
- Educational estimates NorthStar produces are not bank offers and not official creditworthiness assessments.
- NorthStar must not present uncertainty as certainty.
- NorthStar must not use pressure, manipulation, or hidden persuasion to influence a user's choice.

Specific feature-level exclusions for the current release (such as which features are not yet available) are release-scoped decisions, not durable product boundaries, and are defined in [[MVP]] and [[Features]] rather than here.

---

## 14. Document Authority and Related Documents

Product Bible is the stable, high-level statement of NorthStar's product identity and strategy. It does not own detailed decisions, release scope, feature status, design specification, or technical implementation — those are owned elsewhere:

- [[NorthStar Constitution]] owns durable organizational principles and governance.
- [[Decision Register]] owns approved product decisions and their supersession history.
- [[MVP]] owns the scope of the current public release.
- [[Features]] owns the product and feature catalog.
- [[Housing Loans Specification]] and other per-product specifications own detailed product behavior.
- [[Design Bible]] owns interaction and visual design direction.
- [[Architecture]] owns technical implementation.

Where anything in this document conflicts with a newer Founder-approved decision, the newer approved decision takes precedence.