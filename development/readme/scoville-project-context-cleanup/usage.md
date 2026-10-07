## How to use

Ask the agent to add or revise project rules:

```text
Add this to the project rules: edit schemas/ and regenerate docs/generated/.
```

Or name `AGENTS.md`, `CLAUDE.md` or `PROJECT_INDEX.md` explicitly. Requests such as
“Füge das den Projektregeln hinzu” use the same scope.
At a clear project root, this can create a missing
`AGENTS.md`, or `CLAUDE.md` on a Claude host. A missing index
follows the requested format. A text addition alone does not create a Plan.

For an explicit call, use `$scoville-project-context-cleanup`. A file mention,
ordinary README edit or routine Plan progress does not request cleanup.
