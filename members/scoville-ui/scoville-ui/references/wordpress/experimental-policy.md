# Experimental components

Only an explicit project opt-in allows bundled experimental WPDS components;
their availability is no opt-in. Stable `Flex` stays available either way. A
provider never forces a PHP page into React.

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
