# WordPress admin adapter

Read this file for every supported plugin-owned WordPress 7 admin page, after
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
- Use a token to fill a real gap or to show a domain state, such as
  `sync failed`, in markup the plugin owns. A token is no reason to restyle a
  native control.
- Before choosing composition or CSS, read [spacing.md](spacing.md) and stop
  at the first layer of its CSS ownership ladder that fits.

## Classic plugin page checklist

Use this table for every page or region that PHP renders with Core (the
`PHP with Core` route in routing.md). Build such a page from Core APIs, markup,
classes and defaults.

- Implement: write the change so that every row holds for the code you add or
  touch.
- Audit or review: walk the rows in order against the source. Report each
  defect with its row, file and line.

| # | Look at | Correct | Defect |
| --- | --- | --- | --- |
| 1 | Page frame | **Core:** `<div class="wrap">`, one `<h1>`, then `<hr class="wp-header-end">`. | No `.wrap`; a second `<h1>`; a plugin wrapper that adds its own page gutter or padding. |
| 2 | Fields of a page that saves options | **Core:** `register_setting()`, `add_settings_section()` and `add_settings_field()`; the form posts to `options.php` and prints `settings_fields()`, `do_settings_sections()` and `submit_button()` after the fields. | Field rows hand-written outside `add_settings_field()`; a custom table or grid in place of `.form-table`. |
| 3 | Every `<input>`, `<select>` and `<textarea>` | **WCAG:** an associated label: `label_for` in `add_settings_field()` equal to the control's `id`, a `<label for>`, or `<fieldset>` with `<legend>` for a group of checkboxes or radios. | A control named only by its `placeholder` or by text beside it without `for`. |
| 4 | Save, success and error messages | **Core:** `add_settings_error()` with `settings_errors()`, or `<div class="notice notice-success">` (`notice-error`, `notice-warning`, `notice-info`) with the text in `<p>`. A message about one field stays at the field and adds `inline`. | A hand-built message box with its own class, colors, border or inline style; `.below-h2`. |
| 5 | Buttons and action links | **Core:** `submit_button()` for the form; `class="button button-primary"` for the main action and `class="button"` for others. | An action styled through a plugin class with its own colors, padding or radius. |
| 6 | Where the admin stylesheet and script load | **Core:** the `admin_enqueue_scripts` callback compares `$hook_suffix` with the value returned by `add_menu_page()`, `add_submenu_page()` or `add_options_page()` and returns on every other screen. | `wp_enqueue_style()`, `wp_enqueue_script()` or a printed `<style>` that runs on every admin screen. |
| 7 | Selectors in the plugin's CSS | **Core:** every rule starts at a class or ID the plugin owns. | A rule on a Core selector such as `.wrap`, `.wrap h1`, `.form-table th`, `.button`, `.notice` or `.wp-admin`; copied Core CSS; `!important` without a recorded reason. |
| 8 | `width`, `min-width` and `max-width` on the page and its main containers | **Core:** containers take the available width, so the document does not scroll sideways at `782px` and below. | A fixed pixel width, for example `width: 960px`, wider than the content area at `782px`; a page `max-width` set only for looks. |
| 9 | Every status, such as active, failed or pending | **WCAG:** a text, or an icon with a text alternative, tells the states apart in addition to the color. | States that differ only by color: a colored dot, a colored background, red and green text with the same wording. |
| 10 | Every visible and assistive string | **Core:** a gettext function such as `__()`, `esc_html__()`, `esc_html_e()`, `esc_attr__()`, `_n()` or `_x()` with the plugin's literal text domain. | A hard-coded string beside translated ones; a missing, variable or foreign text domain. Whether the escaping fits the output is a Scoville Code check. |
| 11 | Colors, fonts, radii and shadows | **Core:** titles, buttons, controls, Notices and tables keep Core's look. | A plugin palette, font, radius or shadow on those elements. |

All rows can be decided from the source. Implementing does not include
rendering the page to confirm them: report what only a render shows, usually
the overflow in row 8, as unverified. A requested review or check measures it
with [WordPress validation](validation.md). For a React region, the matching
components are in [ui-guidance.md](ui-guidance.md).

## Load only the relevant contract

Pick the references from
[routing.md's focus table](routing.md#select-the-focus).

- Read [examples.md](examples.md) only when a concrete syntax or composition
  question is still open after the references for the focus. Read only the
  section for the page's runtime. An example shows one runtime; do not copy it
  to another.
- Read [sources.md](sources.md) before you state that a rule is official,
  update the WordPress target, or change a token or package rule. Recheck a
  source there when its listed revalidation condition applies.

## Keep every UI translatable

When you create, change or audit visible or assistive strings, apply
[i18n-readiness](internationalization.md).

## Result contract

Open the report with the mode, the page or region and the focus, in one or two
lines. Report only on that scope. For each statement, say whether you saw it
in a render, read it in the source or could not verify it.

For **Audit**, list actionable findings by impact, highest first. Each finding
gives:

- the location;
- the rule it breaks and that rule's label;
- what you observed;
- the effect on the user;
- the simplest sound correction;
- what was not verified.

Keep confirmed defects apart from suspicions and optional suggestions. When
you found none, say so for the inspected scope only; a targeted check cannot
show that the whole UI complies. Change the implementation only when the
request also asks for the correction. Writing an explicitly requested audit
report is part of the audit.

For **Implement**, report the changes, the checks you ran and their limits.
Add only the facts needed to explain the result: which runtime renders the
region, version and loading, spacing, states, i18n, or the CSS exception. Do
not turn the report into a full-audit checklist. Where a rendered check was
requested, take its evidence from [WordPress validation](validation.md).

When the caller requests structured classification, use the canonical field
values and prohibited-recommendation identifiers from
[classification-output.md](classification-output.md) exactly; do not replace
them with prose synonyms.

Label facts as **Core**, **WPDS**, **WCAG**, or **Skill-Norm**. Never describe
the Skill-Norm as an official WordPress HIG.
