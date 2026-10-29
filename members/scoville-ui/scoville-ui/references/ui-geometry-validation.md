# Geometry and sight validation

## Measure relationships, not declarations

For each selected relationship:

1. Before measurement, name reference elements/edges, expected relationship,
   independent source and justified tolerance. Sources may be an unchanged owner
   contract, suitable reference or greenfield direction derived from the brief
   before implementation. Candidate CSS and equally wrong peers supply no target.
2. Settle required fonts, content and transitions; inspect relevant loaded styles
   and final DOM. A substituted or blocked required font invalidates dependent
   measurements. Compare peers under equivalent roles, variants, states,
   typography and layout; explain intended differences.
3. Compare each selected measurement with its target in code before display under
   the [writing rules](writing.md). Report expected relationship/source, actual
   value, tolerance and result; revision, state and viewport may appear per group.

Choose tolerance before results; no universal pixel tolerance applies. An
unresolved target remains unresolved. Geometry proves only the measured
relationships under the reported conditions, not optical quality or page coverage.

Use an existing report or task result, without a prescribed table or new file.

Keep the authored unit or expression, computed value and measured distance separate.
Preserve `em`, `rem`, `px`, percentages, unitless line-height, token references,
calculations and logical properties. Equal current pixels do not authorize
substitution. Record the relevant element or root font or container basis.

For ordered non-overlapping boxes, `B.top - A.bottom` measures border-box
separation, not glyph whitespace or a baseline. Account for flow, collapsing,
padding/borders, line boxes, wrapping and rounding. Summed declarations are not
observed geometry; minimum height is not fixed height.

## Inspect with a comparison and a hypothesis

View the scoped region in context first, then details at a consistent scale.
Keep an unaltered context image or crop when guides help comparison. For each
applicable concern, record a located deviation or scoped pass. Explain relevant
exclusions without producing boilerplate for unrelated lenses.

| Look for | Compare |
| --- | --- |
| Grouping and rhythm | Equivalent relationships within and across sections |
| Content edges and text alignment | Intended shared edge, top, baseline or center, not an assumed universal alignment |
| Apparent whitespace | Line boxes and glyph position alongside measured box gaps |
| Components, including status text, controls and icons | Intended internal text and icon placement as well as outer alignment; check unintended parent stretching and wrapped neighbors |
| Content and state changes | Wrap, clipping, overlap, hidden-content holes and reading order |

Equal outer boxes can have displaced text or icons. View the difference, then
inspect font/line-height, padding, alignment and icon metrics as relevant;
outer rectangles cannot establish baselines. Measure and view internal content
as well as outer layout when claimed; container overflow alone proves no
internal alignment. Preserve intended native variant differences. Report
unresolved optical questions as unverified.

Refresh affected evidence under [Validation](validation.md#select-and-refresh-evidence).
Zoom alone does not test whether `em`, `rem` and fixed pixels behave equivalently.
Where units are at risk, vary element or root font conditions independently.
