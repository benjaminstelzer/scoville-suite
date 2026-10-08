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

Reuse an already verified interpreter meeting this Skill's Python 3.11+
requirement. Otherwise check `py -3`
on Windows or `python3` elsewhere; try `python` if needed. Choose it locally,
without asking the user. Verify its version before the first helper operation.
Use that executable wherever examples say `python` or `<verified-python>`,
including Python commands after `--run --`.
Report a missing runtime only when no suitable installed interpreter is found.

## Runtime helpers

Use the bundled helpers for their operations. Read their invocation instructions,
not their source, unless diagnosing a failure.

Without an applicable limit, read complete UTF-8 directly; invent no budget.
With an applicable limit:

1. Use the smallest declared or explicitly selected limit for the read and
   enclosing output. Read separately unless the complete combined output,
   including labels and metadata, is measured and fits; combined reads share
   that budget.
2. If the file may exceed that limit, use the verified Python interpreter and
   bundled reader:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<document>" --max-output-tokens <limit> --part 1`.
   It validates the complete UTF-8 file and budgets labels too.
3. For multipart output, follow `part=N bytes=start:end/total next=M` with
   `--part M` through `last`,
   where end equals total. Read every unchanged part in order before dependent
   work. Keep the budget unchanged; otherwise restart at part 1.

A reader error leaves the read incomplete, even if its diagnostic cannot fit.
Do not alter or copy the input, truncate it or recover omitted text after an
oversized read.

The reader program is `scripts/check_text_size.py`; pass its document only as
`--file`. Only named `.py` files may be Python program files. SKILL.md, references
and assignments are documents, never programs.
Without suitable Python 3.11+, first read only the check_text_size reference below. Use
a native UTF-8 reader and ordered unchanged parts, measuring each complete
output including labels before display against `floor(limit * 4 / 5)` bytes.
With no limit, read it completely. Without a safe reader, stop dependent work.

| Condition | Required route |
| --- | --- |
| Suitable Python 3.11+ is available | Use the bundled helper; do not load manual references. |
| No suitable Python 3.11+ | Read only the matching optional reference below. |
| Missing script, missing dependency or helper error | Stop the affected operation; this never enables the manual route. |

| Helper | Optional no-Python reference |
| --- | --- |
| `scripts/check_text_size.py` | [check_text_size](references/fallbacks/check_text_size-fallback.md) |
