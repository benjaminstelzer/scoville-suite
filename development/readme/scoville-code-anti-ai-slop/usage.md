## How to use

```text
Use Scoville Code to analyze this codebase for correctness, ownership and missing validation. Report prioritized findings.
```

```text
Analyze this codebase for defects and hidden failure paths. Support findings with code evidence and keep the analysis read-only.
```

### Starting a new project

Project instructions come first. Scoville Code uses its organization fallback
only when you start a wholly new project, and only for choices your instructions
have not already settled. Adding a module to an existing project is not a fresh
start. Neither is a refactor or a missing naming rule.

The defaults live in
[`references/project-conventions.md`](scoville-code-anti-ai-slop/references/project-conventions.md)
inside the installed Skill. They follow the selected language and framework:
Python modules, Angular components and PSR-4 classes have different naming
rules for a reason. Where the ecosystem leaves the choice open, the fallback
uses a small `src/`, `tests/`, `docs/` and `scripts/` layout. Directories appear
when they have a purpose, not as an empty scaffold. Tests can live beside the
code when the framework expects that.

### Your own conventions

You can edit the bundled reference, but a Skill update can replace that edit.
For conventions you want to keep across updates, maintain a Markdown file
outside the Skill installation and explicitly reference it in your global or
project `AGENTS.md`. For example, with an `AGENTS.md` at the project root:

```markdown
### Greenfield project conventions

For the initial organization of a wholly new project, first follow this
project's explicit requirements, then read `docs/project-conventions.md`
for my additional folder and filename conventions. Use Scoville Code's
defaults only for choices neither source settles. Do not apply this
fallback to additions or refactors in an existing project.
```

Create the referenced file with your actual preferences. Relative paths resolve
from the directory containing the referring `AGENTS.md`; a shared personal file
can instead use an explicit absolute path available on that machine. The Skill
does not search your computer for convention files. If the required file cannot
be read, the agent reports that input gap before making dependent choices.

Your file is maintained separately from the installed Skill, so replacing the
Skill does not replace it. Project-specific instructions still take precedence
over generic personal defaults unless you explicitly choose otherwise. Required
framework paths and loading rules remain binding. Naming preferences do not
grant new permissions or extend the fallback to existing projects.
