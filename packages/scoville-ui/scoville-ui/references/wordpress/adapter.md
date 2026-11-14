# WordPress admin adapter

Read this file for every supported plugin-owned admin page, after
[routing](routing.md) has shown that the surface is supported. Routing also
selects the focus and handles excluded surfaces. Mode and the order of
precedence come from [Scoville UI](../../SKILL.md). Site frontends and themes
follow their product or framework, not this adapter. The platform checks named
here run inside Scoville UI's acceptance, not as a separate pass.

## Respect the classified owner

Core renders and styles `.wrap`, the page title, `.wp-header-end`, page
Notices, native `.form-table`, controls and `p.submit`.

- Keep Classic markup that works, with its native spacing.
- Do not rebuild native buttons, controls, Notices, tables, the page shell,
  colors, focus, radii or shadows only to change how they look.
- Do not write `--wpds-*` definitions, overrides or imitations. Documented
  props of a supported public provider may generate scoped overrides.
- A WordPress upgrade alone is no reason to inject experimental components,
  convert a page to React or migrate it to tokens.
- Use a token to fill a real gap, or to show a domain state that no native
  Notice can show, such as `sync failed` in a list row, in markup the plugin
  owns. Such a state needs AA contrast and a cue besides color. A token is no
  reason to restyle a native control.
- Before choosing composition or CSS, read [spacing.md](spacing.md) and stop
  at the first layer of its CSS ownership ladder that fits.

## Classic plugin page checklist

Use this table for every page or region that PHP renders with Core (the
`PHP with Core` route in routing.md). Build such a page from Core APIs, markup,
classes and defaults.

- Implement: write the change so that every row holds for the lines you add
  or change.
- Audit or review of the whole page: walk all rows in order against the
  source. A targeted audit, such as a spacing review, walks only the rows that
  bear on the named concern.

| # | Look at | Correct | Defect |
| --- | --- | --- | --- |
| 1 | Page frame | **Core:** `<div class="wrap">`, one `<h1>`, then `<hr class="wp-header-end">`. | No `.wrap`; more than one `<h1>`; a plugin wrapper that adds its own page gutter or padding. |
| 2 | Fields of a page that saves options | **Core:** `register_setting()`, `add_settings_section()` and `add_settings_field()`; the form posts to `options.php` and prints `settings_fields()`, `do_settings_sections()` and `submit_button()` after the fields. | Field rows hand-written outside `add_settings_field()`; a custom table or grid in place of `.form-table`. |
| 3 | Every `<input>`, `<select>` and `<textarea>` | **WCAG:** an associated label: `label_for` in `add_settings_field()` equal to the control's `id`, a `<label for>`, or `<fieldset>` with `<legend>` for a group of checkboxes or radios. | A control named only by its `placeholder` or by text beside it without `for`. |
| 4 | Save, success and error messages | **Core:** `add_settings_error()` with `settings_errors()`, or `<div class="notice notice-success">` (`notice-error`, `notice-warning`, `notice-info`) with the text in `<p>`. A message about one field stays at the field and adds `inline`. | A hand-built message box with its own class, colors, border or inline style; `.below-h2`. |
| 5 | Buttons and action links | **Core:** `submit_button()` for the form; `class="button button-primary"` for the main action and `class="button"` for others. | An action styled through a plugin class with its own colors, padding or radius. |
| 6 | Where the admin stylesheet and script load | **Core:** the `admin_enqueue_scripts` callback compares `$hook_suffix` with the value returned by `add_menu_page()`, `add_submenu_page()` or `add_options_page()` and returns on every other screen. | `wp_enqueue_style()`, `wp_enqueue_script()` or a printed `<style>` that runs on every admin screen. |
| 7 | Selectors in the plugin's CSS | **Core:** every rule starts at a class or ID the plugin owns. | A rule that starts at a Core class, ID or element; copied Core CSS; `!important` without a styling-exception rationale. |
| 8 | `width`, `min-width` and `max-width` on the page and its main containers | **Core:** containers take the available width, so the document does not scroll sideways at `782px` and below. | A fixed pixel width that is wider than the content area at `782px`; a page `max-width` set only for looks. |
| 9 | Every status the page shows | **WCAG:** a text, or an icon with a text alternative, tells the states apart in addition to the color. | States that differ only in color, including the same text in different colors. |
| 10 | Every visible and assistive string | **Core:** a gettext function such as `__()`, `esc_html__()`, `esc_html_e()`, `esc_attr__()`, `_n()` or `_x()` with the plugin's literal text domain. | A hard-coded string beside translated ones; a missing, variable or foreign text domain. Whether the escaping fits the output is a Scoville Code check. |
| 11 | Colors, fonts, radii and shadows | **Core:** titles, buttons, controls, Notices and tables keep Core's look. | A plugin palette, font, radius or shadow on those elements. |

Decide every row from the source; implementing does not render the page to
confirm them. A requested rendered check, or a requested review of how the
page looks, measures row 8's overflow with
[WordPress validation](validation.md). For a React region, the matching
components are in [ui-guidance.md](ui-guidance.md).

## Load only the relevant contract

Pick the references from
[routing.md's focus table](routing.md#select-the-focus).

- Read [examples.md](examples.md) only when a concrete syntax or composition
  question is still open after the references for the focus. Read only the
  section for the page's runtime. An example shows one runtime; do not copy it
  to another.
- Read [sources.md](sources.md) when asked where a rule comes from or whether
  it is official.

## Keep every UI translatable

When you create, change or audit visible or assistive strings, apply
[i18n-readiness](internationalization.md).

## Result contract

Report only on the requested page or region and focus.

For **Audit**, list actionable findings by impact, highest first. Each finding
names its location (file and line), the rule it breaks with its checklist row
or label, what you observed, its effect and the simplest sound correction.

Keep confirmed defects apart from suspicions and optional suggestions. When
you found none, say so for the inspected scope only; a targeted check cannot
show that the whole UI complies. Change the implementation only when the
request also asks for the correction. Writing an explicitly requested audit
report is part of the audit.

For **Implement**, report the changes, the checks you ran and their limits.
Add only the facts needed to explain the result; do not turn the report into
a checklist. Where a rendered check was
requested, take its evidence from [WordPress validation](validation.md).

When the caller requests structured classification, use the canonical field
values and prohibited-recommendation identifiers from
[classification-output.md](classification-output.md) exactly; do not replace
them with prose synonyms.

When you state a rule's authority, label it **Core**, **WPDS**, **WCAG** or
**Skill-Norm**, as [routing](routing.md#fact-labels) defines them. Never
present a Skill-Norm as official WordPress guidance.
