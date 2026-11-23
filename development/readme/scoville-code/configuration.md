## Configuration

You can edit the bundled [conventions](scoville-code/references/project-conventions.md),
but the next update may overwrite them. To keep your own:

1. Create a Markdown file outside the Skill installation.
2. Reference it from your global or project
`AGENTS.md` (Codex) or `CLAUDE.md` (Claude Code), for example:

```markdown
### Greenfield project conventions

For the initial organization of a wholly new project, first follow this
project's explicit requirements, then read `docs/project-conventions.md`
for my additional folder and filename conventions. Use Scoville Code's
defaults only for choices neither source settles. Do not apply this
fallback to additions or refactors in an existing project.
```

Relative paths resolve from the file that references them. The agent reads
the referenced file and tells you if it can't find it.
