## Compatibility

Designed for Codex and Claude Code.
Requires reference access and the project's framework tools. Geometry
proof needs DOM or equivalent measurement, visual proof needs viewed renders,
and interaction proof needs an interactive runtime. No mandatory network.
The bundled size checker uses Python 3.11+; manual fallback is available only
without suitable Python, not after helper errors.
Tested with `gpt-6.1-sol` and Claude Opus 5.5; these models at medium reasoning effort are the minimum,
because lower effort skips steps more often.
