## How it works

- Plan keeps a Plan, its Work Items and your Decisions as Markdown files in
  the repository: `PROJECT_INDEX.md`, `docs/plans` and `docs/decisions`. A
  Work Item has ordered Steps with a status, dependencies and acceptance
  criteria.
- Before the next item starts, the agent checks the current sources and not
  only the record.
- Progress is recorded as it is observed. Finished means the acceptance was
  checked.
- Confirmed choices become Decisions. Open questions stay proposals and block
  only the work that depends on them.
- A bundled validator checks structure and references. It can't tell whether
  an acceptance result is true.
- Edit Plan records from one session at a time.
