---
name: scoville-ui
description: "Implement or audit interfaces through their framework and design system. Use for information structure, layout, interface wording, components, states, interactions, responsiveness, accessibility and rendered checks. The WordPress adapter covers plugin-owned wp-admin pages, including hypothetical implementation advice; pure visual concepts keep their design scope. Excludes non-UI backend work and prose unrelated to interface text."
compatibility: "Agent Skills host with reference access and the project's framework tools. Geometry proof needs DOM or equivalent measurement; visual proof needs viewed renders; interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No mandatory network. Developed for Codex and Claude Code; other hosts untested. Python 3.11+ for the bundled text-size checker; manual fallback only without suitable Python. Helper errors do not enable fallback."
---

# Scoville UI

Implement and verify UI through its established framework, platform and design
system. Do not silently redesign a settled concern. Here, owner means the
source responsible for a decision or behavior, such as a product requirement for intent,
a design system for visual rules, or a framework or component for implementation.

When writing instructions, reviews or reports, read and apply the
[shared writing rules](references/writing.md). Approved interface text retains
its product contract.

## Gates and owners

{{ include: rules.optout }}

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

Lower sources never override higher authorities. Report material conflicts.

- **LOCAL:** Reuse a repeated pattern only if it is deliberate, current and right for
  the same surface.
- **UNKNOWN EXCEPTION:** If the source responsible for an exception is unclear,
  inspect or ask. Normalize it only with evidence that it is accidental or stale.
- **GREENFIELD:** If no applicable source defines the visual direction,
  use this Skill's bounded local direction. Framework defaults remain primitives.
- **ACCESSIBILITY:** If no target is given, use WCAG 2.2 AA on the web and current
  platform guidance elsewhere. Always use supported components and APIs.
- **OWNER LIMIT:** Name the responsible canonical component or system and its
  limitation; do not introduce a second visual system to bypass that owner.
  Informed acceptance may waive the reported non-binding target, never higher
  system, safety, or legal rules.

## Skill coordination

{{ include: family.contract }}

{{ include: family.neighbors }}

UI owns framework-valid implementation, component semantics and states,
focus and input behavior, responsive mechanics, and rendered and interaction proof.
UI owns new interface wording and terminology consistency within the task,
including greenfield work. Preserve supplied approved wording and settled
product decisions; honor requested text changes without another Skill.
Verify text presentation, labels, and accessibility-name associations.
Ordinary task flow and information structure also belong to UI.

## Mode and scope

Use **Implement** for requested creation, changes or fixes and **Audit** for
inspection, explanation or evaluation. Audit remains read-only. Design-only
work does not authorize code changes. Neither mode authorizes publication.
Select the requested page or region and concerns. A local fix does not become
a redesign or a whole-product audit.

## Select the platform route

| Surface or request | Route and boundary |
| --- | --- |
| Any `wp-admin` concern, including classification and hypothetical advice | First read [routing](references/wordpress/routing.md). For supported plugin-owned pages, also read [adapter](references/wordpress/adapter.md) before dependent advice or work. |
| Excluded host-owned admin surface | Name host owner and stop the plugin-page route; no general-route fallback. |
| Unknown admin ownership | Inspect accessible source first, then ask for the remaining decision-relevant fact. |
| Themes, site frontends, plugin frontend output, non-WordPress surfaces | General route; no admin references. |
| Pure visual concept | Preserve design scope; no WordPress implementation or acceptance rules. |

Classify admin surface, runtime per DOM region and supported versions separately;
React does not imply WPDS.

Both routes use the same Quality and Validation contracts below. WordPress adds
its local platform rules when their triggers apply, including
[validation additions](references/wordpress/validation.md) when Validation is
selected. Reuse one inventory and one evidence pass.

## Workflow

1. Inspect as needed: surface, repository rules, framework version, canonical
   owners, nearest comparable surface.
2. Identify implementation concerns: affected components and states, content
   variation, inputs, breakpoints and adaptation mechanisms, semantics, and proof.
3. Reuse canonical components, tokens, variants, layouts, breakpoints, and
   interactions. Add a primitive only for a demonstrated owner gap.
4. Make the smallest framework-valid change. If a real implementation constraint
   conflicts with a canonical product decision, report the exact component
   constraint to the product or visual decision owner. Implement the revised
   decision after that owner resolves the conflict. Do not silently redesign.
5. Batch related changes, then use the selected Validation contract for
   affected source, measurement, viewed render, and interaction checks. Audit
   reports source defects first and remains read-only. A build or source check
   does not prove rendering; a viewed image does not prove interaction, and
   geometry needs runtime measurement. State missing evidence precisely.

## Reference router

Use matching rows only. Ownership-only questions use the first row instead of
the other triggers; add their normal routes only when the question also concerns
quality, implementation or evidence.

| Concern | Reference and trigger |
| --- | --- |
| Hypothetical support status and responsible systems only | [Framework](references/framework-alignment.md) only if responsibility or fallback remains unresolved. For WordPress admin, use the adapter classification instead. No Quality or Validation unless the question extends to those concerns. |
| General-route implementation owner | Before choosing an owner, read Framework when the stack is unfamiliar, ownership is ambiguous, layers interact, no canonical visual owner exists, customization is uncertain or a component limitation prevents the target. |
| Open quality or implementation question | [Quality](references/ui-quality.md) when creating, translating, changing or reviewing interface text; judging unsettled flow, hierarchy, layout, readability, states, accessibility structure or responsive behavior; or mechanics could violate settled intent. |
| Interface change, consistency audit or judgment of existing proof | Before an interface change, a consistency audit or judging existing proof, read [Validation](references/validation.md) for rendering, responsive behavior, interaction, visual quality or accessibility. Build and source checks do not prove rendering. |
| UI decision fixed; proof only | Validation. Add Quality only for an open quality, state, accessibility-structure or mechanism question; Framework only for unresolved ownership or implementation path. Reuse existing proof; repeat no check without a concrete gap. |
| Source-structure audit or unimplemented design direction | Framework and Quality keep their normal triggers. Omit Validation; report rendered and interactive behavior as unverified. |
| Page consistency | Audit with consistency focus; Quality and Validation with its coverage contract. Framework keeps its normal triggers. |

Merely stating that source-only or unimplemented work leaves rendering,
interaction and accessibility unverified needs no Validation read. WordPress
exclusions still apply.

For page consistency, build and reconcile an inventory through source, measurement and sight results,
including lower scroll regions and relevant same-page variants. Follow
Validation's coverage contract. Missing entries and partial samples prevent an
unqualified whole-page pass. Audit alone never authorizes repairs.

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

For an audit or advice only: return prioritized findings tied to observed evidence; make
no edits.

{{ include: rules.python }}

{{ include: helper.policy }}
