---
name: scoville-setup
description: Show or change the selected project's Scoville Ask and Workflow settings. Use for saved models, effort, Claude limits and context rollover thresholds. Excludes running workflows, installations, updates and monitoring.
---

# Scoville Setup

All Skills included in this suite must be installed and enabled. Use the
applicable owner without checking sibling availability. Load only instructions
needed for the task. Explicit invocation gates and user exclusions still apply.

Manage `.scoville/config.json` in the selected project root. Its values override
the imported Skill defaults per field. There is no personal settings layer or
parent-directory search. This Skill is supplied only in the Codex Suite.

Use the project's known absolute root. Ask for the root only if it is unknown.
Before the first helper call, choose an available Python 3.11+ interpreter
(`py -3.11` or a newer installed version on Windows, `python3` or `python`
elsewhere). Verify its version and use that executable for all helper commands.
The `python` examples below stand for this verified interpreter.

Run the bundled helper with Python 3.11+:

```text
python "<setup-skill-directory>/scripts/setup.py" show --project-root "<project-root>"
```

Show reads and validates settings without creating a file. Explain the relevant
effective values returned by the helper. Defaults are imported from Ask's
[defaults](assets/ask.default.json) and Workflow's [defaults](assets/workflow.toml).
Never maintain another copy of their values in these instructions.

For an explicit request to save settings, pass only the requested fields as a
JSON object on stdin to:

```text
python "<setup-skill-directory>/scripts/setup.py" set --project-root "<project-root>"
```

The object uses `ask` and/or `workflow` sections. Ask supports `advisers`,
`presets` (model, effort, route and optional name) and `claude`
(`max_budget_usd`, `session_persistence`, `customizations`, `timeout_seconds`,
`web_tools`). Workflow supports `execute` and `review` model/reasoning pairs
per route and `context.coordinator_percent` / `context.worker_percent`.
Percentages are integers from 1 through 99. An adviser list replaces the old
selection. Model/effort availability is checked by Ask or Workflow on use.

The helper reuses consumer validation, preserves unrelated saved fields and
writes only after validation succeeds. Report a failed operation's diagnostic
without claiming it was saved. Do not silently substitute values.

Change settings between runs. A one-time model choice stays in the request or
Plan Step unless the user explicitly asks to save it. Do not start Ask,
Workflow, an installer, an update, a monitor or a second configuration system.

Offer and save only `low`, `medium`, `high` and `xhigh` reasoning levels.
Other supported levels require a manual entry in `.scoville/config.json`.
Show and preserve such entries when changing unrelated settings; never silently
map them to another level. Actual model support still determines execution.
