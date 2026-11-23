# WordPress admin adapter

This file holds the rules for a supported plugin-owned admin page: what Core
owns there, the checklist for regions that PHP renders with Core, and what a
report adds for WordPress. Read it for every such page after
[routing](routing.md) has shown that the page is supported; routing also
selects the focus and its references and handles excluded pages and regions.
Mode and precedence come from [Scoville UI](../../SKILL.md). Site frontends and
themes follow their product or framework, not this file. Its checks run inside
SKILL.md's [Check and report](../../SKILL.md#check-and-report), not as a
separate pass.

## Respect Core's ownership

Core renders and styles `.wrap`, the page title, `.wp-header-end`, page
Notices, native `.form-table`, controls and `p.submit`.

- Keep Classic markup that works, with its native spacing.
- Do not rebuild native buttons, controls, Notices, tables, the page shell,
  colors, focus, radii or shadows only to change how they look.
- Do not apply frontend-theme spacing to the admin page.
- Do not write `--wpds-*` definitions, overrides or imitations. Documented
  props of a supported public provider may generate scoped overrides.
- A WordPress upgrade alone is no reason to inject experimental components,
  convert a page to React or migrate it to tokens.
- Use a token to fill a real gap, or to show a domain state that no native
  Notice can show, such as `sync failed` in a list row, in markup the plugin
  owns.
- Before choosing or judging composition, CSS or a spacing value, read
  [spacing.md](spacing.md) and stop at the first layer of its CSS ownership
  ladder that fits.

## Classic plugin page checklist

Use this table for every page or region that PHP renders with Core (the
`PHP with Core` route in routing.md). Build such a page from Core APIs, markup,
classes and defaults.

- Implement: write the change so that every row holds for the lines you add
  or change.
- Audit or review of the whole page: walk all rows in order against the
  source. A targeted Audit or review, such as one of spacing, walks only the
  rows that bear on the named concern.

| # | Look at | Correct | Defect |
| --- | --- | --- | --- |
| 1 | Page frame | **Core:** `<div class="wrap">`, one `<h1>`, then `<hr class="wp-header-end">`. | No `.wrap`; more than one `<h1>`; a plugin wrapper that adds its own page gutter or padding. |
| 2 | Fields of a new options page, or of a page that already uses the Settings API; a working hand-written `.form-table` form keeps its own pattern for added fields | **Core:** `register_setting()`, `add_settings_section()` and `add_settings_field()`; the form posts to `options.php`, prints `settings_fields()` and `do_settings_sections()`, then `submit_button()`. | Field rows hand-written outside `add_settings_field()`; a custom table or grid in place of `.form-table`. |
| 3 | Every `<select>`, `<textarea>` and `<input>` other than types `hidden`, `submit`, `reset`, `button` and `image` | **WCAG** ([base](../../SKILL.md#accessibility)): each control has its own label: `label_for` in `add_settings_field()` equal to its `id`, a `<label for>`, or a `<label>` around it; where a label means something only with its group's question: `<fieldset>` with that question as `<legend>`, or a group component that carries the question as the group's name. | A control named only by its `placeholder` or by text beside it without `for`; a group whose labels need its question, where the markup does not give that question as the group's name. |
| 4 | Save, success and error messages | **Core:** `add_settings_error()`; on a page under Settings, Core prints these messages, and a page elsewhere calls `settings_errors()` once, right after `.wp-header-end`. Or `<div class="notice notice-success">` (`notice-error`, `notice-warning`, `notice-info`) with the text in `<p>`. A message about one field stays at the field; when it uses Core notice styling, it adds `inline`. | A hand-built message box with its own class, colors, border or inline style; `.below-h2`; a `settings_errors()` call on a page under Settings, which prints every message twice. |
| 5 | Buttons and action links | **Core:** `submit_button()` for the form; `class="button button-primary"` for the main action and `class="button"` for others. | An action styled through a plugin class with its own colors, padding or radius. |
| 6 | Where the admin stylesheet and script load | **Core:** the `admin_enqueue_scripts` callback compares `$hook_suffix` with the value returned by `add_menu_page()`, `add_submenu_page()` or `add_options_page()` and returns on every other screen. | `wp_enqueue_style()`, `wp_enqueue_script()` or a printed `<style>` that runs on every admin screen. |
| 7 | Selectors in the plugin's CSS | **Core:** every rule starts at a class or ID the plugin owns. | A rule that starts at a Core class, ID or element; copied Core CSS; `!important` without a styling-exception rationale. |
| 8 | `width`, `min-width` and `max-width` on the page and its main containers | **Core:** containers take the available width, so the document does not scroll sideways at `782px` and below. | A fixed pixel width wider than the content area at any width up to `782px`; a page `max-width` set only for looks. |
| 9 | Every status the page shows, where the backend's accessibility level is WCAG AA | **WCAG:** a text, or an icon with a text alternative, tells the states apart in addition to the color. | States that differ only in color, including the same text in different colors. |
| 10 | Every visible and assistive string | **Core:** a gettext function such as `__()`, `esc_html__()`, `esc_html_e()`, `esc_attr__()`, `_n()` or `_x()` with the plugin's literal text domain. | A hard-coded string beside translated ones; a missing, variable or foreign text domain. Escaping follows [internationalization.md](internationalization.md). |
| 11 | Colors, fonts, radii and shadows | **Core:** titles, buttons, controls, Notices and tables keep Core's look. | A plugin palette, font, radius or shadow on those elements. |

Decide every row from the source; a rendered check also measures row 8's
overflow with [WordPress validation](validation.md). For a React region, the
matching components are in [ui-guidance.md](ui-guidance.md). Read
[examples.md](examples.md) only when a syntax or composition question stays
open after the references for the focus.

## Result contract

Report findings as SKILL.md's
[Check and report](../../SKILL.md#check-and-report) says. For the rule a
finding breaks, cite its checklist row where one applies, and label the rule's
authority **Core**, **WPDS**, **WCAG** or **Skill-Norm**, as
[routing](routing.md#fact-labels) defines them. Never present a Skill-Norm as
official WordPress guidance. Do not walk through this file's checklist rows
in the report.
