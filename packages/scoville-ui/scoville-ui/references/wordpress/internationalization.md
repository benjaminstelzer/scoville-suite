# PHP, JavaScript, and layout internationalization

Use one literal text domain equal to the lowercase hyphenated plugin slug. Apply
the contract to visible text, ARIA labels, screen-reader text, alternative text,
notices, errors, empty states, dates, and numbers.

## Required readiness, optional translation delivery

The default requirement is i18n-readiness. A plugin must allow catalogs and
translations to be generated and loaded later without rewriting its UI strings
or registration structure. It may ship only its source-language strings.

Do not create or maintain POT, PO, MO, Jed JSON, translations, or a `languages/`
directory just to satisfy this Skill. Do not introduce WP-CLI, a translator,
locale downloads, or a PO workflow unless the task requires translation
delivery or the project has explicitly selected that workflow. Preserve an
existing translation workflow when it is in scope, including externally
managed catalogs or WordPress language packs.

Readiness requires extractable source strings, correct domains and i18n APIs,
safe formatting and escaping, appropriate script dependencies and loading
hooks, locale-aware values, and layouts that tolerate expansion. RTL checks
follow the language scope below, not i18n-readiness alone.
Artifact generation and proof of an actually loaded translation belong to the
separate [translation-delivery scope](translation-delivery.md).

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

No placeholder PO file or empty language directory is required. Add an explicit
custom path only when the project's selected delivery mechanism needs one.

## Translation delivery

Read [translation delivery](translation-delivery.md) only when the task requires
bundled translations or changes their existing loading or PO-based delivery.
Readiness alone does not require that reference or its optional workflow.

## Dates and numbers

- PHP uses `wp_date()` and `number_format_i18n()`.
- JavaScript dates use `dateI18n` from `@wordpress/date`.
- The baseline passes PHP-formatted numbers to client UI. A client-only number,
  currency, or percentage formatter requires an authoritative API, explicit
  locale mapping, and a browser test. Do not derive BCP-47 by replacing `_`
  with `-` without a source-backed contract.

## Layout

Test doubled strings, long labels, and locale-dependent dates and numbers.
Synthetic expanded labels do not require production translations or PO files
and are not proof of translation loading. Use logical properties, allow
controls and actions to wrap, and preserve information, function, and source
order. Fix presentation instead of shortening or fragmenting translatable copy.

### Language-scoped RTL checks

Require RTL checks only when a supported or explicitly planned UI language
uses right-to-left direction. Include the admin user's language where it
differs from the site language. General multilingual readiness alone does not
put an RTL language in scope.

For LTR-only tasks, omit RTL from the required test matrix. If target languages
are unspecified and no RTL requirement is established, do not add a mandatory
RTL test or block readiness on that uncertainty. State that RTL was not tested
without claiming RTL support. Revisit the matrix when an RTL language enters
scope.

When RTL is in scope, check the affected layouts, controls, focus and source order,
and directional content. Controlled RTL direction is sufficient for a
readiness layout check without catalogs. Actual translation-loading claims
still require runtime proof. Preserve existing Core direction handling and
logical properties even when no RTL test is required.

## Acceptance by scope

| Situation | Result |
| --- | --- |
| Correct i18n APIs, extractable strings and loading hooks, no catalogs, readiness-only task | Accept readiness after source and layout checks. Do not require PO generation or a translated browser string. |
| Catalogs exist, but visible or assistive source strings bypass i18n APIs | Reject readiness. Catalog presence does not fix source defects. |
| Translation delivery is requested but the claimed translations do not load | Reject the delivery claim. Extractable strings alone do not prove delivery. |
| Project uses external catalogs or language packs | Preserve that mechanism. Do not force a local PO workflow. |
| Supported UI languages are LTR-only, such as English and German | No RTL check required. Keep the other readiness and layout checks. |
| A supported or explicitly planned UI language uses RTL | Require RTL layout checks for the affected UI, independently of whether catalogs are being produced. |
| Target languages are unspecified, with no established RTL requirement | Do not force an RTL check. Report it as untested, not as verified support. |

Review source extractability and registration for readiness. If uncertainty
requires an extraction check, a disposable output may supply evidence without
introducing a maintained catalog workflow. Report readiness, translation
delivery, and actual loading evidence separately.

Reject variable domains, concatenated grammar, missing placeholder comments,
unescaped output, accessible source text outside i18n APIs, and wrong handle
order. When a PO-based delivery workflow is selected, also reject mismatched
source and build references. Reject any claim of loaded translations without
runtime proof. Do not reject readiness merely because translation files or
translations have not been produced.
