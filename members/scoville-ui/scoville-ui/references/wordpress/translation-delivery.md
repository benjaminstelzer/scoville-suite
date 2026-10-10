# Bundled translation delivery

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

Register the JavaScript handle first, attach translations to that exact handle
and literal domain with an explicit language path, then enqueue:

```php
$asset = require plugin_dir_path( __FILE__ ) . 'build/index.asset.php';

wp_register_script(
    'plugin-slug-app',
    plugins_url( 'build/index.js', __FILE__ ),
    $asset['dependencies'],
    $asset['version'],
    true
);

wp_set_script_translations(
    'plugin-slug-app',
    'plugin-slug',
    plugin_dir_path( __FILE__ ) . 'languages'
);

wp_enqueue_script( 'plugin-slug-app' );
```

The build-generated dependency list is authoritative. This prevents missing
runtime handles such as `react` or `react-jsx-runtime` when the build emits
them.

## Optional PO-based delivery example

Use this chain only when producing bundled translations is part of the task
and the project chooses a PO-based workflow. It is not a readiness checklist
or the only supported way to deliver translations.

Before extraction, align PO source references with the registered `build/index.js`,
not `src/index.js`. Generated filenames use the MD5 of the registered relative
build path unless the documented handle filename form is deliberately used.

1. After the JavaScript build, `wp i18n make-pot` extracts PHP and the
   registered build JavaScript to POT. Exclude `src` so the PO cannot acquire a
   source-path reference that disagrees with the registered script path.
2. Maintain `<domain>-<locale>.po` against the POT.
3. `wp i18n make-mo` creates `<domain>-<locale>.mo` in `languages/`.
4. `wp i18n make-json --no-purge` creates Jed JSON from the same PO.
5. Set site locale, then admin-user locale, and verify `determine_locale()`.
6. Assert one genuinely translated PHP string and one translated React string
   in a browser.

When translation delivery is in scope, keep the target project's authored POT
and PO files together with the generated MO and path-hashed Jed JSON required by
its release process. Regenerate them after translatable source or build-path
changes. These artifact requirements do not apply to a readiness-only task.

POT extraction, a PO file, or hard-coded translated text does not prove runtime
loading.
