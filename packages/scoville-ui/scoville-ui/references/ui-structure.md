# Interface structure and layout

This file holds who decides the structure of an interface, the user task and
its actions, readable content, grouping and how the layout adapts. Read it for
a new interface, a changed task flow or composition, a change to grouping,
size, spacing or responsive behavior, and for a review or audit of these.

## Product ownership and UI guarantees

Read the supplied product record, such as requirements or a design brief; it
decides the middle column. Keep its decisions. Keep the right column working.

| Concern | Product decides | UI keeps working |
| --- | --- | --- |
| Primary task | Priority, information sequence, action hierarchy | Required controls and content, semantics, task completion |
| Reading | Typography, spacing roles, emphasis | Wrapping, truncation access, labels, supported fallbacks |
| Layout | Grouping, hierarchy, density, deliberate exceptions | The project's, design system's or framework's components and tokens, semantic relationships |
| Responsive intent | Transformation and priority changes | Valid breakpoints, reflow, persistent content and state, input behavior |
| Interaction | Affordance emphasis, feedback priority, recovery experience | Component semantics, focus and input, transitions |
| State | Presentation, priority and recovery | Every component state, semantics, focus, transitions |

## Start with the user task

In each decision region the task creates or changes, such as a form, make
the task and next action apparent:

1. One action is visibly primary. Before pressing, the user can tell what
   it acts on, for example through a button `Delete 3 orders` or a visible
   selection count beside `Delete`.
2. Secondary actions stay available with less emphasis.
3. Required fields, errors and critical consequences never go into a
   disclosure, and a disclosure does not get in the way of frequent expert
   work.
4. Decision-critical values, terms, states and actions stay visible, readily
   readable and findable, and no decoration obscures or competes with them.
   Judge this by the task, not by a fixed size hierarchy or a prescribed
   visual style.

Keep legitimate density and independent decision regions. Remove or demote
content only when whoever decides that content permits it (the user,
repository instructions, the product record, or the design system or platform
it comes from) and the task stays complete.

## Preserve readable content

Use the project's or platform's typography and spacing, and keep:

- a clear reading order and heading structure;
- room to wrap for realistic and localized content;
- deliberate truncation with a way to reach required information; and
- each label visibly tied to its value.

Fix the layout, not the text, as [Wording](ui-wording.md) says.

## Make relationships perceptible

- Show meaningful groups, order and emphasis with the means of whatever sets
  the visuals: the design system where one exists, otherwise the framework
  or the local direction from [Framework](framework-alignment.md). Add a
  container or decoration only around contents that belong together.
- Compare elements equal in meaning and behavior. Where two differ, read
  their source: a difference set through a variant or token is usually
  deliberate, a one-off override usually drift; look for a stated reason
  either way. [Owners](../SKILL.md#owners) says what to do with each.
- A value that comes from the platform, framework or component is no defect
  just for being off a numeric scale, such as a component's own 10px gap
  beside a 4/8/16 scale. A literal the change adds follows the rule for
  literal values in SKILL.md's
  [Spacing, size, alignment and literal values](../SKILL.md#spacing-size-alignment-and-literal-values).

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

## Evidence for usability claims

Checks of information order, grouping and recovery are heuristics for this
task. An expert walkthrough can show where prerequisites, action scope and
recovery are exposed. Saying an interface is usable for a target population
requires observations with such users.
