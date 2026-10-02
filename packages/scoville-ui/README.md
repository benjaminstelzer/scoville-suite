# Scoville UI

Scoville UI builds and audits interfaces with the project's framework and
design system. It covers clear wording, useful hierarchy, responsive layouts
and accessible interactions, then checks the rendered result. A tidy component
tree is a start. People still have to use the page.

It includes specific guidance for plugin-owned WordPress admin pages, using
Core components and WordPress conventions.

Scoville measures chili heat. UI aims for a sharper interface without making
the user sweat.

## How it works

- Establish the user's task, approved design direction and framework components.
- Build the affected views, wording, states and responsive behavior.
- Inspect the rendered interface and try its relevant interactions.
- Apply the WordPress adapter to supported plugin-owned admin pages. Editor
  surfaces and metaboxes keep their host's conventions.

## What it enforces

- **A coherent interface.** Hierarchy, controls and terminology follow the task
  and the existing design system.
- **Usable states.** Loading, empty, error and success states receive the same
  attention as the convenient example with perfect data.
- **Access across devices.** Check responsive layout, zoom, reading order,
  contrast, focus and keyboard or touch operation where applicable.
- **Rendered proof.** Source checks alone cannot establish that the interface
  works. Unchecked rendering or interaction stays explicitly unverified.

See the [full instructions](https://github.com/benjaminstelzer/scoville-ui/blob/main/scoville-ui/SKILL.md).

## What it costs

- Rendered inspection and interaction checks take tokens and time. They catch problems the source alone cannot show. WordPress tasks also load platform guidance.

## How it was developed

General interface work and WordPress admin tasks shaped the shared checks.
Rendered inspection exposed problems that source review missed. Neither type
of check replaces usability testing with the people who will use the product.

## Compatibility

Needs a frontier model from the Fable, Astra, SOL or Opus families, version
5.0 or newer. Luna was also used in testing.

The host must be able to read the Skill's references, and the target
project's toolchain has to be available.

Visual checks need a running interface, screenshots and access to element
positions and sizes, through the DOM or an equivalent tool. Testing
interactions needs control of a browser or the platform.

WordPress checks need the supported wp-admin runtime with its PHP and
JavaScript components. Reading the source can't verify the rendered
interface, and screenshots alone can't verify interactions.

Developed for Codex and Claude Code. Other hosts haven't been tested.

Install and enable every Skill in the suite. Each applies to its own task scope.

## Install

### Install this Skill

Install this Skill as part of the complete suite from
[the suite's own packages](https://github.com/benjaminstelzer/scoville-suite/tree/main/packages).
Every member must be installed and enabled. Do not fetch or substitute packages
from individual Skill repositories. If any member is missing or incompatible,
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

Make related edits together, then check the code and the rendered result,
including spacing and alignment. If defects remain, collect the corrections
and recheck the affected behavior once that batch is done.

A consistency audit lists regions, variants and states, including content
below the fold. Each finding points to the source, measurements and visual
evidence, or explains what couldn't be checked. Look at alignment, text,
whitespace, the inside of controls, icons, wrapping and clipping, and say
which parts of the interface were checked.

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

## License

MIT. See [LICENSE](LICENSE).
