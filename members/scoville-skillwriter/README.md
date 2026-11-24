# Scoville Skillwriter

Scoville Skillwriter writes and reviews Skills and reusable prompts for current
frontier models. It keeps the goal, real constraints and useful context while
cutting repetition and unnecessary ceremony.

Scoville measures chili heat. Skillwriter keeps instructions sharp without
seasoning every sentence with another warning.

## How it works

- By default it writes for Claude Opus 5.5, Claude Fable 5.1+, GPT-6.1 Sol and
  GPT Astra 6+.
- The intended outcome, activation boundaries, permissions and acceptance
  criteria survive a revision. It asks only about material changes beyond what
  you requested or approved.
- An approved revision keeps the exact state from before the edit for
  comparison. A review returns findings and edits nothing.
- The host's Skill Creator owns Skill structure, packaging and format
  validation.
- It reports what it read in the source apart from what a model was actually
  observed doing.

## How to use

Ask it to write, simplify or review a Skill or a reusable prompt:

```text
Use Scoville Skillwriter to review this Skill for repetition and unclear activation. Report findings without editing.
```

## Install

Needs an Agent Skills host with filesystem access and its Skill Creator:
OpenAI's in Codex or Anthropic's in Claude Code. A standalone prompt needs no
Skill Creator.

Use `gpt-6.2-sol` or Claude Opus 5.5 at medium reasoning effort or higher. Below
that, steps get skipped more often.

It comes with the suite. Install every Skill from
[the suite's packages](https://github.com/benjaminstelzer/scoville-suite/tree/main/packages) - partial
installations aren't supported.

## Background

Skillwriter grew from maintaining Skills and reusable prompts in real
projects. Repeated rules and explanations made instructions longer without
making them clearer.

On one task that simplified an overloaded Skill, `gpt-6.1-sol` and Claude
Opus 5.5 kept every checked rule with Skillwriter and without it, so that
test shows neither an advantage nor harm.

The [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-skillwriter/scoville-skillwriter/SKILL.md) are what the agent reads.
Its [sources](scoville-skillwriter/references/sources-and-evaluation.md) list
what the writing rules build on.

## Developer links

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-skillwriter) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-skillwriter/development/README.md)

## License

MIT. See [LICENSE](LICENSE).
