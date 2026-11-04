---
name: principle-redesign-from-first-principles
description: Reconsider a design when new requirements expose repeated structural workarounds. Preserve the existing structure for changes that fit it.
---

# Redesign From First Principles

When repeated workarounds show that a new requirement does not fit the design, reconsider the structure as if that requirement had been known from the start. Keep a local addition local when the existing design accommodates it.

- Read the affected implementation and understand the relevant design
- Ask: "if we were writing this from scratch with this new requirement, what would we build?"
- Propagate the change through every reference: types, docs, examples, rationale sections
- Think about the redesign holistically, then deliver it incrementally

This is the method for preserving option value when integrating changes into an existing design.
