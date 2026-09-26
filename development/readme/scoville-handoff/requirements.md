## What it enforces

- **Explicit transfer.** A requested handoff produces one continuation prompt.
- **Usable context.** Material facts from the conversation and named sources
  appear in the prompt, including blockers and incomplete work.
- **Preserved authority.** Permissions, file ownership, user changes and
  boundaries on commits, publication or destructive actions remain explicit.
- **Honest state.** Unobserved results remain unknown. Secrets stay out.
- **Actionable continuation.** The first Resume Step gives the next safe action;
  the last defines observable completion.
- **A faithful snapshot.** Creating the handoff reads and describes the task
  without editing, testing or advancing it.

The complete contract is in [SKILL.md]({{ var: contract_url }}).
