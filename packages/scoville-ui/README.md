# Scoville UI

A page must work across screen sizes, input methods and error states.
Scoville UI implements and audits those behaviors through the project's
framework and design system, using rendered evidence to check the result.

For supported WordPress admin pages, it applies Core components, spacing,
version requirements and translation conventions.

The name comes from the Scoville scale, which originally measured chili heat through dilution.
Here, the heat is the task a person can still understand and complete across layouts, interactions and error states.

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
- **Responsive behavior.** Keep the interface usable on narrow and wide screens, with zoom and long content.
- **Accessibility.** Check reading order, names, relationships, contrast, focus and keyboard or touch behavior.
- **Visual checks.** Inspect the rendered interface and test its interactions before reporting them as working.
- **WordPress conventions.** Use the appropriate WordPress components and design tokens for each part of the page. Existing PHP-rendered pages can remain in PHP.

The full instructions are in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md).

## What it costs

- Browser inspection, interaction checks and corrections take tokens and time.
- WordPress tasks load platform-specific guidance.
- Source-only checks leave rendering and interaction unverified.

## How it was developed

- General interface and WordPress admin tasks informed the shared quality checks and platform guidance.
- Skill tests do not establish the usability of an individual interface. That needs testing with its users.

## Compatibility

A current Fable, Astra, SOL or Opus model is recommended. Luna was also used
in testing.

Requires an Agent Skills host with reference access, and the target project's
toolchain.

Visual checks require a running interface, screenshots and access to element
positions and sizes through the DOM or an equivalent tool. Testing interactions
requires browser or platform control.
WordPress checks need the supported wp-admin runtime and its PHP/JavaScript
components. Source inspection cannot verify the rendered interface. Screenshots alone cannot verify interactions.

Developed for Codex and Claude Code. Other hosts are untested. The Skill requires
no network access.

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

### Checking the interface

Group related edits, then inspect the code and rendered result, including
spacing and alignment. If defects remain, collect the corrections and
validate the affected behavior after that batch.

Use the component's supported styling options. When custom CSS is needed,
explain why. Distinguish CSS values from the sizes actually rendered on screen.

A consistency audit inventories regions, variants and states, including content
below the fold. Each finding links to source, measurements and visual evidence
or explains what could not be checked. Check alignment, text, whitespace, control interiors, icons,
wrapping and clipping. State which parts of the interface were checked.

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
