## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

```text
Install the complete Scoville Skill suite for all my projects. Fetch and install every exact package directory below:

{{ include: family.install }}

Preserve existing customizations and ask before overwriting conflicting files. Report every installed location and whether the host discovers each Skill.
```
