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

- Establish the requested page or region, task, approved decisions and component
  owners. Audits stay read-only; a local change stays local.
- Load guidance for open concerns and build through the existing framework.
  Settled design still needs correct states, semantics and input behavior.
- Choose source, geometry, visual and interaction evidence for the actual
  claims. Group related changes and refresh only evidence they invalidate.
- Route WordPress admin advice through surface and runtime classification.
  Supported plugin pages share the same checks; excluded host surfaces have
  no general-route bypass. Pure visual concepts keep their design scope.

## What it enforces

- **A coherent interface.** Hierarchy, controls and terminology follow the task
  and the existing design system.
- **Working mechanics.** Approved design stays intact while affected states,
  semantics, focus, input and recovery receive the checks they need.
- **Access across devices.** Check responsive layout, zoom, reading order,
  contrast, focus and keyboard or touch operation where applicable.
- **Scoped proof.** Source, concepts, geometry, viewed appearance and interaction
  establish different things. Measurements need independent targets and
  tolerances chosen before measurement. Partial coverage cannot establish a
  whole-page pass.
- **Code quality.** UI construction and updates receive the shared review for
  simplicity, relevant algorithmic costs, maintainability and clarity, without
  requiring benchmarks.

See the [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md).

## What it costs

- Rendered inspection and interaction checks take tokens and time. Load them
  when the claim needs them; they catch problems source alone cannot show.
  WordPress tasks load the platform contracts relevant to their scope.

## How it was developed

General interface work and WordPress admin tasks shaped the shared checks. The
current source review covered authority, routing, code quality and evidence
boundaries without a material finding. A paired local browser test then checked
actual form behavior within the scope below.
Neither source review nor browser mechanics replaces usability testing with
the people who will use the product.

### Current model checks

Current validation used native Codex agents with gpt-6.1-sol / low. A paired
baseline/candidate form test passed 18 independent Chrome browser checks per
version at 1024×768 and 375×812. Actual clicks and Enter exercised validation,
success and preview behavior; measurements and viewed renders covered the
selected alignment and overflow claims. Submissions created the expected local
in-memory records without a new page navigation.

That proves the tested local form mechanics. It does not establish backend
processing, durable storage, email delivery, other browsers, full accessibility
conformance, WordPress runtime behavior, translation loading, Claude behavior
or installed discovery. Each version had one model run; this is no reliability
rate or general performance result.

## Compatibility

Designed for Codex and Claude Code.
Requires reference access and the project's framework tools. Geometry
proof needs DOM or equivalent measurement, visual proof needs viewed renders,
and interaction proof needs an interactive runtime. No mandatory network.
The bundled size checker uses Python 3.11+; manual fallback is available only
without suitable Python, not after helper errors.

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

```text
Use Scoville UI to implement this settings screen with the existing component system. Cover its states and verify the rendered interactions.
```

```text
Audit the checkout interface for keyboard use, responsive behavior, accessibility and error recovery. Report findings without changing files.
```

### Checking the interface

Use the styling options the component supports. If custom CSS is needed,
explain why. Keep CSS values and the sizes actually rendered on screen apart.

Make related edits together and review the final source diff. Select evidence
for the claim: a concept needs design reasoning, spacing needs measurements
against an independent target, appearance needs a viewed render, and behavior
needs actual interaction. Keep missing evidence explicit. After corrections,
refresh only the affected checks.

A consistency audit lists regions, variants and states, including content
below the fold and in relevant hidden or virtualized regions. Each finding
points to the applicable evidence or explains what couldn't be checked. Look at
alignment, text, whitespace, the inside of controls, icons, wrapping and clipping, and say
which parts of the interface were checked. A sample supports a scoped result,
not an unqualified whole-page pass.

## Sources

- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package and progressive disclosure.
- [Carbon Design System](https://carbondesignsystem.com/),
  [Atlassian Design System](https://atlassian.design/), and
  [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
  for system-owned components, patterns, and platform conventions.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for accessibility requirements.
  Its guidance on [consistent identification](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html),
  [headings and labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html)
  and [label in name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)
  informs the interface text checks.
- [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips)
  for consistent terminology and wording that supports translation.
- [GOV.UK Design System: Buttons](https://design-system.service.gov.uk/components/button/)
  for labels that describe the action and its relevant effect.

- [Microsoft navigation basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics)
  for task-based navigation, orientation and avoiding unnecessary detours.
- [Microsoft responsive design techniques](https://learn.microsoft.com/en-us/windows/apps/design/layout/responsive-design)
  for adapting composition and using space to reduce navigation.
- Google Android [layout basics](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-basics?hl=en)
  and [content composition](https://developer.android.com/design/ui/mobile/guides/layout-and-content/content-structure?hl=en)
  for grouping, alignment and layouts that adapt to content and available space.
- [Adobe Spectrum switches](https://spectrum.adobe.com/page/switch/)
  and [Microsoft toggle switches](https://learn.microsoft.com/en-us/windows/apps/design/controls/toggles)
  for control meaning and platform-specific activation behavior.
- [Microsoft dialogs](https://learn.microsoft.com/en-us/windows/apps/design/controls/dialogs-and-flyouts/dialogs)
  for bounded interruptions and keeping field errors in context.

The vendor guidance shaped the general rules, but platform-specific layouts,
measurements, control behavior and visual conventions aren't universal
requirements. The working rules are in the Skill itself. These sources show
where they come from, so routine UI changes don't need web research.
Rechecking the composition after elements change is how the Skill applies
these principles.

## Developer links

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)

## License

MIT. See [LICENSE](LICENSE).
