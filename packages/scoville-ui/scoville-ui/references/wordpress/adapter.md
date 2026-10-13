# WordPress admin adapter

Use the mode and authority boundaries from [Scoville UI](../../SKILL.md).
This adapter specializes the shared UI contract for supported plugin-owned
WordPress 7 admin pages. It applies to the plugin's backend UI, never its
frontend output or theme design. It is not another Skill or a second acceptance process.
For excluded host-owned surfaces, report the host owner and stop the plugin-page
route. Do not use the general route to bypass those exclusions. Site frontends
and themes use their actual product or framework owner, not this admin adapter.

## Respect the classified owner

Use [routing.md](routing.md)'s surface, region-runtime and version classification.
Resolve unknown ownership before dependent advice; continue independent checks.
Before choosing composition or CSS, read [spacing.md](spacing.md) and stop at the
first suitable layer in its ownership ladder. Never rebuild native buttons,
controls, Notices, tables, shell, colors, focus, radii or shadows just for appearance.
Never author --wpds-* definitions, overrides or imitations. Supported public
provider props may generate scoped overrides through their documented API.
No experimental component injection, React conversion or token migration follows
from a WordPress upgrade. Keep functioning Classic markup and native spacing.

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
  changing a token or package contract, read [sources.md](sources.md)
  and recheck the relevant source contract when its listed revalidation condition
  applies.
- For `wp-theme`, public `ThemeProvider`, or older-version fallback, read
  [version-compatibility.md](version-compatibility.md).

## Keep every UI translatable

All visible and assistive strings use WordPress i18n APIs and one literal text
domain matching the plugin slug. Require i18n-readiness; catalogs and proof of
loaded translations are required only when translation delivery is in scope.
Before strings, locale values, translation loading or localized-layout work,
read [internationalization.md](internationalization.md), including its scoped
RTL rule.

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

For **Implement**, report the changes, relevant checks and limits. Include only
facts needed for this task: surface/support/runtime/shell/spacing/experimental
owners; supported and tested versions, token names and loading/fallback proof;
reused APIs/components/defaults; relationship and spacing expression; archetype,
responsive states and recovery; i18n-readiness/expansion and applicable RTL;
translation artifacts/loading only for delivery scope; and CSS exceptions with
checked owners, demonstrated gap, smallest scope and relevant reflow, zoom,
focus, content and state evidence. Distinguish rendered, source-only and
unverified results. This is not a mandatory full-audit checklist.

When the caller requests structured classification, use the canonical field
values and prohibited-recommendation identifiers from
[classification-output.md](classification-output.md); do not
replace them with prose synonyms.

Label facts as **Core**, **WPDS**, **WCAG**, or **Skill-Norm**. Never describe
the Skill-Norm as an official WordPress HIG.
