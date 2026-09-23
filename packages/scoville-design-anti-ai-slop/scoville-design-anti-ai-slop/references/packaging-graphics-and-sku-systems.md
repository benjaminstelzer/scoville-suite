# Packaging graphics and SKU systems

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-PACKAGING-GRAPHICS`, `SRC-BRAND-CANON`, `SRC-TYPE-DETAIL`, `SRC-IMAGE-CRAFT`, `SRC-PRODUCTION-PRINT`, `SRC-SOURCE-EVIDENCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when graphics on supplied authoritative package or label geometry must
coordinate panels/faces, assembled or opening views, product information, a
SKU family, shelf or thumbnail recognition, or packaging-specific e-commerce
derivatives. Also load when an existing supplied package or label face is the
artifact and its face-local hierarchy, framing, fit or repeated family relation
is questioned, even when no dieline or assembled view is supplied. In that
case, missing object geometry limits flat-to-object claims; it does not transfer
the visible face relation to general Composition. Load for package-graphic
generation, critique or repair when the flat-to-object relation can change the
result. Do not load for structural
packaging, dieline construction or correction, material/barrier/closure/
protection engineering, mandatory-content determination, barcode data or
symbology, scan certification, print preflight, or provider acceptance. Do not
load for an approved pack that only needs technical export, an ordinary folded
publication, a product-card interface, or a generic flat graphic merely shown
on a box mockup. A supplied graphic explicitly functioning as the package or
label face remains within this module's face-local scope.

## Authority and packaging record

Begin with the actual dieline or label geometry from its accountable owner.
Select fields below that are material to the current packaging decision or
its proof. Record supplied or inspected conditions as such and needed unknowns
as unresolved; do not omit applicable geometry, exact-content, authority or
safety constraints, or expand unrelated SKU and production fields:

- `G`: source, version, date, owner and approval state; dimensions, orientation,
  panel/face IDs, cut/fold/score/perforation/seam/glue/no-print/protected zones,
  curvature or distortion guides, tolerance authority and assembled mapping;
- `C`: exact brand, product, variant, descriptor, quantity, claim, warning,
  instruction, ingredient/specification, identifier, barcode placeholder,
  certification, contact, credit and language content; for each, its source,
  owner, required/optional/unknown state, allowed transformation and placement
  condition;
- `H`: intended brand/product/variant/quantity/claim hierarchy by channel,
  viewing condition, consequence and likely confusion - not one universal
  front/back ranking;
- `S`: SKU IDs, shared invariants, controlled variables, actual product
  differences, closest confusable pairs, pack sizes/forms, locales, markets,
  lifecycle, canonical assets and change owner;
- `V`: relevant flat, primary, secondary, top/bottom, side, opening, handling,
  grouped-shelf, distance, thumbnail, search-result and product-detail views;
- `P`: approved identity, exact content, package truth, differentiation,
  meaningful imagery, protected zones and valid existing relationships;
- `E`: source, rule, render, mockup, shelf/e-commerce, barcode, regulatory,
  production, physical and audience evidence, kept as separate lanes.

Never redraw or repair `G`. Missing, stale, unapproved or contradictory
geometry blocks non-provisional artwork that depends on it; return the exact
question to its owner. The legal, regulatory, product, barcode and claim owners
supply their content and zones. Empty space in a dieline is not permission to
omit, invent, rewrite or relocate them.

## Generate and decide

1. **Map the object before composing it.** Convert the flat dieline into an
   inspectable panel graph: adjacent edges, assembled orientation, visible and
   occluded faces, first/secondary/opening views, seams, transitions and
   protected zones. Use stable IDs in flat artwork and mockups so a finding can
   return to its actual owner.
2. **Define the packaging communication job.** State what must be identified,
   distinguished, understood or acted on in each `V`. Allocate `C` by task,
   exposure, consequence and available face - not by a generic rule that brand is
   always first, legal copy always belongs on the back, or every package needs a
   hero claim.
3. **Design one SKU grammar.** Separate recognition invariants from variant
   variables and forbidden mutations. Give each variable one job: product type,
   flavour, size, strength, audience, market or another supplied distinction.
   Use redundant differentiation when confusion has consequence; colour alone
   may disappear, shift, or imply the wrong taxonomy. Test family coherence and
   individual identification together rather than cloning one pack or styling
   every SKU independently.
4. **Compose with real content.** Use the longest supplied language, smallest
   pack, densest required-content set, closest variants and meaningful image
   extremes. Establish panel hierarchy, reading continuity and handoff between
   faces. Protect critical copy, marks, codes, products and subjects from folds,
   seams, curvature, crop, closure and normal handling as defined by `G`.
5. **Translate flat relations to the object.** Treat cross-panel graphics,
   wraps, repeats, reveal sequences and inside print as relationships across
   assembled states. A continuous flat image is not continuous on the object
   unless orientation, seam, fold, distortion and ordinary view prove it.
6. **Design channel-specific recognition.** Compare a real grouped-shelf or
   distance context when retail discovery matters. For thumbnail/e-commerce
   use, define which verified pack cues and purchase distinctions must survive,
   which may be recomposed, and what cannot be added or enlarged without
   becoming a different product or unsupported claim. A packshot, mobile-ready
   image and product-detail composition are distinct derivatives.
7. **Mock up to expose risk.** Use flat art, assembled multi-view render and an
   identical-context SKU lineup. Add representative shelf/thumbnail/e-commerce
   views and a physical sample only when they can change the decision. A
   flattering three-quarter render is presentation, not proof of hidden faces,
   geometry, print or shelf performance.

## Fill the panel and variant map

For fictional stationery packs on supplied geometry, map `front: family,
variant, quantity`; `back: supplied use text`; `side: exact item ID`. Put actual
copy into the map before judging artwork. Compare “Ruled / 20 sheets” and
“Plain / 20 sheets” at their closest-confusable view: the variant word must
remain discoverable when colour disappears. Keep its role and location stable
unless the task justifies another grammar.

Trace each panel ID from the flat artwork to an assembled view and inspect
seam-adjacent content, not only the attractive front. A long variant name tests
the shared allocation before it becomes a one-off font shrink. Equal layouts
are valid for peer SKUs. This original example allocates supplied content;
it neither provides a dieline nor invents mandatory claims, barcode space or
manufacturing clearance.

## Critique: failure signatures and causes

| Failure signature | Parent cause to test |
| --- | --- |
| Flat artwork is strong but assembled reading breaks | wrong panel graph, orientation, seam/fold relation or viewing sequence |
| The pack is attractive but product or variant is unclear | `H` is unranked, category shorthand displaced identification, or variant cue is weak |
| The range looks coherent but SKUs are confusable | invariants consumed the distinctions; variables encode several meanings or depend on colour alone |
| Every SKU is distinctive but the family fragments | uncontrolled variables, missing invariant priority or local concept drift |
| Required content is tiny, hidden or detached | content manifest/panel allocation failed; decorative or optional material took its protected space |
| A barcode or code area is visually contaminated | supplied protected zone was violated or technical conditions are unknown; route verification to the barcode/production owner |
| Cross-panel image, word or mark breaks at assembly | flat continuity ignored seam, curvature, crop, closure, tolerance or normal view |
| Shelf or thumbnail test is won by one loud cue but meaning is lost | attention was mistaken for identification, correct variant choice or comprehension |
| E-commerce derivative no longer depicts the actual pack | recomposition changed product identity, quantity, claim, relative cue or source truth |
| Mockup hides the defect | geometry/view is approximate, only the best angle is shown, or artwork and mockup versions differ |

Localise each finding to SKU, view, panel/face ID and source version. Separate
visible graphic failure from structural, content, regulatory, barcode and
production uncertainty. Do not turn assumed consumer behaviour or a category
preference into a defect.

## Smallest repair and regression

Freeze `P`. Diagnose in this order: geometry/authority -> content/claim source
-> product and SKU taxonomy -> hierarchy and panel allocation -> assembled
relation -> channel derivative -> base composition/type/image/colour -> local
optical correction. Return geometry, required-content, claim, code or
production causes to their owners. Repair the earliest owned graphic cause,
then regenerate only its dependent panels, SKUs and derivatives.

Preserve exact approved content, CI invariants, real product differences,
working family recognition, valid category orientation and source imagery.
Recheck the closest SKU pairs, smallest/densest/longest cases, primary and
secondary assembled views, opening state, affected seams/folds, shelf or
thumbnail context and delivered language variants. A local nudge may not create
a new SKU ambiguity, hide a requirement, corrupt a code zone or detach the
digital derivative from the pack.

## Rules and exceptions

Binding constraints come from `G`, supplied product/content truth, current CI,
required-content owners, barcode/technical zones, applicable destination
contracts and approved release state. Panel names, front/back allocation,
family size, colour coding, logo scale, claim count, shelf distance, exposure
time, bleed, safe area and type size have no universal design value.

A seam-crossing graphic, unusual face priority, sparse or dense pack, category
departure, inside reveal, disruptive SKU cue, limited-colour system or
recomposed e-commerce image can be valid when its job, authority, protected
content, stable counterstructure, accepted cost, affected contexts and
falsifier are declared. An aesthetic exception cannot alter the dieline,
product truth, mandatory content, barcode conditions, rights, CI authority or
provider limits.

## Proof, ownership and claim ceiling

Bind every render to artwork, `G` and SKU version. Inspect flat art with dieline
overlay; assembled primary, secondary and affected opening/handling views;
critical seams and protected zones; closest-confusable SKUs in one identical
lineup; and relevant shelf, distance, thumbnail and e-commerce derivatives.
For visible frame or panel clearance, use painted fill and stroke edges in the
actual face, not only equal element coordinates or bounding boxes. Check every
repeated SKU face; matching source numbers do not prove matching visible gaps
when stroke widths, fills, clipping or transforms differ.

Compare before/after with identical product content, geometry, camera/view,
lighting, scale and context. Obtain a physical sample, barcode verification,
regulatory approval and provider proof only from their responsible lanes.

Packaging owns graphic mapping on supplied geometry, panel/face communication,
pack hierarchy, SKU grammar, packaging-specific derivatives and their visible
context proof. Brand owns identity architecture, CI and cross-touchpoint
governance; this leaf owns the package template's panel/SKU structure, including
hierarchy and mapping between package faces. Composition joins only when a
separate general within-frame hierarchy, grouping, spacing, grid or content-fit
system is materially open; it does not duplicate packaging-specific panel or
pack hierarchy. General craft experts retain type, colour and imagery systems.
Structural, material, product, regulatory, barcode, rights, sustainability and
Production owners retain their decisions and acceptance.

Claim only the inspected artwork, geometry version, SKUs, views and context.
Do not claim structural fitness, legal completeness, scanability, print
readiness, provider acceptance, sustainability, shelf performance, purchase
effect, recognition or correct consumer choice from a graphic render or mockup.
