# Spacing ownership

This file holds where spacing comes from on a plugin admin page: the reference
for each kind of region, who sets the space in a new plugin-owned group, how
each runtime expresses it, and the CSS ownership ladder. Read it before
choosing or judging composition, CSS or a spacing value. First find what
renders the region:

| Region | Read | Rule |
| --- | --- | --- |
| Classic page built from Core markup | [classic-patterns.md](classic-patterns.md) | Keep its context-specific cascade. |
| Region that consumes WPDS tokens at the WordPress 7.0 pin (bundled experimental WPDS) | [experimental-policy.md](experimental-policy.md), then [wpds-tokens.md](wpds-tokens.md) and [version-compatibility.md](version-compatibility.md) | A token's existence does not map it to a Classic relationship. |
| Region that consumes Core tokens on WordPress 7.1 and later | [version-compatibility.md](version-compatibility.md) for the `wp-theme` style dependency, the optional public `ThemeProvider` and token loading in portals, popups and iframes; [wpds-tokens.md](wpds-tokens.md) for the values | The same. |
| Plugin-owned relationship, new or existing, that Core markup, classes and components leave unspaced, which you check in their source | Only then [fallback-composition.md](fallback-composition.md) | Skill choices that may supply a local fallback where SKILL.md's [rule for literal values](../../SKILL.md#spacing-size-alignment-and-literal-values) would ask for a precedent; not official defaults or targets for normalizing existing UI. |

- A declared `gap` alone proves no visible distance.
- Classic has no universal 4/8px scale.
- Project-specific minimums do not become Core rules.

## Parent ownership

These rules apply to a new plugin-owned group composed with `gap`. They do
not replace working native margin-based flow. Each source of space counts
once, as SKILL.md's
[Spacing, size, alignment and literal values](../../SKILL.md#spacing-size-alignment-and-literal-values)
says.

1. The direct parent sets the spacing between its direct children.
2. A nested group chooses the gap for its own children instead of copying
   the parent's gap.
3. A card or panel sets its internal padding. Its parent sets the distance
   to peers.
4. Hidden, unmounted, or empty children occupy no gap slot.
5. Help, status, and error text stays with the control it explains.
6. Reset heading or paragraph margins only inside the exact plugin-owned gap
   parent that replaces them.
7. A portal or overlay gets its spacing at the element it renders into.

Compare a heading's distance to its content with its distance to the next
section. Keep deliberate differences between levels; do not make every
distance equal. A valid token alone does not show that the rendered grouping
is right.

## Runtime expression

### Classic

Reuse the native shell and Settings API rhythm. Never put a gap stack over
`.wrap`, `.form-table`, or `p.submit`. A plugin-owned inner component may use
a Skill-Norm gap only for a relationship the table above shows Core leaves
unspaced.

Where no Core markup or class spaces such a relationship and the supported
range includes 7.1, express its gap through Core's `--wpds-dimension-gap-*`
tokens, branched at runtime, in narrowly scoped plugin CSS, not through a new
local spacing variable. A stylesheet is not a React runtime. See
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
to grow into remaining space.

## CSS ownership ladder

Stop at the first layer that fits:

1. WordPress API and semantic Core markup.
2. Core class or WordPress component with default CSS.
3. Semantic token actually supplied by the runtime.
4. Plugin-owned composition through props, Grid or Flex, `gap`, and logical
   properties.
5. Narrow plugin CSS, only for a gap the layers above leave open.

Before writing an exception, apply
[SKILL.md's rule on custom styling](../../SKILL.md#custom-styling).
