## Install the suite

Install the complete suite in your agent host to use it across projects.
### New installation

Use this request in your agent host:

```text
Install and enable the complete suite for all my projects from the packages/ directory of {{ include: suite.repository }}.
Preserve personal settings and unrelated Skills. Ask before overwriting conflicting customizations.
Report the installed location and whether the host discovers every member.
```

Do not mix standalone and suite copies of the same Skill. If your host cannot
install from GitHub, download the repository and copy each
`packages/<name>/<name>/` Skill directory into the host's Skills location.
The repository root and development sources are not installable Skills.

### Upgrade or migrate an existing installation

Choose the target suite explicitly. Preserve project settings and personal
customizations, then replace duplicate installed copies with the target suite's
complete packages. Remove only superseded Skills you have selected for removal.
An upgrade is not permission to erase settings or unrelated Skills.
