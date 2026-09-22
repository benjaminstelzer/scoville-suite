## Current Codex lifecycle limitation

On 2026-09-19, the tested Codex Desktop tool surface exposed `interrupt_agent`
but no control whose documented semantics close a completed subagent and free
its slot. Interrupting stops the current turn while leaving the agent available. Other
Codex hosts may expose an equivalent control under a different name. Brainstorm
therefore discovers lifecycle controls by documented behavior, reports unavailable
cleanup before isolated generation, and keeps generators, landscape work, and any
critic within observable capacity. Archiving, deleting a task, or killing a
process is not assumed to free a subagent slot either.

