# Native tasks

Use the bundled [lifecycle contract](../scripts/task_lifecycle.md) for creation
results, matching deliveries and archival. The ASK `prepare` operation owns new
creation payloads and supplies `caller_title` to the shared helper. New tasks
use the local checkout of the verified saved project, fresh context and exactly
`Ask <selected model ID> · <calling task title>`. Preserve the complete caller
title. No numbering or extra suffix.
Task IDs and per-adviser consultation references distinguish identical titles.

Verify native create, wait, message and archive controls before dispatch. Retain
`prepare`'s handle before calling `create_thread` with only `arguments`.
Feed the actual decoded host result to `task_lifecycle.py` operation
`creation_result`; preserve all added handle fields. A `clientThreadId` is
pending, never a ready task ID. Do not create again after unknown or pending
creation. Resolve through a host-provided ready-ID mapping or a listing entry
whose consultation reference is actually exposed and matches. A same-title
listing alone cannot resolve the new ASK handles.

Track ready tasks with `wait_threads`, retaining host IDs and cursors. Receive
answers directly in the caller and use `match_delivery` with the exact sender,
reference and scope after checking completeness. Do not use `read_thread` to
retrieve an adviser's conversation. Request missing result content through the
existing task, not a replacement. Preserve complete answers and individual
failures before reporting the round's result.

## Follow-ups and archival

For an authorized follow-up, verify that the exact task remains unarchived.
Run `ask.py` operation `followup` with the retained handle, a new reference,
question and scope, and `delivery_state:not_sent`. Defaults come from that
handle; explicit adviser overrides must still validate against fresh
`model/list`. Retain the returned handle before sending its arguments. An
unknown send result must be reconciled before sending again.

Leave successful advisers open. Explicit archival consent in the adviser task,
an explicitly authorized cleanup, or an observed access/permission failure may
use `archive` after retaining the answer or failure. Use `verify_archive` with
the actual reply. On permission failure, report the concrete configuration
issue; do not automatically change permissions or retry. Missing or archived
handles cannot be silently replaced or unarchived for continuation.
