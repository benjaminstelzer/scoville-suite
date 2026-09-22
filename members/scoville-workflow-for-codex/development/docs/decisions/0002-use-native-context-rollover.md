---
format_version: 1
id: ADR-0002
status: superseded
created: 2026-09-14
accepted: 2026-09-14
scope: project/context-lifecycle
superseded_by: ADR-0010
---

# Use native task rollover above 66 percent context

## Decision

Do not invoke manual compaction in the native workflow. At a natural internal boundary with a fresh observed context value strictly above 66 percent create one compact successor task for the same Plan unit and role. Preserve model reasoning authorization and remaining work; count no repair. Continue user-decision replies in the same task.

## Problem

The native Codex workflow cannot issue a compaction command through a Skill. Continuing an overfilled task wastes context while treating the successor as a repair would corrupt attempt accounting.

## Drivers

- Preserve the strict-above-66 threshold from the source workflow.
- Keep handoffs compact and exclude information already owned by the Plan.
- Preserve logical unit role route authorization and review boundaries across a context-only rollover.
- Never estimate a hard threshold from message count or prose size.

## Considered alternatives

- Continue and rely only on native automatic compaction: requires no task transition but cannot preserve the requested 66-percent workflow boundary.
- Start a new task after a fixed number of turns: simple but unrelated to actual context occupancy.
- Create a compact successor only from the worker's fresh native rollout value above 66 percent: preserves the requested boundary without a separate runtime.

## Consequences

Context rollover is a terminal transition for the old task and produces a new native task ID without consuming a repair. It adds one task only when the threshold is actually observed. The coordinator archives the old task after retaining the compact handoff. Each local native task identifies its own rollout through `CODEX_THREAD_ID` and reads `last_token_usage.input_tokens` plus `model_context_window`; cumulative usage is not context occupancy. A missing exact rollout or metric is a blocker, never an estimate.

## Confirmation

Observe fresh native context values at and above 66 percent. Confirm same-task continuation at 66 or below and exactly one archived predecessor plus one same-unit successor above 66 with unchanged role model reasoning authorization and repair count. This task provided a native below-threshold observation of 78,240 input tokens over a 258,400-token effective window (30.3 percent) immediately after automatic compaction.

## Revisit when

Reconsider if Codex exposes safe in-place compaction to Skills or changes the native rollout metric or task-ID environment contract.
