---
name: scoville-wordpress-ui-backend-anti-ai-slop
description: Implement or audit WordPress 7 plugin-owned wp-admin pages with platform components, spacing, vertical flow, responsive behavior, accessibility, and PHP/JavaScript internationalization. Use for plugin settings, tools, workflows, dashboards, data views, and explicit Network Admin pages. This Skill owns UI implementation and UI acceptance for supported plugin-owned wp-admin surfaces; do not also activate scoville-ui-anti-ai-slop for the same surface. Use scoville-design-anti-ai-slop only when visual concept or art direction is independently requested. Excludes site frontends, themes, the editor canvas, SlotFills, metaboxes, Dashboard widgets, profile fields, Core-screen extensions, and UI owned by another plugin.
compatibility: "Agent Skills host with reference access. Implementation needs the plugin's PHP/JavaScript toolchain for WordPress 7. Rendered proof needs running wp-admin, DOM geometry inspection and viewed images; interactions need browser control. Source-only or screenshot-only tasks report evidence limits. Developed for Codex and Claude Code; other hosts untested."
---

# Scoville WordPress UI Backend Anti-AI-Slop

Build plugin administration interfaces that belong in WordPress instead of
placing a second design system inside `wp-admin`.

This Skill is complete on its own. For a supported plugin-owned `wp-admin`
surface it is the specialist owner of UI implementation and UI acceptance.
Scoville UI does not start a second process for that surface. An independently
requested visual concept or art-direction task may belong to Scoville Design;
WordPress implementation and acceptance remain here.

Finding another family Skill does not make it available or applicable. Use each
only for its own concern when active and available. Never require or simulate
an absent sibling. An opt-out applies only to the excluded Skill.

- `scoville-brainstorm`: deliberate divergence before selection.
- `scoville-research`: source-backed research and synthesis.
- `scoville-code-anti-ai-slop`: engineering scope, implementation, risk, and validation.
- `scoville-design-anti-ai-slop`: visual definition, art direction, critique, and repair.
- `scoville-ui-anti-ai-slop`: framework UI implementation, accessibility mechanics, and rendered proof.
- `scoville-wordpress-ui-backend-anti-ai-slop`: WordPress plugin-owned wp-admin implementation and UI acceptance.
- `scoville-scribe-anti-ai-slop`: wording, terminology, meaning, and source fidelity.
- `scoville-plan`: durable Plans, Work Items, Decisions, and lifecycle state.
- `scoville-handoff`: active-work transfer.
- `scoville-workflow-for-codex`: explicit Plan execution through native Codex project tasks.

## Select the working mode and scope

Infer the mode from the requested outcome. The user need not name a mode.

| Mode | Requested outcome | Boundary |
| --- | --- | --- |
| **Implement** | Create, design, change, or fix a plugin backend UI. | Deliver only the requested design or implementation and validate affected behavior. A design-only request does not authorize code edits. |
| **Audit** | Inspect, explain, or evaluate an existing UI or a specific concern. | Inspect and report without modifying plugin code, styles, settings, or data. Findings do not authorize fixes. |

Keep mode separate from scope: name the target page or region and the requested
concerns. A complete UI audit is Audit with a broad scope, not a third mode.
"Check and fix spacing" inspects first and then uses Implement within that
same spacing scope. Neither mode authorizes publication or deployment.

Use one design-system contract in both modes. A focused task selects the work
and evidence needed, not weaker styling or accessibility rules. Do not turn a
small edit or spacing audit into a redesign, translation project, or whole-UI
audit. Include adjacent concerns only when needed to explain a finding or
validate an affected behavior. Report serious incidental issues separately
without silently expanding the work.

## Classify the target surface and runtime

Read [routing.md](references/routing.md) first for focus selection and ownership.
Classify three independent axes for the region in scope:

1. the admin surface and whether the version 1 surface-support table in routing.md supports it;
2. the runtime and component owner for each affected DOM region;
3. the supported WordPress versions and relevant public token/provider APIs.

React does not imply WPDS. A page can be Classic, Core Components, bundled
experimental WPDS, or hybrid. For hybrid pages, classify portals and overlays
at their actual render destination.

If the surface is excluded, name its host owner and do not apply this Skill's
plugin-page shell or spacing rules. Resolve an unknown owner first from supplied
context and accessible source or runtime evidence within the authorized scope.
Ask only for a remaining decision-relevant fact that those sources cannot
establish, before recommending dependent components, tokens, spacing, or CSS.
Continue independent checks without inventing the missing owner.

## Follow the owning WordPress layer

For each region, stop at the first layer that can express the requirement:

1. WordPress API and semantic Core admin markup.
2. Existing Core class or WordPress component with its default CSS.
3. Semantic token actually supplied by the selected runtime.
4. Plugin-owned composition of those primitives.
5. New narrowly scoped plugin CSS for a demonstrated gap only.

Never rebuild a WordPress button, control, Notice, table, shell, color system,
focus treatment, radius, or shadow merely to change its appearance. Never
author CSS that defines, overrides, or imitates `--wpds-*`. A supported public
`ThemeProvider` may generate scoped overrides through its documented API.
Do not load experimental components merely to restyle a Classic or
Core-Components page. WordPress 7.1's Core `wp-theme` stylesheet is a separate,
public capability, also usable for missing layout relationships on PHP pages.

Preserve existing Classic pages. Neither WordPress 7.1 nor token availability
requires a migration to React, WPDS components, or token-based styling. Keep
working native markup, controls, tables, and default spacing. Introduce a token
only for an actual requirement the existing owner cannot express.

## Load only the relevant contract

Apply these triggers within the selected scope. Reading a reference does not
activate every example or checklist it contains. A spacing-only source review
does not become an i18n audit merely because the markup is PHP or JavaScript.

- Before choosing gaps, margins, padding, stacks, cards, fields, portals, or
  custom CSS, read [spacing.md](references/spacing.md).
- For page shells, columns, toolbars, data views, narrow widths, zoom, RTL, or
  content expansion, read [responsive.md](references/responsive.md).
- For navigation, hierarchy, actions, forms, Notices, loading, empty, success,
  error, disabled, permission, or recovery states, read
  [ui-guidance.md](references/ui-guidance.md).
- When creating or changing user-facing strings, accessible text, dates,
  numbers, or translation loading, or auditing i18n-readiness or localized
  layout, read
  [internationalization.md](references/internationalization.md).
- Read [examples.md](references/examples.md) only when a concrete syntax or
  composition question remains after the applicable contracts. Read only the
  matching runtime section. Examples demonstrate ownership and are not
  templates to copy across runtimes.
- Before asserting that a rule is official, updating the WordPress target, or
  changing a token/package contract, read [sources.md](references/sources.md)
  and recheck the relevant source contract when its listed revalidation condition
   applies.
- For `wp-theme`, public `ThemeProvider`, or older-version fallback, read
  [version-compatibility.md](references/version-compatibility.md).

## Required validation order

Before implementation or a rendered/consistency audit, read
[validation.md](references/validation.md). Inspect generating code/CSS first.
For Implement, finish the related edit batch and correct known source defects,
then measure and view the result. After a correction batch, repeat only affected
checks once. Audit reports source defects first and remains read-only.
Justify custom styling against a concrete owner gap before writing it. Keep
authored units/expressions, computed values and actual geometry separate.

For an ordinary page-consistency request, use Audit with a consistency focus.
Inventory the scoped regions and variants and reconcile each with source,
measurement and visual evidence, including below-fold and relevant same-page
states. Unverified required entries or partial samples prevent an unqualified
whole-page pass. Run every affected state, viewport, interaction and regression
check required by this contract, but do not duplicate them through a second
Scoville UI process.

## Preserve the vertical-flow invariant

Within new plugin-owned gap compositions, the direct parent owns spacing
between direct children. Preserve existing native margin-based flow. Children do not add the
same outer margin. Cards own internal padding, while their parent owns the gap
between cards. Hidden or empty children leave no gap slot.

In Core Components, specialized components own their internal rhythm. The
following generic stack recipe is Skill-Norm composition, not Core defaults. A new
generic vertical group uses stable `Flex` with `direction="column"`,
`align="stretch"`, `justify="flex-start"`, `wrap={ false }`,
`expanded={ true }`, and a numeric `gap` equal to the chosen Skill-Norm distance in pixels divided
by four. `Flex` multiplies that numeric value by four pixels; the Skill-Norm
is this Skill's composition rule, not a Core default. This remains the
default when experimental policy is `allow`, `deny`, or `unknown`.

## Keep every UI translatable

All visible and assistive strings use WordPress i18n APIs with one literal text
domain matching the plugin slug. Use complete phrases, positional placeholders,
plural and context APIs, translator comments, and context-aware escaping. Bind
registered JavaScript handles with `wp_set_script_translations()`. Treat text
expansion and locale-formatted values as normal responsive inputs. Require RTL
checks only when a supported or explicitly planned UI language uses RTL. An
LTR-only or unspecified language scope does not require an RTL test merely
because the plugin is i18n-ready. Do not claim untested RTL support.

Require i18n-readiness, not a translation-production workflow. Source strings,
domains, placeholders, dependencies, and loading hooks must allow translations
to be added later. Creating or maintaining POT, PO, MO, or Jed JSON files and
proving loaded translations are required only when translation delivery is in
scope. Missing catalogs alone are not a readiness defect. Layout checks may use
synthetic expanded text and, when RTL is in scope, controlled RTL direction
without creating translations.

## Accessibility and proof

Use WCAG 2.2 AA as the default floor. Preserve labels, names, roles, values,
relationships, keyboard behavior, focus order, visible and unobscured focus,
error association, status announcements, zoom, contrast, and target size.

Source or build inspection does not prove rendering. State which behavior was
rendered and operated, which was only inspected, and what remains unverified.

## Result contract

Report the selected mode, target, and focus briefly. Keep the result within
that scope and distinguish rendered, source-only, and unverified evidence.

For **Audit**, report actionable findings in impact order. Each finding names
the location, owning rule and its source label, observed deviation, user impact,
smallest correction, and evidence limit. Separate confirmed defects from
suspicions and optional suggestions. If none were found, state that only for
the inspected scope. Never claim whole-UI compliance from a targeted check.
Do not modify the implementation unless correction was also requested. Writing
an explicitly requested audit report is allowed and does not authorize fixes.

For **Implement**, report what was designed or changed and the relevant checks
and limits. Use the following items only where they affect the requested work,
not as a mandatory report or full-audit checklist for every task:

- surface, support status, runtime, shell, spacing owner, and experimental
  policy;
- supported and observed WordPress versions, token stylesheet owner, required
  token names, enqueue evidence, and fallback when relevant;
- WordPress APIs, components, classes, defaults, and provided tokens reused;
- semantic relationship and its spacing expression;
- page archetype, responsive transformations, relevant states, and recovery;
- PHP/JavaScript i18n-readiness, expansion checks, and language-scoped RTL
  applicability, with translation artifacts and loading proof only when
  translation delivery is in scope;
- any CSS exception with checked owners, demonstrated gap, smallest scope, and
  reflow, zoom, focus, content, and state checks, plus RTL when in scope;
- rendered, source-only, and unverified evidence kept separate.

When the caller requests structured classification, use the canonical field
values and prohibited-recommendation identifiers from `routing.md`; do not
replace them with prose synonyms.

Label facts as **Core**, **WPDS**, **WCAG**, or **Skill-Norm**. Never describe
the Skill-Norm as an official WordPress HIG.
