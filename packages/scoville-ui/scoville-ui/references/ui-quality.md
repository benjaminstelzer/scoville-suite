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
Preserve product intent.

For each visible region, ask:

- What decision or action does it support?
- What information must be understood before that action?
- What can remain secondary, progressive, or contextual?
- What must persist across state or viewport changes?

Required prerequisites and consequences precede the action that needs them.
Disclose rare secondary detail through understandable controls, while keeping
required fields, errors and critical consequences discoverable in time. Avoid
repeated disclosure steps that obstruct frequent expert work. Keep needed values
and object and action terms visible so users recognize rather than recall.
Remove or demote content only when doing so preserves the user's task and the
canonical content owner permits it.

## Preserve readable content

**Product decision:** The canonical product owner owns typography, spacing roles, and intended
reading emphasis. **UI implementation floor:** UI retains text scaling, zoom,
wrapping, truncation access, label association, theme and state contrast, and
supported fallback mechanics.

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

**Product decision:** The canonical product owner owns inclusive communication and equivalent
meaning. **UI implementation floor:** UI retains semantic, interactive,
platform, scaling, input-alternative, status, and rendered mechanics.

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
