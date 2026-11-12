# Worked decisions and approval example

## Historical grounding

Read on 2026-11-12: [Marg Sarthi stack PR #174](https://github.com/NHAI-AI-Cell/margsarthi-prod-stack/pull/174), head `f4dc61180db73e1d6d410fe6be07c17a8fcff984`. The PR was open and described a candidate release, not a completed application deployment. Recheck its current head and deployment evidence before treating any behavior as live.

The candidate used explicit native selection of five audited skills, native shared-skill activation with explicit user opt-outs preserved, removal of an effective model profile plus native endpoint tombstones, and the existing 50-step graph budget. These illustrate routes to investigate, not constants to copy into another project.

Custom changes remained in a deployment reconciler and a small newest-image lookup. Those remain code changes under this skill even when they orchestrate native configuration or change only one line. In particular, selecting a newer file reference must preserve ownership authorization. Fewer lines do not justify losing that check.

## Native behavior is version-specific

The [official Admin Panel documentation](https://www.librechat.ai/docs/configuration/admin_panel) describes persisted configuration profiles and their merging and validation. The [interface documentation](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface) describes role-permission side effects and shared-skill activation. Both were consulted on 2026-11-12 and displayed development-version documentation. Check the deployed tag's schema and implementation before using a field or assuming those semantics.

Suppose the request is to disable an optional profile. Hiding its picker entry may leave direct requests possible. Inspect the effective model specification, endpoint resolution, persisted overrides, and native enforcement in the actual pin. Where supported, remove the profile and apply the native endpoint deletion mechanism in the correct configuration layer. Verify authenticated direct requests are denied while permitted profiles still work. A custom middleware block is not the default solution.

Suppose an imported shared skill is visible but inactive. Inspect sharing permissions, recipient activation, role settings, explicit opt-outs, and the pin's native activation default. A setting that activates shared skills more broadly may affect unrelated skill-enabled profiles. Verify that scope before changing it. If implementing the setting requires editing a reconciler, propose that code change and obtain approval first.

## A concrete lean-change proposal

This is an invented proposal format, not permission to implement it:

> The pinned runtime already supports the desired endpoint deletion. Our deployment helper does not retain that state during reconciliation. Changing only YAML would therefore be ineffective. The checked upgrade candidate does not remove this local helper gap; waiting upstream would not change our helper either.
>
> I propose changing the helper's reconciliation, backup, and restore functions and their existing tests. The estimate is 20-40 changed lines across two files, subject to confirming the exact call sites. This adds no service or dependency, but changes persisted configuration handling on enable, disable, and rollback. It affects every user who inherits the optional endpoint's settings, so the small diff has a broad access effect.
>
> Verification will use the pinned runtime's configuration resolution and endpoint enforcement, permitted and denied ordinary-user requests, concurrent-state refusal, and rollback that restores only the helper-owned state. The helper remains our maintenance responsibility on future schema upgrades. If these requirements cannot fit the estimate, I will revise the proposal before expanding the change.
>
> Mayank, do you approve this helper change within that scope?

Use actual findings and file/function names in a real proposal. The estimate above is illustrative. Do not implement the patch while waiting for approval, and do not weaken the backup or authorization behavior to meet an estimate.

## Trigger and boundary review cases

| Request or finding | Intended behavior |
|---|---|
| Configure a LibreChat endpoint in another project's deployment. | Apply this skill. Inspect the pin and effective native settings; configuration-only changes follow existing authorization. |
| Troubleshoot a feature that stayed enabled after editing YAML. | Apply this skill. Inspect persisted overrides, role state, schema behavior, refresh, and actual server requests. |
| Investigate an integration outside the LibreChat source tree. | Apply this skill. Integration and deployment code still require scoped approval. |
| Fix a bug with a one-line monkeypatch or newest-file lookup. | Investigate native and upstream alternatives, present concrete leanness facts, and wait for approval before writing the patch. |
| A newer upstream release contains a possible fix. | Assess and verify the candidate; do not automatically upgrade or bundle custom code into it. |
| Mayank approved one named helper function, and another middleware change now seems useful. | Implement only the approved scope. Propose the middleware separately before changing it. |
| A request is denied correctly in the UI but succeeds through a direct endpoint request. | UI hiding is insufficient. Investigate native server enforcement before proposing custom authorization. |
| Mayank asks for this reusable skill or another documentation-only update. | Write and validate the authorized documentation. Do not invoke the future application-code approval rule to block it. |
| Draft a letter using LibreChat as an end user. | Outside this engineering skill's trigger; use the relevant content workflow. |
