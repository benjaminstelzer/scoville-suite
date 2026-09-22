## Install

### Install this Skill

In a local Codex session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-suite/tree/main/packages/scoville-workflow-for-codex/scoville-workflow-for-codex
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether Codex discovers the Skill.
As the final installation check, create one no-tool normal project task and verify that its approval policy, access to the project root, and network access match this calling task. Archive the probe. If they differ, do not mark the Skill ready; report the exact mismatch and ask whether to apply the needed Codex configuration change.
```

The agent needs source access and permission to write to the
personal Skills location. The installable package is the nested
`scoville-workflow-for-codex/` directory, not the repository root. Manual fallback:
[Codex Skills guide](https://learn.chatgpt.com/docs/build-skills).
