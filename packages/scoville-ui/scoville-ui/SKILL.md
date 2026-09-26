---
name: scoville-ui
description: "Implement or audit UI through its framework and design system. Use for information structure, components, states, interaction, responsiveness, accessibility mechanics and rendered proof. The WordPress adapter applies only to plugin-owned wp-admin backend pages: settings, tools, workflows, dashboards, data views and explicit Network Admin. It excludes editor canvases, SlotFills, metaboxes, Dashboard widgets, profile fields, Core-screen extensions and UI owned by another plugin. Themes, site frontends and frontend UI produced by plugins use the general route. Excludes non-UI backend work and prose-only tasks."
compatibility: "Agent Skills host with reference access and the project's framework toolchain. Geometry proof needs DOM or equivalent platform measurement; visual proof needs actually viewed renders, and interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No bundled scripts or mandatory network access. Developed for Codex and Claude Code; other hosts untested."
---

# Scoville UI

Implement and verify UI through its canonical framework, platform, and design
system. Do not silently redesign a settled concern.

## Gates and owners

**OPT-OUT:** If the user explicitly excludes this Skill, STOP before references,
Skill tools, changes, or Skill-derived completion claims. If higher-authority
host/project rules require it, report exact conflict.

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

All Skills included in this suite must be installed and enabled. Use the
applicable owner without checking sibling availability. Load only instructions
needed for the task. Explicit invocation gates and user exclusions still apply.





UI owns framework-valid implementation, component semantics and states,
focus/input behavior, responsive mechanics, and rendered/interaction proof.
UI preserves supplied wording and verifies its presentation, labels, and
accessibility-name associations. Ordinary task flow and information structure
belong to UI. Honor requested wording changes without requiring another Skill;
otherwise preserve protected text and settled product decisions.

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

For a plugin backend request, including hypothetical implementation advice, read
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
5. Batch related UI changes before validation. Inspect generating code and CSS
   to guide implementation, then complete the planned edits before running
   affected source checks, measuring actual geometry and viewing the result.
   Do not measure or capture screenshots after every small edit. If validation
   reveals defects, batch the corrections and recheck affected concerns once
   that correction batch is complete. Audit reports source defects first and
   continues read-only.
   Preserve authored units/expressions separately from computed pixels.
   Justify custom styling before writing it against a concrete owner gap.
   Verify only relevant rendered conditions that could disprove the specific
   layout or behavior claim. Report rendered, source,
   and unverified evidence separately. Mark unimplemented or source-only work
   unrendered and rendered behavior unverified; never load Validation merely to
   state this boundary. Rendered proof requires a browser, renderer, or screenshot output that the
   agent can actually view. Interaction proof additionally requires an
   interactive runtime in which the behavior can be exercised. Geometry claims
   require DOM or equivalent platform measurement. Report each missing kind of
   evidence as unverified. Build, source, or an unviewed screenshot file never
   substitutes for a viewed render; a screenshot alone never proves interaction.

## Reference router

**OWNERSHIP-ONLY:** For a routing-only hypothetical asking only for status and
owners, load Framework when ownership or fallback is unresolved. Omit Quality
and Validation unless also judging UI/design quality, implementation mechanics,
or proof. Greenfield or polished intent alone does not broaden this route.
For WordPress admin, the adapter's surface/runtime classification replaces
the general Framework route. These narrow routes do not bypass its exclusions.

- **Framework (general route):** Load
  [framework-alignment.md](references/framework-alignment.md) before choosing an
  owner if stack unfamiliar, ownership ambiguous, UI layers interact, no
  canonical visual owner exists, customization path is uncertain, or a
  component limitation prevents the requested target.
- **Quality:** Load [ui-quality.md](references/ui-quality.md) before judging task
  flow, hierarchy, layout, readability, states, accessibility structure, or
  responsive behavior not settled by a canonical product decision, or
  when implementation mechanics could violate the settled intent.
- **Validation:** Load [validation.md](references/validation.md) before an
  interface change, a consistency audit, or claims of rendered/responsive behavior, observed
  interaction, visual quality, or accessibility. Build/source cannot prove
  rendering.

**EVIDENCE-ONLY:** The UI decision is fixed and the task only evaluates existing
proof. Judging what existing source or build evidence establishes uses
Validation. Merely stating that unimplemented or source-only work leaves
rendering, interaction and accessibility unverified does not. Add Quality only when the current task also judges
an open quality, state, accessibility-structure or mechanism question. Add
Framework only when ownership or the implementation path remains unresolved.
The narrower OWNERSHIP-ONLY case above still applies to a hypothetical asking
only for status and owners.

**SOURCE-ONLY AUDIT:** If structure-only, omit Validation; explicitly mark
rendered/interactive behavior unverified. This exception removes only
Validation. The Framework and Quality conditions still apply: load Framework
for unresolved ownership or implementation paths. Load Quality only when the
audit also judges one of the concerns listed in its row above. For unimplemented direction,
omit Validation only to report the same unrendered boundary.

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
