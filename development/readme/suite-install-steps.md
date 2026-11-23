Ask your agent host:

```text
Install and enable the complete suite for all my projects from the packages/ directory of {{ include: suite.repository }}.
Preserve personal settings and unrelated Skills. Ask before overwriting conflicting customizations.
Report the installed location and whether the host discovers every member.
```

If your host can't install from GitHub, download the repository and copy each
`packages/<name>/<name>/` directory into the host's Skills location. Don't mix
standalone and suite copies of the same Skill.

### Upgrading

Replace the installed copies with the complete packages of the suite you
chose. Your project settings and unrelated Skills stay.
