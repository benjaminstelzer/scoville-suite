# Bundled translation delivery

This file holds custom translation loading for bundled translations and an
optional PO-based delivery chain. Read it only when
[internationalization.md](internationalization.md#required-readiness-optional-translation-delivery)
sends you here: bundled translations are requested, or existing loading or
PO-based delivery changes.

## Optional custom translation loading

Register a custom language path at `init` when the plugin bundles translations:

```php
add_action( 'init', static function () {
    load_plugin_textdomain(
        'plugin-slug',
        false,
        dirname( plugin_basename( __FILE__ ) ) . '/languages'
    );
} );
```

Register and enqueue the JavaScript handle as in
[internationalization.md](internationalization.md#prepare-loading-without-requiring-catalogs),
and attach translations to that exact handle and literal domain with the
explicit language path:

```php
wp_set_script_translations(
    'plugin-slug-app',
    'plugin-slug',
    plugin_dir_path( __FILE__ ) . 'languages'
);
```

## Optional PO-based delivery example

Use this chain only when producing bundled translations is part of the task
and the project chooses a PO-based workflow. It is not a readiness checklist
or the only supported way to deliver translations.

Before extraction, make the PO source references point to the registered
`build/index.js`, not `src/index.js`. Generated filenames use the MD5 of the
registered relative build path unless the documented handle filename form is
deliberately used.

1. After the JavaScript build, `wp i18n make-pot` extracts PHP and the
   registered build JavaScript to POT. Exclude `src` so the PO cannot acquire a
   source-path reference that disagrees with the registered script path.
2. Maintain `<domain>-<locale>.po` against the POT.
3. `wp i18n make-mo` creates `<domain>-<locale>.mo` in `languages/`.
4. `wp i18n make-json --no-purge` creates Jed JSON from the same PO.

A requested check of runtime loading sets the site locale, then the
admin-user locale, verifies `determine_locale()`, and asserts one genuinely
translated PHP string and one translated React string in a browser.

When the selected release process uses authored POT and PO files, keep them
together with the MO and path-hashed Jed JSON files that process requires.
Regenerate the affected files after a translatable string or the build path
changes. Another delivery mechanism keeps its own set of files. A
readiness-only task needs none of them.

POT extraction, a PO file, or hard-coded translated text does not prove runtime
loading.
