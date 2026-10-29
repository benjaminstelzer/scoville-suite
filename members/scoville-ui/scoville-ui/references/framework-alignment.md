# Framework Alignment

Resolve open UI ownership through the canonical layer chosen by the product.
Apply the entrypoint's concern-level authority and conflict contract.

## Find the owners

Inspect only sources relevant to the requested surface:

1. repository and product instructions;
2. installed dependencies and their versions;
3. product design-system documentation and shared UI packages;
4. provider setup, themes, semantic token definitions, component wrappers, and
   approved assets;
5. nearby, repeated rendered patterns and their source; and
6. official documentation for the installed version when supported behavior or
   customization remains uncertain.

Do not fetch mutable third-party skill files or generic design checklists at
runtime. Prefer installed source and version-matched official documentation.

Before custom styling, follow Validation's
[styling exception contract](validation.md#styling-exceptions).
When changing style values, follow the
[authored-unit contract](ui-geometry-validation.md#measure-relationships-not-declarations).

## Classify the stack

### Styled design system

Use supported components, semantic tokens, theme extension points and responsive
APIs as the visual owner. Reuse project wrappers before the underlying library.
Resolve a demonstrated system gap at its canonical owner within authorized scope.

### Headless component library

The library owns its implemented state, focus, keyboard, relationships and
announcements. Derive appearance from project tokens, wrappers and neighboring
surfaces while preserving that supported structure and behavior. A headless
library alone supplies no visual language.

### Utility or application framework

Look for project tokens, presets, component layers and deliberate local patterns.
Without such an owner, an installed UI layer's scale may supply coherent values.
A rendering framework such as React supplies neither a spacing/typography scale
nor product hierarchy, meaning or visual direction.

### Platform UI stack

Use platform components and conventions for navigation, input, focus, scaling,
safe areas, adaptation and accessibility unless the product system owns that
concern. Web-only measurements and interactions do not transfer automatically.

### Multiple layers

Assign each concern independently: visuals, composite interaction, platform
scaling and supplied wording can have different owners. Prefer the highest
canonical abstraction; installed layers alone do not justify mixed APIs.

## Distinguish convention from accident

Inspect a pattern's source, frequency and relation to canonical wrappers/tokens.
A deliberate current convention outranks a lower framework default; a copied
exception, stale screen or workaround alone establishes no product policy.

## Handle true greenfield work

Derive unsettled navigation, groups and flow from user tasks, content
relationships and usage frequency under Quality. For unresolved visuals:

1. follow the user's brief and target platform conventions;
2. use framework defaults and scales where they provide compatible primitives;
3. when polished presentation is part of the outcome, name a deliberate visual
   direction grounded in the product domain and primary task, then carry it
   consistently through information hierarchy, density, typography, shape,
   imagery, and interaction treatment without defaulting to a prescribed
   palette or fashionable template;
4. choose only the minimum internally consistent, reversible values needed for
   the requested surface; and
5. keep those choices local unless the task explicitly creates or extends the
   canonical design system.

For multiple requested views, choose shared values once at their nearest
common code owner. Reuse an existing project structure; if none exists, use the
smallest shared location needed by those views. Do not create a separate token
registry or design-system project for this local direction.

These choices define the requested surface, not a mature project-wide system.
Ask only when materially different directions would change the product outcome.
