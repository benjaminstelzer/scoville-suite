# WordPress validation additions

When the claims trigger [common validation](../validation.md), read it once and
apply these platform checks for the claims and scope it establishes. Resolve
WordPress comparison targets through [spacing.md](spacing.md). Keep Classic,
token and fallback contracts distinct; native values need not match the fallback
scale.

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

`600px` and `390px` are optional intermediate Skill-Norm samples for transitions
that occur there, not universal WordPress breakpoints or mandatory test widths.
Source-only work needs no browser; report its rendering limits. Partial samples
cannot establish a full-page pass. Distinguish source, measured, viewed,
interacted and unverified evidence according to the claim.

## WordPress runtime evidence

For rendered claims, check actually loaded styles, their order and token
availability where consumed.
Registration and a file on disk do not establish page loading. Read the final
DOM after Core Notice relocation. Compare `.notice`, `.updated` and `.error`
using their actual classes and parent, including narrow-width specificity.
For Classic audit targets use [classic-patterns.md](classic-patterns.md).

Version-sensitive results distinguish minimum supported and actually tested
WordPress versions and name the token stylesheet owner/names, loading and fallback
evidence. Stable 7.0/7.1 examples establish neither 6.x nor future/prerelease
support. Apply [version-compatibility.md](version-compatibility.md)'s assertions
for consumed tokens/providers on each supported release; numeric fallback does
not excuse failed token acceptance. Source inspection or stubbed enqueue tests
do not prove rendered behavior.
