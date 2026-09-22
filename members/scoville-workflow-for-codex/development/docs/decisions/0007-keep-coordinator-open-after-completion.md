---
format_version: 1
id: ADR-0007
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/orchestration
supersedes: ADR-0001
---

# Keep the coordinator open after completion

## Decision

Implement `scoville-workflow-codex` entirely with normal native Codex coordinator, executor, repair, and reviewer tasks. Continue an executor or reviewer with the same task ID after a user decision without counting a repair or archiving it; allow the first attempt plus at most two actual repairs; archive each terminal child task, but leave the coordinator open after it posts the requested scope's final completion report.

## Problem

Self-archiving the coordinator as its final action can terminate the turn before Codex displays the completion report, hiding the result the user needs to read.

## Drivers

- The final completion report must remain visible in the coordinator task.
- Completed executor repair and reviewer tasks should still leave the sidebar after their results are retained.
- The launcher and coordinator remain separate native tasks with distinct lifecycle ownership.
- Same-task user-decision continuation and bounded repairs remain unchanged.

## Considered alternatives

- Archive the coordinator after posting: cleans up the task but can still terminate the turn before the report becomes visible.
- Ask the launcher to mirror the report: preserves visibility but breaks launcher isolation and creates a second reporting owner.
- Leave the coordinator open: preserves one reporting owner and makes the final result available without changing child cleanup.

## Consequences

- The coordinator's terminal action is its completion report rather than an archival call.
- The completed coordinator remains in the task list until the user archives it.
- Child task archival and identity verification remain unchanged.
- The native lifecycle qualification must verify a visible completion report and an unarchived coordinator.

## Confirmation

1. Inspect the Skill and operations reference for matching final-report and no-self-archive rules.
2. Run focused tests that reject omitted-ID coordinator archival while retaining child archival assertions.
3. Compare the installed package with the canonical nested package after replacement.

## Revisit when

Codex provides an archival operation that guarantees the current task's final report is displayed before the task closes.
