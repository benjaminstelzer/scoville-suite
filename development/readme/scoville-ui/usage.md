## How to use

```text
Use Scoville UI to implement this settings screen with the existing component system. Cover its states and verify the rendered interactions.
```

```text
Audit the checkout interface for keyboard use, responsive behavior, accessibility and error recovery. Report findings without changing files.
```

### Checking the interface

Use the styling options the component supports. If custom CSS is needed,
explain why. Keep CSS values and the sizes actually rendered on screen apart.

Make related edits together and review the final source diff. Select evidence
for the claim: a concept needs design reasoning, spacing needs measurements
against an independent target, appearance needs a viewed render, and behavior
needs actual interaction. Keep missing evidence explicit. After corrections,
refresh only the affected checks.

A consistency audit lists regions, variants and states, including content
below the fold and in relevant hidden or virtualized regions. Each finding
points to the applicable evidence or explains what couldn't be checked. Look at
alignment, text, whitespace, the inside of controls, icons, wrapping and clipping, and say
which parts of the interface were checked. A sample supports a scoped result,
not an unqualified whole-page pass.
