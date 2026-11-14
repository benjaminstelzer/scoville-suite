---
name: scoville-ui
description: "Implement or audit interfaces through their framework and design system. Use for information structure, layout, interface wording, components, states, interactions, responsiveness, accessibility and rendered checks. The WordPress adapter covers plugin-owned wp-admin pages, including hypothetical implementation advice; pure visual concepts keep their design scope. Excludes non-UI backend work and prose unrelated to interface text."
compatibility: "Agent Skills host with reference access and the project's framework tools. Geometry proof needs DOM or equivalent measurement; visual proof needs viewed renders; interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No mandatory network. Developed for Codex and Claude Code. Python 3.11+ for the bundled text-size checker; manual fallback only without suitable Python. Helper errors do not enable fallback."
---

# Scoville UI

Implement and verify UI through its established framework, platform and design
system. An owner is the source responsible for a decision or behavior: product
requirements for intent, a design system for visuals, a component for mechanics.

## Owners

If the user explicitly excludes this Skill, leave it out: do not read its
references, run its tools or base a change or statement on it. Continue other
authorized work. If a higher-authority rule requires this Skill, report that
conflict.

For each concern, the first of these that settles it is its owner: system,
safety and legally binding accessibility requirements; the explicit user request,
including informed acceptance of a reported limitation against a non-binding
target; repository instructions; canonical product requirements, design-system
components, wrappers, themes, semantic tokens and approved assets; the owning
framework or platform; deliberate, owner-aligned local patterns; and last this
Skill's own principles.

Preserve settled decisions and use supported components and APIs. Report a
material conflict with the exact owning component's limitation, and obtain the
missing owner decision before the change that depends on it. Informed
acceptance can waive a reported non-binding target, but not a system, safety
or legal requirement.

Reuse a local pattern when it is deliberate, current and suitable for this
surface; inspect an unclear exception, and normalize only an established
accident or stale pattern. Without a visual owner, use Framework's bounded
local direction; framework defaults remain primitives. Without an accessibility
target, use WCAG 2.2 AA on the web and current platform guidance elsewhere.

## Skill coordination

All Skills in this suite are installed and enabled together. Use the
Skill that owns a concern without checking its availability, and load only the
instructions the task needs.
Do not use a Skill that needs explicit activation before it is activated, or
one the user excluded.

UI owns task flow, information structure, new interface wording and
terminology, framework-valid implementation, semantics, states, focus and
input, and responsive mechanics. Preserve approved wording, which keeps its
product contract; make requested text changes yourself and keep each
control's visible text in its accessible name.

## Mode and scope

Use **Implement** for requested creation, changes or fixes and **Audit** for
inspection, explanation or evaluation. An audit is read-only: it reads and
reports. Design-only work produces a design; code changes and publication each
need their own request. Work on the requested page or region and concerns; a
local fix does not grow into a redesign or a whole-product audit.

## References

Read every reference whose trigger matches before the work it governs, and no
others. Establish platform support before advice that depends on it. An
ownership-only question loads Quality or Validation only when it also asks
about those concerns.

| Concern | Reference and trigger |
| --- | --- |
| Any `wp-admin` concern, including hypothetical advice or classification | Read [WordPress routing](references/wordpress/routing.md) first. For a plugin-owned page also read the [adapter](references/wordpress/adapter.md) before the first edit or finding: you write the change, or audit the page, against its checklist. Unknown ownership holds only the advice that depends on it; name the missing fact and answer the rest. For a surface the plugin does not own, such as the Block Editor sidebar, a metabox or a Dashboard widget, routing names the host's own mechanism to recommend; do not treat it as a plugin page or through the general route. |
| Themes, frontend output, non-WordPress surfaces, pure visual concepts | General route without admin references; a visual concept keeps its design scope. |
| General-route ownership or implementation path unresolved | [Framework](references/framework-alignment.md) before choosing an owner: unfamiliar stack, interacting layers, uncertain customization, no visual owner, or a component limit in the way. |
| Creating, changing or auditing an interface, a review of how it looks or behaves, or a code review of its source | Before the first edit or finding, read [Quality](references/ui-quality.md) and the topic files its table selects, even when the change looks obvious. The rules for spacing, sizes and alignment are in [Spacing, size and alignment](#spacing-size-and-alignment) below. |
| A requested review or audit of how an interface or a change looks or behaves, a requested rendered check or proof, a judgment of existing proof, or a reported visual defect whose cause you cannot find in the affected element's markup, applied styles and component definitions | Read [Validation](references/validation.md) first. Add [Geometry and sight](references/ui-geometry-validation.md) when spacing, sizes, alignment, paint or optical balance are measured or judged, and [Audit coverage](references/ui-consistency-audit.md) for page consistency. Reuse existing proof; repeat a check only for a concrete gap. For a reported defect, render only to find its cause, then fix it in the source. A code review of interface source, including a diff, reads the source and renders nothing; it and a source-structure audit follow the next rows. |
| Source-structure audit or unimplemented design direction | Framework and Quality by their triggers, without Validation; report rendering, interaction and accessibility as unverified. Stating those gaps needs no Validation read. |
| Choosing or implementing UI code beyond a text or formatting change; a code review of interface source | Read [Code quality](references/code-quality.md) before choosing the implementation or the first finding, within the framework's guarantees. |

WordPress routing and the references it leads to select among the platform
references:
[spacing](references/wordpress/spacing.md),
[classic-patterns](references/wordpress/classic-patterns.md) and
[fallback-composition](references/wordpress/fallback-composition.md) for
spacing and Core markup;
[wpds-tokens](references/wordpress/wpds-tokens.md),
[version-compatibility](references/wordpress/version-compatibility.md) and
[experimental-policy](references/wordpress/experimental-policy.md) for tokens,
versions and experimental components;
[responsive](references/wordpress/responsive.md) for page shells, narrow
widths and zoom;
[ui-guidance](references/wordpress/ui-guidance.md) for guidance, states and
accessibility; [internationalization](references/wordpress/internationalization.md)
and [translation-delivery](references/wordpress/translation-delivery.md);
[validation](references/wordpress/validation.md) for platform checks;
[examples](references/wordpress/examples.md) only for a concrete syntax or
composition question the contracts leave open;
[sources](references/wordpress/sources.md) for official-status claims; and
[classification-output](references/wordpress/classification-output.md) for a
requested structured classification.

## Shared references

Read one when its condition holds. A complete copy already in context counts
as read, including one embedded in your assignment. Read it again only when
that copy is incomplete or a reload is requested.

- [Writing](references/writing.md): a plan, decision, instruction, review, handoff or a report the user asked for as the result; a disputed conclusion.
- [Machine data](references/machine-data.md): a structured report, log file or saved state you must evaluate, such as JUnit XML or coverage data; a test runner's console summary is not one.
- [Shell commands](references/shell-commands.md): composed text or scripts passed through a shell; quoting, PowerShell encoding, exact bytes or several exit statuses matter.
- [Output delivery](references/output-delivery.md): before a command whose output may exceed the display limit; text that must fit a known limit; delivery as a file.
- [Python discovery](references/python-discovery.md): a Python command or bundled helper, no interpreter verified this session.
- [Instruction design](references/instruction-design.md): a reusable instruction, Skill rule or prompt template.

## Implementation and acceptance

Start every task by reading the references the table assigns to it, before
the first edit or finding; they hold the criteria that findings and choices
are judged by.

Before the first edit, read the surrounding code and the patterns the change
must match, and check the framework version where an API choice depends on
it. A settled design still needs the states, input and semantics the change
affects. Batch related changes.

Where the project's own code, the design system or the framework already
provides a component, class, variant or token for the kind of element you
need, use it, so the product keeps one button, one field and one badge; a
hand-written copy of something that exists is a defect. Fit it to its place
through its size variant or a local size. Write a new primitive when nothing
existing covers the need.

Custom styling, including inline styles and styling props, is an exception:
use it only where supported composition and variants cannot meet a need,
keep it to the smallest scope, and say in the report which need the
responsible component or API does not meet. An official token alone does not
justify it.

## Spacing, size and alignment

The aim is a change that looks as if it had always been part of the page;
most visible defects are small mismatches with what is already there. For each
element you add, or whose size, spacing or position you change, work from the
outside in:

1. Outer size first. Before writing a control or row, find the existing ones
   it has to match, nearest first: the same row or bar, then neighbouring
   regions of the same level, then others of its kind on the rest of the
   page. Read how that one is written, its component, size variant and
   classes, and write the new one the same way, so it gets the same height,
   radius, font size and padding; a new row takes the padding of the rows
   around it, equal above and below its content unless those rows differ.
   Leaving a component's size unset picks its default, which is right only
   where the neighbours use the default.
2. Then fit it in. Whatever goes into an existing control, row or bar takes
   the size variant that fits its current height and leaves equal space
   above, below and at the outer edge. Where no variant fits, set a local
   size on the new part; that is a styling exception, kept on that element.
   The container keeps its height.
3. Give each edge and centre a definite reference to line up with, such as
   the neighbouring control's centre line or the container's content edge,
   and derive the offset from the actual paddings and borders in between.
4. Count every source of space between two elements once: parent gap, own
   margin, sibling margin, wrapper padding and legacy element rules. Two
   sources for one gap is the usual cause of doubled or uneven spacing.
5. Keep inner insets of one control equal on both sides. Rows and controls
   the request does not ask to resize keep their size, and an element that
   appears only in some states does not move its neighbours when it appears.
6. Settle these relationships from the source while you write the code: the
   equivalent's component, class and stylesheet values are the evidence.
   Implementing, including fixing a reported defect whose cause the source
   shows, involves no rendering, measuring or operating of the running
   interface, on any platform; the report names what was not rendered or
   operated as unverified. When to render is set in the References table.
7. Before finishing a change, and in a code review of a change, search the
   added lines of the diff for size variants, size classes and literal
   heights, font sizes, radii, paddings and gaps. A new control whose
   resulting height, font size or radius differs from the neighbours step 1
   found is a defect, whatever its variant is called; an unset size resolves
   to the component's default. An added literal that occurs nowhere outside the change, neither
   in the page's source nor in the project's tokens or existing rules for
   that kind of element, is a defect, such as a 7px radius on a new tooltip
   where the project's radii are 4px and 8px. Sizes the request asks for and
   step 2's local size are the exceptions.
8. When implementing, for each control you add beside existing ones, the
   report gives the control it is written like and the resulting height,
   read from the code as it now stands, for example `rewind button: like the
   play button beside it, size lg, 48 high`; controls written alike share
   one line. Where the code differs from that control, the line says how.

Before accepting a change, and in a code review of interface source, read the
diff once for Code quality's questions, step 7's values, custom styling or
compensation whose cause is gone, and preserved state, event and
render-function behavior. Where Validation was selected, its results also
decide acceptance; report source defects before rendered findings. For Audit,
return prioritized findings tied to observed evidence.

## Integrity floor

Appearance never justifies a parallel visual system, bypassed semantic tokens,
a rebuilt accessible component, removed focus or input support, hidden required
content, or meaning carried by a single visual cue, because each trades
something users or the design system rely on for looks. Preserve recovery after
state changes, and keep a local exception local instead of a global theme
override.

Quantitative rules come from the applicable accessibility standard, platform
or design system, so do not impose preferred fonts, palettes, radii, shadows,
card patterns, breakpoints, pixel values or fashionable bans. For a
demonstrated WordPress owner gap, the adapter's explicitly labeled Skill-Norm
composition may supply a local fallback; it is not an official Core rule and
not a reason to normalize working native spacing.
