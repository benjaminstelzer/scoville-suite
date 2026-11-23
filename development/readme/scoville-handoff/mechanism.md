## How it works

- It starts when you ask for a handoff. A summary, a full context window or
  the end of a session isn't a request.
- It uses what the conversation already established and reads only the
  sources named there. Nothing new gets researched.
- Writing the handoff leaves the task alone: no edits, builds or tests. The
  prompt shows the state at the moment you asked.
- Decisions, permissions and blockers carry over as they were. What nobody
  knows is written as `unknown`, not guessed. Secrets become `[redacted]`.
- The prompt ends with one to three next steps. The receiving agent checks
  the current state before it acts and doesn't take the handoff as new
  permission.
