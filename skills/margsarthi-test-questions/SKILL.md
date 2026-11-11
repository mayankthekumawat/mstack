---
name: margsarthi-test-questions
description: "Create or review realistic MargSarthi test and demo questions using sanitized evidence of how NHAI users ask for help. Use for user-like question sets, demo scripts, or test-input wording. Does not run tests, answer the questions, or create live datasets."
---

# MargSarthi test questions

Produce questions an NHAI user could naturally type into MargSarthi. Start with [the sanitized findings and composed examples](references/usage-evidence.md). Incorporate newer authorized evidence when available.

## Establish the evidence and intended use

Establish the requested purpose, count, scope, and available fixtures or conversation context.

Use supplied sanitized findings or an authorized, bounded read-only review. Record its dates, selection, and limits. Separate genuine user messages from tests, assistant text, and suggestions. Convenience samples do not establish population prevalence. Topic-enriched samples support wording within selected topics, not their frequency across users.

Disclose stale or missing evidence. Wait if fresh findings are required. Discover approved access methods locally; do not hard-code worktree paths or treat failed tracing access as usage evidence.

## Preserve how the person asks

Keep relevant NHAI, PIU, RO, IE, and O&M abbreviations. Preserve project mode, agreement context, short topic fragments, and ordinary drafting or circular requests. Do not expand every acronym or turn a brief query into a compound benchmark instruction.

Preserve natural language variation. Do not require lowercase, bad grammar, missing punctuation, or a fixed length. Do not add random typos, Hindi, or jargon to manufacture authenticity.

Keep follow-ups with their necessary prior turns. Omit context deliberately for clarification tests; supply an authorized fixture for completion tests. Do not silently make a follow-up standalone.

## Keep the task independent of feature routing

Write the user's task. Keep internal tools, feature targets, routing expectations, evaluation criteria, and presenter notes outside the input.

Do not insert video, recording, training, or session hints merely to trigger a feature. Do not request policy plus video by default. Include those details when the task requires them, such as a discovery test.

Keep cases added solely for feature coverage separate. Ground them in a plausible task and label the evidence gap.

## Label provenance and keep fixtures separate

Label each item:

- `sanitized-observed`: source wording with documented privacy substitutions, approved for the intended destination. A pattern summary is not an observed question.
- `composed-from-pattern`: new wording, a paraphrase, or a combined scenario based on an observed pattern. Name that basis; do not call it a real user quote.
- `coverage-only`: a new case for a requested capability or gap without supporting usage evidence. State why it is included.

Separate the input from its label, evidence basis, fixture or prior-turn dependency, and proposed check. Use a compact table or the requested format.

Keep question wording, expected capabilities, and reviewed expected answers separate. Retrieval success or a model answer does not establish policy ground truth. Identify the source needed to check correctness, including whether a cited statement comes from an agreement, circular, or training explanation.

## Check the set before delivery

Compare inputs with their evidence. Remove gratuitous constraints, polished benchmark phrasing, invented language habits, feature hints, and near-duplicates.

Check context against the case's purpose. Distinguish authored questions from executed tests.

Keep raw chats, personal data, account IDs, real project identifiers, credentials, private trace links, and re-identification mappings out of public files and PRs. Publish approved sanitized findings and composed examples. Record necessary substitutions in fixture notes.

Deliver the questions, provenance, dependencies, and material limits. Production writes, test execution, live dataset creation, upload, and skill installation require separate authorization.
