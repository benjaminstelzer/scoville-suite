# Scoville UI

A page must work across screen sizes, input methods and error states.
Scoville UI implements and audits those behaviors through the project's
framework and design system, using rendered evidence to check the result.

For supported WordPress admin pages, it applies Core components, spacing,
version requirements and translation conventions.

## How it works

- Identify the design system, responsible components and approved product decisions.
- Read relevant code and use the framework's supported components.
- Apply WordPress guidance to supported plugin-owned `wp-admin` pages. Editor surfaces and metaboxes retain their host conventions.
- Implement affected states and responsive behavior, then inspect the rendered result and interactions.
- Resolve blocked product decisions with their owner. Where visual direction is open, stay within existing framework conventions.

## What it enforces

- **Design consistency.** Follow the existing design system and approved product decisions.
- **Clear hierarchy.** Distinguish primary decisions, supporting information and secondary actions.
- **Complete states.** Cover relevant loading, empty, error, disabled, success and input states.
- **Responsive behavior.** Preserve the task across narrow, wide, zoomed and content-heavy layouts.
- **Accessibility.** Check reading order, names, relationships, contrast, focus and keyboard or touch behavior.
- **Matching evidence.** Support visual and interaction claims with rendered and interactive checks.
- **WordPress conventions.** Respect Classic, Core Components, bundled WPDS and hybrid regions. Using tokens does not require a React migration.

The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md).

## What it costs

- Browser inspection, interaction checks and corrections take tokens and time.
- WordPress tasks load platform-specific guidance.
- Source-only checks leave rendering and interaction unverified.

## How it was developed

- General interface and WordPress admin tasks informed the shared quality checks and platform guidance.
- Development records identify tested packages, models and evidence limits. They provide no measured usability claim for every interface built with the Skill.

- Development links: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)

## Compatibility

Requires a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0
or newer, an Agent Skills host with reference access, and the target project's
toolchain. This is a minimum requirement, not a list of tested models.

Rendered proof needs a running interface, DOM or equivalent geometry inspection
and actually viewed images. Interaction claims need browser or platform control.
WordPress checks need the supported wp-admin runtime and its PHP/JavaScript
components. Source-only and screenshot-only tasks retain their evidence limits.

Developed for Codex and Claude Code. Other hosts are untested. The Skill requires
no network access or separate UI Skill.

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
Use Scoville UI to implement this settings screen with the existing component system. Cover its states and verify the rendered interactions.
```

```text
Audit the checkout interface for keyboard use, responsive behavior, accessibility and error recovery. Report findings without changing files.
```

### Source-first checks and consistency audits

Group related edits, then check the source, measure affected relationships and
view the rendered result. If defects remain, collect the corrections and
validate the affected behavior after that batch.

Custom styling needs a reason grounded in the component's ownership or API.
Keep authored units distinct from computed pixels and visible geometry.

A consistency audit inventories regions, variants and states, including content
below the fold. Each finding links to source, measurements and visual evidence
or a named gap. Check alignment, text, whitespace, control interiors, icons,
wrapping and clipping; state any sampling limits.

## Sources

- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package and progressive disclosure.
- [Carbon Design System](https://carbondesignsystem.com/),
  [Atlassian Design System](https://atlassian.design/), and
  [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
  for system-owned components, patterns, and platform conventions.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for accessibility requirements.

## License

MIT. See [LICENSE](LICENSE).
