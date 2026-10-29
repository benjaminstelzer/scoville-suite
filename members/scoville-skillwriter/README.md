# Scoville Skillwriter

Scoville Skillwriter writes and reviews Skills and reusable prompts for current
frontier models. It keeps the goal, real constraints and useful context while
cutting repetition and unnecessary ceremony.

Scoville measures chili heat. Skillwriter keeps instructions sharp without
seasoning every sentence with another warning.

## How it works

It combines shared instruction-design rules with an authoring workflow. Approved
revisions preserve the exact pre-edit state for comparison; reviews return
findings without editing. The host's Skill Creator owns Skill structure,
packaging and format validation. Source review and format validation are
reported separately from observed model behavior.

## What it enforces

It preserves the intended outcome, activation boundaries, permissions and
acceptance criteria. It asks only about material changes beyond the request or
prior approval. Changed instructions and affected consumers are checked together
in the existing source review.

## What it costs

The Skill has no paid service calls. Host model usage and any explicitly requested evaluation have their usual costs.

## How it was developed

Maintained in the Scoville Suite source project. Standalone and Suite packages share the same instruction-design source.

### Model tests

On 2026-10-29, controlled local tests in Codex with `gpt-6.1-sol` / `low` loaded
the public Skillwriter entry and the host's Skill Creator. The approved,
limited revision was applied with an exact pre-edit copy retained; metadata
and boundaries were preserved, and a separate review-only copy stayed unchanged.
The host's format validator passed. These observations cover the tested revision
and review cases. This run did not cover other authoring cases, installed
discovery or current Claude behavior; the edited Skills were not executed.

A separate standalone-prompt revision preserved the requested meaning and
baseline. The agent also read Skill Creator outside that fixture's permitted
scope. The task result passed; compliance with that reading boundary did not.

## Compatibility

Requires an Agent Skills host with filesystem access and its Skill Creator for
Skill authoring: OpenAI's in Codex or Anthropic's in Claude Code. Standalone
prompts need no Skill Creator. No runtime scripts or network access are required.

## Install

Install and enable every Skill in the suite. Each applies to its own task scope.

### Install this Skill

Use [the suite's own packages](https://github.com/benjaminstelzer/scoville-suite/tree/main/packages).
Keep all members from the same suite. If any member is missing or incompatible,
report the incomplete installation rather than claiming the suite is ready.

The host needs permission to write to its Skills directory. The
[Codex Skills guide](https://learn.chatgpt.com/docs/build-skills) and the
[Claude Code Skills guide](https://code.claude.com/docs/en/skills)
list the locations for each host.



## How to use

Ask to write, simplify or review a Skill or reusable prompt, or invoke `$scoville-skillwriter`. For a revision, it respects already approved changes and asks only for changes outside that approval.

## Sources

See the [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-skillwriter/scoville-skillwriter/SKILL.md) and their sources-and-evaluation
reference for the authoring guidance and the distinction between source review,
format validation and observed model behavior. The Skill is also available as
[Scoville Skillwriter](https://github.com/benjaminstelzer/scoville-skillwriter)
outside the suite.

## Developer links

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-skillwriter) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-skillwriter/development/README.md)

## License

MIT. See [LICENSE](LICENSE).
