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

If the user explicitly excludes this Skill, leave it out entirely: its
references, its tools and any change or claim derived from it. Continue the
other authorized work. If a higher-authority rule requires this Skill, report
that conflict.

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
applicable owner without checking sibling availability, and load only the
instructions the task needs.
A Skill that needs explicit activation stays out until it is activated, and
one the user excluded stays out.

UI owns task flow, information structure, new interface wording and
terminology, framework-valid implementation, semantics, states, focus and
input, responsive mechanics and their proof. Preserve approved wording, which
keeps its product contract, make requested text changes yourself, and verify
presentation and accessible-name associations.

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
| Any `wp-admin` concern, including hypothetical advice or classification | [WordPress routing](references/wordpress/routing.md) first; supported plugin-owned pages also [adapter](references/wordpress/adapter.md). Unknown ownership holds the advice that depends on it, and an excluded surface is not handled through the general route instead. |
| Themes, frontend output, non-WordPress surfaces, pure visual concepts | General route without admin references; a visual concept keeps its design scope. |
| General-route ownership or implementation path unresolved | [Framework](references/framework-alignment.md) before choosing an owner: unfamiliar stack, interacting layers, uncertain customization, no visual owner, or a component limit in the way. |
| Creating, changing, auditing or reviewing an interface | Before the first edit or finding, read [Quality](references/ui-quality.md) and the topic file of each touched concern: [Wording](references/ui-wording.md) for interface text, [Layout](references/ui-layout.md) for grouping, spacing, sizes, alignment and responsive adaptation, [Interactions](references/ui-interactions.md) for controls, focus, input, feedback and states. The trigger is the kind of task, not whether a question looks open. The spacing, size and alignment rules themselves are in this file. |
| A requested review or audit of how an interface or an interface change looks and behaves, a requested rendered check or proof, a judgment of existing proof, or a visual defect the source does not explain | Read [Validation](references/validation.md) first, for rendering, responsive behavior, interaction, visual quality or accessibility. Add [Geometry and sight](references/ui-geometry-validation.md) when spacing, sizes, alignment, paint or optical balance are measured or judged, and [Audit coverage](references/ui-consistency-audit.md) for page consistency. Reuse existing proof and repeat a check only for a concrete gap. Implementing a change by itself calls for no rendered measurement of layout: the spacing, size and alignment rules apply while the code is written, inspecting your own final diff is part of implementing, and the report names what was not rendered as unverified. Exercising a changed interaction follows Interactions, and a platform reference that names a rendered check for the change keeps it. A review measures; a source-only audit follows the next row. |
| Source-structure audit or unimplemented design direction | Framework and Quality by their triggers, without Validation; report rendering, interaction and accessibility as unverified. Stating those gaps needs no Validation read. |
| Choosing or implementing UI code; reviewing interface source, including your final diff | Read [Code quality](references/code-quality.md) before choosing the implementation and before acceptance, within the framework's guarantees. |

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
requested structured report.

## Shared references

Read one when its condition holds. A complete copy already in context from
this build, including one embedded in your assignment, counts as read; read it
again when it is incomplete or uncertain or a reload is requested.

- [Writing](references/writing.md): a plan, decision, instruction, review, handoff or report; a disputed conclusion.
- [Machine data](references/machine-data.md): a test report, log or structured state as a result.
- [Shell commands](references/shell-commands.md): composed text or scripts passed through a shell; quoting, PowerShell encoding, exact bytes or several exit statuses matter.
- [Output delivery](references/output-delivery.md): before a command whose output may exceed the display limit or whose effect or result cannot be repeated; text that must fit a known limit; delivery as a file.
- [Python discovery](references/python-discovery.md): a Python command or bundled helper, no interpreter verified this session.
- [Instruction design](references/instruction-design.md): a reusable instruction, Skill rule or prompt template.

## Implementation and acceptance

Start every implementation, audit and review by reading the references the
table assigns to it, before the first edit or finding; they hold the criteria
that findings and choices are judged by.

Inspect the scoped surface, framework version, owners and comparable patterns.
Identify the affected content, states, inputs, adaptation and semantics;
settled design still requires correct mechanics. Batch related changes.

Where the project's own code, the design system or the framework already
provides a component, class, variant or token for the kind of element you
need, use it, so the product keeps one button, one field and one badge; a
hand-written copy of something that exists is a defect. Fit it to its place
through its size variant or a local size. Write a new primitive when nothing
existing covers the need.

## Spacing, size and alignment

The aim is a change that looks as if it had always been part of the page;
most visible defects are small mismatches with what is already there. For each
element you add or change, work from the outside in:

1. Outer size first. Before writing a control or row, find the existing ones
   it has to match, nearest first: the same row or bar, then neighbouring
   regions of the same level, then others of its kind on the rest of the
   page. Write one line per new control naming the one it copies and the
   resulting size, for example `sort select: like the filter buttons, size
   sm, 32 high`, and give the new one that height, radius, font size and
   padding through the same component, variant, class or token; a new row
   takes the padding of the rows around it, equal above and below its
   content unless those rows differ. Leaving a component's size unset picks
   its default, which is right only where the neighbours use the default. A field 40 high beside fields and selects
   that are 36 high is a defect.
2. Then fit it in. Whatever goes into an existing control, row or bar takes
   the size variant that fits its current height and leaves equal space
   above, below and at the outer edge: a 24 button in a 36 field, small
   controls in a heading whose neighbouring headings use small ones. Where no
   variant fits, set a local size on the new part; that is a styling
   exception, so name the need no variant meets and keep it on that element.
   The container keeps its height.
3. Name what each edge and centre lines up with, such as the neighbouring
   control's centre line or the container's content edge, and derive the
   offset from the actual paddings and borders in between.
4. Count every source of space between two elements once: parent gap, own
   margin, sibling margin, wrapper padding and legacy element rules. Two
   sources for one gap is the usual cause of doubled or uneven spacing.
5. Keep inner insets of one control equal on both sides. Rows and controls
   the request does not ask to resize keep their size, and an element that
   appears only in some states does not move its neighbours when it appears.
6. Settle these relationships from the source while you write the code: the
   equivalent's component, class and stylesheet values are the evidence.
   Rendering and measuring follow the References table: a review, an audit
   or a requested check, not every change.
7. Check the values themselves, when finishing a change and in every review:
   list each literal and each component size variant the change adds for
   height, font size, radius, padding and gap, and search the project's
   tokens and existing rules for the same value on the same kind of element.
   A value found nowhere else, such as a 13px font where the page uses 12px
   and 14px, is a defect unless the request asks for it or it is the local
   size from step 2.

Before accepting UI construction, updates or an interface-source review,
inspect the final scoped diff under Code quality, including rendering and
refresh helpers, and preserve state, event and rendering semantics. Where
Validation was selected, apply its evidence; report source defects first and
name specific gaps. A partial sample cannot establish a whole-page consistency pass. For
Audit, return prioritized findings tied to observed evidence.

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
