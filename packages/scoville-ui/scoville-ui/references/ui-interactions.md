# Interaction and states

## Navigation and orientation

Structure navigation around user tasks and content relationships. Distinguish
global destinations from local views and actions. Make the current location
and available back or cancel paths understandable and accessible through
platform conventions. Avoid unnecessary hierarchy depth and detours between
related content. Preserve needed working context across navigation when safe
and appropriate to the task.

## Make interaction predictable

**Product decision:** The canonical product owner owns intended affordance emphasis, feedback
priority, and recovery experience. **UI implementation floor:** UI retains
component semantics, focus and input behavior, announcements, and state transitions.

Use existing components and platform conventions so affordance and behavior
agree. Choose controls by meaning: navigation, action, single selection,
multiple selection or activation. Follow the owning component's contract;
presentation and feedback must make clear when changes take effect or are saved.
Prefer native semantics and supported existing primitives to custom widgets.
When the task needs a custom composite control, verify its relevant focus and
keyboard sequence in the interactive runtime.

Use modal interruptions for bounded content or interactions that need attention
before continuing. Keep ordinary editing and local field errors in their
working context; do not put complex routine flows in dialogs by default.

For the states introduced or changed by the task, preserve the cues and
recovery needed to answer:

- What can I act on?
- What has focus or selection?
- Did the action start, succeed, fail, or become unavailable?
- What changed, and can I recover or retry?
- What input method and interaction sequence does this control support?

Do not depend on hover for required information or operation. Keep focus order,
keyboard behavior, touch behavior, programmatic relationships, announcements,
and motion accommodations intact. Provide a nearby associated reason for
disabled actions. Confirm consequential actions
that cannot easily be undone; offer undo only when restoration exists.
A custom visual treatment must not weaken the
owning component's semantics or state model.

## Design states as part of the same interface

**Product decision:** The canonical product owner owns intended state presentation, priority,
and recovery. **UI implementation floor:** UI retains component state coverage,
semantics, focus, announcements, transitions, and implementation proof.

Review only states affected by the change, including relevant initial, empty,
loading, partial, success, error, unavailable, and permission-dependent states.
Keep structure stable enough for orientation while making the state change
perceptible through more than one fragile cue. Place feedback where the user can
associate it with the action, and preserve a clear next step or recovery path.

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

Do not manufacture a complete state matrix for an unaffected component. The
floor is completeness for the requested flow, not ceremonial coverage.


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

These are scoped triggers, not a requirement to add every mechanism or test
unaffected flows. WCAG is the normative source where applicable; APG is
implementation guidance, not an additional conformance standard.
