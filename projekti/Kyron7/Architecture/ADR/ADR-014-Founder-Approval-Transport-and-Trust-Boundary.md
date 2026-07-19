# ADR-014: Founder Approval Transport and Trust Boundary

**Status:** Accepted
**Date:** 2026-07-19
**Approved:** 2026-07-19 (Founder)

## 1. Context and Current Blocker

Operationalization work package OP-02 (Founder Console Adapter, per `OP-00-Operationalization-Plan.md`) requires a real, live implementation of `FounderConsolePort` — the boundary through which the Deployment Agent raises a high-risk candidate for Founder approval and receives the decision back. Attempting to design that adapter surfaced a blocker with two independent, sufficient parts:

1. **No transport exists to implement against.** ADR-002 names the intended host (`founder.kyron7.com`, Cloudflare Access-protected) but no approved document — not the Architecture Specification, not the Policy Engine Specification, not the Execution Engine Specification, not ADR-002 itself — defines an API, webhook, polling protocol, request/response schema, or any other integration detail for it. There is nothing concrete to build a client against without inventing that contract unilaterally.
2. **ADR-002's own language is ambiguous about what a compliant adapter may do.** ADR-002's Consequences state: "Founder approval becomes independent of MCP and of AI agents — no AI agent surface exposes or consumes the approval mechanism." This is restated verbatim in `founder-console-integration/README.md`, and paraphrased identically in the Deployment Policy Engine Specification and Deployment Execution Engine Specification ("No AI agent may expose or consume the high-risk approval mechanism"). None of these four restatements defines "AI agent" precisely enough to determine whether a deterministic, non-decision-making software client — authored with AI coding assistance but containing no LLM reasoning at runtime — is itself forbidden from communicating with the Founder Console at all, or only forbidden from performing the parts of that mechanism ADR-002's own Context is actually protecting (identity verification, decision capture, allowlist enforcement).

This ADR does not implement OP-02. It resolves the ambiguity so OP-02 (or a corrected version of it) can proceed once accepted.

## 2. The Exact Ambiguity in ADR-002

ADR-002's Context (the Telegram/Hermes problem it was written to solve) describes a *specific* failure mode: Hermes, an AI agent, sat in the middle of the approval channel, receiving a Telegram message and relaying the Founder's reply back into the system — an AI agent was structurally part of how a human's decision reached the system, and every routine approval consumed Hermes' own reasoning/operating budget for no reason. ADR-002's Decision replaces that channel with a dedicated, Cloudflare Access-authenticated web application. Its Consequences state the resulting property in general terms ("no AI agent surface exposes or consumes the approval mechanism") without specifying:

- **What "AI agent" denotes here.** Does it mean any software whose implementation was produced with AI assistance (which would include the entire Deployment Agent codebase — WP-04 through WP-14 were implemented by Claude Code, per ADR-003's workflow) — or does it mean a runtime system that itself performs autonomous, non-deterministic reasoning (an LLM, an MCP tool surface, a chat agent) as part of handling an individual approval?
- **What "the approval mechanism" denotes.** Does it mean the entire Founder Console system end-to-end, including whatever transport a caller uses to submit a request and receive an already-made decision — or does it mean specifically the identity-verification, decision-presentation, and decision-capture surface a human Founder interacts with (the part Hermes' Telegram relay actually touched)?
- **Whether the already-approved `FounderConsolePort` interaction is itself in scope.** WP-07 (defining `FounderConsolePort`) and WP-09 (the Deployment Agent's `executeHighRiskDeployment`, which calls `submitCandidateForApproval()` and branches on its result) are both **already Implemented and CTO-approved**, with WP-07's own CTO acceptance criteria stating: "Confirmed the Deployment Agent does not expose or consume the approval mechanism itself, and that approval identity verification remains the Founder Console's responsibility, per ADR-002." This is direct evidence that the *Deployment Agent calling `FounderConsolePort` and reading its typed result* was already reviewed against ADR-002 and found compliant. What was never reviewed — because no concrete adapter has existed until OP-02 — is whether a specific *transport mechanism* behind that port would also be compliant.

Read narrowly (any AI-assisted code, or any software touching the mechanism at all, is forbidden), ADR-002 would make `FounderConsolePort` itself unimplementable by this project — a reading inconsistent with WP-07/WP-09's own approval and with the Architecture Specification's requirement that a high-risk deployment "halts and awaits Founder approval through the Founder Console" (§7 step 5), which requires *something* in this codebase to communicate with it. Read too broadly in the other direction, it could be misused to justify building a decision-making or identity-verifying surface inside the Deployment Agent, which ADR-002's Context makes clear is exactly what must not happen. This ADR resolves the ambiguity by drawing the line precisely.

## 3. Decision

**Founder Console and Deployment Agent responsibilities are separated as follows.**

### 3.1 Distinction Between an AI Agent and the Deterministic Deployment Agent Service

For the purposes of ADR-002 and this ADR, **"AI agent"** means a runtime system that performs autonomous, non-deterministic reasoning — an LLM, an MCP tool surface exposing this capability, a chat interface, or an autonomously-acting agent (Claude, ChatGPT, Hermes, or any other) — as part of handling an individual approval request or decision, at the time that request or decision is handled.

**"Deployment Agent"** refers to the deterministic software system already defined by the approved architecture (`DeploymentAgent` class, `FounderConsolePort`, the orchestrator, and any concrete adapter implementing an approved port) — fixed, auditable, testable logic containing no LLM call and no autonomous reasoning at runtime. That this software was *authored* with AI coding assistance (Claude Code, per ADR-003) is a build-time fact about its provenance, not a runtime property of its behavior, and does not make it an "AI agent" under this definition — in the same way a CI/CD pipeline script is not an "AI agent" merely because an AI assistant wrote it.

### 3.2 Components Allowed to Interact With the Approval Mechanism

- **The Founder**, directly, through the Founder Console's own authenticated interface.
- **The Founder Console** itself — the sole owner of identity verification, allowlist enforcement, decision presentation, and decision capture (Section 3.3).
- **The Deployment Agent**, acting strictly as a deterministic machine client of a well-defined transport contract (Section 3.4) — submitting a request, receiving a decision already made by the Founder, and never performing any part of identity verification, decision presentation, or decision capture itself.

### 3.3 Components Explicitly Forbidden From Interacting With the Approval Mechanism

- Any LLM, at any point in the approval path, for any purpose (including summarizing, pre-filtering, or "assisting" a pending request).
- Any MCP tool surface that exposes submission, decision retrieval, or any other part of this mechanism as a callable tool.
- Any AI chat surface (Claude, ChatGPT, Hermes, or any other) invoking or being invoked as part of an individual approval's handling.
- Any autonomous agent making, inferring, or suggesting a decision on the Founder's behalf.
- Any component other than the Founder Console performing identity verification or allowlist enforcement.

### 3.4 Founder Console Responsibilities (exclusive, unchanged from ADR-002)

- Sole authority for Founder identity verification (Cloudflare Access) and allowlist enforcement.
- Sole owner of decision presentation (what the Founder sees) and decision capture (recording what the Founder actually decided).
- Issuing a verifiable, integrity-protected decision record back across the transport contract (Section 3.4 of the companion transport specification), bound to the exact request and candidate it was made against.

### 3.5 Deployment Agent Responsibilities (bounded, new under this ADR)

- Submits an approval request across the transport contract, carrying exactly the fields the transport specification defines — no more, no less.
- Waits, bounded by a finite timeout (Section 3.7), for a decision.
- Verifies the decision's integrity and binding to the exact request/candidate before accepting it (Section 3.9).
- Returns exactly `"approved"` or `"rejected"` — the existing `FounderApprovalDecision` domain type, unchanged — when, and only when, a validly bound, unexpired, unambiguous decision was received.
- **Never creates, infers, defaults, or alters a Founder decision.** Any condition other than a validly received `"approved"` or `"rejected"` — timeout, unavailable service, malformed response, failed integrity verification, expired decision, mismatched binding — is an adapter failure, not a domain decision, and must prevent deployment (Section 3.6).

### 3.6 Fail-Closed Behavior

The default and only permitted behavior on any uncertainty is to prevent deployment. Specifically:

- A timeout produces an adapter failure. It is never converted to `"rejected"` (which would fabricate a Founder decision that was never made) and never to `"approved"` (which would be far worse).
- An unavailable Founder Console, a malformed response, a response that fails integrity verification, an expired decision, or a decision that does not bind to the exact outstanding request all produce an adapter failure by the same rule.
- An adapter failure must propagate as a failure the Deployment Agent's orchestration can distinguish from a genuine `"approved"`/`"rejected"` domain decision — this ADR does not itself define that distinction's exact representation (that is implementation detail for OP-02, following the pattern already established by `GitHubIntegrationAdapterError` in OP-01), but requires that no implementation collapse an adapter failure into either domain decision value.
- There is no "default to approve" path under any circumstance, and no "default to reject after N failures" auto-decision path either — both would fabricate a Founder decision.

### 3.7 Timeout Behavior

Every call across the transport contract operates under a finite, bounded timeout, mirroring the requirement already established for OP-01. This ADR does not fix a specific number (that is implementation detail for OP-02 and the companion transport specification's Interaction Model analysis) but requires: a default, a caller-configurable value, and a defensible maximum, exactly as OP-01 established for `git` invocations. A human Founder's response time is not itself bounded by this ADR; what is bounded is how long a single adapter call may wait before failing closed (Section 3.6). How the Deployment Agent's caller responds to that failure (retry later, re-trigger the whole flow, abandon the deployment) is an operational/scheduling question this ADR does not resolve — see Section 8.

### 3.8 Audit Requirements

Every request submission, every decision received (whether accepted or rejected by this adapter's own integrity/binding checks), and every adapter failure must be recordable through the existing Audit Trail boundary (`AuditTrailPort`, WP-03), consistent with the Architecture Specification's requirement that an audit trail entry exist "for every decision point and action" (§7 step 10). This ADR does not change `AuditTrailPort` or `AuditableAction`'s closed set — recording a new event type for this boundary, if needed, is implementation detail for OP-02, following the same "one entry per distinct architectural event" discipline WP-03's own corrective established, not a new architectural requirement introduced here.

### 3.9 Replay and Stale-Decision Protection

Every approval transaction is bound by a set of **transport-level metadata** — values that exist only for this adapter-to-Founder-Console exchange, generated and checked entirely inside the concrete adapter and Founder Console's own transport handling. None of these are additions to `FounderApprovalDecision`, `FounderApprovalRequest`, `CandidateDeployment`, or any other existing domain contract; they never appear on those types, and no domain contract changes to accommodate them. The transport-level metadata is:

- the request identifier (Section 3.10, unchanged from the original text of this section);
- the candidate identifier (`candidate.id`);
- the candidate artifact reference (`candidate.artifactRef`);
- the request creation timestamp;
- an **approval nonce** — a single-use, cryptographically unpredictable value **generated by the Deployment Agent when the approval request is created** and included in the approval transport request. The Founder Console's decision response must bind this exact value back unchanged. The Deployment Agent verifies the returned nonce matches what it generated, and marks it consumed only after that verification succeeds; a response whose nonce is missing, altered, mismatched, or already marked consumed is rejected outright. The approval nonce is never generated by Founder Console — only echoed back by it.
- the decision timestamp (set by Founder Console when the Founder's decision is captured — the only piece of this metadata Founder Console itself generates, distinct from the approval nonce).

**A valid approval response must satisfy every one of the following, conjunctively:**

1. Request identifier matches the exact request this adapter is currently awaiting a decision for.
2. Candidate identifier (`candidate.id`) matches what was submitted.
3. Candidate artifact reference (`candidate.artifactRef`) matches what was submitted.
4. The request has not expired (current time is before the request's expiry timestamp, Section 1 of the companion transport specification).
5. The approval nonce returned in the response exactly matches the nonce the Deployment Agent generated for this request, has not previously been marked consumed, and is neither missing nor altered — any mismatch, absence, alteration, or prior consumption is rejected outright.
6. The decision timestamp falls within the allowed validity window relative to the request's creation timestamp (neither before creation nor implausibly far in the future).

**Failure of any single one of these six checks is an adapter failure. It must never become `"approved"` and must never become `"rejected"`** — collapsing a failed verification into either domain value would fabricate a Founder decision that was never actually, verifiably made, which is exactly what Section 3.5 and 3.6 forbid. A previously-consumed decision (one this adapter has already accepted and returned once, for any reason including approval-nonce reuse) must not be accepted a second time for a new orchestration call — each request identifier and each approval nonce are both single-use, and the Deployment Agent marks the approval nonce consumed itself, immediately upon successful verification.

### 3.10 Binding a Decision to the Exact Candidate Deployment and Its Transport Metadata

A decision is only valid if the Founder Console's response demonstrably corresponds to **all** of the transport-level metadata enumerated in Section 3.9 — not the request identifier and candidate alone. This is a deliberately stronger requirement than binding to the request identifier by itself: a response that is well-formed and carries a recognized request identifier but whose candidate identity, artifact reference, approval nonce, or decision timestamp do not check out is an adapter failure, exactly as an unrecognized request identifier would be. Silently trusting any single field of this set — the request identifier alone, or the candidate alone — would allow a decision meant for one specific approval exchange to be misapplied to a different one under a race, a replay, or an implementation defect on either side of the boundary. Binding to the full set is what makes a decision deterministically verifiable as belonging to exactly one specific approval exchange, per this ADR's replay-protection, audit-traceability, and forensic-evidence purposes.

### 3.11 Confidentiality and Secret-Redaction Requirements

- No credential, token, session identifier, or other secret material — on either the request or the response side — may appear in any audit event, log line, or error message this adapter produces, mirroring OP-01's `sanitizeRepositoryIdentifier` precedent.
- Any identifier that must appear in an audit event or error for operational traceability (request ID, candidate ID) is safe to include only if it is not itself sensitive; this ADR does not authorize including anything beyond what the transport specification's Request Semantics defines as the request's own fields.
- Transport-level authentication material (however the companion specification's Interaction Model recommendation ultimately authenticates the Deployment Agent to the Founder Console) is configuration input to the adapter, never a value the adapter constructs, logs, or exposes back to any caller.

### 3.12 Future-Proofing Note (Non-Normative)

*The following is not a requirement of this ADR, not part of the MVP, and not required for Operationalization. It is recorded only as a possible future evolution, so a future reader does not need to rediscover it independently.*

A future production-hardening pass may introduce a **signed, immutable Approval Token** — a durable, independently verifiable artifact of the Founder's decision, suitable for external audit and compliance review beyond this project's own audit trail. This ADR does not define such a token's format, signing mechanism, storage, or verification procedure, and does not require one for OP-02 or for Operationalization generally. The transport-level metadata this ADR already requires (Sections 3.9–3.10) is deliberately structured so that, if such a token is introduced later, it would have a natural set of fields to bind to — but that is an observation about future extensibility, not a specification, and implementing it is explicitly out of scope here.

## 4. Consequences

- OP-02 may proceed once this ADR (or a corrected version of it) and the companion transport specification are Accepted/Approved, implementing a live adapter strictly within the boundaries this ADR draws.
- The Deployment Agent gains a defined, narrow authority to act as a deterministic client of the Founder Console — nothing more. It does not gain any identity-verification, allowlist, or decision-making responsibility.
- `FounderConsolePort`, `FounderApprovalRequest`, `FounderApprovalDecision`, and `HighRiskDeploymentOutcome` are unchanged by this ADR. WP-07 and WP-09's existing approval stands; this ADR does not reopen it.
- A new, adapter-specific failure representation will be needed in OP-02 (mirroring `GitHubIntegrationAdapterError`) to satisfy Section 3.6's fail-closed requirement — this ADR does not itself define that type, only requires that it exist and be distinguishable from a genuine domain decision.
- The question of how a caller should respond to a bounded adapter failure across multiple deployment attempts (retry policy, re-scheduling, abandonment) is explicitly deferred — see Section 8 — and must not be answered by OP-02 inventing scheduling behavior unilaterally.

## 5. Alternatives Considered

- **Read ADR-002 as forbidding any Deployment Agent interaction with the Founder Console at all, including through the already-approved `FounderConsolePort`:** rejected. This directly contradicts WP-07 and WP-09's own CTO-approved implementation and acceptance criteria, and would make the Architecture Specification's own required flow (§7 steps 5–7) unimplementable. If this had been the intended reading, WP-07/WP-09 should not have been approved as they were.
- **Read ADR-002 as forbidding only literal LLM/chat-surface involvement, with no further constraint on what a "deterministic" adapter may do:** considered, but rejected as insufficiently protective — this would permit an adapter that, for example, silently treats a timeout as `"rejected"`, which fabricates a Founder decision and defeats ADR-002's actual security purpose (a human, and only a human, decides) even though no LLM was involved. Section 3.6's fail-closed rule exists specifically to close this gap.
- **Allow the Deployment Agent to perform its own lightweight identity check (e.g., verify a shared secret) as a substitute for full Cloudflare Access verification, to simplify the transport:** rejected. Section 3.4 keeps identity verification exclusively with the Founder Console, per ADR-002's own Decision; weakening it here would be a security regression this ADR should not introduce as a side effect of resolving a documentation ambiguity.
- **Resolve the ambiguity informally (a Founder confirmation in chat, with no written record) rather than a formal ADR:** rejected. A security-critical trust boundary should be traceable in the same authoritative record every other architectural decision in this project lives in, not left to conversational context that a future session cannot recover — consistent with the standing rule to treat the ODS Vault, not conversation history, as this project's source of truth.

## 6. Relationship to ADR-002

This ADR **clarifies** ADR-002; it does not amend or supersede it. ADR-002's Decision (adopt the Founder Console, Cloudflare Access-protected, in place of Telegram/Hermes) and its core Consequence (identity verification is independent of AI agents) are unchanged and remain fully in force. This ADR adds the precision ADR-002 itself did not provide: a concrete definition of "AI agent" for this boundary, and an explicit statement of what a compliant deterministic adapter may and must not do. If Accepted, ADR-002's Consequences section should be read together with this ADR's Section 3, not in isolation.

## 7. Non-Goals

This ADR does not:

- Define the transport contract's concrete request/response shape — that is the companion document, `Founder-Console-Integration-Contract.md` (Approved).
- Select or approve an interaction model (synchronous request/response, long-polling, a local broker, or an async port change) — the companion document analyzes options and recommends one without approving it.
- Implement any code, contract, or port.
- Change `FounderConsolePort`, `FounderApprovalRequest`, `FounderApprovalDecision`, or `HighRiskDeploymentOutcome`.
- Define retry, re-scheduling, or abandonment behavior for a deployment whose approval request timed out (Section 8).
- Grant OP-02 implementation authority by itself — that requires this ADR (or a corrected version) to reach Accepted/Approved status, per this project's standing review-gate workflow.

## 8. Open Question Deliberately Left Unresolved

How a caller (whatever ultimately schedules or re-triggers `runDeploymentLifecycle`) should respond to a bounded adapter failure — retry immediately, retry later, surface it to the Founder through some other channel, or abandon the candidate — is an operational/scheduling concern outside `FounderConsolePort`'s boundary and outside this ADR's scope. It is flagged here so it is not silently decided inside OP-02's implementation without its own review.

## 9. References

- ADR-002 — Founder Console Replaces Telegram Approval (Accepted)
- ADR-003 — AI Engineering Workflow v2 (Accepted) — basis for the AI-agent/deterministic-service distinction in Section 3.1
- ADR-008 — MVP Deployment Execution Outcome (Approved) — precedent for a boundary contract behind which an undefined/future concrete mechanism sits
- ADR-009 — MVP High-Risk Deployment Outcome (Approved) — precedent for fail-closed, non-fabricated outcome representation (rejection is a real value, never inferred)
- ADR-012 — Verification Ownership Model (Approved) — precedent for this ADR's structure and for separating "who initiates/sequences" from "who determines"
- Kyron7 Deployment Agent MVP — Architecture Specification (Approved), §6, §7 steps 5–7
- Kyron7 Deployment Policy Engine Specification (Approved) — "From ADR-002" section
- Kyron7 Deployment Execution Engine Specification (Approved) — "From ADR-002" section
- `WP-14-Design-Acceptance.md` §4 — confirms no live Founder Console channel exists yet
- `OP-00-Operationalization-Plan.md` — OP-02, blocked pending this ADR
- `founder-console-integration/README.md`
- `deployment-agent/contracts/founder-console-port.ts`, `founder-approval-request.ts`, `founder-approval-decision.ts`, `high-risk-deployment-outcome.ts`
- `github-integration/github-integration-adapter.ts` (OP-01) — precedent for timeout bounding, input validation, and adapter-specific error wrapping this ADR requires OP-02 to mirror
