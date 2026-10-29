---
name: scoville-ui
description: "Implement or audit interfaces through their framework and design system. Use for information structure, layout, interface wording, components, states, interactions, responsiveness, accessibility and rendered checks. The WordPress adapter covers plugin-owned wp-admin pages, including hypothetical implementation advice; pure visual concepts keep their design scope. Excludes non-UI backend work and prose unrelated to interface text."
compatibility: "Agent Skills host with reference access and the project's framework tools. Geometry proof needs DOM or equivalent measurement; visual proof needs viewed renders; interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No mandatory network. Developed for Codex and Claude Code. Python 3.11+ for the bundled text-size checker; manual fallback only without suitable Python. Helper errors do not enable fallback."
---

# Scoville UI

Implement and verify UI through its established framework, platform and design
system. An owner is the source responsible for a decision or behavior: product
requirements for intent, a design system for visuals, or a component for mechanics.

Before requesting or reading machine reports, logs or structured state, writing
instructions, reviews or reports, or answering a disputed factual or technical
conclusion, read and apply the
[shared writing rules](references/writing.md). Approved interface text retains
its product contract.

## Gates and owners

If the user explicitly excludes this Skill, do not apply it: read none of its
references, use no Skill-directed tools and make no Skill-derived changes or
claims. Continue other authorized work under its responsible instructions.
If higher authority requires this Skill, report the exact conflict.

For each concern, follow the highest applicable authority in this order:

1. system, safety, legally binding accessibility;
2. explicit user request, including informed acceptance of a reported
   limitation against a non-binding target;
3. repository instructions;
4. canonical product requirements, design-system components, wrappers, themes,
   semantic tokens, approved assets;
5. owning framework or platform for unresolved concerns;
6. deliberate owner-aligned local patterns;
7. this Skill's standalone principles for the remaining gap.

Preserve settled decisions. Report material conflicts and the exact owning
component's limitation; obtain the missing owner decision before a dependent
change. Informed acceptance can waive a reported non-binding target, never
system, safety or legal requirements. Use supported components and APIs.

Reuse local patterns when deliberate, current and suitable for this surface.
Inspect unclear exceptions; normalize only an established accident or stale
pattern. Without a visual owner, use Framework's bounded local direction;
framework defaults remain primitives. Without an accessibility target, use
WCAG 2.2 AA on the web and current platform guidance elsewhere.

## Skill coordination

All Skills in this suite must be installed and enabled. Use the applicable
owner without rechecking sibling availability; load only task-needed instructions.
Explicit activation requirements and user exclusions apply in either layout.

UI owns task flow, information structure, new interface wording and terminology,
framework-valid implementation, semantics, states, focus/input, responsive
mechanics and their proof. Preserve approved wording; honor requested text
changes without another Skill. Verify presentation and accessible-name associations.

## Mode and scope

Use **Implement** for requested creation, changes or fixes and **Audit** for
inspection, explanation or evaluation. Audit remains read-only. Design-only
work does not authorize code changes. Neither mode authorizes publication.
Select the requested page or region and concerns. A local fix does not become
a redesign or a whole-product audit.

## Reference router

Load matching routes only. Establish platform support before dependent advice.
An ownership-only question adds quality or proof routes only when it also asks
about those concerns.

| Concern | Reference and trigger |
| --- | --- |
| Any `wp-admin` concern, including hypothetical advice or classification | First read [WordPress routing](references/wordpress/routing.md); supported plugin-owned pages also read [adapter](references/wordpress/adapter.md). Unknown ownership blocks dependent advice; exclusions have no general-route bypass. |
| Themes, site/plugin frontend output, non-WordPress surfaces | General route; no admin references. |
| Pure visual concept | Keep design scope; no WordPress implementation or acceptance rules. Framework and Quality use their normal triggers. |
| General-route ownership or implementation path unresolved | [Framework](references/framework-alignment.md) before choosing an owner when the stack is unfamiliar, layers interact, customization is uncertain, no visual owner exists or a component limit prevents the target. |
| Open quality or implementation question | [Quality](references/ui-quality.md) when creating, translating, changing or reviewing interface text; judging unsettled flow, hierarchy, layout, readability, states, accessibility structure or responsive behavior; or mechanics could violate settled intent. |
| Interface change, consistency audit or judgment of existing proof | Before an interface change, a consistency audit or judging existing proof, read [Validation](references/validation.md) for rendering, responsive behavior, interaction, visual quality or accessibility. |
| UI decision fixed; proof only | Validation. Add Quality only for an open quality, state, accessibility-structure or mechanism question; Framework only for unresolved ownership or implementation path. Reuse existing proof; repeat no check without a concrete gap. |
| Source-structure audit or unimplemented design direction | Framework and Quality keep their normal triggers. Omit Validation; report rendering, interaction and accessibility as unverified. Merely stating these gaps needs no Validation read. |
| Review or audit of interface source code, including your final diff of a UI source change | Read [Code review quality](references/code-review.md) as an acceptance condition. Other rows keep their triggers. |
| Page consistency | Audit with consistency focus; Quality and Validation with its coverage contract. Framework keeps its normal triggers. |

Validation selects evidence by claim, including [Geometry and sight](references/ui-geometry-validation.md)
only for geometry, paint or optical questions. WordPress adds its
[platform validation](references/wordpress/validation.md) within the same pass.
Reuse one compatible inventory and evidence set.

## Implementation and acceptance

Inspect the scoped surface, framework version, owners and comparable patterns.
Identify affected content, states, inputs, adaptation and semantics; settled
design still requires correct mechanics. Reuse canonical components, tokens,
variants, layouts and interactions; add a primitive only for a demonstrated gap.
Choose the simplest sound framework-valid solution at the responsible owner and
batch related changes.

Before accepting UI construction, updates or an interface-source review, inspect
the final scoped diff under [Code review quality](references/code-review.md).
Its relevant paths include rendering and refresh helpers; preserve state,
event and rendering semantics. Apply the selected Validation evidence, report
source defects first and name specific gaps. A partial sample cannot establish
a whole-page consistency pass.

## Integrity floor

Never improve appearance by introducing a parallel visual system, bypassing
semantic tokens, rebuilding an accessible component, removing focus or input
support, hiding required content, or conveying meaning through only one visual
cue. Preserve recovery after state changes. Keep a local exception local rather
than applying it through a global theme override.

Never impose preferred fonts, palettes, radii, shadows, card patterns,
breakpoints, pixel values, or fashionable bans. Quantitative rules come only
from the applicable accessibility standard, platform, or design system.
For a demonstrated WordPress owner gap, the adapter's explicitly labeled
Skill-Norm composition may supply a local fallback. It is never an official
Core rule or a reason to normalize working native spacing.

For Audit, return prioritized findings tied to observed evidence.
