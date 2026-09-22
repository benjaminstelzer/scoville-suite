# Native Codex operations

Use only normal Codex project-task controls. There is no coordinator CLI runner, private
worker home, process supervisor, SQLite state, snapshot, adoption, or Skill list.
The entrypoint owns only the role gate, launcher, coordinator boundary, and
routing classes. This index owns shared invariants and phase routing. Each linked phase owns its
operation; do not copy those contracts into other files.

The project-root `AGENTS.md` contract is cooperative. It reaches native tasks
that receive project instructions, but it is not a filesystem lock. A native
task, editor, or external process can ignore it. The guard helper serializes its
own state transitions; contract and workspace checks detect later drift and
fail closed without claiming to identify or physically stop its source.

## Required invariants

Every later guard transition supplies the current workflow ID, revision and
generation and is accepted only from the runtime `CODEX_THREAD_ID` permitted by
the current state. The coordinator never edits guard JSON directly. Invalid,
busy, wrong-workflow, stale-generation or stale-revision results stop writes and
preserve the observed file. Before each coordinator Plan write, call `verify`
with `role=coordinator` and `capability=plan`; before staging or committing,
verify `capability=stage_commit`; a writer verifies `capability=source` with its
exact unit and dispatch key. Reviewers and other read-only checks require the
successful `read_only` result rather than write authorization.

The coordinator's sole self-identity owner is its exact runtime
`CODEX_THREAD_ID`. Keep it as `coordinator_self_id`. Never substitute a
delegation `source_thread_id`, launcher ID, caller ID, return-task ID, title, or
the newest visible task. A missing or changing self identity is a blocker before
project reads, dispatch, Plan mutation, commit, or archival. Ask the exact user
decision needed to restart or cancel and remain unarchived.

The canonical Plan is the workflow's only durable progress owner. The launcher,
coordinator, and children never call `create_goal` for the workflow objective and
never create another automatic or scheduled continuation mechanism. Treat user
instructions such as "set this as your goal", "finish the complete Plan", "keep
going", or "stop only for a decision" as requested scope and continuation intent
inside this operations loop, not as authorization to create a persistent Codex
goal. A persistent goal would create a second continuation owner beside the
coordinator's exact-child wait loop and is therefore incompatible with one
authoritative coordinator.

If a persistent Codex goal from an older run is already active, do not dispatch
a new child under it. When the user explicitly asks to pause that goal, call
`update_goal` with `status=paused`, report the returned status, and continue the
Scoville workflow only through its coordinator-owned wait loop. Pausing that
Codex goal does not pause the canonical Plan or cancel an already active child.
Without that explicit pause instruction, ask for it once and perform no wait,
poll, status narration, or project transition from automatic goal-continuation
turns.

## Load by phase

Read this core and the row's references completely before the action. At a
phase change, load only newly required references. Follow each phase's explicit
links before crossing into that operation; never interpret “above/below” as
permission to skip another owner's gates.

Reuse a reference only while its complete contents remain available and its
source is unchanged. A read marker or hash alone is not the contents. After
compaction or context loss, reload this core and the currently required phases;
do not reload unrelated phases. On a changed source or incomplete read, load
the affected full reference before its action. Never act on a truncated rule.
Do not routinely hash or reread unchanged available instructions. Live Plan,
guard and delivery evidence still need their operation-specific fresh checks.

| Next action | Required references |
| --- | --- |
| Initial activation and intent | [activation](operations-activation.md), [scope](operations-scope.md) |
| Select/form a unit | [scope](operations-scope.md), [selection](operations-selection.md), [dispatch](operations-dispatch.md) |
| Create, activate or send a child | [activation](operations-activation.md), [selection](operations-selection.md), [wait](operations-wait.md) |
| Wait or report exact child status | [wait](operations-wait.md) |
| Recover or validate completed result | [wait](operations-wait.md), [results](operations-results.md) |
| Review, repair, archive or resume terminal-child cleanup | [results](operations-results.md), [review](operations-review.md) |
| Child compaction or context handoff | [compaction](operations-compaction.md), [checkpoint](operations-checkpoint.md), [review](operations-review.md) |
| Accept, commit or finish scope | [review](operations-review.md), [accepted](operations-accepted.md), [scope](operations-scope.md), [rollover](operations-rollover.md) |
| Coordinator boundary or rollover start/validation/activation | [rollover](operations-rollover.md), [activation](operations-activation.md), [wait](operations-wait.md) |
| Stop or cancellation | [stop](operations-stop.md), [wait](operations-wait.md), [review](operations-review.md) |
| Failure or interrupted operation | Reload the interrupted phase; apply its failure branch before any new phase. Unknown dispatch uses activation's transport recovery; ambiguous results use results; interrupted rollover uses rollover. |
