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
- **Navigable code structure.** Existing work follows project conventions and
  surrounding module boundaries. Greenfield work starts with the smallest
  coherent responsibility-based layout. A 2,000-line default ceiling remains
  a backstop with concrete exceptions, never an architecture target.
- **Material questions only.** It asks when a missing choice changes behavior,
  authority, cost, reversibility, or scope, not for details the code settles.
- **Defaults for a wholly new project.** Project instructions come first.
  Only complete greenfield work uses the stack-specific conventions in the
  Skill's `references/project-conventions.md`. Keep personal overrides outside
  the installed Skill and reference them explicitly from `AGENTS.md` so Skill
  updates do not replace them. Existing projects keep their organization.
  The [customization guide](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop#your-own-conventions)
  explains paths, precedence and update behavior with a copyable example.
- **Complete handoff.** The final report names changed behavior, relevant
  validation, unresolved failures, and relevant repository state.

- The complete contract is in [SKILL.md]({{ var: contract_url }}).
