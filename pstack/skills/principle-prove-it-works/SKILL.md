---
name: principle-prove-it-works
description: Verify a feature, integration or artifact against its actual acceptance criteria before declaring it complete.
---

# Prove It Works

Verify every task output by checking the real thing directly. Do not infer from proxies, self-reports, or "it compiles."

**Why:** Unverified work has unknown correctness. Indirect verification (file mtimes, output freshness, agent self-reports, cached screenshots) feels cheaper than direct observation. Acting on a wrong inference costs far more than checking the source.

**Pattern:** Choose checks proportional to the change and its acceptance criteria. A documentation edit needs an accurate diff and valid references, not an unrelated application test suite.

Check the real thing, not a proxy:
- Check process liveness directly, not indirectly through derived state
- Read the actual value, not a cached or derived representation
- When verification fails, suspect the observation method before suspecting the system

Code and features:
1. Build it (necessary but not sufficient)
2. Run it and exercise the actual feature path
3. Check the full chain: does data flow from input to output?
4. For integrations or load replays, prove one complete user path, including relevant UI and downloads, before scaling up.
5. Report completed/total work and distinguish synthetic, component and full-application tests. A successful component check does not establish application capacity.

Delegation: trust artifacts, not self-reports.
When verifying delegated work, inspect the actual output artifact (git diff, file contents, runtime behavior), not the delegate's summary. Agents report what they intended, not always what happened.

## Script the check when you can

Reuse existing checks first. Add a deterministic script when repetition or a difficult comparison justifies it, then run it and keep the result. Small changes do not require a new verification artifact.

Keep the artifact visible for the human. Commit it only for large or complex work where the trail has to be auditable later, like a big port or migration (the **show-me-your-work** skill). Most work just needs it visible, not committed.
