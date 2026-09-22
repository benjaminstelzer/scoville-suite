## What it enforces

- **Outcome over ceremony.** Plans, tests, docs, and refactors support the
  requested behavior. Producing them is not completion by itself.
- **Canonical ownership.** The change fits the project's existing architecture,
  records, terminology, and workflow instead of creating a second owner.
- **Proportionate risk.** Small reversible work stays small. Destructive,
  public-facing, security, data, or release work receives stronger gates.
- **Evidence before claims.** Checks prove only what they observed. A failed
  tool is not silently promoted to a passing product.
- **Root-cause correction.** The agent changes approach after repeated failure
  instead of repeating the same unsuccessful fix.
- **Navigable code structure.** Hand-written source files use a default ceiling
  of 2,000 physical lines with project priority and concrete exceptions. Domain
  ownership, module boundaries, dependency direction, generated sources, and
  resource cleanup remain explicit without forcing one architecture.
- **Material questions only.** It asks when a missing choice changes behavior,
  authority, cost, reversibility, or scope, not for details the code settles.
- **Complete handoff.** The final report names changed behavior, relevant
  validation, unresolved failures, and relevant repository state.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/blob/main/scoville-code-anti-ai-slop/SKILL.md).
