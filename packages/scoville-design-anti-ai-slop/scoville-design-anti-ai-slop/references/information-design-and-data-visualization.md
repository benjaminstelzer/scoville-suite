# Information design and data visualization

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-DATA-CANON`, `SRC-DATA-EMPIRICAL`, `SRC-DATA-ACCESS-LOCALE`, `SRC-SOURCE-EVIDENCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when data must become a chart, table, dashboard, annotation system, or
accessible/responsive information graphic, or when an existing encoding or
claim is being judged or repaired. Load for material source, grain,
transformation, uncertainty, missingness, locale, interaction, or data-handoff
questions. Do not load for ordinary prose with one settled number, purely
spatial encoding, relation diagrams without quantitative fields, or visual
polish that cannot change data meaning. Those concerns retain their own owners.

## Inputs and formal variables

Inspect the data and the intended decision, not only the rendered graphic.
Record only open relevant fields; otherwise use the Core minimal record:

- `Q`: audience, question, lookup/comparison/monitoring task, decision,
  consequence, permissible claim, cadence, and freshness requirement;
- `D`: source owner, snapshot/version, extraction time, grain, keys, units,
  denominators, filters, joins, exclusions, imputation, aggregation, derived
  fields, rounding, update path, and reconciliation state;
- `V`: field roles and semantics: identifier, category, ordinal, quantity,
  time, interval, distribution, relationship, target, benchmark, or geography;
- `U`: variability, measurement/sampling/model/forecast uncertainty,
  assumptions and coverage, plus distinct zero, missing, suppressed, not
  applicable, imputed, partial-period, and stale states;
- `M`: destination, dimensions, viewing distance, interaction, print/static
  fallback, locale, language, assistive path, and responsive states;
- `P`: immutable values, definitions, source facts, protected privacy,
  incumbent visual system, and conclusions the evidence does not authorise;
- `E`: available source, calculation, structured, render, interaction, access,
  and human/domain evidence, with unverified checks named.

Freeze a reproducible displayed table and field dictionary before styling.
Keep machine values separate from localised display strings.

## Generate and decide

1. **State the reading thesis.** Name the question, comparison and conclusion
   the evidence permits. Distinguish observation, interpretation, benchmark,
   event and causal hypothesis; do not turn association into causation.
2. **Choose whether to visualise.** Use concise text for one decisive value, a
   table for exact lookup or heterogeneous records, and a chart for pattern or
   comparison. Combine overview and detail when both tasks matter. A request
   for a chart does not make a chart the clearest answer.
3. **Choose marks and channels from task and field semantics.** Amount,
   ranking, deviation, distribution, correlation, temporal change,
   part-to-whole, flow, hierarchy and exact lookup impose different demands.
   Prefer channels that support the needed precision, but never treat an
   empirical channel ordering as a universal chart ranking.
4. **Make scale semantics recoverable.** When physical bar length or filled
   area encodes amount, normally retain the meaningful zero. For lines and
   points, choose domain and aspect from the target variation plus comparison
   context. Use logarithmic or other transformed axes only for a matching task,
   valid domain and explicit transformation, ticks and excluded values.
   For a declared linear axis, derive the affine map from at least two known
   value/position pairs, then predict every other tick and encoded mark within
   an explicit tolerance. Printed labels do not validate their own positions;
   preserve a visible scale judgment as a separate lane.
5. **Encode uncertainty and absence as meaning.** Identify what uncertainty
   represents before selecting intervals, distributions, ensembles, scenarios
   or frequency frames. Never merge zero, missing, suppressed, not applicable
   and imputed, connect an unsupported gap, or expose protected small counts.
6. **Build one metric model.** In dashboards, define outcome, drivers,
   guardrails, cadence, freshness, active filters, incomplete periods,
   permissions, failure states and drill path. Titles, annotations and
   reference lines must update from the same snapshot and filter state.
7. **Design transformation, not shrinkage.** For each destination decide what
   may resize, reposition, simplify, aggregate, facet, relabel, disclose,
   change interaction, or switch form while preserving thesis and values.
8. **Provide an equivalent data path.** Supply a concise purpose/takeaway and
   task-appropriate structured detail: semantic table or data, descriptions,
   keyboard-operable exploration, names, focus/order and redundant encodings.
   Localise numbers, dates, percentages, currency and units from current locale
   data while preserving source precision.

## Choose a form by the question

Use this comparison aid when representation is open; it is not a chart mandate.

| Question | Candidate to sketch | Failure to check / useful control |
| --- | --- | --- |
| Which is larger, and by how much? | Aligned bars or dots with a common scale | Long labels, false baseline or hidden small differences; compare a value table for lookup |
| How does a value change across an ordered domain? | Connected positions or small multiples | Connection implies continuity/order the source may not have; unordered categories need another relation |
| How are observations distributed? | Dots, bins or a distribution summary | Binning or aggregation conceals sample size, outliers or multimodality; inspect source points where permitted |
| How do two measures relate? | Scatter positions | Overplotting, unequal units, absent values or an invented causal story |
| How do parts contribute to a whole? | Shared-whole bars or another explicitly bounded composition | Denominator, omitted parts or incomparable wholes; compare direct values |

Sketch the leading candidate with actual values and labels, then test the
question that would favour the alternative. A line can serve an ordered
non-temporal domain. A table can be the final design when exact lookup matters
more than a visual pattern. Preserve meaning while changing form, not only the
numbers printed beside it.

## Critique: failure signatures and causes

| Failure signature | Likely parent cause to test |
| --- | --- |
| Polished graphic answers the wrong question | wrong grain, filter, denominator, period, join, definition or stale extract |
| Magnitudes or trends feel exaggerated | truncated extent, arbitrary aspect, area/angle/3D depth, incompatible scales, or transformed axis without matching task |
| Chart is true but headline is not | annotation outruns source, uncertainty, benchmark or causal authority |
| Gap reads as zero or continuous trend | missing/suppressed/imputed states collapsed or interpolated without authority |
| Dashboard panels disagree | metric definitions, grains, time windows, filters, permissions or freshness are not shared |
| Exact lookup is slow or table context disappears | wrong form; weak row/column semantics, units, grouping, alignment, headers or precision |
| Narrow view tells a different story | uniform shrinking, hidden labels, changed aggregation, hover-only values or unsynchronized interaction |
| Alternative is present but not equivalent | stale prose/raw table, lost hierarchy, relation, filter state, uncertainty or task |
| Dashboard reads as equal tiles, gauges and donuts | metric model absent; dashboard library chose encoding instead of decision, task and field semantics |

Monitoring accepted thresholds may legitimately use tiles or gauges; a real
part-to-whole task may use a donut. Repair missing metric/decision semantics
before choosing another encoding, not because a chart type is unfashionable.

Treat a detector or checklist as localisation evidence, not a truth or quality
oracle. For every finding name observation, likely reader error, cause as
confirmed/inferred/unknown, severity/confidence, smallest repair, preserved
strength and missing proof.

## Smallest repair, preservation, and regression

Freeze `P`. Diagnose in this order: source/definition/grain -> transformation
and denominator -> permitted claim -> form -> encoding/scale -> composition ->
labels/decoration. Repair the earliest cause and regenerate every dependent
title, chart, table, alternative and export from the authoritative mapping.
Preserve correct values, uncertainty, useful comparisons, recognisable visual
language and valid filters. Recompute after every data or transform change;
compare the same snapshot before/after; reject a repair that hides outliers,
changes the question, fabricates precision, weakens exact lookup, breaks locale
or access, or makes another destination disagree.

## Rule classes and exceptions

Source values, logical relations, declared transformations, privacy, supplied
definitions and applicable access/platform contracts are binding. Empirical
findings about channel accuracy, baseline perception or uncertainty are bounded
by studied task, mark, population and medium. Chart families, direct labels,
axis ranges, table order, dashboard density and interaction are contextual
conventions; preferences never override truth or access.

A cropped baseline, logarithmic scale, dual scale, pie/donut, animation,
embellishment or unusual sequence can be valid only when the task and data
justify it, the transformation is conspicuous, required values and relations
remain recoverable, a simpler control is considered, and equivalent static and
accessible paths survive. Reject fixed category, colour, KPI, gridline, chart,
or dashboard-count recipes.

## Proof, ownership, and claim ceiling

Reconcile displayed values to `D`; recompute totals, rates, changes and derived
fields; diff the declarative mapping against the source; inspect exact labels,
scales, units, missingness and annotations. Test supplied locales, structured
alternatives, keyboard/state behaviour, and narrow/wide/static/print renders from
the same snapshot. Preserve source data, transformation/field dictionary,
editable mapping and evidence receipts; label unrun checks `unverified`.

Information Design owns form, encoding, annotation and responsive information
intent. Data/statistical owners validate definitions, inference and analysis;
source owners validate evidence; UI/Web implement interaction and responsive
mechanics; Production validates delivered artifacts. A correct render supports
only that representation under tested conditions. It does not prove source
truth, statistical validity, causality, comprehension, accessibility
conformance, decision improvement, or universal chart quality.
