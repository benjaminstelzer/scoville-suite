## How to use

Ask the agent to add or revise project rules:

```text
Add this to the project rules: edit schemas/ and regenerate docs/generated/.
```

Or name `AGENTS.md` or `PROJECT_INDEX.md` explicitly. Requests such as
“Füge das den Projektregeln hinzu” use the same scope.

For an explicit call, use `$scoville-project-context-cleanup`. A file mention,
ordinary README edit or routine Plan progress does not request cleanup.
