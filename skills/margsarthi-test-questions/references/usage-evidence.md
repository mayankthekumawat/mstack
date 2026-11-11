# Sanitized usage evidence

Findings supplied on 2026-11-11 from a bounded read-only review of production LibreChat messages. Queries and text processing stayed inside the existing application container. No raw chats, identities, message IDs, or conversation IDs were exported. This reference records aggregate findings and newly composed examples, not a production transcript.

## Sample and limits

The broad sample covered 28 October through 11 November 2026 UTC. Four query windows were used: 28 October-1 November, 1-5 November, 5-8 November, and 8-12 November. The last window was bounded by the review date. Each query considered at most 800 candidate messages and retained at most 60 qualifying distinct conversations per window.

The retained sample contained 240 messages from 162 distinct regular users: 85 initial turns and 155 later turns. Admin, test, and synthetic identities, greetings, very short acknowledgments, and duplicates were excluded. This is a recent convenience sample, not a random or population-representative sample. Exclusions also limit what it says about very short conversational replies.

Median length was 12 words, with a 25th-75th percentile range of 6-29. Nineteen messages contained a question mark, and 115 began lowercase. These describe this selection; they are not targets for generated questions.

Literal cue counts were: `please` 44, `as per` 35, `circular` 39, `draft` 31, `prepare` 23, and `provision` 14. Abbreviation counts included NHAI 41, PIU 26, RO 17, and IE 11. These overlapping substring or token features are not precise intent classifications or quotas.

A separate topic-enriched sample contained 80 messages selected around arbitration, maintenance, concession, and pavement. It included `as per` 28, `circular` 35, `please` 18, concession-topic hits 20, maintenance 25, IE 11, and O&M 8. Use it to support language and examples within those topics. It cannot establish their prevalence across production usage and must not be pooled with the broad sample to claim that prevalence.

The reviewer attempted Langfuse observations through an approved official-CLI tunnel helper, but SSH credential access failed. They also reported a metadata-only tracing policy for the source application. The evidence here therefore comes from the authenticated read-only chat database, not Langfuse observations. No live dataset was created. Future access should use the current environment's approved tooling, without assuming a machine-specific path or that tracing contains user text.

## What the findings support

Short topic fragments and ordinary drafting or circular requests are useful starting points. Preserve the NHAI user's relevant project mode, agreement context, and acronyms. Later turns can depend on earlier context. Do not turn every request into a standalone, polished, multi-part benchmark question.

The sample does not establish that all users write briefly, lowercase, or imperfectly. It does not establish which answers are correct, which features work, or how users would phrase a request for an unobserved feature.

## Newly composed examples

Every input below is `composed-from-pattern`, not a verbatim production query. The first was supplied with the sanitized findings; the remaining examples were composed for this skill. Their fixture notes and checks are authoring guidance, not observed outcomes or verified gold answers.

| Input | Evidence basis | Fixture or context and proposed check |
|---|---|---|
| `concessionaire not attending potholes in BOT project. what action can PIU take as per agreement` | Supplied synthetic candidate reflecting concession and maintenance topics, PIU, project mode, and `as per` wording. | Provide an authorized BOT agreement fixture for an answer test. Keep its version and relevant documents in fixture notes. Check whether the answer grounds action in the applicable agreement or asks for missing context. For capacity-building coverage, record the feature under test in metadata without adding a session or video hint to the input. |
| `draft letter to concessionaire for poor maintenance` | Drafting cues in the broad sample and maintenance/concession wording in the enriched sample. | Provide a fictional issue record and the applicable agreement for a completed-letter test. Otherwise assess whether missing facts are identified. Do not invent a real project or add a legal conclusion. |
| `NHAI circular on O&M` | Topic-fragment style, circular requests, NHAI, and O&M. | Supply a controlled circular collection. Check relevant retrieval or clarification of the intended issue. Do not silently add a request for a video or training session. |
| `what is role of IE in BOT project` | IE usage and concession context; BOT is retained from the supplied synthetic scenario. The exact task is newly composed. | Use the relevant agreement fixture. Check whether the response keeps the project mode and distinguishes documented duties from assumptions. |

A newly composed two-turn case can start with the pothole question above, followed by `draft letter`. Label both turns `composed-from-pattern`. The second turn requires the earlier issue, the preceding assistant response, and the same fixture context. Drafting cues and the presence of later turns support the construction; this sequence was not observed or measured as a production workflow.

For a requested media-discovery test, compose a separate `coverage-only` case if no usage evidence supports that request. Explicit media wording then belongs to the discovery task. State that this is coverage design rather than an observed user pattern. Do not rewrite the general pothole question to spoon-feed a known session name or demand policy plus video.

## Reported staging check of the synthetic candidate

On 2026-11-11, the reviewer reported testing the exact synthetic pothole/BOT question above against staging document retrieval. It retrieved four PDF sources and a relevant BOT capacity-building session at 36:31, with no native citation warnings. This supports using an ordinary work question to test relevant session retrieval without a video or session hint. It does not make the wording an observed production query or establish a guarantee for another corpus or deployment.

The generated answer also treated a figure from the training session as an updated contractual provision. That answer-attribution issue is separate from question realism. Absence of citation warnings does not validate the claim. Keep the retrieved material as evidence for a retrieval check; do not use the generated answer as a gold label. A reviewed policy answer would need authoritative agreement or circular support and correct attribution of training commentary.
