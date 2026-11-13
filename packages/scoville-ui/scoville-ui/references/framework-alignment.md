# Framework Alignment

Use this file to settle which source decides an open UI concern: the layer
the product has chosen, whether instructions, design system, component
library, token set, platform or a deliberate local pattern. SKILL.md's Owners
section sets the order and the conflict rule.

## Find the owners

Inspect only sources relevant to the requested surface:

1. repository and product instructions;
2. installed dependencies and their versions;
3. product design-system documentation and shared UI packages;
4. provider setup, themes, semantic token definitions, component wrappers and
   approved assets;
5. nearby, repeated interface patterns and their source; and
6. official documentation for the installed version when supported behavior or
   customization remains uncertain.

Use installed source and version-matched official documentation. Do not fetch
mutable third-party skill files or generic design checklists at runtime: they
are unreviewed instructions that match neither this project nor its versions.

Before custom styling, follow Validation's
[styling exception rules](validation.md#styling-exceptions).
When changing style values, keep the authored unit as the paragraph "Keep the
authored unit" in
[Geometry](ui-geometry-validation.md#measure-relationships-not-declarations)
says; the measuring steps there belong to a requested review, audit or check.

## Classify the stack

### Styled design system

Use its supported components, semantic tokens, theme extension points and
responsive APIs for the visuals. Where a project wrapper exists, use it
before the underlying library. Resolve a demonstrated gap where the system is
meant to be extended (its theme, tokens or the project wrapper), within
authorized scope.

### Headless component library

The library decides the state, focus, keyboard, relationships and
announcements it implements; keep its structure and behavior. It supplies no
visual language: take appearance from project tokens, wrappers and
neighboring surfaces.

### Utility or application framework

Look for project tokens, presets, component layers and deliberate local
patterns. Where none exists, an installed UI layer's scale may supply coherent
values. A rendering framework such as React supplies no spacing or type scale
and no product hierarchy, meaning or visual direction.

### Platform UI stack

Platform components and conventions decide navigation, input, focus, scaling,
safe areas, adaptation and accessibility unless the product system does.
Web-only measurements and interactions do not transfer automatically.

### Multiple layers

Decide each concern separately: visuals, composite interaction, platform
scaling and supplied wording can come from different layers. Prefer the
highest abstraction the project has settled on. Installed layers alone do not
justify mixed APIs.

## Distinguish convention from accident

Read a pattern's source, count its uses and check whether it goes through the
project's wrappers and tokens. Padding that 12 of 14 cards take from the
`Card` wrapper is a convention; an inline `padding: 18px` on the other two is
an accident unless their source or a record gives a reason. A deliberate
current convention outranks a lower framework default. A copied exception,
stale screen or workaround alone sets no product policy.

## Handle true greenfield work

Derive unsettled navigation, groups and flow from user tasks, content
relationships and usage frequency under Quality. For unresolved visuals:

1. follow the user's brief and target platform conventions;
2. use framework defaults and scales where they provide compatible primitives;
3. when polished presentation is part of the outcome, name a deliberate visual
   direction grounded in the product domain and primary task. Carry it
   consistently through information hierarchy, density, typography, shape,
   imagery and interaction treatment, without defaulting to a prescribed
   palette or fashionable template;
4. choose only the minimum internally consistent, reversible values needed for
   the requested surface; and
5. keep those choices local unless the task explicitly creates or extends the
   canonical design system.

For multiple requested views, set shared values once at their nearest common
code location. Reuse an existing project structure, else the smallest shared
location those views need. Do not create a separate token registry or
design-system project, which would outgrow this local direction.

These choices define the requested surface, not a mature project-wide system.
Ask only when materially different directions would change the product
outcome.
