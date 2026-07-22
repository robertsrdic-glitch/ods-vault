# Care Circle Product Foundation

Document status: Founder Approved — local ODS commit authorized; ODS push and live verification pending
Source decision status: Approved

## Vision

Care Circle is a calm, privacy-first, local-first medication organizer for individuals, families and caregivers.

Its purpose is organization — not diagnosis, treatment advice or verification that medication was actually taken.

> A simple way to organize medications for yourself and the people you care for.

## Product category

Care Circle is an organizational tool. It is not:

- a medical advisor;
- a diagnostic tool;
- a medication interaction checker;
- proof that a medicine was actually swallowed;
- a replacement for a doctor or pharmacist.

## Product principles

- Reliability before Features
- Simplicity First
- Local First
- Family and Caregiver First
- Human Confirmation
- Calm Design
- Privacy First
- One screen, one question
- No scope creep

See [[Navigation Accessibility and Simplicity]] for the permanent UX rule these principles anchor.

## Primary users

- caregivers;
- families;
- older adults;
- people managing medication for multiple people;
- individuals taking multiple medicines.

## Caregiver model

The person using the phone and the person taking the medicine may be different.

A profile may represent:

- the device owner;
- a parent;
- a child;
- a partner;
- a relative;
- a friend;
- another cared-for person.

A caregiver-managed profile may exist even when the represented person never uses the application.

## First markets and languages

- Slovenia
- Croatia

Languages: Slovenian, Croatian, English.

## Core product model

Therapies generate Medication Events. The Today screen is centered on today's Medication Events — not on a medicine catalogue.

See [[Care Circle Domain Model Overview]] for the full entity model.

## Product promise

> Know what needs attention today, without unnecessary complexity.

## Technical direction (summary)

- React Native + TypeScript
- Expo Development Build and Expo Router
- encrypted SQLite with SQLCipher
- domain-driven Medication Event engine
- replaceable Android/iOS notification adapters
- local-first, no server

See [[Care Circle Architecture Overview]] for full technical detail.

---

**Source repository:** https://github.com/robertsrdic-glitch/care-circle.git
**Source path:** README.md; docs/product/PRODUCT-001-Product-Definition.md
**Source commit or commit range:** 99e9d9c52865d0d736af765702f514637133caed
**Consolidated on:** 2026-07-22
**Canonical ODS status:** Founder Approved — local ODS commit authorized; ODS push and live verification pending (source decision status: Approved)
**Notes:** Structured consolidation of README.md (project summary) and PRODUCT-001 (Approved 2026-07-21), merged and reorganized under new section headers. All material content from both sources is represented and no decision was reinterpreted, but this is not a verbatim/full copy of either source.
