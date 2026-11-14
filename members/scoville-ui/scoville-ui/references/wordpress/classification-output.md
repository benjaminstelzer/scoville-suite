# Structured WordPress classification

Read this file only when a structured classification was explicitly
requested, after [routing.md](routing.md). Routing decides what is supported
and excluded; this file fixes the values to output.

## Classification output

Return a structured object with all eight fields:

1. `surface`
2. `support_status`
3. `runtime_owner`
4. `shell_owner`
5. `spacing_owner`
6. `experimental_components_policy`
7. `evidence`: observed facts supporting the values.
8. `prohibited_recommendations`: every applicable stable identifier below.

Use the canonical values and precedence below. Take each value from what
you observed, not from an example. Ordinary findings report only the facts
needed to explain the result, not a full classification.

Use this matrix for the excluded surfaces. Add the identifiers of every
runtime rule below that also applies; the surface row does not replace them.
Example: a React SlotFill whose package is unknown also gets the unknown-React
identifiers.

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
| Supported page whose project explicitly opted in to bundled experimental WPDS components | Policy `allow`. |
| Supported PHP/Core page, or hybrid page whose regions all use non-experimental Core, without that opt-in | Policy `deny`. |
| Any other supported page without that opt-in | Policy `unknown`. |
| Excluded named Classic PHP host using Core, without that override | Policy `deny`. It records a host fact; the surface stays the host's. |
| Excluded React-owned or unspecified host runtime | Policy `unknown`. The surface stays the host's. |
| Page placement or host boundary not established by supplied facts | `shell_owner: unknown`; neither Hybrid nor runtime opt-in establishes a Core shell. |
| Page placement or another decision-relevant owner unresolved | `support_status: needs-clarification`; runtime opt-in does not resolve placement. |

Unknown policy still forbids introducing experimental APIs.

Emit these exact values, not prose variants:

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
| surface | Plugin-owned page with unspecified category | `plugin-owned-unspecified` |
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

What five of the identifiers prohibit:

| Identifier | Prohibits | Does not prohibit |
| --- | --- | --- |
| `own-host-surface` | Treating a host's surface as the plugin's own page | Naming the host's own mechanism from routing.md |
| `recommend-without-clarification` | Advice that depends on a fact the user has not given | Advice that does not depend on it |
| `inject-wpds-into-classic` | Bundled experimental components added merely to restyle Classic UI | A Core `wp-theme` stylesheet |
| `define-wpds-tokens` | Plugin-authored token assignments or imitations | Supported public provider props |
| `unlock-private-theme-provider` | Private APIs on every version | The public 7.1 export |

Minimum identifiers per route. Add every other identifier from the list that
applies; do not invent identifiers.

| Route | Must include |
| --- | --- |
| Unknown React runtime | `assume-react-is-wpds`, `define-wpds-tokens`, `recommend-without-clarification` |
| Excluded host surface | Its row in the matrix above, which always has `own-host-surface`; also `recommend-without-clarification` when a host fact needed for a recommendation is absent |
| Classic PHP plugin page using Core | `frontend-theme-spacing`, `inject-wpds-into-classic`, `global-wp-admin-overrides`, `custom-css-before-core` |
| Bundled WPDS route | `unlock-private-theme-provider`, `define-wpds-tokens`, `global-wp-admin-overrides`, `custom-css-before-core` |