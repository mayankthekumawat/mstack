# mstack

Agent Skills for real production work, beginning with a runtime-neutral pstack.

mstack collects skills that have earned a place in day-to-day engineering work. It starts with [pstack](./pstack/), created by [poteto](https://x.com/poteto), and replaces its runtime-specific interfaces with capability-based instructions that work across coding agents.

mstack is broader than pstack. pstack is the first collection, not the boundary. Future skills can cover deployment, incident response, access operations, maintenance, and other repeated work from production systems.

## How mstack differs from pstack

| | Original pstack | mstack |
|---|---|---|
| Purpose | One opinionated engineering stack | A home for pstack and other production skills |
| Runtime | Built as a Cursor plugin | Uses the Agent Skills format and capability-based instructions |
| Models | Can refer to runtime-specific model choices | Defaults to the current agent and supports optional workspace overrides |
| Runtime integrations | Runtime calls can appear inside the skills | Runtime-specific files live in isolated adapters |
| Growth | Extends the pstack workflow | Can add independent skills without folding them into pstack |

The port does not rewrite pstack's engineering principles, playbooks, or voice. It changes the parts that bind those instructions to one agent runtime.

## What belongs in mstack

A skill belongs here when it meets these conditions:

- It solves a repeated job from a real production system.
- It says when to run, what it may change, and what counts as done.
- Its core instructions do not depend on one agent's private tool names or model identifiers.
- It provides a direct way to verify the result.
- It credits any source material and keeps upstream authorship clear.

Read [the contribution guide](./CONTRIBUTING.md) before adding or adapting a skill.

## Collections

| Collection | What it contains | Status |
|---|---|---|
| [pstack](./pstack/) | Engineering workflows, review panels, verification tools, writing skills, and operating principles | Available |

New independent skills can live under `skills/`. Existing pstack work stays under `pstack/` so the source and its adaptations remain easy to audit.

| Independent skill | What it does |
|---|---|
| [agent-mcp-design](./skills/agent-mcp-design/) | Captures Mayank's priorities for agent autonomy, minimal context, progressive disclosure, clear failure tracing, and realistic regression checks. |
| [monthly-progress-report](./skills/monthly-progress-report/) | Builds a personal monthly report from work records and a previous report, checks claims against dated evidence, and renders a PDF with editable content. Includes an AI Cell format profile. |
| [margsarthi-test-questions](./skills/margsarthi-test-questions/) | Writes realistic MargSarthi test and demo questions from sanitized NHAI usage evidence, preserving natural wording and separating observed patterns from composed examples. |
| [librechat-native-first](./skills/librechat-native-first/) | Prefers supported LibreChat configuration and native behavior, verifies effective runtime semantics, and requires Mayank's scoped approval with a concrete lean-change assessment before code edits. |
| [suggest-a-skill](./skills/suggest-a-skill/) | Captures useful workflow discoveries and sends sanitized suggestions to Mayank's review thread for consultation before implementation or a PR. Includes a T3 delivery adapter. |

## Install skills

Install the directories you want from [`skills/`](./skills/) or [`pstack/skills/`](./pstack/skills/). You can also install the full collection.

- For Codex, copy each skill directory to `~/.codex/skills/`.
- For a workspace that follows the Agent Skills convention, copy them to `.agents/skills/`.
- For another agent, use that runtime's skill directory.

Start a new agent session if the runtime loads its skill registry only at startup.

To inspect or copy skills with Python, run this from the repository root:

```text
python scripts/sync-skills.py --destination ~/.codex/skills --skill monthly-progress-report
python scripts/sync-skills.py --destination ~/.codex/skills --skill monthly-progress-report --apply
```

Repeat `--destination` for multiple agent homes, or omit `--skill` to select both collections. The default prints a plan. `--apply` copies missing files, preserves unrelated skills, and skips any skill with conflicting local edits. Conflicts return exit code 2 and must be reconciled separately. The script does not delete files or create a background sync service.

Most pstack workflows start with `poteto-mode`. Individual skills such as `architect`, `interrogate`, `how`, `why`, and `tdd` can also run directly.

## Attribution

[pstack](https://github.com/cursor/plugins/tree/main/pstack) was created by [poteto](https://x.com/poteto). Its principles, playbooks, prompts, and voice remain his work.

The runtime-neutral modifications and the mstack repository are by [Mayank Kumawat](https://github.com/mayankthekumawat).

The included pstack collection retains its [MIT license](./pstack/LICENSE).
