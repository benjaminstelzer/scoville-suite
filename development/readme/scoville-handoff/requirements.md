## What it enforces

- **Explicit transfer.** A handoff starts when you request one. Preparing it is
  read-only and does not advance the task.
- **Faithful context.** Decisions, permissions, ownership and blockers survive
  the transfer. Existing approval is preserved within its scope. Unknown
  results stay unknown, and secrets stay out, including quoted secrets.
- **A useful next action.** The prompt tells the next session where to resume
  and how to recognize completion.

Keep preferences distinct from binding requirements. The receiving session
still needs the exact permissions and acceptance criteria for its next action.

See the [full instructions]({{ var: contract_url }}).
