## What it enforces

- **One planning owner.** Existing repository instructions and records stay authoritative.
- **Records a worker can use.** Each fact has one owner. Goals describe the current target, Work Items describe resumable outcomes, and numbered Steps name the actual work.
- **Check before starting.** Compare the next item with current sources and relevant completed work. Repair stale assumptions before executing them.
- **One active item.** The Plan names the current work and its first unfinished action.
- **Durable changes of direction.** Queue additions without losing current work. Preserve explicit stops, priorities and requested returns after a redirect.
- **Evidence before completion.** A file and a green structure check do not prove that the requested result works.
- **Explicit decisions.** Record human choices without asking twice. Keep inferred choices proposed until accepted.
- **No planning for the sake of planning.** Editing the Plan changes its records directly. It does not create another Work Item to maintain them.

- When Workflow is active, Steps expose the scope and boundaries needed for dispatch. The coordinator chooses the route. Plan can retain an explicit executor choice, but does not quietly turn a small-looking edit into low-risk work.

- The complete contract, including dispatch projections and direct-edit limits, is in [SKILL.md]({{ var: contract_url }}).

Let the current run finish before editing the same records elsewhere. Plan does
not lock files. Concurrent changes require reconciliation.
