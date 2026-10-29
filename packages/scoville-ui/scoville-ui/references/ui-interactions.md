# Interaction and states

Apply [Quality's ownership table](ui-quality.md#product-ownership-and-ui-guarantees):
preserve component semantics/state coverage, focus/input, announcements,
transitions and proof, including on a direct Validation route.

## Navigation and orientation

Organize navigation around tasks and content relationships, distinguishing
global destinations from local views/actions. Show location and accessible
back/cancel paths through platform conventions; preserve needed working context
without unnecessary detours.

## Make interaction predictable

Choose controls by meaning and use native semantics and supported primitives.
Make action availability, focus/selection, save timing, progress, outcomes and
recovery apparent. For a custom composite control, exercise its focus and
keyboard sequence. Use modals for bounded attention-before-continuation tasks;
keep ordinary editing and field errors in context.

Do not depend on hover for required information or operation. Keep focus order,
keyboard behavior, touch behavior, programmatic relationships, announcements,
and motion accommodations intact. Provide a nearby associated reason for
disabled actions. Confirm consequential actions
that cannot easily be undone; offer undo only when restoration exists.
A custom visual treatment must not weaken the
owning component's semantics or state model.

## Design states as part of the same interface

Cover affected initial, empty, loading, partial, success, error, unavailable and
permission states. Preserve orientation, make changes perceptible beyond one
fragile cue and associate feedback with its action and real next/recovery step.

Distinguish no data from filtered zero results and incomplete results. Preserve
usable partial results and name what is missing. Keep feedback discoverable for
as long as its consequence requires. Never report success after a failed action.
For missing permission, explain unavailable access without sensitive details,
keep unavailable actions consistent and provide a safe return to the task.

Use persistent visible labels, with placeholder text only as a supplement.
Explain format, requiredness and consequences before avoidable errors. Associate
errors with their fields, preserve safe entered values and offer only real
correction, retry or cancellation. Add an error summary when it helps locate
multiple errors, not as a universal platform rule. Use the owning group component
or fieldset with a legend for related inputs.

## Exercise affected transitions

When the requested flow includes these mechanisms, operate the relevant path
with controlled data and local targets. Do not cause unrequested external or
durable effects merely to gather interaction evidence:

- Navigation, controls and adaptive view changes: verify orientation, available
  back and cancel paths, actual change and save timing and preservation of the working
  context needed for the task. Do not require every value or position to persist.
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

When loading or input latency is a concrete risk, observe layout movement and
input responsiveness during the transition, not only its settled end state.
Use focused local measurements when needed. Lab observations, emulation and
real-device interaction remain distinct; field performance claims require
matching field data. Do not introduce backend tuning or a universal benchmark.

These triggers apply to the requested flow. WCAG is normative where applicable;
APG is implementation guidance, not an additional conformance standard.
