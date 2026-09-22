## How it was developed

- Workflow grew out of a CLI-based Scoville workflow whose communication and supervision added work of their own.
- The native version kept Plan ownership, routing, review and rollover, while moving execution into ordinary Codex tasks.
- Real-project histories are analyzed alongside results to identify failures and unnecessary context use.
- Targeted simulation and optimization workflows inform revisions. Changes are retained only when the required behavior survives.

- Beta testing still needs to cover automatic context compaction immediately after handoff and waiting beyond the host's maximum wait duration.
