---
name: scoville-ui
description: "Implement or audit interfaces through their framework and design system. Use for information structure, layout, interface wording, components, states, interactions, responsiveness, accessibility and rendered checks. The WordPress adapter covers plugin-owned wp-admin pages, including hypothetical implementation advice; pure visual concepts keep their design scope. Excludes non-UI backend work and prose unrelated to interface text."
compatibility: "Agent Skills host with reference access and the project's framework tools. Geometry proof needs DOM or equivalent measurement; visual proof needs viewed renders; interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No mandatory network. Developed for Codex and Claude Code. Python 3.11+ and the bundled text-size checker are required for output capture, size checks and delivery as a file."
---

# Scoville UI

Implement and verify UI through its established framework, platform and design
system. An owner is the source responsible for a decision or behavior: product
requirements for intent, a design system for visuals, a component for
mechanics.

{{ include: rules.optout }}

## Mode and scope

Use **Implement** for requested creation, changes or fixes and **Audit** for
inspection, explanation or evaluation. An audit changes no product file: it
reads, runs only what its evidence route below allows, with disposable
output where Scoville Code permits it, and reports. It covers the requested
page, region and concerns. Design-only work produces a design; code changes
and publication each need their own request.

Choose the evidence route before any execution:

| Request or finding | Authorized interface evidence |
| --- | --- |
| Implement, including a reported problem explained by source | Check the affected source and applicable non-browser tests. |
| Implement to fix a reported visual defect the affected markup, applied styles and component source do not explain | Render to find its cause. Then fix the source and run further rendered checks only as requested. |
| Review of interface source or of an unimplemented design, or evaluation of supplied evidence. A review of a UI change that does not name appearance, behavior or a rendered check is a source review. | Use the source, the design and the supplied proof. Static checks and non-browser tests may run where the request or assignment permits execution. Do not render, measure or operate the running interface; report which required observations are missing. |
| Review or audit of appearance or behavior, or a requested rendered check | Inspect the running interface within the requested scope. Observe state without saves, submissions or external effects during an Audit. |

### Read the request

A mockup, screenshot or example the user supplies is part of the request: read
it before building and build what it shows, including what it leaves out.
Where a word for position, size or emphasis allows more than one reading, such
as which edges line up or how small, the supplied image decides; without one,
the elements beside it do, as [Spacing, size, alignment and literal
values](#spacing-size-alignment-and-literal-values) says. A rule the user
gives for one place or case applies there, and to another place, state or
element only where the same reason holds.

## Owners

For each concern, the first of these that settles it is its owner: system,
safety and legal requirements; the explicit user request, including informed
acceptance of a reported limitation; repository instructions; canonical
product requirements, design-system components, wrappers, themes, semantic
tokens and approved assets; the owning framework or platform; deliberate,
owner-aligned local patterns; and last this Skill's own principles.

Preserve settled decisions and use supported components and APIs. Report a
material conflict with the exact owning component's limitation, and obtain the
missing owner decision before the change that depends on it. Informed
acceptance can waive a reported limitation, but not a system, safety or legal
requirement.

Reuse a local pattern when it is deliberate, current and suitable for this
page; inspect an unclear exception, and normalize only an established
accident or stale pattern through the component or layout responsible for
the affected group. Without a visual owner, use Framework's bounded
local direction; framework defaults remain primitives.

## Accessibility

The base holds on the frontend and the backend, for every control the task
adds, alters or reviews:

- It can be reached and operated with the keyboard alone, and the focused
  control is visible.
- It is the element or component that carries its meaning: a button acts, a
  link navigates. Where nothing existing provides it, use the native element
  or a supported primitive.
- An input has a label tied to it in the markup or the platform's
  accessibility API, and a control without visible text has a name that says
  its purpose. Where a label gets its meaning only from the question its
  group answers, that question is the group's name in the markup or the
  platform's accessibility API.

Beyond the base there is one level: WCAG AA in full, in version 2.1 unless
the rule file names 2.2. It holds for the frontend or the backend when the
project's rule file says so, which a project does where the law requires it.
The line names a level for each, for example
`Accessibility: frontend WCAG 2.1 AA, backend base`. The backend is where
the product is administered, `wp-admin` included; everything visitors use is
the frontend. A component used on both meets the stricter level.

Where that line is missing and the task, beyond the text-only case under
[References](#references), adds or alters an element of the interface, ask the
user once whether the law requires WCAG AA for the frontend, the backend or
both, and record the answer as that line, with version 2.1 unless the user
chooses 2.2, in the project's rule file with Scoville
Project Context Cleanup. A review, an audit or a run without a
user to ask does not ask and works to the base.

Where the base holds, nothing beyond the base is built or reported as
missing. Where WCAG AA holds,
[Accessibility](references/accessibility.md) applies as well.

## Skill coordination

{{ include: family.contract }}

{{ include: family.neighbors }}

UI owns task flow, information structure, new interface wording and
terminology, framework-valid implementation, semantics, states, focus and
input, and responsive mechanics.

For interface-only work, use this entry and the project's source and local
test commands. Use the Code workflow for affected server-side behavior or a
separate consumed contract.

## References

For a change to copy or the displayed value in an existing text element
whose role, visibility rules, layout and interaction stay the same, read only
[Wording](references/ui-wording.md). In WordPress plugin or theme code also
read [internationalization](references/wordpress/internationalization.md)
when the change affects placeholders, plurals, context or escaping, or the
string is not yet translatable.

For other interface work, read every reference whose row matches before the
work it governs, and beyond those only a section one of them points to:

| Reference | Read when |
| --- | --- |
| [WordPress routing](references/wordpress/routing.md) | Any `wp-admin` work, including advice and ownership questions. Read it first: it selects the [adapter](references/wordpress/adapter.md) for a plugin-owned page and the other WordPress files. |
| [internationalization](references/wordpress/internationalization.md) | WordPress plugin or theme code, in `wp-admin` or elsewhere, adds, changes or reviews a string a user sees or assistive technology reads. |
| [Framework](references/framework-alignment.md) | Outside `wp-admin`, the owner or the implementation path is unresolved: unfamiliar stack, interacting layers, uncertain customization, no visual owner, or a component limit in the way. |
| [Accessibility](references/accessibility.md) | The frontend or backend being worked on is at WCAG AA under [Accessibility](#accessibility). |
| [Structure](references/ui-structure.md) | New interface, or a changed task flow, composition, grouping, size, spacing or responsive behavior, or a review or audit of those. |
| [Interactions](references/ui-interactions.md) | Control behavior, focus, input, asynchronous feedback or recovery. |
| [Wording](references/ui-wording.md) | New, translated, changed or reviewed interface text or a control's accessible name, also as part of another change. |
| [Validation](references/validation.md) | The evidence route inspects the running interface or evaluates supplied rendered evidence. Reuse proof that covers the current source and conditions. |
| [Geometry and sight](references/ui-geometry-validation.md) | With Validation, for a judgment of size, distance or appearance. |
| [Consistency audit](references/ui-consistency-audit.md) | With Validation, for the consistency of a page or region. |
| [Code quality](references/code-quality.md) | UI code beyond text or formatting, or a review of interface source. Use its review section for a source review, whoever requested or assigned it. |

{{ include: rules.references }}

## Only what the task needs

Every text, hint, message, icon, status display, confirmation step, control
and option you add is something the user has to read and the project has to
translate and keep in step, and it hides what matters. An addition needs a
need, whether you build it or ask for it in a review: the request, a project
rule, the product record, or an applicable rule of this Skill that an element
the change adds or alters would otherwise break. That it could help is not a
need. Without one:

- no sentence that says what does not happen or was not done;
- no success line for an action whose result the page already shows;
- no second copy of a status in another place or for another audience;
- no explanation of how the implementation works;
- no step in which the user confirms or carries out what the product can do
  itself, and no block on input the product can clean up.

The interface offers the user's action, not the implementation's steps:
internal phases, limits and mechanics stay internal. Where an addition seems
necessary and nobody asked for it, name it in the report as a question.

## Before changing an existing element

Before you add a style rule, a handler or a state to an existing element,
find what already acts on it: other rules that match it, where a more
specific selector wins over yours; handlers and observers on it, on its
ancestors or on the whole page; code that replaces or rebuilds it; the order
in which the page initialises it; and what the host platform's own styles and
scripts do to that kind of element. Make the change where it takes effect
against these. Reuse an existing state only after reading everything else
that state switches.

Preserve the affected states, input, semantics and recovery, also where the
design is settled. When moving, removing, reinserting or replacing stateful
controls, read the required live state from its owner immediately before the
mutation and keep or restore it through the component's API. A remembered
value is valid only if all writers update it; programmatic changes need not
emit user events. Keeping the same element object does not preserve its live
selection, focus or editing state automatically. For what the new path has
to keep setting, apply rule 6 of [Code quality](references/code-quality.md).

{{ include: rules.preserve_existing }}

## States of what you add

For each element you add or make conditional, go through the values its data
can take, including zero, empty, filtered out, loading, read-only, no
permission, finished, failed and nothing to do, and decide what it shows in
each. Where it cannot help the user, it is not shown, and what belongs to it
(separator, label, frame, count) goes with it. Where more than one path
produces the same element, such as a server render and a client update, change
each and compare them.

For lists and repeated updates, apply rule 1 of
[Code quality](references/code-quality.md).

## Use what exists

Deliver the requested behavior through the components and layouts responsible
for it, including shared ones. Where the project's own code, the design system
or the framework already provides a component, class, variant or token that
meets the required semantics, states and behavior, use it, so the product
keeps one button, one field and one badge; a hand-written copy of something
that exists is a defect. Fit it to its place through its size variant or a
local size. When nothing existing covers the need, write the new component in
the layer that holds the project's own components of that kind, the way those
are written. Check the framework version when an API choice depends on it.
Appearance never justifies removed focus or input support or hidden required
content.

### Custom styling

Custom styling of an existing component, including inline styles and styling
props, is an exception:
use it only where supported composition and variants cannot meet a need,
apply it at the component or layout that needs it, and say in the report
which need the responsible component or API does not meet. An official token
alone does not justify it. Keep a local exception local instead of a global
theme override.

## Spacing, size, alignment and literal values

The aim is a change that looks as if it had always been part of the page;
most visible defects are small mismatches with what is already there. For each
element you add, or whose size, spacing or position you change, work from the
outside in:

1. Outer size first. Before writing a control or row, find the existing ones
   it has to match, nearest first: the same row or bar, then neighbouring
   regions of the same level, then others of its kind on the rest of the
   page. Skip a match whose size comes from a one-off override rather than
   its component, variant or the project's tokens; match the deliberate
   pattern instead. Read how that one is written, its component, size variant and
   classes, and write the new one the same way, so it gets the same height,
   radius, font size and padding; a new row takes the padding of the rows
   around it, equal above and below its content unless those rows differ.
   Leaving a component's size unset picks its default, which is right only
   where the neighbours use the default. Where the design calls for the same
   dimensions across different components, choose the variants whose source
   provides them.
2. Then fit it in. Whatever goes into an existing control, row or bar takes
   the size variant that fits the containing layout and leaves equal space
   above and below it. Inside a control, such as a step button in a number
   field, the space at its outer edge matches that space; in a row or bar it
   keeps the content edge the other items keep. An icon beside a label takes
   its size from that label's text, not from the icon set's default. Where no
   variant fits, apply [Custom styling](#custom-styling) at the responsible
   component or layout. Preserve dimensions required by the owning design.
3. Give each edge and centre a definite reference to line up with, such as
   the neighbouring control's centre line or the container's content edge,
   and derive the offset from the actual paddings and borders in between.
   Texts in one row line up on their baseline, and a control or icon beside
   a text is centred on that text's line; the edges of their boxes line up
   only where no text relates them.
4. Count every source of space between two elements once: parent gap, own
   margin, sibling margin, wrapper padding, whitespace between inline
   elements, legacy element rules, the host platform's rules for that
   element, and the empty space inside a box that is larger than what it
   shows, such as a pointer target around a small icon. Two sources for one
   gap is the usual cause of doubled or uneven spacing. A pointer target that
   has to be larger than its icon extends into the space around it instead
   of adding to it.
5. Keep inner insets of one control equal on both sides. An indicator that
   appears only in some states, such as a spinner or badge, does not move its
   neighbours when it appears; content shown for a state, such as an error
   message or an opened disclosure, may push what follows down.

A literal size, spacing or colour value the change adds needs a precedent on
an element of the same role in the page, or support in the project's tokens
or rules for that element. That the value occurs somewhere is no precedent,
and neither is a preference for a font, palette, radius, shadow, card
pattern, breakpoint or pixel value, in what you build or in what a review
asks for. Only the request, step 2 or, where there is no visual owner,
Framework's local direction sets a value without one. When changing a style
value, keep its authored unit or expression: equal current pixels do not
turn `1rem` into `16px`.

## Check and report

Before delivery or in a review of interface source, check each element the
change adds or alters against the sections above and the selected
references, together with Code where it applies. The changed lines alone do
not show most interface defects: what those sections have an implementer
find or read first, a review searches for in the existing code.

Asking for something the change does not contain needs a need: for the
interface under [Only what the task needs](#only-what-the-task-needs), for
the code behind it under rule 2 of [Code quality](references/code-quality.md).

A size, a gap, an offset or the space inside a box that the source
determines is computed from the values and judged. Report as unverified only
what depends on the rendering or lies outside the evidence route.

A finding names its place (file and line, or the element observed), the rule
it breaks, what was observed, its effect and the simplest sound correction.
Keep confirmed defects apart from suspicions, and order findings by impact;
among equal ones, source defects come before rendered ones. When none was
found, say so for the inspected scope only: a targeted check cannot show that
the whole interface complies. Writing an explicitly requested audit report is
part of the Audit. For Implement, report the changes, the checks they rest on
and their limits, with what Code's report requires where that Skill applies.
Where the change alters what a state or place the request does not name
shows, say what it shows now and ask whether that is wanted.
Where no accessibility level is recorded and the user was not asked, the
report says that none is recorded and that the work was held to the base.
When a requested check selected Validation, use its results to decide
acceptance too.
