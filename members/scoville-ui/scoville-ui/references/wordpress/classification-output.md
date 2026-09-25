# Structured WordPress classification

Load only when structured classification was explicitly requested, after
[routing.md](routing.md). The router owns the semantic boundaries.

Use this handoff matrix for the excluded version-1 surfaces. Combine its
required prohibitions with every applicable runtime rule below. For example,
a React SlotFill with an unknown package owner also requires the unknown-React
prohibitions. The surface row does not replace them.

| Excluded surface | Policy | Required prohibited identifiers |
| --- | --- | --- |
| Block Editor sidebar/SlotFill | `unknown` | `own-host-surface`, `frontend-theme-spacing`, `recommend-without-clarification` |
| Editor canvas | `unknown` | `own-host-surface`, `frontend-theme-spacing`, `recommend-without-clarification` |
| Post metabox | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| Dashboard widget | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| Profile field | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides`, `custom-css-before-core` |
| Existing Core list/screen | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| UI inside another plugin | `unknown` | `own-host-surface`, `assume-react-is-wpds`, `recommend-without-clarification` |

## Canonical structured values

When a caller requests structured classification, emit these exact stable
values instead of prose variants:

| Meaning | Canonical value |
| --- | --- |
| Plugin settings or tool | `plugin-settings-tool` |
| Plugin workflow or dashboard | `plugin-workflow-dashboard` |
| Plugin data view | `plugin-data-view` |
| Explicit Network Admin | `plugin-network-admin` |
| Block Editor sidebar/SlotFill | `block-editor-sidebar-slotfill` |
| Editor canvas | `editor-canvas` |
| Post metabox | `post-metabox` |
| Dashboard widget | `dashboard-widget` |
| Profile field | `profile-field` |
| Extension of an existing Core screen | `core-screen-extension` |
| UI inside another plugin | `foreign-plugin-surface` |
| Plugin-owned page with unspecified runtime | `plugin-owned-unspecified` |
| Admin surface with unspecified placement | `unknown-admin-surface` |
| Supported stable route | `supported` |
| Supported bundled experimental route | `supported-experimental-opt-in` |
| Supported Network Admin route | `supported-explicit-multisite` |
| Excluded host-owned route | `excluded-route-to-host-owner` |
| Missing decision-relevant fact | `needs-clarification` |
| PHP with Core admin | `php-core` |
| React with Core Components | `react-core-components` |
| Bundled experimental WPDS | `bundled-wpds` |
| Region-owned mixed page | `hybrid` |
| Excluded host-owned runtime | `host-owned` |
| Core admin shell | `core-admin` |
| Core shell plus plugin root | `core-admin-plugin-root` |
| Core/React region map | `core-admin-region-map` |
| Network Admin shell | `network-admin` |
| Network Admin/React region map | `network-admin-region-map` |
| Block Editor shell | `block-editor` |
| Editor canvas shell | `editor-canvas` |
| Post editor shell | `post-editor` |
| Core Dashboard shell | `core-dashboard` |
| Core profile screen | `core-profile-screen` |
| Existing Core list/screen | `core-list-screen` |
| Host plugin shell | `foreign-plugin` |
| Core default rhythm | `core-default-css` |
| Core Components | `core-components` |
| WPDS Stack and exported tokens | `wpds-stack-and-exported-token-stylesheet` |
| Region-owned spacing | `region-map` |
| Block Editor spacing | `block-editor` |
| Editor canvas spacing | `editor-canvas` |
| Post editor/metabox spacing | `post-editor-metabox` |
| Core Dashboard widget spacing | `core-dashboard-widget` |
| Core profile-screen spacing | `core-profile-screen` |
| Existing Core list/screen spacing | `core-list-screen` |
| Host plugin spacing | `foreign-plugin` |
| Unknown owner | `unknown` |

For structured `prohibited_recommendations`, use only the applicable stable
identifiers: `assume-react-is-wpds`, `custom-css-before-core`,
`define-wpds-tokens`, `frontend-theme-spacing`, `global-wp-admin-overrides`,
`inject-wpds-into-classic`, `own-host-surface`,
`recommend-without-clarification`, and `unlock-private-theme-provider`.
Their prose explanation may follow outside the structured object.

An unknown React runtime must include `assume-react-is-wpds`,
`define-wpds-tokens`, and `recommend-without-clarification`. An excluded host
surface must include `own-host-surface`; when the host facts needed for a
downstream recommendation are absent, also include
`recommend-without-clarification`. Additional applicable identifiers are
allowed, but these route-specific prohibitions must not be omitted.

A Classic PHP/Core plugin page must include `frontend-theme-spacing`,
`inject-wpds-into-classic`, `global-wp-admin-overrides`, and
`custom-css-before-core`. A bundled WPDS route must include
`unlock-private-theme-provider`, `define-wpds-tokens`,
`global-wp-admin-overrides`, and `custom-css-before-core`. A Block Editor
sidebar/SlotFill handoff must include `own-host-surface`,
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
