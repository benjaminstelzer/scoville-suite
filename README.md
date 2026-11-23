# Scoville Suite

Scoville helps your agent plan work, write code, improve interfaces and carry
unfinished tasks into the next conversation. The Skills keep the goal, the
project's conventions and the verified results in view.

Scoville is the scale for chili heat. These Skills aim for sharper work and
less diluted context. Adding more instructions is easy. Keeping the useful
ones is the point.

This edition is for Claude Code and other Agent Skills hosts. For Codex desktop
there is [Scoville Suite for Codex Mainloop](https://github.com/benjaminstelzer/scoville-suite-for-codex-mainloop),
which adds Workflow, Ask and Setup.

| Skill | What it does |
| --- | --- |
| [Code](members/scoville-code/README.md) | Keeps implementation, debugging and review tied to the result you asked for. |
| [Plan](members/scoville-plan/README.md) | Keeps goals, decisions and progress in the repository so longer work survives the next conversation. |
| [UI](members/scoville-ui/README.md) | Builds and audits interfaces with the project's framework and design system. |
| [Handoff](members/scoville-handoff/README.md) | Transfers the work state, not the whole conversation. |
| [Project Context Cleanup](members/scoville-project-context-cleanup/README.md) | Adds and revises project rules without losing what made them useful. |
| [Skillwriter](members/scoville-skillwriter/README.md) | Writes and reviews Skills and reusable prompts for current frontier models. |

## Install

The bundled helpers need Python 3.11+ - without it,
the affected step stops and says so.

Use `gpt-6.2-sol` or Claude Opus 5.5 at medium reasoning effort or higher. Below
that, steps get skipped more often.

Ask your agent host:

```text
Install and enable the complete suite for all my projects from the packages/ directory of https://github.com/benjaminstelzer/scoville-suite.
Preserve personal settings and unrelated Skills. Ask before overwriting conflicting customizations.
Report the installed location and whether the host discovers every member.
```

If your host can't install from GitHub, download the repository and copy each
`packages/<name>/<name>/` directory into the host's Skills location. Don't mix
standalone and suite copies of the same Skill.

### Upgrading

Replace the installed copies with the complete packages of the suite you
chose. Your project settings and unrelated Skills stay.

### Additional Scoville Skills

#### scoville-ask-for-codex

For Codex, installed on its own. Ask your Codex host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-ask-for-codex/tree/main/scoville-ask-for-codex
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

## Background

Scoville grew from a frustrating pattern in real software projects: an agent
could follow plenty of rules and still lose the goal between planning,
implementation and review. Every idea is tested and then used in real
workflows on large projects, and what those show goes into the next revision.
The [development notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/docs/README.md)
tell the longer story.

## Deprecated

These Skills are retired. In testing, they didn't do enough better than
current frontier models to be worth maintaining.

- **Scoville Scribe Anti-AI-Slop:** The writing comparisons showed no reliable
  benefit, and the tested version added claims it couldn't support.
- **Scoville Design Anti-AI-Slop:** Its comparison with modern frontier models
  ended in a tie.
- **Scoville Research:** It didn't reach the quality I expect, and good
  research tools already exist.
- **Scoville Brainstorm:** It didn't reach the quality I expect, and good
  tools for ideation already exist.

## Developer links

Sources, tests and notes for every Skill live in this repository. The
[build guide](development/shared/build/fragments.md) covers builds and checks.

- **scoville-code**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-code/development/README.md)
- **scoville-plan**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-plan/development/README.md)
- **scoville-ui**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)
- **scoville-handoff**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-handoff/development/README.md)
- **scoville-project-context-cleanup**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-project-context-cleanup) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-project-context-cleanup/development/README.md)
- **scoville-skillwriter**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-skillwriter) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-skillwriter/development/README.md)

## License

The bundled Skills use the MIT license. Each package includes its `LICENSE` file.

