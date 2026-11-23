# Scoville Project Context Cleanup

Project rules grow. Unfortunately, clarity does not grow automatically with
them. This Skill adds or revises the rules you request in
`AGENTS.md` or `CLAUDE.md` and
context in `PROJECT_INDEX.md`, keeping useful information where the next agent
will find it.

It preserves meaning, scope and safeguards. Suitable text stays as it is.

Scoville measures chili heat. Context Cleanup removes the dilution, not the
ingredients that made the rules useful.

## How it works

- It finds the right file, reads the rules that already apply and checks for
  duplicates and conflicts before it writes.
- Changes stay within the project-context files you named.
- Scope, conditions, permissions, safeguards and the reasons that matter
  survive the edit. A condition or exception stays with its rule.
- Where a choice would change the meaning, it asks.

## How to use

```text
Add this to the project rules: edit schemas/ and regenerate docs/generated/.
```

You can also name `AGENTS.md`, `CLAUDE.md` or `PROJECT_INDEX.md` directly, or
name the Skill in your request. At a clear project root it creates a
missing `AGENTS.md`, or `CLAUDE.md` on a Claude host. A missing
`PROJECT_INDEX.md` is Plan's to create. Mentioning a file or editing a README
doesn't start a cleanup.

## Install

Context Cleanup comes with the suite and has no repository of its own. Install
the suite for your host from [its packages](https://github.com/benjaminstelzer/scoville-suite/tree/main/packages).
It needs Python 3.11+ for its bundled helper.

Use `gpt-6.2-sol` or Claude Opus 5.5 at medium reasoning effort or higher. Below
that, steps get skipped more often.

## Background

Edits to project rules kept losing exceptions, and references didn't carry the
full rule. Brevity only helps when the meaning survives. The
[full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-project-context-cleanup/scoville-project-context-cleanup/SKILL.md) are what the agent reads.

Sources: [OpenAI's Skills and AGENTS.md guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra),
Anthropic on [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents),
the [AGENTS.md format](https://agents.md/) and two studies on context files,
[AGENTbench](https://arxiv.org/abs/2602.11988) and an
[efficiency study](https://arxiv.org/abs/2601.20404).

## License

MIT. See [LICENSE](LICENSE).
