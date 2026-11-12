# T3 suggestion delivery

This adapter routes suggestions to the existing review thread selected by Mayank. It does not create threads, run delegates, or authorize implementation of a suggested skill.

## Destination

Verified by reading the thread on 2026-11-12:

<t3-thread://v2/01523451-db68-4495-97d6-d6ff9e278720/cd39c506-13f0-4fd4-8f76-6c53cea1a7ed>

- Environment ID: `01523451-db68-4495-97d6-d6ff9e278720`.
- Thread ID: `cd39c506-13f0-4fd4-8f76-6c53cea1a7ed`.
- Project ID: `e72a0329-4c98-4546-b401-30f7ada0ca41`.

The thread title can change. Use the identifiers, then verify the returned link and project rather than finding a different thread by a similar title.

## Read before sending

Discover the available T3 thread tools. Use the runtime's current-thread identity; if unavailable, `t3_thread_list` with `limit: 1` returns `currentThreadId`. If it matches the destination, follow the skill's local consultation path and do not send.

Use `t3_environment_links` to check the current environment. On the destination environment, omit `environmentId`. From another environment, pass the destination `environmentId` only through an available authorized link. If the destination is unlinked or inaccessible, report the unsent packet instead of changing connections or permissions.

Read the target with `t3_thread_read`, using the configured `threadId`, a small `limit`, and bounded `maxCharsPerItem`. Verify the returned identity, project, link, and that the thread is not archived. Do not read the whole history. When checking for likely duplicates, a bounded `t3_thread_search` in the destination project can help; consider only matches for the destination thread. Search is not exhaustive.

## Queue the proposal

Call `t3_thread_send` with:

- `threadId`: the configured destination thread ID.
- `environmentId`: only when routing from another linked environment.
- `mode: "queue"`: submit a new turn without interrupting the hub's current work.
- `message`: the sanitized `Skill suggestion:` packet, ending with a request to consult Mayank before implementation or a PR.

Use the existing thread, not `t3_thread_launch`, and do not use `restart` or `steer`. Do not include a request to implement the idea immediately or expand the target thread's permissions. T3 may reject delivery when the target's modes are broader than the sender's; treat that as a delivery limitation, not approval to alter either mode.

Inspect the send result. Retain the returned message ID for a delivery check and use its `link` verbatim when reporting to the user. Say queued when it is queued. Do not claim consultation or approval from that receipt. On an error or lost acknowledgment, check for the existing packet before another attempt; if delivery cannot be established, report it as unconfirmed.

No live test packet is needed when authoring or installing this skill. In the hub itself, a test send would enqueue a message to the same conversation rather than validate the normal sender path. Read-only route checks and a clearly labeled delivery limitation are preferable to a self-message loop.
