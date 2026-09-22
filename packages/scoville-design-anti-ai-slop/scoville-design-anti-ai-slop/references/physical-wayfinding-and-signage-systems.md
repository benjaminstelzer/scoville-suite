# Physical wayfinding and signage systems

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-WAYFINDING-SYSTEMS`, `SRC-CARTOGRAPHY`, `SRC-TYPE-DETAIL`, `SRC-DATA-ACCESS-LOCALE`, `SRC-BRAND-CANON`, `SRC-PRODUCTION-PRINT`, `SRC-SOURCE-EVIDENCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when a physical journey, destination hierarchy, decision-point/location
schedule, route-confirmation system, sign family, route-integrated map, or
post-occupancy wayfinding audit must be designed, critiqued or repaired. Load
only when navigation through a real or supplied built environment is material.
Do not load for website/app navigation, a standalone map, one isolated room
sign or poster, non-navigational exhibition/environmental graphics, naming a
destination, architecture or landscape planning, GIS/survey work, regulated
escape/safety or traffic signage, structural/electrical mounting, fabrication,
installation, certification or provider acceptance.

## Authority and wayfinding record

Work from accountable site and destination information, not a plausible plan.
Record only open relevant fields; otherwise use the Core minimal record:

- `J`: people and journeys - origins, destinations, tasks, frequency,
  familiarity, time/stress, mobility, sensory/cognitive needs, languages,
  companions, carrying conditions and consequence of error;
- `D`: stable destination IDs, owner-approved display names, aliases only when
  authorised, hierarchy, parent/location relation, public/restricted state,
  opening or temporal condition, naming owner, source/version and change state;
- `R`: authoritative route/source version, entrances, exits, levels, paths,
  nodes, transitions, decision and confirmation points, arrival criteria,
  recovery routes, relevant landmarks, sight barriers and unresolved spatial
  truth;
- `S`: sign roles and IDs - orientation, direction, confirmation,
  identification, directory/index and bounded regulatory information supplied
  by its owner; message, location intent, approach, viewing condition,
  dependencies and lifecycle;
- `M`: map orientation and extent, symbol/arrow/colour/number conventions,
  terminology, language variants, tactile/audible/digital relations, brand
  constraints and alternate modalities that actually apply;
- `P`: approved names, route and access facts, safety boundaries, working
  landmarks, identity, legible information, privacy and intentional character;
- `E`: plan/site, route observation, prototype, render, participant,
  accessibility, safety, GIS, fabrication, installation and maintenance
  evidence, kept separate.

This leaf owns the structure and application of approved destination labels,
not the names themselves. If `D` or `R` is missing, stale, contradictory or
outside the supplied authority, stop the affected route decision and return the
exact question to the site/domain owner. Do not infer an accessible or safe
route from visual inspection, a floor plan, an ordinary path or model memory.

## Generate and decide

1. **Model journeys before signs.** Trace representative `J` from actual entry
   to confirmed arrival, including level changes, ambiguous branches,
   interruption, missed turns, backtracking and recovery. Distinguish route
   truth from a proposed communication layer. Adding more signs cannot repair
   a false route or inaccessible destination.
2. **Build one governed destination registry.** Apply owner-approved labels and
   hierarchy consistently across directories, signs, maps and supporting
   channels. Decide which level is necessary at each stage - site, building,
   zone, floor, department, room or service - without exposing irrelevant or
   restricted destinations. Do not rename a service to make a layout fit.
3. **Place information at decisions.** At each point, state the traveler's
   question, available paths, required distinction, advance notice, visible
   environmental cues, next confirmation and recovery. Reveal only the detail
   needed to choose and continue, but provide it early enough for a safe,
   realistic action. A sign at the destination cannot repair a missed upstream
   branch.
4. **Coordinate the sign family.** Define roles, recurring anchors, arrow and
   destination relations, ordering, terminology, typography, symbols, colour,
   numbering, maps and confirmation behaviour. Preserve recognition while
   adapting message length, location and viewing context. Do not give every
   sign equal prominence or use a graphical family to disguise inconsistent
   route logic.
5. **Connect map, sign and place.** Keep destination IDs, names, levels,
   directions, entrances and landmarks consistent. Choose map orientation,
   simplification and extent for the actual located task; record the spatial
   source and distortion. Cartographic appearance cannot establish GIS truth.
6. **Design multimodal intent.** Do not depend on colour, one learned symbol,
   visual acuity, one language, perfect hearing or smartphone access where the
   supplied access context requires alternatives. Specify redundant text,
   number, shape, landmark, tactile, audible or human-support relationships for
   qualified review; do not self-certify them.
7. **Prototype in route context.** Use plan annotations only to prepare the
   test. Inspect approach direction, sightline, occlusion, competing clutter,
   lighting, distance, decision timing, sign-to-place relation and confirmation
   along complete routes. Temporary full-scale signs can test information and
   placement intent; they do not prove mounting, photometrics, fabrication or
   compliance.
   On a drawn plan or sign, enumerate each route segment where it approaches or
   crosses label ink, arrows, markers and boundaries. Check painted clearance
   at those local intersections separately from path connectivity and topology;
   a connected route can still obscure its destination label.
8. **Govern change.** Bind every public label, map and sign message to `D`, `R`
   and an owner. Record additions, moves, renames, temporary closures,
   replacement, inspection and expiry so a corrected source cannot leave stale
   signs or derivatives in service.

## Fill a decision point from the route

Fictional source: arriving from Reception, the corridor branches left to the
Archive and right to the Store. Record the approach direction before drawing
arrows. Compare the sign's destination groups with that view, then follow each
choice to its next confirmation. “Archive” on arrival confirms location; the
branch sign answers a different question. A missed turn needs a recoverable
return to the decision, not an arrow invented from the page's left/right.

Place the proposed sign in an approach study with the viewer's line of sight
and the actual decision point. Check whether the message arrives before the
choice is committed. A straight route with one destination may need only
arrival identification. This original walkthrough tests message/route
relations; distance, installation, physical access and safe-route acceptance
still need their actual authorities and evidence.

## Critique: failure signatures and causes

| Failure signature | Parent cause to test |
| --- | --- |
| Many signs exist but travelers still hesitate | journey/decision model is wrong; information arrives too early, late or at the wrong branch |
| A destination appears under different names | destination registry, authority or version drift - not typography - is the parent failure |
| Direction is readable but the route is ambiguous | arrow/path relation, destination hierarchy, viewpoint or next confirmation is missing |
| A route works outbound but not on return or recovery | only the ideal journey was modeled; reversal, level change or missed-turn state is absent |
| Directory, map and signs disagree | derivatives do not share stable destination and route IDs or source versions |
| Sign family is consistent but places are hard to distinguish | identity grammar outran destination hierarchy, landmark relation or task difference |
| One large sign dominates yet the needed choice is missed | visual prominence was mistaken for decision timing and relevant information |
| Colour/symbol coding fails when separated from its key | code is learned, too similar, inconsistent, language-bound or the only carrier |
| Desktop mockup works but site view fails | approach, sightline, occlusion, light, distance, motion or clutter was not represented |
| Work looks accessible or safe but evidence is absent | visual intent was mistaken for user, specialist, route, standard or installation proof |

Localise findings to journey, origin/destination IDs, route/source version,
decision point, sign ID and approach condition. Separate a communication defect
from false spatial data, naming authority, architecture, regulated safety,
accessibility certification, installation and preference.

## Smallest repair and regression

Freeze `P`. Diagnose in this order: destination/route authority -> journey and
arrival definition -> hierarchy -> decision/confirmation placement -> message
and arrow/path relation -> sign/map family -> typography/composition/colour ->
local optical correction. Return false names, routes, accessibility or safety
facts to their owners. Repair the earliest owned wayfinding cause rather than
adding another sign or making every element louder.

Preserve correct names and paths, working landmarks, familiar orientation,
successful sign roles, identity constraints and valid access provisions.
Rewalk affected routes in both required directions and the relevant missed-turn
or interruption state. Recheck directories, maps, signs, language variants,
temporary states and every dependent location. A local repair may not create a
new ambiguity upstream, reverse another approach, expose restricted locations
or leave an old label elsewhere.

## Rules and exceptions

Binding constraints come from approved `D` and `R`, site and domain authority,
applicable safety/access/traffic standards, current CI, fabrication/provider
conditions and release state. Sign counts, viewing distances, letter-height
ratios, arrow forms, mounting heights, colour meanings, map orientation,
destination depth and maximum line count are not universal design rules.

A landmark-led route, sparse sign system, deliberate visual interruption,
unusual map orientation, local shorthand, colour district, duplicated
destination, temporary route or intentionally different sign may be valid when
the journey job, authority, audience, learned-code cost, stable
counterstructure, access/safety floor, affected routes, expiry and falsifier
are explicit. No aesthetic exception may invent a destination, alter spatial
truth, override regulated safety signs, authorise a route, or certify
installation.

## Proof, ownership and claim ceiling

Bind prototypes and renders to destination, route, plan/site and sign versions.
Inspect complete representative journeys from entry to confirmed arrival, not
isolated signs: every consequential decision, transition, level change,
confirmation and recovery point at its real or faithfully represented approach
condition. Compare control/before/after with identical routes, names, temporary
states and participant tasks. Add unfamiliar-user, access-specialist,
post-occupancy, safety, fabrication and installation evidence only from their
qualified lanes.

Wayfinding owns the physical journey model, approved-label hierarchy and
application, decision/confirmation information, sign-family relations,
route-integrated map intent, contextual prototype and route-evaluation record.
Site/domain owners own destination names and operational hierarchy;
architecture, GIS, transport, safety and access authorities own their facts and
requirements. Brand owns identity governance; Typography, Composition,
Cartography and Imagery own their craft systems; Fixed Media owns isolated
non-navigational fixed graphics; Production and specialists own fabrication,
installation and acceptance.

Claim only the inspected routes, destination/source versions, sign states,
participants and contexts. Do not claim spatial truth, universal findability,
comprehension, accessibility, code or safety compliance, emergency adequacy,
structural fitness, installation approval or post-occupancy success from a plan,
sign family, render or model walkthrough.
