# User guidance, navigation, forms, and states

Use WordPress conventions to make the primary task, current location, next
action, state, and recovery understandable without implementation knowledge.

## Task and hierarchy

Identify the primary task, required prior information, one primary action for
the current decision region, secondary or progressive information, states, and
available recovery. Visual difference must represent a real difference in
meaning or interaction. Avoid decorative cards or emphasis.

Use exactly one primary page title. Heading levels follow content hierarchy, not
desired visual size.

Preserve the owning Core heading color, font size and font weight. For a
reported mismatch, inspect the computed values and winning CSS declarations
against an equivalent Core heading in the same WordPress version and runtime.
Compare page titles with page titles and section headings with section headings.
Do not flatten their differences or replace a native style merely because a
semantic token is available. Keep source findings separate from rendered proof.

## Navigation

- Put one small settings or tool page under Settings or Tools.
- Use a top-level menu only for a distinct, frequently used, multi-page product
  area. Provide consistent local navigation and expose the current item.
- Do not duplicate the Core admin menu with ornamental navigation.
- A page-title action is appropriate only when it is understandable before the
  main content. Form submission usually follows its fields.

Classic page header order:

```html
<div class="wrap">
  <h1>...</h1>
  <hr class="wp-header-end">
  <!-- Core moves non-inline page notices here. -->
</div>
```

## Actions

- Use one primary action per decision region.
- Name an action by its actual result. Use the same object term in the action,
  status, success, and error.
- Name the object and consequence for destructive actions. Confirm actions that
  are consequential and not easily undone. Offer undo only when restoration is
  real.
- A disabled action needs a nearby, programmatically associated reason.
- During loading, prevent accidental duplicate submission while preserving
  action context and predictable focus.

## Forms

- Use persistent visible labels. Placeholder text is not the only label or
  instruction.
- Help text explains format, consequence, or a non-obvious choice instead of
  repeating the label.
- Communicate requiredness and constraints before avoidable failure.
- Use fieldset/legend or the owning WordPress group component.
- Keep errors near fields and add a summary only when it helps locate multiple
  errors. Preserve entered values when safe.
- Do not solve localized layout problems by shortening or fragmenting copy.

## Feedback

### Classic

- Use `add_settings_error()` and `settings_errors()` where applicable.
- Page Notices remain movable so Core places them after `.wp-header-end`.
- Field/component messages stay at their source and use `.inline` when Core
  notice styling is suitable. Do not use deprecated `.below-h2`.

### React

- Use `Notice` for persistent, important, actionable, error, warning, or
  page-level information.
- Use `Snackbar` only for low-priority short-lived confirmation when the result
  remains discoverable elsewhere.
- Expose asynchronous state programmatically without moving focus unless the
  interaction requires it.

## State requirements

| State | Required guidance |
| --- | --- |
| Initial | Primary task, values, prerequisites, and action are clear. |
| Loading | Name what changes, prevent duplicate action, preserve orientation, announce status. |
| Partial | Distinguish available results from missing parts, preserve usable results, name what is incomplete, and offer only real retry or continuation. |
| Empty | Explain what is absent and offer one valid next action if available. |
| Success | State what changed. Keep the success message visible for as long as the consequence requires. |
| Error | State the user-relevant problem and an available next action. Do not promise unsupported retry. |
| Disabled | Explain why and what requirement enables the action. |
| Permission | Explain unavailable access without sensitive detail, make impossible actions consistent, provide a safe return. |

Include only states possible in the flow, but cover every state introduced by
the implementation.

## Accessibility

- WCAG 2.2 AA is the default floor.
- Preserve keyboard operation, logical focus order, visible and unobscured
  focus, names, roles, values, labels, descriptions, error association, and
  status announcements.
- Visible control text appears in its accessible name, preferably at the start.
  Icon-only controls use purpose-based names.
- Reuse Core/component contrast and focus behavior. A necessary custom color
  requires measured WCAG AA evidence.
- Never rely on color, position, shape, hover, or motion alone.
- Pointer targets meet `24 x 24 CSS px` or a documented WCAG exception.
