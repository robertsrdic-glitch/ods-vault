# AI Context Pack Generator

Version: 1.0
Status: Draft
Category: Foundation
Owner: Founder
Related Documents:
- [[NorthStar Constitution]]
- [[NorthStar Brand DNA]]
- [[Product Bible]]
- [[Design Bible]]
- [[Design Foundation Specification]]

---

# Purpose

NorthStar documentation is the single source of truth.

AI systems should never read the entire documentation directly.

Instead,

specialized Context Packs are generated from the documentation.

---

# Context Packs

The following Context Packs exist:

## Design Context Pack

Audience:

- Claude Design
- Figma AI
- UX Designers

Includes:

- Brand DNA
- Design Bible
- Design Foundation Specification

Excludes:

- Engineering
- Backend
- Architecture

---

## Development Context Pack

Audience:

- Claude Code
- Codex
- Cursor
- Windsurf

Includes:

- Product Bible
- Engineering
- API
- Architecture
- Product Specifications

Excludes:

- Design philosophy
- Visual identity

---

## AI Behavior Context Pack

Audience:

- NorthStar AI
- Future AI Assistants

Includes:

- AI Response Specification
- AI Conversation Specification
- Trust Engine
- Product Bible

Excludes:

- UI implementation
- Technical implementation

---

# Generation Rules

Every Context Pack must:

- contain only relevant information
- remove duplicate content
- preserve original meaning
- never invent information
- always reference the latest approved documentation

---

# Updating

Whenever the source documentation changes,

Context Packs should be regenerated.

They are derived documents.

The source documentation always has priority.

---

# Rule

AI systems should consume Context Packs,

not raw project documentation.

This reduces ambiguity,

improves consistency,

and minimizes unnecessary context.

---

# Success

Every AI receives exactly the knowledge required for its role,

and nothing more.
