# Results phase

Completion and delivery gates: [wait](operations-wait.md). Before archival or any next transition: [review](operations-review.md).

## Result contract

Every executor and reviewer knows before starting that its regular output is one
compact JSON object. Before its own final response it attempts exactly one send
of the same bytes to the coordinator under the supplied delivery reference. A
definite delivery failure is never retried and never suppresses the identical
final response. A still-pending `waitingOnApproval` call must resolve first.
Host-required progress commentary is at most one short factual sentence and
never repeats the Plan or work log.

- Executor: `completed`, `blocked`, `needs_user_decision`, `context_handoff`.
- Reviewer: `pass`, `changes_requested`, `blocked`, `needs_user_decision`,
  `context_handoff`.
- Executor or repair keys: exactly `status`, `summary`, `review`, and `findings`.
- Reviewer keys: exactly `status`, `summary`, and `findings`.
- Completed executor or repair `review`: exactly the keys `code_changed` and
  `critical_docs_changed`, each with the string value `yes` or `no`.
- Other executor or repair statuses: `review` is `null`.
- Summary: at most 800 characters.
- Findings: at most eight, each at most 400 characters.
- Combined prose: target 2,000; hard stop above 4,000.
- `pass` requires an empty findings list.
- No truncation.

Before the delivery attempt, the child parses its finished JSON and verifies
one complete object against every role key, status, type, and limit above. It
corrects any failure before sending. The coordinator still performs its
independent validation after wait completion.

`code_changed` is `yes` for changes to source, tests, executable scripts,
build, deployment, runtime, configuration, or generated-code artifacts and
`no` otherwise. `critical_docs_changed` is `yes` when changed documentation
materially governs security, permissions, data handling, migrations,
deployment, operations, public behavior, or required acceptance and lifecycle
behavior and `no` otherwise. Before setting either value, inspect the actual
final changed result. Never infer the values from the unit title, Step wording,
activity name, or route class. Every executor and repair prompt includes these
definitions as part of the Result contract. A child already dispatched with the
former exact two-boolean contract may return that object for its one in-flight
result; never send the legacy form in a new prompt.

The handoff summary contains only completed effects, changed paths, decisive
checks, unverified behavior, remaining work, and unresolved state. Its findings
contain only unresolved defects with location, mechanism, impact, and smallest
fix. Group repeated defects by root cause. Never include a Plan Evidence dump
or an execution diary.

A completed executor or repair summary also names its completed effects,
changed paths, decisive checks, and unverified behavior; it explicitly says
when no path changed or no behavior remains unverified. The reviewer receives
that complete result verbatim and no coordinator supplement.

Before accepting or archiving a result, validate its exact role-specific keys,
strings for `status` and `summary`, a list of strings for `findings`, an allowed
status for the role, summary, finding, count, and combined prose limits, and
empty findings for `pass`. A completed executor or repair also requires the
exact two-string `review` object, except for the retained in-flight legacy case
above. Its other statuses require `review: null`.

Treat the assistant-message text from `wait_threads` as the candidate payload.
When a fresh wait result says the latest turn is completed but that candidate is
missing, syntactically invalid, schema-invalid, or byte-different from the
authenticated delivery for this same dispatch, make exactly one
`read_thread` call for that child with `turnLimit: 1`, `includeOutputs: false`,
and `maxOutputCharsPerItem: 6000`. Use its assistant-message text only when the
returned task ID, host ID, completed turn ID, and, when projected by both APIs,
final assistant-message ID exactly match the wait result. Keep the wait cursor
and native state authoritative. Never use this read for an already matching valid candidate, an
active or nonterminal child, status inspection, evidence discovery, or repeated
chat reads.
For a delivery mismatch, accept the source message automatically only when its
complete text equals the authenticated delivered JSON byte-for-byte and all
identity, completion, role-schema and size checks pass. Retain the differing
projection and source identity as evidence. Use the source bytes unchanged,
including `changes_requested` and every finding; this recovers transport, not
project acceptance. Do not normalize punctuation, compare semantic similarity,
ask for a new review, or request user approval for this proven recovery.
If the exact source still differs, is truncated, or cannot be identified,
retain the conflict and fail closed; do not label it formatting or accept either
version. This mismatch route grants no additional rollout lookup or reread.
An invalid task-API projection is not proof that the child omitted a required
field. In particular, when an already-dispatched legacy result projects the two
Boolean review values as missing or null but the identity-matched source message
contains both valid Boolean values, accept the source message under the retained
legacy exception before considering a formatting correction.

If both task APIs omit the assistant message for that exact completed turn,
perform one final read-only lookup in native rollout storage. Select exactly one
active or archived rollout whose session identity equals the recorded child task
ID; never select by title, time, recency, path order, or another task. Duplicate
files, a missing session identity, or an unreadable record fail closed. Require
exactly one `session_meta` whose session ID equals the recorded child task ID;
that record binds the file. Native `task_started`, `turn_context`, and
`task_complete` events need only carry the exact wait-turn ID and inherit the
verified file session; reject an event-level task identity when present and
contradictory. Require one same-turn `item_completed` AgentMessage with the
verified session as its `thread_id` and `phase=final_answer`, then bind its item
ID to exactly one assistant `response_item` with the same ID, native assistant
role, and `phase=final_answer`. The `response_item` itself need not carry a
top-level turn ID; embedded turn metadata may be absent but must match when
present. Both message ordinals must follow the latest same-turn context ordinal
and precede completion, with no intervening task start, failed or aborted turn,
duplicate ordinal, or conflicting identity. A native replacement-history copy
with that same ID is one mirror, not another candidate; a different ID is
ambiguity. Ignore tool output, commentary, reasoning, user text, quoted JSON,
and JSON embedded only in compaction prose.

The rollout supplies only the omitted final-message bytes. It never supplies
completion, task identity, cursor, or archival authority. If the rollout shows
a later turn or any activity after the matched completion, stop on the
conflicting fresher native state and ask for disposition. Do not start a second
wait after the one completion-confirmation call.
Validate recovered bytes with the unchanged role schema and limits.

Classify failure before correction. A present exact candidate whose bytes are
syntactically or schema-invalid receives one compact formatting correction in
the same task without model or thinking overrides and with a new delivery
reference; this consumes no repair. A
second invalid result is a blocker. Missing rollout identity, absence of a final
assistant message, ambiguity, truncation, task failure, or mismatched ordering
cannot be repaired as formatting: retain the minimal terminal diagnostic,
archive and verify that exact failed task, and then record the coordinator-owned
Plan blocker. None of these paths may invent success, start review or repair,
mutate the Plan as accepted work, commit, or create a successor.

### Result payload recovery scenarios

| Scenario | Recovery read | Treatment |
| --- | --- | --- |
| Valid `wait_threads` payload | None | Validate the wait payload normally |
| Completed projection differs from authenticated delivery | Read the exact completed turn once | Automatically use unchanged source bytes only if they exactly equal delivery and all identity/schema checks pass; otherwise retain the conflict |
| Invalid completed payload with matching valid source message | Read the newest completed turn once | Validate the recovered message text and retain wait state and cursor |
| Legacy DIVI Boolean values are missing or null only in the completed task projection | Read the identity-matched completed turn once | Accept the valid source-message Booleans under the one in-flight legacy exception; do not request a format correction |
| Both task APIs omit one exact completed result and the exact rollout has one matching final message | Read the exact native rollout once | Validate only its message bytes and retain wait state and cursor |
| Exact candidate exists but its bytes are malformed | One API read and if needed one exact-rollout read | Send one same-task formatting correction |
| Identity ordering absence ambiguity or truncation remains | One API read and if eligible one exact-rollout read | Archive as terminal failure and record a blocker without success transitions |
| Active or nonterminal child | None | Return to the same exact-child wait loop with the saved cursor |
