# WordPress 7.0 and 7.1 source contracts

## Pinned WordPress 7.0 repository state

| Owner | Ref and resolved commit | Target packages |
| --- | --- | --- |
| `WordPress/wordpress-develop` | `7.0` at `90a615f1834824d2583a43bfc698d9c710e5c094` | WordPress 7.0 admin source |
| `WordPress/gutenberg` | `wp/7.0` at `28c0dedc4eaf001a24237a1fbba4b0887698b000` | `@wordpress/ui` 0.7.1, `@wordpress/theme` 0.7.1, `@wordpress/admin-ui` 1.8.1, `@wordpress/components` 32.2.1 |
| `WordPress/WordPress` | tag `7.0` at `b16cd68ea199838d8f9daf0ff7e3f35042ba0ad0` | WordPress 7.0 runtime |

## WordPress 7.1 theming contract

The 7.0 package restrictions above remain scoped to their pins, not to all
WordPress 7 releases.

- `WordPress/WordPress` tag `7.1` resolved to
  `b998fef9238af183f9523b3df71618e6e57498b6`. Its
  [script-loader.php](https://github.com/WordPress/WordPress/blob/b998fef9238af183f9523b3df71618e6e57498b6/wp-includes/script-loader.php)
  registers the `wp-theme` style handle with the Core design-token stylesheet.
- `@wordpress/theme` 1.0.0 was published at Gutenberg commit
  `7fe6fa42d4cf9cdd084223e3150f796567914f87`. Its
  [theme runtime entry](https://github.com/WordPress/gutenberg/blob/7fe6fa42d4cf9cdd084223e3150f796567914f87/packages/theme/src/index.ts)
  publicly exports `ThemeProvider`. Its pinned README and implementation own
  the 7.1 prop and wrapper contract.
- The [7.1 Dev Note](https://make.wordpress.org/core/2026/07/31/design-system-theming-in-wordpress-7-1/)
  documents plugin use of the Core stylesheet, direct semantic tokens for
  plugin-specific CSS, and the separate public JavaScript provider.
- The [package reference](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-theme/)
  documents stylesheet ownership, scoped theming, and the distinction between
  inside-WordPress and standalone applications. It is a moving reference, not
  proof that every currently documented prop exists in every 7.x release.

The stable 7.1 tag and inspected 7.1 Core source agree on style registration,
semantic gap and padding tokens, and the public JavaScript export. That shows
the source, not that a real plugin page enqueues it or looks right.

[version-compatibility.md](version-compatibility.md) has the enqueue example
and its checks.

## Classic source and token separation

The 7.1 patterns in [classic-patterns.md](classic-patterns.md) were checked
against the immutable Core ref above. That shows where the values come from,
not a loaded page or its geometry. Keep declarations in their original units. The WPDS matrices are in [wpds-tokens.md](wpds-tokens.md). The fallback
scale is labeled Skill-Norm and never becomes a Classic compliance scale.

## Primary owners by fact

| Fact | Primary source |
| --- | --- |
| Classic shell, `.wrap`, heading, and `782px` behavior | pinned `wp-admin/css/common.css` |
| Form-table rhythm, mobile form reflow, and mobile controls | pinned `wp-admin/css/forms.css` |
| Notice relocation and `.inline` behavior | pinned `src/js/_enqueues/admin/common.js` |
| Settings and menu APIs | WordPress Plugin Handbook and Code Reference |
| WPDS gap, padding, density, public exports, and semantic-token policy | pinned `@wordpress/theme` package exports, runtime index, exported design-token CSS, README, and `dimension.json` |
| Experimental bundled UI and `Stack` direction/gap behavior | pinned `@wordpress/ui` README and source |
| Modern `Page` shell | pinned `@wordpress/admin-ui` source |
| Stable `Flex` contract | pinned `@wordpress/components` source and official component reference |
| PHP and JavaScript i18n | WordPress Plugin Handbook, Common APIs, Block Editor Handbook, Code Reference, and WP-CLI i18n commands |
| Accessibility | WordPress Accessibility Coding Standards and WCAG 2.2 |
| Host mechanisms of routing.md's excluded surfaces: editor SlotFills, Panel components, block supports, metabox, Dashboard widget, profile and list-table hooks | Block Editor Handbook, Plugin Handbook, Common APIs and Code Reference |

Official entry points:

- <https://developer.wordpress.org/plugins/settings/settings-api/>
- <https://developer.wordpress.org/plugins/administration-menus/>
- <https://developer.wordpress.org/block-editor/reference-guides/components/>
- <https://developer.wordpress.org/coding-standards/wordpress-coding-standards/accessibility/>
- <https://www.w3.org/TR/WCAG22/>
- <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/>
- <https://developer.wordpress.org/apis/internationalization/internationalization-guidelines/>
- <https://developer.wordpress.org/block-editor/how-to-guides/internationalization/>
