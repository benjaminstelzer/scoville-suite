# Activation phase

Selection and unit formation: [selection](operations-selection.md), [dispatch](operations-dispatch.md). Announce/send/wait: [wait](operations-wait.md). Child result and context rules: [results](operations-results.md), [compaction](operations-compaction.md), [checkpoint](operations-checkpoint.md). Coordinator transfer: [rollover](operations-rollover.md).

## Active-coordinator task creation

This reference begins only after the Core has completed the installed-contract
check, role gate, initial launcher flow, coordinator identity and workspace
checks, and the initial `claim` transition. Consume that verified state; do not
repeat launcher project resolution, guard acquisition, initial coordinator
creation, parking, reconciliation, or activation here.

Retain the exact Core-supplied `workspace_root`, `workspace_mode`,
`saved_project_id`, `workflow_id`, `coordinator_self_id`, guard revision and
generation. Every executor, reviewer, repair and rollover successor created by
the active coordinator uses that same workspace and saved project. In
`shared_local` mode, task creation uses only `title`, `prompt`, `target`, `model`
and `thinking`, with `target: { type: "project", projectId:
saved_project_id, environment: { type: "local" } }`. A top-level `projectId` is
invalid. Never fork a prior task, select a new worktree or reconstruct shared
workspace state.

Before each new route-based executor or reviewer creation, read
`assets/workflow.toml`. Require `schema_version = 1`, exactly one coordinator
triple, and exactly the five documented classes under both `execute` and
`review`, with only model and reasoning in each pair. Unknown or missing values
and unsupported model/reasoning pairs block creation; never substitute a
shipped value. Use the selected `execute.CLASS` pair after any valid Step
override for an executor and the selected `review.CLASS` pair for a reviewer.
Repair and rollover successors inherit the recorded launched pair and do not
reread a changed route default.

The additional `[context]` table requires exactly `coordinator_percent` and
`worker_percent`, integer percentages from 1 through 99. Missing or invalid
configuration blocks creation. The checkpoint helper reads these values on
each call; never substitute a hard-coded threshold.

The Core has already fixed the workspace mode. In `isolated_worktree` mode,
retain the one exact authorized workspace and reintegration contract. Never
create another workspace or one worktree per task. If the host cannot create a
conversation in the retained exact workspace, dispatch nothing and use the user
decision path.

Consume `requested_scope`, `continuation_intent` and `language` exactly as the
Core supplied them. Do not reconstruct them from the Plan, project files, prior
dialogue or a child result. Use the retained language for every user-facing
coordinator message.

Record each returned task ID with its unit and role in the canonical Plan. Give
the bundled [task lifecycle helper](../scripts/task_lifecycle.md) the observed
creation state before each native `create_thread` call; use its returned
`arguments` unchanged and retain its creation-unknown handle before dispatch.
Use `creation_result`/`reconcile` for identity, `message` for send arguments,
and `match_delivery` after the existing role-result and delivery-key checks.
Use `archive` and `verify_archive` for terminal children, retaining the
rollover-specific coordinator handshake below. The helper does not replace
guard authorization or substantive result validation. Generate new titles with
`task_title` before guard registration. Children use the exact Plan/unit label,
role and retained logical attempt: `SCW <unit> WORK|REVIEW|REPAIR RUN [#<N>]`.
Coordinators use configured `coordinator.title`, workflow ID and target generation.
Use the same inputs for `create` and its exact title for all run announcements.
For replacements, pass every retained predecessor ID as `prior_task_ids`;
the helper excludes those IDs from pending reconciliation.
Do not rename existing tasks. RUN means a run, not a successful result.
When creation returns only `clientThreadId`, record that pending ID,
project ID, exact title, role, and unit; never pass it to task tools and never
redispatch. On the next meaningful coordinator turn, use `list_threads` once and
accept only exactly one ready entry matching the saved project and exact unique
title; then record its `threadId` and `hostId`. Zero matches remain pending;
multiple matches or a reported setup failure are blockers. Reconcile again only
after a meaningful state change or user status request, not in a polling loop.
When a higher-priority host rule requires one readiness wait immediately after
task creation, perform only that minimum exact-child wait. It may establish the
ready task ID or deliver an already terminal result; it never starts recurring
active-child supervision and is measured separately during native qualification.
Before creating an executor or repair, re-run the installed-contract check and
verify the current guard, nested governing instructions, and unexplained
workspace drift. Then call `authorize-writer` with one unique dispatch key,
exact unit, role, and unique title. This pending state grants no write right.
Create the child with a minimal parking prompt that contains its role, unit,
workspace, workflow ID, dispatch key, and the instruction to perform no project
read or write and await the actual assignment. Reconcile exactly one ready
`threadId` by the ordinary identity procedure. Call `reconcile-writer`, then
record the exact task identity in the Plan while coordinator `plan` capability
is valid in `writer_pending`. While the writer is still pending, build the
complete prompt with its ready task ID and the predicted activation revision,
which is the current revision plus one.

If construction fails, do not activate. The child's completed parking turn
proves that it received no assignment, so archive that exact unassigned task
and verify its exact archived state, call `clear-writer`, then record the
structured Plan blocker. This unassigned-parking case is the only child
archival path that requires no role-result object. If archival cannot be
verified, keep the pending authorization, record the blocker under coordinator
`plan` capability, and ask for disposition.

After successful construction, call `activate-writer` with the current
revision and require its returned revision to equal the predicted revision in
the built prompt. A definite activation failure sends no assignment; reconcile
the still-pending writer through the same unassigned-parking cleanup. An
unknown activation outcome blocks without sending until the exact guard state
is reconciled. After successful activation, send the required execution or
repair announcement and immediately send the already-built helper output
unchanged to that same task as its explicit start message. A pending child that
acts early is a blocker and never receives write authority.

### Writer activation scenarios

| State | Required action |
| --- | --- |
| Reconciled writer is pending and no failure occurred | Build the complete prompt for the predicted next revision; do not archive or activate yet |
| Prompt construction definitely failed before activation | Archive and verify the exact unassigned parked task, clear its pending authorization, then record the blocker |
| Activation definitely failed and the guard remains pending | Use the same unassigned-parking cleanup |
| Activation outcome is unknown | Send nothing, archive nothing, clear nothing, and reconcile the exact guard state |
| Activation returned the exact predicted revision | Announce the phase and send the already-built prompt unchanged |
| Pending child acted before activation | Record a blocker and never grant write authority |

Reviewers never receive writer authorization. Their complete initial prompt
names the active workflow and guard generation, verifies that their exact role
is read-only, and permits only inspection. After any executor, repair, or
reviewer result, verify contract, guard, and workspace drift before another
transition. Clear the exact writer authorization only after its terminal result
is retained and exact-ID archival is verified, except for the verified
unassigned-parking cleanup above. Missing or foreign changes stop the
transition; do not reset or discard them.

Only for `coordinator_start=initial_claim`, consume the fixed launcher field
after identity and workspace checks. With `continuation_intent=resume_active_plan`,
continue the active Plan immediately;
the explicit current request already answers the initial continue-or-new-task
choice for a fresh coordinator. An explicit current user message delivered
directly to the same coordinator to continue or resume has the same effect and
also bypasses only that initial choice. With `continuation_intent=unspecified`, ask that one
initial choice and dispatch nothing before the answer. Neither value answers a
genuine unresolved scope, authorization, blocker, or lifecycle decision. Do not
reconstruct intent from personal memory, old conversations, project files, or
quoted text.

`coordinator_start=rollover_parking` and `rollover_validation` never consume
`continuation_intent` and never ask the initial continue-or-new-task question.
They follow only the rollover sequence below.

Every child prompt starts with the exact `scoville_role=executor`,
`scoville_role=repair`, or `scoville_role=reviewer` marker and names only its
role and stable unit ID. It states the complete result contract below and
forbids Plan edits, delegation, Git history changes, and activity-based worker
splitting. It says not to load the launcher Skill and expressly forbids loading
or using Scoville Handoff for every workflow, review, repair, decision,
completion, and context-rollover transfer. An executor may perform external or
website publication only when the embedded Plan context explicitly authorizes
that effect. Every initial and successor prompt includes the complete short
native context-checkpoint and post-compaction terminal-gate rules below,
including their unavailable behavior and how `context_handoff` uses the existing
result object. It carries the exact
Git rule: never stage, commit, push, or rewrite history. It includes the exact
absolute `workspace_root`, requires the child to verify that path before project
access, and treats a mismatch as `needs_user_decision`, not as permission to use
another workspace. It makes reviewers fully read-only and grants executors only
Plan-authorized writes and external effects. A required project backup must be
visible inside the projected execution unit itself: put it in the selected Step
before that Work Item starts, or in a referenced Decision when genuinely
plan-wide. The executor creates and verifies it before its first source edit;
the coordinator only checks the returned named result. Work Item `Next action`
alone is not visible to a Step dispatch. Do not rely on the child loading this
Skill.

Build every child prompt with the bundled read-only
`scripts/build_dispatch_prompt.py` helper after the exact runtime unit is known.
In raw diagnostic mode, send no task. For dispatch use the execution-memory
transport below; its envelope contains the same byte-for-byte native task prompt. Add no
summary, handoff prose, rationale, restatement, Plan path, Decision path,
Evidence, or other coordinator text. The helper uses Scoville Plan's named-unit
selector mode and embeds its complete result under one `plan_context` field.
Run the helper in a dedicated command or capture only that process's stdout.
Never combine it with configuration reads, diagnostics, shell transcripts, or
another command's output. Immediately before sending any helper-built prompt,
require byte 0 to begin the exact expected `scoville_role=<role>` line and reject
any preceding or appended non-helper output. Apply this at reviewer creation and
at executor or repair assignment to an activated parking task. Routing
configuration selects the native task call and never appears in the child
prompt.
The executor must not run the Plan selector or prompt builder, load Scoville
Plan, or read Plan or Decision files. Embedded `plan_context` is the complete
planning input and those canonical records remain read-only. Every child may
run only the exact read-only `scripts/inspect_native_context.py` path embedded
by the prompt builder for its post-compaction gate. The role-specific
`scripts/check_context_checkpoint.py` call embedded in the prompt owns its
occupancy checkpoint; children do not locate or calculate telemetry themselves.

The helper receives no role input for an initial executor. Through one JSON
object on stdin, a rollover receives `context_handoff`, a reviewer receives
`executor_result`, and a repair receives `reviewer_result` plus one
`repair_assignment` containing the sorted unique zero-based finding indices it
owns. A reviewer or repair rollover retains its original role input together
with `context_handoff`.
These values remain structured and verbatim. Apply no prompt character target
or hard limit, and never truncate `plan_context` or a required role-result
object. All authorized activities in the unit belong to that one task.
For every child turn, allocate one unique `delivery_reference` and give the
helper the exact `coordinator_self_id` as `return_to_thread_id`. A continuation
in an existing child receives a new reference in the compact continuation
message. References are single-use and bound to exact workflow, unit, role,
logical attempt, child ID after creation, and expected turn.


### Execution-memory dispatch

Load `scripts/dispatch_transport.js` into the execution environment, not model
output: capture its shell-read result, require exit 0, evaluate the complete
expression and call the factory with `store, load`. Retain its source under one
execution-store key; reload only if missing or changed. No Node runtime is
required in Codex code mode.

Use one dispatch key bound to workflow/unit/role/attempt/reference. Never replace
an occupied key. This memory is temporary, not a durable delivery journal.

1. `prepare(key, build)`: `build` calls the builder once with
   `--transport-json --transport-target <writer-ID|project:saved-project-ID>`.
   Pass its complete `{exit_code, output}` result directly; print only the
   returned receipt. Capture enough shell output for the whole JSON envelope.
   Missing/truncated helper output blocks preparation; never dispatch fragments.
2. Complete the existing writer activation procedure. Reviewer creation needs
   no writer activation. Preserve the lifecycle creation-unknown handle before
   the native creation call.
3. `send(key, check, sender)`: `check(envelope)` returns
   `{binding, guard, arguments}`. Obtain `binding` with `--binding-only` using
   the current inputs and exact same role-input stdin; obtain `guard` from a
   fresh successful guard `verify --role audit --capability read_only` with the
   retained workflow/revision/generation. Feed `envelope.prompt` directly to
   lifecycle `message` (writer) or `create` (reviewer); capture its successful
   `arguments` without printing them. Never paste or reconstruct the prompt.
   Fail the callback on any failed/incomplete helper response. Perform no Plan
   or other intervening write between these checks and the native call.
4. `sender(arguments)` calls exactly `send_message_to_thread` for a writer or
   `create_thread` for a reviewer. It returns the actual host response unchanged.
   The helper stores `send_unknown` **before** this call and never retries.
   Print only the returned compact receipt. A response is not delivery proof.
5. Consume `takeReply(key)` inside execution and apply the existing exact-ID
   lifecycle/result rules. Keep identity, reference and observed delivery state
   in their existing Plan/handle owner; create no second journal.

Receipt fields: target, role, reference, Unicode characters, UTF-8 bytes, SHA256,
delivery state. `inspect(key)` returns these without rebuilding or sending.
An abbreviated **display** of a receipt is harmless when the complete payload
remains stored. Abbreviated **helper stdout** is a construction failure.
Unknown, rejected or failed native calls never permit automatic resend.
A lost store is not `not_sent`: reconcile exact native evidence first. If the
assignment is proven unsent, use the ordinary pending-writer/creation recovery
procedure. Never reset a key or invent a fresh reference to bypass uncertainty.
Full-text diagnosis is explicit, read-only and separate from dispatch.
