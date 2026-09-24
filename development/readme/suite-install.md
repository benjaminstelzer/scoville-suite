## Install the suite

Use this request in your agent host:

```text
Install and enable every Skill in this suite for all my projects, using only
this repository's own packages:
{{ include: suite.repository }}/tree/main/packages
Each packages/<name>/<name>/ directory contains one installable Skill.
Require every member declared by suite.json. Do not fetch Skills from individual
repositories or replace a missing package with another distribution.
If any member is missing or incompatible with this host, report the blocker;
do not skip it or claim a complete suite installation.
{{ profile: general }}Use Python helpers when available. Load their manual procedures only when
Python is absent; an old interpreter or helper error does not permit that route.
{{ /profile }}{{ profile: codex }}Codex and Python 3.11 or newer are required. Verify the interpreter before
copying Skills. If missing, install supported Python through the normal package
manager or official installer and verify the version. Report blocked host
permissions instead of continuing with an incomplete installation.
{{ /profile }}Preserve personal configuration and unrelated installed Skills. Install only
the inner package directories, not members/ or development/. Report locations,
the complete installed member set and discovery results.
```

All included Skills must remain enabled. Their task scope and invocation rules
still apply; Workflow requires an explicit invocation. Choose standalone Skill
packages instead if you want only selected Skills. Do not mix standalone and
suite copies of the same Skill.

If the host cannot install directly from GitHub, download this suite repository
and copy all its inner package directories to the host's documented Skills
location. This uses the same complete suite packages and requirements.
