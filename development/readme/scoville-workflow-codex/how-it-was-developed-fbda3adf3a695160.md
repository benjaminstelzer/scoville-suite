## How it was developed

Workflow grew out of a CLI-based Scoville workflow whose communication and
supervision added work of their own. The native version kept Plan ownership,
routing, review and rollover, while moving execution into ordinary Codex tasks.

Later task-history audits exposed repeated dispatch text and unnecessary full
rule reads. Dispatch now separates the payload from its receipt, and the
operations contract loads by phase. Contract tests and focused model cases
check those paths. They do not settle the host-level limits listed below.

The current source belongs to Scoville Suite. Common helpers are built into the
package, so an installation does not depend on the development workspace.
