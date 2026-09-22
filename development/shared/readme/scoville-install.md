## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/{{ var: skill_name }}/tree/main/{{ var: skill_name }}
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide]({{ var: codex_skills_guide }})
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.
