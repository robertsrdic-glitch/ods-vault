# ADR-002: Founder Console Replaces Telegram Approval

**Status:** Accepted
**Date:** 2026-07-16

## Context

Telegram, as the Founder approval channel for NorthStar Artifact Gateway submissions, introduces an unnecessary dependency on the Hermes agent for a routine, high-frequency action, and consumes Hermes operating credits for work that does not require an AI agent in the loop at all. It also ties a security-critical approval path to a third-party consumer messaging platform rather than to infrastructure Kyron7 controls directly.

## Decision

Reject Telegram as the long-term Founder approval channel.

Adopt a secure Founder Console (`founder.kyron7.com`), protected by Cloudflare Access, as the approval channel instead.

## Consequences

- Founder approval becomes independent of MCP and of AI agents — no AI agent surface exposes or consumes the approval mechanism.
- Normal approval operation no longer depends on Hermes; Hermes is no longer required for routine submission approval or rejection.
- Identity verification moves from a Telegram user ID to a Cloudflare Access-authenticated, server-verified identity, checked against an explicit Founder allowlist.
- The Founder Console becomes the first user-facing component of the broader long-term control-center vision (products, agents, deployments, incidents, analytics, administrative actions), starting deliberately minimal with submission approval as its first function.
