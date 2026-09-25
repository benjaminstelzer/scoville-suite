## Compatibility

Requires Codex desktop, a saved local project, native task creation, waiting,
messaging and archival controls, access to the task's own `CODEX_THREAD_ID`,
and Scoville Plan v1.8.0 or a compatible source_text selector. Python 3.11+ runs the deterministic helpers.
There is no CLI or Claude Code execution path.

Tasks must share the existing checkout. If the host cannot provide that,
Workflow asks for a decision instead of silently creating another workspace.
Measured rollover uses native `token_count` data when available. Missing or
contradictory measurements do not by themselves block valid bounded work.

Native approval can hold a cross-task message pending. Keep that task handle
and wait without duplicate sends. The coordinator collects results from the
exact completed task with `read_thread`, preserving the original line breaks.
The compact `wait_threads` snapshot is not the input to the result parser.
No separate result-delivery message is required.
