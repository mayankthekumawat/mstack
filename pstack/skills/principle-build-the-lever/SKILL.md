---
name: principle-build-the-lever
description: Build a rerunnable tool when repetition or a difficult comparison makes automation materially useful. Reuse existing checks for ordinary edits.
---

# Build the lever

Use a codemod, generator, query or verification script when it reduces repeated work or makes a result reliably checkable. Prefer an existing tool when it already does the job.

- Learn the transformation on one unit before applying it broadly. Verify that unit, then automate the repeated work.
- Make the operation safe to rerun and preserve a usable verification result.
- Keep the tool no larger than the task needs. A straightforward fix or existing test command does not need a new script or framework.
- For delegated repetitive work, share the recipe and verification contract once, with separate output locations.
- Keep the tool with the work when future runs need it; commit it when it belongs to the project.

The useful artifact is a result another person can check or rerun. A new file is not a requirement by itself.
