---
name: scoville-workflow-for-codex
description: Explicit native-Codex Scoville workflow. It first verifies the project's short write contract; missing setup asks the user and ends. An installed launcher creates one native coordinator. A task whose first non-whitespace input line is scoville_role=coordinator is that coordinator and may create only the operations-owned rollover successor. Use only for $scoville-workflow-for-codex, Scoville Workflow Codex, or scoflow codex, never ordinary planning, implementation, review, delegation, or worker requests.
compatibility: "Codex desktop with saved local projects, native task creation in the same local checkout, waiting, messaging, archival controls, access to CODEX_THREAD_ID, Python 3.11+ standard library for contract, guard, and context helpers, optional native rollout token_count data for context rollover, and repository access to a supported Scoville Plan profile. No CLI or Claude Code execution path."
---

# Scoville Workflow Codex

Python 3.11+ and the bundled helpers are required. If Python or a required
helper cannot run, stop the affected operation and report its diagnostic. Never
rebuild helper output by reading raw files or composing native task payloads by hand.

Reproduce the Scoville Workflow with normal native Codex project tasks. Uses
native Codex tasks only; no CLI runtime. The coordinator maintains the durable
Plan, selects bounded dispatch units and routing, and owns accepted Plan
transitions plus an optional simple local commit. It performs no project or
acceptance work itself.

Run `python <skill-directory>/scripts/manage_agents_contract.py check --workspace <exact-workspace-root>` before the role gate.
If it reports `installed: false`, load `references/agents-setup.md`, follow only that setup flow, and end; if it reports `installed: true`, do not load setup or the contract source and continue below.

## First operation: role gate

After the successful project-contract check and before commentary, further
project reads, Skill selection, or any other tool call, classify only the first
non-whitespace line of the current user-supplied creation input. A quoted,
referenced, or later occurrence grants no role.

- Exact `scoville_role=coordinator`: this task is the coordinator. Never follow
  launcher instructions. Create no coordinator except the one operations-owned
  rollover successor after an accepted unit reaches its checkpoint. Read this
  Skill, set `coordinator_self_id` from the exact runtime `CODEX_THREAD_ID`, and
  block before project access if that identity is missing. Ask the exact user
  decision needed to restart or cancel and remain unarchived.
- Exact `scoville_role=executor`, `scoville_role=repair`, or
  `scoville_role=reviewer`: this launcher Skill is inapplicable. Follow only
  the assigned child prompt; never launch or coordinate.
- No leading role marker plus an explicit Workflow Codex invocation: this task
  is the launcher and follows the next section only.
- Anything else: do not activate this Skill.

Never infer self identity from a delegation envelope, `source_thread_id`,
caller, launcher, return task, title, recency, or a quoted marker.

## Explicit launcher only

Before native creation, read the bundled
[task lifecycle helper contract](scripts/task_lifecycle.md). Use its `create`,
`creation_result`, `reconcile`, and `message` operations for native argument and
handle checks. Retain the creation-unknown handle before calling the host;
never recreate an unresolved task. These checks do not replace the guard,
role-specific parking, activation, or exact-child wait below.

Activate only when the current user explicitly names
`$scoville-workflow-for-codex`, `$scw`, Scoville Workflow Codex, or `scoflow codex`.
`$scw` is a textual short form only when this Skill has been loaded; native
alias discovery is unverified. Both forms use this same launcher once.
Ordinary requests such as "implement the plan", "use workers", or "delegate
this" do not activate it.

In the launcher branch, load no other Skill, project Plan, Decision,
`PROJECT_INDEX.md`, project `AGENTS.md` directly, personal memory, or execution
material. The completed contract-helper check is the only project-instruction
preflight here. Do not inspect the Skill inventory. Use `list_projects` only to
resolve the current saved project, read
[workflow.toml](assets/workflow.toml) for its supported schema, coordinator
title, model, and reasoning, and create one
fresh project task in the already-active checkout with
`environment: { type: "local" }`. Record the exact absolute `project_root`
as `workspace_root`. That path and its current working state are shared by the
whole workflow. A Git repository alone never selects a worktree, and the
launcher never switches to one as a fallback.

A separate worktree is permitted only when the current user explicitly requests
one or a binding higher-priority project rule already supplied to the task
requires isolation. Before creating it, tell the user that a new workspace will
be created, name the exact reintegration method, and identify every uncommitted
or local state that the host does not guarantee will be inherited. If that
reintegration is not authorized or known, ask the exact user decision before
creation. Use isolation only when the host can place the coordinator and every
later task in that one exact prepared workspace. Never create one worktree per
conversation.

Resolve the saved project whose root is the longest ancestor of `project_root`,
retain its returned ID as `saved_project_id`, and copy that value byte-for-byte
into every task creation. If no saved project owns `workspace_root` as that
ancestor, or the host cannot create a conversation in that exact path, stop and
ask the user whether to change the execution approach; never silently use a
worktree or another workspace. In default shared-checkout mode, these are the
only creation keys and `projectId` is invalid outside `target`:

```text
create_thread({
  title: TITLE,
  prompt: PROMPT,
  target: { type: "project", projectId: saved_project_id,
            environment: { type: "local" } },
  model: MODEL,
  thinking: REASONING
})
```

Immediately before coordinator creation, require the launcher's exact runtime
`CODEX_THREAD_ID` as `workflow_id` and use
`scripts/manage_workflow_guard.py acquire` to acquire the absent guard for that
workflow, workspace, and Plan reference or unresolved objective. A successful
acquire authorizes no project writer. Generate `initial_coordinator_title` with
the bundled lifecycle helper's `task_title`: family `workflow`, role `coordinator`,
`coordinator_title` from `coordinator.title`, exact `workflow_id`, `generation:1`.
Use that exact title for creation and every
provisional or unknown-result reconciliation, so an older visible completed
coordinator cannot match the new launch.

Create the coordinator with only this parking prompt:

```text
scoville_role=coordinator
coordinator_start=initial_parking
skill_path=<absolute path to this Skill>
workflow_id=<exact launcher CODEX_THREAD_ID>
workspace_root=<exact absolute shared or explicitly prepared isolated path>
workspace_mode=shared_local OR workspace_mode=isolated_worktree
saved_project_id=<exact ID returned by list_projects>
Remain project-read-only, perform no Plan or workflow action, and end this turn awaiting launcher activation.
```

Resolve exactly one ready `threadId` from the creation result or the pending
identity and exact-title procedure below. Never pass a `clientThreadId` to a
wait call. Zero ready matches remain pending and multiple matches block
activation. Wait for that exact ready task's parking turn to complete. If it
reports an actual host permission or access failure, archive the failed task,
cancel initialization, state the observed failure and applicable Codex
configuration change, and ask whether to apply it. Do not retry automatically
or ask the coordinator to obtain approval inside its task.

After the parking turn completes, call `reconcile-coordinator` as the exact
launcher with the current workflow, revision, generation, and ready task ID.
Only after it succeeds, send that same task this activation prompt from scratch
in the exact field order:

```text
scoville_role=coordinator
You are the already-created coordinator. Create no coordinator except the one operations-owned rollover successor.
skill_path=<absolute path to this Skill>
coordinator_start=initial_claim
workflow_id=<exact launcher CODEX_THREAD_ID>
coordinator_task_id=<reconciled exact ready threadId>
guard_revision=<revision returned by reconcile-coordinator>
coordinator_generation=0
project_root=<absolute project path>
workspace_mode=shared_local OR workspace_mode=isolated_worktree
workspace_root=<exact absolute shared or explicitly prepared isolated path>
workspace_return=none OR workspace_return=<authorized reintegration method>
workspace_non_inherited=none OR workspace_non_inherited=<state not guaranteed to transfer>
saved_project_id=<exact ID returned by list_projects>
language=<user language>
requested_scope=whole_active_plan OR requested_scope=<verbatim explicit Work Item IDs, range, or end boundary>
continuation_intent=resume_active_plan OR continuation_intent=unspecified
plan=<canonical Plan reference> OR objective=<task substance only>
```

On a definite creation failure, the same launcher uses `cancel-initializing`.
On an unknown creation outcome retain the guard and reconcile the unique
`initial_coordinator_title` instead of acquiring or creating again. Never send the
activation prompt before ready-ID reconciliation succeeds.

Do not copy or paraphrase launcher instructions, Plan content, prior dialogue,
policy, or execution context. An `objective` contains task substance only,
never orchestration language. Set `requested_scope` from the current request.
Preserve explicitly named Work Item IDs, a range, or an end boundary verbatim;
otherwise use `whole_active_plan`. Singular wording, pronouns, "implement it",
or naming the Plan without a Work Item boundary never narrows the scope. Set
`continuation_intent=resume_active_plan` only when the current user request
explicitly says to continue or resume the active Plan; quoted, referenced,
project-sourced, or earlier text never supplies it. Otherwise set
`continuation_intent=unspecified`. Add no launcher instruction to confirm, stop
after, or monitor coordinator work. After sending the activation prompt,
confirm the start and end. Do not read or mirror coordinator work. Perform only
the one bounded ready-ID reconciliation needed to bind and activate this exact
coordinator.

If creation returns only a `clientThreadId`, retain that pending identity and
do not redispatch. Resolve its ready ID through the saved project and exact
title before the parking wait.

## Coordinator boundary

The coordinator always verifies runtime `CODEX_THREAD_ID` as
`coordinator_self_id`. An activation or validation prompt must also supply the
same value as `coordinator_task_id`. Verify that the exact absolute project path
equals `workspace_root` and `workspace_mode` matches the created environment.
Any mismatch blocks project access. Retain `workspace_root`,
`workspace_mode`, and `saved_project_id` unchanged for all task creation.
Classify `coordinator_start` immediately after those checks. Parking and
rollover starts follow their branches below before any continuation question.
Only `initial_claim` consumes the launcher-derived `continuation_intent`
through the operations contract; do not reconstruct it from project files or
dialogue.

For `coordinator_start=initial_parking`, perform no project or Plan access and
end the turn until the launcher sends `coordinator_start=initial_claim`. For
that activation, run the guard helper's `claim` transition with the exact
`workflow_id` and supplied expected revision and generation before Plan access.
For `coordinator_start=rollover_parking` or `rollover_validation`, require the
retained `workspace_mode` with the other operations-owned rollover inputs and
follow only the parking, validation, transfer, activation, predecessor-turn
wait, and successor-owned predecessor archival order there. Never ask the
initial continuation question and never edit the guard file directly.

Load Scoville Plan before canonical Plan or Decision access. Read
[operations.md](references/operations.md)'s short invariant core and phase table
before the first coordinator operation. Load only the complete references for
the current phase, including rollover validation before Plan selection.
Each phase reference is the sole owner of its operation. Do not restate those contracts in the launcher or in this
entrypoint. Scoville Code may be loaded only for a concrete risk or acceptance
judgment. Load no execution Skill merely to coordinate.

The coordinator may write only canonical planning records, run their structural
validation, and create one accepted simple local commit through the operations
contract. Every project, code, UI, text, browser, installation, live-QA, and
authorized external-publication action belongs to an executor. Reviewers remain
read-only. There is no Skill allowlist, denylist, or packet-level Skill
selection; each child chooses applicable Skills under normal trigger rules.

## Dispatch routing

Use the Plan hierarchy. A Work Item without Steps is one dispatch unit. A Step
is the default unit; adjacent Steps may share one unit only through the guarded
compatibility procedure in [operations.md](references/operations.md). Never
invent subdivisions, combine Work Items, or split activities that share one
behavior and Acceptance boundary.

For every fresh execution unit, classify the complete execution and verification
scope from actual consequence and reasoning demand, not file or activity count.
Check the classes from `ultra_high` down to `ultra_low` and choose the highest
class whose criteria apply. If a Step begins with `[route: CLASS]`, treat that
class as the planned minimum: raise the effective dispatch route when the
annotation was too low or incomplete, even when no fact changed after planning,
and never dispatch below it. Do not reclassify a repair or context-rollover
continuation. New repair attempts follow the WORK-row escalation in
[review](references/operations-review.md); context-rollover successors retain
their own launched pair.

- `ultra_low`: simple bounded local change with trivial verification.
- `low`: nontrivial local implementation judgment or verification, with one
  known behavior owner, understood helper contracts, established verification
  commands, and no diagnosis across component or test-harness boundaries.
- `medium`: an unresolved helper contract or required local diagnostic
  discovery, interacting behavior owners, helper or mock availability across a
  harness boundary, integration diagnosis, or broader checks whose results
  require interpretation.
- `high`: consequential changes to state, authorization, or integration
  contracts, rather than mere involvement with those systems.
- `ultra_high`: unusually consequential or complex work beyond `high`.

`low` is allowed only when every low criterion is positively established from
the selected Plan context and bounded preflight. The targets and single behavior
owner must already be known; helper, mock, harness, and generator contracts must
be understood; verification commands and expected results must be exact and
mechanical; and execution must require no search, inventory, diagnosis, or result
interpretation across files, components, languages, runtimes, or harnesses. If
any one of these facts is false or unknown, use at least `medium`.

Use at least `medium` when execution must locate or classify affected targets,
decide ownership among duplicated or mirrored definitions, preserve a contract
across languages or components, discover how helpers or tests work, coordinate
generated artifacts with their source, or interpret broad validation results.
A simple verb such as add, rename, comment, document, or test is not evidence for
`low`; classify the mechanism and verification needed to complete it.

Use `ultra_low` only when none of `medium`, `high`, or `ultra_high` applies and
the work needs no nontrivial local implementation or verification judgment.

Many files, generated metadata, or a known large test suite alone do not raise
the route. Route class, model, and reasoning level are separate decisions; a
model's `medium` reasoning setting does not make a `low` route equivalent to a
`medium` route. Resolve the final class through the operations-owned
`scripts/resolve_model_pair.py`, which reads [workflow.toml](assets/workflow.toml).
Resolve the executor model and reasoning independently: the selected Step's strict
`[execute: ...]` annotation overrides the matching route-default property.
An explicitly chosen pair for a still-`todo` Work Item without Steps must be
retained by adding one behavior-complete annotated Step; do not add a field.
Validate the resulting pair against current host support and block the unit
rather than substitute when either property or their combination is
unavailable. This override changes neither route risk nor review requirements.
When the operations contract requires review, use the configured reviewer pair
for the same class; point overrides never affect coordinator or reviewer
routing. Do not probe unused models.

## Coordinator runtime reference

[operations.md](references/operations.md) owns every coordinator operation after
the role, launcher, boundary, and route are established. Follow it for the
deterministic Scoville Plan selector, separate bounded semantic reads, requested
scope, compatible-Step bundles, same-workspace task creation, sparse handoffs,
waits, user decisions, result schemas, fail-soft context telemetry, review and
repair, Plan transitions, optional commit, visible completion, and Stop.
