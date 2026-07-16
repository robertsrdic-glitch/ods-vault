# Security Sprint 1A — Completion Record

**Sprint:** Security Sprint 1A  
**Status:** Completed and Frozen  
**Completion Date:** 2026-07-16  
**Gateway Version:** 1.0.0  
**Public Endpoint:** https://mcp.kyron7.com  

---

## Implemented Fixes

| ID | Severity | Title | Implementation |
|---|---|---|---|
| H4 | High | OAuth endpoint rate limiting | Custom Express middleware using CF-Connecting-IP as key. 5 registrations/hour, 15 OAuth requests/minute. SDK built-in rate limiting disabled (uses req.ip which is 127.0.0.1 for tunnel traffic). `validate: false` on express-rate-limit to disable proxy header validation warnings. `app.set('trust proxy', true)` to read CF-Connecting-IP. |
| M3 | Medium | OAuth security audit logging | `appendAudit()` calls added to `registerClient`, `authorize`, `exchangeAuthorizationCode`, `revokeToken`. Logs: timestamp, action, truncated client_id (first 8 chars + ...), scopes, result. Never logs: tokens, secrets, codes, verifiers. |
| H2 | High | 60-second authorization-code expiry | `expiresAt` field added to auth code record. Checked in `challengeForAuthorizationCode()` (called by SDK before exchange) and `exchangeAuthorizationCode()`. Expired codes are deleted. One-time use enforced by deletion after exchange. |
| H3 | High | PKCE S256 enforcement | Handled by MCP SDK via `challengeForAuthorizationCode()` + `verifyChallenge()` from `pkce-challenge` package. SDK calls these before `exchangeAuthorizationCode()`. No custom PKCE code needed. `skipLocalPkceValidation` is falsy (default) — SDK enforces PKCE. |
| H1 | High | redirect_uri matching at token exchange | `if (redirectUri && authCode.redirectUri !== redirectUri) throw new Error('Redirect URI mismatch')` in `exchangeAuthorizationCode()`. |
| L2 | Low | 7-day refresh-token expiry | `refreshTokenExpiresAt` field added to `InMemoryToken`. Checked in `exchangeRefreshToken()`. Expired refresh tokens and their access tokens are deleted. |
| L3 | Low | Client-wide token revocation | `revokeToken()` now iterates all tokens in `this.tokens` Map and deletes all with matching `clientId`. Also deletes their refresh tokens. |

## Files Changed

| File | Changes |
|---|---|
| `src/index.ts` | Added `rateLimit` import. Added `rateLimitKeyGenerator()`. Added `expiresAt` to authCodes type. Added `refreshTokenExpiresAt` to InMemoryToken. Modified `registerClient()`, `authorize()`, `challengeForAuthorizationCode()`, `exchangeAuthorizationCode()`, `exchangeRefreshToken()` (signature fix), `revokeToken()`. Added rate limiter middleware. Set trust proxy. Disabled SDK rate limiting. |
| `src/types.ts` | Made `submission_id`, `filenames`, `hashes` optional in `AuditEntry`. Added `client_id` and `scopes` fields. |

## Verification Results

### Pre-deployment (clean code)
- Full MCP protocol: 18/18 passed

### Post-deployment
- Gateway process: 1 running, stable
- Local /health: HTTP 200
- Public https://mcp.kyron7.com/health: HTTP 200
- OAuth discovery: HTTP 200, all URLs use https://mcp.kyron7.com
- Full MCP protocol: 18/18 passed
- OAuth state parameter flow: 8/8 passed
- Five tools exposed: submit_design_deliverables, inspect_staged_submission, approve_submission, reject_submission, get_submission_status
- Read-only get_submission_status call: returned expected "Not found" for nonexistent submission
- No write tools called
- ods-vault git status: clean (no modifications)
- Audit log: entries for client_registration, authorize, token_exchange — no secrets logged
- Gateway logs: no errors
- Claude Remote MCP connector: successfully authenticated and operational

## Rate Limiting Approach

Cloudflare Tunnel forwards `CF-Connecting-IP` header with the real client IP. All tunnel traffic appears as `127.0.0.1` to Express, so default IP-based rate limiting would lump all users into one bucket. Custom `keyGenerator` reads `CF-Connecting-IP` (set only by cloudflared on loopback). Direct external access to port 8819 is blocked by Hostinger firewall. `app.set('trust proxy', true)` allows Express to read proxy headers.

## Rollback Backup Path

```
/opt/data/northstar-artifact-gateway/backups/sprint1a-20260716T164318Z/
  ├── index.ts   (pre-Sprint 1A original)
  ├── types.ts   (pre-Sprint 1A original)
  └── .env       (pre-Sprint 1A original)
```

Rollback commands:
```bash
cp /opt/data/northstar-artifact-gateway/backups/sprint1a-20260716T164318Z/index.ts /opt/data/northstar-artifact-gateway/src/index.ts
cp /opt/data/northstar-artifact-gateway/backups/sprint1a-20260716T164318Z/types.ts /opt/data/northstar-artifact-gateway/src/types.ts
cd /opt/data/northstar-artifact-gateway && npx tsc
pkill -f "^node dist/start"; sleep 2; nohup node dist/start.js >> /opt/data/logs/northstar-gateway.log 2>&1 &
```

## Remaining Findings

### Critical
| ID | Title | Sprint |
|---|---|---|
| C1 | Open dynamic client registration | 1B |
| C2 | Auto-approve authorization without user login | 1C |
| C3 | No scope restriction per tool | 1B |
| C4 | Attacker can push to ods-vault via approve_submission | 1C |

### Medium
| ID | Title | Sprint |
|---|---|---|
| M1 | No scope enforcement per MCP tool | 1B |
| M2 | Tokens stored in memory only (lost on restart) | Future |
| M4 | Cloudflare tunnel token in plaintext file | 1E |

### Low
| ID | Title | Sprint |
|---|---|---|
| L1 | State parameter not cryptographically validated | 1D |

## Next Approved Order

1. **Sprint 1C** — Manual approval queue (addresses C2, C4 — highest remaining risk)
2. **Sprint 1B** — Registration controls + scope enforcement (addresses C1, C3, M1)
3. **Sprint 1D** — Cloudflare Access on /authorize (addresses C2 final layer, L1)
4. **Sprint 1E** — Tunnel token hardening (addresses M4)

## Gateway Source Repository Status

The gateway source code at `/opt/data/northstar-artifact-gateway/` is **NOT a Git repository**. There is no `.git` directory, no remote, no commits. The code exists only on the VPS filesystem with timestamped backups.

**Recommendation:** Initialize a Git repository for the gateway source code and push to GitHub (under the `robertsrdic-glitch` account, either as a new repo or within an existing Kyron7 repo). This should be done before Sprint 1C to ensure proper version control of security-critical code. Requires Founder approval.

A Git tag `security-sprint-1a` would be appropriate AFTER the repository is initialized, to mark the frozen Sprint 1A state.
