# Spacing ownership

Before choosing or judging a spacing value, find what renders the region:

| Region | Read | Rule |
| --- | --- | --- |
| Classic page built from Core markup | [classic-patterns.md](classic-patterns.md) | Keep its authored units and context-specific cascade. Classic has no universal 4/8px scale. |
| Region that consumes WPDS tokens | [wpds-tokens.md](wpds-tokens.md), [version rules](version-compatibility.md) | A token's existence does not map it to a Classic relationship. |
| New plugin-owned relationship that Core markup, classes and components leave unspaced, which you check in their source | Only then [fallback-composition.md](fallback-composition.md) | Skill choices, not official defaults or targets for normalizing existing UI. |

- A requested rendered check, or a requested review or audit of how the page
  looks, takes its spacing evidence from [validation.md](validation.md);
  `gap` alone proves no visible distance.
- Keep original units, unitless line-height, tokens and calculations: `1em`
  at a 13px font resolves to 13px but must not become a new `13px` or `1rem`
  rule.
- A native value outside a 4/8px scale is not a defect for that reason.
- Project-specific minimums do not become Core rules.

## Parent ownership

These rules apply to a new plugin-owned group composed with `gap`. They do
not replace working native margin-based flow.

1. The direct parent sets the spacing between its direct children.
2. Children do not add the same outer margin when their parent uses `gap`.
3. A nested group chooses the gap for its own children instead of copying
   the parent's gap.
4. A card or panel sets its internal padding. Its parent sets the distance
   to peers.
5. Hidden, unmounted, or empty children occupy no gap slot.
6. Help, status, and error text stays with the control it explains.
7. Reset heading or paragraph margins only inside the exact plugin-owned gap
   parent that replaces them.
8. A portal or overlay gets its spacing at the element it renders into.

Compare a heading's distance to its content with its distance to the next
section. Trace an unexplained difference to the parent gap, child margins,
padding and native elements in between before changing a value. Keep
deliberate differences between levels; do not make every distance equal. A
valid token alone does not show that the rendered grouping is right.

## Runtime expression

### Classic

Reuse the native shell and Settings API rhythm. Never put a gap stack over
`.wrap`, `.form-table`, or `p.submit`. A plugin-owned inner component may use
a Skill-Norm gap only for a relationship that Core markup, classes and
components leave unspaced, which you check in their source.

Where no Core markup or class spaces a new relationship, a 7.1 page may
express its gap through Core's loaded `--wpds-dimension-gap-*` tokens in
narrowly scoped plugin CSS. A stylesheet is not a React runtime.
Prefer this supplied token over a new local spacing variable, and do not
apply it over native rhythm that works. See
[version-compatibility.md](version-compatibility.md) for the explicit 7.0
fallback and registration, loading and token-name checks.

### Core Components

Specialized components space their own internals. For a new generic group,
first confirm that no existing component or prop expresses the relationship;
only then use the prop combination below. It is Skill-Norm composition, not
the component defaults. `GAP_PX` is the chosen distance in pixels. Stable
`Flex` multiplies its numeric gap by four pixels, so divide `GAP_PX` by four.
This recipe is the default whether or not the project opted in to experimental
components:

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

Before this route, read [experimental-policy.md](experimental-policy.md) for
public APIs, token ownership and explicit Stack props at the pin.

### Core tokens and public theming in 7.1

- Inside WordPress, depend on the existing `wp-theme` style handle. Do not
  bundle a second token stylesheet.
- A public `ThemeProvider` is optional, for scoped React theming. It does not
  replace the stylesheet, and PHP does not need it.
- For portals, popups and iframes, check which document loads the tokens.

## CSS ownership ladder

Stop at the first layer that fits:

1. WordPress API and semantic Core markup.
2. Core class or WordPress component with default CSS.
3. Semantic token actually supplied by the runtime.
4. Plugin-owned composition through props, Grid or Flex, `gap`, and logical
   properties.
5. Narrow plugin CSS, only for a gap the layers above leave open.

Before writing an exception, apply common Validation's
[styling-exception rules](../validation.md#styling-exceptions); for a local
React stack, `Flex` is one of the supported options they weigh.

Reject global `.wp-admin`, `.wrap`, `.form-table`, or Core-control overrides,
copied Core CSS, custom Core-primitive rebuilds, unloaded WPDS references,
parallel colors, radii and shadows, and `!important` without a
styling-exception rationale.
