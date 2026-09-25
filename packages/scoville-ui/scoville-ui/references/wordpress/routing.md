# Task, surface, and runtime routing

For every request, read `Select the focus` through `Experimental policy` before
dependent recommendations or actions. These sections contain the supported
surface, owner and prohibition semantics. Read `Canonical structured values`
and `Classification output` only when the caller explicitly requests structured
classification. Exact identifiers and the output protocol are conditional;
the meaning of every prohibition and exclusion is not.

Use the working mode defined in [Scoville UI](../../SKILL.md#mode-and-scope).
Within the selected scope, classify the surface before the runtime. Do not
infer either from the other.

## Select the focus

Take the target page or region and concerns from the request. Combine concerns
when requested or causally necessary, not merely because they share a file.
An unqualified page audit covers that page's applicable UI concerns. It does
not cover every plugin screen. A targeted audit covers only the selected
concerns and the dependencies needed to evaluate them.

| Focus | Inspect | Main reference |
| --- | --- | --- |
| Spacing and vertical flow | Parent/child ownership, gap versus margins, internal padding, hidden content, Core defaults, actual rendered distances where available. | [spacing.md](spacing.md) |
| Core defaults, tokens, and CSS | Runtime owner, reused Core markup/components, token availability and loading when consumed, CSS exceptions. | [spacing.md](spacing.md), [version-compatibility.md](version-compatibility.md) when version-sensitive |
| Responsive layout | Affected reflow, wrapping, overflow, order, zoom, and relevant widths. | [responsive.md](responsive.md) |
| User guidance and states | Task hierarchy, actions, feedback, recovery, and states possible in the selected flow. | [ui-guidance.md](ui-guidance.md) |
| Accessibility | Relevant semantics, keyboard/focus behavior, labels, contrast, targets, and reflow. | [ui-guidance.md](ui-guidance.md), [responsive.md](responsive.md) for layout |
| i18n-readiness | Strings, domains, formatting, dependencies/loading hooks, expansion, and language-scoped RTL. Translation delivery only when requested. | [internationalization.md](internationalization.md) |

For a consistency audit, read [validation.md](validation.md) and reconcile the
complete scoped element inventory with source, geometry and viewed evidence.
Include distinct variants, known exceptions, lower scroll areas and relevant
read-only same-page states. Do not infer complete coverage from a sample.

For a spacing audit, inspect the affected subtree and its actual spacing owner.
After source inspection, use computed styles and actual geometry for rendered
spacing claims. Missing runtime evidence is unverified, not an optional pass. A declared `gap`
alone does not establish the visible distance when margins, padding, or layout
participate. Compare against Core/component defaults before applying a
Skill-Norm. A native spacing value is not defective merely because it differs
from the Skill's fallback scale.

Check responsive or state variants when they can change the spacing conclusion,
such as wrapped controls or a hidden child. Do not automatically add catalog
generation, RTL tests, navigation redesign, or every application state. For a
source-only request, report source findings and the unverified rendering
boundary rather than requiring a browser or claiming visual proof.

In Implement, new pages apply all relevant design-system concerns to that page.
An isolated fix applies them to the changed region and affected behavior, not
unrelated screens. Preserve functioning Classic elements and Core defaults.
Stop when the requested outcome has proportionate evidence. Missing browser
access limits rendered claims, not the ability to provide a source audit.

## Surface support

| Surface | Version 1 status | Shell owner |
| --- | --- | --- |
| Plugin-owned single-site settings or tool page | supported | Core admin shell |
| Plugin-owned workflow or dashboard page | supported | Core shell plus explicit plugin root |
| Plugin-owned data view | supported | Core shell plus explicit plugin root |
| Plugin-owned Network Admin page | supported with explicit Multisite context | Network Admin shell |
| Block Editor sidebar or SlotFill | excluded | Block Editor owner |
| Editor canvas | excluded | Editor owner |
| Post metabox | excluded | Post editor/metabox owner |
| Dashboard widget | excluded | Core Dashboard owner |
| Profile field | excluded | Core profile-screen owner |
| Extension of an existing Core list or screen | excluded | Host Core screen |
| UI inside another plugin | excluded | Host plugin |

For an excluded surface, route to its host and stop. Do not apply a
plugin-owned page shell, a generic spacing matrix, or global admin CSS.

## WordPress version and capabilities

| Target | Core token stylesheet | Public provider | Routing consequence |
| --- | --- | --- | --- |
| 7.0 pinned baseline | No Core `wp-theme` style handle in the verified baseline | Not exported by pinned `@wordpress/theme` 0.7.1 | Preserve Classic/Core defaults. The explicitly opted-in bundled experimental path below remains version-specific. |
| 7.1 | Core registers `wp-theme` with semantic tokens for plugin UIs | Public `ThemeProvider` from `@wordpress/theme` through the Core script handle | PHP may consume Core tokens without React. React may use the public provider when needed. Neither requires experimental-component opt-in. |

Check the actual supported installation and minimum supported version. Style
and script registries are separate even though both use `wp-theme`. Registration
does not prove enqueue, successful loading, token availability, or rendering.
Read [version-compatibility.md](version-compatibility.md) when the task depends
on token/provider availability, loading, or fallback. A spacing check on native
Core markup does not require a token-loading audit if it consumes no tokens.
Do not infer future 7.x contracts or package versions from either row.

## Runtime owners

### PHP/Core

- Use WordPress APIs, semantic admin markup, Core classes, and Core default CSS.
- Core owns `.wrap`, the page title, `.wp-header-end`, native Notices,
  `.form-table`, controls, and `p.submit` where those structures are used.
- Preserve existing Classic pages. No mandatory token conversion, React rewrite,
  or replacement of native elements follows from a WordPress upgrade.
- Do not add experimental WPDS components or a second spacing owner over the
  same subtree. Core `wp-theme` tokens are allowed for a demonstrated missing
  relationship or domain state inside a plugin-owned region, not for restyling
  native controls. The runtime remains `php-core`.

### React/Core Components

- Use Core-provided `@wordpress/components` and registered WordPress packages.
- React alone does not authorize bundled experimental WPDS.
- Specialized components own their internal spacing. Stable `Flex` owns a new
  generic vertical group.

### Bundled experimental WPDS

- Requires an explicit project choice, exact package versions, public package
  APIs, and the exported design-token stylesheet.
- `@wordpress/ui`, `@wordpress/theme`, and `@wordpress/admin-ui` are an
  experimental bundled path at the WordPress 7.0 target.
- `ThemeProvider` is not a public runtime export at this pin. Never unlock
  `@wordpress/theme` private APIs from plugin code.
- Consume semantic tokens only when the selected exported stylesheet supplies
  them. The supported baseline uses default density.
- These package pins describe 7.0, not all WordPress 7 releases. On 7.1 use
  Core's token stylesheet instead of a second copy, and independently verify
  compatibility of any opted-in bundled component package.

### Hybrid

Record one owner per DOM region. A common boundary is:

| Region | Owner |
| --- | --- |
| `#wpcontent`, `.wrap`, title, `.wp-header-end`, page Notices | Core |
| Plugin React mount and descendants | selected React runtime |
| Portal or overlay | runtime and token stylesheet at actual render root |

`.form-table` and a plugin gap stack never own the same subtree.

## Experimental policy

Use `allow`, `deny`, or `unknown`. `unknown` behaves as `deny` for introducing a
new experimental API. Availability alone is not opt-in. A pre-existing
experimental subtree remains its owner unless the task has a functional reason
to change it. Stable `Flex` remains available for all three values.

Core's 7.1 token stylesheet and public `ThemeProvider` are not bundled
experimental components. `deny` does not prohibit their supported use. A
provider is optional and must never force a PHP page into React.

Use `deny` when the request selects a non-experimental PHP/Core route or a
Core-only hybrid route. Use `allow` only for an explicit bundled experimental
WPDS opt-in. Use `unknown` only when the request leaves a decision-relevant
experimental policy or runtime fact genuinely unspecified; do not replace a
known non-experimental route with `unknown`.

For an excluded host-owned surface, report `deny` when the named host is a
Classic/Core PHP surface and `unknown` when it is React-owned or the host
runtime is unspecified. This field records the known host fact; it never gives
this Skill permission to prescribe the excluded surface.

Use this exact handoff matrix for the excluded version-1 surfaces. The listed
prohibitions are required; add other applicable stable identifiers only when
the request supplies evidence for them.

| Excluded surface | Policy | Required prohibited identifiers |
| --- | --- | --- |
| Block Editor sidebar/SlotFill | `unknown` | `own-host-surface`, `frontend-theme-spacing`, `recommend-without-clarification` |
| Editor canvas | `unknown` | `own-host-surface`, `frontend-theme-spacing`, `recommend-without-clarification` |
| Post metabox | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| Dashboard widget | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| Profile field | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides`, `custom-css-before-core` |
| Existing Core list/screen | `deny` | `own-host-surface`, `inject-wpds-into-classic`, `global-wp-admin-overrides` |
| UI inside another plugin | `unknown` | `own-host-surface`, `assume-react-is-wpds`, `recommend-without-clarification` |

If the request explicitly says that no experimental component policy was
provided, return `unknown` even when the known runtime is Core Components;
`unknown` still behaves as deny for adding an experimental API. If the page's
placement or host boundary is not specified, return `unknown` for
`shell_owner` rather than assuming a Core plugin root.

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

`inject-wpds-into-classic` prohibits introducing a bundled experimental component
runtime merely to restyle Classic UI. It does not prohibit a Core `wp-theme`
stylesheet dependency. `define-wpds-tokens` prohibits plugin-authored token
assignments or imitations, not supported public provider props.
`unlock-private-theme-provider` prohibits private APIs on every version, not
the public 7.1 export. Keep these identifiers stable with these precise meanings.

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

For a version-sensitive recommendation, also record supported/observed versions,
token stylesheet owner, required token names, and loading/fallback evidence.
These facts supplement the six stable fields, they do not change a PHP route
to `bundled-wpds` just because Core tokens are available.

First seek needed surface, runtime, token-style, or ownership evidence in the
supplied context and accessible source or runtime within the authorized scope.
If a decision-relevant fact remains unresolved after that inspection, return
`needs-clarification`, name the missing fact, and emit no downstream spacing or
component recommendation that depends on it. A token-style fact is not needed
for a native Core region that consumes no tokens. Continue independent checks
within scope without inventing the missing owner or blocking on unrelated facts.

## Fact labels

- **Core:** documented API, established admin convention, or explicitly named
  observed implementation with its WordPress version named.
- **WPDS:** documented or observed token/component behavior with its provider
  and version named. This label does not by itself mean experimental.
- **WCAG:** normative accessibility requirement.
- **Skill-Norm:** an openly identified rule that closes an unspecified gap.

Observed Core selectors are not automatically public extension APIs.
