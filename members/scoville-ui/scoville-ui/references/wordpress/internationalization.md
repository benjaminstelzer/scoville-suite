# PHP, JavaScript, and layout internationalization

Use one literal text domain equal to the lowercase hyphenated plugin slug. Apply
the contract to visible text, ARIA labels, screen-reader text, alternative text,
notices, errors, empty states, dates, and numbers.

## Required readiness, optional translation delivery

Default to i18n-readiness: extractable source strings, correct domains/APIs,
safe formatting and escaping, script dependencies and loading hooks,
locale-aware values, and expansion-tolerant layouts. Catalogs must be generatable
and loadable later without rewriting strings or registration; shipping only
source-language strings is valid.

Create POT, PO, MO, Jed JSON, translations or a `languages/` directory only for
translation delivery or an explicitly selected workflow. The same condition
governs introducing WP-CLI, a translator, locale downloads or a PO workflow.
Preserve the selected delivery mechanism, including external catalogs and
WordPress language packs. Read [translation-delivery.md](translation-delivery.md)
only for requested bundled translations or changes to existing loading or
PO-based delivery. RTL has its separate language scope below.

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
before enqueueing. This registration can exist before translation files do.
Do not add a JavaScript build to a PHP-only page for this purpose.

Without a custom catalog location, use the standard loading path:

```php
wp_set_script_translations( 'plugin-slug-app', 'plugin-slug' );
```

Add an explicit custom path only when the selected delivery mechanism needs one.

## Dates and numbers

- PHP uses `wp_date()` and `number_format_i18n()`.
- JavaScript dates use `dateI18n` from `@wordpress/date`.
- The baseline passes PHP-formatted numbers to client UI. A client-only number,
  currency, or percentage formatter requires an authoritative API, explicit
  locale mapping, and a browser test. Do not derive BCP-47 by replacing `_`
  with `-` without a source-backed contract.

## Layout

Use logical properties, allow controls and actions to wrap, and preserve
information, function and source order. Fix presentation instead of shortening
or fragmenting translatable copy. Apply [WordPress validation's content
cases](validation.md#select-the-platform-checks); synthetic expansion requires
no production translations or PO files and proves no translation loading.

### Language-scoped RTL checks

Require RTL checks when a supported or explicitly planned UI language uses
right-to-left direction, including an admin-user language that differs from
the site's. Check affected layouts, controls, focus/source order and directional
content. Controlled RTL direction suffices for readiness layout evidence.

For LTR-only or unspecified languages without an established RTL requirement,
omit mandatory RTL tests and do not block readiness. Report RTL as untested
without claiming support; revisit when an RTL language enters scope. Preserve
Core direction handling and logical properties in either case.

## Acceptance by scope

| Situation | Result |
| --- | --- |
| Readiness only | Accept after source and applicable layout checks meet this contract; catalogs and translated browser strings are unnecessary. |
| Source strings bypass i18n APIs or violate the domain, formatting, escaping, dependency or handle-order contracts above | Reject readiness even if catalogs exist. |
| Translation delivery | Verify the selected mechanism's artifacts and source/build references; prove claimed translations actually load at runtime. Extractability or controlled RTL alone cannot establish delivery. |

If source extractability remains uncertain, a disposable extraction can supply
evidence without introducing a maintained catalog workflow. Report readiness,
translation delivery and actual loading evidence separately.
