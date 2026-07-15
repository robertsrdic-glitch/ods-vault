# Collaboration Rules

Status: Approved

---

## NorthStar Workflow Standards

### Claude Packages

Whenever possible, execute work from a complete Claude Package.

A Claude Package contains:

- Task instructions
- Destination
- Complete document content
- Validation requirements

Avoid multi-step workflows when a single package can safely complete the task.

---

### Vault Integrity

After every completed task:

- validate internal wiki links
- repair safe references automatically
- report every repaired reference
- never silently change document content

---

### Quality Guardian

Before finishing any task, perform a quality review.

Check for:

- duplicated documentation
- conflicting documentation
- broken links
- incorrect document location
- naming inconsistencies
- architecture inconsistencies

Never silently fix architectural decisions.

Report them instead.

---

### Decision Safety

If multiple valid interpretations exist:

Stop.

Ask the Founder.

Never guess.

---

### Reporting

Every completed task should include:

- Files created
- Files modified
- Files renamed
- Links repaired
- Validation results
- Open issues (if any)

---

### Documentation First

Documentation is the primary source of truth.

Implementation follows documentation.

Never create implementation that contradicts approved documentation.

---

### Long-Term Thinking

Optimize for a vault that remains understandable after hundreds of documents.

Prefer consistency over speed.

Prefer maintainability over convenience.
