# WordPress runtime examples

This file holds one example for each of three runtimes a supported plugin page
can use: a Classic Settings API page, a React region with Core Components, and
a PHP shell with a React root. Read it only when a syntax or composition
question is still open after the references for the focus, and read only the
section for the region's runtime, which routing establishes. An example shows
one runtime; do not copy it to another.

Other examples sit with their rules: Core tokens, the older-version fallback
and the public React provider in
[version-compatibility.md](version-compatibility.md), for a layout
relationship Core leaves unspaced; bundled experimental WPDS at the 7.0 pin in
[experimental-policy.md](experimental-policy.md); script registration with
translations in
[internationalization.md](internationalization.md#prepare-loading-without-requiring-catalogs).

## Classic Settings API

PHP with Core.

```php
function plugin_slug_render_settings_page() {
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_die( esc_html__( 'You are not allowed to manage these settings.', 'plugin-slug' ) );
    }
    ?>
    <div class="wrap">
        <h1><?php echo esc_html( get_admin_page_title() ); ?></h1>
        <hr class="wp-header-end">

        <form action="options.php" method="post">
            <?php
            settings_fields( 'plugin_slug_settings' );
            do_settings_sections( 'plugin-slug' );
            submit_button( __( 'Save settings', 'plugin-slug' ) );
            ?>
        </form>
    </div>
    <?php
}
```

## React with Core Components

Core Components, without an experimental opt-in.

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

export function ConnectionSettings( { error, onSave } ) {
    const [ endpoint, setEndpoint ] = useState( '' );

    return (
        <>
            <h2>{ __( 'Connection', 'plugin-slug' ) }</h2>
            <p>{ __( 'Configure the endpoint used by this connection.', 'plugin-slug' ) }</p>
            <Flex
                direction="column"
                align="stretch"
                justify="flex-start"
                wrap={ false }
                expanded={ true }
                gap={ 3 }
            >
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
                    <Button
                        variant="primary"
                        onClick={ () => onSave( endpoint ) }
                        __next40pxDefaultSize
                    >
                        { __( 'Save connection', 'plugin-slug' ) }
                    </Button>
                </FlexItem>
            </Flex>
        </>
    );
}
```

The [Core Components recipe](spacing.md#core-components) sets this `Flex`.
The heading and intro keep their native margins outside the `Flex`.
`gap={ 3 }` expresses the `12px` Skill-Norm relationship between the elements
of one field group through the component's 4-px multiplier. The children are
intrinsic, so they use `FlexItem`.

## Hybrid shell and React root

Hybrid: a PHP shell with Core and a Core Components root.

```php
<div class="wrap">
    <h1><?php echo esc_html( get_admin_page_title() ); ?></h1>
    <hr class="wp-header-end">
    <div id="plugin-slug-app"></div>
</div>
```

The PHP shell renders the title, and Core places page-level Notices after
`.wp-header-end`. The React root renders and spaces only its descendants. A field error belongs inside the React field
region. Do not wrap the entire `.wrap` in another spacing system.
