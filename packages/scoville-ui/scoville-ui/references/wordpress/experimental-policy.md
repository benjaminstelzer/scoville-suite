# Bundled experimental WPDS at the WordPress 7.0 pin

This file holds the bundled experimental WPDS packages at the WordPress 7.0
pin: what they require, the density they support, and their `Stack` and
token-stylesheet example. Read it before any change or advice in a region
that uses these packages or would add them. Whether a project may add them is
[routing's opt-in rule](routing.md#choose-the-runtime-per-region). Core tokens
and the public provider on 7.1 and later are in
[version-compatibility.md](version-compatibility.md).

## Requirements

- `@wordpress/ui`, `@wordpress/theme` and `@wordpress/admin-ui` are an
  experimental bundled path at the WordPress 7.0 target.
- Use exact package versions, public package APIs and the exported
  design-token stylesheet.
- `ThemeProvider` is not a public runtime export at this pin.
- Consume semantic tokens only when the selected exported stylesheet supplies
  them. The supported baseline uses default density; a non-default density
  needs a future public provider contract and is unavailable at this pin.
- These package pins describe 7.0, not all WordPress 7 releases. On 7.1,
  follow [version-compatibility.md](version-compatibility.md) for the token
  stylesheet, and independently verify compatibility of any opted-in bundled
  component package.
- Do not change an existing Classic page to this runtime merely to obtain
  spacing tokens.

## Stack and token stylesheet

The 7.0 bundled `Stack` has neither a default direction nor a default
semantic gap; set both explicitly:

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

`2xl` means the supplied WPDS gap token, whose default is `32px`; it is not
the padding token with the same name.

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

This recipe is for the 7.0 pin only. On 7.1 and later, use the
[versioned PHP example](version-compatibility.md#php-layout-with-a-core-token-and-older-version-branch)
instead.
