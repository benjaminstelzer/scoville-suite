# Responsive layout and page archetypes

WordPress has no universal content width for all plugin pages. Choose an
archetype, keep the shell owner intact, and adapt intrinsically before adding a
breakpoint.

## Shared invariants

- At `<=782px`, respect Core mobile admin behavior. Select boundary, reflow and
  content cases through [WordPress validation](validation.md#select-the-platform-checks).
- Preserve DOM, keyboard, and screen-reader order when layout changes.
- Matching text inputs and selects follow Core's `40px` mobile minimum height. WCAG 2.2
  AA separately requires `24 x 24 CSS px` pointer targets or an allowed
  exception.
- Use logical properties in unavoidable plugin CSS.
- Adapt to localized and expanded content using
  [internationalization's layout contract](internationalization.md#layout).
- Primary actions remain visible. Secondary actions wrap or move to an
  accessible labeled menu.
- Non-exempt shells satisfy:

  ```js
  document.documentElement.scrollWidth <= document.documentElement.clientWidth
  ```

A two-dimensional data view may use one labeled local horizontal scroll
container. The document must not overflow.

## Shells

Classic and hybrid pages inherit `.wrap` and Core gutters. Do not add a second
page gutter. A bundled WPDS `Page` has its own package- and version-specific
padding. Recheck that component source before using its historical 16px block
and 24px inline values. Never apply them to Classic gutters. Density is not a
responsive switch.

## Focused settings or tool page

- One main source-order column.
- Use Settings API and Core form-table behavior on Classic pages.
- Do not impose a plugin page max-width just to create an aesthetic measure.
- Limit prose locally only for a demonstrated reading problem and label that
  choice as Skill-Norm.
- Put submission after the values it affects.
- At `<=782px`, labels and controls stack through Core behavior. Plugin-owned
  inline actions wrap or stack without reordering.

## Workflow or dashboard

- Separate header, primary task, supporting regions, and status and recovery by
  meaning.
- Use the owner-provided Grid or Flex primitive. A custom intrinsic grid requires
  a documented CSS exception.
- Use content-aware minimums. Avoid fixed column counts chosen only from device
  labels.
- **Skill-Norm:** At `<=782px`, default to one visual column unless a smaller group proves
  readable content, target size, and focus order.
- Cards represent real groups. The parent owns inter-card gap.

## Data view

- Use the available admin width instead of the focused-settings measure.
- Keep title, primary action, filters, bulk actions, result status, data region,
  and pagination in source order.
- Wrap toolbars into multiple rows without losing labels or accessible names.
- Prefer a compact list or detail disclosure when it preserves the task.
- If columns must remain two-dimensional, use a labeled local scroll container
  with visible keyboard focus.
- Sticky or clipped UI must not obscure focus.

## Test selection

Use [WordPress validation](validation.md#select-the-platform-checks) for the
scoped layout claims and report inspected cases and remaining gaps.
