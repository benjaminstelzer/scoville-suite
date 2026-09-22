# Scope phase

Before another unit, use [selection](operations-selection.md) and [dispatch](operations-dispatch.md). Accepted transitions require [accepted](operations-accepted.md) and [rollover](operations-rollover.md); terminal children require [review](operations-review.md).

## Resolve and run the requested scope

After the user chooses the current Plan, the coordinator resolves the supplied
`requested_scope` against canonical Work Items. `whole_active_plan` includes
every nonterminal item. An explicit scope includes only its named items, range,
or end boundary. An invalid or ambiguous explicit boundary requires an exact
user decision; an absent boundary means the whole active Plan.

After every accepted unit transition and its scoped commit when Git is in use,
evaluate the requested-scope terminal condition and run the coordinator
checkpoint before any next-unit selection. Only the coordinator retained or
activated by that checkpoint reruns deterministic Plan selection and dispatches
the next eligible in-scope unit without another confirmation. Continue
remaining dispatch units in the current Work Item before advancing to another
Work Item. Advance only when the current Work Item is terminal and accepted or
its blocker invokes the independent-work rule below. Never treat one completed
dispatch unit, singular request wording, or the initially current item as
implicit completion. The coordinator returns control during an unfinished scope
only for `needs_user_decision`.

When a child blocks or fails, retain the exact blocker detail, archive and
verify the terminal child, then record the exact Plan blocker. Continue another
independent eligible in-scope Work Item if one exists. If none exists, ask the
exact disposition decision needed to wait,
authorize remediation, change scope, or cancel. Keep the coordinator unarchived
and resume the same loop after the answer. Do not spin on unchanged state.

Independent eligibility also requires commit compatibility with every
outstanding unit in the shared Git workspace and a candidate accepted transition
that can stage one complete structurally valid Plan profile. Retained terminal
blocker state from an earlier unit may enter the next accepted unit commit only
as accumulated coordinator Plan state; unaccepted project changes from that
earlier unit never do. If no complete valid staged Plan can preserve that
boundary, ask for disposition before dispatch. If a blocked unit retains source
changes made after a required `HEAD`-bound pre-change backup but before its
accepted commit, preserve that entire interval and ask for its disposition
before another unit is dispatched or allowed to advance the same `HEAD`.
Disjoint paths do not make that commit safe.

Required executor or reviewer pair unavailability follows the same blocker
path. Record it for that unit and continue another independent eligible
in-scope dispatch unit with its own configured pair. Do not substitute or probe
unused models. Ask disposition only when no independent eligible unit remains.

### Continuation scenarios

| State | Next action | Return control | Coordinator remains open |
| --- | --- | --- | --- |
| W-001 point A accepted while point B remains and scope is W-001 | Dispatch W-001 point B | No | Yes |
| W-001 terminal and W-002 is eligible in whole-Plan scope | Dispatch W-002 first unit | No | Yes |
| Explicit boundary through W-003 is accepted | Emit boundary completion | Completion only | Yes |
| W-001 unit blocked while independent W-002 is eligible | Record W-001 blocker and dispatch W-002 | No | Yes |
| W-001 is blocked after a HEAD-bound backup and source edit while W-002 is otherwise eligible | Preserve the interval and ask before W-002 dispatch or commit | User decision | Yes |
| W-001 required pair unavailable while independent W-002 is eligible | Record W-001 blocker and dispatch W-002 with its configured pair | No | Yes |
| Blocker leaves no eligible in-scope unit | Ask exact disposition decision | User decision | Yes |
| User explicitly says stop | Forward Stop and reconcile Plan | User cancellation | Yes |
