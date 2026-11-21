# Interaction and states

This file holds how navigation, controls, states and transitions behave. Read
it when the task adds, changes or reviews control behavior, focus, input,
asynchronous feedback or recovery. The points below hold for the controls
and states the change adds or alters and for those whose behavior it
affects. Where it is
unclear whether product or UI decides something, see the
[ownership table](ui-structure.md#product-ownership-and-ui-guarantees).

## Navigation and orientation

Build navigation from tasks and content relationships. Keep global
destinations apart from local views and actions.

## Make interaction predictable

- Give a custom composite control a complete focus and keyboard sequence.
- Use a modal for a bounded task that needs attention before continuing.
  Ordinary editing and field errors stay in context.
- Required information and operation never depend on hover.
- Keep focus order, keyboard and touch behavior, programmatic relationships,
  announcements and motion accommodations intact. Custom styling does not
  weaken the component's semantics or state model.
- Ask for confirmation only before an action whose effect the user cannot
  undo. Offer undo only where restoration exists.

## Design states as part of the same interface

Cover the states in
[States of what you add](../SKILL.md#states-of-what-you-add). Tie feedback to
its action and to a recovery step that exists.

- No data, filtered zero results and incomplete results are not shown as one
  another; usable partial results stay.
- Keep feedback discoverable as long as its consequence requires. Never
  report success after a failed action.
- Missing permission reveals no sensitive details and leaves no action that
  fails on use.
- Use persistent visible labels; placeholder text only supplements them.
- Show an error about one field at that field, keep safe entered values and
  offer only real correction, retry or cancellation.

## Affected transitions

Write each affected flow so that the points below hold.

- Navigation, controls and adaptive view changes: the user keeps orientation
  and back and cancel paths, can tell whether a change takes effect at once or
  needs saving, and keeps the working context the task needs without unnecessary
  detours. Not every value or position must persist.
- Dialogs: focus moves into the dialog when it opens, every control in it is
  reachable, closing or cancelling returns focus to the invoking control or
  the next sensible place, and no overlay or sticky region hides a focused
  control.
- Dragging: cancelling a drag leaves a consistent state.
- Forms and authentication: paste, autofill and password managers keep
  working where relevant.
- Async flows: a second trigger of a running action does not repeat its
  effect, a failure reaches the user, and a late old response cannot overwrite
  the current result.
