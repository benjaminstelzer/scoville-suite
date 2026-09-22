---
format_version: 1
id: ADR-0017
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/commit
supersedes: ADR-0015
---

# Commit complete Plan state at accepted boundaries

## Decision

Keep coordinator Plan changes uncommitted while their child is active. The next accepted unit commit contains its accepted project changes and the complete valid coordinator Plan state accumulated since the previous accepted commit. Retained terminal blocker state from an earlier unit may be included, but never that unit's unaccepted project changes. Required HEAD-bound backup intervals gate conflicting units, and only an authorized executor creates a replacement backup before source editing.

## Problem

Deferring every blocked unit's Plan state until its own acceptance can make a later independent unit's staged Plan structurally invalid because `current_item` and the sole `in_progress` or `paused` state must move together.

## Drivers

- Preserve one structurally valid canonical Plan profile at every accepted commit.
- Avoid standalone Plan checkpoint commits after dispatch.
- Keep unaccepted project changes out of another unit's commit.
- Preserve repository backup hooks and every existing change without bypass or destructive recovery.
- Keep project backup writes with executors while the coordinator owns selection and evidence checks.

## Considered alternatives

- Leave earlier blocker state unstaged: Keeps unit ownership narrow but can produce an invalid committed `current_item` and Work Item lifecycle.
- Stop all independent work after any blocker: Preserves commit isolation but discards the workflow's safe independent-work continuation.
- Commit complete accumulated Plan state at the next accepted boundary: Preserves profile validity and avoids publishing earlier unaccepted project changes.

## Consequences

- Canonical Plan, Decision, and index files are staged as complete files, never as unit-local hunks, and must match the validated working profile.
- A retained terminal blocker can become durable in a later accepted unit commit after exact-ID archival verification.
- A blocked source unit with an open HEAD-bound backup interval prevents another same-workspace unit from dispatching or committing until disposition.
- If a stale backup has no source edits, the Plan selects backup creation first and the authorized executor performs it before editing.

## Confirmation

1. Run the workflow contract suite and verify all unit-commit and independent-continuation scenarios.
2. Confirm an independent accepted unit commits a complete valid Plan containing earlier retained terminal blocker state but no earlier project changes.
3. Confirm a blocked unit with source edits after its HEAD-bound backup prevents another same-workspace dispatch or commit.
4. Confirm every staged canonical planning file equals its validated working bytes before commit.

## Revisit when

Reconsider when canonical Plan lifecycle state is independently durable and no longer shares Git commit boundaries with project work.
