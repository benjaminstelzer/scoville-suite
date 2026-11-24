# Scoville UI

Scoville UI builds and audits interfaces with the project's framework and
design system. It covers wording, hierarchy, responsive layouts and accessible
interactions, with checks matched to the result being claimed. A tidy component
tree is a start. People still have to use the page.

It includes specific guidance for plugin-owned WordPress admin pages, using
Core components and WordPress conventions.

Scoville measures chili heat. UI aims for a sharper interface without making
the user sweat.

## How it works

- Hierarchy, controls and wording follow the task and what the design system
  already has.
- An approved design stays as it is. States, semantics, focus, input and
  error recovery get the checks they need.
- It checks responsive layout, zoom, reading order, contrast, focus and
  keyboard or touch operation where they apply.
- The evidence matches the claim: spacing needs a measurement, appearance a
  viewed render and behavior an actual interaction. A sample doesn't establish
  a whole-page pass.
- Audits stay read-only, and a local change stays local.
- On WordPress, for a surface the plugin doesn't own, such as a Block Editor
  panel or a metabox, it recommends the host's own mechanism.
- New and changed UI code gets the same review for simplicity and
  maintainability as other code.

## What it costs

Rendered inspection and interaction checks take tokens and time. They catch
problems the source alone can't show.

## How to use

```text
Use Scoville UI to implement this settings screen with the existing component system. Cover its states and verify the rendered interactions.
```

```text
Audit the checkout interface for keyboard use, responsive behavior, accessibility and error recovery. Report findings without changing files.
```

## Install

Works in Codex and Claude Code. It needs the project's framework tools and
Python 3.11+ for its bundled helper. Rendered checks need an interface the
agent can open and operate.

Use `gpt-6.2-sol` or Claude Opus 5.5 at medium reasoning effort or higher. Below
that, steps get skipped more often.

It comes with the suite. Install every Skill from
[the suite's packages](https://github.com/benjaminstelzer/scoville-suite/tree/main/packages) - partial
installations aren't supported.

## Background

Interface work, including WordPress admin pages, shaped UI. Repeated problems
with spacing, alignment and interaction showed why plausible code and a good
screenshot are not enough. Usability still needs the people who will use the
product.

In reviews of 22 interface defects from my own projects, Claude Opus 5.5
found 14 with UI and 7 to 9 without, `gpt-6.2-sol` 10 and 6 - measured with
an earlier revision of the rules.

The [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md) are what the agent reads. The
working rules are in the Skill itself, so routine UI changes don't need web
research. The [development notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)
list the design systems and guidelines they come from.

## Developer links

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)

## License

MIT. See [LICENSE](LICENSE).
