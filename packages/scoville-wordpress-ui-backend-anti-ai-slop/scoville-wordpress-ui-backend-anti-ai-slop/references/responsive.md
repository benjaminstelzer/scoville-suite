# Responsive layout and page archetypes

WordPress has no universal content width for all plugin pages. Choose an
archetype, keep the shell owner intact, and adapt intrinsically before adding a
breakpoint.

## Shared invariants

- At `<=782px`, respect Core mobile admin behavior. Check `783px` as the
  boundary immediately above it.
- At `320 CSS px`, non-exempt content retains information and function in one
  scrolling direction. Also check the equivalent `1280px` at `400%` zoom.
- `600px` and `390px` are Skill-Norm intermediate test widths, not official
  universal WordPress breakpoints.
- Preserve DOM, keyboard, and screen-reader order when layout changes.
- Matching text inputs and selects follow Core's `40px` mobile minimum height. WCAG 2.2
  AA separately requires `24 x 24 CSS px` pointer targets or an allowed
  exception.
- Use logical properties in unavoidable plugin CSS.
- Treat doubled text, long labels, errors, notices, dates, and numbers as
  normal content inputs. Include RTL only when a supported or explicitly
  planned UI language requires it, following the
  [language-scope rule](internationalization.md#language-scoped-rtl-checks).
- Primary actions remain visible. Secondary actions wrap or move to an
  accessible labeled menu.
- Non-exempt shells satisfy:

  ```js
  document.documentElement.scrollWidth <= window.innerWidth
  ```

A two-dimensional data view may use one labeled local horizontal scroll
container. The document must not overflow.

## Shells

Classic and hybrid pages inherit `.wrap` and Core gutters. Do not add a second
page gutter. A bundled WPDS `Page` has its own package/version-specific
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

- Separate header, primary task, supporting regions, and status/recovery by
  meaning.
- Use the owner-provided Grid/Flex primitive. A custom intrinsic grid requires
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

## Test matrix

For a new page or a full responsive audit, render each applicable archetype at
`783`, `782`, `600`, `390`, and `320` CSS
pixels, plus `1280px` at `400%` zoom or an equivalent reflow setup. Repeat the
decisive cases with doubled text, long labels, errors/notices,
empty/loading/success/permission states, and keyboard-only traversal.
Add RTL cases only when RTL is in language scope. LTR-only or unspecified
language scope does not make an RTL check mandatory.

For a focused audit or isolated change, select the widths, content, and states
that can affect the scoped conclusion. A spacing check includes a wrapping
boundary when wrapping changes those distances, not every page and state by
default. Preserve the same reflow and accessibility requirements for the
affected UI. Report which cases were inspected, without calling a partial
matrix a complete responsive audit. A source-only review leaves rendered
behavior unverified rather than requiring a browser session.

Source and build inspection do not prove these conditions.
