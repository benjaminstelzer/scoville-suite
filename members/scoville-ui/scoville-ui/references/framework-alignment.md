# Framework Alignment

Use this reference to determine who owns a UI decision. Framework fidelity is
not passive obedience to every default; it is changing the interface through
the canonical layer that the product has chosen.

## Contents

- Find the owners
- Classify the stack
- Distinguish convention from accident
- Handle true greenfield work
- Resolve accessibility conflicts

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

Apply the entrypoint's concern-level authority order. Preserve approved product
decisions; resolve implementation conflicts under its Workflow rather than
silently redesigning.

Do not fetch mutable third-party skill files or generic design checklists at
runtime. Prefer installed source and version-matched official documentation.

Before custom styling, follow Validation's
[styling exception contract](validation.md#styling-exceptions).
When changing style values, follow the
[authored-unit contract](ui-geometry-validation.md#measure-relationships-not-declarations).

## Classify the stack

### Styled design system

Examples include component systems that supply visual defaults, theme tokens,
variants, and layout conventions. Treat their supported components, semantic
tokens, theme extension points, and responsive APIs as the visual owner. Reuse
project wrappers before reaching for the underlying library directly.

Do not replace the system's spacing, typography, shape, elevation, color, or
breakpoint language with personal defaults. If a local need reveals a genuine
system gap, extend the canonical owner rather than building a parallel layer in
one feature.

Change a canonical component or design-system rule only within the authorized
task. If it would alter a settled product decision or expand scope, report the
specific conflict and obtain the missing decision before that dependent change.

### Headless component library

Treat the library as the owner of the behavior and semantics it implements:
state machines, focus movement, keyboard interaction, relationships, and
announcements. It does not supply a visual language unless the project has
added one around it. Derive appearance from project tokens, wrappers, and
neighboring surfaces while preserving the library's supported structure and
behavior.

### Utility or application framework

A rendering framework, CSS utility library, module system, or routing framework
does not by itself define the product's design language. Look for project
tokens, presets, component layers, and deliberate local patterns. When no such
owner exists and an installed UI layer supplies a value scale, that scale may
supply coherent implementation values. A rendering framework such as React
does not supply a spacing or typography scale. Neither settles hierarchy,
product meaning, or visual direction.

### Platform UI stack

Native mobile, desktop, and terminal UIs inherit platform conventions for
navigation, input, focus, scaling, safe areas, window or viewport adaptation,
and accessibility. Use platform components and adaptation mechanisms unless the
canonical product system explicitly owns the concern. Do not translate web-only
measurements or interaction assumptions into another platform.

### Multiple layers

Assign each concern independently. A styled component system may own visuals,
a headless primitive may own a composite interaction, the platform may own text
scaling, and supplied content owns visible wording. Prefer the highest canonical layer
that intentionally abstracts the lower one. Do not mix APIs from several layers
merely because they are all installed.

## Distinguish convention from accident

Apply the entrypoint's LOCAL and UNKNOWN EXCEPTION rules. Inspect a pattern's
source, frequency and relationship to canonical wrappers/tokens; a copied
exception, stale screen or workaround is not product policy. A deliberate
current convention is project-level evidence above a lower framework default.
Normalize only an established accidental/stale exception through its owner;
uncertain or conflicting intent requires inspection or the remaining choice.

## Handle true greenfield work

For unsettled concerns of the requested surface, derive navigation, content
groups and task flow from user tasks, content relationships and usage frequency.
Apply Quality's principles even without a supplied product structure. Preserve
settled decisions; this does not authorize new features or a wider redesign.

For an unresolved visual owner, apply the entrypoint's GREENFIELD rule through
the bounded procedure below.

When polished presentation is requested, the requested surface owns a
deliberate local direction. Framework defaults may supply compatible primitives
and scales, but they never become the visual owner.

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

Do not pretend a single screen's choices are a mature project-wide system. Ask
only when materially different visual directions would change the product
outcome.

## Resolve accessibility conflicts

Apply the entrypoint's ACCESSIBILITY and OWNER LIMIT rules through supported
framework/project mechanisms. Name the exact canonical owner and unmet floor;
only informed acceptance of a non-binding limitation may waive that target.
System, safety and legal requirements remain binding.
