## How to use

```text
Use Scoville UI to implement this settings screen with the existing component system. Cover its states and verify the rendered interactions.
```

```text
Audit the checkout interface for keyboard use, responsive behavior, accessibility and error recovery. Report findings without changing files.
```

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
