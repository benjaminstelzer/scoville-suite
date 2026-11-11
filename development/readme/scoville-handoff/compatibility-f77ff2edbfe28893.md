## Compatibility

Developed for Codex and Claude Code with read access to the task's
relevant sources. Python 3.11+ supports the bundled size checker; a manual
fallback is available only when suitable Python is unavailable, not after a
helper failure.
Read-only Git inspection is optional. Handoff requires no network access or
subagents.
Tested with `gpt-6.1-sol` and Claude Opus 5.5; these models at medium reasoning effort are the minimum,
because lower effort skips steps more often.
