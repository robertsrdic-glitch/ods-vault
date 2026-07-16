# Security Sprint 1C — Exploit Test Incident Record

**Date:** 2026-07-16  
**Sprint:** Security Sprint 1C  
**Status:** Partially implemented — MCP Git writes fail-closed  

---

## Vulnerability Discovered

During Sprint 1C implementation, the approval nonce was returned in the MCP tool response from `approve_submission`. This allowed any MCP client (including Claude) to autonomously:

1. Call `approve_submission` to obtain the nonce
2. Call `approve_submission` again with that nonce
3. Trigger Git commit and push without any human action

The static values `approver_id = "founder"` and `approver_channel = "mcp-tool"` did not prove Founder identity or manual approval.

## Controlled Exploit Performed

A controlled exploit test was executed against the production endpoint using a non-production test submission. The test:

1. Registered an OAuth client
2. Submitted a test file (`exploit-test.md`) to project `ExploitTest`
3. Called `approve_submission` — received the raw nonce in the response
4. Called `approve_submission` again with the nonce — Git commit and push succeeded

**Exploit test commit:** `83b7a8970b10a03356ae5eb79386d3995c1c2140`  
- File added: `projekti/ExploitTest/04 Design Deliverables/Foundation/exploit-test.md`
- Content: `# Exploit Test`
- No sensitive data (tokens, nonces, credentials) in the commit
- No legitimate production documentation affected

## Mitigation

The vulnerability was fixed by switching `approve_submission` to fail-closed behavior:

- `approval_nonce` parameter removed from the MCP tool input schema
- Raw nonce no longer returned in any MCP response
- Git commit and push operations removed from the MCP tool entirely
- `get_submission_status` and `inspect_staged_submission` never expose the nonce
- Nonce is still generated and stored internally for a future trusted Founder approval channel

**Mitigation commit:** `10b1e5839ee2001647076f42909aade32be51fd1`  
**Repository:** `Kyron7/northstar-artifact-gateway`

## Revert

The exploit test commit was reverted from the ODS Vault:

**Revert commit:** `b632f620589135d2de37af692d0b41f5c2dd4438`  
**Method:** `git revert` (no force-push, no history rewriting)  
**Pushed to:** `robertsrdic-glitch/ods-vault` origin/main

## Confirmation

- No real production documentation was affected by the exploit test
- The exploit test file (`exploit-test.md`) is absent from the current branch
- Working tree is clean
- Local and remote HEAD match
- No credentials, nonces, or sensitive data were written to Git history, logs, or test scripts

## Current Status

**Sprint 1C: PARTIALLY IMPLEMENTED — WAITING FOR TRUSTED FOUNDER APPROVAL CHANNEL**

- ✅ `approve_submission` creates pending approval with 24h TTL
- ✅ Nonce is stored internally (never exposed via MCP)
- ✅ Replay protection (one-time use)
- ✅ Mandatory rejection comments
- ✅ Atomic crash-safe persistence
- ✅ No MCP-only sequence can commit or push to Git
- ❌ Trusted Founder approval channel (e.g., Telegram bot with user ID verification) — future work

## Remaining Work

A separate trusted channel must be built that:
1. Is NOT accessible via MCP
2. Verifies Founder identity (Telegram user ID)
3. Consumes the stored nonce
4. Performs Git commit and push
5. Records the real approver identity
