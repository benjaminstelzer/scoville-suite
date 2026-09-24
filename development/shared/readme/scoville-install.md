## Install

### Install this Skill

{{ package: standalone }}This standalone package works independently. Ask your compatible agent host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/{{ var: skill_name }}/tree/main/{{ var: skill_name }}
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```
{{ /package }}{{ package: suite }}Install this Skill as part of the complete suite from
[the suite's own packages]({{ include: suite.repository }}/tree/main/packages).
Every member must be installed and enabled. Do not fetch or substitute packages
from individual Skill repositories. If any member is missing or incompatible,
report the incomplete installation rather than claiming the suite is ready.
{{ /package }}
The host needs permission to write to its Skills directory. See the
[Codex Skills guide]({{ var: codex_skills_guide }}) {{ profile: general }}or the
[Claude Code Skills guide](https://code.claude.com/docs/en/skills){{ /profile }}
for host-specific locations.
