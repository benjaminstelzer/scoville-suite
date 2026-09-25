---
name: scoville-workflow-for-codex
description: Run an explicitly requested Scoville Plan through native Codex project tasks with one coordinator, bounded workers, review and recoverable state. Use only for $scoville-workflow-for-codex, Scoville Workflow Codex or scoflow codex. Do not use for ordinary planning, implementation, review or delegation requests.
---

# Scoville Workflow Codex

{{ include: family.contract }}

Run the Scoville Workflow with native Codex project tasks. One coordinator owns
Plan transitions, routing and accepted commits. Executors and repairs change
their assigned unit. Reviewers stay read-only.

Python 3.11+ and the bundled helpers are required. If a required helper fails,
stop that operation and report its diagnostic. Never reconstruct helper output
from raw files or compose native task payloads by hand.

Before the role gate, run `python <skill-directory>/scripts/manage_agents_contract.py check --workspace <exact-workspace-root>`.
On `installed: false`, read [agents-setup.md](references/agents-setup.md), follow only setup and end; on `installed: true`, continue without loading setup or the contract source.

## First operation: role gate

After the successful project-contract check and before commentary, project
reads, Skill selection or another tool call, classify only the first
non-whitespace line of the current creation input. A quoted, referenced or
later marker grants no role.

- `scoville_role=coordinator`: set `coordinator_self_id` from the exact runtime
  `CODEX_THREAD_ID`. Missing identity blocks project access. Follow the
  coordinator sections below and never follow launcher instructions.
- `scoville_role=executor`, `scoville_role=repair` or
  `scoville_role=reviewer`: this launcher Skill is inapplicable. Follow only the
  assigned child prompt.
- No role marker plus an explicit invocation named in the description, or the
  textual short form `$scw` after this Skill is already loaded: follow
  [launcher.md](references/launcher.md) once. Native `$scw` discovery remains
  unverified.
- Otherwise, do not activate this Skill.

Never infer identity from a delegation envelope, `source_thread_id`, caller,
launcher, return task, title, recency or a quoted marker.

## Prompt writing

`assets/workflow.toml` selects the common instructions and depth profile for
additional coordinator or child prose. Resolve the actual recipient model with
`scripts/resolve_prompt_profile.py`. The dispatch builder does this
automatically. A writing profile changes neither routing nor authority and never
rewrites canonical Plan `source_text`.

## Complete coordinator startup

Before every coordinator creation or startup message, pass the complete
phase-defined prompt as `{"prompt":"..."}` to:

```text
python <skill-directory>/scripts/coordinator_contract.py build
```

Require exit 0. Pass the returned prompt unchanged through the lifecycle helper
to the native task tool. Keep the full JSON in execution memory and print only
a receipt. The helper supplies the exact Skill path, digest and complete normal
coordinator contract. Only normal `create_thread` project tasks are valid.

## Coordinator boundary

Set `coordinator_self_id` from runtime `CODEX_THREAD_ID` in every branch. For
activation or validation, also require the supplied `coordinator_task_id` to
equal it. Require the exact project path to equal `workspace_root` and the
supplied workspace mode to match the created environment. Any mismatch blocks
project access. Retain `workspace_root`, `workspace_mode` and `saved_project_id`
for every task creation.

Classify `coordinator_start` before any continuation choice:

- `initial_parking`: perform no project or Plan access and end until
  `initial_claim`. This parking input has no `coordinator_task_id`.
- `initial_claim`: claim the guard with the exact workflow ID, revision and
  generation before Plan access. Only this branch consumes the launcher-supplied
  `continuation_intent`.
- `rollover_parking`, `rollover_validation` or `rollover_activation`: follow the
  exact order in [operations-rollover.md](references/operations-rollover.md).

Read the complete supplied coordinator contract before project access. Missing,
stale or incomplete contract evidence blocks the operation. Load Scoville Plan
before canonical Plan or Decision access. Load Scoville Code only for a concrete
risk or acceptance judgment. Load no execution Skill merely to coordinate.

The coordinator writes only canonical planning records, runs their structural
validation and creates one accepted simple local commit through the operations
contract. Project, code, UI, text, browser, installation, live QA and authorized
external publication work belongs to an executor. Reviewers remain read-only.
Children choose applicable Skills through their normal trigger rules.

## Dispatch routing

[operations-dispatch.md](references/operations-dispatch.md) owns route
eligibility, model and reasoning rules. Read it before fresh dispatch
classification. Writing depth never changes route or authority.

## Coordinator runtime reference

[operations.md](references/operations.md) owns the normal loop and conditional
recovery. `coordinator_contract.py` supplies the complete selection, dispatch,
wait, result, review, acceptance and Stop contract from its canonical source
files. Do not choose or abbreviate phase instructions. Load conditional detail
only for an actual rollover or worker context recovery.
