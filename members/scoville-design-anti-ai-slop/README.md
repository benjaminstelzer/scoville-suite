# Scoville Design Anti-AI-Slop

A design can look polished and still miss the brief. An 80s reference becomes
neon, chrome and VHS noise, but the combination says little about the actual
subject. Or every element is neatly spaced, yet nothing tells the reader where
to start.

Scoville Design connects the visual choices to the content, audience and medium.
It helps create a direction, develop it into an artifact, inspect the result and
repair specific problems. A critique should explain what is wrong and why,
while preserving the parts that work.

The agent has to explain how typography, composition and visual references serve
the brief, then inspect the artifact and make targeted corrections. This adds
critique and revision time, and generated variants can add token or image costs.
More iterations are not useful when they no longer resolve a concrete problem.

Use it for graphic, editorial, brand, advertising, packaging, wayfinding, web,
interface, information and motion design. It also handles style interpretation.
Mechanical edits to a settled design, conversion or rendering alone, backend
work and prose-only editing do not need it.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
In Design, that means keeping the idea and the content legible through the visual choices.

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

The installed Core contract is in [SKILL.md](scoville-design-anti-ai-slop/SKILL.md).

## How it works

The Core runs a compact studio loop: frame and route, explore, consolidate,
execute, inspect, resolve and deliver. Composition foundations apply throughout
Design work. A direct index selects from 30 specialist modules only when an open
decision or needed method calls for them. Rough ideas can stay provisional.
Shared spacing and type roles are committed before repetition, then the actual
render is inspected from the whole down to groups and native details.

Visual inspection and suitable measurements check the same final artifact.
Neither substitutes for the other. A clean first render can pass, and repair
has no one-correction cap. After two unsuccessful passes, reassess the cause and
method. Preserve useful expression while fixing the supported problem.

The package has three modes: generation, read-only critique and repair.
Style direction remains a domain available within each mode. A requested artifact must be editable and rendered through
the appropriate format tool when available. Advice alone does not complete an
artifact request.

The modules include practical ways to build and compare a design: adjust
measure and leading with the actual text, construct a role palette, compare
mark contours, allocate content across media, or place map labels without
moving their features. Select the operation the task needs. These methods
do not impose a universal visual preset or a module-size target.

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

## How it was developed

I developed Design by comparing the instructions with actual visual work.
Source review, rendered artifacts and blind comparisons exposed different
problems, and I revised the Skill around what each could show. That led to
composition foundations in the Core and specialist methods loaded only when
the task needs them.

The [changelog](CHANGELOG.md) follows that development. I continue reading task
histories alongside the resulting artifacts to find missed defects, repeated
repairs and reference reads that do not help the design. The comparisons used
changing briefs and Skill versions with one human reviewer (me, with over 20 years
of experience in media design). They helped me
revise the instructions, but are not a benchmark of general design quality.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

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

## Development

Maintained in the suite. Individual repositories contain generated packages.

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-design-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-design-anti-ai-slop/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-design-anti-ai-slop/development/README.md)

## License

MIT. See [LICENSE](LICENSE).

