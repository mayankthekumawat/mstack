---
name: agent-mcp-design
description: "Design and review AI agents and MCP servers for agent autonomy, minimal context, progressive disclosure, and clear failure tracing. Use for agent or MCP engineering, not routine use of existing tools."
---

# Agent and MCP design

Optimize for two primary goals:

- **Agent autonomy.** Give the agent enough flexibility to discover information, choose tools, compose requests, and solve the task without fighting the MCP or architecture.
- **Context efficiency.** Ruthlessly remove redundant instructions, tool descriptions, schemas, and output. Keep as few instructions as will reliably do the job.

Progressive disclosure is central to the architecture. Reveal what the agent needs when it needs it. Clear observability supplies the feedback needed to diagnose failures and improve both goals. Follow the current task's requirements and authorization.

## Establish the useful capability

Identify the user, their actual questions or actions, and the sources that support them. Inspect real API responses, documents, data samples, and schemas. Check existing MCPs before building another. Describe one realistic interaction through discovery, tool calls, returned information, and the final answer or file.

## Prefer native behavior and lean integration

Check the deployed version, current upstream documentation, supported configuration, and stock behavior before adding code. Prefer native framework capabilities and configuration. Check upstream fixes before maintaining a fork. A demonstrated gap can justify a small coherent change. Removing custom code must preserve the user experience and answer quality.

Use native file handling, document understanding, managed search, sandboxes, and structured outputs when they meet the requirement. Attach metadata to the actual document. Verify a representative input before adding preprocessing or scaling ingestion. Do not freeze historical provider choices into permanent requirements.

## Give the agent room to reason

Expose purposeful, composable tools with authoritative contracts. Let the agent choose relevant sources, filters, requests, and combinations within the supported operations and authorization. Consider schema discovery followed by request execution when it makes an integration more flexible. Avoid forcing every task through a rigid path or adding a tool for every anticipated question.

Keep stable role expectations concise. Return source-specific guidance with the relevant discovery result. Choose direct tools and programmatic tool calling deliberately, avoiding redundant exposure. Server-side retrieval intelligence is useful when it has a clear purpose. Diagnose weak answers before adding more instructions or routing code.

## Make progressive disclosure the default

Start with compact capabilities or categories. Reveal the selected source's schema, definitions, filters, and instructions only when needed. Avoid initial catalog dumps and repeating guidance across the system prompt, tool descriptions, and results. Inspect what the model actually receives, including large payloads and duplicated discovery calls.

Cut context without losing meaning. Preserve relevant units, periods, methodology, geography, and source coverage. Do not invent dimensions or apply filters outside their scope. Return only the data and metadata needed for the next decision or a verifiable answer. Keep provider-internal identifiers behind the interface unless the caller needs them.

## Keep known facts and access deterministic

Use supported structured outputs and validation for machine-readable contracts. Derive citation labels, document identity, and dates from authoritative metadata or native runtime values. Keep source statements, calculations, and inferred interpretation distinguishable. For decision support, gather grounded facts and useful citations so the person can make the consequential judgment.

Use supported consent, identity, token-storage, refresh, and access mechanisms for private data. Autonomy does not broaden permission. Use the framework's error contract and preserve useful validation details. Failed operations must remain distinguishable from successful empty results.

## Make failures easy to find and explain

Design observability with the system. Prefer supported tracing, such as Langfuse, that connects a user request to model calls, tool calls, retrieval or execution steps, and the final outcome. Make the failed step, error, timing, and relevant request context easy to inspect. Capture enough bounded diagnostic detail to explain the failure, with appropriate privacy controls.

Verify the failure path: a controlled tool or model failure must appear as a failure in the trace and be easy to locate. Check whether the agent recovered and whether the user actually received a usable result. Healthy endpoints or installed instrumentation alone do not establish workflow success.

Use failed traces to iterate. Distinguish model reasoning, missing context, tool contracts, data or retrieval defects, and infrastructure failures. Fix the responsible layer, retain representative failures as regression cases, and compare subsequent traces. Prefer changes that preserve autonomy and remove unnecessary context.

## Verify the complete experience and existing behavior

Use natural questions, representative documents, and historical successes and failures. Exercise cross-tool workflows where needed. Inspect actual answers, data, citations, files, downloads, and follow-up behavior. Check the UI when affected. Citations must open the intended source and support the claim. Use page anchors only when verified.

Prioritize regressions alongside new capabilities. Keep prompts, files, configuration, and concurrency comparable when comparing versions. Inspect actual context, tool traces, quality, grounding, latency, tool-call count, cost, and resources as relevant. State coverage limits and distinguish model-quality issues from systemic defects.

Reuse existing verification and delivery mechanisms. Deliver the requested result with evidence of agent flexibility, context economy, visible failures, and preserved behavior. Historical tool counts, budgets, review panels, and rollout approvals do not govern a new task.
