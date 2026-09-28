## Install the suite

Install the suite once in your agent host for use across projects.


### New installation

Use this request in your agent host:

```text
Install and enable the complete suite for all my projects directly from {{ include: suite.repository }}.
```

<details>
<summary>Upgrade from an earlier Scoville or Ask suite</summary>

### Upgrade from an earlier Scoville or Ask suite

Use this request in your agent host:

```text
Uninstall these Skills completely, including their settings, when present:
scoville-brainstorm, scoville-code-anti-ai-slop,
scoville-design-anti-ai-slop, scoville-handoff, scoville-plan,
scoville-research, scoville-scribe-anti-ai-slop,
scoville-ui-anti-ai-slop, scoville-wordpress-ui-backend-anti-ai-slop,
scoville-workflow-for-codex, scoville-workflow-codex,
ask-astra-for-review-for-codex, ask-sol-for-review-for-codex,
ask-claude-for-codex, ask-claude-and-astra-for-codex,
ask-claude-and-sol-for-codex.
Skip absent entries, leave unrelated Skills untouched, and keep no backup or settings migration. Then install and enable the complete suite for all my projects directly from {{ include: suite.repository }}.
```

</details>

Do not mix standalone and suite copies of the same Skill.

If the host cannot install directly from GitHub, download this suite repository
and copy all its inner package directories to the host's documented Skills
location. This uses the same complete suite packages and requirements.
