# Native Work Item operations

Use P for record syntax, E for writing and verification, and this reference for
Work Item changes. Read G when creating or changing outcome boundaries or Steps.

## Preserve authored history

Edit, move or remove only `todo` items in a `draft` or `active` Plan. After start,
retain ID, title, dependencies, Decisions, Outcome, Acceptance, Steps and position.
Only status, `Blocked by`, Evidence and `Next action` remain mutable. A paused
item resumes to `in_progress`, never to `todo` for editing.

Two narrow exceptions:

- For an explicit rewrite of a confirmed wholly unstarted Plan, read
  [L's exception](native-project-lifecycle.md#rewrite-or-delete-an-unstarted-plan).
  It can permit authored edits to cancelled records, never reopening them or
  rewriting executed history.
- An explicit user choice may replace only the `[execute: ...]` annotation of
  one named unperformed Step after start. Preserve its action and route, all
  other authored content, and completed or running dispatches. Add, remove,
  move or rewrite no Step under this exception.

## Handle active messages and direct maintenance

Classify each part of a message before changing execution or records:

| Message | Action |
| --- | --- |
| Explicit stop, pause, cancellation or immediate redirect | Stop live work. Apply only the authorized lifecycle change. Preserve an explicitly requested later return as described below. |
| Correction invalidating current execution | Stop affected execution and reconcile through the Work Item or Decision route. Do not infer cancellation or rewrite started fields. |
| Additive request, including a plain imperative without immediate priority | Queue it after current work using the deferred operation below. Do not start it or change the current item. |
| Information or status question without retained work | Answer and continue; create no Work Item. |
| Direct request to add, refine, reorder, remove or clean up Plan records | Apply the normal record mutation directly. Never create a Work Item for Plan maintenance itself. |

For mixed messages handle an interrupting correction first, then queue independent
additions. A substantive new outcome gets exactly one Work Item; removing or
rewriting records gets no replacement item merely to track that maintenance.

Queueing requires a complete supported active Plan and must fit its Goal and
Non-goals. Ask only for unresolved scope or lifecycle choices, keeping independent
current work unchanged. Do not initialize a profile or broaden scope implicitly.
A stop still governs execution even when queueing is unavailable.

## Pre-flight and refine todo work

Before starting the next `todo` item, compare its premises, paths, contracts,
data and checks with current sources and relevant completed dependencies in
this Plan. Refine stale instructions before start. Do not scan historical Plans
or reread the whole active Plan without a concrete relevance reason.

- Insert one complete H3 block at the end or beside an anchor. Allocate the
  highest Work Item ID plus one. Move whole blocks without renumbering.
  Dependencies must exist, precede their dependents and remain acyclic.
- A generic update may replace title, dependencies, Decisions, Outcome,
  Acceptance, Steps, Evidence and Next action. Preserve ID, status, blockers,
  position and current selection.
- Delete only if another item remains and no dependency targets the item.
  Deleting the current item requires an explicit dependency-ready `todo` or
  `paused` replacement in the same prepared change.
- G owns decomposition and dispatch boundaries; P owns Step and annotation
  syntax; E owns concrete wording and file discovery. Steps have no separate
  lifecycle. Keep the next unperformed action or unobserved Acceptance check
  in Next action, not a second progress system.
- Plan does not infer routes or reasoning. Preserve an existing route prefix
  or record an explicit user choice. Route changes require `todo`. Record an
  explicit model or reasoning choice with `[execute: ...]`; for a `todo` item
  without Steps, add one coherent annotated Step if needed. After start use
  only the annotation exception above.

One Step is one dispatch by default. An explicitly invoked Workflow may bundle
adjacent Steps only under its accepted Decision, with the same outcome, owner,
authorization, route, workspace and Acceptance boundary. Changed Decisions,
external effects, higher risk, different routes or independently resumable
results force separate dispatch. Bundling changes no Plan field, order or
Acceptance owner.

## Queue deferred work

This is a planning checkpoint, not a change of current execution. Preserve
`current_item` and every field of the current started item.

Use existing H3 titles for durable sequencing provenance:

- `Deferred after W-001: Describe the observable outcome` identifies work
  queued after the named anchor. Consecutive `todo` blocks with this prefix
  form its deferred segment, in arrival order unless the user chooses otherwise.
- `Prioritized after W-001:` records an explicitly selected future `todo`
  successor. Allow at most one per anchor. Unmarked authored order is not an
  implicit recorded priority.

Prefixes become immutable history after start. Change them only on `todo`
items when the user-authorized order changes. Together with ordered H3 blocks,
IDs, dependencies, blockers and Decisions, they are the whole durable queue:
no extra field, hidden marker, checkbox or chat-only list.

Inspect the anchored segment and its last queued `todo` item. Apply G's batching
criteria. Merge a compatible addition into that block while preserving its ID,
prefix, position, status, blockers and current selection. Otherwise allocate
the next ID and insert after earlier deferred items for that anchor, ahead of
unmarked lower-priority future `todo` work. Do not jump back across a separate
queued outcome to merge an older batch.

Do not override a prioritized successor, move started work or invent a dependency
to force order. Ask about a conflicting explicit priority. If that priority
remains, anchor the addition after it. If a real prerequisite must come first,
anchor after that prerequisite at the earliest valid position and report why
the addition cannot be immediate.

Persist and verify before acknowledging the queued ID, then resume unchanged
current work. A failed write means it is not durably queued and must not start.
On recovery, derive order from the native records. Multiple priorities for one
anchor, a missing anchor, or an anchor placed after its prefixed item requires
human direction, not silent normalization.

After current Acceptance, reread the intended successor. If start-eligible,
complete and advance. If dependencies are done but a blocker or unresolved
Decision prevents starting, ordinary completion may select it without starting
or clearing that obstacle. If no dependency-ready replacement exists or the
successor is ambiguous, keep current work non-terminal and ask. Never skip
queued work or finish the Plan with non-terminal deferred work.

## Preserve an explicit return after redirect

Only when the user requests a later return, pause the outgoing item and retain
its first unfinished action in Next action, for example:
`After W-004 completes, resume W-001 and perform ACTION.` Do not change the
started item's title or position. An ordinary pause keeps an ordinary Next
action. Allow one paused return target per redirected item; ask about conflicts.

On recovery, inspect paused items for a return naming the current redirected
item. After its Acceptance, complete it while selecting the paused target, then
resume that target and restore its saved concrete action. Do not use
`complete_and_advance`, which starts `todo` work. If the return is blocked,
dependency-invalid, missing or ambiguous, preserve it and ask; do not start
another item automatically.

## Select, advance and block

- Only an active Plan has `current_item`. Select a `todo`, `in_progress` or
  `paused` item whose dependencies are done, with no other `in_progress` item.
  External blockers may remain visible on a selected item.
- Start only current `todo` work with done dependencies and no blockers. Pause
  only current `in_progress` work. Resume only current `paused` work with done
  dependencies and no blockers. At most one item is `in_progress`, always current.
- `complete_and_advance` prepares completion of the current item and start of
  the explicit replacement together. Apply neither if either is invalid.
- Add an absent valid external blocker with an updated Next action. Resolve
  only the named blocker, record observed evidence and the next concrete action.
  A blocker is not evidence.
- Changing Next action alone changes no other field. For non-terminal work it
  names the first unfinished action; after implementation, the first unobserved
  test, build, browser check, review or evaluator-owned verification.

## Complete or cancel

Complete only current `todo` or `in_progress` work in an active Plan with done
dependencies, observed Acceptance evidence, explicitly cleared blockers and a
named eligible replacement. Resume paused work before completion.

Cancellation requires an explicit choice, evidence and explicit blocker clearing.
It applies to `todo`, `in_progress` or `paused` work in draft or active Plans;
current work needs an eligible replacement. Cancelled work satisfies no dependency.

Terminal work retains non-empty Evidence, has no blockers or Next action, and
never transitions again. For the final real item use
[L's Plan completion](native-project-lifecycle.md#complete-or-cancel-a-plan),
including the idle index. Invent no successor to keep the Plan active.
