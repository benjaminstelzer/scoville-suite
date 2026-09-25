---
name: scoville-workflow-for-codex
description: Explicit native-Codex Scoville workflow. It first verifies the project's short write contract; missing setup asks the user and ends. An installed launcher creates one native coordinator. A task whose first non-whitespace input line is scoville_role=coordinator is that coordinator and may create only the operations-owned rollover successor. Use only for $scoville-workflow-for-codex, Scoville Workflow Codex, or scoflow codex, never ordinary planning, implementation, review, delegation, or worker requests.
compatibility: "Codex desktop with saved local projects, native task creation in the same local checkout, waiting, messaging, archival controls, access to CODEX_THREAD_ID, Python 3.11+ standard library for contract, guard, and context helpers, optional native rollout token_count data for context rollover, and repository access to a supported Scoville Plan profile. No CLI or Claude Code execution path."
---

# Scoville Workflow Codex

All Skills included in this suite must be installed and enabled. Use the
applicable owner without checking sibling availability. Load only instructions
needed for the task. Explicit invocation gates and user exclusions still apply.

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

Additional instructions for every coordinator, worker and reviewer use this
Skill's [prompting] configuration in `assets/workflow.toml`, independently of
Plan's settings. Use the bundled `scripts/resolve_prompt_profile.py` for the
actual recipient model; the dispatch builder applies it automatically. Apply
its common rules and selected profile to additional prose only. Pass canonical
Plan source_text unchanged. Never assume conversation history. Coordinator
creation and rollover use the same helper and retain their fixed contracts.

## Complete coordinator startup

Before every coordinator creation or coordinator startup message, including
initial parking, initial claim, rollover parking, validation and activation,
pipe `{"prompt":"<the phase-defined coordinator prompt>"}` to
`python <skill-directory>/scripts/coordinator_contract.py build`.
Require exit 0 and pass its returned `prompt` unchanged through the lifecycle
helper to the native task tool. Capture the full JSON in execution memory;
print only a receipt, never reconstruct or truncate the prompt.
The builder supplies the exact `skill_path` and the complete normal coordinator
contract. A path alone is insufficient. Every start uses this same builder.
Only normal `create_thread` project tasks are supported. Never substitute
`collaboration.spawn_agent`, `followup_task`, a fork or a CLI worker.

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
The title is `SCW COORD G<N> [<workflow_id>]`: keep the full workflow ID last.
Use that exact title for creation and every
provisional or unknown-result reconciliation, so an older visible completed
coordinator cannot match the new launch.

Use this parking input for the coordinator-contract builder:

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
Only after it succeeds, build and send that same task this activation input from scratch
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

Read the complete supplied coordinator runtime contract before project access.
If it is missing, remain read-only and report the invalid startup. The guard
verifies its exact native creation envelope before coordinator capability.
Load Scoville Plan before canonical Plan or Decision access. Scoville Code may
be loaded only for a concrete risk or acceptance judgment. Load no execution
Skill merely to coordinate.

The coordinator may write only canonical planning records, run their structural
validation, and create one accepted simple local commit through the operations
contract. Every project, code, UI, text, browser, installation, live-QA, and
authorized external-publication action belongs to an executor. Reviewers remain
read-only. There is no Skill allowlist, denylist, or packet-level Skill
selection; each child chooses applicable Skills under normal trigger rules.

## Dispatch routing

[operations-dispatch.md](references/operations-dispatch.md) owns the complete
route eligibility, model and reasoning rules. Read that contract before fresh
dispatch classification. Writing depth never changes route or authority.

## Coordinator runtime reference

[operations.md](references/operations.md) owns contract delivery and conditional
routing. `coordinator_contract.py` supplies the normal loop completely, including
selection, dispatch, waiting, result handling, review, acceptance and Stop.
The linked phase files are its canonical source fragments. The coordinator
need not discover or choose them. Only actual rollover and worker context
recovery require their conditional references.
