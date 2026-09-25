# WordPress admin adapter

Use the mode and authority boundaries from [Scoville UI](../../SKILL.md).
This adapter specializes the shared UI contract for supported plugin-owned
WordPress 7 admin pages. It applies to the plugin's backend UI, never its
frontend output or theme design. It is not another Skill or a second acceptance process.
For excluded host-owned surfaces, report the host owner and stop the plugin-page
route. Do not use the general route to bypass those exclusions. Site frontends
and themes use their actual product/framework owner, not this admin adapter.

## Classify the target surface and runtime

Read [routing.md](routing.md) first for focus selection and ownership.
Classify three independent axes for the region in scope:

1. the admin surface and whether the version 1 surface-support table in routing.md supports it;
2. the runtime and component owner for each affected DOM region;
3. the supported WordPress versions and relevant public token/provider APIs.

React does not imply WPDS. A page can be Classic, Core Components, bundled
experimental WPDS, or hybrid. For hybrid pages, classify portals and overlays
at their actual render destination.

If the surface is excluded, name its host owner and do not apply this adapter's
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
  custom CSS, read [spacing.md](spacing.md).
- For page shells, columns, toolbars, data views, narrow widths, zoom, RTL, or
  content expansion, read [responsive.md](responsive.md).
- For navigation, hierarchy, actions, forms, Notices, loading, empty, success,
  error, disabled, permission, or recovery states, read
  [ui-guidance.md](ui-guidance.md).
- When creating or changing user-facing strings, accessible text, dates,
  numbers, or translation loading, or auditing i18n-readiness or localized
  layout, read
  [internationalization.md](internationalization.md).
- Read [examples.md](examples.md) only when a concrete syntax or
  composition question remains after the applicable contracts. Read only the
  matching runtime section. Examples demonstrate ownership and are not
  templates to copy across runtimes.
- Before asserting that a rule is official, updating the WordPress target, or
  changing a token/package contract, read [sources.md](sources.md)
  and recheck the relevant source contract when its listed revalidation condition
   applies.
- For `wp-theme`, public `ThemeProvider`, or older-version fallback, read
  [version-compatibility.md](version-compatibility.md).

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
