---
format_version: 1
id: ADR-0014
status: superseded
created: 2026-09-19
accepted: 2026-09-19
scope: project/dispatch
superseded_by: ADR-0024
---

# Embed selected Plan context in child prompts

## Decision

The coordinator embeds the complete unmodified selector result in every initial executor prompt together with only the role, unit, workspace, and receiver rules. The executor does not reread Plan or Decision files. Later child roles receive a fresh selector result and only the validated structured result required by that role, without free-form transition prose or a prompt-size cap.

## Problem

The coordinator selects bounded Plan context but the former child prompt tells the executor to read canonical Plan records again, which can load the complete Plan and repeats work the coordinator already performed.

## Drivers

- Make one deterministic selection the planning input for both coordination and execution.
- Preserve the complete current Work Item and every referenced Decision without a lossy summary.
- Prevent child tasks from reopening a large Plan or reconstructing intent from paths.
- Keep role rules and later validated result objects explicit without adding transition prose.

## Considered alternatives

- Let each child read canonical records: Keeps prompts short but repeats selection and can load the complete Plan.
- Send a compact coordinator summary plus paths: Reduces prompt size but creates a second lossy interpretation and still invites rereads.
- Embed the exact selector result: Increases the prompt by the selected context size but removes duplicate Plan recovery and preserves the bounded source facts.

## Consequences

- Initial executor prompts contain only role and receiver rules, the workspace, and exact `plan_context` data.
- The former 8,000-character prompt limit no longer applies; the selector's existing complete-output budget remains the boundary.
- Rollover, reviewer, and repair prompts may add only their required validated structured result object.
- The coordinator reruns selection after Plan writes and before later child dispatches.

## Confirmation

1. Run the workflow contract suite and verify the prompt envelope includes exact selector output without a summary or size cap.
2. Resume DIVI and EMPCO at their next dispatch boundaries and inspect the created executor prompts.
3. Confirm those executors use embedded `plan_context` and do not read Plan or Decision files.

## Revisit when

Reconsider when native tasks can consume a verified structured Plan attachment without placing it in the prompt.
