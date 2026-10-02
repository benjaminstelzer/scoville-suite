---
name: scoville-ui
description: "Implement or audit UI through its framework and design system. Use for information structure, UI wording and terminology, components, states, interaction, responsiveness, accessibility mechanics and rendered proof. The WordPress adapter applies to implementation or audit of plugin-owned wp-admin backend pages, including hypothetical implementation advice, not pure visual concepts for a future page. Supported pages include settings, tools, workflows, dashboards, data views and explicit Network Admin. It excludes editor canvases, SlotFills, metaboxes, Dashboard widgets, profile fields, Core-screen extensions and UI owned by another plugin. Themes, site frontends and frontend UI produced by plugins use the general route. Excludes non-UI backend work and prose unrelated to interface text."
compatibility: "Agent Skills host with reference access and the project's framework toolchain. Geometry proof needs DOM or equivalent platform measurement; visual proof needs actually viewed renders, and interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No bundled scripts or mandatory network access. Developed for Codex and Claude Code; other hosts untested."
---

# Scoville UI

Implement and verify UI through its canonical framework, platform, and design
system. Do not silently redesign a settled concern.

## Gates and owners

**OPT-OUT:** If the user explicitly excludes this Skill, stop applying it before
loading its references or making Skill-derived claims. Continue other authorized
work under its own owner. If higher-authority host/project rules require this
Skill, report the exact conflict.

Apply the highest owner per concern:

1. system, safety, legally binding accessibility;
2. explicit user request, including informed acceptance of a reported
   limitation against a non-binding target;
3. repository instructions;
4. canonical product requirements, design-system components, wrappers, themes,
   semantic tokens, approved assets;
5. owning framework/platform for unresolved concerns;
6. deliberate owner-aligned local patterns;
7. this Skill's standalone principles for the remaining gap.

Lower sources never override higher owners; report material conflicts.

- **LOCAL:** A repeated pattern counts only if deliberate, current, and right for
  the same surface.
- **UNKNOWN EXCEPTION:** Ownership is unresolved. Inspect or ask; normalize only
  with evidence it is accidental or stale.
- **GREENFIELD:** If no visual owner exists, use this Skill's bounded local
  direction; framework defaults remain primitives.
- **ACCESSIBILITY:** No target: web uses WCAG 2.2 AA; elsewhere use current
  platform guidance; always use supported components and APIs.
- **OWNER LIMIT:** Name the responsible canonical component or system and its
  limitation; do not introduce a second visual system to bypass that owner.
  Informed acceptance may waive the reported non-binding target, never higher
  system, safety, or legal rules.

## Skill coordination

{{ include: family.contract }}

{{ include: family.neighbors }}

UI owns framework-valid implementation, component semantics and states,
focus/input behavior, responsive mechanics, and rendered/interaction proof.
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

For WordPress admin classification, read the routing contract below, including
when the result may be an excluded host-owned surface. Its implementation and
audit rules apply only to supported plugin-owned backend pages in `wp-admin`.
Themes, site frontends and frontend output from plugins use the general UI
route. Excluded host-owned admin surfaces retain their host's contract.

For pure visual concepts for a future page, keep the requested design scope
without activating the WordPress implementation or acceptance rules.
For a plugin backend implementation or audit request, including hypothetical implementation advice, read
[the WordPress adapter](references/wordpress/adapter.md) and its required
[routing contract](references/wordpress/routing.md) before dependent advice or
implementation. Classify the surface, actual runtime per DOM region and supported
versions separately. React does not imply WPDS. Unsupported host-owned surfaces
stay with their host owner; do not apply the plugin-page shell or silently fall
back to the general route. Unknown ownership requires source inspection or the
remaining decision-relevant fact.

For other surfaces, follow the general Framework route below. WordPress site
frontends and themes follow their own framework and product contract. Do not
load admin references for them or for unrelated frameworks.

Both routes use the same Quality and Validation contracts below. WordPress adds
its local platform rules when their triggers apply, including
[validation additions](references/wordpress/validation.md) when Validation is
selected. Reuse one inventory and one evidence pass.

## Workflow

1. Inspect as needed: surface, repository rules, framework version, canonical
   owners, nearest comparable surface.
2. Identify implementation concerns: affected components and states, content
   variation, inputs, breakpoints/adaptation mechanisms, semantics, and proof.
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

**OWNERSHIP-ONLY:** A hypothetical asking only for status and owners loads
Framework when ownership or fallback is unresolved; it does not load Quality
or Validation without a quality, implementation, or evidence question. For
WordPress admin, the adapter's classification replaces general Framework.
Its exclusions still apply.

- **Framework (general route):** Load
  [framework-alignment.md](references/framework-alignment.md) before choosing an
  owner if stack unfamiliar, ownership ambiguous, UI layers interact, no
  canonical visual owner exists, customization path is uncertain, or a
  component limitation prevents the requested target.
- **Quality:** Load [ui-quality.md](references/ui-quality.md) when creating,
  translating, changing or reviewing interface text, or before judging task
  flow, hierarchy, layout, readability, states, accessibility structure, or
  responsive behavior not settled by a canonical product decision, or
  when implementation mechanics could violate the settled intent.
- **Validation:** Load [validation.md](references/validation.md) before an
  interface change, a consistency audit, or evaluating existing proof of
  rendering, responsive behavior, interaction, visual quality, or
  accessibility. Build/source cannot prove rendering.

**EVIDENCE-ONLY:** When the UI decision is fixed, use Validation to judge what
existing proof establishes. An existing result or test report can supply that
proof; do not repeat checks without a concrete gap. Merely stating that
unimplemented or source-only work leaves rendering, interaction and
accessibility unverified needs no Validation read. Add Quality for an open
quality, state, accessibility-structure or mechanism question; add Framework
for unresolved ownership or implementation path.

**SOURCE-ONLY AUDIT:** If structure-only, omit Validation; explicitly mark
rendered/interactive behavior unverified. Framework and Quality retain their
normal triggers. Unimplemented direction uses the same evidence boundary.

For a page-consistency request, use Audit with a consistency focus and load
Quality and Validation. Load Framework only under its existing conditions.
Build and reconcile an inventory through source, measurement and sight results,
including lower scroll regions and relevant same-page variants. Follow
Validation's coverage contract. Missing entries and partial samples prevent an
unqualified whole-page pass. Audit alone never authorizes repairs.

## Integrity floor

Never improve appearance through: parallel visual language; semantic-token
bypass; accessible-component rebuild; removed focus/input accommodation; hidden
required content; meaning carried solely by one visual cue; missing changed-state
recovery; local exception applied through a global theme override.

Never impose preferred fonts, palettes, radii, shadows, card patterns,
breakpoints, pixel values, or fashionable bans. Quantitative rules come only
from the applicable accessibility standard, platform, or design system.
For a demonstrated WordPress owner gap, the adapter's explicitly labeled
Skill-Norm composition may supply a local fallback. It is never an official
Core rule or a reason to normalize working native spacing.

Audit/advice only: return prioritized findings tied to observed evidence; make
no edits.
