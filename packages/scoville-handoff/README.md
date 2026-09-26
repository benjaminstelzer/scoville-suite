# Scoville Handoff

The next session needs enough information to continue, not another transcript.
A long summary can still miss the current blocker, unfinished changes or the
reason an earlier approach failed.

Scoville Handoff produces one compact continuation prompt with the objective,
current state, authority and next safe action. It preserves the facts needed
to resume without quietly advancing or completing the work.

## How it works

- Use established conversation facts and read named task sources with bounded recovery when a read is incomplete.
- Capture decisions, ownership, evidence, blockers and hazards without secrets.
- Organize the result into Receiver Instructions, Objective, State and Resume Steps.
- Compare the prompt against the captured facts and return one copy-ready block.
- The receiver checks current state before acting. A tight limit removes repetition before necessary facts.

## What it enforces

- **Explicit transfer only.** Ordinary summaries and context reduction do not
  produce a handoff artifact.
- **One receiver contract.** Every handoff contains Receiver Instructions,
  Objective, State, and Resume Steps in one copy-ready block.
- **Facts instead of pointers.** Conversation facts remain available. Named sources are read with targeted recovery
  for truncation or a transient failure, within explicit user limits. Their material
  facts enter the artifact so the receiver has them when resuming.
- **Authority and ownership survive.** Commit, publication, destructive-action,
  external-effect, file-owner, and dirty-tree boundaries stay explicit.
- **Unknown stays unknown.** Running or unobserved work never becomes a success
  claim, and secret values never enter the handoff.
- **The receiver can act.** Step 1 is the next safe action. The final step names
  an observable completion result.
- **Transfer does not advance the task.** Handoff reads the named state but does
  not edit, test, publish, or otherwise improve it on the way out.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-handoff/scoville-handoff/SKILL.md).

## What it costs

- Reading the task state and preparing the handoff use additional tokens and time.

## How it was developed

- Handoff grew out of moving real work between sessions and seeing what the next session was missing.
- A long summary could still omit the current blocker or fail to say which local changes belonged to the user.
- The [changelog](CHANGELOG.md) traces the move from a large conditional template to four sections built around continuing the work.
- Real-project histories are analyzed alongside results to identify failures and unnecessary context use.
- Targeted simulation and optimization workflows inform revisions. Changes are retained only when the required behavior survives.

## Compatibility

Requires a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0
or newer, in an Agent Skills host that can read named task sources. Read-only
version-control inspection is optional. Handoff uses no scripts, network or
subagents.

Developed for Codex and Claude Code. Other hosts are untested. The model
requirement does not establish successful tests across those model families.

This package requires every Skill included in this suite to be installed and
enabled. Partial installation is not supported. Skills keep their own task
scope and invocation rules. Workflow still requires an explicit request.

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
