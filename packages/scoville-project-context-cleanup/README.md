# Scoville Project Context Cleanup

Project rules grow. Unfortunately, clarity does not grow automatically with
them. This Skill adds or revises the rules you request in `AGENTS.md` and
context in `PROJECT_INDEX.md`, keeping useful information where the next agent
will find it.

It preserves meaning, scope and safeguards. Suitable text stays as it is.

Scoville measures chili heat. Context Cleanup removes the dilution, not the
ingredients that made the rules useful.

## How it works

- Resolve the target file and read its relevant governing rules.
- Check the addition for useful project information, duplicates and conflicts.
- Place concise wording in the affected structure, with conditions and exceptions together.
- Inspect the saved change and use the record owner's checks where required.

## What it enforces

- Requested additions and cleanup stay within the named project-context files.
- Scope, conditions, permissions, safeguards and necessary reasons survive edits.
- Existing formats and record owners remain responsible for fields and lifecycle.
- Suitable text stays unchanged, and unresolved material choices are asked directly.

## What it costs

- Reading the rules and checking edits takes tokens and time. The useful return is clearer context for later work, without deleting necessary detail.

## How it was developed

Project-rule edits exposed lost exceptions and references that did not carry
the full rule. Those cases shaped the checks for scope, independent copies
and complete context. Brevity only helps when the meaning survives.

## Compatibility

Requires a frontier model from the Fable, Astra, SOL or Opus families,
version 5.0 or newer. Targeted behavior cases also ran with Codex Luna.

The host needs access to the project files and permission for requested writes.
The Skill uses no scripts, services or network. Its shared writing reference
is included in every built package.

Developed and tested in Codex. Other Agent Skills hosts have not been tested.
Implicit selection depends on the host and task, not file-access monitoring.

Install and enable every Skill in the suite. Each applies to its own task scope.

## Install

Install this Skill with the complete released suite from
[the suite packages](https://github.com/benjaminstelzer/scoville-suite/tree/main/packages).
Use the edition for your host and preserve unrelated Skills and settings.
The package is distributed through the suite, without a separate Skill repository.

## How to use

Ask the agent to add or revise project rules:

```text
Add this to the project rules: edit schemas/ and regenerate docs/generated/.
```

Or name `AGENTS.md` or `PROJECT_INDEX.md` explicitly. Requests such as
“Füge das den Projektregeln hinzu” use the same scope.
At a clear project root, this can create a missing `AGENTS.md`. A missing index
follows the requested format. A text addition alone does not create a Plan.

For an explicit call, use `$scoville-project-context-cleanup`. A file mention,
ordinary README edit or routine Plan progress does not request cleanup.

## Sources

- [OpenAI: current Skills and AGENTS.md guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [AGENTS.md format](https://agents.md/)
- [AGENTbench study](https://arxiv.org/abs/2602.11988) and [efficiency study](https://arxiv.org/abs/2601.20404): different results, no universal savings claim.

## License

MIT. See [LICENSE](LICENSE).
