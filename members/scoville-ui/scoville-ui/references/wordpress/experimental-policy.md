# Experimental components

Availability alone is not opt-in; use `allow` only for explicit bundled WPDS
opt-in. Stable `Flex` remains available under every policy value. A provider
never forces a PHP page into React. Apply the policy gates in routing.md.

### Bundled experimental WPDS

- Requires an explicit project choice, exact package versions, public package
  APIs, and the exported design-token stylesheet.
- `@wordpress/ui`, `@wordpress/theme`, and `@wordpress/admin-ui` are an
  experimental bundled path at the WordPress 7.0 target.
- `ThemeProvider` is not a public runtime export at this pin. Never unlock
  private APIs from plugin code on any version.
- Consume semantic tokens only when the selected exported stylesheet supplies
  them. The supported baseline uses default density.
- These package pins describe 7.0, not all WordPress 7 releases. On 7.1 use
  Core's token stylesheet instead of a second copy, and independently verify
  compatibility of any opted-in bundled component package.

For the 7.0 bundled Stack, set direction and semantic gap explicitly; it has
neither default.
