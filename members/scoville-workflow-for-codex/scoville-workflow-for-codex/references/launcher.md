# Explicit launcher

Use this procedure only after the entry point classifies the current task as an
explicit launcher.

## Prepare one native coordinator

Read the bundled [task lifecycle helper contract](../scripts/task_lifecycle.md).
Use its `create`, `creation_result`, `reconcile` and `message` operations. Save
the creation handle before the host call. Never recreate an unresolved task.

Load no other Skill, project Plan, Decision, `PROJECT_INDEX.md`, project
`AGENTS.md` directly, personal memory or execution material. Use `list_projects`
only to resolve the current saved project. Read `../assets/workflow.toml` for
its supported schema, coordinator title, model and reasoning.

Use the current project path as `workspace_root`. Resolve the saved project
whose root is its longest ancestor and retain its exact ID as
`saved_project_id`. Create the coordinator in that saved project's local
checkout. Stop for an execution-approach decision if no saved project owns the
path or the host cannot create a task there. Never silently select another
workspace.

A separate worktree is allowed only when the current user or a binding project
rule explicitly requires it. Before creation, state the reintegration method
and any uncommitted or local state the host may not inherit. If reintegration is
unknown or unauthorized, ask before creation. Every workflow task must use the
same prepared workspace.

The lifecycle helper supplies the `create_thread` arguments. In shared-local
mode they contain exactly this target shape:

```text
target: { type: "project", projectId: saved_project_id,
          environment: { type: "local" } }
```

`projectId` is invalid outside `target`.

## Acquire and park

Require the launcher's exact runtime `CODEX_THREAD_ID` as `workflow_id`. Run
`scripts/manage_workflow_guard.py acquire` for that workflow, workspace and the
supplied Plan reference or unresolved objective. Acquisition authorizes no
writer.

Generate the coordinator title with the lifecycle helper's `task_title` using
family `workflow`, role `coordinator`, `coordinator.title`, the exact workflow
ID and generation 1. Retain the exact title for creation and reconciliation.

Build this parking input through `coordinator_contract.py build` as required by
the entry point:

```text
scoville_role=coordinator
coordinator_start=initial_parking
skill_path=<absolute path to this Skill>
workflow_id=<exact launcher CODEX_THREAD_ID>
workspace_root=<exact workflow workspace>
workspace_mode=shared_local OR workspace_mode=isolated_worktree
saved_project_id=<exact saved project ID>
Perform no project or Plan access, perform no workflow action, and end this turn awaiting launcher activation.
```

Create one native project task with the lifecycle helper's exact arguments.
Resolve one ready `threadId` from the creation result or its pending identity.
Never pass a `clientThreadId` to wait. Zero ready matches remain pending and
multiple matches block activation. Wait for the exact ready task's parking turn.

On definite creation failure, use `cancel-initializing`. On unknown creation
outcome, retain the guard and reconcile the saved exact title. If the parked
task reports a host permission or access failure, archive that failed task,
cancel initialization, report the observed failure and applicable configuration
change, and ask whether to apply it. Do not retry automatically.

## Activate

After parking completes, call `reconcile-coordinator` as the exact launcher with
the current workflow, revision, generation and ready task ID. Only after success,
build and send this activation input in the shown field order:

```text
scoville_role=coordinator
You are the already-created coordinator. Create no coordinator except the operations-owned rollover successor.
skill_path=<absolute path to this Skill>
coordinator_start=initial_claim
workflow_id=<exact launcher CODEX_THREAD_ID>
coordinator_task_id=<reconciled ready threadId>
guard_revision=<revision returned by reconcile-coordinator>
coordinator_generation=0
project_root=<absolute project path>
workspace_mode=shared_local OR workspace_mode=isolated_worktree
workspace_root=<exact workflow workspace>
workspace_return=none OR workspace_return=<authorized reintegration method>
workspace_non_inherited=none OR workspace_non_inherited=<state not guaranteed to transfer>
saved_project_id=<exact saved project ID>
language=<user language>
requested_scope=whole_active_plan OR requested_scope=<verbatim explicit Work Item IDs, range, or end boundary>
continuation_intent=resume_active_plan OR continuation_intent=unspecified
plan=<canonical Plan reference> OR objective=<task substance only>
```

An objective contains only task substance. Copy no Plan content, dialogue,
policy or launcher instructions. Preserve an explicitly named Work Item, range
or end boundary verbatim. Otherwise use `whole_active_plan`. Singular wording or
naming only the Plan does not narrow scope. Set `resume_active_plan` only from
the current user's explicit continue or resume instruction. Otherwise use
`unspecified`.

After sending activation, confirm the start and end the launcher. Do not monitor,
read or mirror coordinator work.
