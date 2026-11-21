# Accessibility at WCAG AA

SKILL.md's [Accessibility](../SKILL.md#accessibility) section holds the base
and says how the project sets the level for the frontend and the backend.
This file applies where the frontend or backend is at WCAG AA, to everything
the task adds, alters or reviews there, for whoever writes it and whoever
reviews it.

The standard itself decides, in the version the project's line names, also
for what this file does not name; the
sections below name what interface code most often gets wrong. Platform
conventions, APG implementation guidance and this Skill's choices are not
additional WCAG criteria. On a platform other than the web, that platform's
accessibility guidance takes the place of the WCAG numbers.

Choose the component and layout so that they carry these requirements
themselves; accessibility is not a final pass over a finished interface. An
automated scan does not prove the interaction is usable.

## Screen reader

- Each control exposes its role, name, state and value, and its
  relationships to the elements it controls or describes, through the
  component, the markup or the platform's accessibility API.
- A status message, such as a result, a progress state or an error, is
  announced to assistive technology without moving focus.
- The order in the code keeps the meaning of the visual order, and what
  looks like a heading, list or table is marked up as one.
- An image or icon that carries meaning has a text alternative; a decorative
  one is hidden from assistive technology.

## Vision

- Foreground (text, icons, control and focus cues) and background meet the
  contrast the standard requires, in every supported state and theme.
- Text can be enlarged to 200 percent, and content reflows at a width of
  320 CSS pixels without scrolling in two directions.
- No meaning rests on color alone.
- Content that appears on hover or focus can be dismissed, can be hovered
  itself and stays until the user leaves it.

## Pointer

- In version 2.2, web pointer targets meet the 24 by 24 CSS-pixel
  requirement or an applicable documented exception.
- No version sets a universal 44-pixel AA target; do not invent one or
  substitute measurements.
- In version 2.2, a task done by dragging can also be done with a single
  pointer without dragging, unless an applicable exception applies.

## Forms and errors

- An error is tied to its field programmatically as well as visually, and
  its text says how to correct it where that is known.
- Format and requiredness are available to assistive technology before the
  error occurs.
- A visible text that names a group of inputs is also their group name: the
  owning group component or a fieldset with a legend.
- A field that collects the user's own data declares its purpose, so the
  browser can fill it.
- In version 2.2, redundant entry and cognitive-function tests are avoided
  where the standard requires alternatives or assistance; its exceptions
  stay.

## Motion and time

- Content that moves, blinks or updates on its own for more than five
  seconds can be paused, stopped or hidden, and nothing flashes more than
  three times a second.
- A time limit can be extended or turned off, apart from the exceptions the
  standard names.
