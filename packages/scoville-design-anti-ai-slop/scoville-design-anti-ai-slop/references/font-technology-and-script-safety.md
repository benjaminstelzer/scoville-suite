# Font technology and script safety

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-FONT-TECH`, `SRC-FONT-LICENCE-PROOF`, `SRC-DATA-ACCESS-LOCALE`, `SRC-PROFESSIONAL-SCOPE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when a decision depends on actual font files, repertoire, features or
variation, shaping, language forms, fallback metrics/loading, mixed direction,
vertical flow, embedding/subsetting, or font-specific proof. Load for unfamiliar
writing systems even when the visual brief seems simple. Do not load for Latin
face character, pairing, hierarchy, or paragraph setting alone; typography owns
those decisions. This leaf supplies a safety and evidence floor, not native
art-direction expertise for every writing system.

## Inputs and formal variables

Require real strings and files wherever available. Record only open relevant fields; otherwise use the Core minimal record:

- `L`: language/locale, script, logical string order, base and embedded
  direction, numerals, punctuation, combining marks, and vertical requirement;
- `Q`: critical strings and code points, including names, IDs, dates, prices,
  phone numbers, mixed-direction values, and longest/minimum content;
- `F`: exact family/file, version/hash when appropriate, source, format,
  `cmap`, GSUB/GPOS, language systems, axes, instances, metrics, embedding
  flags, and declared fallback order;
- `R`: shaping/layout engine, browser/OS/app/PDF path, loading policy, supported
  properties/features, and requested screen/print states;
- `D`: use and delivery: web/app/ebook/print, embedding, subsetting,
  modification, redistribution, service terms, receiver/provider contract;
- `P`: protected text, logical order, meaning, line/page geometry, interaction,
  editability/search/access, and approved typographic intent;
- `E`: file inspection, shaping output, source, render, interaction,
  native-reader, font-engineer, licence, preflight, and provider evidence.

Unknown file, engine, language, licence, or receiver facts stay unknown. A font
name, web listing, installed copy, or screenshot is not a receipt.

## Generate and decide

1. **Select exact files, not family labels.** Inspect the candidate's actual
   repertoire, marks, language systems, styles, metrics, axes/features,
   synthesised-form behaviour, and target renderer support. A `cmap` hit proves
   character mapping only; it does not prove shaping, language-appropriate
   forms, mark placement, line breaking, or native quality.
2. **Build a script and feature matrix.** For each `L`, list required characters,
   combining sequences, substitutions/positioning, localised forms, numerals,
   punctuation, line-break/hyphenation behaviour, direction, and vertical
   orientation. Test representative `Q` through the actual shaping/layout
   engine. Never transfer Latin casing, tracking, italic, hyphenation, word
   spacing, or line-height logic without relevant authority.
3. **Define fallback as controlled substitution.** Name each operative fallback
   and the strings/scripts that select it. Compare x-height/aspect, advance
   widths, ascent, descent, line gap, weight/width impression, features, and
   glyph coverage. Capture primary, forced-fallback, missing-font, and before/
   after-load states. Derive metric overrides only from measured files; do not
   tune one heading by eye and call the chain compatible.
4. **Preserve logical order and semantic direction.** Set language and base
   direction at semantic boundaries; isolate inserted names, IDs, paths, and
   values. Test brackets, punctuation, digits, wrapping, selection, cursor
   movement, copy/paste, and accessible order in mixed runs. Never reverse a
   source string to imitate RTL.
5. **Treat vertical text as a writing mode.** Verify block progression, glyph
   orientation and vertical alternates, punctuation, Latin/numeral treatment,
   ruby/annotations, columns, interaction, and reading order. Rotating a
   horizontal block is not vertical typesetting.
6. **Use features and axes from evidence.** Prefer a supported high-level
   control when it expresses the intent. Confirm the actual feature or axis
   exists, works at the selected instance, survives fallback/export, and does
   not destabilize data or layout. Do not assume optical size, small caps,
   localised forms, ligatures, or slashed zero from a tag name.
7. **Create the font receipt before delivery.** Record exact files/source,
   licence/EULA or service basis, permitted media, embedding/subsetting,
   modification, redistribution, reserved names/attribution, and delivered
   derivatives. Inspect embedding flags as technical evidence, never as the
   whole legal permission. Recheck current commercial/service and receiver
   terms at use time.

## A compact substitution specimen

For a Latin identifier field, a filled local specimen might use
`Order I1l-008 / O0 / 27.50`: primary file and actual instance, renderer/version,
the same field width, and the named fallback forced in a second render. Inspect
glyph identity, total advance, baseline and clipping, then the containing row.
A recorded field such as `primary not loaded; fallback rendered; row grew to
two lines` is useful evidence; `font-family declared` is not proof of which
font drew the glyphs. Replace this illustrative string with the task's actual
confusables and language. It neither demonstrates another script's shaping nor
requires a fallback experiment for a raster-only delivery.

## Measure rendered text without confusing metrics

Resolve required font loading and layout before measuring real strings. Record
the engine, effective setting and metric used. `document.fonts.ready` completes
the current browser font-loading/layout cycle; it does not prove that every
glyph came from the intended file or that no fallback occurred. Investigate a
material substitution through the specimen above.

Use layout rectangles/advances for occupied line space and containment;
use actual shaped glyph contours or a target-size render for visible ink.
SVG text `getBBox()` is based on glyph cells, not exact ink. Browser client
rectangles and nominal em sizes likewise cannot prove optical centering.
Convert coordinates to one frame and account for transforms. Rotated text,
strokes, masks and clips require a suitable metric or explicit uncertainty.
Do not estimate width from character count and label it measured.

The optional [`measure-layout.js`](../scripts/measure-layout.js) runs in an
already loaded browser document and returns explicit client-rectangle/style
checks; HTML text insets use DOM text Range rectangles by default, while an
explicit box metric checks allocation only. Neither text cells nor Range bounds
are exact ink or complete line boxes. Unsupported mixed/generated content needs
separate measurement. Results include their metric and limits. It changes no
artifact and rejects missing,
hidden or unsupported geometry as unverified. It is a measurement convenience,
not a shaper, an optical judge or a required dependency for other renderers.

## Critique: signatures and causes

| Failure signature | Likely technical cause to test |
| --- | --- |
| Missing box, tofu, blank, or wrong glyph | absent mapping, wrong fallback, broken resource, variation/encoding mismatch |
| Joining breaks; marks detach/collide; cluster order looks wrong | shaping bypassed, required GSUB/GPOS/language system absent, wrong engine/tag/font |
| Correct characters look linguistically foreign | language-specific forms, punctuation, digits, or type design is inappropriate; native authority missing |
| Wraps, controls, or page count jump during load/substitution | fallback widths or vertical metrics differ; loading or metric override is wrong |
| Mixed RTL/LTR punctuation, number, cursor, or copy order breaks | source order, base direction, isolation, semantic markup, or renderer behaviour is wrong |
| Vertical run is rotated or punctuation/Latin faces the wrong way | horizontal composition was transformed instead of using correct writing mode/orientation |
| Feature/axis request has no effect or changes on export | feature absent, unsupported, synthesised, overridden, or lost through fallback/subsetting |
| PDF/app/web output substitutes or outlines text unexpectedly | embedding rights/flags, package resources, export preset, receiver policy, or missing font is unresolved |
| Resize, reflow, or text-spacing state clips or hides text | fixed geometry, line metrics, overflow policy, or unsuitable font substitution owns the failure |

Distinguish source, font, shaper, layout engine, implementation, export, and
human-language failures. Do not repair an unfamiliar script with visual nudges
before the responsible layer is identified.

## Smallest repair and preservation

Freeze `P`. Repair in causal order: wrong logical text/language/direction ->
wrong or damaged font resource -> missing repertoire/language support -> wrong
shaping or feature configuration -> uncontrolled fallback/loading -> metric
substitution -> layout geometry -> local optical adjustment. Change the smallest
owning font, semantic marker, feature, fallback, or metric cause and rerender
every affected `L` and `Q`. Preserve exact Unicode text, logical order,
typographic role/voice, line and page relations, interaction, and editability.
Reject manual string reversal, per-glyph positioning, hidden overflow,
unauthorised outlining, or image replacement when they conceal the cause or
remove search, selection, access, or localisation.

## Rules and exceptions

Binding facts come from actual content, font files, licence/contract, applicable
standard, renderer support, and qualified language authority. “Open source,”
“free,” “variable,” “Unicode,” and “web safe” are not deployment proofs. Loading
policy, feature use, metric adjustment, synthesis, subsetting, and outlining are
tradeoffs, not universal defaults; record their effect and receiver scope.

A typographic exception cannot waive missing content, corrupt logical order,
broken shaping, required access, or licence terms. Experimental deformation or
unusual script mixing requires an authorised concept, recoverable meaning, a
correct semantic/text alternative where needed, target-render proof, and native
review. Do not claim an intentional native convention from model memory.

## Proof, ownership, and claim ceiling

Use deterministic checks for file identity, tables, repertoire declarations,
features/axes, metrics, logical source order, semantic language/direction,
resource loading, embedding, and geometry. Render actual `Q` with the primary
and every operative fallback in each target `R`; compare before/after loading,
narrow/wide or page contexts, zoom, and applicable text-spacing/reflow states.
For print/PDF, inspect embedding/subsetting, substitutions, missing glyphs, and
target output; obtain provider proof when required.

Deterministic evidence cannot prove readability, appropriate voice, native
forms, correct cultural convention, licence interpretation, or print approval.
Require a native reader for consequential unfamiliar language/script. Require
a font engineer when diagnosis or repair needs font-internal engineering or
available checks cannot establish a reliable technical conclusion. Routine
configuration repairs, such as selecting the correct supplied file or applying
measured fallback metrics, need no external engineer when their cause and
result can be demonstrated with the available tools. Do not extend that local
proof to native-language quality or uninspected font internals. Escalate unclear
rights to the rights owner and physical/output acceptance to the actual provider.

Typography owns visual type intent; this leaf owns font-specific requirements,
fallback/script safety, and requested font proof; UI/format owners implement;
production owns export and handoff; the durable rights registry owns licence
records. Claim only the tested fonts, strings, engines, languages, states, and
delivery conditions. Never infer universal multiscript coverage, native
quality, accessibility, legal clearance, or production readiness from one file
inspection or render.
