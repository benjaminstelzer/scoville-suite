# UI Quality

Apply the guarantees the task touches. The [UI entrypoint](../SKILL.md)
selects the topic references and evidence route.

## Product ownership and UI guarantees

Read the supplied product record, such as requirements or a design brief; it
decides the middle column. Keep its decisions. Where the project, the design
system or the framework already provides a component, token or platform
mechanism for one, build it with that. Keep the right column working.

| Concern | Product decides | UI keeps working |
| --- | --- | --- |
| Primary task | Priority, information sequence, action hierarchy | Required controls and content, semantics, task completion |
| Reading | Typography, spacing roles, emphasis | Scaling, zoom, wrapping, truncation access, labels, contrast per theme and state, supported fallbacks |
| Accessibility | Inclusive communication and equivalent meaning | Semantic, interaction, platform, scaling, input-alternative, status and rendered mechanics |
| Layout | Grouping, hierarchy, density, deliberate exceptions | The project's, design system's or framework's components and tokens, semantic relationships |
| Responsive intent | Transformation and priority changes | Valid breakpoints, reflow, persistent content and state, input behavior |
| Interaction | Affordance emphasis, feedback priority, recovery experience | Component semantics, focus and input, announcements, transitions |
| State | Presentation, priority and recovery | Every component state, semantics, focus, announcements, transitions |

## Start with the user task

In each decision region the task creates or changes, such as a form, make
the task and next action apparent:

1. One action is visibly primary. Before pressing, the user can tell what
   it acts on, which fields it uses, what must come first and its
   consequences, for example through a button `Delete 3 orders` or a visible
   selection count beside `Delete`.
2. Secondary actions stay available with less emphasis.
3. Put rare detail behind a disclosure. Required fields, errors and critical
   consequences never go there, and the disclosure does not get in the way of
   frequent expert work.
4. Needed values and terms stay visible; working context survives state and
   viewport changes.

Keep legitimate density and independent decision regions. Remove or demote
content only when whoever decides that content permits it (the user,
repository instructions, the product record, or the design system or platform
it comes from) and the task stays complete.

## Preserve readable content

Use the project's or platform's typography and spacing, and keep:

- a clear reading order and heading structure;
- legibility at supported text scaling and zoom;
- room to wrap for realistic and localized content;
- deliberate truncation with a way to reach required information;
- each label tied to its value, visually and programmatically (markup or the
  platform's accessibility API); and
- foreground (text, icons, control and focus cues) and background that meet
  the applicable accessibility target in every supported state and theme.

Keep protected copy and facts. Unless the task explicitly includes a wording
change, fix the layout: let `Billing address` wrap or widen its column.

## Keep accessibility structural

Accessibility is not a final color pass. Choose the component and layout so
that they keep the required names, labels, roles, values, relationships,
reading order, focus behavior, input alternatives, scaling and status
messages. Use approved wording where supplied, otherwise the
[wording rules](ui-wording.md), in both the visible text and the names the
code exposes.

- The accessible name starts with the control's visible text where possible.
- An icon-only control is named by its purpose.
- No meaning rests on color, position, shape, hover or motion alone.
- Numbers come from the applicable standard or platform rule. Where WCAG 2.2
  AA applies under the entrypoint's ownership rules, web pointer targets meet
  its 24 by 24 CSS-pixel requirement or an applicable
  documented exception; do not invent a universal 44-pixel AA target or
  substitute measurements.
- An automated scan does not prove the interaction is usable.

## Evidence for usability

Checks of information order, grouping and recovery are heuristics for this
task. WCAG requirements are normative where applicable; platform conventions,
APG implementation guidance and this Skill's choices are not additional WCAG
criteria. An expert
walkthrough can show where prerequisites, action scope and recovery are
exposed. Saying an interface is usable for a target population requires
observations with such users.
