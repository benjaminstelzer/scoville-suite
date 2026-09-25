# Results phase

Completion and delivery gates: [wait](operations-wait.md). Before archival or any next transition: [review](operations-review.md).

## Result contract

Every executor, repair and reviewer returns one UTF-8 `SCOVILLE_RESULT_V1`
line result as its final response. It sends no callback message. The
coordinator retrieves the exact completed turn through `wait_threads`; the
recorded delivery reference continues to bind the assignment and result.
Host-required progress commentary is at most one short factual sentence and
never repeats the Plan or work log.

The first line is exactly `SCOVILLE_RESULT_V1`. Remaining lines use `key=value`
without Markdown fences, padding, blank lines, or multiline values. Their
order is fixed:

- Reviewer: `role=reviewer`, `status=...`, `summary=...`, then zero to eight
  `finding=...` lines.
- Completed executor or repair: matching `role=...`, `status=completed`,
  `code_changed=yes|no`, `critical_docs_changed=yes|no`, `summary=...`, then
  zero to eight `finding=...` lines.
- Other executor or repair statuses omit both change fields and continue with
  `summary=...`, then zero to eight `finding=...` lines.

Executor and repair statuses are `completed`, `blocked`,
`needs_user_decision`, or `context_handoff`. Reviewer statuses are `pass`,
`changes_requested`, `blocked`, `needs_user_decision`, or `context_handoff`.
Summary contains 1 to 800 characters. Each finding contains 1 to 400
characters. Combined summary and findings target 2,000 and must not exceed
4,000 characters. `pass` has no finding lines. Unknown, missing, duplicated,
or unordered fields, more than eight findings, empty values, trailing lines,
and truncation are invalid.

Before its final response, the child checks the header, matching role, field
order, status, counts, and limits. It corrects any failure before returning.
The coordinator still performs independent validation after wait completion
with `scripts/parse_role_result.py`. The helper is the only result parser. It
fails closed and returns the same internal `status`, `summary`, `review`, and
`findings` structure used by review and repair prompts. Models never compose
result JSON.

`code_changed` is `yes` for changes to source, tests, executable scripts,
build, deployment, runtime, configuration, or generated-code artifacts and
`no` otherwise. `critical_docs_changed` is `yes` when changed documentation
materially governs security, permissions, data handling, migrations,
deployment, operations, public behavior, or required acceptance and lifecycle
behavior and `no` otherwise. Before setting either value, inspect the actual
final changed result. Never infer the values from the unit title, Step wording,
activity name, or route class. Every executor and repair prompt includes these
definitions as part of the Result contract.

The handoff summary contains only completed effects, changed paths, decisive
checks, unverified behavior, remaining work, and unresolved state. Its findings
contain only unresolved defects with location, mechanism, impact, and smallest
fix. Group repeated defects by root cause. Never include a Plan Evidence dump
or an execution diary.

A completed executor or repair summary also names its completed effects,
changed paths, decisive checks, and unverified behavior; it explicitly says
when no path changed or no behavior remains unverified. The reviewer receives
the complete helper-produced result object and no coordinator supplement.

Before accepting or archiving a result, pass the exact recovered bytes and the
recorded role to `scripts/parse_role_result.py`. Continue only when it returns
`valid: true`; use its `result` object as the coordinator-internal value. Do not
repair, normalize, or manually reconstruct a new line result.

Treat the assistant-message text from `wait_threads` as the candidate payload.
When a fresh wait result says the latest turn is completed but that candidate is
missing, protocol-invalid, or byte-different from the
authenticated delivery for this same dispatch, make exactly one
`read_thread` call for that child with `turnLimit: 1`, `includeOutputs: false`,
and `maxOutputCharsPerItem: 6000`. Use its assistant-message text only when the
returned task ID, host ID, completed turn ID, and, when projected by both APIs,
final assistant-message ID exactly match the wait result. Keep the wait cursor
and native state authoritative. Never use this read for an already matching valid candidate, an
active or nonterminal child, status inspection, evidence discovery, or repeated
chat reads.
For a delivery mismatch, accept the source message automatically only when its
complete text equals the authenticated delivered result byte-for-byte and all
identity, completion, role-protocol and size checks pass. Retain the differing
projection and source identity as evidence. Use the source bytes unchanged,
including `changes_requested` and every finding; this recovers transport, not
project acceptance. Do not normalize punctuation, compare semantic similarity,
ask for a new review, or request user approval for this proven recovery.
If the exact source still differs, is truncated, or cannot be identified,
retain the conflict and fail closed; do not label it formatting or accept either
version. This mismatch route grants no additional rollout lookup or reread.
An invalid task-API projection is not proof that the child omitted a required
field. Recover the identity-matched source bytes through the same strict line
protocol before considering a formatting correction.

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
ambiguity. Ignore tool output, commentary, reasoning, user text, and results
quoted only inside compaction prose.

The rollout supplies only the omitted final-message bytes. It never supplies
completion, task identity, cursor, or archival authority. If the rollout shows
a later turn or any activity after the matched completion, stop on the
conflicting fresher native state and ask for disposition. Do not start a second
wait after the one completion-confirmation call.
Validate recovered bytes with the unchanged role protocol and limits.

Classify failure before correction. A present exact candidate whose bytes are
protocol-invalid receives one compact formatting correction in
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
| Completed projection differs from authenticated delivery | Read the exact completed turn once | Automatically use unchanged source bytes only if they exactly equal delivery and all identity/protocol checks pass; otherwise retain the conflict |
| Invalid completed payload with matching valid source message | Read the newest completed turn once | Validate the recovered message text and retain wait state and cursor |
| Both task APIs omit one exact completed result and the exact rollout has one matching final message | Read the exact native rollout once | Validate only its message bytes and retain wait state and cursor |
| Exact candidate exists but its bytes are malformed | One API read and if needed one exact-rollout read | Send one same-task formatting correction |
| Identity ordering absence ambiguity or truncation remains | One API read and if eligible one exact-rollout read | Archive as terminal failure and record a blocker without success transitions |
| Active or nonterminal child | None | Return to the same exact-child wait loop with the saved cursor |
