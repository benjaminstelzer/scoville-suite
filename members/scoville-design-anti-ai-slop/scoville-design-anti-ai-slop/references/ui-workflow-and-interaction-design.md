# UI workflow and interaction design

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-UI-HCD-IA`, `SRC-UI-FORMS-STATES`, `SRC-UI-EVALUATION`, `SRC-BRIEF-HCD`, `SRC-BRAND-SYSTEM-GOVERNANCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when task flow, information architecture, navigation, forms, interaction
patterns, state/recovery intent, or product UI-system definition can change the
design. Do not load for a static marketing layout, visual styling alone,
responsive transformation without an interaction task, framework/component
implementation, ARIA or focus mechanics, browser testing, or backend policy.

## Design UI record

Record only open relevant fields; otherwise use the Core minimal record:

`outcome | actor/role | trigger/entry | domain objects/relations/lifecycle |
knowledge/data | decisions/branches | permissions/risk | side effects |
interruption/re-entry/cancellation | completion evidence | incumbent system |
open facts/policy | validation target | implementation owner`.

Do not invent policy, eligibility, analytics, research findings or user
success. Distinguish:

- **Information architecture:** objects, relationships, taxonomy, labels,
  permissions, lifecycle and findability.
- **Navigation model:** paths and controls through that structure, including
  orientation, current location, search, deep links and backtracking.
- **Task flow:** actions and decisions required to reach an outcome, including
  side effects and recovery.
- **Rendered navigation:** an implementation of the accepted intent, not the IA
  itself.

A screen list, sitemap, component inventory, organisation chart or database
schema is not a task model.

## Generate and decide

Map the shortest coherent path that preserves required knowledge, decisions,
control, status and recovery rather than minimising raw clicks. For each step
record `actor action | system response | decision | persisted data | side
effect | interruption | cancellation | recovery | exit`. Compare consequential
patterns as hypotheses against task frequency, object/data shape, risk,
platform convention, incumbent support, access intent, interruption and
recovery. State the benefit, failure condition and evidence that would overturn
the choice. Familiarity and novelty are not sufficient reasons.

For information architecture, test whether labels predict destinations,
sibling choices are distinguishable, current location is recoverable, filters
and context survive movement, and search complements rather than conceals weak
structure. There is no universal click count, item limit or correct depth. A
linear transaction may need no competing global navigation; a repeated
multi-task product may require persistent orientation.

For forms, record for each datum `purpose | user/consumer | required status |
sensitivity | accepted representations | dependencies | persistence |
validation moment | recovery`. Group by user task and semantic relationship,
not storage schema. Separate invalid input from eligibility, permission, policy,
unavailable service and server failure. Validate only when input is sufficiently
complete for feedback to be actionable. Preserve entered data, locate the
repair, prevent duplicate consequences, and supply honest completion evidence.

Derive states from `flow × data × permission × connectivity × latency ×
concurrency × risk × time`. For every applicable state record `trigger | visible
meaning | available actions | preserved information | persistence | exit |
recovery`; state why commonly expected states are not applicable. Distinguish
no data, no results, filtered empty, unavailable, denied, loading, partial,
stale, conflict, offline, interrupted, failure and committed success only where
they differ operationally. Use optimistic presentation only when rollback and
reconciliation are clear. Prefer undo for safely reversible changes and
confirmation for costly or irreversible consequences; neither is universal.

Define a UI design system as principles and product language, semantic roles,
pattern/component purpose, anatomy, variants, applicable states, content and
responsive intent, anti-patterns, accessibility intent, owners, contribution,
deprecation, maturity and evidence. Tokens or a component catalog encode
decisions; they do not make them. Preserve the incumbent system unless evidence
supports an owner-level extension, reinterpretation or replacement. Record the
gap, intended effect, allowed variation, migration and validation target.

Corporate Design/Brand supplies identity requirements, approved assets and
cross-touchpoint invariants. This leaf owns the product's workflow, pattern,
component-purpose and state-system definition. The implementation owner handles
strict framework/component implementation. No partner is required for
authorised implementation. A brand-governed template does not transfer
its medium-specific interactive structure to Brand, and framework availability
does not transfer design-system definition to UI implementation.

## Compare the cost of an editing pattern

For a frequently corrected single field, compare direct editing with a separate
detail view. Direct editing keeps the surrounding comparison visible but must
make edit state, save/cancel and failure recovery understandable. A detail view
can give related fields and consequential changes enough context, at the cost
of leaving the list and recovering position. A dialog may suit a bounded
interruption when focus and return are clear; it is not automatically the
middle answer.

Use the same task and content for the comparison. Count the meaningful context
switches and inspect how a mistaken value is recovered, rather than awarding
the fewest clicks. Keep the incumbent pattern when its task costs are already
appropriate. This example chooses interaction intent; it neither mandates new
controls nor implements the framework's state, focus or persistence mechanics.

## Critique failure signatures and causes

- **Shell-first dashboard:** sidebar, four KPI tiles, line chart and table
  precede the task. Test missing object or decision hierarchy. Rebuild IA and
  task pattern from the most frequent and highest-consequence decisions; show
  the state the actor must act on first. Keep useful monitoring tiles and familiar
  navigation when they serve that task; changing surface personality is no repair.
- **Ambiguous paths or lost context:** labels, grouping, lifecycle, location or
  deep-link model is wrong; repair the parent structure before another menu.
- **Database-shaped form:** field order follows storage, unnecessary or
  sensitive data lacks purpose, or branching surprises; restore task grouping
  and field necessity.
- **Premature or blaming error:** unfinished input, policy, permission or server
  failure is labelled user error; correct the condition, timing and recovery.
- **Happy-path-only UI:** partial, stale, conflict, permission, interruption or
  duplicate effects are possible but unmodelled; add only causally applicable
  states.
- **False success:** irreversible work has not committed; show pending truth,
  preserve control, and define reconciliation.
- **Near-duplicate system pattern:** a mockup forced local tokens or components;
  reuse the incumbent or request an owner-level change.
- **Cosmetic anti-slop repair:** gradients, cards, radii or familiar navigation
  are banned by fashion. Preserve them when they serve task and system; repair
  only interchangeability, weak hierarchy or unsupported decoration.

## Smallest repair and regression

Trace `observation → task/decision effect → workflow/IA/state/system cause →
smallest parent change → preserved facts/progress/system constraints → proof`.
Repair one owner-level cause rather than decorating screens. Preserve exact
content, stored input, task position, legitimate platform convention, incumbent
system and any state that already communicates truth. Regression-check entry,
completion, interruption/re-entry, cancellation, permission, failure, partial
success, duplicate action and consequential recovery where applicable.

## Exceptions

A custom pattern is valid when the incumbent cannot express the task and the
new pattern preserves recognition, control, recovery and access intent; record
its falsifier and owner approval. Dense interfaces can suit frequent expert
work, while high-consequence or unfamiliar tasks may need more separation and
disclosure. One-question pages, inline validation, confirmations, undo,
optimistic UI, navigation persistence and comprehensive state inventories are
contextual choices, never universal recipes.

## Proof and handoff

Design proof is an inspectable task/IA/state/system record, same-content state
set, causal critique, and validation targets. It establishes intent only.
The implementation owner maps
accepted intent to supported framework components, tokens,
semantics, names/roles/relationships, focus, keyboard/touch/input behaviour,
announcements, mechanics and runtime tests. If a framework constraint changes
the intended outcome, return that exact concern to Design rather than silently
redesigning. Require UI-owned runtime evidence before claiming behaviour,
semantics, focus, input, announcements, responsive mechanics or conformance.

## Ownership and claim ceiling

This leaf owns workflow, IA, navigation and pattern intent, form/state/recovery
intent, and UI-system definition. Product and policy owners own rules and
eligibility; visual craft owners own typography, composition, colour and
imagery; the implementation owner owns strict system/framework implementation
and rendered interaction evidence.
Heuristic review, a mockup, scanner or attractive render
does not prove intuitive, usable, user-centred, accessible, validated,
conversion-improving, policy-correct or successful.
