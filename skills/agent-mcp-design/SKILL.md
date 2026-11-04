---
name: agent-mcp-design
description: "Design and review AI agents and MCP servers using the user's preferences for agent autonomy, native integrations, progressive discovery, grounded answers, and realistic regression checks. Use for agent or MCP engineering, not routine use of existing tools."
---

# Agent and MCP design

Build an environment in which the model can discover relevant information, choose useful tools, and solve the user's task. These are engineering defaults distilled from the author's recurring requests. Follow the current task's requirements and authorization when they differ.

## Establish the useful capability

Start with who will use the agent, the questions or actions they need, and the sources that can support them. Inspect real API responses, documents, data samples, and schemas before choosing tables or tools. Check what existing MCPs already expose and identify the additional capability a new integration earns.

Describe one realistic interaction from the user's request through discovery, tool calls, returned information, and the final answer or file. Use that interaction to assess the design. A connected endpoint alone does not show that the system is useful.

## Prefer native behavior and configuration

Inspect the actual deployed version, current upstream documentation, supported configuration, and stock behavior before adding custom code. In a FastMCP or LibreChat integration, first look for the framework's existing implementation of the required behavior. Check upstream fixes before maintaining a fork or copying a service into the application repository.

Prefer configuration and existing behaviors. When a demonstrated gap remains, make the smallest coherent code change and explain the gap it closes. Compare with a stock baseline when investigating whether a patch is still needed. Removing custom code must preserve the relevant user experience and answer quality.

Use native file upload, document understanding, managed search, sandbox, and structured-output capabilities when they meet the requirement. Attach metadata to the actual document during ingestion. Do not add OCR, conversion, splitting, local extraction, or a bespoke retrieval pipeline merely from habit. Verify one representative input first, then address any demonstrated capability limit and scale the working path.

## Give the agent schemas and room to reason

Expose purposeful, composable tools with authoritative contracts. Let the model choose relevant sources, filters, requests, and combinations. Consider schema discovery followed by request execution when it makes an API integration leaner and more flexible. The service still enforces its supported operations, permissions, and input contract.

Keep prompts concise. Give stable role and answer expectations in the base instructions, then return source-specific usage guidance with the relevant discovery result. Avoid adding a scripted route or a longer system prompt to compensate for every weak answer. First identify whether the problem is model reasoning, missing context, the tool contract, retrieval, or infrastructure.

Choose direct tools and programmatic tool calling deliberately, using supported runtime behavior. Avoid redundant exposure that adds context or ambiguity without a useful capability. Server-side retrieval intelligence is valid when it has a clear purpose; autonomy does not require removing every server-side model call.

## Reveal context progressively and truthfully

Start discovery with compact categories and descriptions. Return the selected source's schema, dimensions, definitions, filters, and instructions when needed. Avoid dumping every indicator, author, filter value, or full catalog into the initial context. Keep provider-internal identifiers behind the client-facing interface unless the caller actually needs them.

Preserve the source's real meaning: units, time periods, methodology, geography, definitions, and coverage. Do not invent dimensions or apply a filter outside its valid scope. Explain why a variable or source answers the question. Provide the metadata needed to verify the result without duplicating the same description across prompts and code.

## Make factual contracts deterministic

Use supported structured outputs and validation for required machine-readable shapes. Derive citation labels, document identity, dates, and other known facts from authoritative metadata or native runtime values. Do not ask the model to guess values the system already knows.

Use the framework's error contract and preserve useful validation feedback. An error must remain distinguishable from a successful empty result. Fix a broken tool or data contract before adding another tracing adapter or prompt workaround around its symptoms.

For private-data integrations, design the actual consent, identity, token-storage, refresh, and access boundaries using supported mechanisms. Preserve authorization across the complete workflow. Agent autonomy does not grant additional access or permission to take consequential actions.

## Ground answers and preserve human judgment

Make decision-support agents collect the relevant facts and resources, cite them, and help the person assess the available actions. Keep source statements, calculations, and inferred interpretation distinguishable. Avoid unsupported conclusions, claims of expertise, and recommendations that skip the evidence needed for the person's decision.

Verify that citations open the intended source and support the associated claim. Prefer useful document or passage references over a generic repository link. Add page anchors only when the system can verify them. Preserve the project's citation policy and the source metadata the reader needs.

## Test the real workflow and protect existing behavior

Use natural domain questions, representative documents, and real historical successes and failures. Include cross-tool workflows where users need them. Inspect the actual answer, returned data, citations, generated file, and download or follow-up behavior relevant to the change. Check the user interface when the change can affect it.

Prioritize regression coverage as well as the new capability. For a comparison or load replay, keep the relevant prompts, files, configuration, and concurrency comparable. Inspect tool traces to locate errors, wasted calls, and latency. Report quality, grounding, completed workflows, tool-call count, latency, cost, and resource use when relevant and observable. State sampling and coverage limits beside the result.

Separate model-quality problems from missing capabilities, data defects, and operational failures. Do not solve all of them by adding code or assume that a more capable model repairs a broken system. Choose checks proportional to the change and reuse existing evaluation, deployment, and synchronization mechanisms.

Deliver the requested design, implementation, or review with the native capabilities reused, remaining custom-code justification, user-visible behavior, and verification evidence. Historical provider choices, tool counts, budgets, review panels, and rollout approvals are examples, not permanent requirements or authority for the current task.
