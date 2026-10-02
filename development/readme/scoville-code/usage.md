## How to use

```text
Use Scoville Code to analyze this codebase for correctness, ownership and missing validation. Report prioritized findings.
```

```text
Use Scoville Code to fix the failing checkout total when a coupon and free shipping combine. Find the cause, change the responsible code and verify the corrected case.
```

```text
Use Scoville Code to add CSV export to the orders page. Follow the existing structure and verify the exported fields and values against a representative local test order.
```

### Starting a new project

In a brand-new project, Scoville Code falls back on
[`references/project-conventions.md`](scoville-code/references/project-conventions.md)
for anything the project instructions leave open. Those defaults follow the
language and framework, with a small `src/`, `tests/`, `docs/` and `scripts/`
layout where it fits. Directories are only added when they're needed, and
tests can sit next to the code if the framework expects that. Existing
projects keep their organization, even during refactors or when modules are
added.
