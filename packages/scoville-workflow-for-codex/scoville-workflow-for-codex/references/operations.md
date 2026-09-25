# Execute the requested scope

The caller is the coordinator. There is no launcher task or parked worker.
At startup or resume, read the canonical Plan and `.scoville/workflow.md`.
Keep `.scoville/workflow.md` and `.scoville/handoffs/` local and never commit
them; `.scoville/config.json` may be versioned. Remove completed run state only
after retaining results and finishing any pending handoff. Keep unfinished
state for resume.
An existing child must be reconciled by its retained exact task/host ID before
a new one starts. A saved result is evidence only for what was actually observed.

## One unit through acceptance

1. Select the next eligible unit under Scoville Plan: one Step, or the complete
   Work Item if it has no Steps. Check its assumptions against completed work.
   Do not bundle Steps, skip prerequisites or rewrite started authored history.
2. Apply [dispatch](operations-dispatch.md). Save the creation handle, create
   the worker with its complete assignment, and retain the returned task ID.
   Pending IDs remain pending. An uncertain creation is reconciled, not retried.
3. Wait for that exact task with `wait_threads`, retaining its cursor. A timeout
   means it is still being observed. Use `read_thread` only to retrieve missing
   result or identity facts. Do not use repeated status narration as progress.
4. After actual task completion, retrieve its original final `agentMessage.text`
   with `read_thread`, matching the exact task and completed turn and selecting
   `phase:final_answer`. Request `maxOutputCharsPerItem:6000` to cover the full
   result contract. Preserve its line breaks. `wait_threads` is a status snapshot and may flatten or truncate
   the answer; never parse that snapshot as the original result. If the original
   is truncated or missing, retrieve the complete final item before judging its
   format. Run `scripts/parse_role_result.py --role <role>` on that original text.
   Retain the parsed result
   before any acceptance or archive call. For a format-only failure, request
   one correction in the same task; it may only restate its existing result.
   A second malformed result is a reported blocker, not a fabricated success.
5. Handle `context_handoff` through [rollover](operations-rollover.md) before
   review or acceptance. `needs_user_decision` remains open for the answer.
   For `blocked` or a native failure, preserve the changes and actual diagnostic.
   Continue independent eligible work only if it cannot mix unaccepted changes,
   invalidate required backups or advance a dependent Plan item.
6. Inspect the actual scoped diff, changed paths and named checks. Review is
   required for code, executable/configuration changes, critical documentation,
   an explicit requirement or unresolved materiality. The worker's yes/no
   fields help identify the boundary but never override the observed diff.
   Routine documentation with two consistent no values may skip review.
7. When needed, directly create one fresh read-only reviewer for the same unit,
   using its configured pair and the worker result. For `changes_requested`,
   handle Plan-owned corrections in the coordinator and send only source-owned
   findings to a fresh repair worker. Repair 1 uses the original executor pair;
   repairs 2 and 3 resolve upward from that original pair in the current route
   table. Rollover never consumes a repair. Create no fourth repair.
8. Check corrections against every retained finding. Code, critical-documentation
   or material corrections, explicit requirements and unclear outcomes require
   another review. A clearly non-material correction may be accepted after a
   bounded comparison, with the reason recorded. Unresolved findings after
   repair 3 require the user's disposition before further work on that unit.
9. Only after observed Acceptance and required review, update the canonical
   Plan through Scoville Plan, including concise evidence and the next action.
   Run its structural validator. With existing commit authority, inspect the
   staged diff and commit only accepted source changes together with the
   complete affected Plan records. Honor backups and hooks. Do not commit
   merely because Git is present, publish, or hide a failed check.
10. If requested work remains, run the coordinator checkpoint immediately after
    the accepted unit and before selecting or writing the next unit:

```text
python "<workflow-skill-directory>/scripts/check_context_checkpoint.py" --project-root "<workspace_root>" --role coordinator --accepted-unit <unit>
```

`rollover` requires [rollover](operations-rollover.md), with no next-unit work
in this coordinator. `continue` permits the next eligible unit. Report
unavailable telemetry without guessing occupancy or claiming a handoff.
Invalid configuration blocks continuation until corrected. A failed helper
is a failure, not an unavailable-signal result.

A completed Step does not complete its Work Item. Continue the requested scope
without another routine permission request. Only after all of its real work
and acceptance checks finish, complete the Plan/index through their owner and
mark the run record finished. Report a narrower boundary as that boundary.

## Archive once, after retaining the result

After actual child completion and retention of its result or failure, use the
shared lifecycle helper's `archive`, call `set_thread_archived` once with its
exact task/host ID, then check the actual reply with `verify_archive`. Record the
outcome with the retained task handle so resume does not repeat the call.
For `context_handoff`, wait for successor takeover under the rollover reference.
Report a failure or missing state; it does not invalidate acceptance or block
the next unit. Leave active tasks and tasks awaiting a user decision open.
Keep the final coordinator visible. A successor may archive its ended
predecessor as described in the rollover reference.

## Stop and resume

On a user stop, dispatch no new work. Forward the stop to the exact active child
and observe its state. If sending does not interrupt the child, report that
fact and the exact task the user must stop in the UI. Never claim a cascade
that was not observed. Do not commit, review or archive to simulate stopping.
Retain completed effects, unaccepted changes and the next action. Reconcile the
Plan once the child's actual state is known.

On resume or compaction, recover the run record, the Plan, the actual diff and
any pending exact task. Continue from the first unperformed action. Do not
repeat accepted work, recreate an unresolved child or upgrade an active old
runtime contract in place.
