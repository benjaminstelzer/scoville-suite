# Responsive layout and page archetypes

WordPress has no universal content width for plugin pages. Pick the page type
below, leave the shell to Core, and let content wrap and columns flex before
adding a breakpoint.

## Shared invariants

- At `<=782px`, keep Core's mobile admin behavior. A requested rendered check
  takes its widths and content cases from
  [WordPress validation](validation.md#select-the-platform-checks).
- Preserve DOM, keyboard, and screen-reader order when layout changes.
- Matching text inputs and selects follow Core's `40px` mobile minimum height. WCAG 2.2
  AA separately requires `24 x 24 CSS px` pointer targets or an allowed
  exception.
- Use logical properties in unavoidable plugin CSS.
- Adapt to localized and expanded content using
  [internationalization's layout contract](internationalization.md#layout).
- Primary actions remain visible. Secondary actions wrap or move to an
  accessible labeled menu.
- The document does not scroll sideways; a fixed pixel width that breaks
  this at `782px` is a defect:

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
- Do not set a page max-width only to get a pleasing line length.
- Limit prose locally only for a demonstrated reading problem and label that
  choice as Skill-Norm.
- Put submission after the values it affects.
- At `<=782px`, labels and controls stack through Core behavior. Plugin-owned
  inline actions wrap or stack without reordering.

## Workflow or dashboard

- Separate header, primary task, supporting regions, and status and recovery by
  meaning.
- Use the Grid or Flex primitive of the region's runtime. A custom
  intrinsic grid needs spacing.md's CSS exception record.
- Size columns from content, as in `minmax(min(100%, 18rem), 1fr)`, not
  from a column count per device class.
- **Skill-Norm:** At `<=782px`, default to one visual column unless a smaller group proves
  readable content, target size, and focus order.
- Cards represent real groups. The parent sets the gap between cards.

## Data view

- Use the available admin width instead of the focused-settings measure.
- Keep title, primary action, filters, bulk actions, result status, data region,
  and pagination in source order.
- Wrap toolbars into multiple rows without losing labels or accessible names.
- Prefer a compact list or detail disclosure when it preserves the task.
- If columns must remain two-dimensional, use a labeled local scroll container
  with visible keyboard focus.
- Sticky or clipped UI must not obscure focus.
