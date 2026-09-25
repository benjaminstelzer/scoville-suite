# Scoville Ask for Codex

A second opinion should give you another assessment, not repeat your own reasoning back to you. Scoville Ask sends a self-contained question to the advisers you choose and brings their answers back to the original task. One configuration replaces the five separate Ask Skills.

## How it works

- Select one or more advisers, each with its own model, reasoning effort and native Codex or Claude CLI route.
- Send independent questions, retain task or session handles and continue the same consultation when needed.
- Use separate reviews for review requests. For general questions, combine independent answers into a synthesis.

## What it enforces

- Advisers inspect and answer. Changes remain with the calling task.
- Native tasks use `Ask <model> · <original task title>`. Identity comes from task IDs and consultation references.
- Invalid settings, unavailable models and failed advisers remain visible. There is no silent replacement model or route.

Native advisers follow a read-only instruction, but the host does not add a
technical write barrier when creating their task. Claude permits Read, Grep and
Glob by default. Enable `claude.web_tools` explicitly for WebSearch and WebFetch.
Claude model communication remains online even when these web tools are off.

## What it costs

- Each adviser adds a separate model call and waiting time. Native tasks use the connected Codex account, and Claude CLI uses its own configured account.
- You maintain the adviser configuration and review disagreements. More advisers do not guarantee a better answer.

## How it was developed

- Consolidated the native and Claude adapters from the previous Ask Suite.
- Functional and instruction checks use an independent SOL 6 Medium subagent. The development record distinguishes simulated host calls from actual provider checks.

## Compatibility

**Codex online.** Requires Codex desktop with native task controls for native advisers, a verified calling task and saved project, network access, and Python 3.11 or newer. Use a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0 or newer. Tests performed are recorded separately from this minimum.

The model catalog comes from the current Codex app-server through `model/list`. A listed model still needs to be accepted by the task host. Native third-party models require a suitable provider connection, such as EasyCLIProxy where configured. The Claude CLI route requires installed, authenticated Claude Code. Opus 5.5 requires version 2.1.280 or newer. See “How to Ask with Claude Code” for setup.

The Python helpers are required. A missing interpreter or helper failure has no manual replacement route. Tasks use the host’s normal sidebar sorting.

Ask is also available as a standalone Skill from
[scoville-ask-for-codex](https://github.com/benjaminstelzer/scoville-ask-for-codex).
Its standalone package works independently. Installing the complete suite uses
the suite packages and includes every member.

Python 3.11 or newer is required. Choose a working interpreter once for the
session and use it wherever examples say `python`. Verify its actual version
with `--version`: on Windows try `py -3`, then `python`; on macOS/Linux try
`python3`. A Windows Store alias that opens the Store or returns no usable
version is not an interpreter. Python 3.9/3.10 is too old for these helpers;
macOS does not imply any particular installed Python version. Quote script
and project paths, including paths without spaces in the current example.
If Python is missing, use the authorized normal package manager or official
installer and verify its version. Report installation or permission failures.
Project settings use `.scoville/config.json`. Follow the selected installation
or migration instructions. A helper error has no manual fallback.

This package requires every Skill included in this suite to be installed and
enabled. Partial installation is not supported. Skills keep their own task
scope and invocation rules; Workflow still requires an explicit request.

## Install

### Install this Skill

Install this Skill as part of the complete suite from
[the suite's own packages](https://github.com/benjaminstelzer/scoville-suite-for-codex/tree/main/packages).
Every member must be installed and enabled. Do not fetch or substitute packages
from individual Skill repositories. If any member is missing or incompatible,
report the incomplete installation rather than claiming the suite is ready.

The host needs permission to write to its Skills directory. See the
[Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
for host-specific locations.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite-for-codex).
Install its released Skill packages, not development templates.

## How to use

Ask naturally, for example:

```text
Use scoville-ask-for-codex to ask SOL for an independent review of this patch.
```

```text
Ask Fable and Claude independently how they would approach this problem, then compare their answers.
```

### Configure defaults

`config.default.json` beside the installed `SKILL.md` owns the shipped defaults.
Save project choices under `ask` in `.scoville/config.json` at the project root.
Missing values use the shipped defaults. Reading settings creates no file.
Explicit requests override these values for that call without saving them.

The `astra`, `sol`, `claude` and `fable` presets resolve named requests. The
shipped `advisers` list applies when you do not name an adviser. Every preset's
model, effort and route is configurable. Current defaults:

```json
{
  "schema_version": 1,
  "advisers": ["astra"],
  "presets": {
    "astra": {"route": "native", "model": "gpt-6-astra", "effort": "high"},
    "sol": {"route": "native", "model": "gpt-6-sol", "effort": "high"},
    "claude": {"route": "claude-cli", "model": "claude-opus-5-5", "effort": "high"},
    "fable": {"route": "claude-cli", "model": "claude-fable-5-1", "effort": "medium"}
  },
  "claude": {
    "max_budget_usd": 10,
    "session_persistence": true,
    "customizations": false,
    "timeout_seconds": 3600,
    "web_tools": false
  }
}
```

For example, this `.scoville/config.json` selects SOL and Fable by default and
changes only SOL's effort:

```json
{
  "ask": {
    "advisers": ["sol", "fable"],
    "presets": {"sol": {"effort": "medium"}}
  }
}
```

Objects merge by field. The adviser list replaces earlier selections. Higher-layer preset fields also override inherited inline adviser fields; inline adviser fields win over presets within the same layer. An
explicit per-call model or effort wins without changing the saved defaults.
Follow-ups retain their original settings unless explicitly changed. For a
custom adviser, supply an ID, route, exact model and effort in `advisers`.
See the installed configuration reference for helper inputs and migration.

### How to Ask with Claude Code

1. Install [Claude Code](https://code.claude.com/docs/en/setup) if needed. Open a new terminal or PowerShell window; the folder does not matter.
2. Run `claude --version`. Opus 5.5 needs **2.1.280 or newer**. For an older version, run `claude update`, then check again. Keep running Claude sessions open.
3. Run `claude auth login` and complete sign-in in your browser. Run `claude auth status` to check that you are signed in.
4. In Codex with this Skill installed, ask: **“Ask Claude to review this change.”** The imported defaults above determine the model and effort. Change the `ask` settings in `.scoville/config.json` or name another model or effort in the request.

If ASK reports an expired OAuth session, repeat step 3 and retry. An old CLI can reject the correct model ID; repeat step 2 instead of substituting a model.

## Sources

- [Codex App Server and model/list](https://learn.chatgpt.com/docs/app-server#models).
- [Codex Skills](https://learn.chatgpt.com/docs/build-skills).
- [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference).

## License

MIT. See [LICENSE](LICENSE).
