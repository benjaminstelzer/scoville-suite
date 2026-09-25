# Native project and Plan lifecycle

Use this reference with the Plan format and native editing safety guides for
profile initialization, Plan creation and updates, activation, deletion, cancellation,
and final completion.

## Contents

- Classify setup state
- Initialize a profile
- Create and refine Plans
- Rewrite or delete an unstarted Plan
- Activate a Plan
- Complete or cancel a Plan

## Classify setup state

List the workspace root before probing canonical files. Classify the profile as
one of:

- complete and supported: use the existing profile;
- wholly absent: initialize only when a durable Plan was explicitly requested;
- partial or foreign: preserve the reserved paths and stop;
- unsupported: require a matching Skill or explicit migration; or
- invalid: repair only a specific format defect that changes no authored
  intent, otherwise stop.

Never overwrite a partial or foreign profile, copy the format contract into the
project, or initialize merely because project state was requested.

## Initialize a profile

Require explicit Plan title, Goal, Non-goals, and one behavior-complete initial
Work Item with title, Outcome, Acceptance, optional Steps, and `Next action`.
Do not invent missing authored facts.

Prepare `docs/plans/`, `docs/decisions/`, `PLAN-0001`, `W-001`, and
`PROJECT_INDEX.md` as one complete profile. The initial Plan is `active`, the
initial item is `todo` and `current_item`, dependencies, blockers, Decisions,
and Evidence are empty, and the index points to `PLAN-0001`. Create the index
last. If any member fails, report the partial state and stop.

After initialization, record any explicit or possible material Decisions
through the ordinary Decision route and link them while the affected Work Item
is still `todo`.

## Create and refine Plans

Create each later Plan as `draft` with the next highest Plan ID and at least one
`todo` Work Item. Every initial Decision reference must already exist. A generic
Plan update changes only title, Goal, and Non-goals, preserves ID, lifecycle,
dates, current selection, and all Work Items, and advances `updated` only on a
real change. Before a Goal write, classify the complete proposed Goal by its
canonical owners as required by E's compact-record rules. Operational-only messages leave
Goal bytes unchanged. A separately authorized normalization may move existing
facts only when every future dispatch that needs them can still reach them
through its Work Item, a referenced Decision, or a demonstrated loaded
repository contract.

Cancel a draft only after an explicit user choice. Completed and cancelled
Plans are terminal retained history, except for the narrow unstarted-Plan
rewrite and deletion rules below.

## Rewrite or delete an unstarted Plan

Before execution starts, a user may request rewriting or physical deletion of
a Plan without first setting it to `cancelled`. Rewrite through the Plan and
Work Item edit routes; preserve IDs and valid references for retained records.
Activation or current-item selection alone does not start execution.

Check the Work Items and relevant Evidence or known execution before treating
a Plan as unstarted.
An `in_progress`, `paused`, or `done` item establishes prior execution. `draft`
or all-`todo` metadata does not override evidence that work actually began.
A `cancelled` item may have been cancelled before or after execution; use its
Evidence to distinguish them. If start history is unclear, clarify that fact
before using this exception. Once execution has begun, retain the Plan and its started
history; use the existing cancellation route when abandoning it. Unstarted
items remain editable under W.

For an explicit rewrite request, confirmed non-execution of the whole Plan
also permits changing authored fields of its `todo` or `cancelled` items,
including when the Plan itself is `cancelled`. This narrow exception takes
precedence over W's restriction to `todo` items in `draft` or `active` Plans.
Preserve retained IDs, references, Evidence, record order and lifecycle fields;
change only the requested authored content. A content rewrite does not reopen,
activate or start anything: retain `cancelled` status, empty blockers and no
`Next action` on cancelled items. This exception authorizes no status transition
and never applies when execution has begun or its history is unclear.

For an authorized deletion, inspect incoming references and prepare a valid
remaining profile through E, then validate it through V. Do not silently rewrite
retained history or delete linked Decisions. Resolve any reference that would
become invalid before deletion. If this Plan is active, set `active_plan: null`
in the same prepared change unless the user selected an eligible replacement
through the activation route. Preserve the index and canonical directories even
when no Plans remain. Require neither a cancellation record nor a placeholder
Plan or Work Item.

## Activate a Plan

From idle state, activate one draft Plan by changing that Plan and the index as
one prepared change. The user selects a dependency-ready `todo` or `paused`
target as `current_item`. Setting current does not start it.

From active state, prepare the index, target draft Plan, and outgoing active
Plan together. Require the user to select the outgoing Plan status (`draft`,
`completed`, or `cancelled`) and the exact current-item action:

- preserve a `todo` or `paused` item;
- pause an `in_progress` item;
- complete a `todo` or `in_progress` item with evidence and blocker clearing;
  or
- cancel a `todo`, `in_progress`, or `paused` item with evidence and blocker
  clearing.

The final outgoing Plan must satisfy its selected status invariants. Change no
other Work Item implicitly. If any member is invalid or only partly written,
stop as an incomplete transaction.

## Complete or cancel a Plan

Complete the active Plan only together with its final current `todo` or
`in_progress` Work Item. Require observed evidence, explicit blocker clearing,
all dependencies done, and every other Work Item terminal. Set the item to
`done`, the Plan to `completed`, remove `current_item`, and set the index to
`active_plan: null` as one prepared two-file change. A paused item must resume
first.

The sole active Plan never cancels or completes through a standalone status
edit. Draft cancellation is the only standalone Plan lifecycle transition.
Never create a successor Plan or placeholder Work Item merely to avoid the
valid idle state.
