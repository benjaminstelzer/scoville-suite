## Install

In a local Codex session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/{{ var: skill_name }}/tree/main/{{ var: skill_name }}
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
As the final installation check, create one normal no-tool project task that reports its effective approval policy, access to this project root, and network access. Compare those values with the installing task, archive the probe, and report any mismatch plus the needed Codex configuration change before asking whether to apply it.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills).
