# Release Management

Version: 1.0
Status: Draft
Owner: Founder
Related Documents:
- [[AI Product OS Constitution]]
- [[Operating Model]]
- [[Request for Change (RFC) Process]]
- [[Repository Standard]]
- [[CHANGELOG]]

---

# Purpose

Defines how the AI Product OS itself is versioned, released, and evolved over time. This is operating system governance, not software release management — it governs when the collective state of the repository's own documentation is declared a stable, referenceable version, not when any product built on the OS ships code.

---

# Release Philosophy

The AI Product OS advances in deliberate, recorded steps rather than continuous informal drift. A release is a declaration that a known set of documents, in a known state, is stable enough to build on and reference by name. Every release is reproducible from repository history alone, and every change it contains traces back to an approved RFC where one was required.

---

# Versioning Model

Versions follow a `MAJOR.MINOR` pattern at the level of the AI Product OS as a whole (for example, `v0.1`, `v1.0`).

- **MAJOR** increments when a Foundation Document changes in a way that alters governance, roles, or the operating model itself, or when the OS reaches a new stage of structural maturity (e.g. Foundation complete).
- **MINOR** increments when supporting documentation, templates, or workflow documents are added, clarified, or extended without altering governance itself.

Individual documents also carry their own `Version` metadata field, independent of the overall OS version. A document's own version increments whenever its content changes; the OS version increments only at a declared release.

---

# Release Types

## Foundation Releases

Mark the completion or consolidation of the core governance layer itself — Constitution, Operating Model, Organization Charter, Repository Standard, and the roles and processes that depend directly on them. A Foundation Release is a MAJOR-class event.

## Minor Releases

Add or refine supporting documentation — templates, workflow index entries, role contracts — without changing governance, ownership, or the operating model. Minor Releases do not require an RFC unless they touch a Foundation Document.

## Major Releases

Introduce or change governance itself: new decision authority, new Foundation Documents, or structural changes to how roles or the Operating Model function. A Major Release always requires at least one approved RFC.

---

# Release Approval Process

1. A release is proposed by the Founder or by a role with a documented recommendation accepted by the Founder.
2. Every change included in the release is checked against the Repository Standard and, for any Foundation Document change, against an approved RFC.
3. The Founder approves the release as a whole, recording its version, title, and status in the CHANGELOG.
4. Approval of a release does not retroactively approve any individual change that lacked its own required review or RFC — each change must already have been properly approved before the release can include it.

---

# Compatibility Policy

Documents referencing a released version of the AI Product OS should specify which version they were written against. A Minor Release does not break compatibility with documents written against an earlier release within the same MAJOR version. A Major Release may introduce breaking changes to governance and must state them explicitly in the CHANGELOG.

---

# Deprecation Policy

No document is deleted when superseded. A deprecated document is moved to `99 Archive`, retains its original content, and is marked with the version and release in which it was superseded. Documents that reference a deprecated document are updated to point to its replacement as part of the same release.

---

# Migration Policy

Where a release changes governance in a way that affects existing product-level work (such as NorthStar), the release notes in the CHANGELOG state what, if anything, downstream products must do to remain consistent with the new release. Where no action is required, this is stated explicitly rather than left silent.

---

# Release Validation

Before a release is recorded as Released, the following are confirmed:

- All wikilinks across the repository resolve.
- No governance content is duplicated across documents.
- Every Foundation Document change included in the release traces to an approved RFC.
- The CHANGELOG entry accurately reflects the repository's actual state at release time.

---

# Definition of Done

A release is Done when every document it includes is in Approved or intentionally-Draft state as declared, every required RFC is closed, and the CHANGELOG entry has been written and validated.

---

# Definition of Release

A release exists, organizationally, only once it is recorded in the CHANGELOG with a version, status, and title. An undocumented release did not happen.

---

# Rules

- Only approved changes may enter a release.
- Every release must be reproducible.
- Every release must be traceable.
- Every release must reference approved RFCs.
- No release may modify frozen documents without an approved RFC.
