# Constitution Amendment 001

Version: 1.0
Status: Draft
Category: Foundation
Owner: Founder
Related Documents:
- [[NorthStar Constitution]]
- [[NorthStar Brand DNA]]
- [[Design Bible]]
- [[Design Foundation Specification]]
- [[Trust Engine Specification]]
- [[NorthStar Design Context Pack]]

---

# Status of This Document

This is a proposal only. It has not been approved and does not change anything. The NorthStar Constitution has not been modified. Only the Founder can approve, reject, or modify this proposal.

---

# 1. Description of the Conflict

The Constitution's "Decision Priority" section ranks: 1. Trust, 2. User Understanding, 3. Independence, 4. Simplicity, 5. Long-Term Sustainability, 6. Growth.

Two design-tier documents rank the same two values in the reverse order. Design Bible's "Design Philosophy" states Understanding is "one principle above all others." Design Foundation Specification's "Design Priorities" lists an explicit ranking: 1. Understanding, 2. Trust. This is a genuine ordering conflict between the Constitution and the documents that govern day-to-day design decisions.

---

# 2. Evidence from Existing Documentation

This section was independently verified against the five documents named in the originating task, not taken at face value.

**Direct, explicit evidence of Understanding-before-Trust:**

- Design Bible, "Design Philosophy": "NorthStar follows one principle above all others: Understanding First... should reduce uncertainty. Never increase it."
- Design Foundation Specification, "Design Priorities": explicit ranked list — "1. Understanding, 2. Trust, 3. Clarity, 4. Consistency, 5. Accessibility, 6. Beauty."

**Documents cited in the originating task that do not actually support this claim, on inspection:**

- NorthStar Brand DNA's "Design Philosophy" states "Understanding comes before aesthetics. Clarity comes before density. Consistency comes before creativity." None of these three comparisons involve Trust. Brand DNA never ranks Understanding against Trust anywhere in the document. It should not be treated as evidence for this conflict.
- Trust Engine Specification opens with "Trust is the primary product feature of NorthStar" and closes with "Trust is NorthStar's competitive advantage. Every product decision should strengthen it." This reads as Trust-primary framing, not Understanding-primary. The document does list understanding-generating behaviours (explain reasoning, acknowledge uncertainty, distinguish facts from assumptions) as the mechanism for earning trust, but it never states that Understanding outranks Trust — the framing is arguably closer to the Constitution's model than the Design Bible's. It should not be cited as supporting evidence for this amendment.
- NorthStar Design Context Pack (generated earlier this session) explicitly reported this exact conflict as unresolved rather than adopting a position. Citing it as evidence "for" Understanding-first misrepresents what it says.

**Net assessment:** only two of the five documents named in the originating task provide genuine, explicit Understanding-first evidence. The conflict is real, but narrower than originally described — it exists between the Constitution and specifically Design Bible plus Design Foundation Specification, not across the whole design documentation set.

---

# 3. Architectural Analysis

Two distinct, internally coherent causal models are in play — this is not a documentation typo, it is two different theories of how trust is generated:

**Model A — Trust-primary (Constitution's current model):** users first need to trust NorthStar enough to engage with it; understanding follows as trust is established through consistent, honest behaviour over time.

**Model B — Understanding-primary (Design Bible / Design Foundation Specification's model):** users trust NorthStar because they understand what it is telling them and why; understanding is the mechanism, trust is the resulting state.

The Constitution's own "Living Constitution" clause anticipates exactly this kind of question: "If experience clearly shows that a principle should evolve, the Founder may approve revisions." This is a legitimate product-strategy decision, not an error to be silently corrected.

---

# 4. Risks of Keeping the Constitution Unchanged

- Design Bible and Design Foundation Specification already contradict the Constitution's stated order. Per Design Foundation Specification's own "Primary Design Inputs" hierarchy, the Constitution outranks both documents — meaning, on paper, two documents meant to operationalize the Constitution are currently non-compliant with it.
- Day-to-day design decisions are likely already being made under the Understanding-first assumption embedded in those two documents, widening the gap between stated governance and actual practice the longer it goes unresolved.
- The same conflict will likely resurface in every future audit or generated context pack that touches both documents, repeatedly consuming review time instead of being settled once.

---

# 5. Benefits of Changing the Priority Order

- Would align the Constitution with the two documents that most directly drive daily design decisions, removing friction for whoever executes design work.
- "Understanding creates Trust" is arguably the more internally consistent causal story for a product whose founding Preamble already states its purpose as "understanding, not persuasion" rather than trust-building for its own sake.
- Would prevent this conflict from recurring in future audits or generated documents.

---

# 6. Recommendation

This document does not recommend a side. Both models are defensible, and the underlying question — whether trust or understanding should win when the two genuinely trade off — has not yet been tested against a real product decision. Per the vault's own Collaboration Rules ("if multiple valid interpretations exist, stop, ask the Founder, never guess"), that call belongs to the Founder.

What this document does recommend: resolve the ambiguity in one direction or the other. Leaving it unresolved is worse than either resolution, since it currently allows two tiers of governing documentation to quietly disagree.

---

# 7. Proposed New Wording

If the Founder adopts the Understanding-first model, the Constitution's "Decision Priority" section could read:

1. User Understanding
2. Trust
3. Independence
4. Simplicity
5. Long-Term Sustainability
6. Growth

with an optional clarifying line: "Trust is earned by first ensuring users understand; understanding is the mechanism, trust is the outcome."

If the Founder instead keeps Trust first, the correction would run the other direction — amending Design Bible and Design Foundation Specification to match the Constitution. This document does not modify either, since only the Founder can direct which side changes.

---

# 8. Backward Compatibility Assessment

- Verified vault-wide: no document other than the Constitution itself references "Decision Priority" by name or cites its 1–6 ordering. Decision Log, Housing Loans Specification, User Journey Specification, Trust Engine Specification, AI Response Specification, and AI Conversation Specification make no reference to it. A reorder would not break any existing cross-reference.
- If Understanding-first is adopted: Design Bible and Design Foundation Specification would become consistent with the Constitution rather than requiring changes themselves. NorthStar Design Context Pack's existing "Design Philosophy" section already reflects Understanding-first framing and would need no change.
- If Trust-first is kept instead: Design Bible and Design Foundation Specification would need separate amendment proposals of their own — out of scope for this document.

---

# Decision

Not approved. Not rejected. Awaiting Founder review.
