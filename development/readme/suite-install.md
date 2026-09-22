## Install the suite

Use one request in your agent host:

```text
Install all Scoville Skills compatible with this host for all my projects from
https://github.com/benjaminstelzer/scoville-suite/tree/main/packages
Each packages/<name>/<name>/ directory contains one installable Skill.
Inspect each Skill's compatibility first. Workflow requires Codex desktop.
Preserve personal configuration and unrelated installed Skills. Do not install
members/, development/, or another copy from the individual repositories.
Report installed locations, skipped incompatibilities and discovery results.
```

The suite supplies all its Skills from one repository. Your host still sees
separate Skills, so you can enable or disable them individually. Workflow is
suite-only. The specialist Skills are also available from their individual repositories.

If your host cannot fetch or install them, copy each compatible inner Skill
directory to its documented Skills location. See the
[Codex Skills guide](https://developers.openai.com/codex/skills/) or
[Claude Code Skills guide](https://code.claude.com/docs/en/skills).
