## Configuration

### Your own conventions

You can edit the bundled [conventions](scoville-code/references/project-conventions.md),
but the next Skill update may overwrite them. To keep your conventions:

1. Create a Markdown file outside the Skill installation.
2. Reference it explicitly from your global or project
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

3. Resolve relative paths from the referencing `AGENTS.md` or `CLAUDE.md`.
   A personal file shared across projects can use an absolute path.

The agent reads the referenced file and tells you if it can't find it.

Project-specific instructions and framework requirements still apply.
