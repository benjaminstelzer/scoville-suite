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

## Coordinator delivery

The launcher and every rollover predecessor supply one complete runtime contract
through `scripts/coordinator_contract.py build`. The helper composes the normal
phases and task lifecycle directly from their canonical sources, omitting only
labelled scenario examples. These files remain source owners, not optional
reading choices for a running coordinator.

Guard state proves ownership and writer activation, but does not uniquely
distinguish selection, review, acceptance, Stop or recovery. Never select a
phase subset from guard state or a model-supplied phase label. Supply the
complete normal contract. Add the conditional rollover or worker-recovery
reference only when its trigger is observed.

The native creation envelope carries the complete contract, exact Skill path
and content digest. Read it before project access. Do not use
`collaboration.spawn_agent`, `followup_task` or forks for workflow roles.
The guard checks the native creation envelope before granting coordinator
capability, and native writer provenance before binding a writer. Missing,
ambiguous, stale or incomplete evidence blocks the operation. This proves
supplied instructions and transport, not comprehension or a host-level lock.

After compaction or context loss, run `python <skill-directory>/scripts/coordinator_contract.py show`
and read the complete output before continuing. The guard requires that complete
tool-delivered contract after the latest native compaction event before another
coordinator operation. A read marker or hash alone is not the contents. Reload a conditional reference when its contents are lost or
its source changes. Never act on truncated instructions.

The normal contract includes the coordinator checkpoint at every accepted
boundary and the Stop procedure. Load conditional detail only for its trigger:

| Trigger | Required reference |
| --- | --- |
| Actual coordinator rollover | [rollover](operations-rollover.md) and its linked readiness helper |
| Worker context handoff or compaction recovery | [compaction](operations-compaction.md), [checkpoint](operations-checkpoint.md) |
| Missing project contract at explicit launch | [setup](agents-setup.md) |

Guard `read_only`, `clear-writer` and `release` remain available for exact Stop
reconciliation of an older workflow. This exception grants no new writer,
Plan write, commit or successor. Stop before upgrading a live installation;
a changed runtime contract requires a fresh, authorized launch.
