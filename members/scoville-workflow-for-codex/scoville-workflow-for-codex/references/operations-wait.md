# Wait phase

On completion, load [results](operations-results.md) before recovery or validation, then [review](operations-review.md) before archival or transition. A Stop uses [stop](operations-stop.md).

## Wait and communicate

Announce each real workflow phase transition once in the retained `language`.
Make the selection and pass every prerequisite for starting that phase, then
send the announcement immediately before the action that starts it. Use one or
two short sentences, normally at most 400 characters. Name the exact runtime
unit ID and the selected Work Item, Step, or contiguous Step range. Add a brief
description grounded only in the selected authored Plan text so the user can
identify the work without opening the Plan.

### Required phase announcements

Before dispatch, report the intended send, not execution. A successful send
confirms delivery only. Say work started only after observing a child work
action beyond parking and its required gates. Do not add status polling.

| Transition | When to announce | Required content |
| --- | --- | --- |
| Initial execution | Immediately before sending the activated executor its complete assignment, after parking-task identity reconciliation, unit formation, preflight, routing, prompt construction, and guard activation succeed | Identify the exact unit and selected Plan work; say that the execution assignment will now be sent |
| Required review | Immediately before creating each required reviewer, after the review decision is final | Identify the exact unit and completed or corrected result under review; say that the review request will now be sent |
| Assigned repair | Immediately before sending the activated repair its complete assignment, after parking-task identity reconciliation, prompt construction, and guard activation and after correction ownership and finding indices are final | Identify the exact unit and assigned findings; say that the repair assignment will now be sent |
| Accepted completion transition | After the applicable review gate is satisfied and immediately before Plan mutation, structural validation, staging, or commit | Identify the exact unit; say that the completion phase begins and whether it is closing the unit, an explicit requested boundary, or the whole Plan when that target is already known |

The completion-phase announcement reports a transition, not successful
completion. Success is claimed only by the final completion report after every
gate passes. Do not announce a phase before its selection and prerequisites are
final. Do not repeat an announcement for a rollover successor that continues the
same phase. A follow-up reviewer or repair is a new phase transition and receives
its own announcement. Do not expose prompts, child payloads, model or reasoning
choices, hidden routing details, or internal deliberation. These announcements
do not authorize polling, periodic progress chatter, or messages while a child
is active.

An automatic persistent-goal continuation is not a meaningful coordinator
state change and never authorizes project inspection or an "I am waiting"
message. The coordinator remains in its current turn and uses only the exact
child wait loop below.

Throughout every live workflow, including worker execution and each rollover,
at least one coordinator task must remain unarchived and visible with its latest
user-facing phase or blocker. Terminal completion or explicit cancellation also
leaves its final coordinator visible. A coordinator must not finish its turn
merely because a child is running. After successful activation and assignment
dispatch, retain the exact child ID, host ID, latest cursor, and single-use
delivery reference. Then call `wait_threads` for exactly that child with a
timeout no greater than 60 seconds:

```text
wait_threads({
  targets: [{threadId: exact_child_id, hostId: exact_host_id,
             afterCursor: latest_cursor}],
  timeoutMs: 60000
})
```

Omit `afterCursor` only before the first cursor exists. On an unchanged timeout,
emit no commentary and call `wait_threads` again with the returned cursor while
retaining the same exact child ID, host ID, and delivery reference. Continue
until the expected turn completes, needs attention, new user input interrupts
the wait, or the wait tool itself fails. A status request reports one fresh
snapshot and then resumes this loop. A changed scope, Stop, or required user
decision follows its own control path instead. Never use `read_thread` as this
wait loop.

Every child constructs its final role JSON, sends exactly one
`workflow_result_delivery=<reference>` message containing those exact JSON
bytes to `coordinator_self_id`, and then returns the same bytes as its own final
response. Delivery may fail when the coordinator already has an active waiting
turn. The exact final response observed through `wait_threads` is therefore the
normal completion source; a successfully delivered copy is an additional
byte-for-byte check, not the only wake path.

The host may hold an authorized cross-task message call in
`waitingOnApproval`. Treat that exact call as pending delivery, not as failure
or a reason for another model turn. Do not retry, relay, recreate either task,
poll, or send progress narration. Resume only when the host resolves the same
call. Approval continues that call. After a definite rejection or tool failure,
the child does not retry or request a replacement delivery; it returns the
already-validated identical JSON as its final response so the coordinator's
wait loop can recover it.

On a completed wait result or result delivery, process these gates in order
before any Plan, project, archival, successor, reviewer, repair, or commit
action:

1. Authenticate that the waited task ID equals the recorded child ID and that
   its unit, role, logical attempt, and expected turn match the retained pending
   dispatch. When a delivery exists, also authenticate its native source task
   ID and single-use reference.
2. Require authoritative completion of the expected turn from `wait_threads`.
   A still-running or unchanged timeout returns to the same cursor-bound wait
   loop without project action or commentary.
3. Recover the exact candidate bytes through the result-recovery chain below
   when the completed wait projection is missing, malformed, or differs from
   the authenticated delivery bytes.
4. When delivery succeeded, require the recovered candidate bytes to equal the
   delivered JSON byte-for-byte. When delivery failed or never arrived,
   validate the final-response bytes from the exact completed turn directly.
   In both cases validate the unchanged role schema and limits.
5. Branch on the validated status. `needs_user_decision` retains the exact child
   open and asks only its question. Every terminal role status retains the
   result, archives the exact child with verified state, and only then performs
   the permitted transition.

When a child reports an actual host permission or access failure, handle it
before the ordinary result branch. Archive that child, keep the coordinator and
guard visible, state the observed failure and applicable Codex configuration
change, then ask whether to apply it. Do not request approval inside the child,
alter configuration without that answer, or retry automatically.

Delivery supplies result-ready bytes only; it never supplies completion,
cursor, archival, or transition authority. A mismatched source, unknown
reference, conflicting delivered bytes, different turn, or unexpected state
fails closed without project action. Consume the reference only after its
terminal transition settles. An identical source, reference, and byte retry
reconciles that pending or settled transition idempotently; conflicting reuse
blocks. A new actual turn, including formatting correction or user
continuation, receives a new reference.

An unchanged wait timeout is not a failure and authorizes only another wait for
the same child with the updated cursor. A completed or needs-attention result
ends the loop. A real `wait_threads` tool error stops the workflow visibly:
report the error, keep coordinator, child, pending dispatch, and guard intact,
and perform no archival, Plan or project transition, successor, reviewer,
repair, or commit. Do not use `read_thread` as a polling loop and do not narrate
timeouts or unchanged state. A state claim requires a fresh native result.

A nonterminal `needs-attention` state preserves the exact child, cursor,
pending dispatch, delivery reference, guard, and coordinator. Use only the
attention reason returned by that exact `wait_threads` result; do not inspect
the project or infer a cause. Report the exact required user action once. After
the host or user resolves it, resume the same child with the returned cursor.
Do not archive, replace, redispatch, mutate the Plan or project, or end the
coordinator merely because attention is required.

Do not read an active child conversation during normal coordination. For a
generic status request, use one immediate or bounded `wait_threads` snapshot
and report only that fresh state. Outside the identity-bound completed-result
recovery below, only an explicit user request to inspect or read one named child
conversation permits one bounded `read_thread` call with the smallest useful
turn and output limits. Do not repeat that inspection unless the user asks
again. Chat content never replaces the wait cursor or native child state. After
inspecting a nonterminal child, return to the same exact-child wait loop; a
completed-result recovery continues from its already-fresh wait state.

Coordinator commentary consists of the required phase announcements above and
exceptional control output. Do not emit additional messages for routine child
completion, archival, passing review, Plan writes, or commit. User decisions,
blockers, review findings, unexpected failures, and final completion remain
reportable. When a
higher-priority host rule requires periodic progress, combine the latest state
into at most one short factual message per required 60-second interval; a routine
transition inside the same interval does not justify another message.
Outside the required phase announcements and host cadence, send one or two
sentences, normally at most 400 characters, only for a meaningful state change,
user decision, blocker, failed check, review finding, unexpected failure, or
final completion.

If the task returns `needs_user_decision`, keep it unarchived. Ask the user only
the exact missing decision. After the user answers, call `send_message_to_thread`
for that same task ID with a compact message containing the unit ID, the exact
answer, “continue the same task”, and a new single-use delivery reference. Omit
model and thinking so its existing settings and conversation remain intact.
Enter the same exact-child wait loop. Never
replace or fork it merely because a user decision interrupted the turn.

### Coordinator wake scenarios

| Event while child is active | Coordinator wake | Required action |
| --- | --- | --- |
| Exact child remains active through a wait timeout | No state change | Wait again with the updated cursor and no commentary or project inspection |
| Exact child completes with one final role result | One completion result | Recover validate and when present compare delivered bytes |
| Exact child completes with `needs_user_decision` | One decision result | Confirm the completed turn then ask only the exact decision |
| User requests status | One user wake | Report one exact-child wait snapshot then resume the same wait loop |
| Identical retry of one pending or settled delivery | One reconciliation wake | Reuse the same transition state; do not wait or transition twice |
| Unknown source or conflicting delivery reuse | One rejected wake | Fail closed with no project or Plan action |
| Completed wait projection differs from authenticated delivery | One recovery read | Apply the exact-source recovery rule below; no transition before it passes |
| Result delivery arrives before native completion | Expected race | Continue the same exact-child wait loop until authoritative completion |
| `wait_threads` returns a tool error | Visible blocker | Preserve coordinator child and guard; perform no workflow transition |
