# Compaction phase

Coordinator result acceptance: [wait](operations-wait.md) and [results](operations-results.md). Before a child successor: [review](operations-review.md), [activation](operations-activation.md).

## Post-compaction terminal gate

Every child prompt requires this gate before project action after host
compaction. The only permitted pre-gate action is running the exact read-only
`scripts/inspect_native_context.py` path embedded in that prompt with its role,
current delivery reference, and exact coordinator task ID. The helper resolves
exactly one active rollout by the task's own `CODEX_THREAD_ID`, requires
matching `session_meta`, and never selects another session or selects by
recency.

The helper inspects the same-turn interval from exact `task_started` through the
preceding `turn_context`, successful result delivery or final response,
compaction, and resumed `turn_context`. A delivery is successful only when one
native `functions.exec` wrapper contains exactly one direct
`mcp__codex_app__send_message_to_thread` call with inline JSON arguments for the
exact coordinator and reference, and its unique correlated native tool output
returns that coordinator ID. The helper never treats an uncorrelated output,
failed wrapper, variable-built payload, prompt mention, or another destination
as delivery. It requires strictly increasing unique ordinals and rejects a
failed or aborted turn, another task start, or contradictory task, turn,
message, delivery, or replacement-history identity. A same-ID
`item_completed` AgentMessage and same-ID replacement-history copy are mirrors.
Missing mirrors remain compatible only when the verified session, exact start,
event order, and absence of conflicting activity establish one uninterrupted
interval.

Apply the helper action literally:

1. **`continue_role`:** no own terminal result was emitted or delivered in the
   inspected interval. Continue the unchanged role. An inherited
   `context_handoff` remains only continuation input.
2. **`return_only`:** one protocol-valid own final result was emitted, or an
   already-dispatched callback settled successfully or with a definite
   failure. Return its exact `result_text` as the final response without a
   callback or any other work.
3. **`return_blocked`:** native evidence is unavailable, ambiguous,
   contradictory, duplicated, malformed, or the helper cannot run. Perform no
   project action and return an ordinary protocol-valid `blocked` result naming
   only this gate failure.

Successful delivery or final-message emission freezes project execution for
that turn even before host `task_complete`. The coordinator still accepts no
result until the ordered completion and recovery gates above pass. Replaying
the same terminal bytes after compaction never creates a new logical result or
a duplicate successor.

For each accepted handoff, derive one rollover transition key from stable
workflow identity, unit, role, logical attempt, and exact predecessor task ID.
Retries for that predecessor reconcile the one recorded or exactly titled
successor before any creation. A new predecessor, including the successor's
later rollover or another executor, repair, or reviewer in the same unit, gets a
different key. Never use one unit-wide key that conflates legitimate rollovers.

A successor receives its predecessor's `context_handoff` only as continuation
input. It is never evidence that the successor itself is terminal. The fresh
successor performs remaining role work even when its first turn has no local
compaction. If that successor later emits its own `context_handoff`, its summary
must include `progress_after_dispatch=<newly completed unit action>;
evidence=<new observation>`. Task, turn, message, model, attempt, or replacement
identifiers and copied or reworded predecessor content are not progress.

Before creating a next-generation successor, compare the new handoff with the
inherited continuation. A normal completed role result, a new concrete blocker
or user decision, or the required newly completed action and evidence is
progress. Otherwise archive the exact completed child, preserve the unit and
logical attempt, create no further successor, add `WORKFLOW-NOPROGRESS`, and ask
the user for disposition. This coordinator-owned gate is semantic rather than
literal byte equality: a paraphrased inherited handoff still stops. A no-progress
predecessor therefore has one successor and no grandchild; each legitimate
progress-bearing predecessor still has exactly one successor and unchanged
repair accounting.

### Post-compaction scenarios

| Inspected interval | Child action | Coordinator effect |
| --- | --- | --- |
| Exact own result delivered before compaction but final response absent | Return the delivered result bytes without a second delivery | Accept only after exact turn completion and byte recovery |
| Exact own final result before compaction but delivery absent | Return the same result bytes without a callback or further work | Accept only after exact turn completion and byte recovery |
| Complete interval with no own terminal result | Continue the unchanged role | Normal result handling |
| Missing duplicate malformed or contradictory evidence | Return `blocked` without project action | Archive exact failure and record a blocker |
| Same predecessor is delivered twice | Repeat the same terminal result | Reconcile the existing successor; create no duplicate |
| Fresh successor receives inherited handoff and has no local compaction | Treat it only as continuation input and perform remaining role work | No terminal transition from inherited content |
| Successor copies or paraphrases inherited handoff without new action and evidence | Return no accepted rollover progress | Archive it add `WORKFLOW-NOPROGRESS` and create no grandchild |
| A successor later rolls over after new action and evidence | Use its distinct predecessor key | Create at most one next-generation successor |
