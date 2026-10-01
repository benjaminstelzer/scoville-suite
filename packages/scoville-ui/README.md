# Scoville UI

A page has to work across screen sizes and input methods, and in error
states. Scoville UI builds and audits that behavior with the project's
framework and design system, including plugin-owned WordPress admin pages,
and checks the result in the rendered interface. It also takes care of
interface text: labels say what they're for, buttons name their action, and
terms stay consistent across views and translations.

On supported WordPress admin pages, it uses Core components and follows
WordPress spacing, version requirements and translation conventions.

## How it works

- Find out which design system, components and approved product decisions
  apply.
- Read the relevant code and use the components the framework supports.
- Apply the WordPress guidance to supported plugin-owned `wp-admin` pages.
  Editor surfaces and metaboxes keep their host's conventions.
- Take blocked product decisions to whoever owns them. Where the visual
  direction is still open, stay within the framework's existing conventions.
- Implement the affected states and responsive behavior, then look at the
  rendered result and try the interactions.

## What it enforces

- **Design consistency.** Changes follow the existing design system and
  approved product decisions.
- **Clear hierarchy.** Main decisions, supporting information and secondary
  actions are visibly distinct.
- **Task structure.** Open navigation and layout questions are decided around
  the user's task. Controls are chosen by what they mean, and modal
  interruptions are used deliberately.
- **Interface text.** Labels and buttons say what they're for and what they
  do. Terms stay the same across views, states and translations.
- **Complete states.** Relevant loading, empty, error, disabled, success and
  input states are covered.
- **Responsive behavior.** The interface stays usable on narrow and wide
  screens, with zoom and long content.
- **Changes in context.** When elements change, the affected group and flow
  get another look, including whether the responsive layout still works.
- **Accessibility.** Reading order, names, relationships, contrast, focus and
  keyboard or touch behavior are checked.
- **Visual checks.** Nothing is reported as working until the rendered
  interface has been inspected and its interactions tested. Source checks
  alone leave rendering and interaction unverified.
- **WordPress conventions.** Each part of the page uses the appropriate
  WordPress components and design tokens. Existing PHP-rendered pages can stay
  in PHP.

The full instructions are in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md).

## What it costs

- Browser inspection, interaction checks and corrections take tokens and time.
- WordPress tasks load extra platform guidance.

## How it was developed

- General interface work and WordPress admin tasks shaped the shared quality
  checks and the platform guidance.
- Skill tests can't tell you whether a particular interface is usable. That
  takes testing with its users.

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
