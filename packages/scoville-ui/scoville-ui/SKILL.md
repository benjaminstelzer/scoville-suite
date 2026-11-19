---
name: scoville-ui
description: "Implement or audit interfaces through their framework and design system. Use for information structure, layout, interface wording, components, states, interactions, responsiveness, accessibility and rendered checks. The WordPress adapter covers plugin-owned wp-admin pages, including hypothetical implementation advice; pure visual concepts keep their design scope. Excludes non-UI backend work and prose unrelated to interface text."
compatibility: "Agent Skills host with reference access and the project's framework tools. Geometry proof needs DOM or equivalent measurement; visual proof needs viewed renders; interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No mandatory network. Developed for Codex and Claude Code. Python 3.11+ for the bundled text-size checker; manual fallback only without suitable Python. Helper errors do not enable fallback."
---

# Scoville UI

Implement and verify UI through its established framework, platform and design
system. An owner is the source responsible for a decision or behavior: product
requirements for intent, a design system for visuals, a component for mechanics.

If the user explicitly excludes this Skill, leave it out: do not read its
references, run its tools or base a change or statement on it. Continue other
authorized work. If a higher-authority rule requires this Skill, report that
conflict.

## Mode and scope

Use **Implement** for requested creation, changes or fixes and **Audit** for
inspection, explanation or evaluation. An audit changes no product file: it
reads, runs only the checks its evidence route below allows, with disposable
output where Scoville Code permits it, and reports. Design-only work produces
a design; code changes and publication each need their own request. Deliver the requested interface behavior through the
components and layouts responsible for it, including shared owners. An
audit covers the requested page, region and concerns.

Choose the evidence route before any execution:

| Request or finding | Authorized interface evidence |
| --- | --- |
| Implement, including a reported problem explained by source | Check the affected source and applicable non-browser tests. |
| Implement to fix a reported visual defect the affected markup, applied styles and component source do not explain | Render to find its cause. Then fix the source and run further rendered checks only as requested. |
| Assigned source review or evaluation of supplied evidence with read-only execution limits | Inspect the source and retained proof within those limits. Report which required observations are missing. |
| Review or audit of appearance or behavior, or a requested rendered check | Inspect the running interface within the requested scope. Observe state without saves, submissions or external effects during an Audit. |
| Interface code review, source audit or unimplemented design | Use source or design evidence. A review of a UI change that does not name appearance, behavior or a rendered check is a code review. For this route do not render, measure or operate the running interface. |

## Owners

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
accident or stale pattern through the component or layout responsible for
the affected group. Without a visual owner, use Framework's bounded
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
product contract. Make requested text changes yourself and keep each
control's visible text in its accessible name.

For interface-only work, use this entry and the project's source and local
test commands. Use the Code workflow for affected backend behavior or a
separate consumed contract. For running-interface evidence, follow Mode and
scope. Report a required guarantee as unverified when its proof is outside
that scope.

## References

For a change to copy or the displayed value in an existing text element
whose role, visibility rules, layout and interaction stay the same, read only
[Wording](references/ui-wording.md). On a `wp-admin` page also read
[internationalization](references/wordpress/internationalization.md) when the
change affects placeholders, plurals, context or escaping. Use the table
below for other interface work.

Read every reference whose trigger matches before the work it governs, and no
others. Establish platform support before advice that depends on it. An
ownership-only question loads Quality or Validation only when it also asks
about those concerns.

| Concern | Reference and trigger |
| --- | --- |
| `wp-admin` work beyond the text-only case above, including hypothetical advice or ownership classification | Read [WordPress routing](references/wordpress/routing.md) first. For a supported plugin-owned page, read the [adapter](references/wordpress/adapter.md) before the first edit or finding and apply its checks to the regions it names. Routing selects the mechanisms for host-owned surfaces and the platform references. Unknown ownership holds only dependent advice. |
| Themes, frontend output, non-WordPress surfaces, pure visual concepts | General route without admin references; a visual concept keeps its design scope. |
| General-route ownership or implementation path unresolved | [Framework](references/framework-alignment.md) before choosing an owner: unfamiliar stack, interacting layers, uncertain customization, no visual owner, or a component limit in the way. |
| New interface, changed task flow, composition or accessibility, or audit of those guarantees | Read the applicable guarantees in [Quality](references/ui-quality.md). Use [Layout](references/ui-layout.md) for grouping, size, spacing or responsive changes and the spacing checks below. |
| Control behavior, focus, input, asynchronous feedback or recovery | Read [Interactions](references/ui-interactions.md) for the affected states. Use Quality when the work also changes its guarantees or their owner is unclear. |
| New, translated, changed or reviewed interface text, including as part of another change | Read [Wording](references/ui-wording.md). |
| Evidence route calls for a runtime observation or evaluates retained rendered evidence | Read [Validation](references/validation.md). Add [Geometry and sight](references/ui-geometry-validation.md) for size or visual judgment and [Audit coverage](references/ui-consistency-audit.md) for page consistency. Reuse proof that covers the current source and conditions. |
| UI code beyond text or formatting, or review of interface source | Use the applicable [Code quality](references/code-quality.md) criteria once. Use the review section for requested code reviews. |

## Shared references

Read one when its condition holds. A complete, unchanged copy in context
counts as read, including one embedded in your assignment. Fetch incomplete
or changed passages, and reload when requested.

- [Writing](references/writing.md): a plan, decision, instruction, review, handoff or a report the user asked for as the result; a disputed conclusion.
- [Machine data](references/machine-data.md): a structured report, log file or saved state you must evaluate, such as JUnit XML or coverage data; a test runner's console summary is not one.
- [Shell commands](references/shell-commands.md): composed text or scripts passed through a shell; quoting, PowerShell encoding, exact bytes or several exit statuses matter.
- [Output delivery](references/output-delivery.md): before a command whose output may exceed the display limit or is needed as evidence and cannot be reproduced; text that must fit a known limit; delivery as a file.
- [Python discovery](references/python-discovery.md): a bundled helper or other Python you run, no interpreter verified this session.
- [Instruction design](references/instruction-design.md): a reusable instruction, Skill rule or prompt template.

## Implementation and acceptance

Check the framework version when an API choice depends on it. Preserve
the affected states, input and semantics even when the design is settled.

For lists and repeated updates, apply rule 1 of
[Code quality](references/code-quality.md).

When moving, removing, reinserting or replacing stateful controls, read the
required live state from its owner immediately before the mutation and keep
or restore it through the component's API. A remembered value is valid only
if all writers update it; programmatic changes need not emit user events.
Keeping the same element object does not preserve its live selection, focus
or editing state automatically. Preserve the required state after partial
updates and failure as well as on full completion.

Where the project's own code, the design system or the framework already
provides a component, class, variant or token that meets the required
semantics, states and behavior, use it, so the product keeps one button, one
field and one badge; a hand-written copy of something that exists is a
defect. Fit it to its place through its size variant or a local size. Write a new primitive when nothing
existing covers the need.

Custom styling, including inline styles and styling props, is an exception:
use it only where supported composition and variants cannot meet a need,
apply it at the component or layout that needs it, and say in the report
which need the responsible component or API does not meet. An official token
alone does not justify it.

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
plugin-owned relationship that Core leaves unspaced, as
[spacing](references/wordpress/spacing.md) defines it, the Skill-Norm
composition in the WordPress spacing references may supply a local fallback;
it is not an official Core rule and not a reason to normalize working native
spacing. Any other literal size or spacing value the change adds needs a
precedent in the page or support in the project's tokens or rules for that
element, unless the request or step 2 below sets it or Framework's local
direction applies where there is no visual owner.

## Spacing, size and alignment

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
   where the neighbours use the default.
2. Then fit it in. Whatever goes into an existing control, row or bar takes
   the size variant that fits the containing layout and leaves equal space
   above and below it. Inside a control, such as a step button in a number
   field, the space at its outer edge matches that space; in a row or bar it
   keeps the content edge the other items keep. Where no variant fits, apply
   the styling-exception rule above at the responsible component or layout.
   Preserve dimensions required by the owning design.
3. Give each edge and centre a definite reference to line up with, such as
   the neighbouring control's centre line or the container's content edge,
   and derive the offset from the actual paddings and borders in between.
4. Count every source of space between two elements once: parent gap, own
   margin, sibling margin, wrapper padding and legacy element rules. Two
   sources for one gap is the usual cause of doubled or uneven spacing.
5. Keep inner insets of one control equal on both sides. An indicator that
   appears only in some states, such as a spinner or badge, does not move its
   neighbours when it appears; content shown for a state, such as an error
   message or an opened disclosure, may push what follows down.
6. Compare the component, size variant and classes with the matched control.
   Where the design calls for the same dimensions across different components,
   choose the variants whose source provides them. Use the containing layout's
   variant and preserve deliberate differences.

## Check and report

Before delivery or in a review of interface source, read the diff once,
together with Code where it applies, and check that it does what this Skill
and the references it selected require; correct what is part of this change.

When a requested check selected Validation, use its results to decide
acceptance too. Report source defects before rendered findings. For Audit,
return findings tied to observed evidence, prioritized by impact.
