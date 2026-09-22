## How to use

Name Scoville UI for interface design, implementation, or audit work:

```text
Use Scoville UI to implement this settled settings-screen design through the product's existing component system. Cover loading, empty, error, and success states, then verify the rendered result responsively.
```

```text
Use Scoville UI to audit the current checkout for hierarchy, accessibility, keyboard use, responsive behavior, and recovery from errors. Do not change files.
```

```text
Use Scoville Design with Scoville UI. Design owns the workflow, hierarchy, typography, spacing, and design-system decision. UI implements that record through the existing framework and proves component states and interactions.
```

Explicit `$scoville-ui-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

### Source-first checks and consistency audits

Implementation groups related UI changes before validation. Complete the planned
edits, then check source, measure affected relationships and view the result.
Screenshots and measurements follow the completed batch, not each small edit.
If checks reveal defects, collect the related corrections and validate affected
concerns after that correction batch is complete.

Custom styling needs a concrete owner/API justification
before it is written. Authored units and expressions remain distinct from their
computed pixel values and visible geometry.

An ordinary request to check a page for consistency uses a read-only inventory
of its regions, variants and relevant states, including content below the fold.
Every entry maps to source, measurement and visual evidence or a named gap.
The visual routine compares intended edges, text position, apparent whitespace,
control interiors, icons, wrapping and clipping. Sampling limits remain explicit.
