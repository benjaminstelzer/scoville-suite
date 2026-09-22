---
format_version: 1
id: ADR-0027
status: accepted
created: 2026-09-20
accepted: 2026-09-20
scope: project/coordinator-context-rollover
---

# Roll over the coordinator at accepted unit boundaries

## Decision

At each successfully accepted dispatch-unit boundary, immediately before any
next-unit selection or dispatch, the coordinator reads fresh telemetry from its
exact own native rollout. Occupancy at or above 33 percent creates one successor
coordinator at that boundary. After one ready successor is reconciled, validates
the handoff, receives the existing guard atomically, and is explicitly
activated, that successor archives the exact predecessor task. The successor
alone selects and starts the next dispatch unit. No mid-unit polling, persistent rollover-due
field, or separate Plan checkpoint is required: execution, required review,
repairs, Acceptance, Plan transition, validation, and the scoped commit already
form one indivisible unit transition.

A dispatch unit is one Step, one authorized compatible adjacent-Step bundle, or
one complete Step-less Work Item. A successful Work Item boundary is not
required when an earlier Step unit has already reached its accepted boundary.

## Problem

Long-running coordinators repeatedly carry an increasingly large conversation
through many independently accepted Steps. Waiting improvements remove idle
turns but do not bound the context retained across successive dispatch units.
Waiting until a complete Work Item can keep an already large coordinator alive
through several separately accepted Steps.

## Drivers

- Keep coordinator context well below the model window during long Plans.
- Preserve the existing execution, review, repair, Acceptance, Plan, and commit
  gates for the current dispatch unit.
- Use the same boundary the workflow already treats as accepted and resumable.
- Prevent two coordinators from selecting or dispatching the next unit.
- Keep the canonical Plan as the source of work state instead of creating a
  free-form conversation summary.
- Fail softly when exact telemetry or successor identity is unavailable.
- Keep the new lifecycle small enough for a lower-capability coordinator to
  apply as one ordered decision rather than another parallel state machine.

## Considered alternatives

- Poll and mark rollover due immediately at 33 percent: detects the crossing
  earlier but adds state and can split or complicate
  execution, review, repair, or the accepted transition for one unit.
- Wait for the complete Work Item: preserves a broad boundary but can retain
  several additional independently accepted Step units.
- Roll over after an accepted dispatch unit: bounds context while preserving
  the workflow's existing atomic unit and transition gates.

## Consequences

- Fresh occupancy below 33 percent leaves the coordinator unchanged; occupancy
  at or above 33 percent makes rollover due.
- Missing, stale, malformed, or contradictory telemetry is never estimated. It
  continues in the same coordinator and does not stop otherwise valid work.
- Telemetry is checked once at the accepted boundary and never between the
  executor, reviewer, repair, Acceptance, Plan-transition, validation, or commit
  phases.
- A blocker, unresolved user decision, failed validation, failed commit, or
  unaccepted unit is not a rollover boundary.
- A completed requested scope, explicit Stop, or complete Plan creates no
  successor.
- The successor receives stable workflow identity, exact workspace and saved
  project identity, requested scope and language, canonical Plan reference,
  expected Git HEAD or an explicit non-Git not-applicable value, accepted unit
  ID, predecessor ID, generation, and the configured coordinator model and
  reasoning. It receives no free-form dialogue summary.
- The predecessor first records one pending transition in the existing guard.
  A predecessor-bound transition key, accepted-unit identity, unique successor
  title, and host-task reconciliation make retries find the same successor
  instead of creating duplicates. An unknown creation outcome never permits a
  second creation until reconciliation proves that no successor exists.
- A provisional `clientThreadId` is not sufficient archival proof. The
  predecessor remains unarchived until the one pending successor resolves to a
  ready `threadId`. A ready ID alone grants no ownership. The successor first
  validates the workspace, Plan profile, expected Git HEAD or non-Git state,
  accepted boundary, and next eligible unit while read-only. The predecessor
  receives one identity-bound validation acknowledgement from the successor. The
  predecessor then transfers the guard atomically, sends one explicit activation
  message, ends that turn, and performs no self-archival. The activated successor
  sends no activation acknowledgement, waits exactly once for that predecessor
  turn to finish, archives the exact predecessor ID, and requires explicit
  same-ID `archived: true` proof before next-unit selection.
  Setup or validation failure remains visible and starts no replacement or next
  unit.
- After successor creation the predecessor performs only the bounded
  reconciliation, guard transfer, and activation message required to complete
  or safely stop the handoff. It performs no archival, Plan transition, project
  work, or next-unit selection.
- `references/operations.md` owns the full ordered rollover procedure. The
  entrypoint contains only the narrow permission needed to replace a coordinator
  and points to that owner; it does not restate the lifecycle.
- The rollover adds no Plan-only commit. One concise coordinator announcement
  names the accepted unit and the coordinator transition before successor
  creation.

## Confirmation

1. Verify 32.99 percent continues without rollover and exactly 33 percent rolls
   over using integer comparison rather than floating-point rounding.
2. Verify no rollover occurs during execution, review, repair, Acceptance,
   Plan transition, validation, or commit for the active unit.
3. Verify one accepted Step, accepted compatible Step bundle, and accepted
   Step-less Work Item each permit rollover before the next dispatch.
4. Verify only the activated successor dispatches the next unit and retries,
   compaction, provisional creation, unknown creation outcomes, and setup
   failure never create duplicate successors.
5. Verify missing or stale telemetry is not estimated and continues in the same
   coordinator without archival. Verify the successor archives the predecessor
   only after completed guard transfer and activation and after the predecessor's
   activation-message turn ends. Completion, Stop, blockers, and unresolved user
   decisions create no successor.
6. Verify language, requested scope, workspace, saved project, Plan identity,
   expected Git HEAD or explicit non-Git state, accepted unit, model, and
   reasoning survive the rollover.
7. Give the final coordinator contract and boundary scenarios to a fresh Luna
   task. Require it to choose the correct next action and forbidden actions for
   below-threshold, threshold, mid-unit, completed-scope, provisional-successor,
   and retry cases without additional explanation.
8. In the native qualification, retain the predecessor's boundary occupancy,
   the successor's first occupancy, coordinator model-turn counts, successor
   count, and accepted unit IDs. Confirm the check itself creates no polling or
   otherwise empty coordinator turn.

## Revisit when

Reconsider when Codex provides a native coordinator replacement primitive or a
different authoritative context-occupancy contract.
