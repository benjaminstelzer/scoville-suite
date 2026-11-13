# WordPress validation additions

When Scoville UI selects [common validation](../validation.md), read it once
and add these platform checks for the same statements and scope. Find the
WordPress element to compare with through [spacing.md](spacing.md). Judge
Classic, token and fallback values each by its own reference; native values
need not match the fallback scale.

## Select the platform checks

Select widths, content and states that can change the scoped result:

| Trigger | Required evidence |
| --- | --- |
| Affected Core mobile-admin transition | Check `782px` and `783px`, immediately above the `<=782px` boundary. |
| Reflow or affected web UI with an AA target | Apply [common Validation's reflow and accessibility checks](../validation.md#derive-the-test-surface), including applicable 320 CSS px reflow and zoom. |
| Wrapping, grouping, visibility, content or state-dependent layout | Use realistic long or doubled text, locale-dependent dates/numbers, empty content and changed states where they can affect the result; inspect the affected group's layout and focus. |
| Language-scoped RTL | Apply [internationalization's RTL rule](internationalization.md#language-scoped-rtl-checks). |
| Plugin-specific semantic state colors | Verify token resolution, contrast and non-color cues in the actual theme and affected interaction states. Official tokens alone prove no accessibility result. |
| CSS exception | Apply the above affected cases and the [common styling-exception contract](../validation.md#styling-exceptions). |

Source-only work needs no browser; report its rendering limits. Say for each
statement whether it rests on source, measurement, viewing, interaction or is
unverified.

## WordPress runtime evidence

For a statement about the rendered page:

- Check actually loaded styles, their order and consumed tokens.
  Registration and a file on disk do not show page loading.
- Read the final DOM after Core Notice relocation.
- Compare `.notice`, `.updated` and `.error` by their actual classes and
  parent, including narrow-width specificity.
- For a Classic audit target use [classic-patterns.md](classic-patterns.md).

For a version-sensitive result:

- Name the minimum supported and the actually tested WordPress versions, and
  the token stylesheet's source, token names, loading and fallback evidence.
- Stable 7.0/7.1 examples establish neither 6.x nor future/prerelease support.
- Apply [version-compatibility.md](version-compatibility.md)'s assertions for
  consumed tokens/providers on each supported release; numeric fallback does
  not excuse failed token acceptance.
- Source inspection or stubbed enqueue tests do not prove rendered behavior.
