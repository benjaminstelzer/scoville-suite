# WordPress admin adapter

Use the mode and authority boundaries from [Scoville UI](../../SKILL.md).
This adapter specializes the shared UI contract for supported plugin-owned
WordPress 7 backend pages. [Routing](routing.md) owns surface exclusions,
classification and focus; site frontends and themes use their product or
framework owner. Apply platform checks within the shared acceptance process.

## Respect the classified owner

Before choosing composition or CSS, read [spacing.md](spacing.md) and stop at the
first suitable layer in its ownership ladder. Core owns `.wrap`, title,
`.wp-header-end`, page Notices, native `.form-table`, controls and `p.submit`.
Preserve functioning Classic markup and native spacing. Never rebuild native
buttons, controls, Notices, tables, shell, colors, focus, radii or shadows just
for appearance.
Never author --wpds-* definitions, overrides or imitations. Supported public
provider props may generate scoped overrides through their documented API.
No experimental component injection, React conversion or token migration follows
from a WordPress upgrade. Tokens may fill an actual plugin-owned gap or domain
state; they do not authorize restyling native controls.

## Load only the relevant contract

Use [routing.md's focus table](routing.md#select-the-focus).

- Read [examples.md](examples.md) only when a concrete syntax or
  composition question remains after the applicable contracts. Read only the
  matching runtime section. Examples demonstrate ownership and are not
  templates to copy across runtimes.
- Before asserting that a rule is official, updating the WordPress target, or
  changing a token or package contract, read [sources.md](sources.md)
  and recheck the relevant source contract when its listed revalidation condition
  applies.

## Keep every UI translatable

When creating, changing or auditing visible or assistive strings, apply
[i18n-readiness](internationalization.md). Locale values, loading and localized
layout use the router's focus triggers; translation delivery and RTL checks
follow that reference's scope conditions.

## Result contract

Report the selected mode, target, and focus briefly. Keep the result within
that scope and distinguish rendered, source-only, and unverified evidence.

For **Audit**, report actionable findings in impact order. Each finding names
the location, owning rule and its source label, observed deviation, user impact,
simplest sound correction, and evidence limit. Separate confirmed defects from
suspicions and optional suggestions. If none were found, state that only for
the inspected scope. Never claim whole-UI compliance from a targeted check.
Do not modify the implementation unless correction was also requested. Writing
an explicitly requested audit report is allowed and does not authorize fixes.

For **Implement**, report changes, checks and limits with the ownership,
version/loading, spacing, state, i18n or CSS-exception facts needed to explain
the scoped result. Use [WordPress validation](validation.md) for applicable
evidence; do not turn the result into a full-audit checklist.

When the caller requests structured classification, use the canonical field
values and prohibited-recommendation identifiers from
[classification-output.md](classification-output.md); do not
replace them with prose synonyms.

Label facts as **Core**, **WPDS**, **WCAG**, or **Skill-Norm**. Never describe
the Skill-Norm as an official WordPress HIG.
