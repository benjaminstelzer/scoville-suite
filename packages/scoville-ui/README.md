# Scoville UI

A good desktop screenshot does not show whether someone can use the page.
The main action may disappear on mobile, keyboard focus may be missing, or an
error may leave the user with no way forward.

Scoville UI implements and audits interfaces through the framework and design
system already in use. One shared contract covers information structure, states,
accessibility and rendered evidence. For supported WordPress admin pages, it
loads a local adapter for Core components, native spacing, versions and i18n.

## How it works

- Identify the existing design system, implementation owner and approved product decisions.
- Load the local WordPress adapter only for admin surfaces. Other frameworks use the general route.
- Read the relevant component and styling code before changing the interface.
- Implement affected states and responsive behavior through supported framework components.
- Check the completed batch in the actual rendered interface, including relevant input and focus behavior.
- Use one common validation process with the selected platform's additional checks.
- Return blocked product decisions to their owner. Without a visual owner, use the bounded new-interface direction.

## What it enforces

- **The product keeps its visual owner.** The incumbent design system comes
  first. UI implements approved product decisions; without a visual owner, it uses a bounded local direction.
- **The task has a hierarchy.** Primary decisions, supporting information, and
  secondary actions remain distinguishable.
- **Real states exist.** Loading, empty, error, disabled, success, focus,
  keyboard, and touch behavior are covered when relevant.
- **Responsive means adapted.** The task survives narrow, wide, zoomed, and
  content-heavy conditions rather than just scaling down the desktop layout.
- **Accessibility is structural.** Reading order, names, relationships,
  contrast, focus, and input behavior are checked in their real context.
- **Evidence matches the claim.** Source inspection can prove structure.
  Rendered or interactive claims require rendered or interactive evidence.

- **WordPress keeps its native owners.** Classic, Core Components, bundled WPDS and hybrid regions remain distinct. Tokens do not require a React migration.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md).

## What it costs

- Browser inspection, interaction checks and corrections use additional tokens and time.
- WordPress work loads extra platform references. Other frameworks do not need them.
- Source-only work leaves rendering and interaction unverified. These instructions do not establish measured usability gains.

## How it was developed

- General UI and WordPress instructions were developed separately and are now maintained as one Skill with a local platform adapter.
- Common quality and validation rules have one source. WordPress retains its surface, version, spacing and translation contracts.
- Historical reports cover their original packages and models. They do not establish the merged package's runtime behavior.

## Compatibility

Requires a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0
or newer, an Agent Skills host with reference access, and the target project's
toolchain. This is a minimum requirement, not a list of tested models.

Rendered proof needs a running interface, DOM or equivalent geometry inspection
and actually viewed images. Interaction claims need browser or platform control.
WordPress checks need the supported wp-admin runtime and its PHP/JavaScript
components. Source-only and screenshot-only tasks retain their evidence limits.

Developed for Codex and Claude Code. Other hosts are untested. The merged package
has no mandatory network access or dependency on another installed UI Skill.

This package requires every Skill included in this suite to be installed and
enabled. Partial installation is not supported. Skills keep their own task
scope and invocation rules; Workflow still requires an explicit request.

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

Implementation groups related UI changes before validation. Complete the planned
edits, then check source, measure affected relationships and view the result.
Screenshots and measurements follow the completed batch, not each small edit.
If checks reveal defects, collect the related corrections and validate affected
concerns after that correction batch is complete.

Custom styling needs a concrete owner/API justification
before it is written. Authored units and expressions remain distinct from their
computed pixel values and visible geometry.

An ordinary request to check a page for consistency uses a read-only inventory
of its regions, variants and relevant states, including content below the fold.
Every entry maps to source, measurement and visual evidence or a named gap.
The visual routine compares intended edges, text position, apparent whitespace,
control interiors, icons, wrapping and clipping. Sampling limits remain explicit.

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
