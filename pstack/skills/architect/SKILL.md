---
name: architect
description: Design module boundaries and contracts for consequential architectural changes or explicit architecture requests. Skip routine fixes and configuration changes.
---

# Architect

Resolve the structural choice before implementation. Scale the sketch to the task: caller usage and the important types, signatures or module boundaries are usually enough.

## Ground

Read the affected implementation and trace the relevant behavior. Use `how` or `why` when the flow or rationale is genuinely unclear; do not require a separate subsystem report for an already-understood change.

## Sketch and choose

Write the caller's usage first, then the contracts that make it work. For a consequential unresolved choice, compare the smallest useful sketches of viable alternatives. If constraints determine one approach, proceed with it.

Use `arena` when parallel candidates are requested or would resolve a concrete uncertainty worth their cost, and delegation is permitted by the active runtime and task. It is not a mandatory step for every architecture task. When using runners, use `architect runners` from `.pstack/models.yaml` when configured and `inherit-parent` for missing entries. Honor explicitly requested models and candidate counts.

Use [design-red-flags.md](references/design-red-flags.md) when reviewing module boundaries. Prefer an interface that hides useful complexity without spreading coordination across callers. Use [rationale-template.md](references/rationale-template.md) when a durable design rationale helps the reviewer; a small sketch does not need a separate package.

For an authorized arena run, pass [runner-prompt.md](references/runner-prompt.md) with the task, relevant grounding, and an isolated output location to each candidate.

## Implement within the requested scope

If the user requested a design only or a checkpoint, stop at the reviewable sketch. Otherwise implement within the existing authorization.

Treat deviations as evidence: correct the sketch when a real requirement was missed, and avoid adding abstractions merely to preserve it. Revisit the architecture when repeated workarounds show that its shape is wrong. An isolated edge case does not require a redesign or another arena run.

Deliver the implementation or design requested, with the contracts, material tradeoffs and verification needed to assess it.
