# Review phase

Validate completion first using [wait](operations-wait.md) and [results](operations-results.md). Handoff needs [compaction](operations-compaction.md) and [checkpoint](operations-checkpoint.md). Review/repair dispatch uses [activation](operations-activation.md); blockers use [scope](operations-scope.md). Before acceptance use [accepted](operations-accepted.md).

## Review, repair, and archive

Branch on `context_handoff` first: archive the predecessor after collecting the
handoff, verify archival, and use the predecessor-scoped rollover key to
reconcile an already-created successor. An initial child that received no
inherited handoff may create its one same-role successor. A child created from
an inherited handoff may create a next-generation successor only after the
inherited-continuation progress gate passes. A failed progress gate uses
`WORKFLOW-NOPROGRESS` and creates no successor. Do not start a
review of incomplete executor work. On `blocked`, archive the child, record the
blocker, and continue through the requested-scope rules above. After the initial
executor returns `completed`, archive that task and compare its review report
with the final scoped diff, changed paths, and named evidence. Require review
when either Result-contract value is `yes`. Explicit user, Plan, and repository
requirements override the threshold. Ambiguous materiality resolves to review.

Read-only discovery, project inspection, preparation, coordinator-owned Plan
maintenance, and routine documentation changes do not require review by
themselves. Use the executor report as the primary classification and compare it
with the scoped result. Never classify from the unit title, Step wording, or
route class. Read the completed executor's `code_changed` and
`critical_docs_changed` values before deciding. Either `yes`
requires review. Two `no` values permit a skip after one bounded consistency
check against the final scoped diff, changed paths, and named evidence. Do not
repeat project inspection, tests, acceptance work, or a review. `no` values
never override an observed qualifying change or an explicit review requirement.
A conflict or unclear classification requires review. For a qualifying result,
send the required review-phase announcement, then start one fresh reviewer with
the same unit identity, exact `workspace_root`,
and the complete helper-produced `executor_result` object. Add no free-form appended prose
or complete Evidence histories. Supply necessary additional facts only through
the validated `supplemental_context` input before binding, including needed
content from sources the reviewer may not read. Preserve canonical source_text
and the helper-produced executor_result without semantic changes; the result
names changed paths and decisive checks. For a non-qualifying
result, create no reviewer or repair and record the observed threshold result in
Work Item Evidence before lifecycle advancement. A reviewer `context_handoff`
creates its same-review successor only after the inherited-continuation progress
gate passes. Archive every terminal task immediately after
collecting and retaining its result. Child archival uses only the ready
`threadId` and `hostId` recorded for that exact child role and unit. Require an
authoritative archival-state response for that same ID with `archived: true`
before any Plan mutation, successor, reviewer, or repair creation, or next
dispatch. A tool-call wrapper reporting `completed`, a response that repeats
only the ID, or presence or absence in a general active or archived task listing
is not archival-state proof.

When the archive response lacks that proof, perform one bounded reconciliation
for the same exact ID: use an available exact-ID archival-state read, or repeat
the archive request once when that operation returns explicit state, then require
the same ID and `archived: true`. Never substitute a title, recency match, caller
ID, or another task. If exact state remains false, mismatched, or unavailable,
ask the exact user decision and keep the coordinator unarchived; do not mutate
the Plan, create another child, or dispatch more work.

At resume and before any new transition, reconcile every retained terminal child
from the interrupted unit whose archival was not explicitly verified. A terminal
child still visible is re-archived only after its valid final result or captured
native failure is retained, using the same ID and the bounded verification above.
An active child, a `needs_user_decision` child, or a terminal child without a
safely retained result is never archived by this recovery.

`needs_user_decision` is nonterminal and remains open. `blocked`, `completed`,
`pass`, `changes_requested`, and `context_handoff` are terminal for that task. A
failed native task is also terminal after its failure is captured. Never archive
before a valid final handoff is safely available, except for the explicit
coordinator-owned invalid-result or format-exhaustion failure path above.

### Archival verification scenarios

| Scenario | Proof | Next action |
| --- | --- | --- |
| Archive response returns the exact child ID and `archived: true` | Verified | Continue the guarded transition |
| Archive call reports `completed` but no explicit archival state | Unverified | Reconcile the same exact ID once |
| General task lists omit or include the child | Unverified | Do not infer archival state from list membership |
| Retained terminal child is still visible after resume | Unverified until exact-state confirmation | Re-archive the same ID once and verify before transition |
| Exact state remains false mismatched or unavailable after reconciliation | Failed | Ask the user and perform no Plan mutation or child creation |

A `changes_requested` result does not automatically create a repair executor or
second reviewer. Partition every finding by correction owner. Apply all
permitted coordinator-owned Plan corrections first and run the Plan validator,
including for mixed Plan and project findings. Send only executor-owned
corrections to one fresh repair executor in the same exact `workspace_root`.
Count only a new executor-owned correction as a repair attempt. Before creating
it, resolve its pair through `scripts/resolve_model_pair.py`: repair 1 uses the
original executor's launched pair, repair 2 moves one WORK row above that pair,
and repair 3 moves two rows above it, capped at `ultra_high`. Pass the original
launched pair each time, not the previous repair's pair. If that pair is outside
the current WORK table when escalation is required, stop with the helper
diagnostic rather than risk a weaker assignment. Repair escalation does not
change the unit's route class or reviewer route. Each newly created reviewer
resolves its pair from the current configuration; a running reviewer retains
its launched pair. Pass the complete helper-produced `reviewer_result` object
without semantic changes plus one
`repair_assignment` whose sorted
unique zero-based indices select only the unresolved executor-owned findings.
Create and activate the repair through the pending-writer parking sequence.
Send the required repair-phase announcement immediately before sending that
activated repair its complete assignment.
The repair corrects only that assignment and does not repeat accepted unit work
or coordinator-owned Plan changes. The coordinator retains the complete finding
set for the final gate. If no executor-owned correction
remains, create no repair executor. Count each repair executor against the first
attempt plus at most three repair executors. A coordinator Plan correction
consumes no repair attempt. If executor-owned findings remain after the third
repair executor, create no fourth repair; retain all changes and evidence,
record the exact unresolved findings, and request the user's disposition before
any further repair, acceptance transition, or commit.

After every required correction is complete, perform one bounded comparison of
the complete corrected result against the reviewer findings, unit risk, repair
review values when present, and explicit review requirements. Start another
reviewer, after sending the required review-phase announcement, when any
correction changed code, changed critical documentation,
materially touched the unit's risk boundary, conflicted with the reported
classification, remained unclear, or has an explicit review requirement. This includes a
coordinator-owned Plan correction when its meaning is material. An exact
non-material Plan correction or routine non-critical documentation correction
needs no second review when the findings and complete scoped result agree. Route
class informs the decision but does not require a follow-up by itself. When a
Plan-only correction requires follow-up, dispatch the reviewer directly without
creating a repair executor. Record a skipped follow-up review and its observed
basis in Work Item Evidence. A threshold-skipped initial result creates no repair
path. A user-decision continuation uses the same task and does not count as a
repair.

### Review correction scenarios

| Scenario | Plan correction | Repair executor | Review result |
| --- | --- | --- | --- |
| Initial code or critical documentation change | None | None | Reviewer required |
| Initial consistent non-qualifying result | None | None | Reviewer skipped |
| Initial conflict explicit requirement or ambiguity | None | None | Reviewer required |
| Exact non-material Plan-only finding | Coordinator | None | Follow-up skipped after bounded comparison |
| Material explicit or ambiguous Plan-only finding | Coordinator | None | Follow-up required |
| Routine non-critical project-documentation finding | None | Project correction | Follow-up skipped when report and result agree |
| Code critical-documentation or material-risk project finding | None | Project correction | Follow-up required |
| Mixed Plan and project findings | Coordinator handles Plan part | Project correction only | Decide from all corrections and require follow-up when qualifying or unclear |
