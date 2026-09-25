# Versioned Core tokens and public theming

Read this after routing. WordPress version, CSS token availability, and React
component ownership are independent facts. Do not migrate an existing Classic
page merely because a newer WordPress version offers tokens.

The missing relationship must be established from actual native markup and
component options before using the examples. Preserve source units and token
expressions. Resolved pixels in verification are evidence for a named state,
not replacement source declarations. See [classic-patterns.md](classic-patterns.md)
for native relationships and [wpds-tokens.md](wpds-tokens.md) for token facts.

## Compatibility rules

1. Keep native markup, default spacing, buttons, inputs, tables, and Notices.
   No new stylesheet or provider is needed when these already meet the task.
2. For a genuine plugin-owned layout gap on 7.1, use supported semantic tokens
   from Core `wp-theme`. This does not introduce experimental components.
3. Inside WordPress, use its registered stylesheet. Do not ship a second token
   copy or deregister/replace the Core handle. Registration of a script called
   `wp-theme` does not establish registration of the stylesheet, or vice versa.
4. Verify the stylesheet in the actual document and every required token at
   the consuming element. A registered or queued handle alone is not proof.
5. For older supported versions without the stylesheet, preserve Core defaults.
   Only missing plugin layout relationships receive an explicitly tested,
   narrowly scoped Skill-Norm fallback. Never add an unregistered dependency.
6. On 7.1, `ThemeProvider` is public. On the pinned 7.0 package it is not.
   Private API unlocking is forbidden in both cases. A PHP page needs no React
   conversion, and a React page needs no provider without a theming requirement.

## PHP layout with a Core-token and older-version branch

This example adds a grid only for a new plugin-owned summary region that has
no native layout owner. It is not applied to `.wrap`, `.form-table`, or native
controls. The plugin main file defines this hook. Replace the example page hook
with the actual value returned by the menu registration API.

```php
function plugin_slug_enqueue_summary_layout( $hook_suffix ) {
    if ( 'settings_page_plugin-slug' !== $hook_suffix ) {
        return;
    }

    $wp_version      = wp_get_wp_version();
    $is_core_71      = 1 === preg_match( '/^7\.1(?:\.\d+)?$/', $wp_version );
    $has_core_tokens = $is_core_71
        && wp_style_is( 'wp-theme', 'registered' );
    $dependencies   = $has_core_tokens ? array( 'wp-theme' ) : array();

    wp_enqueue_style(
        'plugin-slug-summary-layout',
        plugins_url( 'assets/summary-layout.css', __FILE__ ),
        $dependencies,
        '1.0.0'
    );

    // Only stable 7.0/7.1 are covered here. Other minors and prereleases are
    // unverified; the numeric fallback is not evidence of version support.
    $gap = $has_core_tokens ? 'var(--wpds-dimension-gap-lg)' : '16px';
    wp_add_inline_style(
        'plugin-slug-summary-layout',
        '.plugin-slug-summary-grid { gap: ' . $gap . '; }'
    );
}
add_action( 'admin_enqueue_scripts', 'plugin_slug_enqueue_summary_layout' );
```

The plugin's `assets/summary-layout.css` contains only the missing layout:

```css
.plugin-slug-summary-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
}
```

On verified 7.1, the dependency causes Core's tokens to load before the plugin
layout. On the verified 7.0 baseline without that style registration, the
explicit `16px` Skill-Norm fallback expresses related summary groups. It does
not pretend to be a WordPress token and does not copy Core token definitions.
The example introduces no new plugin spacing variable or token namespace.

The stable WordPress minor-line gate and registration check select between already
verified compatibility paths. Registration alone is not a capability check:
the Gutenberg plugin or another plugin may register the same global handle on
an older Core release. An approved backport needs its own explicit, tested
capability branch with verified provenance and token names.
This example's verified matrix is stable 7.0.x and 7.1.x only. Prereleases and
other minor lines are excluded. A numeric branch on another version is not
evidence of support, and must not be accepted without revalidation.

The code cannot inspect CSS token contents. On 7.1 with an unexpectedly missing
handle, its numeric branch preserves layout but the installation fails token
acceptance and must be investigated. A registered handle with missing tokens,
a failed request, or an altered registration also fails validation, even if
the page still looks plausible. Do not hand-write a numeric fallback inside
the token reference. Generated fallbacks from official build tooling do not
change this source rule or remove the rendered token check.

Existing Classic pages with no missing relationship do not call this example
and do not acquire a migration requirement. Domain states should first reuse
native Notices. A genuinely custom state may use supported semantic token
pairs, but requires contrast and non-color status cues, not just token presence.

## React with the public 7.1 provider

This is a separate, optional React capability, not the PHP loading mechanism.
For a plugin-owned React region with an actual theming requirement, use the
public export from the target's supported package entry:

```jsx
import { ThemeProvider } from '@wordpress/theme';

export function PluginThemeBoundary( { children } ) {
    return <ThemeProvider>{ children }</ThemeProvider>;
}
```

The 7.1 provider renders a wrapper `div` whose Core class uses
`display: contents`. It creates no independent layout box, but it does apply
the resolved corner-radius preset attribute even without color overrides and
does not accept wrapper customization props. Add only props verified as public
in `@wordpress/theme` 1.0.0, and only to satisfy an explicit requirement. Do not
use `isRoot` in a plugin subtree inside the Core document, unlock private APIs,
author `--wpds-*` assignments, or assume all props in moving package docs are
available in 7.1. Preserve the existing component owner.

Build against a package version compatible with the target. With WordPress
dependency extraction, verify that `build/index.asset.php` includes the
`wp-theme` script dependency and that the built entry does not bundle another
provider runtime. Enqueue `wp-theme` as a **style** dependency as well. Register
the script using the generated dependency list and bind translations as shown
in [examples.md](examples.md). Do not import the CSS subpath into the JS entry.
If supporting 7.0 too, select a separately built no-provider entry on that
version. A conditional JSX branch around a missing static export is not a
compatible fallback.

The provider does not replace the token stylesheet. CSS inheritance follows
the DOM, so check portals at their destination. Iframes and popup documents
need their own verified stylesheet loading. Avoid forwarding plugin theming
to the Core document or unrelated plugins.

## Verification and audit outcomes

| Case | Required result |
| --- | --- |
| Existing Classic page, 7.0 or 7.1 | Preserve native elements and default CSS. No mandatory tokens, React, or component conversion. |
| PHP missing layout, 7.1 | `php-core`, Core `wp-theme` style dependency, required semantic tokens resolved, no duplicate token bundle. |
| PHP missing layout, older supported version without tokens | Native elements preserved, no unregistered dependency, explicit tested local layout fallback. |
| WordPress 7.0 with an unrelated or unapproved `wp-theme` registration | Ignore it for the Core 7.1 path and use the verified older-version fallback. |
| WordPress 7.1 with the Core handle unexpectedly missing | Preserve layout with the fallback, but fail token acceptance and investigate the installation. |
| Other minors (including 7.2), prereleases or unknown version | Unverified. The numeric fallback does not establish support or pass token acceptance; verify that version separately. |
| Registered but not loaded, or required token missing | Fail loading/token acceptance. Investigate the real document and registration, not runtime classification. |
| React 7.1 public provider | Public import and Core script dependency, Core stylesheet loaded, no private APIs, no second runtime. |
| React pinned 7.0 | No public provider assumed. Preserve the tested older entry without importing that export. |
| Experimental component policy is deny | Core token stylesheet and the public 7.1 provider remain allowed when needed. No experimental component opt-in inferred. |

In a rendered check, inspect the token and its consuming property separately:

```js
const style = getComputedStyle(document.querySelector('.plugin-slug-summary-grid'));
const token = style.getPropertyValue('--wpds-dimension-gap-lg').trim();
if (!token) throw new Error('Required Core gap token is missing');
if (style.gap !== '16px') throw new Error('Unexpected gap for the verified default density');
```

On every supported stable 7.1 installation where this example is used, require
the Core handle and run the token assertion regardless of which branch the
code selected. An unexpected numeric fallback must not pass token acceptance.
On the supported 7.0 fallback, assert the computed `gap` without requiring the
token. The `16px` expectation applies to the single density shipped by the 7.1
Core stylesheet. WordPress 7.1 and `@wordpress/theme` 1.0.0 expose no public
density switch. Do not transfer the compact or comfortable 7.0 package-table
values into this path. Check successful stylesheet loading and computed styles
on each supported release. Then test
320px reflow, 782/783px, zoom, text expansion, empty content, focus,
and affected states. Add RTL checks only under the
[language-scope rule](internationalization.md#language-scoped-rtl-checks).
Any state colors require contrast tests in the actual
theme. A source check or stubbed enqueue test is not rendered UI proof.

Primary sources and immutable release refs are in [sources.md](sources.md).
