---
format_version: 1
id: ADR-0015
status: superseded
created: 2026-09-19
accepted: 2026-09-19
scope: project/commit
superseded_by: ADR-0017
---

# Defer unit checkpoint commits

## Decision

From child dispatch through Acceptance and review, keep coordinator-owned Plan checkpoints uncommitted. When Git is in use, one accepted unit commit contains the accepted project result and every Plan change accumulated for that unit, with no intermediate commit after a required pre-change backup. An outstanding HEAD-bound backup interval gates other same-workspace units, and only an authorized executor creates a replacement backup before source editing.

## Problem

A Plan-only checkpoint commit can advance `HEAD` after a valid pre-change backup and cause the later source commit hook to reject that backup.

## Drivers

- Preserve repository backup and validation hooks without bypass.
- Keep task IDs, results, review state, Evidence, blockers, and `Next action` durable in the shared working tree until the unit is accepted.
- Prevent a coordination checkpoint from invalidating a project safety prerequisite.
- Preserve every existing commit and working-tree change during recovery.
- Keep project backup writes with executors while the coordinator owns only selection and evidence checks.

## Considered alternatives

- Commit each Plan checkpoint immediately: Makes coordination history granular but can invalidate a backup tied to the earlier `HEAD`.
- Commit project changes before review then add Plan state later: Preserves the backup order but publishes an unaccepted result.
- Commit accepted project and Plan state together: Keeps one review-gated unit boundary and leaves the backup-to-source-commit interval free of Plan commits.

## Consequences

- Active-unit Plan changes remain visible through the shared working tree but are not individually committed.
- A failed commit hook leaves the unit uncommitted with its diagnostic and changes intact.
- A blocked unit with source changes after its HEAD-bound backup prevents another same-workspace unit from advancing HEAD until the user resolves that interval.
- If earlier commits stale a backup while source is unchanged, the Plan selects backup creation first and the authorized executor performs it before editing; otherwise recovery requires the user's exact decision without discarding work.

## Confirmation

1. Run the workflow contract suite and verify every unit-commit scenario.
2. Inspect a DIVI source unit and confirm no Plan-only commit occurs between its valid backup and accepted unit commit.
3. Confirm the final commit contains both accepted project paths and all Plan changes accumulated for that unit.
4. Block one unit after its backup and source edit and confirm no other same-workspace unit advances HEAD.

## Revisit when

Reconsider when the project backup contract no longer depends on the current `HEAD` or Plan state has an independent durable owner outside Git history.
