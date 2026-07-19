# ADR-003: AI Engineering Workflow v2

**Status:** Accepted
**Date:** 2026-07-16

## Context

The engineering workflow across AI agents needs an explicit division of responsibility to reduce deployment cost while improving quality. Without a defined workflow, agent responsibilities overlap ad hoc, making cost and quality harder to reason about and control.

## Decision

Official workflow:

```
ChatGPT (Architecture)
  → Claude Code (Implementation)
  → ChatGPT (Review)
  → Hermes (Deployment)
  → ChatGPT (Final Audit)
```

## Consequences

- Hermes is limited to deployment and production verification — not architecture, implementation, or review — reducing the scope (and cost) of Hermes-driven work to the operations it is uniquely positioned for (VPS access).
- Claude Code's role is scoped to implementation within this workflow.

**Note on current practice:** this ADR formalizes the intended division of labor going forward. It does not describe how recent work in this project was actually produced — architecture and design proposals (including the Sprint 1C/1C.1 series and the Kyron7 Engineering Standard) were authored directly by Claude Code at the Founder's direction, not by ChatGPT, and Claude Code performed review of Hermes-produced work (the Foundation F1 package) rather than deployment-only work. This is recorded here as an observation, not a correction to the decision — the Founder may intend this ADR to govern future work from this point forward, in which case the practice should shift to match; if the intent was instead to describe workflow already in effect, that would be worth reconciling explicitly.
