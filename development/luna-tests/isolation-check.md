# Evaluation isolation check

After code-12 changed the host clipboard, native tool-capable Luna tests stopped.
No test child remains live. SOL performed read-only runtime inspection; no model
or provider call was made during this check.

Observed CLI: 0.155.0-alpha.9.2. Per-run feature overrides can disable shell,
apps, browser/computer use, plugins and ordinary hooks. They do not establish a
complete tool deny-list. SOL observed that `mcp_servers={}` left bootstrap MCP
servers present; node_repl required an explicit enabled=false override.

Generated local ThreadStartParams schema documents `environments: []` as
disabling environment access. It exposes no global tool-choice/deny field;
dynamicTools adds tools rather than replacing built-ins. This is a candidate,
not demonstrated isolation. Read-only filesystem policy alone does not prove
clipboard or other host effects are blocked. No global config was changed.

Sources: local `codex exec --help`, `codex features list`, generated app-server
schema under workspace temp/2026-09-21-suite-luna-evaluation/isolation-schema;
https://developers.openai.com/codex/config-reference/ .

Resume requires an isolated disposable test environment or a verified runtime
that denies host-mutating tools while retaining package reads and actual Luna
Medium evidence. Do not replace this with more prompt warnings or mark
unexecuted cases passed. Infrastructure setup beyond the current workspace
needs user direction. Preserve all frozen inputs and recorded failures.
