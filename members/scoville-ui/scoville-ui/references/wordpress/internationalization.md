# PHP, JavaScript, and layout internationalization

Use one literal text domain equal to the lowercase hyphenated plugin slug. Apply
these rules to visible text, ARIA labels, screen-reader text, alternative text,
notices, errors, empty states, dates, and numbers.

## Required readiness, optional translation delivery

Default to i18n-readiness: extractable source strings, correct functions and
domain, safe formatting and escaping, script dependencies and loading hooks,
locale-aware values, and layouts that tolerate longer text. Catalogs can then
be generated and loaded later without rewriting strings or registration.
Shipping only source-language strings is valid.

| Situation | Action |
| --- | --- |
| No translation delivery requested, no workflow explicitly selected | Create no POT, PO, MO, Jed JSON, translations or `languages/` directory; introduce no WP-CLI, translator, locale downloads or PO workflow. |
| A delivery mechanism is selected, including external catalogs and WordPress language packs | Keep it. |
| Bundled translations requested, or existing loading or PO-based delivery changes | Only then read [translation-delivery.md](translation-delivery.md). |

RTL has its own condition below.

## PHP

- Use WordPress gettext functions with the literal domain.
- Translate complete phrases instead of concatenating translated fragments.
- Use positional placeholders, `_n()` for plurals, and `_x()` for context.
- Put `translators:` comments immediately before non-obvious placeholders.
- Treat translations as untrusted and escape for the final output context.
- Keep URLs and structural markup outside translatable strings unless a safe
  documented markup pattern requires otherwise.

```php
/* translators: %1$s: site name, %2$s: localized pending item count. */
$message = sprintf(
    _n(
        '%1$s has %2$s pending item.',
        '%1$s has %2$s pending items.',
        $count,
        'plugin-slug'
    ),
    $site_name,
    number_format_i18n( $count )
);

echo esc_html( $message );
```

## JavaScript

- Use `@wordpress/i18n` or the registered `wp-i18n` dependency.
- Use the same literal domain, complete phrases, positional placeholders,
  plural and context APIs, and immediate translator comments.
- Translate accessible text too.
- Rendering through React does not make translated HTML safe.

```js
import { __, sprintf } from '@wordpress/i18n';

/* translators: %s: settings section name. */
const message = sprintf(
    __( 'Settings for %s were saved.', 'plugin-slug' ),
    sectionName
);
```

## Prepare loading without requiring catalogs

For a JavaScript UI, register its real script handle and dependencies, then
bind that handle to the literal domain with `wp_set_script_translations()`
before enqueueing. This works before any translation file exists.
Do not add a JavaScript build to a PHP-only page for this purpose.

Without a custom catalog location, use the standard loading path:

```php
wp_set_script_translations( 'plugin-slug-app', 'plugin-slug' );
```

Add an explicit custom path only when the selected delivery mechanism needs one.

## Dates and numbers

- PHP uses `wp_date()` and `number_format_i18n()`.
- JavaScript dates use `dateI18n` from `@wordpress/date`.
- By default, pass PHP-formatted numbers to the client UI. A client-only
  number, currency, or percentage formatter requires an authoritative API,
  explicit locale mapping, and a browser test. Do not derive BCP-47 by
  replacing `_` with `-` unless a source defines it.

## Layout

Use logical properties, let controls and actions wrap, and keep information,
function and source order. When longer text breaks the layout, fix the layout,
not the string. A rendered check uses [WordPress validation's content
cases](validation.md#select-the-platform-checks); lengthened test text needs
no production translations or PO files and proves no translation loading.

### Language-scoped RTL checks

| Languages in scope | RTL check |
| --- | --- |
| A supported or explicitly planned UI language is right-to-left, including an admin-user language that differs from the site's | Required. Check affected layouts, controls, focus/source order and directional content. A test with direction set to RTL suffices as readiness layout evidence. |
| LTR only, or unspecified with no established RTL requirement | Not required; does not block readiness. Report RTL as untested without claiming support; revisit when an RTL language enters scope. |

Keep Core's direction handling and logical properties in both cases.

## Acceptance by scope

| Situation | Result |
| --- | --- |
| Readiness only | Accept when the source and the applicable layout checks meet the rules above; catalogs and translated browser strings are unnecessary. |
| Source strings bypass i18n functions or break the domain, formatting, escaping, dependency or handle-order rules above | Reject readiness even if catalogs exist. |
| Translation delivery | Verify the selected mechanism's artifacts and source/build references; prove claimed translations actually load at runtime. Extractability or an RTL-direction test alone cannot establish delivery. |

When extractability stays uncertain, a throwaway extraction can supply
evidence without a maintained catalog workflow. Report readiness, translation
delivery and proof of actual loading separately.
