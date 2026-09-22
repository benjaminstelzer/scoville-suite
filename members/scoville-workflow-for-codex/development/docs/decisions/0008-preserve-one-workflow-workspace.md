---
format_version: 1
id: ADR-0008
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/workspace
---

# Preserve one workflow workspace

## Decision

Use the workflow's already-active checkout as the shared workspace for the coordinator and every executor reviewer repair and rollover successor. Create a separate worktree only when the user explicitly requests one or a binding higher project rule requires isolation, and never use a worktree as an automatic fallback when same-workspace task creation is unavailable.

## Problem

Automatically creating a Git worktree for a new conversation separates that conversation from uncommitted changes Plan updates and local runtime state that belong to the active workflow.

## Drivers

- One continuous workflow and Work Item loop needs one current working state.
- New conversations must see the same absolute project path and uncommitted files immediately.
- A repository being managed by Git is not an isolation requirement.
- Deliberate isolation must preserve the user's or project's explicit choice.
- Unsupported same-workspace execution must remain visible as a decision instead of becoming silent isolation.

## Considered alternatives

- Create a worktree for every Git repository: provides isolation but loses the active checkout's uncommitted and local state by default.
- Copy state into each new workspace: duplicates ownership and cannot reliably reproduce all local runtime state.
- Reuse the active checkout unless isolation is explicit: preserves continuity and keeps workspace changes deliberate.

## Consequences

- Every native task creation reuses the same saved project and local environment by default.
- Executor reviewer repair and rollover successor conversations observe the active checkout's current state rather than a branch snapshot.
- Explicit isolation requires a pre-start explanation of the new workspace transfer path and state that will not be inherited automatically.
- Missing host support for same-workspace creation pauses dispatch for an exact user decision.

## Confirmation

1. Inspect every coordinator child repair reviewer and rollover creation rule for the same absolute project path and local environment.
2. Run focused source-contract cases for dirty-state visibility Git-only no-worktree behavior explicit isolation and unsupported same-workspace handling.
3. Compare the installed package with the canonical nested package after replacement.

## Revisit when

Codex provides a different native workspace identity that demonstrably shares the active checkout's uncommitted files Plan records and local runtime state.
