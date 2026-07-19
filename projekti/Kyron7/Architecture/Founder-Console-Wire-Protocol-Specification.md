# Founder Console Wire Protocol Specification

**Type:** Design Specification (implementation specification beneath ADR-014, not a replacement for it)
**Status:** Approved
**Approved:** 2026-07-19 (Founder)
**Date:** 2026-07-19
**Revision:** CTO security-review refinement pass, 2026-07-19 — normative MVP timing values, base64url-per-field HMAC canonicalization, key-ID-based signature headers, strict schema behavior, precise idempotency response, scoped 429/`Retry-After` handling. No architecture or trust-boundary change.
**Depends on:** ADR-002 (Accepted); ADR-014 (Accepted); Founder Console Integration Contract (Approved); `OP-00-Operationalization-Plan.md` (Approved); `FounderConsolePort`, `FounderApprovalRequest`, `FounderApprovalDecision`, `CandidateDeployment` (all unchanged)

This document supplies the concrete wire-level mechanics the Founder Console Integration Contract deliberately left undefined (its own §6 Non-Goals: "Select a serialization format, HTTP library, or specific transport technology"). It does not reopen ADR-014's trust-boundary decision or the Integration Contract's behavioral requirements — every rule in those two documents governs unchanged; this document only makes them concretely implementable. It is not a new ADR: no architecture, port, or domain contract changes as a result of it (verified in §11).

---

## 1. Transport

- HTTPS only.
- JSON request and response bodies (`Content-Type: application/json`).
- Versioned API namespace: `/api/v1`. A future breaking change increments to `/api/v2`; this document governs `v1` only.

## 2. Submission Endpoint

`POST /api/v1/approval-requests` — creates one immutable Founder approval transaction.

### 2.1 Request

Headers:
- `Content-Type: application/json`
- `Accept: application/json`
- `CF-Access-Client-Id: <service token client ID>` — Cloudflare Access' own standard service-token header (see §7.1); not invented here.
- `CF-Access-Client-Secret: <service token secret>` — companion header to the above.

Body — every field is either already available from `CandidateDeployment` or synthesized by the adapter per the Integration Contract §1; fields are flattened (not nested) so their names match the canonicalization field names in §8.1 exactly, removing any ambiguity about which JSON path a canonical field name refers to:

```json
{
  "protocolVersion": "1",
  "requestId": "<adapter-generated unique identifier>",
  "candidateId": "<candidate.id>",
  "candidateArtifactRef": "<candidate.artifactRef>",
  "requestCreatedAt": "<ISO-8601 UTC timestamp>",
  "expiresAt": "<ISO-8601 UTC timestamp — requestCreatedAt + 15 minutes, per §5>",
  "approvalNonce": "<adapter-generated single-use value, base64url-encoded, unpadded>"
}
```

No `targetEnvironment` or `classificationRationale` field — per the Integration Contract §1, neither is available to the Deployment Agent under the current architecture, and this document does not authorize adding either.

### 2.2 Responses

- **Successful, new transaction — `201 Created`:** echoes every immutable field back, so the adapter can verify Founder Console stored exactly what was submitted, byte-for-byte, before trusting the transaction exists correctly:
  ```json
  {
    "requestId": "<echoed>",
    "status": "pending",
    "candidateId": "<echoed>",
    "candidateArtifactRef": "<echoed>",
    "requestCreatedAt": "<echoed>",
    "expiresAt": "<echoed>",
    "approvalNonce": "<echoed>",
    "acceptedAt": "<ISO-8601 UTC timestamp — server receipt time>"
  }
  ```
  A compliant adapter compares every echoed field against what it sent; any mismatch is treated as a `malformed-response` adapter failure (§9) — Founder Console recording something other than what was submitted is never silently trusted.
- **Duplicate submission, same `requestId` with byte-equivalent logical values for every immutable field — `200 OK`:** identical body shape to the above, describing the *existing* transaction's current state (its `status` may by now be `"decided"` — see §6.6). No second transaction is created. "Byte-equivalent logical values" means the parsed, validated values match — not that the two raw JSON request bodies were textually identical (differing whitespace or key order does not make a resubmission "conflicting").
- **Duplicate submission, same `requestId` but any differing immutable value — `409 Conflict`:** refused outright; neither the original nor the conflicting version is silently preferred.
- **Malformed request** — `400 Bad Request`, body `{ "error": "malformed_request", "detail": "<safe, non-sensitive description>" }`. Covers: invalid JSON; a duplicate JSON object key within the request body, where the parser or validation layer is able to detect it; a missing required field; a field of the wrong type; an unsupported `protocolVersion` (see §9 — a version bump is the only forward-compatible path, never silent tolerance of an unrecognized version); and any unknown top-level field (§9 — strict for MVP, not ignored).
- **Expired at submission** (`expiresAt` not strictly after `requestCreatedAt`, or `expiresAt` already past at receipt time) — `400 Bad Request`, `{ "error": "expired_at_submission" }`. Rejected before any transaction record is created — never silently accepted, never treated as a decision.
- **Authentication failure** (missing/invalid `CF-Access-Client-*` headers) — `401 Unauthorized`. A structurally valid token that is not authorized for this operation — `403 Forbidden`.
- **Oversized body** — `413 Payload Too Large`.
- **Server error** — `500 Internal Server Error`.

## 3. Polling Endpoint

`GET /api/v1/approval-requests/{requestId}?waitSeconds=<value>` — bounded long-polling for the status of one exact, already-submitted approval request.

`waitSeconds` (optional):
- **Default: 20** — used when the parameter is omitted.
- **Maximum: 25** — a client-requested value above 25 is silently clamped to 25 (the server's own ceiling governs, never the client's raw request).
- A provided value that is not a positive integer is treated as omitted (default 20 applies) rather than rejected — `waitSeconds` is a non-security-relevant hint, unlike every value covered by §8's signing.

Headers: same `CF-Access-Client-Id`/`CF-Access-Client-Secret` pair as submission — this endpoint is equally machine-authenticated.

### 3.1 Transport-Level Statuses

Exactly two: `pending` and `decided`. **`pending` is not a domain decision** — it means "no Founder decision exists yet," nothing more. **Only a `decided` response may carry a domain decision**, and that decision is exactly one of `"approved"` or `"rejected"` — no other domain decision is ever permitted at this endpoint or any other.

### 3.2 Pending Response

`200 OK`:
```json
{ "requestId": "<echoed>", "status": "pending" }
```
No signature required — nothing decision-bearing is being asserted.

### 3.3 Decided Response

`200 OK`:
```json
{
  "requestId": "<echoed>",
  "status": "decided",
  "candidateId": "<echoed>",
  "candidateArtifactRef": "<echoed>",
  "requestCreatedAt": "<echoed from the original request>",
  "approvalNonce": "<echoed>",
  "decisionTimestamp": "<ISO-8601 UTC timestamp>",
  "decision": "approved"
}
```
(`"decision"` is `"approved"` or `"rejected"` — nothing else.) `decisionTimestamp` is the **sole** decision timestamp — it appears once, in the body, and is the exact value covered by the signature (§8.1). No separate timestamp header exists; there is nothing that could diverge from it.

Response headers, **required** on every `decided` response:
- `X-Signature-Key-Id: <non-secret key identifier>` — selects which configured verification secret to check against (§8.2).
- `X-Signature: v1=<lowercase hex-encoded HMAC-SHA-256>` — `v1` identifies the signature/canonicalization protocol version (§8.1), not a secret version; secret rotation is handled entirely by `X-Signature-Key-Id` (§8.2).

### 3.4 Other Polling Responses

- **Unknown or purged `requestId` — `404 Not Found`.**
- **Rate limited — `429 Too Many Requests`.** See §5 for exact `Retry-After` handling. Server-side rate limiting is a permitted, recommended behavior — **not a mandatory OP-02 MVP completion criterion**; an implementation that never triggers it is still compliant. `429` never represents, and must never be interpreted as, Founder rejection or any other domain decision.
- **Authentication failure — `401`/`403`,** same as submission.
- **Server error — `500`.**

## 4. HTTP Status Model (Summary)

| Status | Meaning | Endpoint(s) |
|---|---|---|
| 200 | Idempotent duplicate submission; pending poll result; decided poll result | submit, poll |
| 201 | New transaction created | submit |
| 400 | Malformed request; expired at submission | submit |
| 401 | Missing/invalid machine authentication | submit, poll |
| 403 | Valid machine identity, not authorized for this operation | submit, poll |
| 404 | Unknown/purged request identifier | poll |
| 409 | Duplicate request identifier, conflicting data | submit |
| 413 | Oversized request body | submit |
| 429 | Rate limited (optional; never mandatory) | poll |
| 500 | Founder Console internal failure | submit, poll |

**A Founder rejection is always `200 OK` with `"status": "decided", "decision": "rejected"` in the body — never an HTTP error status.** No HTTP status in this table is ever a substitute for, or implies, either domain decision; the domain decision exists only inside a `200`/`decided` body.

## 5. Timeout and Polling Model — Normative MVP Values

Every value below is **fixed and required for MVP compliance**, not an illustrative default (superseding the prior draft's "adjustable implementation parameter" framing for these specific numbers):

- **Approval request validity: 15 minutes.** `expiresAt = requestCreatedAt + 15 minutes`, set by the adapter at submission.
- **Default `waitSeconds`: 20.** Used when the client omits the parameter (§3).
- **Maximum `waitSeconds`: 25.** Server-enforced ceiling regardless of client request (§3).
- **Client per-request timeout: 30 seconds.** Bounds a single poll HTTP call — comfortably above the 25-second maximum server-held wait, with margin for network latency.
- **Total adapter timeout: 15 minutes, and never later than `expiresAt`.** In practice these two 15-minute windows are the same window (both anchored to submission time), so this rule is a safety bound against clock skew or misconfiguration, not two independently-drifting timers — whichever of "15 minutes elapsed" or "past `expiresAt`" is reached first ends the wait.
- **No polling delay after a `pending` response.** The next bounded long-poll begins immediately — the server-held wait itself *is* the interval; no additional client-side sleep is introduced.
- **`429` / `Retry-After` handling:** on a `429` response, the adapter honors the `Retry-After` header **only** when it is present, expressed as a non-negative integer count of seconds (the HTTP-date form of `Retry-After` is not supported for MVP — treated as unusable), strictly positive, no greater than 30 seconds, and — after adding it to the current time — still resolves to a moment before both the remaining total-adapter-timeout budget is exhausted and `expiresAt`. If `Retry-After` is missing, non-numeric, zero, negative, greater than 30 seconds, in the unsupported HTTP-date form, or would not fit within either remaining bound, the adapter treats the `429` as an adapter failure (rate-limit-unusable) rather than guessing a backoff.
- **Timeout is never converted to the domain decision `"rejected"`** (or `"approved"`) — it is an adapter failure, exactly as ADR-014 §3.6 already requires for every other verification failure.
- **No indefinite blocking under any configuration** — every value above is finite.

## 6. Replay and Lifecycle Semantics

- **Request identifiers** are immutable, unique, and generated fresh by the Deployment Agent per approval transaction. A retried *attempt* after a timeout is a new transaction with a new request identifier and a new nonce — the old one is never reused, even if it might still resolve later.
- **Approval nonces** are single-use, generated 1:1 with a request identifier, never reused across requests.
- **Duplicate submission, identical logical data:** idempotent (§2.2, `200`) — safe for the adapter's own transport-level retries. Comparison uses the parsed, validated logical values, never a raw-JSON-substring or textual comparison (§8.1 applies the same principle to signing).
- **Duplicate submission, conflicting data:** refused (§2.2, `409`) — never silently resolved either way.
- **Decision immutability:** once Founder Console records a decision for a request identifier, that decision is fixed. **Founder Console must never allow a second or replacement decision for the same approval transaction.** Re-polling a decided request always returns the same `decided` body and the same signature.
- **Consumed-nonce ownership — split, matching ADR-014 §3.9 and this task's explicit direction:**
  - The **Deployment Agent** keeps *process-local* state — in memory, for the lifetime of one synchronous `submitCandidateForApproval()` call only — solely for its own immediate duplicate-processing protection within that call. This state does not survive a process restart, and does not need to.
  - **Founder Console is the authoritative, durable system of record.** It must durably retain request and decision state for at least the approval validity window plus the audit retention period, independent of whether any particular Deployment Agent process is still running to collect the result.
- **Behavior across process restarts:** the Deployment Agent's local bookkeeping is lost on restart — this is not a gap, because each synchronous call is self-contained (fresh request identifier and nonce every time) and Founder Console's durable store, not the Deployment Agent process, is what actually prevents a decision from being manufactured twice or a conflicting resubmission from being silently accepted.

**Conflict check against ADR-014 / the Integration Contract:** ADR-014 §3.9's statement that "the Deployment Agent marks the approval nonce consumed itself, immediately upon successful verification" describes the adapter's own local bookkeeping for one call — it does not, on inspection, assign the Deployment Agent as the *durable* system of record. Founder Console additionally, independently enforcing durable replay/conflict prevention on its own side is complementary to that local check, not contradictory to it. **No conflict found; this document proceeds without alteration to either governing document's substance.**

## 7. Authentication and Trust Boundaries

### 7.1 Machine Identity — Cloudflare Access Service Token

The Deployment Agent authenticates to Founder Console using a Cloudflare Access **service token** — Cloudflare's own existing mechanism, not invented here — presented via the `CF-Access-Client-Id` / `CF-Access-Client-Secret` header pair (Cloudflare's standard header names for this mechanism). Configuration ownership: both values are adapter *configuration inputs*, sourced from whatever composes/deploys the Deployment Agent for a given environment, never generated, derived, or persisted by the adapter itself, and never logged (§9). No example or placeholder secret value appears in this document.

**This service token proves only "this call is the deterministic Deployment Agent machine client."** It carries no Founder identity and does not, by itself, authorize the creation of a Founder decision — it only gets the adapter through Founder Console's front door to submit a request and poll for a result someone else (the Founder) must actually produce.

### 7.2 Founder Identity

Unchanged from ADR-014 §3.4 and the Integration Contract §3, restated for completeness, not redefined: Founder Console remains solely responsible for interactive Founder authentication, Founder allowlist verification, decision presentation, decision capture, and decision-timestamp generation. **This document does not design, specify, or implement any part of the Founder-facing web UI or its authentication flow** — that is explicitly out of scope for this task and for OP-02.

## 8. Decision Integrity — HMAC Model

- **Algorithm:** HMAC-SHA-256.
- **Secret:** a dedicated verification secret, configured independently from the Cloudflare Access service token (different value, different configuration input, never derived from one another) — compromise of one does not compromise the other.
- **Headers, both required on every `decided` response:**
  - `X-Signature-Key-Id: <non-secret key identifier>` — a label (e.g. an opaque short string or date-stamped name), never secret material itself, selecting which configured verification secret the adapter should check against.
  - `X-Signature: v1=<lowercase hex-encoded HMAC-SHA-256>` — `v1` is the signature/canonicalization protocol version defined by this document (§8.1), independent of which key ID produced the signature.

### 8.1 Canonical Signing Representation

Encoding and structure, precisely, so two independent implementations can never sign different byte sequences for the same logical response:

- Encoding: UTF-8 throughout.
- Fixed, ordered field names (below) — field names are literal ASCII and are **not** themselves encoded.
- Every logical field *value* is Base64url-encoded, **without padding** (no trailing `=`), before being placed in the canonical string. "Logical value" means the parsed, validated value the adapter/server actually operates on — never a raw JSON substring, and never dependent on how the surrounding JSON happened to be formatted or ordered.
- Each line has the exact form `fieldName=base64urlValue`.
- Lines are separated by exactly one ASCII LF (`\n`). There is **no terminal newline** after the last line.

Field order (exactly):

1. `protocolVersion`
2. `requestId`
3. `candidateId`
4. `candidateArtifactRef`
5. `requestCreatedAt`
6. `approvalNonce`
7. `decisionTimestamp`
8. `decision`

This fully covers every field ADR-014 §3.9's binding check requires (the six-field binding set) plus the decision itself, and — because every value is Base64url-encoded before insertion — no escaping rule is needed: a Base64url alphabet (`A–Z a–z 0–9 - _`) cannot itself contain a literal `\n` or `=`, so no field's encoded value can ever be mistaken for the line delimiter or for another field's boundary, regardless of what characters the original logical value contained.

#### Example (obviously fake, non-sensitive values — illustrating format only)

Given:
```
protocolVersion       = 1
requestId              = example-request-0001
candidateId            = deadbeefdeadbeefdeadbeefdeadbeefdeadbeef
candidateArtifactRef   = https://example.invalid/example-org/example-repo.git#main@deadbeefdeadbeefdeadbeefdeadbeefdeadbeef
requestCreatedAt       = 2026-07-19T18:00:00.000Z
approvalNonce          = example-nonce-0001-not-real
decisionTimestamp      = 2026-07-19T18:05:00.000Z
decision               = approved
```

The canonical string (each line `fieldName=base64urlValue`, joined by `\n`, no trailing newline) is exactly:

```
protocolVersion=MQ
requestId=ZXhhbXBsZS1yZXF1ZXN0LTAwMDE
candidateId=ZGVhZGJlZWZkZWFkYmVlZmRlYWRiZWVmZGVhZGJlZWZkZWFkYmVlZg
candidateArtifactRef=aHR0cHM6Ly9leGFtcGxlLmludmFsaWQvZXhhbXBsZS1vcmcvZXhhbXBsZS1yZXBvLmdpdCNtYWluQGRlYWRiZWVmZGVhZGJlZWZkZWFkYmVlZmRlYWRiZWVmZGVhZGJlZWY
requestCreatedAt=MjAyNi0wNy0xOVQxODowMDowMC4wMDBa
approvalNonce=ZXhhbXBsZS1ub25jZS0wMDAxLW5vdC1yZWFs
decisionTimestamp=MjAyNi0wNy0xOVQxODowNTowMC4wMDBa
decision=YXBwcm92ZWQ
```

(449 bytes total, verified.) HMAC-SHA-256 of exactly these bytes, with the obviously-fake example secret `example-secret-not-real`, is:

```
9a1b1d9f06e5ee973f54a79ed0f005a7a7484cd5c25a9d6fe3c3c4f381bfb8f4
```

so the response would carry `X-Signature: v1=9a1b1d9f06e5ee973f54a79ed0f005a7a7484cd5c25a9d6fe3c3c4f381bfb8f4` (both the canonical string and this HMAC were computed and verified while drafting this document, not hand-typed).

### 8.2 Verification

- **Generation ownership:** Founder Console, at the moment it produces a `decided` response, using whichever secret `X-Signature-Key-Id` names.
- **Verification ownership:** the Deployment Agent adapter, before accepting any `decided` response's `decision` value.
- **Key selection:** the adapter reads `X-Signature-Key-Id` and looks up the matching secret from its own configuration. **An unknown key ID is an integrity failure** — the adapter never falls back to a default secret or attempts every configured secret as a substitute for correct key selection.
- **Comparison:** the adapter recomputes the HMAC using the selected secret and the canonical representation (§8.1) it constructs from the response body's own logical values (never from the raw signature header or any other part of the response). It first validates that the received signature, after hex-decoding, is exactly 32 bytes (SHA-256 output length) — a different length is an integrity failure before any comparison is attempted. Only then does it compare using a **constant-time** byte comparison (e.g. `crypto.timingSafeEqual` or equivalent) — never a standard string/array equality check, to avoid a timing side-channel.
- **Missing signature or missing key ID header:** integrity failure — treated identically to an invalid one, never as if an unsigned or unkeyed response were implicitly trusted.
- **Malformed signature** (not valid lowercase hexadecimal, or wrong decoded length): integrity failure.
- **Unsupported signature version** (an `X-Signature` prefix other than `v1`): integrity failure — the adapter does not attempt to verify against a canonicalization scheme it doesn't implement.
- **Invalid signature** (well-formed, correct length, doesn't match recomputed value): integrity failure.
- **Key rotation:** `X-Signature-Key-Id` is the rotation mechanism. The Deployment Agent may hold a **bounded set** of active verification secrets (e.g. current plus one prior, during a rotation window), each addressed by its own key ID; it looks up the specific secret the header names rather than trying several. Key IDs are non-secret and may appear in logs/configuration inspection; the secrets themselves never may.
- **Never accepted from the response body:** neither a key ID nor a secret value is ever read from the JSON body — both, when relevant, come only from the response headers (key ID) or the adapter's own local configuration (secret); a body field that happened to be named similarly is never treated as authoritative for either.
- **Redaction:** the HMAC secret (any key/version) is never logged, never included in an error message, never echoed back by the adapter to any caller. Key IDs, being non-secret, may appear in diagnostic output.

**Any integrity failure — missing/malformed/unsupported-version/invalid signature, unknown key ID, or a key-ID/signature-header mismatch of any kind — is an adapter failure. It must never become `"approved"` and must never become `"rejected"`,** exactly as ADR-014 §3.6 and §3.9 already require for every other verification failure.

## 9. Strict Schema Behavior and Error/Privacy Model

**Strict for MVP** (supersedes the prior draft's "unknown fields ignored" leniency, per this review):

- **Unknown top-level fields in a submission request** — `400 malformed_request` (§2.2). Not silently ignored.
- **Unknown top-level fields in a `pending` or `decided` polling response** — treated as `malformed-response`, an adapter failure. The adapter does not silently tolerate server-side fields it doesn't recognize.
- **Missing required fields** (either direction) — the corresponding protocol failure: `400 malformed_request` on submission, `malformed-response` adapter failure on a response.
- **Duplicate JSON object keys within a single body** — rejected wherever the parser or validation layer is capable of detecting the duplication (most JSON parsers silently keep only the last-seen value for a duplicate key, which is exactly the kind of ambiguity this document does not want silently resolved one way or the other); treated as `malformed_request` / `malformed-response`.
- **Forward compatibility is achieved only through a new, explicitly supported `protocolVersion`** (e.g. this document's future `v2`) — never by a party silently ignoring a field it doesn't understand. An unrecognized `protocolVersion` on a request is `400`; an unrecognized signing version on a response (§8.2) is an integrity failure.

| Condition | Handling |
|---|---|
| Malformed JSON | `400 malformed_request` (submission); `malformed-response` (polling) |
| Missing required field | `400 malformed_request` / `malformed-response` |
| Unknown field | `400 malformed_request` (submission) / `malformed-response` (polling) — strict, not ignored |
| Duplicate JSON key | `400 malformed_request` / `malformed-response`, where detectable |
| Oversized body | `413` |
| Invalid/unparseable timestamp | `400 malformed_request` |
| `expiresAt` not after `requestCreatedAt`, or already past | `400 expired_at_submission` |
| Invalid nonce or request-identifier format | `400 malformed_request` (submission); `404` (polling an unrecognized identifier) |
| Mismatched candidate data in a `decided` response | Adapter-side binding failure (ADR-014 §3.9/§3.10) — detected after an otherwise-valid `200` |
| Unsupported `protocolVersion` | `400` (request); unsupported signing version is an integrity failure (response, §8.2) |
| Authentication failure | `401`/`403` |
| HMAC/key-ID verification failure | Integrity failure (§8.2) |
| Expired decision | Adapter failure, per ADR-014 §3.9 check 4/6 |
| Replayed/mismatched response | Adapter failure, per ADR-014 §3.9 check 1/5 |
| `429` with missing/malformed/excessive/unusable `Retry-After` | Adapter failure (rate-limit-unusable, §5) |
| Founder Console unavailable | Transport failure (connection refused, DNS failure, 5xx, timeout) |

**Never exposed in any log, error message, or audit event:** Cloudflare Access service-token values (`CF-Access-Client-Id`/`Secret`), any HMAC secret (any key ID), any authorization-equivalent header, and raw/unsanitized response bodies in full — errors carry only the structured, safe fields this document and ADR-014 §3.11 already define (operation, request/candidate identifiers, failure category, non-secret key ID where relevant), never a verbatim dump of what Founder Console returned.

## 10. Correction to the Approved Founder Console Integration Contract

No further correction was made this pass. The single correction from the prior revision (§4's "not an approval or a decision" sentence, replaced to state that bounded, client-driven long-polling is the Approved interaction model with wire detail delegated to this document) remains the only change to that file. Nothing in this refinement pass introduces a new contradiction with the Integration Contract's text — the changes here (normative timing values, HMAC canonicalization detail, strict schema behavior) are all within the concrete-wire-detail scope the Integration Contract already delegates to this document, not a restatement or alteration of any behavioral rule the Integration Contract itself states.

## 11. Impact Analysis (Verified Against the Repository)

Re-checked via `git status`/`git diff` immediately before this revision — zero changes to any of the following:

- **`FounderConsolePort`** — no change required. Every wire-level field this document defines (request identifier, approval nonce, timestamps, canonicalization) is constructed and consumed entirely inside the concrete adapter, never crossing this interface.
- **`FounderApprovalRequest`** — no change required. Remains `{ candidate: CandidateDeployment }`.
- **`FounderApprovalDecision`** — no change required. Remains exactly `"approved" | "rejected"`.
- **`CandidateDeployment`** — no change required. `id`/`artifactRef` are read, not modified.
- **Orchestrator behavior** — no change required. It only ever calls `submitCandidateForApproval(request)` and branches on the returned `FounderApprovalDecision`; it has no visibility into anything this wire specification defines.

**Answer: no.** Implementation under this specification requires no change to any of the above.

## 12. Traceability

- ADR-002 — Founder Console Replaces Telegram Approval (Accepted)
- ADR-014 — Founder Approval Transport and Trust Boundary (Accepted) — governs the trust boundary and behavioral requirements this document makes concrete
- Founder Console Integration Contract (Approved) — this document's direct parent
- `OP-00-Operationalization-Plan.md` (Approved) — OP-02, still not yet implemented
- `deployment-agent/contracts/founder-console-port.ts`, `founder-approval-request.ts`, `founder-approval-decision.ts`, `candidate-deployment.ts` — verified unchanged, §11
- `deployment-agent/orchestrator.ts` — verified unchanged, §11
- `github-integration/github-integration-adapter.ts` (OP-01) — precedent this specification's timeout, validation, and error-wrapping model continues to follow

## 13. Non-Goals / Restrictions

This document does not, and its existence does not authorize:

- Writing any source code.
- Creating the Founder Console service itself, or any part of its web UI or Founder-facing authentication flow.
- Modifying `FounderConsolePort`, `FounderApprovalRequest`, `FounderApprovalDecision`, `CandidateDeployment`, or any other domain contract.
- Changing ADR-002, ADR-014, or any other existing ADR.
- Beginning OP-02 implementation, OP-03, or any later Operationalization work package.
- Its own promotion to Accepted/Approved status — that remains a separate, future CTO/Founder decision.

## 14. Unresolved Decisions Requiring CTO or Founder Review

- Whether the normative MVP timing values in §5 (15-minute validity, 20s/25s `waitSeconds`, 30s per-request timeout, 15-minute total timeout) should be implemented as hardcoded constants or exposed as overridable configuration (mirroring OP-01's default-plus-max pattern) — the *values* are now fixed by this document; whether OP-02's code structure allows overriding them is an open implementation-style question, not a protocol one.
- Whether a `v2` key-rotation model ever needs more than "current plus one prior" secret held concurrently, if rotation windows in practice need to be longer.
- Confirmation that this specification, once implemented, fully satisfies "the Approved bounded interaction model" referenced in OP-00's OP-02 entry, or whether OP-00 needs its own further update once implementation begins.
