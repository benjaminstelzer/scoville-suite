# Media production and handoff

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-COLOUR-MANAGEMENT`, `SRC-FIXED-EDITORIAL`, `SRC-CRITIQUE-EMPIRICAL`, `SRC-UI-EVALUATION`, `SRC-PRODUCTION-PRINT`, `SRC-PRODUCTION-DIGITAL`, `SRC-PRODUCTION-ACCESS`, `SRC-SOURCE-EVIDENCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when the job requires technical export, rebuildability, authoritative
source and derivative lineage, preflight, format-specific semantics or access,
receiver/provider acceptance, physical proof, or a durable handoff record
beyond Core's ordinary create-and-render loop. Do not load merely because an
artifact is created, displayed once, or exported to PDF. A fully specified
unchanged conversion or export with no open production-evidence decision stays
with the implementation/format owner and does not select this module. The
format Skill or implementation owner creates the artifact; this module defines
and inspects the production evidence contract.

## Artifact contract and inputs

Before export record the open relevant fields below; otherwise use the Core minimal record:

Use only fields needed by this delivery contract. A local draft or bounded
export needs identifiable source/output, applicable file checks and honest
proof status, not a full release dossier. Reproducible handoff additionally
needs exact versions, hashes and rebuild settings; regulated or provider
acceptance needs the applicable external receipts. Missing evidence withholds
only the dependent acceptance claim, not unaffected authorised source work.

- deliverable purpose, medium, dimensions/duration, variants and quantities;
- authoritative editable sources, asset/font/data dependencies, versions,
  owners, hashes and rebuilding toolchain;
- derivative graph: output, source parent, transform, settings, destination,
  version and invalidation state;
- exact format/profile/standard only when named by the receiver, platform,
  printer, publisher or regulation;
- content, type, image, colour, metadata, accessibility, privacy, rights and
  attribution conditions that must survive;
- validators, renderers, devices or physical proof conditions, acceptance
  owner, due date and unresolved blockers.

Distinguish **source-created**, **syntax-validated**, **resources-resolved**,
**semantics-inspected**, **render-inspected**, **interaction/playback-tested**,
**preflighted**, **provider-accepted**, and **physical-proofed**. None implies
the next. A checksum proves file identity, not correctness.

## Common production spine

1. Keep one named authoritative source for each independently editable object.
   Never repair a rasterized preview, exported PDF or transcoded video when the
   editable cause exists upstream.
2. Preserve source-to-output lineage. When rebuildability or exact identity is
   required, record source hash, transform/tool/version, parameters, dependency
   versions and output hash. Mark old evidence stale
   whenever a parent or production condition changes.
3. Validate structure before appearance: parse the actual file, resolve fonts,
   links, images, profiles and other resources, then inspect semantics and a
   render. A screenshot cannot expose missing tags, wrong links, substitutions,
   stale data or hidden objects.
4. Inspect the rendered whole and diagnostic views: intended size/context plus
   thumbnail, zoom, narrow/wide, page/slide strip, separations, sampled frames,
   greyscale, alternate state, or physical proof as applicable.
5. Bind every receipt to unambiguous artifact identity, conditions, tool/version, date and
   result. Record warnings and unknowns; never turn a declared target into
   evidence that it was met.
6. Handoff the smallest complete package: authoritative source, approved
   derivatives, dependency/asset manifest, specifications, evidence receipts,
   known limits, rejected variants, repair path, owner and acceptance state.

## A small delivery record can be enough

Illustrative local record: `source: label.svg revision B; derivative: label.png;
scope: supplied screen preview; inspected: dimensions and target render;
receiver acceptance: not requested`. Replace these example values with the
actual source, output and evidence; a filename alone does not establish their
identity. A print job with open font or provider questions needs those fields,
but an ordinary screen export does not inherit a release dossier.

When raster resolution is material, calculate effective density from retained
pixels divided by placed inches, using the cropped dimension actually placed.
Compare it with the real receiver condition; this arithmetic supplies no
universal target and upsampling creates no new captured detail.

## Format gates

Apply only the gates used by the job. The shared spine applies at the delivery
contract's scope; unrelated format detail and inapplicable records are omitted.

### SVG and raster

- Parse SVG/XML and raster headers; verify intrinsic dimensions, viewBox,
  orientation, colour/profile/alpha and intended scaling.
- Resolve linked or embedded images, masks, filters, gradients, symbols,
  patterns, fonts and external resources. Test the receiver's support rather
  than assuming browser support equals editor, print or email support.
- Decide live text versus outlines from editability, accessibility, search,
  localisation, font rights and receiver constraints. Preserve an authoritative
  live-text source even when a bounded derivative requires outlines.
- Inspect clipping, crop, pixel density at physical size, interpolation,
  transparency halos, banding, sharpening, compression, metadata and each
  requested background/density variant.

### Print and PDF

- Use the supplier's current specification. Confirm final/trim size, page
  boxes, bleed, safe region, fold/panel/face relation, imposition authority,
  scaling, orientation and page order. Do not invent generic bleed or safe-area
  numbers.
- Inspect font embedding/subsetting/substitution and missing glyphs; effective
  image resolution; profiles and output intent; spot/process names; ink and
  black construction where governed; overprint, trapping authority,
  transparency flattening, hairlines and separations.
- Validate the exact requested PDF or packaging profile with an appropriate
  preflight. A profile name, export preset or green preflight result does not
  prove the design, content, printer setup or physical result.
- When semantics/access matter, inspect tags, language, heading/list/table
  structure, alternate descriptions, links, reading order, bookmarks/forms and
  actual assistive use. Visual page order and tagged reading order are separate.
- Require provider acceptance and a physical proof when substrate, ink, finish,
  fold, cut, binding, scale, installation or viewing distance can materially
  change the result.

### Documents, reports and presentations

- Preserve editable text, styles, masters/templates, theme relationships,
  source data and logical structure. Record embedded versus substituted fonts
  and target office/viewer versions.
- Inspect every page/slide and the overview strip for overflow, reflow, crop,
  hidden content, notes, transitions, masters, repeated anchors and contrast.
  Test long/short/localised content where the template promises reuse.
- Inspect document/deck semantics: title, language, heading hierarchy,
  lists/tables, alt descriptions, link purpose, reading order, slide title and
  object order as applicable. Automated checks locate candidates; they do not
  prove comprehension or full access.
- Reopen the delivered file in the receiver's application and render the
  exported derivative. A correct PDF cannot prove the editable source survives
  font substitution or a different office renderer.

### Motion and timed media

- Record timeline authority, timebase/frame rate, duration, dimensions,
  colour/transfer characteristics, audio layout, caption/subtitle sources,
  poster/thumbnail and destination variants.
- Inspect full playback plus sampled key/transition frames, first/last state,
  loop seam, interruption/resume, reverse when supported, audio sync, captions,
  safe regions, compression, banding and platform transcode.
- Deliver reduced-motion or static meaning-equivalent outputs when required by
  the design contract. A still frame is not equivalent when timing or state
  carries meaning.
- Keep editable timeline, linked assets and font/license receipts. A playable
  local master does not prove streaming, device performance, platform encoding
  or accessibility.

### Web and UI handoff

- Hand off design intent, exact assets/fonts/data, responsive/state record,
  semantics/access requirements and proof targets to the implementation owner.
  Do not prescribe framework internals from this module.
- Validate built bundles and runtime in the actual owner lane: resource loading,
  font fallback, image variants, zoom/reflow, keyboard/focus, accessible names,
  announcements, states, browsers and devices as scoped.
- Source code, a component catalogue, a design-system token file or one
  screenshot is not deployed/runtime evidence.

### Packaging, signs and installed graphics

- Treat dielines, cut/crease/glue zones, panel order, seams, distortion,
  substrate, finish, regulatory faces, barcode/mark zones, structural mockups,
  installation, lighting, viewing distance, decision points and tactile/audible
  conditions as specialist/provider inputs.
- Design owns face, sequence and viewing intent. Supplier, packaging engineer,
  wayfinding/access specialist, fabricator and site authority own the technical
  conditions within their competence. Stop rather than infer a safe dieline,
  structural performance, code compliance or installation approval.

## Critique: failure signatures and causes

- **Looks correct but cannot be rebuilt:** derivative became authority, linked
  assets or fonts are missing, versions are unknown, or manual edits are not in
  the source.
- **Parses but renders incorrectly:** unsupported feature, unresolved resource,
  fallback/substitution, coordinate/crop error, colour/alpha difference or
  renderer-specific behaviour.
- **Renders correctly but semantics fail:** reading/order/tag/name/link/state
  information is absent or contradicts visual intent.
- **Preflight passes but output is wrong:** validator covered syntax/profile,
  not content, physical process, receiver settings or intended appearance.
- **One derivative is repaired while others remain stale:** parent cause and
  dependency graph were not used.
- **Handoff is large but unactionable:** no authority, status, acceptance owner,
  conditions, known limits or source-first repair path.

Report artifact/hash, observable failure, affected consumer, proof layer,
confirmed/inferred/unknown cause, severity/confidence, owning source, smallest
repair, preserved constraints and stale evidence.

## Repair, exceptions and regression

Repair the editable authoritative cause, rebuild every affected derivative,
rerun only the relevant validators/renders/provider checks, and invalidate
superseded receipts. Preserve content, design intent, semantics, rights,
approved profiles/assets and unaffected variants. Do not flatten, outline,
rasterize, convert, retag or strip metadata globally to make one check pass.

A receiver-specific outline, flattening, legacy codec, spot conversion,
untagged decorative object, reduced variant or provider exception may be valid
when owner, destination, reason, affected function, editable source, fallback,
proof and expiry are recorded. It remains local; never rewrite the canonical
design rule or call it universal best practice.

## Proof, ownership and claim ceiling

Bind source and output identity to applicable parser/validator results and an
intended-context render, or disclose unavailable evidence. Use hashes when
the contract requires byte identity or reproducibility. Add resource, semantics/access, interaction/playback,
preflight, provider and physical receipts only where the claim requires them.
Use the receiver's exact file and environment; label automated, visual, human,
specialist and provider evidence separately.

Production owns lineage, format validation, renders, preflight and handoff
evidence. Craft and medium modules own design decisions; format/UI/code owners
create and implement; provider or specialist accepts physical and regulated
conditions; qualified users determine usability or access outcomes. Never claim
production readiness, accessibility, conformance, print fidelity, playback
performance or receiver acceptance from a source file, screenshot, soft proof,
validator, metadata declaration or local render alone.
