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

For a wholly new project, Scoville Code uses
[`references/project-conventions.md`](scoville-code/references/project-conventions.md)
for choices the project instructions leave open. Its defaults follow the
language and framework, with a small `src/`, `tests/`, `docs/` and `scripts/`
layout where appropriate. Directories are added when needed. Tests may sit
beside code when the framework expects it. Existing projects retain their
organization, including during refactors or module additions.

### Your own conventions

You can edit the bundled reference, but a Skill update can replace that edit.
For conventions you want to keep across updates, maintain a Markdown file
outside the Skill installation and explicitly reference it in your global or
project `AGENTS.md` (Codex) or `CLAUDE.md` (Claude Code). For example, add
this to the applicable file at the project root:

```markdown
### Greenfield project conventions

For the initial organization of a wholly new project, first follow this
project's explicit requirements, then read `docs/project-conventions.md`
for my additional folder and filename conventions. Use Scoville Code's
defaults only for choices neither source settles. Do not apply this
fallback to additions or refactors in an existing project.
```

Create the file with your conventions. Relative paths resolve from the
referring `AGENTS.md` or `CLAUDE.md`. A shared personal file can use an absolute path.
The agent reads the explicitly referenced file and reports it if unavailable.

Project-specific instructions and framework requirements still apply.
