# Claude Code and Codex CLI capabilities for PLAN-0019

Probed on 28 September 2026 in a disposable project with Claude Code 2.1.283 and `claude-opus-5-5`. A project `PreToolUse` Bash hook recorded its inputs. “Interactive” means a normal session; “headless” means `claude -p` launched from that session. These are observations of the named versions, not guarantees for later hosts.

## Claude Code

| Property | Version and probe | Observation and limit |
| --- | --- | --- |
| Interactive agent launch | 2.1.283, `Agent` without a foreground/background option | Launched in the background and returned a task completion notification. The interactive schema exposed `description`, `isolation`, `model`, `prompt` and `subagent_type`. |
| Nested agent | 2.1.283, `probe-nester` with `tools: Agent, Read, Bash` | The background agent received `Agent`, `Read`, `Bash` and `SubagentHandback`, launched `probe-leaf` at depth 2, received its completion and returned `LEAF-OK`. Metadata recorded `requestShape: background` and depths 1 and 2. Plugin-agent nesting was not tested. |
| Headless nesting | 2.1.283, `claude -p` with the same nester | The schema included `run_in_background`; the nester ran the leaf in the foreground. `subagent_stats` reported two foreground agents and maximum depth 2. |
| Continue an agent | 2.1.283, `SendMessage` to an `agentId` | Resumed a completed agent, which remembered its earlier token. Addressing by description failed with “No agent named ... is reachable.” |
| Model selection | 2.1.283, `Agent` with `model: "haiku"` | Transcript identified `claude-haiku-4-5-20251001`. Interactive `model` accepted family names `sonnet`, `opus`, `haiku`, `fable`, not pinned versions. |
| Frontmatter effort | 2.1.283, `effort: low` in project and plugin agents | Both transcripts recorded `low` and the hook reported `effort.level: low`; otherwise the session value was `medium`. Haiku reported null effort. `xhigh` and `max` came only from CLI help. Effort together with a model override was not checked. |
| Hook identity | 2.1.283, project `PreToolUse` Bash hook | Subagent input had `agent_id` and `agent_type`. `transcript_path` always pointed to the main transcript; `agent_transcript_path` was null. |
| Transcripts | 2.1.283, filesystem inspection | The main transcript was under `~/.claude/projects/<project-slug>/<session_id>.jsonl`. Nested and direct subagents were flat under `<session_id>/subagents/agent-<agent_id>.jsonl`; metadata included `parentAgentId`, `spawnDepth`, `requestShape` and `model`. |
| Context usage | 2.1.283, last assistant message | `message.usage` contained input, cache creation, cache read and output tokens. The transcript had no context-window field. Headless JSON output reported `modelUsage.<model>.contextWindow`. |
| Environment identity | 2.1.283, `env` in main session and subagent | Both had the main session's `CLAUDE_CODE_SESSION_ID` and `CLAUDE_EFFORT`. Neither exposed an agent ID or transcript path. Interactive sessions also set `CLAUDE_CODE_SESSION_ID`. |
| Model window | 2.1.283, `claude -p --model <family-or-id> --output-format json "/context"` | Returned formatted text with model ID and window, with no model turn or reported cost. Haiku showed 200k; Sonnet, Opus and Fable showed 1m. Values were rounded text, not a documented API. Hooks had no window field. |
| Fresh sessions | 2.1.283, `claude --help` and `claude agents --help` | Help listed `claude --bg`, `claude agents --json`, `attach`, `logs`, `stop` and `respawn`; `SendMessage` and `ListAgents` described cross-session reach. None of these session routes was run. |
| Dynamic Workflows | 2.1.283, `workflow-authoring` Skill lookup | Unavailable in the probe session; `agent()` options were not observed. |
| Model-triggered compaction | 2.1.283, headless request to call `compact` through `Skill` | Rejected: “compact is a built-in CLI command, not a skill.” No model tool was found that triggered compaction. The documented hook claim was not tested. |
| Caller-triggered compaction | 2.1.283, `claude -p --resume <id> "/compact"` | Produced no answer turn, but the summary used a model call. Transcript recorded `compact_boundary`, `trigger: manual` and `preTokens`. Only the prompt sender could invoke this route. |
| Content after compaction | 2.1.283, headless Skill with 40 rules, `/compact`, then a question without tools | The summary retained the tested task, open work, rule 37 and a memory word; the answer succeeded. It pointed to the earlier full transcript. Skill text was not reattached verbatim, while environment, project instructions and agent list were. One probe does not establish general recovery reliability. |
| Disabled model invocation | 2.1.283, `disable-model-invocation: true` in interactive and headless Skills | The interactive model declined to invoke it; headless Skill listing omitted it. A user could invoke it with a slash command. |
| Skill directory variable | 2.1.283, headless `/probe-skill` and plugin Skill calls | `${CLAUDE_SKILL_DIR}` expanded to the absolute Skill directory for project and plugin Skills, including one disabled for model invocation. Git Bash needed `MSYS_NO_PATHCONV=1` for slash arguments. Interactive behavior was not checked. |
| Plugin agents | 2.1.283, `--plugin-dir` with agent files | Loaded and answered as `probe-plugin:probe-plugin-agent`. `claude plugin validate` passed with an author warning. Documentation says plugin agents ignore `permissionMode`, `hooks` and `mcpServers`; this was not observed. Background `Agent` access inside a plugin agent was not checked. |
| Plugin Skill layout | 2.1.283, headless `--plugin-dir`, `skills: ["./packages/<name>"]`, layout `packages/<name>/<name>/SKILL.md` | User slash calls reached the visible and plugin Skills. Only the visible Skill appeared model-callable. The member Skill with disabled model invocation was not called. |
| Skill preload | 2.1.283, agent frontmatter `skills: [probe-skill]` with disabled model invocation | Not tested; the user excluded this second probe from acceptance. |
| Plugin CLI | 2.1.283, `claude plugin --help` | Listed validate, install, marketplace, list, enable/disable, update, uninstall, details, eval, tag, init and prune. |
| Plugin evals | 2.1.283, `claude plugin eval --help` | Help described `case.yaml` or `prompt.md` and grader inputs, model and cost options, and an optional comparison without the plugin. Without `--no-publish`, it publishes an HTML report. No eval was run. |

## Codex CLI

The first probe used `codex-cli 0.154.0`; the second used `0.158.0-alpha.2.1`. The executable path depends on the installation. Observations below are from 0.158 unless marked otherwise. The earlier raw data were overwritten, so 0.154 observations come from the first analysis. Probes ran in an empty directory and asked the model to attempt writes.

| Property | Version and probe | Observation and limit |
| --- | --- | --- |
| Read-only execution | 0.158, `codex exec - --sandbox read-only --json --skip-git-repo-check -C <dir> -c model_reasoning_effort=low` | Prompt came from stdin. Shell write failed, no file appeared, and exit was 0. The 0.154 probe also blocked the write. |
| Read-only patch | 0.158, same call asking for `apply_patch` | Rejected with “patch rejected: writing is blocked by read-only sandbox.” |
| JSONL events | 0.158, `--json` | Observed `thread.started` with `thread_id`, `turn.started`, item events with message/command/web-search types, and `turn.completed` usage fields. The answer was the last `agent_message`. |
| Errors | 0.158, resume an unknown session | Exit 1 without a JSONL line; reason only on stderr. No `error` or `turn.failed` event was observed. Warnings on stderr also occurred with exit 0. |
| Read-only resume | 0.158, `codex exec resume <id> - --json --skip-git-repo-check -c sandbox_mode="read-only"` | Write failed, no file appeared, and the `thread_id` stayed the same. |
| Resume without override | 0.158, omit `-c sandbox_mode=...` after a read-only start | Write succeeded. Resume did not inherit the starting sandbox. |
| Resume working directory | 0.158, same resume route | Resume had no `-C`; use the process working directory. The 0.154 probe exited 2 for `-C`. |
| Ephemeral execution | 0.158, `exec --ephemeral` | Returned a `thread_id`, but resuming it failed because no rollout was saved. |
| Ignore user config | 0.158, `exec --ignore-user-config` | Execution worked and sign-in remained available. |
| Web search | 0.158, search request with `--ignore-user-config` | Search was available by default. `-c web_search="disabled"` disabled it; live-search options enabled it. `exec` had no `--search` flag. |
| Search after resume | 0.158, start with search disabled, then resume with and without a live override | Neither resume searched. Search behavior was set at start in the observed route. |
| External tools | 0.158, ask the read-only model to list tools | It listed app tools with potential external effects. The shell sandbox did not test those effects. `--disable apps` removed them; collaboration tools remained visible even with `--disable multi_agent`. |
| Resume tool restrictions | 0.158, start with `--disable apps --ignore-user-config --ignore-rules`, then resume | Without repeating restrictions, app and user MCP tools returned. Repeating them kept those tools absent. |
| Subagent shell write | 0.158, spawn a subagent from a read-only session with a write assignment | Subagent reported the shell write blocked by read-only policy; no file appeared. External tools were not exercised. |
| MCP server | 0.158, `codex --help` | No `mcp-server` command appeared in the command list. |
| CLI options | 0.158, `codex exec --help` and `codex exec resume --help` | `exec` exposed sandbox, directory, model, ephemeral, config and feature flags. Resume had model, config and feature flags but no sandbox or directory flag; use `-c sandbox_mode=...` and process cwd. |

## Consequences for PLAN-0019

- ADR-0104: the old documentation blocker did not hold in 2.1.283, but background nesting remained undocumented and unverified for plugin agents. The main session coordinates without rollover; workers and reviewers stay at depth 1.
- ADR-0105: model selection and frontmatter effort worked, including in a plugin agent. Haiku reported null effort. W-003 must check effort by model family. Plugin agents and Skills loaded from the package layout.
- ADR-0107: resolve the Codex path, repeat every required restriction on every resume, omit `-C` on resume and use the process directory. Disable web search at start and app tools explicitly. `--ephemeral` rules out follow-up. Treat exit 0 plus a nonempty final `agent_message` as success.
- Context checkpoint: a subagent finds its transcript through `CLAUDE_CODE_SESSION_ID` and its assignment file; usage comes from that transcript, the window from `/context` under ADR-0114. W-006 still needs a live subagent check of this route.