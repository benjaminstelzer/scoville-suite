# Task lifecycle

Python 3.9+. Pipe one JSON object to:
`python <skill-dir>/scripts/task_lifecycle.py`

PowerShell UTF-8: `$OutputEncoding = [System.Text.UTF8Encoding]::new($false)`

Each request contains `operation` plus the fields below. Exit nonzero or
`ok:false`: stop the operation. Otherwise pass only `arguments` to the named
Codex tool. The helper makes no host calls. Authorization, Workflow guard
checks and result validation remain with the Skill. Claude CLI is separate.

Use actual host evidence. Never invent IDs or set evidence flags without proof.
Retain returned `handle` values in the existing task/Plan record.

## Create and resolve

| Operation | Required fields | Result and next action |
| --- | --- | --- |
| `create` | Title inputs below plus `projectId`, `reference`, `prompt`, `model`, `thinking`, `creation_authorized:true`, `prior_state:not_started` | Save returned handle **before** one `create_thread` call. |
| `creation_result` | `handle`, actual decoded creation `reply` | Save updated handle. `threadId` + `hostId` means ready. `clientThreadId` means pending. Missing identity stays unknown. |
| `reconcile` | pending/unknown `handle`, `entries` from normal and pinned task lists | Exactly one Codex entry matching project and full title becomes ready. Zero stays unresolved. Multiple matches block. |

For `create`:
- `family:workflow` uses role `coordinator|executor|reviewer|repair`.
  Start `prompt` with the exact `scoville_role=<role>\n` marker.
- `family:ask` uses `role:adviser` and also requires `return_to_thread_id`.
  Supply the fixed adviser role followed by the question. The helper adds
  the role marker, consultation reference and return destination.
- `reference` is the unique dispatch/consultation key. Resolve model and effort
  first. Creation uses the saved project's local checkout. For explicitly
  isolated work, use the Skill's placement procedure instead.
- Set `not_started` only before any creation attempt. Pending or unknown
  creation must be reconciled, never recreated. This is not a host-level lock.
- List entries use native `id`, `kind`, `hostId`, `projectId`, `title`.
  The helper maps Codex `id` to `threadId`. Never replace a known ready ID by
  title matching. Keep the Skill's existing reconciliation timing.

## New-task titles

`task_title` returns `title` without creating anything. `create` uses the same
inputs and formatter; optional supplied `title` must match. Use its exact output
for guard registration, creation, retained records and user-facing run labels.

| `family` / `role` | Additional inputs | Output |
| --- | --- | --- |
| `workflow` / `coordinator` | `coordinator_title` from config, `workflow_id`, `generation` | Default `SCW COORD [<workflow_id>] G<N>` |
| `workflow` / `executor`, `reviewer`, `repair` | `unit`, `attempt` | `SCW <unit> WORK`, `REVIEW` or `REPAIR RUN [#<N>]` |
| `ask` / `adviser` | `subject`, `adviser`, `attempt` | `ASK <subject> <adviser> RUN [#<N>]` |

Use the exact Plan/unit label and resolved adviser label (`ASTRA`, `SOL`, or
`CLAUDE`). Numbers are positive integers. Labels have no outer whitespace,
controls or brackets: unit/subject max 80 characters, adviser max 32, workflow
ID max 64; coordinator title max 32; full title max 160. This is a helper limit, not a verified host limit.
Do not truncate identifiers. On overflow, choose a shorter unambiguous label.

`attempt` is the retained logical attempt, not a success claim. A replacement
within the same attempt retains it. Reconcile only against that creation's
saved evidence. Supply known predecessor IDs as `prior_task_ids` to `create`;
reconciliation excludes them. An older same-title task is not proof of a new task. Ambiguous
matches block creation recovery. Never rename existing tasks or replace ready
IDs with titles. Claude uses the label for its CLI result, not a native task.

## Message and receive

`message`: ready `handle`, `prompt`, `delivery_state:not_sent`.
Optional `model`/`thinking` follow the Skill's setting rules.
Check authorization, guard and open-task state first. Record the intended send,
then call `send_message_to_thread`. Unknown previous delivery blocks replay.
A send does not prove execution started.

`match_delivery`: `handle`, `expected_scope`, `delivery` containing
`threadId`, `reference`, `scope`, `complete`, `body`.
Use the host envelope's sender. Set `complete:true` only after content validation.
This checks identity/scope, not substantive correctness. Keep Workflow's
role-result, delivery-key and native-turn checks. Receipts are not answers.

## Archive

`archive`: ready `handle`, observed `status`, `result_retained:true`.
Call `set_thread_archived` only when these additional rules hold:

| Task | Required evidence |
| --- | --- |
| Workflow child | Terminal status from Operations. For `unassigned_parking`, also `parking_turn_completed:true` and `assignment_not_sent:true`. |
| Successful Ask adviser | `status:completed` and `explicit_yes_in_adviser:true` from the user's answer in that task. |
| Failed Ask adviser | `status:failed` and `failure_rule_applies:true`. |
| Authorized Ask cleanup | `explicit_cleanup_authorized:true` and terminal status `completed|failed|cancelled|replaced`. |

Active, pending and `needs_user_decision` tasks stay open.
Coordinator archival uses the rollover contract, not `archive`.

`verify_archive`: same ready `handle`, actual decoded `reply`.
Only exact `threadId` plus boolean `archived:true` proves archival.
A completed wrapper or list absence does not. On failure, apply the Skill's
bounded reconciliation rule. Do not advance a transition requiring archival.
