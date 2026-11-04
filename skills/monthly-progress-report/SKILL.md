---
name: monthly-progress-report
description: Create a personal monthly progress report from a previous report, release records, work history, and user updates. Use for a monthly work report or personal MPR, including AI Cell reports. Excludes querying a project's MPR issue data unless it supports the personal report.
---

# Monthly progress report

Produce a reviewable PDF in the supplied report's style, with editable content and a private evidence record. Treat the previous report as a format and voice reference, not evidence that its achievements or plans happened again.

## Establish the reporting period and format

Use the last completed month when the request makes that period clear. Inspect the reference PDF's text and rendered pages. Recover relevant corrections from the original report conversation when available. Ask only for missing choices that would materially change the report, and keep gathering evidence while waiting for optional updates.

For an AI Cell report like the September 2026 reference, read [references/ai-cell-format.md](references/ai-cell-format.md). For another template, follow its actual sections and visual style instead.

## Reconstruct the month's work

Read the relevant repositories, release and deployment records, dated service checks, and available work conversations. Use the entire reporting month in the user's timezone. Distinguish commit dates, merge dates, deployment dates, and later verification dates. An old commit deployed this month may count; a commit merged this month but deployed later belongs under preparation or validation.

Keep a local evidence ledger with one row per proposed claim: reporting date, project, work, status, source, and limitation. Prefer deployment receipts and observed behavior over PR titles. Consolidate commits that address the same officer-facing outcome. Read the outcome of an investigation before presenting it as a fix.

Use the user's account of meetings, manual work, milestones, and priorities as attributed evidence. Ask for useful missing updates once. If they remain unavailable, deliver a clearly marked draft and list the unresolved facts separately. Do not invent counts, release status, cost savings, or completion of last month's plans.

For costs and usage, record the date window, timezone, units, included services or billing keys, and whether figures are monthly, cumulative, sampled, estimated, or a trial. Do not imply that selected-day savings continued all month. Add an evidence appendix only when actual supporting material warrants it. Keep raw conversations, credentials, customer records, internal host details, and billing screenshots out of public skill repositories.

## Write for the report's reader

Describe each substantial update in a short paragraph that connects the earlier issue, the change, and its practical benefit. Let that structure guide the wording without adding literal labels such as "Before", "What changed", or "Impact". Explain service behavior in familiar terms. Keep implementation details in the evidence ledger unless the report's reader needs them.

Keep production deliveries separate from trials, staging validation, and future plans. Preserve material caveats beside the claim they qualify. Propose next-month priorities as draft priorities until confirmed, and recheck carried-forward plans instead of treating them as delivered or still blocked automatically.

## Build and verify

Reuse a suitable existing report builder when available. The optional [scripts/render_report.py](scripts/render_report.py) creates a compact A4 PDF and editable HTML from JSON without browser automation. It needs Python and PyMuPDF, and supports explicit page grouping. See [references/render-input.md](references/render-input.md) for the input and command. Use another document tool if the requested reference needs features this renderer does not provide.

Render every final PDF page to images and inspect them. Check hierarchy, wrapping, clipping, page breaks, whitespace, identity, month, footer numbers, and any appendix. Extract the final PDF text and compare it with the content and evidence ledger. Fix and rerender any defect. The renderer's overflow check does not replace visual review.

Deliver the PDF and an editable source. Identify draft status and the few facts that still need confirmation. Report completion only after the files exist and pass these checks. Creating a report does not authorize sending it, changing production systems, publishing private evidence, or installing skills.
