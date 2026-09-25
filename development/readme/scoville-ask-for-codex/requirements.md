## What it enforces

- Advisers inspect and answer. Changes remain with the calling task.
- Native tasks use `Ask <model> · <original task title>`. Identity comes from task IDs and consultation references.
- Invalid settings, unavailable models and failed advisers remain visible. There is no silent replacement model or route.

Native advisers follow a read-only instruction, but the host does not add a
technical write barrier when creating their task. Claude permits Read, Grep and
Glob by default. Enable `claude.web_tools` explicitly for WebSearch and WebFetch.
Claude model communication remains online even when these web tools are off.
