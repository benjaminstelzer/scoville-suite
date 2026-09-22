# Coordinator rollover check

After activation, run a fresh guard `capability=plan` check. Then call
`task_lifecycle.py` with `operation:rollover_readiness` and these fields:

| Field | Required source |
| --- | --- |
| `guard`, `guard_capability_verified:true` | Guard object from that successful check. |
| `workflow_id`, `generation` | Expected handoff identity and successor generation. |
| `successor`, `predecessor` | Retained ready handles. |
| `exact_successor` | Exact-ID host read: `threadId`, `hostId`, `reachable:true`. |
| `activation_turn_id` | Retained predecessor activation turn ID. |
| `predecessor_turn` | Native completion proof: `threadId`, `hostId`, `turnId`, `status:completed`. Idle state is insufficient. |
| `listing` | Actual `list_threads` response. |
| `status_retained:true` | Successor has posted or retained the current user-facing phase or blocker. |

On helper error, stop. On `may_continue:true`, ordinary guarded selection may
continue. This grants no writer authority.

- Retain `archive_record` in the existing handoff record, including when an
  archive call fails. It contains
  identity and completed-turn evidence, not fresh authority.
- `may_archive_predecessor:false`: retain `archive_blockers`. At the next
  accepted-unit boundary before selection or rollover, retry once with the
  record plus `operation:rollover_readiness`, a fresh verified guard, exact
  successor read, actual listing and current `status_retained`. Never reuse
  an earlier archive permission. Missing visibility still permits continuation;
  do not add polling. Preserve unresolved records across handoff or completion.
- `may_archive_predecessor:true`: call `set_thread_archived` with
  `archive_arguments`. Require `verify_archive` for that predecessor before
  advancing the associated transition. Archive failure blocks that transition.
  If an inherited chain is open, use the recovery operation below instead of
  separately archiving the immediate predecessor.

Never create a replacement successor because a task is absent from the list.

## Older open predecessors

Pass `archive_chain` and `archive_receipts` with each successor validation and
activation message. Append the new `archive_record` after activation. Keep all
links from the oldest unresolved predecessor through the current coordinator;
an archived intermediate coordinator still supplies a required chain link.

At activation and each accepted-unit boundary, use
`operation:recover_rollover_archives` with the current rollover fields above,
`archive_chain` (oldest first), and `archive_receipts` (default `[]`). The helper
requires one workflow, consecutive generations, linked exact IDs/hosts, completed
activation turns and the current fresh guard/visibility proof. Never reconstruct
missing links from titles or fabricate completion evidence; report a missing
chain and preserve its tasks.

Call each returned `archive_arguments` entry sequentially. After each success,
run `verify_archive` and retain `{threadId,hostId,reply}` in `archive_receipts`,
using the actual decoded host reply. Stop on a failed or unknown archive result;
retain outstanding targets for the next meaningful boundary. A later recovery
skips verified receipts. Empty arguments plus nonempty `pending_predecessors`
means deferred, not complete. Discard the chain only when no predecessor remains.
