# User Flow Specification

Version: 1.0
Status: Draft
Category: Product
Owner: Founder
Related Documents:
- [[NorthStar Constitution]]
- [[NorthStar Brand DNA]]
- [[Product Bible]]
- [[Design Bible]]
- [[Housing Loans Specification]]
- [[User Journey Specification]]

---

# 1. Goal

Define the complete primary "happy path" for NorthStar: a user uploads a housing loan PDF and leaves understanding their offer with confidence. This document describes behaviour only. It does not describe screens, layouts, or UI elements.

---

# 2. User

A person who has received, or is considering, a housing loan offer and wants to understand it before deciding. No assumption is made about their financial literacy — the flow must work for a first-time buyer and an experienced borrower alike.

---

# 3. Preconditions

- The user has a housing loan offer available as a PDF.
- The user has reached the Housing Loans module (entry path is out of scope here).
- No account, authentication, or profile setup is required for this flow.

---

# 4. User Journey

---

## Step 1 — Entry

**User Goal:** Find out whether NorthStar can help them understand their loan offer.

**User Action:** Arrives at the Housing Loans module.

**System Response:** Presents the option to upload a document for explanation, alongside other ways to engage (learning content, asking a question directly).

**AI Behaviour:** None yet — no analysis has started. AI presence is available but not intrusive.

**Success Criteria:** The user understands they can upload their loan offer and what will happen if they do.

---

## Step 2 — Upload

**User Goal:** Get their specific offer analysed, not a generic explanation.

**User Action:** Uploads the housing loan PDF.

**System Response:** Confirms the document was received and that analysis is starting.

**AI Behaviour:** Begins reading the document. No claims are made about the outcome yet.

**Success Criteria:** The user has a clear, immediate signal that their document was received and something is happening.

---

## Step 3 — Analysis

**User Goal:** Trust that the analysis is thorough and accurate before seeing results.

**User Action:** Waits.

**System Response:** Communicates that NorthStar is analysing the offer, per the Trust Engine Specification's rule to reduce uncertainty during processing rather than leaving the user guessing.

**AI Behaviour:** Extracts financial terminology, important clauses, obligations, costs, fees, and risks from the document, per the Housing Loans Specification's PDF Offer Explanation feature. Distinguishes what it can determine with confidence from what is unclear, per Trust Engine Specification's rule to never invent missing information.

**Success Criteria:** The user is not left wondering whether anything is happening, and understands roughly what NorthStar is doing during the wait.

---

## Step 4 — Explanation

**User Goal:** Understand what the offer actually says, in plain language.

**User Action:** Reviews the explanation NorthStar provides.

**System Response:** Presents the explanation following the AI Response Specification's standard structure: a short direct answer, why it matters, a practical example where useful, things to watch (risks and common misunderstandings), and a suggested next step.

**AI Behaviour:** Explains terminology, clauses, obligations, costs, fees, and risks. Never tells the user which offer to choose or whether to accept it — the Housing Loans Specification is explicit that NorthStar never makes this decision for the user. States uncertainty clearly wherever the document is ambiguous, rather than guessing.

**Success Criteria:** The user can, in their own words, describe what the offer means and what it will cost them.

---

## Step 5 — Exploration

**User Goal:** Go deeper on anything that's unclear or concerning, at their own pace.

**User Action:** Asks follow-up questions, requests clarification on specific terms, or asks how this offer compares to what they should expect.

**System Response:** Follows the AI Conversation Specification's flow: understand the question, explain, verify understanding, then offer further help. Never rushes the user toward a conclusion.

**AI Behaviour:** Answers using the same standard response structure as Step 4. Presents trade-offs neutrally when multiple interpretations or options exist, per the AI Response Specification's rule to remain neutral in comparisons. Adapts depth to the user's demonstrated familiarity, per the AI Conversation Specification's adaptive communication principle.

**Success Criteria:** The user's specific concerns or questions about the offer have been addressed, not just the generic explanation.

---

## Step 6 — Resolution

**User Goal:** Leave with enough understanding to make their own informed decision, elsewhere and in their own time.

**User Action:** Ends the session, or moves on to another module (e.g. Affordability, Financial Terms).

**System Response:** Suggests a next logical step if relevant (per the Universal User Journey's "Continue" step) without forcing it. The final decision is left entirely to the user.

**AI Behaviour:** Does not push toward closure or urgency. Confirms understanding was reached rather than celebrating the interaction itself, per Design Bible's Success States principle.

**Success Criteria:** The user leaves able to explain their offer to someone else, and feels informed rather than persuaded.

---

# 5. Decision Points

- **After upload:** does the document contain enough extractable information to proceed, or does NorthStar need to explain a limitation (see Error States)?
- **After the initial explanation:** does the user want more detail (Step 5) or do they have what they need (Step 6)?
- **At resolution:** does the user want to continue into an adjacent module (Affordability, Financial Terms) or end the session?

None of these decision points are made by NorthStar on the user's behalf — each one is the user choosing their own next action.

---

# 6. Error States

Major failure modes only.

- **Unreadable or corrupted PDF:** NorthStar states plainly that the document could not be read and asks the user to try again, rather than guessing at its contents.
- **Document is not a housing loan offer:** NorthStar says so directly and does not attempt to force an explanation onto the wrong document type.
- **Analysis produces low-confidence results:** per Trust Engine Specification's "Unknown Information" rule, NorthStar states what is known, states what is uncertain, and suggests a reliable next step (e.g. asking the bank directly) — it never fills the gap with an invented answer.

---

# 7. Trust Opportunities

- Communicating what NorthStar is doing during analysis, rather than a silent wait (Step 3).
- Distinguishing confirmed facts from assumptions at every explanation point (Steps 3–5).
- Never recommending a decision, only explaining options and trade-offs neutrally (Steps 4–5).
- Naming uncertainty explicitly instead of projecting false confidence (Steps 3, 6, Error States).
- Ending the flow without pressure toward any particular outcome (Step 6).

---

# 8. UX Principles Applied

- **Understanding Builds Trust** (Design Bible, Design Philosophy) — every step is structured to build understanding first; trust is the resulting state, not a separate thing to be engineered directly.
- **Progressive Disclosure** (Design Bible) — the standard response structure in Steps 4–5 leads with a short answer and lets the user go deeper only if they choose to.
- **Calm Interfaces** (Design Bible) — no urgency is introduced anywhere in the flow, including at resolution.
- **AI Interface Principles: Guidance not control** (Design Bible) — the AI recommends understanding, never decisions, throughout.
- **User First** (NorthStar Constitution) — every step is evaluated against whether it helps the user, reduces uncertainty, and increases trust.

---

# 9. Definition of Success

The flow succeeds when the user can explain their housing loan offer in their own words, understands its costs and risks, and leaves the interaction having made no decision they didn't arrive at themselves. Success is measured by understanding achieved, not by engagement time or how impressive the analysis appears.
