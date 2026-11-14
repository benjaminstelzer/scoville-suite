# Interaction and states

Preserve component semantics, state coverage, focus and input, announcements
and transitions. Where it is unclear whether product or UI decides something,
see
[Quality's ownership table](ui-quality.md#product-ownership-and-ui-guarantees).

## Navigation and orientation

Build navigation from tasks and content relationships. Keep global
destinations apart from local views and actions. Show location and accessible
back and cancel paths through platform conventions. Keep needed working
context without unnecessary detours.

## Make interaction predictable

- Choose a control by its meaning and keep native semantics: use the
  project's, design system's or framework's component for it where one
  exists, otherwise the native element or a supported primitive. A button
  acts, a link navigates.
- Make action availability, focus and selection, save timing, progress,
  outcomes and recovery apparent.
- Give a custom composite control a complete focus and keyboard sequence.
- Use a modal for a bounded task that needs attention before continuing.
  Ordinary editing and field errors stay in context.
- Required information and operation never depend on hover.
- Keep focus order, keyboard and touch behavior, programmatic relationships,
  announcements and motion accommodations intact. Custom styling does not
  weaken the component's semantics or state model.
- A disabled action shows an associated reason nearby.
- Confirm a consequential action that cannot easily be undone. Offer undo
  only when restoration exists.

## Design states as part of the same interface

Cover affected initial, empty, loading, partial, success, error, unavailable
and permission states. Keep orientation, make changes perceptible beyond one
fragile cue and tie feedback to its action and the real next or recovery
step.

- Distinguish no data, filtered zero results and incomplete results. Keep
  usable partial results and name what is missing.
- Keep feedback discoverable as long as its consequence requires. Never
  report success after a failed action.
- Missing permission: explain unavailable access without sensitive details,
  keep unavailable actions consistent and give a safe return to the task.
- Use persistent visible labels; placeholder text only supplements them.
- Explain format, requiredness and consequences before avoidable errors.
- Associate errors with their fields, keep safe entered values and offer only
  real correction, retry or cancellation.
- Add an error summary when it helps locate several errors, not as a
  universal platform rule.
- Group related inputs with the owning group component or a fieldset with a
  legend.

## Affected transitions

Write each affected flow so that the points below hold. When Validation has
you operate one, use controlled data and local targets, and cause no
unrequested external or durable effect.

- Navigation, controls and adaptive view changes: the user keeps orientation
  and back and cancel paths, can tell when a change takes effect and when it
  is saved, and keeps the working context the task needs. Not every value or
  position must persist.
- Dialogs: focus moves into the dialog when it opens, every control in it is
  reachable, closing or cancelling returns focus to the invoking control or
  the next sensible place, and no overlay or sticky region hides a focused
  control.
- Dragging: the same task can be completed without dragging unless an
  applicable WCAG exception applies; cancelling a drag leaves a consistent
  state.
- Forms and authentication: paste, autofill and password managers keep
  working where relevant; errors are associated with their fields, safe
  values are kept and correction is possible. Avoid redundant entry and
  cognitive-function tests where WCAG 2.2 requires alternatives or
  assistance; preserve the criteria's actual exceptions.
- Async flows: loading, partial results, failure, duplicate-action
  prevention, cancellation and retry are handled, and a late old response
  cannot overwrite the current result.

When a checked flow has a concrete loading or input-latency risk, observe
layout movement and input responsiveness during the transition, not only its
settled end state, with focused local measurements where needed. Lab
observations, emulation and real-device interaction remain distinct; field
performance claims require matching field data. Do not introduce backend tuning or a universal benchmark.
