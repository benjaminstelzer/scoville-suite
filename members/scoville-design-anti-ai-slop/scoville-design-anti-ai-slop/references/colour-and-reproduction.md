# Colour and reproduction

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-COLOUR-PERCEPTION`, `SRC-COLOUR-MANAGEMENT`, `SRC-COLOUR-ACCESS-DATA`, `SRC-PRODUCTION-PRINT`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when colour carries hierarchy, identity, state, data, accessibility, or
cross-output meaning; or when gamut, profile, ink, substrate, overprint, WCG,
HDR, spot colour, or output intent can change the result. Do not load for one
settled decorative colour or for print work whose colour chain is already fixed
and unaffected.

## Inputs and formal variables

Select the fields below that are material to the current open colour decision
or its proof. Retain applicable content, authority, accessibility and production
constraints; do not expand unrelated roles or output chains.

Record the communication roles before coordinates: background, surface, text,
accent, action, focus, success, warning, error, selection, disabled, data
series, annotation, and any brand or material colour. For each role record its
importance, adjacent colours, occupied area, text or mark size, state/theme,
redundant cue, and permitted variation.

Record viewing surround, adaptation and illumination; display capability and
settings; target colour space, profile and output intent; ink/process/spot
model, paper or substrate, finish, opacity, trapping or overprint conditions;
and every destination that must preserve the relation. Separate source values,
working space, conversion, destination values, device state, and physical
appearance. A hex, Lab value, profile tag, swatch name, or soft proof describes
one part of that chain, not the final appearance.

## Generate or decide

1. Define a role map in neutral language before choosing hues. Decide which
   distinctions must remain perceivable without colour and which may be purely
   expressive.
2. Build palette relationships in their real surround and proportions. Judge
   lightness, chroma, hue, temperature, simultaneous contrast, area, texture,
   and material response together. Harmony names can suggest comparisons; they
   do not decide quality.
   For open hue decisions record origin as `supplied | incumbent | material |
   data | place | invented`. Invented hues need a named role. Neon on near-black
   or a purple-to-blue gradient describes a treatment, not its communication job.
3. Make hierarchy economical. Reserve the highest-attention contrast for the
   most consequential role, coordinate repeated states, and keep decorative
   contrast from impersonating state or action.
4. Encode meaning redundantly where loss would harm use: label, shape, pattern,
   position, icon, line treatment, or explicit text. Preserve the same meaning
   through light, dark, forced-colour, greyscale, reduced-colour, and print
   states when those states apply.
5. For data, assign colours from variable type, comparison task, missingness,
   uncertainty, background, and accessible alternatives. Do not use a smooth
   sequential ramp for unordered categories or a categorical palette for
   magnitude merely because it looks varied.
6. Define the reproduction chain before conversion. Preserve an authoritative
   source, choose the destination profile or named provider condition, identify
   out-of-gamut and total-ink/overprint risks, then select a rendering or
   spot/process strategy by the actual job. Never convert repeatedly between
   derivatives.
7. Treat gradients, transparency, glow, blend modes, very dark colours, wide
   gamut, and HDR as destination-dependent effects. Supply a bounded fallback
   that preserves role and hierarchy when the effect is unsupported.

## Construct a role palette in place

Start with the actual background, largest surface and reading text. Establish
their lightness relation in the layout, then introduce the accent where the
task needs attention. For example, a pending decision may get the accent while
completed items use text and a quiet status marker. Compare changing accent
area with changing its chroma; equal swatches hide this difference.

For a muddy palette, isolate the failed adjacent pair. Change lightness when
figure/ground is weak, chroma when attention is misallocated, or hue when a
category distinction is needed; retain the other role relations for comparison.
For ordered values compare a progression with consistent perceptual direction;
for categories compare separability without implying rank.

When an alternate theme is required, map each role again against its new
surround: reading text, quiet text, surface boundary and accent may need
different adjustments. Do not invert every coordinate. Inspect the same
content and attention order in both themes and without hue where meaning
requires redundancy. An entirely neutral palette can already serve the job;
these construction steps do not require an accent, a theme or a colour count.

## Critique: failure signatures and likely causes

- **A role disappears or changes meaning across states.** Likely cause: values
  were chosen per screen rather than from a semantic role system, or colour is
  the only cue.
- **Everything is vivid, or the accent no longer attracts.** Likely cause:
  chroma and contrast were allocated without consequence or area context.
- **A palette passes sampled contrast but reads poorly.** Check actual text
  size/weight, antialiasing, gradients, transparency, backdrop, glare, local
  adaptation, thin strokes, and the exact criterion scope.
- **A colour-vision simulation suggests confusion.** Treat it as a diagnostic,
  not a human verdict. Inspect redundant cues, adjacent lightness and the real
  task; do not design one universal “CVD-safe” palette from a simulator alone.
- **Screen and print disagree.** Trace wrong/absent profiles, multiple
  conversions, uncalibrated viewing, paper colour, gamut, black construction,
  transparency, overprint, spot substitution, ink and finish before adjusting
  the palette by taste.
- **Dark, forced-colour, office-print, WCG or HDR variants lose hierarchy.**
  Likely cause: coordinates were inverted or clipped instead of remapping
  semantic relationships for that destination.
- **A data palette implies an order, midpoint, certainty, or category that the
  data do not possess.** The defect is semantic encoding, not decoration.
- **Palette reads as a trend set rather than a system.** Test whether hues came
  from fashion or a generator without role, material, incumbent or data origin.
  Rebuild the role map from subject origins before changing hues. A trend colour
  with a justified role is not a defect; invented colours remain available.

For every finding state the observed pair or state, context, likely effect,
cause as confirmed/inferred/unknown, severity and confidence, smallest repair,
what must remain, and the exact proof still missing.

## Repair and preserve

Repair the highest owning cause, not every swatch. If role assignment is wrong,
repair the role map; if only one state fails, repair that state mapping; if a
conversion is wrong, return to the authoritative source and rebuild the
derivative. Add a redundant cue before forcing unrelated hues apart. Change
lightness, chroma, area, adjacency, texture, outline, or placement according to
the failed relation rather than applying “more contrast” indiscriminately.

After repair, preserve approved brand relations, intended attention order,
legible text, data meaning, supplied spot/brand specifications, and unaffected
destinations. Recheck all consumers of the changed role, including focus,
disabled, selected, validation, charts, illustrations, logos, themes, print and
fallback states. Invalidate any proof made from the superseded derivative.

## Rule classes and exceptions

- **Binding:** supplied meaning and content; applicable access criterion;
  approved brand/spot specification; named profile, provider, ink, substrate or
  receiver contract; no fabricated measurement or production proof.
- **Evidence-bounded:** scoped contrast and non-colour requirements, colour
  management, profile and output-intent behaviour. Apply the exact version,
  object, medium and exception, not a remembered slogan.
- **Contextual convention:** semantic roles, accent scarcity, warm/cool or
  harmony relations, dark-theme remapping, black construction and proofing
  practice. They yield to the actual task and production chain.
- **Heuristic:** begin with fewer functional roles, compare in context, and
  preserve lightness structure when hue changes. These are starting tests, not
  universal palette recipes.

A low-contrast, monochrome, fluorescent, overprinted, limited-ink, material,
or deliberately dissonant system can be correct when its purpose is declared,
required information and access survive, the destination supports it, a
compensating structure exists, and a conventional control does not perform
better on the protected task. Do not convert an expressive exception into a
general rule.

## Proof and claim ceiling

Inspect actual adjacent pairs and full compositions at target size, brightness,
surround and state. Where applicable, test exact contrast/non-colour criteria,
forced colours, greyscale, themes, zoom, display gamut and data alternatives.
For reproduction, inspect profile assignments and conversion settings, gamut
warnings, separations/overprint, ink/spot definitions and the named export;
compare a calibrated soft proof and provider or physical proof when the job
requires them.

Report only the evidence achieved. A contrast calculation does not prove
readability or aesthetic quality; a simulation does not prove experience for
all colour-vision differences; an ICC profile does not prove correct output; a
soft proof does not prove ink on substrate; and a physical proof from one
provider does not certify every run. Colour owns role, appearance intent and
reproduction decisions. The UI owner implements states, Production validates
files, the provider accepts the process, and qualified users or specialists
judge outcomes outside the available evidence.
