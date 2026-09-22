---
format_version: 1
id: ADR-0010
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/context-lifecycle
supersedes: ADR-0002
transition_batch: ceb5f6701e6eeee4dcfff59821f58b05445f975f4eae602d0ce6bbbf3ec20e83
transition_batch_members: [ADR-0009, ADR-0010]
---

# Make unavailable context telemetry non-blocking

## Decision
Replace the missing-metric blocker in ADR-0002: preserve the strict above-66-percent rollover trigger at a natural boundary when fresh exact context telemetry is available and material work remains, but let bounded work continue when telemetry is missing, stale, or contradictory unless an observed host failure independently blocks progress.

## Problem
ADR-0002 makes a missing exact rollout or metric a blocker, which can terminate otherwise valid bounded work even when no context-exhaustion failure is observed.

## Drivers

- Prevent unavailable or stale telemetry from becoming the sole reason to stop valid executor or reviewer work.
- Preserve rollover only at natural boundaries with material work remaining.
- Use fresh native context occupancy when available and never estimate it from message count or prose size.
- Retain explicit evidence and user authority for any threshold change.

## Considered alternatives

- Keep missing telemetry as a blocker: Preserves ADR-0002 exactly but retains false-positive workflow stops.
- Ignore context telemetry entirely: Avoids false blockers but can waste context and miss genuine exhaustion risk.
- Treat unavailable telemetry as non-blocking while retaining evidence-based rollover: Preserves bounded progress and still reacts to fresh occupancy data.

## Consequences

- Missing, stale, or contradictory telemetry alone no longer creates a blocker or successor task.
- Fresh telemetry can still trigger one same-role successor at a natural boundary under the strict above-66-percent threshold unless the proposal is explicitly revised before acceptance.
- A threshold change requires explicit acceptance in the superseding Decision rather than inference from traces.
- Actual host failures remain ordinary blockers with observed evidence.

## Confirmation

1. Exercise unavailable, stale, contradictory, below-threshold, above-threshold, post-compaction, and completed-without-checkpoint cases.
2. Confirm bounded work continues without a telemetry-only blocker and fresh above-threshold occupancy creates exactly one same-role successor only when material work remains.
3. Verify unchanged repair accounting, user-decision continuation, archival, and task identity behavior.

## Revisit when
Reconsider if Codex provides reliable in-place compaction or a new authoritative context-availability contract.
