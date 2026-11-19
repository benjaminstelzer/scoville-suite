# WordPress guidance additions

Read [common UI quality](../ui-quality.md) for information order, actions,
forms, states and accessibility. Apply these WordPress mappings to the same
scope. A local spacing audit does not bring in unrelated concerns.

## Headings

Use exactly one primary page title. Heading levels follow content hierarchy, not
desired visual size.

Keep Core's heading color, font size and font weight. For a reported
mismatch, compare the CSS declarations that win in the source with those of an
equivalent Core heading in the same WordPress version and runtime; a requested
rendered check, or a requested review of how the page looks, also compares the
computed values: page title with page title, section heading with section
heading. Do not level their differences or replace a native style merely
because a semantic token is available. Do not present a source finding as
rendered proof.

## Navigation

- Put one small settings or tool page under Settings or Tools.
- Use a top-level menu only for a distinct, frequently used, multi-page product
  area. Provide consistent local navigation and expose the current item.
- Do not duplicate the Core admin menu with ornamental navigation.
- A page-title action is appropriate only when it is understandable before the
  main content. Form submission usually follows its fields.

## Feedback

### Classic

The page frame and messages follow rows 1 and 4 of the
[adapter checklist](adapter.md#classic-plugin-page-checklist).

### React

- Use `Notice` for persistent, important, actionable, error, warning, or
  page-level information.
- Use `Snackbar` only for low-priority short-lived confirmation when the result
  remains discoverable elsewhere.
- Expose asynchronous state programmatically without moving focus unless the
  interaction requires it.


## Components and accessibility

Keep Core or component contrast and focus behavior. A necessary custom color
requires WCAG AA contrast against its background: calculate it from the
declared colors when implementing, and measure it in the actual theme in a
requested rendered check or a requested review of how the page looks.
