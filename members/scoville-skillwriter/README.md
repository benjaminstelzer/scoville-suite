# Scoville Skillwriter

Scoville Skillwriter writes and reviews Skills and reusable prompts for current
frontier models. It keeps the goal, real constraints and useful context while
cutting repetition and unnecessary ceremony.

Scoville measures chili heat. Skillwriter keeps instructions sharp without
seasoning every sentence with another warning.

## How it works

It combines a shared instruction-design core with an authoring workflow: review before revision, preserve the baseline, and validate the affected outcome. The host's Skill Creator owns Skill structure and packaging.

## What it enforces

An Agent Skills host with filesystem access. Skill authoring also uses the host's Skill Creator; standalone prompts do not need it. No runtime scripts or network access are required.

## What it costs

The Skill has no paid service calls. Host model usage and any explicitly requested evaluation have their usual costs.

## How it was developed

Maintained in the Scoville Suite source project. Standalone and Suite packages share the same instruction-design source.

## Compatibility

Requires an Agent Skills host with filesystem access and its Skill Creator for
Skill authoring, with standalone prompts needing no Skill package.
Targeted candidate-path tests in Codex with gpt-6.1-sol / low exercised approved
revision, baseline preservation, explicit and implicit activation, review with
the shared criteria loaded, a validated new Skill package and an actual generated prompt consumed unchanged by a fresh
receiver, while executing the generated Skill, other providers and installed
discovery remain unverified.

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

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-skillwriter) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/development/instruction_tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-skillwriter/development/README.md)

## License

MIT. See [LICENSE](LICENSE).
