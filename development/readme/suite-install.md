## Install the suite

Use this request in your agent host:

```text
Uninstall these Skills completely, including their settings, when present:
scoville-code-anti-ai-slop, scoville-handoff, scoville-plan,
scoville-ui-anti-ai-slop, scoville-wordpress-ui-backend-anti-ai-slop,
scoville-brainstorm, scoville-research, scoville-design-anti-ai-slop,
scoville-scribe-anti-ai-slop.
{{ profile: codex }}For Codex, include:
scoville-workflow-for-codex, scoville-workflow-codex,
ask-astra-for-review-for-codex, ask-sol-for-review-for-codex,
ask-claude-for-codex, ask-claude-and-astra-for-codex,
ask-claude-and-sol-for-codex.
{{ /profile }}Skip absent entries, leave unrelated Skills untouched, keep no backup or settings migration, {{ profile: general }}treat Python 3.10 or newer as optional, {{ /profile }}{{ profile: codex }}use Codex's integrated Python 3.11 or newer, {{ /profile }}then install and enable the complete suite for all my projects directly from {{ include: suite.repository }}.
```

All included Skills must remain enabled. Their task scope and invocation rules
still apply; Workflow requires an explicit invocation. Choose standalone Skill
packages instead if you want only selected Skills. Do not mix standalone and
suite copies of the same Skill.

If the host cannot install directly from GitHub, download this suite repository
and copy all its inner package directories to the host's documented Skills
location. This uses the same complete suite packages and requirements.
