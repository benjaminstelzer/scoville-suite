# Runtime-owned examples

Classify the region first. Each example holds for one runtime; do not copy
it to another.

## Classic Settings API

**Surface:** plugin settings. **Support:** supported. **Runtime:** PHP with Core.
**Shell:** Core. **Spacing:** Core. **Token owner:** none. **Experimental
policy:** deny.

```php
function plugin_slug_render_settings_page() {
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_die( esc_html__( 'You are not allowed to manage these settings.', 'plugin-slug' ) );
    }
    ?>
    <div class="wrap">
        <h1><?php echo esc_html( get_admin_page_title() ); ?></h1>
        <hr class="wp-header-end">

        <?php settings_errors(); ?>

        <form action="options.php" method="post">
            <?php
            settings_fields( 'plugin_slug_settings' );
            do_settings_sections( 'plugin-slug' );
            submit_button( esc_html__( 'Save settings', 'plugin-slug' ) );
            ?>
        </form>
    </div>
    <?php
}
```

Do not add a page gutter, form-row grid, custom button, or stack gap over
`.form-table`. A plugin-owned subcomponent may add a local flow only after
you checked that Core does not already space it.

This remains valid on 7.1 without any token or React migration. For a genuine
missing PHP layout relationship, the
[versioned examples](version-compatibility.md) show optional Core tokens, the
older-version fallback, and the public React provider separately.

## React with Core Components

**Surface:** plugin workflow. **Support:** supported. **Runtime:** Core
Components. **Shell:** Core plus plugin root. **Spacing:** specialized
components, then stable `Flex`. **Token owner:** Core component props and
default CSS. **Experimental policy:** unknown, therefore no new experimental
component.

```jsx
import {
    Button,
    Flex,
    FlexItem,
    Notice,
    TextControl,
} from '@wordpress/components';
import { useState } from '@wordpress/element';
import { __ } from '@wordpress/i18n';

export function ConnectionSettings() {
    const [ endpoint, setEndpoint ] = useState( '' );
    const [ error, setError ] = useState( '' );

    return (
        <Flex
            direction="column"
            align="stretch"
            justify="flex-start"
            wrap={ false }
            expanded={ true }
            gap={ 4 }
        >
            <FlexItem>
                <Flex
                    className="plugin-slug-heading-flow"
                    direction="column"
                    align="stretch"
                    justify="flex-start"
                    wrap={ false }
                    expanded={ true }
                    gap={ 2 }
                >
                    <FlexItem className="plugin-slug-heading-item">
                        <h2>{ __( 'Connection', 'plugin-slug' ) }</h2>
                    </FlexItem>
                    <FlexItem className="plugin-slug-heading-item">
                        <p>{ __( 'Configure the endpoint used by this connection.', 'plugin-slug' ) }</p>
                    </FlexItem>
                </Flex>
            </FlexItem>
            { error && (
                <FlexItem>
                    <Notice status="error" isDismissible={ false }>
                        { error }
                    </Notice>
                </FlexItem>
            ) }
            <FlexItem>
                <TextControl
                    label={ __( 'Endpoint URL', 'plugin-slug' ) }
                    help={ __( 'Enter the complete HTTPS endpoint.', 'plugin-slug' ) }
                    value={ endpoint }
                    onChange={ setEndpoint }
                    __next40pxDefaultSize
                />
            </FlexItem>
            <FlexItem>
                <Button variant="primary" __next40pxDefaultSize>
                    { __( 'Save connection', 'plugin-slug' ) }
                </Button>
            </FlexItem>
        </Flex>
    );
}
```

This explicit Flex prop combination is Skill-Norm composition, not Core
component defaults or a Classic normalization target. Use it only for a new
plugin-owned relationship that no existing component or prop spaces.

`gap={ 4 }` expresses the `16px` Skill-Norm relationship between related
setting groups through the component's 4-px multiplier. The nested
`gap={ 2 }` sets the `8px` heading-to-intro relationship. Reset only the native
heading and paragraph margins inside `.plugin-slug-heading-flow` so that this
gap is the only source of that distance; do not add sibling margins. The
children are intrinsic, so they use `FlexItem`. Use `FlexBlock` only for a
child intended to grow.

```css
.plugin-slug-heading-flow > .plugin-slug-heading-item > :where(h2, p) {
    margin-block: 0;
}
```

## Bundled experimental WPDS at the 7.0 pin

**Surface:** plugin dashboard. **Support:** supported. **Runtime:** bundled
WPDS. **Shell:** Core plus plugin root. **Spacing:** public `Stack`. **Token
owner:** bundled `@wordpress/theme/design-tokens.css`. **Experimental policy:**
allow through explicit project opt-in.

This legacy pinned example is not the 7.1 enqueue recipe. Do not change an
existing Classic page to this experimental runtime merely to obtain spacing
tokens.

```jsx
import { Stack } from '@wordpress/ui';

export function DashboardRegions( { header, main, secondary } ) {
    return (
        <Stack direction="column" gap="2xl">
            { header }
            { main }
            { secondary }
        </Stack>
    );
}
```

Resolve the public CSS export during the build, copy it unmodified to the plugin
build, and enqueue that emitted stylesheet at the actual render root. Do not
import the CSS subpath from the JavaScript entry: the pinned dependency
extraction records it as a script handle.

```php
wp_enqueue_style(
    'plugin-slug-wpds-tokens',
    plugins_url( 'build/design-tokens.css', __FILE__ ),
    array(),
    $version
);
```

At the WordPress 7.0 pin, `@wordpress/theme` does not publicly export
`ThemeProvider`. The public route bundles `@wordpress/ui` plus the exported
design-token stylesheet and uses the default token values. `Stack` has neither
a default direction nor a default gap, so both are explicit. `2xl` means the
supplied WPDS gap token, whose default is `32px`; it is not the padding token
with the same name. A non-default density needs a future public provider
contract and is unavailable on this pin.

## Hybrid shell and React root

**Surface:** plugin settings. **Support:** supported. **Runtime:** hybrid.
**Shell:** Core. **Inner root:** Core Components. **Spacing:** owner per region.
**Token owner:** Core in the shell and Core Components inside the root.
**Experimental policy:** deny because every named region uses a known
non-experimental Core owner.

```php
<div class="wrap">
    <h1><?php echo esc_html( get_admin_page_title() ); ?></h1>
    <hr class="wp-header-end">
    <?php settings_errors(); ?>
    <div id="plugin-slug-app"></div>
</div>
```

The PHP shell places the title and page-level Notices. The React root renders
and spaces only its descendants. A field error belongs inside the React field
region. Do not wrap the entire `.wrap` in another spacing system.

## Documented CSS exception without Core tokens

Use custom CSS only after spacing.md's ladder is exhausted. This PHP workflow
region needs a responsive card grid. Core has no layout primitive for it, and
Core Components `Flex` is not available in the PHP runtime. This is an
explicit older-version fallback, not the default for a 7.1 region with
supported Core tokens. Test it on each older supported baseline.

```css
.plugin-slug-summary-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
    gap: 16px;
}
```

Record `16px` as the Skill-Norm relationship for related summary groups, not a
WordPress token. Keep the selector inside the plugin root and select affected
layout cases through [WordPress validation](validation.md#select-the-platform-checks).
For a 7.1 token branch, use the versioned example instead of combining both
rules.

## i18n registration for React

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
    'plugin-slug'
);

wp_enqueue_script( 'plugin-slug-app' );
```

Use the dependency and version data generated for the built entry; do not
write the dependency list by hand. Binding the registered handle to the domain
prepares standard translation loading before any catalog exists. Pass a third,
custom-path argument only when the selected delivery mechanism needs it. When
producing translations is in scope, check the chosen files against the
registered build path and prove they load. A readiness-only task creates no
PO files and needs no translated PHP or React strings.
