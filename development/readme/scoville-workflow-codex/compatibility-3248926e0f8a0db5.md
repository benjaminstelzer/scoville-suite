## Compatibility

Requires Codex desktop, a saved local project, native task creation, waiting,
messaging and archival controls, access to the task's own `CODEX_THREAD_ID`,
and Scoville Plan v1.8.0 or a compatible source_text selector. Python 3.11+ runs the deterministic helpers.
There is no CLI or Claude Code execution path.

Tasks must share the existing checkout. If the host cannot provide that,
Workflow asks for a decision instead of silently creating another workspace.
Measured rollover uses native `token_count` data when available. Missing or
contradictory measurements do not by themselves block valid bounded work.

Native approval can hold a cross-task message pending. Workflow waits without
polling or duplicate delivery. A definite result-delivery failure still leaves
the child's validated final result available to the coordinator's recovery path.
