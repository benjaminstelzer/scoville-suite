# UI Quality

Apply only the lenses that can change the requested outcome. These are outcome
tests, not a visual recipe.

## Contents

- Start with the user task
- Make relationships perceptible
- Preserve readable content
- Make interaction predictable
- Adapt instead of merely shrinking
- Design states as part of the same interface
- Keep accessibility structural

## Start with the user task

**Product decision:** Primary-task priority, information sequence, and intended
action hierarchy belong to the canonical product owner. Consume its record when supplied.
**UI implementation floor:** Required controls, content, semantics, and task
completion remain available through the owning framework.

Make the primary task and its next meaningful action understandable from the
interface, not from implementation knowledge. Secondary actions and supporting
information should remain available without competing equally for attention.
Use one primary next action per decision region, not a page-wide one-button
limit. Make each action's affected fields, object and consequence clear before
activation. Preserve legitimate information density and separate decision regions.
Preserve domain terminology and product intent; do not simplify away necessary
distinctions.

For each visible region, ask:

- What decision or action does it support?
- What information must be understood before that action?
- What can remain secondary, progressive, or contextual?
- What must persist across state or viewport changes?

Required prerequisites and consequences precede the action that needs them.
Disclose rare secondary detail through understandable controls, while keeping
required fields, errors and critical consequences discoverable in time. Avoid
repeated disclosure steps that obstruct frequent expert work. Keep needed values
and consistent object/action terms visible so users recognize rather than recall.
Remove or demote content only when doing so preserves the user's task and the
canonical content owner permits it.

## Make relationships perceptible

**Product decision:** The canonical product owner owns intended grouping, hierarchy, density,
and deliberate visual exceptions. **UI implementation floor:** Implement those
relations with canonical components/tokens and preserve semantic relationships.

Use the owning system's hierarchy, grouping, alignment, sequence, and emphasis
mechanisms so related information reads together and distinct concerns remain
distinct. Visual difference must represent a real difference in meaning or
interaction. Avoid adding containers, decoration, or emphasis that creates no
new relationship.

Consistency means that the same meaning and behavior receive the same treatment
within the relevant product context. It does not mean making unlike tasks look
identical. Preserve a deliberate exception when it communicates a genuine
difference. Fix accidental drift at the canonical owner when the fix is in
scope; otherwise report it without expanding the task.

For consistency, compare owner-backed equivalent relationships and component
variants. Native differences are not defects merely because they break a
numeric scale. Use Validation's geometry and optical diagnosis separately,
including inventory coverage when auditing a named page.

## Preserve readable content

**Product decision:** The canonical product owner owns typography, spacing roles, and intended
reading emphasis. **UI implementation floor:** UI retains text scaling, zoom,
wrapping, truncation access, label association, theme/state contrast, and
supported fallback mechanics.

Use the project or platform's typography and spacing language while protecting:

- a clear reading order and heading structure;
- legibility at supported text scaling and zoom;
- wrapping and available space for realistic and localized content;
- deliberate truncation with a way to access required information;
- labels and values that remain associated visually and programmatically; and
- foreground/background relationships that meet the applicable accessibility
  target across supported states and themes.

Preserve protected copy and facts. Honor wording changes explicitly included in
the task; otherwise fix the presentation constraint instead of shortening,
fragmenting or inventing text to hide a layout problem.

## Make interaction predictable

**Product decision:** The canonical product owner owns intended affordance emphasis, feedback
priority, and recovery experience. **UI implementation floor:** UI retains
component semantics, focus/input behavior, announcements, and state transitions.

Use existing components and platform conventions so affordance and behavior
agree. For the states introduced or changed by the task, preserve the cues and
recovery needed to answer:

- What can I act on?
- What has focus or selection?
- Did the action start, succeed, fail, or become unavailable?
- What changed, and can I recover or retry?
- What input method and interaction sequence does this control support?

Do not depend on hover for required information or operation. Keep focus order,
keyboard behavior, touch behavior, programmatic relationships, announcements,
and motion accommodations intact. Name actions by their real result and provide
a nearby associated reason for disabled actions. Confirm consequential actions
that cannot easily be undone; offer undo only when restoration exists.
A custom visual treatment must not weaken the
owning component's semantics or state model.

## Adapt instead of merely shrinking

**Product decision:** The canonical product owner owns the intended responsive transformation
and priority changes. **UI implementation floor:** UI retains framework-valid
breakpoints, reflow mechanics, content/state persistence, input behavior, and
rendered proof.

Responsive behavior preserves the task as space, content, text size, input
method, orientation, or window mode changes. Determine transformations from the
content and the project's supported breakpoints rather than imposing a fixed
device matrix.

Depending on the task and owner, adaptation may change flow, grouping,
disclosure, navigation, ordering, density, or interaction form. Preserve
meaning, required controls, status, and recovery. Do not clip, hide, or collapse
required content simply to eliminate overflow. Avoid separate interaction logic
for each viewport when one semantic flow can adapt through canonical layout
mechanisms.

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
or fieldset/legend for related inputs.

Do not manufacture a complete state matrix for an unaffected component. The
floor is completeness for the requested flow, not ceremonial coverage.

## Keep accessibility structural

**Product decision:** The canonical product owner owns inclusive communication and equivalent
meaning. **UI implementation floor:** UI retains semantic, interactive,
platform, scaling, input-alternative, status, and rendered mechanics.

Accessibility is not a final color pass. Confirm that required names, labels,
roles, values, relationships, reading order, focus behavior, input alternatives,
scaling, and status communication survive the chosen component and layout.
The content owner supplies wording; UI verifies that the interface exposes
and presents it correctly.

Visible control text belongs in its accessible name, preferably at the start.
Name icon-only controls by purpose. Do not convey meaning solely through color,
position, shape, hover or motion. Use the applicable standard or platform rule
for quantitative requirements. Web pointer targets meet WCAG 2.2 AA's 24 by 24
CSS-pixel requirement or an applicable documented exception; do not invent a
universal 44-pixel AA target.
Do not invent substitute measurements or treat an automated scan as proof that
the interaction is usable.

## Evidence for usability

Information-order, grouping and recovery checks are task-specific heuristics.
WCAG requirements remain normative where applicable; platform conventions and
Skill choices are not additional WCAG criteria. An expert walkthrough can show
where prerequisites, action scope and recovery are exposed. Claims of usability
for a target population require observations with relevant users.
