# Diagrams and relational information

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-DIAGRAM-SEMANTICS`, `SRC-DATA-CANON`, `SRC-DATA-EMPIRICAL`, `SRC-DATA-ACCESS-LOCALE`, `SRC-SOURCE-EVIDENCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when nodes, actors, states, steps, systems, containers, dependencies,
messages, flows or other relations must be designed, judged or repaired. Load
when direction, cardinality, containment, ordering, notation or source-model
parity can change meaning. Do not load for decorative arrows, ordinary charts,
geographic maps, or a settled diagram whose only open issue is file export.

## Inputs and formal variables

Begin from an authoritative typed model, not the current drawing. Record only open relevant fields; otherwise use the Core minimal record:

- `Q`: audience, question, lookup/tracing/explanation task, consequence and
  allowed abstraction;
- `N`: stable node IDs, types, labels, states, scopes, ownership and attributes;
- `R`: stable relation/edge IDs, source and target, relation type, direction,
  cardinality, state/condition, ordering and permitted endpoints;
- `C`: containment, hierarchy, lanes, boundaries, phases, repeated entities,
  cross-view identity and rules that distinguish grouping from ownership;
- `T`: selected standard notation and version, custom symbols, markers, line
  styles, orientation, key and explicitly unsupported semantics;
- `M`: dimensions, viewing/reading distance, interaction, locale/script,
  structured alternative, print/static fallback and receiver;
- `P`: immutable model facts, protected labels, approved abstraction, source
  version and relations that may not be invented or deleted;
- `E`: model diff, syntax/validator, render, access, domain-owner and audience
  evidence, including unknowns.

## Generate and decide

1. **Inventory before geometry.** Validate unique `N` and `R`; type every node
   and relation; resolve direction, cardinality, state and containment before
   drawing. An arrow must mean a named relation, not generic activity.
2. **Choose notation deliberately.** Use UML, BPMN, C4 or another formal system
   only when its semantics fit the source and audience. Follow the selected
   version exactly. For a custom grammar, define every node, edge, marker,
   direction and grouping cue in a compact key; do not borrow authoritative-
   looking symbols with changed meaning.
3. **Select views by task.** Separate overview, path, state, dependency or
   exception views when one frame cannot preserve both completeness and
   legibility. Keep stable IDs and an explicit scope/filter so decomposition
   does not become silent omission.
4. **Make geometry serve semantics.** Arrange by process order, topology,
   hierarchy, lifecycle or comparison as appropriate. Use alignment, spacing,
   ports, edge routing and crossings to support traceability. Proximity,
   enclosure, colour or lanes must not imply absent containment, sequence or
   ownership.
5. **Preserve relation readability.** Label ambiguous edges, distinguish
   direction and state redundantly where consequence is high, keep arrowheads
   visible at target size, and avoid crossings or parallel routes that make
   endpoint tracing uncertain. A tidy graph is not correct if it changes `R`.
6. **Provide a structured equivalent.** Supply the purpose and scope plus a
   task-appropriate node/edge list, adjacency, ordered steps, nested outline or
   textual path. Preserve IDs, type, direction, cardinality and conditions;
   localised labels may change presentation, not model identity.

## Lay out and trace the difficult relation

Sketch directionally ordered stages for a process, parent/child levels for a
real hierarchy, or a non-hierarchical arrangement for peer connections. A
radial centre implies a privileged entity; a neat circle can obscure sequence.
Choose from the actual question, not a layout engine's name.

For a feedback loop, place the main progression first and reserve a distinct
return corridor. Choose departure/arrival sides that preserve arrow direction
and keep the return label near its own segment, away from a competing edge.
Trace the loop from source node through label to the exact destination; repeat
in reverse as an inspection, not as a new graph relation. At a crossing, check
that no visual junction is implied. If moving one node solves several crowded
edges, compare that parent change before adding bends. Keep stable node IDs;
duplicating a node to tidy the page needs an explicit repeated-view notation.
Symmetry and curved routing remain valid when endpoints and relations read
clearly. These are local layout/tracing operations, not an automatic
comprehension test or a required notation.

## Critique: failure signatures and causes

| Failure signature | Likely parent cause to test |
| --- | --- |
| Arrow direction or meaning is ambiguous | edge type/marker/key absent; route or arrowhead unreadable |
| Clean-up removes or reverses a relation | geometry was edited without a source-model diff |
| Group looks like a container or owner | enclosure, proximity, lane or colour contradicts `C` |
| Same entity appears to be several entities | repeated node lacks stable identity or cross-view reference |
| Diagram is dense but decomposition loses paths | views lack declared scope, bridge IDs or completeness contract |
| Formal-looking symbol misleads specialists | notation version or semantics were invented, mixed or only decorative |
| Labels are readable but tracing fails | crossings, long parallel edges, hidden endpoints, weak direction or scale |
| Structured alternative disagrees | derivative was authored separately from the canonical `N`/`R` model |

Do not diagnose complexity from node count alone. Task, relation density,
label length, topology, notation literacy, scale and required completeness all
matter. Distinguish model defect, mapping defect, geometry defect and audience
unfamiliarity before proposing a repair.

## Smallest repair, preservation, and regression

Freeze `P` and diff current output against `N`, `R`, `C` and `T`. Repair in
this order: source model -> type/relation mapping -> scope/view -> notation ->
geometry/routing -> labels/style. If the model is wrong, return it to its owner;
do not silently correct reality in the picture. If geometry is wrong, move or
reroute without changing the inventory. Preserve valid abstraction, recognisable
orientation, stable IDs, working paths and successful hierarchy. After repair,
rerun the semantic diff and inspect every view/alternative; reject any result
that gains whitespace by deleting facts, merges unlike relations, invents
containment, breaks locale, or makes another required path untraceable.

## Rule classes and exceptions

The authoritative source model, selected formal notation, supplied scope and
applicable access/receiver contracts are binding. Evidence about graphical
perception or path tracing is task- and population-bounded. Orientation,
orthogonal versus curved routing, edge labels, colour, grouping, decomposition
and custom notation are contextual conventions.

An intentional crossing, repeated node, collapsed group, unconventional
direction, schematic geometry or custom symbol may be valid when its semantic
meaning is explicit, a key or cross-reference compensates, required paths stay
traceable, the source-model diff remains exact, and a conventional control does
not perform better. Never claim complete UML, BPMN, C4 or other conformance from
visual resemblance or a partial validator.

## Proof, ownership, and claim ceiling

Machine-diff stable node/edge/type/direction/cardinality inventories against the
authoritative model. Validate the selected notation where tools exist; inspect
markers, endpoints, labels, key, scope, repeated identity, containment and all
critical paths at target size. Compare rendered and structured alternatives
from the same model and test with representative tasks or accountable domain
review when comprehension matters. Mark untested paths and notation support
`unverified`.

Diagram Design owns visual relation, view and geometry. The model/process/domain
owner owns source semantics and completeness; Information Design owns
quantitative field encoding when present; UI and Production own interaction,
implementation and export proof. Model parity does not prove the model is true,
complete, current, comprehensible, standard-conformant, accessible, or fit for
operational decisions.
