---
name: principle-exhaust-the-design-space
description: Compare alternatives for a consequential UI or architecture choice with several viable approaches; skip choices already settled by constraints.
---

# Exhaust the Design Space

When a novel interaction or architectural decision has no established precedent, explore several concrete alternatives before implementation. Building the wrong thing costs more than exploring three options.

**The rule.** When a wrong choice would cause substantial rework, compare two or three viable approaches using the smallest useful sketches or prototypes. A familiar pattern or constraints that settle the choice do not need a competing prototype.

**When it applies:**
- Novel UI interactions (no prior art in the codebase)
- Architectural choices with multiple viable approaches
- Product design decisions where user experience depends on feel, not logic

**When it doesn't:**
- Mechanical implementation where the pattern is established
- Bug fixes or refactors with a clear target state
- Changes where constraints dictate a single viable approach
