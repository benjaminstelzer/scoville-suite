# WordPress guidance additions

This file holds the WordPress mappings for headings, navigation, feedback and
custom colors on a supported plugin page. Read it when routing's focus
includes user guidance and states or accessibility. It adds to the general
rules on information order, actions, forms and states in
[Structure](../ui-structure.md) and [Interactions](../ui-interactions.md), for
the same scope.

## Headings

Use exactly one primary page title. Heading levels follow content hierarchy, not
desired visual size.

Keep Core's heading color, font size and font weight. For a reported
mismatch, compare the CSS declarations that win in the source with those of an
equivalent Core heading in the same WordPress version and runtime; a rendered
check also compares the computed values: page title with page title, section
heading with section heading. Do not level their differences. Do not present
a source finding as rendered proof.

## Navigation

- Put one small settings or tool page under Settings or Tools.
- Use a top-level menu only for a distinct, frequently used, multi-page product
  area. Provide consistent local navigation and expose the current item.
- Do not duplicate the Core admin menu with ornamental navigation.
- A page-title action is appropriate only when it is understandable before the
  main content. Form submission usually follows its fields.

## Feedback

On a Classic page, the page frame and messages follow rows 1 and 4 of the
[adapter checklist](adapter.md#classic-plugin-page-checklist).

In React:

- Use `Notice` for persistent, important, actionable, error, warning, or
  page-level information.
- Use `Snackbar` only for low-priority short-lived confirmation when the result
  remains discoverable elsewhere.

## Components and accessibility

Keep Core or component contrast and focus behavior. Where the backend's
accessibility level is WCAG AA, calculate the contrast of a necessary custom
color against its background from the declared colors in the source, and
measure it in the actual theme in a rendered check.
