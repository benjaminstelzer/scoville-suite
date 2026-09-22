# Coordinator rollover check

After activation, run a fresh guard `capability=plan` check. Then call
`task_lifecycle.py` with `operation:rollover_readiness` and these fields:

| Field | Required source |
| --- | --- |
| `guard`, `guard_capability_verified:true` | Guard object from that successful check. |
| `workflow_id`, `generation` | Expected handoff identity and successor generation. |
| `successor`, `predecessor` | Retained ready handles. |
| `exact_successor` | Fresh exact-ID host read: `threadId`, `hostId`, `reachable:true`, `status` from `thread.status.type`. Never infer status from the guard. |
| `activation_turn_id` | Retained predecessor activation turn ID. |
| `predecessor_turn` | Native completion proof: `threadId`, `hostId`, `turnId`, `status:completed`. Idle state is insufficient. |
| `listing` | Actual `list_threads` response, including availability diagnostics. |
| `status_retained:true` | Successor has posted or retained the current user-facing phase or blocker. |

On helper error, stop. On `may_continue:true`, ordinary guarded selection may
continue. This grants no writer authority.

Archive requires the successor's exact ID/host in `listing.threads` OR
`exact_successor.status:active`. A list omission alone is not a failed handoff.
Both paths require complete placement lists, no unavailable hosts/sources, no
successor pin or section entry, retained status and all handoff proofs above.
Missing or non-active exact status cannot replace a missing list entry.

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
activation turns and the current fresh guard/successor proof. Never reconstruct
missing links from titles or fabricate completion evidence; report a missing
chain and preserve its tasks.

Archive only returned predecessor IDs, never the current coordinator. For each
target, in order:

1. Call `set_thread_archived` with its returned arguments.
2. Run `verify_archive` on the actual decoded reply. Require the same target ID
   and `archived:true` before calling the next target.
3. On failure, unknown reply or failed verification: stop the archive loop.
   Keep the full chain, verified receipts and all unverified targets for the next
   accepted boundary. Do not advance this archive transition or claim completion.
4. On verified success: retain `{threadId,hostId,reply}` in `archive_receipts`.
   Only then proceed to the next target.

Recovery skips verified receipts. Empty arguments with pending predecessors
means deferred, not complete. Discard the chain only when none remain.
