# Structured WordPress classification

Load only when structured classification was explicitly requested, after
[routing.md](routing.md). The router owns the semantic boundaries.

Use this handoff matrix for the excluded version-1 surfaces. Combine its
required prohibitions with every applicable runtime rule below. For example,
a React SlotFill with an unknown package owner also requires the unknown-React
prohibitions. The surface row does not replace them.

| Excluded surface | Policy | Required prohibited identifiers |
| --- | --- | --- |
| Block Editor sidebar or SlotFill | `unknown` | `own-host-surface`, `frontend-theme-spacing`, `recommend-without-clarification` |
| Editor canvas | `unknown` | `own-host-surface`, `frontend-theme-spacing`, `recommend-without-clarification` |
| Post metabox | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| Dashboard widget | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| Profile field | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides`, `custom-css-before-core` |
| Existing Core list or screen | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| UI inside another plugin | `unknown` | `own-host-surface`, `assume-react-is-wpds`, `recommend-without-clarification` |

## Canonical structured values

| Classification condition | Required value or boundary |
| --- | --- |
| Request explicitly says no experimental policy was supplied | `experimental_components_policy: unknown`, even for Core Components or an otherwise deny route. |
| Excluded named Classic PHP host using Core, without that override | Policy `deny`; records host facts, grants no right to prescribe the surface. |
| Excluded React-owned or unspecified host runtime | Policy `unknown`; grants no right to prescribe the surface. |
| Page placement or host boundary unspecified | `shell_owner: unknown`. |
| Decision-relevant ownership unresolved | `support_status: needs-clarification`; supported surface category alone does not resolve it. |

Unknown policy still forbids introducing experimental APIs.

When a caller requests structured classification, emit these exact stable
values instead of prose variants:

| Field | Meaning | Canonical value |
| --- | --- | --- |
| surface | Plugin settings or tool | `plugin-settings-tool` |
| surface | Plugin workflow or dashboard | `plugin-workflow-dashboard` |
| surface | Plugin data view | `plugin-data-view` |
| surface | Explicit Network Admin | `plugin-network-admin` |
| surface | Block Editor sidebar or SlotFill | `block-editor-sidebar-slotfill` |
| surface | Editor canvas | `editor-canvas` |
| surface | Post metabox | `post-metabox` |
| surface | Dashboard widget | `dashboard-widget` |
| surface | Profile field | `profile-field` |
| surface | Extension of an existing Core screen | `core-screen-extension` |
| surface | UI inside another plugin | `foreign-plugin-surface` |
| surface | Plugin-owned page with unspecified runtime | `plugin-owned-unspecified` |
| surface | Admin surface with unspecified placement | `unknown-admin-surface` |
| support_status | Supported stable route | `supported` |
| support_status | Supported bundled experimental route | `supported-experimental-opt-in` |
| support_status | Supported Network Admin route | `supported-explicit-multisite` |
| support_status | Excluded host-owned route | `excluded-route-to-host-owner` |
| support_status | Missing decision-relevant fact | `needs-clarification` |
| runtime_owner | PHP with Core admin | `php-core` |
| runtime_owner | React with Core Components | `react-core-components` |
| runtime_owner | Bundled experimental WPDS | `bundled-wpds` |
| runtime_owner | Region-owned mixed page | `hybrid` |
| runtime_owner | Excluded host-owned runtime | `host-owned` |
| shell_owner | Core admin shell | `core-admin` |
| shell_owner | Core shell plus plugin root | `core-admin-plugin-root` |
| shell_owner | Core and React region map | `core-admin-region-map` |
| shell_owner | Network Admin shell | `network-admin` |
| shell_owner | Network Admin and React region map | `network-admin-region-map` |
| shell_owner | Block Editor shell | `block-editor` |
| shell_owner | Editor canvas shell | `editor-canvas` |
| shell_owner | Post editor shell | `post-editor` |
| shell_owner | Core Dashboard shell | `core-dashboard` |
| shell_owner | Core profile screen | `core-profile-screen` |
| shell_owner | Existing Core list or screen | `core-list-screen` |
| shell_owner | Host plugin shell | `foreign-plugin` |
| spacing_owner | Core default rhythm | `core-default-css` |
| spacing_owner | Core Components | `core-components` |
| spacing_owner | WPDS Stack and exported tokens | `wpds-stack-and-exported-token-stylesheet` |
| spacing_owner | Region-owned spacing | `region-map` |
| spacing_owner | Block Editor spacing | `block-editor` |
| spacing_owner | Editor canvas spacing | `editor-canvas` |
| spacing_owner | Post editor or metabox spacing | `post-editor-metabox` |
| spacing_owner | Core Dashboard widget spacing | `core-dashboard-widget` |
| spacing_owner | Core profile-screen spacing | `core-profile-screen` |
| spacing_owner | Existing Core list or screen spacing | `core-list-screen` |
| spacing_owner | Host plugin spacing | `foreign-plugin` |
| runtime_owner / shell_owner / spacing_owner | Unknown owner | `unknown` |

For structured `prohibited_recommendations`, use only the applicable stable
identifiers: `assume-react-is-wpds`, `custom-css-before-core`,
`define-wpds-tokens`, `frontend-theme-spacing`, `global-wp-admin-overrides`,
`inject-wpds-into-classic`, `own-host-surface`,
`recommend-without-clarification`, and `unlock-private-theme-provider`.
Their prose explanation may follow outside the structured object.

`inject-wpds-into-classic` prohibits introducing bundled experimental
components merely to restyle Classic UI, not a Core `wp-theme` stylesheet.
`define-wpds-tokens` prohibits plugin-authored token assignments or imitations,
not supported public provider props. `unlock-private-theme-provider` prohibits
private APIs on every version, not the public 7.1 export.

An unknown React runtime must include `assume-react-is-wpds`,
`define-wpds-tokens`, and `recommend-without-clarification`. An excluded host
surface must include `own-host-surface`; when the host facts needed for a
downstream recommendation are absent, also include
`recommend-without-clarification`. Additional applicable identifiers are
allowed, but these route-specific prohibitions must not be omitted.

A Classic PHP plugin page using Core must include `frontend-theme-spacing`,
`inject-wpds-into-classic`, `global-wp-admin-overrides`, and
`custom-css-before-core`. A bundled WPDS route must include
`unlock-private-theme-provider`, `define-wpds-tokens`,
`global-wp-admin-overrides`, and `custom-css-before-core`. A Block Editor
sidebar or SlotFill handoff must include `own-host-surface`,
`frontend-theme-spacing`, and `recommend-without-clarification` because this
Skill must stop before prescribing the host-owned details.

## Classification output

For an explicit classification request, return:

- `surface` and `support_status`;
- `runtime_owner`;
- `shell_owner`;
- `spacing_owner`;
- `experimental_components_policy`;
- supporting source or repository evidence;
- prohibited recommendations for this route.

When structured output was requested, use the canonical values above for all
six fields and for each prohibited-recommendation identifier. Otherwise use
these facts to establish ownership and report only those needed to explain the
scoped result. Do not add a full classification report to every finding.
