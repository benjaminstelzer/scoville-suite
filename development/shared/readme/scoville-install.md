### Install this Skill

{{ package: standalone }}Ask your agent host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/{{ var: skill_name }}/tree/main/{{ var: skill_name }}
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```
{{ /package }}{{ package: suite }}Use [the suite's own packages]({{ include: suite.repository }}/tree/main/packages).
Keep all members from the same suite. If any member is missing or incompatible,
report the incomplete installation rather than claiming the suite is ready.
{{ /package }}
The host needs permission to write to its Skills directory. {{ profile: general }}The
[Codex Skills guide]({{ var: codex_skills_guide }}) and the
[Claude Code Skills guide](https://code.claude.com/docs/en/skills)
list the locations for each host.{{ /profile }}{{ profile: codex }}The
[Codex Skills guide]({{ var: codex_skills_guide }}) lists where to install it.{{ /profile }}
