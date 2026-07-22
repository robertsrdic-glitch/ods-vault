# Navigation, Accessibility and Simplicity

Document status: Approved
Source decision status: Approved

## Permanent UX rule

The application must be as simple as possible and avoid unnecessary complexity because users may include patients and older people.

Simplicity, clarity, large elements, few steps and low cognitive load take priority over extra options.

## UX-P04 — Simplicity First

Care Circle must remain usable for patients, older adults and people with limited technical confidence.

Rules:

- one main question per screen;
- one clearly dominant action;
- large text and touch targets;
- short, ordinary language;
- no hidden critical gestures;
- no unnecessary settings;
- no medical jargon where plain language works;
- status is never communicated by color alone;
- common actions are fast;
- errors preserve entered data;
- progressive disclosure instead of crowded screens;
- safe defaults instead of mandatory configuration.

When additional flexibility conflicts with clarity in the MVP, clarity wins.

## Approved navigation

1. Today
2. People
3. Medicines
4. Settings

Exactly four destinations, in this order, as implemented in [[WP-02 Application Shell and Navigation Foundation]] and confirmed unchanged through [[WP-04 Encrypted SQLite Bootstrap and Key Management]].

No hamburger menu. Back behavior follows platform conventions. Unsaved work is protected. Important actions are never available only through hidden gestures. Cards have large clickable areas. Primary actions are placed within easy reach.

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** docs/ux/UX-P04-Simplicity-First.md; docs/ux/UX-012-Navigation-and-Global-Interaction.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Approved (source decision status: Approved)
**Notes:** Structured consolidation: UX-P04's rule list (Approved 2026-07-21) is reproduced verbatim, combined in one document with the navigation rules drawn from UX-012. Combining two separate sources into one document is the reason for the "Structured consolidation" treatment recorded in the Source Register, even though neither source's own wording was shortened. This is the permanent, cross-cutting simplicity rule referenced throughout the Care Circle ODS documentation.
