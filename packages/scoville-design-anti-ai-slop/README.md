# Scoville Design Anti-AI-Slop

A design can look polished and still miss the brief. An 80s reference becomes
neon and chrome, but the combination says little about the subject. Or every
element is neatly spaced, yet nothing tells the reader where to start.

Scoville Design connects visual choices to content, audience and medium. It
supports generation, read-only critique and targeted repair, turning a vague
style request into choices that can be inspected and explained.

## How it works

- Frame the brief and choose generation, critique or repair.
- Develop a direction through composition, typography, colour, imagery and the actual content.
- Load specialist methods only for an open design question. Keep rough ideas provisional until a direction is needed.
- Inspect the complete rendered artifact, then its groups and details. Use suitable measurements alongside visual judgment.
- Repair specific defects while preserving strengths. After two unsuccessful passes, reassess the cause and method.
- When UI is also active, Design owns visual intent and UI owns framework implementation and interaction proof. The incumbent system still takes priority.

## What it enforces

- **The brief becomes a design thesis.** Purpose, audience, content, medium,
  constraints, and desired effect shape one specific direction.
- **Relationships do the work.** Hierarchy, composition, typography, colour,
  imagery, spacing, data, and sequence support the same intent.
- **Style is a system.** Period, movement, genre, or vernacular traits are
  translated through structure, type, colour, image logic, material, and
  medium. Familiar signs remain available when they help recognition.
- **Rules may be broken deliberately.** The communication and accessibility
  floors survive, the intent is legible, and compensating structure prevents a
  local exception from becoming general damage.
- **Critique makes repair actionable.** Findings connect observation, likely
  effect, severity, the smallest coherent correction, and preserved strengths.
  Critique stays read-only. An authorised repair adds the change and its render.
- **Evidence matches the claim.** Source, syntax, render, interaction, and
  production proof remain distinct. Attractive output does not prove rights,
  accessibility, or press readiness.
- **Professional boundaries stay visible.** Asset rights, cultural authority,
  provenance, supplier specifications, and human approval are not guessed
  from appearance.

- The installed Core contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop/blob/main/scoville-design-anti-ai-slop/SKILL.md).

## What it costs

- Critique, rendering and revision take time. Generated variants can add image or token costs.
- Attractive output does not establish asset rights, accessibility or production readiness.
- Mechanical conversions and prose-only tasks do not need this process.

## How it was developed

- I developed Design by comparing the instructions with actual visual work.
- Source review, rendered artifacts and blind comparisons exposed different problems, and I revised the Skill around what each could show.
- That led to composition foundations in the Core and specialist methods loaded only when the task needs them.
- Real-project histories are analyzed alongside results to identify failures and unnecessary context use.
- Targeted simulation and optimization workflows inform revisions. Changes are retained only when the required behavior survives.

## Compatibility

Any Agent Skills host that can read references/ and examples/. Visual inspection needs an image or screenshot viewer provided by the host; without one, render checks stay unverified. Optional scripts/read-source.py needs Python 3. Web access only for standards, licence or living-community checks. Developed for Codex and Claude Code; other hosts untested.

Creating artifacts also requires tools for the requested format.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-design-anti-ai-slop/tree/main/scoville-design-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://developers.openai.com/codex/skills/)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

## How to use

Name Scoville Design when the task needs design judgment or original visual
direction:

```text
Use Scoville Design to create an editable A3 poster from this brief. Develop one subject-specific concept, typeset every required line, inspect the render, and repair the highest-impact problem.
```

```text
Use Scoville Design to critique this webpage. Distinguish defects, tradeoffs, preferences, and deliberate exceptions. Preserve what works and propose the smallest coherent repair.
```

```text
Use Scoville Design to make this landing page feel unmistakably like professional 1980s neon and retro computing. Use period DNA structurally, avoid a pile of familiar symbols, and verify desktop and mobile renders.
```

Explicit `$scoville-design-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

### Design and UI

Each Skill works independently.

When both Skills are active and applicable, Scoville Design defines and judges
the design. It owns concept, workflow intent, corporate-design/visual-identity
definition, hierarchy, design-system definition, typography, spacing, art
direction, responsive transformation intent, and style. Scoville UI consumes
the resulting record and owns supported framework implementation, component
states, semantics, focus and input behavior, announcements, responsive
mechanics, and rendered interaction proof.

An incumbent product design system outranks a new Design proposal. When Design
is absent, inactive, inapplicable, or explicitly excluded, UI retains its
bounded Greenfield fallback. Neither Skill searches for, requires, or simulates
the other.

## Sources

The Skill contains original synthesis, not copied books, screenshots, datasets,
or third-party Skill prose. The [source index](scoville-design-anti-ai-slop/references/source-index.md)
resolves the source IDs declared by all 30 modules.

Primary foundations include [Graphic Design and Print Production Fundamentals](https://opentextbc.ca/graphicdesign/),
[Google Fonts Knowledge](https://fonts.google.com/knowledge),
[WCAG 2.2](https://www.w3.org/TR/WCAG22/), and the
[Agent Skills specification](https://agentskills.io/specification).
Sources establish provenance, not an online runtime dependency or a guarantee
of professional competence. Rights, production, and jurisdiction-specific
claims still need current verification.

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

