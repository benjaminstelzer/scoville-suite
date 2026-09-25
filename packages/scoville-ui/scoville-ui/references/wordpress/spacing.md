# Spacing ownership

Classify the owning region before selecting or judging a spacing value.

- **Classic/Core markup:** Read [classic-patterns.md](classic-patterns.md).
  Preserve its authored units and context-specific cascade. There is no
  universal Classic 4/8px spacing scale.
- **A region consuming WPDS tokens:** Read [wpds-tokens.md](wpds-tokens.md)
  and the relevant [version contract](version-compatibility.md). A token's
  existence does not map it to a Classic relationship.
- **A demonstrated native-owner gap:** Only then read
  [fallback-composition.md](fallback-composition.md). Those are Skill choices,
  not official defaults or targets for normalizing existing UI.

Inspect source first, then actual geometry, then sight as specified in
[validation.md](validation.md). Preserve original units, unitless line-height,
tokens and calculations. `1em` at a 13px element font resolves to 13px but must
not become a new `13px` or `1rem` rule. Native values outside a 4/8px scale are
not defects for that reason. Project-specific minimums do not become Core rules.

## Parent ownership

These rules govern new plugin-owned gap composition. They do not replace
working native margin-based flow.

1. The direct parent owns spacing between its direct children.
2. Children do not add the same outer margin when their parent uses `gap`.
3. Nested groups choose the relationship for their own children instead of
   inheriting the parent gap blindly.
4. A card or panel owns internal padding. Its parent owns distance to peers.
5. Hidden, unmounted, or empty children occupy no gap slot.
6. Help, status, and error text stays with the control it explains.
7. Reset heading or paragraph margins only inside the exact plugin-owned gap
   parent that replaces them.
8. Portals and overlays declare the owner at their render destination.

Compare the heading-to-content relationship with separation from adjacent
sections. Trace unexplained differences to the actual parent, child margins,
padding and intervening native elements before changing values. Preserve
deliberate hierarchy instead of making every distance equal. A valid token
alone does not prove the intended grouping in the rendered composition.

## Runtime expression

### Classic

Core owns native shell and Settings API rhythm. Reuse it. A plugin-owned inner
component may use a Skill-Norm gap only after Core markup, classes, and default
CSS have been checked. Never apply a gap stack over `.wrap`, `.form-table`, or
`p.submit`.

Existing Classic layout does not need token migration. When an actual new
relationship lacks a Core owner, 7.1 may express its gap through Core's loaded
`--wpds-dimension-gap-*` tokens in narrowly scoped plugin CSS. A stylesheet is
not a React runtime. Prefer this supplied semantic token over a new local
spacing variable. Do not apply it over native rhythm that already works.
See [version-compatibility.md](version-compatibility.md) for an explicit 7.0
fallback and registration, loading, and token-name checks.

### Core Components

Specialized components own their internals. The following explicit prop
combination is Skill-Norm composition for a new generic group, not the
component defaults. Select its gap only after confirming that the existing
owner cannot express the required relationship. `GAP_PX` is the chosen distance
in pixels. Divide it by four to obtain the numeric `Flex` gap value:

```jsx
<Flex
  direction="column"
  align="stretch"
  justify="flex-start"
  wrap={ false }
  expanded={ true }
  gap={ GAP_PX / 4 }
>
  { children }
</Flex>
```

Use `FlexItem` for intrinsic content. Use `FlexBlock` only for content intended
to grow into remaining space. Preserve an existing `__experimentalVStack`
subtree unless a functional requirement justifies changing it.

### Bundled WPDS at the 7.0 pin

Bundle the public `@wordpress/ui` API and the exported
`@wordpress/theme/design-tokens.css`, then select the semantic token. At this
pin `ThemeProvider` is not a public runtime export; never unlock
`@wordpress/theme` private APIs from plugin code. `Stack` has neither a default
direction nor a default gap, so set `direction="column"` and the semantic gap
explicitly for vertical flow. The stylesheet supplies the default-density
tokens. Never define, override, or imitate the `--wpds-*` namespace. Primitive
tokens are implementation details.

### Core tokens and public theming in 7.1

Within WordPress, depend on the existing `wp-theme` style handle. Do not bundle
a second token stylesheet. A public `ThemeProvider` is optional for scoped React
theming and does not replace the stylesheet. PHP does not need the provider.
Keep the actual token-owning document in view for portals, popups, and iframes.

Supported semantic foreground/background/stroke tokens may express a genuine
plugin-specific domain state when no Core component already owns it. Preserve
native controls, tables, Notices, focus treatment, and existing layout. Verify
contrast, non-color cues, interaction states, and token resolution. Do not
invent a palette or override `--wpds-*` in plugin CSS. Using official tokens
does not automatically prove accessibility or authorize broader restyling.

## CSS ownership ladder

Stop at the first suitable owner:

1. WordPress API and semantic Core markup.
2. Core class or WordPress component with default CSS.
3. Semantic token actually supplied by the runtime.
4. Plugin-owned composition through props, Grid/Flex, `gap`, and logical
   properties.
5. Narrow plugin CSS for a demonstrated gap only.

Before writing an exception, record the DOM/runtime owner, concrete relevant
WordPress options checked, why
those options fail, why `Flex` fails for a local React stack, the smallest
plugin scope, token or Skill-Norm source, and checks for reflow, zoom, focus,
text expansion, empty content, and affected states. Add RTL checks only under
the [language-scope rule](internationalization.md#language-scoped-rtl-checks).

Reject global `.wp-admin`, `.wrap`, `.form-table`, or Core-control overrides,
copied Core CSS, custom Core-primitive rebuilds, unloaded WPDS references,
parallel colors/radii/shadows, and undocumented `!important`.
