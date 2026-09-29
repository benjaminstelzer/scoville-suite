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

### Your own conventions

You can edit the bundled reference, but the next Skill update may overwrite
it. For conventions you want to keep, maintain a Markdown file outside the
Skill installation and reference it explicitly from your global or project
`AGENTS.md` (Codex) or `CLAUDE.md` (Claude Code). For example, add this to
the file at the project root:

```markdown
### Greenfield project conventions

For the initial organization of a wholly new project, first follow this
project's explicit requirements, then read `docs/project-conventions.md`
for my additional folder and filename conventions. Use Scoville Code's
defaults only for choices neither source settles. Do not apply this
fallback to additions or refactors in an existing project.
```

Then create the file with your conventions. Relative paths are resolved from
the `AGENTS.md` or `CLAUDE.md` that references them, and a personal file
shared across projects can use an absolute path. The agent reads the
referenced file and tells you if it can't find it.

Project-specific instructions and framework requirements still apply.
