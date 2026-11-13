# Interaction and states

Preserve component semantics, state coverage, focus and input, announcements,
transitions and proof; rendered layout proof belongs to a requested review,
audit or check. Where it is unclear whether product or UI decides something,
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
- Exercise the focus and keyboard sequence of a custom composite control.
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

## Exercise affected transitions

When the requested flow includes one of these mechanisms, operate that path
with controlled data and local targets. Cause no unrequested external or
durable effect to gather interaction evidence:

- Navigation, controls and adaptive view changes: verify orientation, available
  back and cancel paths, actual change and save timing and preservation of the
  working context needed for the task. Not every value or position must persist.
- Dialogs: open, reach controls, close or cancel and verify focus returns to the
  invoking control or the appropriate next location. Check that overlays and
  sticky regions do not obscure focused controls.
- Dragging: complete the same task without dragging unless an applicable WCAG
  exception applies. Exercise cancellation and preserve the resulting state.
- Forms and authentication: preserve relevant paste, autofill and password
  manager support. Check error association, safe value retention and correction.
  Avoid redundant entry and cognitive-function tests where WCAG 2.2 requires
  alternatives or assistance; preserve the criteria's actual exceptions.
- Async flows: delay or fail the relevant operation, then observe loading,
  partial results, duplicate-action prevention, cancellation, retry and stale
  responses. A late old response must not overwrite the current user's result.

When loading or input latency is a concrete risk in the requested flow,
observe layout movement and input responsiveness during the transition, not
only its settled end state.
Use focused local measurements when needed. Lab observations, emulation and
real-device interaction remain distinct; field performance claims require
matching field data. Do not introduce backend tuning or a universal benchmark.
