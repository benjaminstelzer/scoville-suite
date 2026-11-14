# Layout and adaptation

Apply
[Quality's ownership table](ui-quality.md#product-ownership-and-ui-guarantees):
the product record decides grouping and responsive priorities.

## Make relationships perceptible

- Show meaningful groups, order and emphasis with the means of whatever sets
  the visuals: the design system where one exists, otherwise the framework
  or the local direction from [Framework](framework-alignment.md). Add a
  container or decoration only around contents that belong together.
- Compare elements equal in meaning and behavior. Where two differ, read
  their source: a difference set through a variant or token is usually
  deliberate, a one-off override usually drift; look for a stated reason
  either way. Keep deliberate differences; fix accidental drift where it is
  set, in the elements the task changes.
- A value that comes from the platform, framework or component is no defect
  just for being off a numeric scale, such as a component's own 10px gap
  beside a 4/8/16 scale. A literal the change adds follows SKILL.md's value
  check.
- When SKILL.md's References table selects [Validation](validation.md), that
  file selects the conditions (widths, states, themes, content, settings) and
  the checks for geometry, appearance and consistency.

## Adapt instead of merely shrinking

- Derive each adaptation from content, supported environments and the
  breakpoints and transformations the project, design system or platform
  defines. Change flow, grouping, disclosure or density; keep meaning,
  required content and controls, status and recovery.
- Where possible keep one markup order and adapt it with the project's
  responsive mechanism. Clipping or hiding required content does not solve
  overflow.
- A sequential task shows its steps in order. Where users often compare or
  switch, put related panes side by side where space allows. On small
  screens a sequence of views keeps that relation and the needed context.

## Reassess composition after changes

After elements change, reassess from the source the affected group's
hierarchy, space and transitions against its task. Where needed, adjust the
local composition through the component, token or layout mechanism that sets
it; keep functions and settled decisions. Report a required wider redesign
as a conflict.
