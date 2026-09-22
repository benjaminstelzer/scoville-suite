---
format_version: 1
id: ADR-0024
status: superseded
created: 2026-09-20
accepted: 2026-09-20
scope: project/dispatch
supersedes: ADR-0014
superseded_by: ADR-0025
---

# Dispatch exact execution-unit context

## Decision

The coordinator invokes a read-only Workflow Python helper that builds the complete ready-to-send child prompt from an exact deterministic projection of the selected execution unit. A Work Item without Steps remains one complete dispatch unit; a Work Item with Steps requires the exact named Step or authorized adjacent Step bundle. For a Step unit the projection contains Plan frontmatter, Goal and Non-goals, Work Item identity and live control fields, Outcome, Acceptance, only the selected Step text, Next action, direct-dependency status lines, and every Work Item-referenced Decision. It omits every other Step and all Work Item Evidence. Existing selector calls without a unit remain backward compatible for coordinator recovery.

## Problem

A Step executor and its reviewer currently receive every Step and the accumulated Evidence history because the selector projects the complete Work Item even though both roles own one exact execution unit.

## Drivers

- Each worker must see its exact assigned task and every binding fact required to execute and verify it.
- Evidence is proof for coordinator lifecycle decisions rather than executable instruction or authorization.
- Referenced Decisions are normative Plan inputs and must not be silently filtered by dispatch-time model judgment.
- Selection must remain deterministic and must not replace source facts with coordinator prose.
- Prompt construction must not rely on the coordinator reproducing role rules or JSON envelopes from memory.
- Existing projects and selector consumers must keep their current Work Item recovery behavior.

## Considered alternatives

- Keep embedding the complete Work Item: Preserves the current interface but repeatedly sends unrelated Steps and superseded execution history.
- Let the coordinator summarize the task: Reduces prompt size but creates a lossy second interpretation of canonical Plan facts.
- Add only an exact selector unit mode: Gives workers the right Plan slice but still leaves prompt assembly and accidental extra prose to the coordinator.
- Add an exact unit projection plus a read-only prompt builder while retaining the existing whole-item mode: Gives workers only their assigned task and makes the sent envelope deterministic without changing Plan files.

## Consequences

- Initial executors, rollover successors, reviewers, and repairs receive the same exact unit projection for their assigned Step.
- The coordinator sends the prompt builder output verbatim and adds no transition prose or Plan data.
- All Work Item-referenced Decisions remain present; irrelevant Decision links are corrected in a mutable Plan rather than hidden at dispatch.
- Other Step bodies and accumulated Evidence entries never enter child context.
- The coordinator still owns complete Work Item Evidence and lifecycle transitions.
- Required worker context must reside in Goal, Non-goals, Outcome, Acceptance, the selected Step, Next action, or a referenced Decision rather than Evidence.
- Helper diagnostics fail closed and never trigger a raw Plan read or coordinator-authored fallback.

## Confirmation

1. Extend the Scoville Plan selector tests to prove unchanged whole-item output and exact named-Step or authorized-bundle projection with fail-closed invalid-unit handling.
2. Exercise the Workflow prompt helper for Work Items with and without Steps and prove initial executor, rollover, reviewer, and repair prompts embed all referenced Decisions, no Evidence, and no coordinator additions.
3. Replay DIVI `W-006/step-3` and confirm that its prompt retains every binding field while excluding Steps 1, 2, and 4 plus their accumulated attempt history.

## Revisit when

Reconsider when the native Plan format gains independently lifecycle-managed Step records or native tasks can consume verified structured Plan attachments outside the prompt.
