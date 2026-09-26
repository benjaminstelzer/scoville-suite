# Scoville Handoff

The name comes from the Scoville scale, which originally measured chili heat through dilution.
Here, the heat is the working context another session needs after a long conversation is condensed.

Continuing a task requires its current blocker, unfinished changes and relevant
decisions. Scoville Handoff gathers those facts into one compact, copy-ready
prompt with the objective, permissions and next action, so another session can
resume the work.

## How it works

- Read conversation facts and named sources, recovering incomplete reads within the user's limits.
- Capture decisions, ownership, evidence and blockers while excluding secrets.
- Organize and check one copy-ready prompt with Receiver Instructions, Objective, State and Resume Steps.
- Preserve necessary facts under length limits. The receiver checks current state before acting.

## What it enforces

- **Explicit transfer.** A requested handoff produces one continuation prompt.
- **Usable context.** Material facts from the conversation and named sources
  appear in the prompt, including blockers and incomplete work.
- **Preserved authority.** Permissions, file ownership, user changes and
  boundaries on commits, publication or destructive actions remain explicit.
- **Honest state.** Unobserved results remain unknown. Secrets stay out.
- **Actionable continuation.** The first Resume Step gives the next safe action;
  the last defines observable completion.
- **A faithful snapshot.** Creating the handoff reads and describes the task
  without editing, testing or advancing it.

The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-handoff/scoville-handoff/SKILL.md).

## What it costs

- Reading the task state and preparing the handoff use additional tokens and time.

## How it was developed

- Transfers between real sessions exposed missing blockers, decisions and ownership of local changes.
- Project histories, targeted simulations and optimization workflows informed the four-section template and checks for necessary continuation facts.
- Test results and limitations are retained in the development records.

- Development links: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-handoff/development/README.md)

## Compatibility

Requires a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0
or newer, in an Agent Skills host that can read named task sources. Read-only
version-control inspection is optional. Handoff uses no scripts, network or
subagents.

Developed for Codex and Claude Code. Other hosts are untested. The model
requirement does not establish successful tests across those model families.

Install and enable every Skill in the suite. Each applies to its own task scope.

## Install

### Install this Skill

Install this Skill as part of the complete suite from
[the suite's own packages](https://github.com/benjaminstelzer/scoville-suite/tree/main/packages).
Every member must be installed and enabled. Do not fetch or substitute packages
from individual Skill repositories. If any member is missing or incompatible,
report the incomplete installation rather than claiming the suite is ready.

The host needs permission to write to its Skills directory. See the
[Codex Skills guide](https://learn.chatgpt.com/docs/build-skills) or the
[Claude Code Skills guide](https://code.claude.com/docs/en/skills)
for host-specific locations.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

## How to use

```text
Use Scoville Handoff to transfer this active task to a new session. Include the current repository state and verified evidence.
```

```text
Create a compact handoff for another agent. Preserve the objective, decisions, changed files, blockers and next action. Do not continue the work.
```

## Sources

- Compact Handoff `v1.0.0` for explicit activation, snapshot freshness, secret
  redaction, and copy-ready transfer.
- [Microsoft SkillOpt](https://github.com/microsoft/SkillOpt) for
  validation-driven Skill optimization.
- [SkillReducer](https://arxiv.org/abs/2603.29919v2) for semantic-unit analysis
  and progressive disclosure.
- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package contract.
- [OWASP LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
  for keeping consequential authority explicit across agent boundaries.

## License

MIT. See [LICENSE](LICENSE).
