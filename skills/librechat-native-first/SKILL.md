---
name: librechat-native-first
description: "Use for LibreChat engineering, configuration, integration, troubleshooting, and upgrade work in any project or fork. Prefer supported native configuration and built-in behavior. Verify the pinned runtime and effective settings, and obtain Mayank's approval before application, integration, helper, or deployment code changes."
---

# LibreChat native first

Prefer supported native configuration and built-in behavior. Treat custom code as an exception after investigating native routes. Apply this preference across projects, including work on integrations or deployment helpers outside the LibreChat source tree.

## Approval boundary for code

Before implementing any new LibreChat application or integration code change, explain the concrete proposed change, assess how lean it is, and ask Mayank for approval. This includes a one-line runtime patch, monkeypatch, fork edit, helper or deployment-script change, and custom middleware. There is no exemption for tiny, safe, temporary, or reversible code changes. Executable logic embedded in configuration is code too.

Do not write or apply an implementation, including a temporary runtime workaround, before approval. Read-only investigation, inspection of upstream code, existing authorized checks, and preparing a reviewable proposal may continue. Identify this skill as the reason for the approval request.

Carry approval forward only within the specifically approved scope. A broad request to fix or upgrade LibreChat does not authorize an unspecified custom patch. Do not ask again for the same specifically approved change; ask before materially expanding it.

Routine configuration-only work follows the task's existing authorization and deployment boundaries. This code-approval rule does not block already authorized skill documentation or other documentation-only work.

## Inspect what actually runs

Confirm the intended environment and available read permissions. Record the exact installed image tag and digest or source commit, application/package versions, and relevant fork patches. A YAML configuration version is not the application version.

Trace the effective settings through environment variables, mounted files, persisted Base and principal overrides, role permissions, user preferences, startup seeding, and configuration caches as applicable. Inspect schema validation, merge order, array selection, deletion or tombstone behavior, and refresh semantics in the pinned runtime. Do not assume editing `librechat.yaml` controls the resulting application.

Reproduce the problem within authorized scope and distinguish configuration, access, provider, and capacity failures from code defects. If the runtime or effective state is unavailable, state what remains unverified rather than assuming custom code is necessary.

## Exhaust native routes before custom code

Check the relevant [official documentation](https://www.librechat.ai/docs/configuration), [upstream releases](https://github.com/LibreChat-AI/LibreChat/releases), and [open and fixed issues](https://github.com/LibreChat-AI/LibreChat/issues). Look for a supported setting, existing feature or enforcement path, known regression, or upstream fix. Match the findings to the installed version and source; current development documentation may describe behavior absent from the pin. A closed issue alone does not prove its fix shipped in that version.

Distinguish the practical options:

- Existing supported configuration or built-in behavior: first preference; identify the effective layer to change and how to prove the result.
- Upstream upgrade: assess the specific fix, compatibility, migrations, regression coverage, and rollback. It is a candidate, not an automatic action or justification for a larger change.
- Wait or report upstream: explain the operational cost and any supported interim configuration. Draft a report if useful; submit it only when authorized.
- Custom code: explain the demonstrated gap and smallest viable solution, then obtain the scoped approval before implementation.

## Explain how lean the proposal is

Make the code proposal concrete enough to approve. Include:

- Why supported configuration and the checked upstream options do not meet the requirement.
- The smallest viable change, affected files and functions, and estimated changed lines where useful. Label estimates and unknowns.
- Whether it adds a runtime patch, dependency, service, or persistent state, and who maintains it.
- Blast radius across users, endpoints, roles, files, integrations, and startup or deployment paths as relevant. Explain when a tiny diff has a wide effect.
- Upgrade and maintenance burden, including patch removal or conflicts with upstream changes.
- Verification against the pinned runtime, ownership and authorization checks, and a scoped rollback that preserves unrelated state.

Then ask Mayank to approve that scope and wait for the answer. An invented leanness score cannot replace these facts. See [the worked decisions and approval example](references/decisions.md) when preparing the proposal.

## Prove the effective behavior

Exercise the real pinned runtime. A parsed or schema-ignored field and a hidden picker option do not prove a server-side disable. Check the resolved configuration and relevant authenticated requests, including affected ordinary users, existing sessions, permitted paths, and denied paths. Use an existing native enforcement path before proposing new authorization logic.

Verify skill selection, shared activation, explicit user opt-outs, and ownership checks when affected. Preserve existing operating budgets unless a separately justified change is authorized. Runtime mocks and green health checks are useful but do not establish connected persistence, cache propagation, provider access, or real-user behavior.

Keep backups and rollback scoped to the state the change owns. Do not remove correctness, ownership checks, conflict detection, or rollback safety to reduce line count. If an environment changes, update its existing runbook with dated results and recheck commands.

Deliver the selected route, any approved code scope, actual verification, remaining limits, and rollback information. Keep historical examples separate from current deployment facts.
