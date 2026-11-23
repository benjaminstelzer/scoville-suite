{{ package: standalone }}Ask your agent host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/{{ var: skill_name }}/tree/main/{{ var: skill_name }}
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

The host needs write access to its Skills directory. {{ profile: general }}The
[Codex]({{ var: codex_skills_guide }}) and
[Claude Code](https://code.claude.com/docs/en/skills) Skills guides say where
that is.{{ /profile }}{{ profile: codex }}The
[Codex Skills guide]({{ var: codex_skills_guide }}) says where that is.{{ /profile }} This Skill works on its own. The other Scoville Skills are in the
[Scoville Suite]({{ include: suite.repository }}).
{{ /package }}{{ package: suite }}It comes with the suite. Install every Skill from
[the suite's packages]({{ include: suite.repository }}/tree/main/packages) - partial
installations aren't supported.
{{ /package }}
