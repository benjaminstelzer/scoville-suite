# Task lifecycle

Python 3.9+. Pipe one JSON object to:
`python "<skill-dir>/scripts/task_lifecycle.py"`

PowerShell UTF-8: `$OutputEncoding = [System.Text.UTF8Encoding]::new($false)`

Each request contains `operation` plus the fields below. Exit nonzero or
`ok:false`: stop the operation. Otherwise pass only `arguments` to the named
Codex tool. The helper makes no host calls. Authorization and result validation remain with the Skill. Claude CLI is separate.

Use actual host evidence. Never invent IDs or set evidence flags without proof.
Retain returned `handle` values in the existing task/Plan record.

## Create and resolve

| Operation | Required fields | Result and next action |
| --- | --- | --- |
| `create` | Title inputs below plus `projectId`, `reference`, `prompt`, `model`, `thinking`, `creation_authorized:true`, `prior_state:not_started` | Save returned handle **before** one `create_thread` call. |
| `creation_result` | `handle`, actual decoded creation `reply` | Save updated handle. `threadId` + `hostId` means ready. `clientThreadId` means pending. Missing identity stays unknown. |
| `reconcile` | pending/unknown `handle`, `entries` from normal and pinned task lists | Exactly one Codex entry matching project, full title and required reference becomes ready. Zero stays unresolved. Multiple matches block. |

For `create`:
- `family:workflow` uses role `coordinator|executor|reviewer|repair`.
  Start `prompt` with the exact `scoville_role=<role>\n` marker. The helper
  inserts `workflow_reference=<reference>` immediately after it.
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
for creation and retained records.

| `family` / `role` | Additional inputs | Output |
| --- | --- | --- |
| `workflow` / `coordinator` | `plan_id`, `run_number` | `S-MNGR-#<n>-PLAN-NNNN` |
| `workflow` / `executor`, `reviewer`, `repair` | `unit`, `run_number` | `S-WORK`, `S-REVW`, `S-FIXR`, each followed by `-#<n>-W-NNN/STEP-N` (omit Step for a whole item) |
| `ask` / `adviser` | `caller_title`, selected `model` | `Ask <model> · <caller_title>` |
| Legacy Ask / `adviser` | `subject`, `adviser`, `attempt` | `ASK <subject> <adviser> RUN [#<n>]` |

Preserve the original caller title, including Unicode and brackets. Reject
control characters. `run_number` is the positive task counter for that role,
not the workflow run ID. Each role starts at 1 within a fresh workflow run.
Every new task of that role, including a rollover successor, receives its next
number. Same-task continuation and uncertain-creation reconciliation retain it.
Child `unit` is the exact selected Plan unit, including its Step when present.
Preserve it during rollover. Workflow titles use uppercase for display only;
canonical IDs and dispatch inputs remain unchanged. Include no caller or Work
Item title in Workflow labels.
Legacy Ask labels keep their existing
limits: subject 80, adviser 32 and complete title 160 characters.

New Workflow and caller-title Ask handles require `workflow_reference` or
`consultation_reference` respectively during reconciliation. Obtain that marker
from the actual candidate task's prompt when listings omit it. A matching title
alone is insufficient. Supply known predecessor IDs as `prior_task_ids` to
`create`; reconciliation excludes them. Never rename another task or a task
found through reconciliation, or replace a ready ID with a title match.
Workflow registers and names its own initial calling coordinator under its
startup procedure. Claude CLI creates no native task.

## Message and receive

`message`: ready `handle`, `prompt`, `delivery_state:not_sent`.
Optional `model`/`thinking` follow the Skill's setting rules.
Check authorization and open-task state first. Record the intended send,
then call `send_message_to_thread`. Unknown previous delivery blocks replay.
A send does not prove execution started.

`match_delivery`: `handle`, `expected_scope`, `delivery` containing
`threadId`, `reference`, `scope`, `complete`, `body`.
Use the host envelope's sender. Set `complete:true` only after content validation.
This checks identity/scope, not substantive correctness. Keep the Skill's
result validation and native completion checks. Receipts are not answers.

## Archive

`archive`: ready `handle`, observed `status`, `result_retained:true`.
Call `set_thread_archived` only when these additional rules hold:

| Task | Required evidence |
| --- | --- |
| Workflow executor, reviewer or repair | Actual task completion and retained terminal result/failure. Accepted statuses: `completed`, `pass`, `changes_requested`, `blocked`, `context_handoff`, `failed`, `replaced`. |
| Workflow rollover predecessor, including coordinator | Additionally `predecessor_ended:true` and `successor_started:true`, based on actual completion and successor takeover. Pending creation alone is insufficient. |
| Successful Ask adviser | `status:completed` and `explicit_yes_in_adviser:true` from the user's answer in that task. |
| Failed Ask adviser | `status:failed` and `failure_rule_applies:true`. |
| Authorized Ask cleanup | `explicit_cleanup_authorized:true` and terminal status `completed|failed|cancelled|replaced`. |

Active, pending and `needs_user_decision` tasks stay open. Keep the final
Workflow coordinator visible. Archive the exact retained task/host ID, never a
title match or an entire group.

`verify_archive`: same ready `handle`, actual decoded `reply`.
Only a non-error reply with exact `threadId` and boolean `archived:true` proves
archival. Completion, list absence and a textual success claim do not.
Workflow records one archive attempt and its outcome with the handle. Report
failure or uncertainty without blocking accepted work or retrying on resume.
Ask retains its own cleanup and consent rules.
