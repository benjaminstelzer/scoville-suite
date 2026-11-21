# WordPress validation additions

The WordPress checks for a rendered check of a `wp-admin` page. Read this
file together with [common validation](../validation.md), which it extends
for the same statements and scope. Judge
Classic, token and fallback values each by its own reference.

## Select the platform checks

Select widths, content and states that can change the scoped result:

| Trigger | Required evidence |
| --- | --- |
| Affected Core mobile-admin transition | Check `782px` and `783px`, immediately above the `<=782px` boundary. |
| Wrapping, grouping, visibility, content or state-dependent layout | Use realistic long or doubled text, locale-dependent dates/numbers, empty content and changed states where they can affect the result; inspect the affected group's layout and focus. |
| Language-scoped RTL | Apply [internationalization's RTL rule](internationalization.md#language-scoped-rtl-checks). |
| Plugin-specific semantic state colors | Verify token resolution in the actual theme and the affected interaction states. Contrast follows [ui-guidance](ui-guidance.md#components-and-accessibility), color cues [adapter row 9](adapter.md#classic-plugin-page-checklist). Official tokens alone prove no accessibility result. |
| CSS exception | Apply the above affected cases and the [styling-exception rule](../../SKILL.md#custom-styling). |

## WordPress runtime evidence

For a statement about the rendered page:

- Check actually loaded styles, their order and consumed tokens.
  Registration and a file on disk do not show page loading.
- Read the final DOM after Core Notice relocation.
- Compare `.notice`, `.updated` and `.error` by their actual classes and
  parent, including narrow-width specificity.
- For a Classic page, compare with [classic-patterns.md](classic-patterns.md).

For a version-sensitive result:

- Name the WordPress versions you tested; for a region that consumes tokens,
  also the token stylesheet's source and loading evidence.
- Stable 7.0/7.1 examples establish neither 6.x nor future/prerelease support.
- Apply [version-compatibility.md](version-compatibility.md)'s assertions for
  consumed tokens/providers on the releases you test.
- A source review or stubbed enqueue tests do not prove rendered behavior.
