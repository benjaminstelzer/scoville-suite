# UI Quality

Apply the common task, readability and accessibility rules below. Read each
complete topic file only when its concern can change the requested outcome.

| Concern | Reference |
| --- | --- |
| New, translated, changed or reviewed interface text | [Wording](ui-wording.md) |
| Grouping, hierarchy, layout, responsive adaptation or changed composition | [Layout](ui-layout.md) |
| Navigation, controls, focus, input, feedback, states or recovery | [Interactions](ui-interactions.md) |

These are outcome tests, not a visual recipe. A settled unrelated concern adds
no topic read. Preserve canonical decisions and all affected implementation guarantees.

## Product ownership and UI guarantees

Read the supplied product record and preserve its decisions; UI implements them through their owner.

| Concern | Product owns | UI preserves |
| --- | --- | --- |
| Primary task | Priority, information sequence, action hierarchy | Required controls/content, semantics and task completion |
| Reading | Typography, spacing roles, emphasis | Scaling, zoom, wrapping, truncation access, labels, theme/state contrast, supported fallbacks |
| Accessibility | Inclusive communication and equivalent meaning | Semantic, interaction, platform, scaling, input-alternative, status and rendered mechanics |
| Layout | Grouping, hierarchy, density, deliberate exceptions | Canonical components/tokens and semantic relationships |
| Responsive intent | Transformation and priority changes | Valid breakpoints, reflow, content/state persistence, input behavior and rendered proof |
| Interaction | Affordance emphasis, feedback priority, recovery experience | Component semantics, focus/input, announcements and transitions |
| State | Presentation, priority and recovery | Component state coverage, semantics, focus, announcements, transitions and proof |

## Start with the user task

Make the task and next meaningful action apparent in each decision region.
Give that region a clear primary action, with its affected object, fields,
prerequisites and consequences understandable before activation. Preserve
legitimate density and independent decision regions.

Keep secondary actions available without equal emphasis. Disclose rare detail
without hiding required fields, errors or critical consequences, or obstructing
frequent expert work. Keep needed values and terms visible; preserve working
context across states and viewports. Remove or demote content only when its
owner permits it and the task remains complete.

## Preserve readable content

Use the project or platform's typography and spacing language while protecting:

- a clear reading order and heading structure;
- legibility at supported text scaling and zoom;
- wrapping and available space for realistic and localized content;
- deliberate truncation with a way to access required information;
- labels and values that remain associated visually and programmatically; and
- foreground and background relationships that meet the applicable accessibility
  target across supported states and themes.

Preserve protected copy and facts. Honor wording changes explicitly included in
the task; otherwise fix the presentation constraint instead of shortening,
fragmenting or inventing text to hide a layout problem.

## Keep accessibility structural

Accessibility is not a final color pass. Confirm that required names, labels,
roles, values, relationships, reading order, focus behavior, input alternatives,
scaling, and status communication survive the chosen component and layout.
Use approved wording where supplied; otherwise apply the [wording rules](ui-wording.md). Verify that the interface exposes and presents it correctly.

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
