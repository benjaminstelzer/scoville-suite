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

When writing instructions, reviews or reports, or assessing a disputed factual
or technical conclusion, read and apply the
[shared writing rules](references/writing.md). Approved interface text retains
its product contract.

## Gates and owners

If the user explicitly excludes this Skill, do not apply it: read no Skill
references, use no Skill-directed tools, and make no Skill-derived changes or
claims. Continue other authorized work under its responsible instructions.
If higher-authority instructions require this Skill, report the exact conflict.

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

All Skills included in this suite must be installed and enabled. Use the
applicable owner without checking sibling availability. Load only instructions
needed for the task. Explicit invocation gates and user exclusions still apply.

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
| Themes, site frontends, plugin frontend output, non-WordPress surfaces | General route; no admin references. |
| Pure visual concept | Preserve design scope; no WordPress implementation or acceptance rules. |

The WordPress router owns classification and exclusions; unknown ownership
blocks dependent advice and excluded surfaces have no general-route fallback.

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
5. Batch related changes, then validate under the selected Validation contract.
   Audit reports source defects first and stays read-only. State missing evidence precisely.

## Reference router

Use matching rows only. Ownership-only questions use the first row instead of
the other triggers; add their normal routes only when the question also concerns
quality, implementation or evidence.

| Concern | Reference and trigger |
| --- | --- |
| Hypothetical support status and responsible systems only | [Framework](references/framework-alignment.md) only if responsibility or fallback remains unresolved. For WordPress admin, use the adapter classification instead. No Quality or Validation unless the question extends to those concerns. |
| General-route implementation owner | Before choosing an owner, read Framework when the stack is unfamiliar, ownership is ambiguous, layers interact, no canonical visual owner exists, customization is uncertain or a component limitation prevents the target. |
| Open quality or implementation question | [Quality](references/ui-quality.md) when creating, translating, changing or reviewing interface text; judging unsettled flow, hierarchy, layout, readability, states, accessibility structure or responsive behavior; or mechanics could violate settled intent. |
| Interface change, consistency audit or judgment of existing proof | Before an interface change, a consistency audit or judging existing proof, read [Validation](references/validation.md) for rendering, responsive behavior, interaction, visual quality or accessibility. |
| UI decision fixed; proof only | Validation. Add Quality only for an open quality, state, accessibility-structure or mechanism question; Framework only for unresolved ownership or implementation path. Reuse existing proof; repeat no check without a concrete gap. |
| Source-structure audit or unimplemented design direction | Framework and Quality keep their normal triggers. Omit Validation; report rendered and interactive behavior as unverified. |
| Page consistency | Audit with consistency focus; Quality and Validation with its coverage contract. Framework keeps its normal triggers. |

Whenever Validation applies, read [Geometry and sight](references/ui-geometry-validation.md)
before measuring geometry or judging optical alignment.

Merely stating that source-only or unimplemented work leaves rendering,
interaction and accessibility unverified needs no Validation read. WordPress
exclusions still apply.

For page consistency, read Validation's coverage contract before a whole-page
claim; a partial sample cannot establish it. Audit never authorizes repairs.

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

Reuse an already verified interpreter meeting this Skill's Python 3.11+
requirement. Otherwise check `py -3`
on Windows or `python3` elsewhere; try `python` if needed. Choose it locally,
without asking the user. Verify its version before the first helper operation.
Use that executable wherever examples say `python` or `<verified-python>`,
including Python commands after `--run --`.
Report a missing runtime only when no suitable installed interpreter is found.

Before processing machine reports or logs, use the [shared writing rules](references/writing.md).
If their complete text is not loaded, read it in a separate call before reading
the data. Reuse retained rules under their existing reload conditions.
Before helper calls, follow [shell command rules](references/shell-commands.md).

## Runtime helpers

Use the bundled helpers for their operations. Read their invocation instructions,
not their source, unless diagnosing a failure.

| Condition | Required route |
| --- | --- |
| Suitable Python 3.11+ is available | Use the bundled helper; do not load manual references. |
| No suitable Python 3.11+ | Read only the matching optional reference below. |
| Missing script, missing dependency or helper error | Stop the affected operation; this never enables the manual route. |

| Helper | Optional no-Python reference |
| --- | --- |
| `scripts/check_text_size.py` | [check_text_size](references/fallbacks/check_text_size-fallback.md) |
