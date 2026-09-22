---
format_version: 1
id: ADR-0009
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/dispatch
transition_batch: ceb5f6701e6eeee4dcfff59821f58b05445f975f4eae602d0ce6bbbf3ec20e83
transition_batch_members: [ADR-0009, ADR-0010]
---

# Bundle compatible Plan steps within one executor

## Decision
Permit one executor and one behavior-boundary review to cover adjacent Plan Steps only when they share one outcome, owner, authorization, route, workspace, and Acceptance boundary. Retain a dispatch boundary whenever any of those facts differs.

## Problem
The current one-Step-per-task contract repeatedly pays task creation and project-recovery cost even when adjacent Steps form one behavior-complete unit.

## Drivers

- Reduce fresh-task and context reconstruction cost without hiding independently resumable work.
- Preserve Plan-authored order, route distinctions, user-decision boundaries, and Acceptance ownership.
- Keep dispatch mechanics in Workflow while Scoville Plan owns the public Step compatibility contract.
- Require the public compatibility update before enabling bundles.

## Considered alternatives

- Keep one task per Step: Preserves the current contract but retains repeated recovery and review overhead.
- Bundle every Work Item: Reduces task count but can mix routes, authority, external effects, and independently resumable outcomes.
- Bundle only adjacent compatible Steps: Reduces overhead while retaining deterministic boundaries and the Work Item's Acceptance contract.

## Consequences

- A bundle is runtime dispatch state and creates no new Plan field or hidden project record.
- Mixed routes, changed Decisions, external effects, or independently resumable results remain separate dispatches.
- Workflow cannot implement bundling until Scoville Plan publishes the compatible public guidance.
- Review remains behavior-boundary based and cannot be skipped solely because several Steps share one executor.

## Confirmation

1. Run a compatible five-step fixture and observe one executor plus at most one required reviewer.
2. Run mixed-route, changed-Decision, external-effect, and user-decision fixtures and observe separate dispatches.
3. Verify unchanged Plan ordering, Acceptance ownership, repair accounting, and review requirements.

## Revisit when
Reconsider if native task startup and recovery cost becomes negligible or bundling obscures independently resumable outcomes.
