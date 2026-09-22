# Scoville UI Anti-AI-Slop

A good desktop screenshot does not show whether someone can use the page.
The main action may disappear on mobile, keyboard focus may be missing, or an
error may leave the user with no way forward.

Scoville UI implements and audits interfaces through the framework and design
system already in use. It connects component choices, interaction states,
responsive behavior and accessibility to evidence from the rendered interface.

## How it works

- Identify the existing design system, implementation owner and any active Design decisions.
- Read the relevant component and styling code before changing the interface.
- Implement affected states and responsive behavior through supported framework components.
- Check the completed batch in the actual rendered interface, including relevant input and focus behavior.
- Return only a blocked design decision for revision. Without Design, use the bounded new-interface fallback.

## What it enforces

- **The product keeps its visual owner.** The incumbent design system comes
  first. Within it, an active Design record owns design judgment while UI owns
  implementation. Without Design, UI uses its bounded fallback.
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

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/blob/main/scoville-ui-anti-ai-slop/SKILL.md).

## What it costs

- Browser checks and corrections add time and tokens beyond a source-only change.
- Without rendered or interactive access, visual and interaction claims remain unverified. Backend-only work does not need this Skill.
- The latest change to validation after related edits has not yet been tested in a browser or through a live agent regression run.

## How it was developed

- UI developed through interface work and comparisons of how agents use the instructions.
- One recurring problem was checking the rendered page before understanding which component or CSS rule owned it.
- Another was interrupting related edits with repeated screenshots.
- Real-project histories are analyzed alongside results to identify failures and unnecessary context use.
- Targeted simulation and optimization workflows inform revisions. Changes are retained only when the required behavior survives.

## Compatibility

Agent Skills host with reference access and the project's framework toolchain. Geometry proof needs DOM or equivalent platform measurement; visual proof needs actually viewed renders, and interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No bundled scripts or mandatory network access. Developed for Codex and Claude Code; other hosts untested.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

## How to use

Name Scoville UI for interface design, implementation, or audit work:

```text
Use Scoville UI to implement this settled settings-screen design through the product's existing component system. Cover loading, empty, error, and success states, then verify the rendered result responsively.
```

```text
Use Scoville UI to audit the current checkout for hierarchy, accessibility, keyboard use, responsive behavior, and recovery from errors. Do not change files.
```

```text
Use Scoville Design with Scoville UI. Design owns the workflow, hierarchy, typography, spacing, and design-system decision. UI implements that record through the existing framework and proves component states and interactions.
```

Explicit `$scoville-ui-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

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

## Family

- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns engineering scope, implementation, risk, and validation.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans, Work Items, Decisions, and lifecycle state.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns wording, terminology, factual meaning, and source fidelity.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns framework-aligned implementation, interface mechanics, accessibility, and rendered evidence, with a standalone design fallback.
- [WordPress UI Backend](https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop) owns plugin-owned WordPress admin interfaces, platform components, spacing, accessibility and internationalization.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns visual definition, art direction, design systems, critique, and repair.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active work to another agent or session.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web, GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores materially different mechanisms before selection.
- [Workflow Codex](https://github.com/benjaminstelzer/scoville-suite) coordinates explicit Plan execution through native Codex project tasks.

## License

MIT. See [LICENSE](LICENSE).

