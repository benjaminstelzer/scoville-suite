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

WordPress admin route: for any request about a `wp-admin` surface, including
classification and hypothetical implementation advice, first read the
[routing contract](references/wordpress/routing.md). For a supported plugin-owned
page, also read [the WordPress adapter](references/wordpress/adapter.md) before
dependent advice or work. Classify surface, runtime per DOM region and supported
versions separately; React does not imply WPDS. For an excluded host-owned
surface, name its host owner and stop the plugin-page route; do not fall back to
the general route. Resolve unknown ownership from accessible source first, then
ask for the remaining decision-relevant fact.

General route: themes, site frontends, plugin frontend output and non-WordPress
surfaces; do not load admin references for them. Pure visual concepts keep their
design scope without WordPress implementation or acceptance rules.

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

**OWNERSHIP-ONLY:** For a hypothetical question limited to support status and
responsible systems, read Framework only if responsibility or fallback remains
unresolved. Do not load Quality or Validation unless the question also concerns
quality, implementation or evidence. For WordPress admin, use the adapter's
classification instead of general Framework. Its exclusions still apply.

- **Framework (general route):** Load
  [framework-alignment.md](references/framework-alignment.md) before choosing an
  owner when any of these conditions applies:
  - The stack is unfamiliar.
  - Ownership is ambiguous or UI layers interact.
  - No canonical visual owner exists.
  - The customization path is uncertain.
  - A component limitation prevents the requested target.
- **Quality:** Load [ui-quality.md](references/ui-quality.md) when creating,
  translating, changing or reviewing interface text, or before judging task
  flow, hierarchy, layout, readability, states, accessibility structure, or
  responsive behavior not settled by a canonical product decision, or
  when implementation mechanics could violate the settled intent.
- **Validation:** Load [validation.md](references/validation.md) before an
  interface change, a consistency audit, or evaluating existing proof of
  rendering, responsive behavior, interaction, visual quality, or
  accessibility. Build or source inspection cannot prove rendering.

**EVIDENCE-ONLY:** When the UI decision is fixed, use Validation to judge what
existing proof establishes. An existing result or test report can supply that
proof; do not repeat checks without a concrete gap. Merely stating that
unimplemented or source-only work leaves rendering, interaction and
accessibility unverified needs no Validation read. Add Quality for an open
quality, state, accessibility-structure or mechanism question; add Framework
for unresolved ownership or implementation path.

**SOURCE-ONLY AUDIT:** When the audit concerns only source structure, omit
Validation and explicitly report rendered and interactive behavior as unverified.
Framework and Quality retain their normal triggers. Apply the same evidence
limit to an unimplemented design direction.

For a page-consistency request, use Audit with a consistency focus and load
Quality and Validation. Load Framework only under its existing conditions.
Build and reconcile an inventory through source, measurement and sight results,
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
