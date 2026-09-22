# Cartography and spatial data

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-CARTOGRAPHY`, `SRC-DATA-CANON`, `SRC-DATA-EMPIRICAL`, `SRC-CULTURE-AUTHORITY`, `SRC-PEOPLE-PRIVACY`, `SRC-SOURCE-EVIDENCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when location, distance, direction, extent, topology, region, route,
boundary, place name, spatial uncertainty, or geographic distribution can
change the design or verdict. Load for deciding map versus non-map, not merely
after a map has been requested. Do not load for a location list that needs no
spatial reasoning, generic background maps, ordinary coordinate plumbing, or
relational diagrams whose geometry is not geographic.

## Inputs and formal variables

Record only open relevant fields; otherwise use the Core minimal record:

- `Q`: spatial question, audience task, decision, consequence, map-versus-
  non-map alternative, and prohibited inference;
- `G`: geometry type, coordinate reference, spatial unit/resolution, extent,
  scale, projection, topology, geocoding quality and generalization;
- `D`: source/version, observation time, boundary vintage, grain, value type,
  denominator, normalisation, classification, uncertainty, no-data and update
  path;
- `A`: publisher/jurisdiction, place-name and boundary authorities, affected
  people or custodians, contested positions, required scripts and notices;
- `P`: sensitive people, homes, resources or sites; re-identification and
  aggregation risk; permitted accuracy and disclosure;
- `M`: print/web/static/interactive destinations, size, zoom, locale,
  accessible alternative and receiver evidence;
- `E`: inspected source, GIS/domain, authority, privacy, render and user
  evidence, with unknowns explicit.

Never infer `A`, a neutral boundary, a safe disclosure level, or an individual
condition from a plausible basemap or model familiarity.

## Generate and decide

1. **Test map necessity.** Use a map when spatial position, proximity, route,
   pattern or regional context is part of the question. Compare a chart, table
   or ranked list when shape mainly obstructs a quantitative comparison.
2. **Choose the spatial frame from the question.** Projection, centre, extent,
   crop, scale and generalization redistribute error and attention. State which
   properties must be preserved and what distortion is accepted; do not choose
   a familiar projection as a neutral default.
3. **Match value to mark.** Choropleth colour normally represents a defensible
   rate, ratio or other normalized value with its denominator; proportional
   symbols can represent totals. Match sequential, diverging or categorical
   treatment to actual order and reference meaning. Show no-data separately.
4. **Make classification inspectable.** Record method, breaks, class count,
   inclusivity, outliers and whether breaks are shared across comparable maps.
   Prefer continuous or unclassified views when classes invent a conclusion;
   never tune breaks merely for visual drama.
5. **Bound spatial inference.** Describe results at the observed unit. Do not
   infer individual behaviour from area aggregates, treat geocoding as exact,
   or hide aggregation, resolution, sample change or spatial uncertainty.
6. **Treat names and boundaries as authored claims.** Record source, vintage,
   jurisdiction/publisher position, affected authority, alternate names/scripts
   and dispute notation. Preserve qualifiers across crops and variants.
7. **Protect sensitive geography.** Minimize collection and displayed
   precision; consider aggregation, withholding, generalized areas or safe
   alternatives according to accountable privacy/domain authority. Cosmetic
   jitter, blur or omission does not by itself prove protection.
8. **Design the reading system.** Coordinate figure-ground, labels, symbols,
   legend, source/date, uncertainty, basemap and annotations. Include scale,
   direction or inset only when it supports the task; ensure small regions and
   dense labels do not silently disappear.

## Repair labels at the target scale

For a crowded point pair, keep the feature coordinates fixed and compare
several label positions with explicit association. Prefer candidates that
avoid the other symbol, label and consequential geometry; block positions
that would imply the wrong feature. If displacement becomes ambiguous, compare
a leader or inset rather than moving the site or hiding a required name.

For a line feature, compare a label following a readable portion of its course
with a clearly associated horizontal label. Choose the segment and orientation
so the name belongs to the intended line, not a nearby crossing; any separate
smoothed label path must not replace the source geometry. Repeat a name only
where it helps readers recover the same feature across the view.

For an area, try an interior label that reads as belonging to the region and
does not cross a hole or neighbouring boundary. If the region is too narrow,
compare an exterior label with an explicit callout anchored to that region.
Do not move or enlarge the polygon to fit its name. Distinguish this area
association from a point's positional label and a line's directional reading;
inspect both the name and its feature at the required output sizes.

Inspect the same extent at both required scales. A solution at the larger
size may collide after reduction even though geographic positions are correct.
Retain task-critical features and labels; reduce optional background detail,
split a view or provide an explicit alternative when everything cannot fit.
Any geometric generalization must preserve the supplied spatial invariants
and accountable authority. It is not a licence to move boundaries for polish.
This original procedure draws on configurable placement candidates, not a
universal preferred corner, label distance or automatic GIS correctness claim.

## Critique: failure signatures and causes

| Failure signature | Likely parent cause to test |
| --- | --- |
| Map mostly shows population or polygon area | raw totals in choropleth, wrong denominator, or area-biased mark |
| Pattern changes dramatically with styling | unstable classification, arbitrary extent/projection, outlier handling or incomparable breaks |
| Empty region reads as zero | no-data, suppressed, outside-scope and true zero were merged |
| Small regions or routes vanish | unsuitable scale/generalization, occlusion, line hierarchy or label priority |
| Map implies precise people-level conclusion | ecological inference, coarse aggregation, uncertain geocoding or unsupported causality |
| Boundary/name appears official or neutral | authority, vintage, dispute, script or publisher position is unstated |
| Sensitive site can be recovered | precision, joins, labels, metadata or surrounding context defeats protection |
| Geography adds shape but not insight | spatial question was never established; non-map comparison is stronger |

Localise findings to the exact feature, zoom/size, dataset and authority state.
Separate visible encoding defects from GIS correctness, political/cultural
authority, privacy, and preference.

## Smallest repair, preservation, and regression

Freeze supplied evidence and authorised positions. Diagnose: map necessity ->
source/boundary/grain -> denominator/normalisation -> projection/extent ->
classification/mark -> label/legend/composition. Repair or replace the earliest
cause, then regenerate all legends, annotations, alternatives and variants.
Preserve valid spatial context, supplied values, authorised names, uncertainty,
privacy floors and working visual hierarchy. Reject a cosmetic recolour when
normalisation is wrong, or a cleaner crop that erases disputes, small regions,
routes or required context. Recheck whether the repaired map still beats its
non-map control for `Q`.

## Rule classes and exceptions

Supplied spatial facts, current accountable authority, privacy restrictions,
required notices and applicable destination contracts are binding. Projection
and graphical-perception evidence is bounded by property and task. Map types,
classification methods, north arrows, scale bars, insets, label density and
basemap detail are contextual conventions, not universal recipes.

A cartogram, schematic map, distorted extent, discontinuous territory, unusual
orientation, locally preferred name or omitted sensitive feature may be valid
when the purpose and authority are recorded, distortion/omission is legible,
required relations remain recoverable, privacy and access survive, and a
conventional control does not serve the protected task better. Style never
waives geoprivacy or contested-name/boundary accountability.

## Proof, ownership, and claim ceiling

Recompute rates and classifications; verify geometry, coordinate reference,
boundary vintage, place-name records, source/date, joins and no-data states.
Compare projection/extent and map/non-map alternatives; inspect representative
small/large regions, labels, legends and dispute notices across print/web,
narrow/wide and relevant zoom states. Test the accessible data/description
against the same snapshot. Obtain accountable review for sensitive or
contested release and label missing authority `unverified`.

Cartography owns map choice and spatial encoding intent. GIS/statistical/domain
owners validate geometry, transformations and inference; culture/publisher or
geospatial authorities decide contested representation; privacy owners decide
safe disclosure; UI and Production prove interaction and delivery. A map render
does not prove boundary neutrality, political recognition, privacy, individual
behaviour, causal explanation, cartographic correctness, comprehension, or
fitness outside the tested question and authority context.
