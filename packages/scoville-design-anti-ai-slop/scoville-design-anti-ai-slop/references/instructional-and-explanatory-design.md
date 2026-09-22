# Instructional and explanatory design

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-INSTRUCTIONAL-COMMUNICATION`, `SRC-COMMUNICATION-CLARITY`, `SRC-DIAGRAM-SEMANTICS`, `SRC-DATA-ACCESS-LOCALE`, `SRC-SOURCE-EVIDENCE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when a visual artifact must teach a concept, correct a misconception,
explain a mechanism or causal relation, demonstrate a procedure, support a
decision path, communicate a warning, or provide evidence of understanding.
Do not load for a generic diagram with no learning or explanation objective,
an ordinary information display, curriculum planning, a lesson plan, long-form
wording, UI onboarding mechanics, LMS implementation, or source verification
alone.

## Explanation record and authority

Record the explanation objective, intended audience and context, prior
knowledge, required terms, likely misconception or use error, authoritative
subject source, protected facts and sequence, target action or transfer,
medium, exposure and replay conditions, accessibility needs, consequence of
misunderstanding, proof target, approval owner, and unknowns. Distinguish what
the learner must recognize, describe, predict, choose, perform, or transfer.
Do not infer prior knowledge, a safe procedure, hazard, warning, or domain fact
from general familiarity.

For procedures and warnings require, when applicable, an authoritative supplied
procedure, preconditions, equipment and environment, action order, decision
branches, stop conditions, hazards, warning content, recovery, completion
state, and qualified owner. If any safety-critical field is missing or
contradictory, keep the explanation provisional and block release. Design may
make authorised content perceivable and test comprehension. It cannot determine
that the procedure is safe or complete.

Use only open relevant fields; otherwise use the Core minimal record:

`objective | audience/prior knowledge | protected truth | misconception or use
error | sequence or model | term and referent map | visual-verbal relation |
guidance and check states | warning chain | access equivalent | proof target |
source/owner/status | unknowns`.

## Generate and decide

1. State the smallest observable learning or execution outcome. Replace vague
   goals such as understand or know with the distinction, prediction, choice,
   action, or explanation that would demonstrate it.
2. Build a correct content model before styling. Identify entities, states,
   parts, actions, relations, causality, chronology, scale, uncertainty, and
   exceptions. Preserve the source's limits. Do not make a continuous process
   look discrete, a correlation causal, or a simplified model complete.
3. Start from the audience's likely model. Expose the exact misconception,
   hidden relation, unfamiliar term, or action ambiguity the artifact must
   repair. Remove background that does not support this change.
4. Choose a representation by job. A diagram can expose relation, a sequence
   can expose change, an annotated image can identify real parts, a comparison
   can discriminate cases, a map can locate, and text can preserve conditions
   and nuance. No modality is inherently clearer.
5. Assign complementary jobs to words and visuals. Put labels next to their
   referents, synchronize narration with the visible change when time matters,
   and preserve exact conditions near the action they govern. Intentional
   repetition is valid for access, memory, verification, or error prevention.
6. Segment by conceptual or action boundary, not by arbitrary card count. Give
   the learner control over pace when possible. Prepare essential terms before
   they are needed, but do not turn every term into a preface that delays the
   task.
7. Signal structure through hierarchy, grouping, alignment, sequence, emphasis,
   numbering, or motion only where it directs attention to a meaningful
   relation. Decoration that competes with the model is extraneous. Rich
   context is valid when it carries identification or transfer.
8. For procedures, make preconditions visible before action. Keep each action,
   object, location, state, and result unambiguous. Show branches at the point
   of decision, a check after consequential actions, recovery where failure is
   foreseeable, and a recognisable completion state.
9. Place warnings before exposure to the hazard. Connect the hazard, consequence,
   avoidance action, and stop or recovery condition without separating them
   across screens, pages, panels, or temporal steps that can be skipped. Use
   only approved warning language and symbols.
10. Design an equivalent route for the required task. Alternatives may use
    structured text, tactile or audio information, captions, transcripts,
    tables, descriptions, or assisted practice. An alternative is adequate
    only when it preserves the relevant learning or execution relation.
11. Prototype with real content at intended size, pace, device, distance, and
    environmental conditions. Ask participants to predict, explain, choose, or
    perform. Preference and visual polish are not comprehension tests.

For a multi-state physical or diagrammatic instruction, make a transition
ledger before styling: `part identity | state N geometry/label/colour | state
N+1 geometry/label/colour | permitted transformation | unresolved physical
claim`. Check every adjacent transition and the final state. Visible continuity
can validate identity and direction; assembly or folding feasibility remains
unverified without an appropriate construction view, model or physical trial.

## Build an example that can transfer

For a fictional sorting rule “A to M titles use the upper shelf; N to Z use the lower
shelf”, show one supplied title, highlight its first letter and connect that
letter to the correct shelf. Then show a deliberately wrong placement with
the violated branch marked. Give a new title whose answer is initially absent
so the reader must apply the rule rather than copy the picture. Preserve the
rule's exact alphabet and scope; this example supplies no advice for other
writing systems. If the audience already knows the distinction, the short rule
alone may be sufficient. Use an observed response for a learning claim;
including a practice item does not prove that learning occurred.

## Critique failure signatures and causes

- **Visually clear but conceptually wrong.** The rendering is coherent while
  source relations, scale, state, uncertainty, or causality changed. Repair the
  content model before layout.
- **Audience can follow but not transfer.** The artifact demonstrates one
  surface example without the governing relation, varied case, or boundary.
  Expose the invariant and test a new instance.
- **Labels require visual search.** Referents are distant, ambiguous, crossed,
  transient, or identified only by colour. Repair adjacency and durable
  identity before adding a legend.
- **Every fact is emphasized.** No learning priority exists, so signalling
  becomes noise. Rank prerequisite, governing relation, action, exception, and
  background.
- **Sequence is decorative.** Panels or animation imply order without showing
  state change, dependency, or decision. Restore meaningful transitions or use
  a static representation.
- **Narration, text, and image compete.** Modal allocation repeats long content,
  arrives at the wrong time, or splits attention. Reassign jobs and synchronize
  only the relation that benefits.
- **Procedure assumes hidden knowledge.** Tools, starting state, object names,
  direction, feedback, branch, or completion cue is missing. Add the smallest
  authoritative support before simplifying language or graphics.
- **Warning is visible but ineffective.** It appears after the hazardous action,
  lacks referent or avoidance action, competes with surrounding emphasis, or
  uses an unverified symbol. Repair the warning chain and obtain safety review.
- **Example becomes the rule.** A convenient case hides exceptions or creates
  false precision. State the bounded model and add a counterexample when it
  changes correct action.
- **Comprehension is inferred from attention.** Gaze, completion, liking, or
  designer agreement was treated as understanding. Run an outcome-matched task
  or narrow the claim.
- **Accessible alternative loses the lesson.** Alt text names an image but
  omits the relation, sequence, values, or decision required by the objective.
  Rebuild the equivalent around the task.

For every finding name the exact frame, step, relation, or referent, the visible
observation, likely learner error, source authority, confirmed or inferred
cause, consequence, smallest repair, protected truth, validation task, owner,
and unknowns. Separate a visual defect from absent source truth, an intentional
simplification, attributed preference, and unverified comprehension.

## Repair and regression

Repair in causal order. Correct authoritative content or content mapping before
representation, representation before sequence, sequence before signalling,
and signalling before surface polish. If the supplied source is wrong,
contradictory, or incomplete, return it to the domain owner rather than
silently repair it as design.

Preserve correct relations, required terminology, approved action order,
warnings, strong examples, successful referent mapping, and useful learner
control. Re-render only affected states, then recheck the complete explanation
at actual exposure. Test prerequisites, first use, branches, errors, recovery,
completion, replay, locale, reduced or static mode, and the equivalent access
route when applicable.

Compare before and after with the same task and content. Test the intended
outcome directly. Examples include identifying the correct part, predicting a
state change, explaining the relation in the participant's own words, choosing
the correct branch, executing the authorised procedure, or applying the model
to a new case. Record prompting and assistance because they change the claim.

## Rules and deliberate exceptions

Binding constraints include authoritative facts, supplied procedure order,
hazard and warning content, required terminology, source limits, protected
states, access duties, and qualified approval. Common practices such as
coherence, signalling, contiguity, segmenting, pretraining, worked examples,
and learner pacing are contextual mechanisms, not universal recipes. Expertise,
task, medium, time pressure, culture, and prior knowledge can change their
effect.

Dense expert displays, delayed labels, productive ambiguity, desirable
difficulty, non-linear exploration, decorative context, deliberate redundancy,
or a continuous animation can be valid when the explanation objective requires
it, the audience can use it, protected truth and access survive, and a named
test can falsify the choice. A creative exception cannot alter an authorised
procedure, hide a hazard, weaken a required warning, or substitute designer
judgment for safety acceptance.

## Proof, ownership, and claim ceiling

Evidence can include the frozen source model, objective and misconception
record, storyboard or state map, referent dictionary, real-content prototype,
warning and procedure trace, access equivalent, participant task protocol,
observations, response artifacts, error and assistance log, repair comparison,
and qualified approvals. A correct source model plus a polished render proves
only the represented explanation. It does not prove learning or safe action.

This leaf owns explanation objective, visual content model, sequence,
visual-verbal coordination, guidance, referent and check-state integrity,
cognitive-load cause localisation, and comprehension-test contract. Domain and
source owners own factual and procedural truth. Qualified safety, regulatory,
medical, technical, or operational authorities approve hazards, warnings, and
safe execution. The wording owner owns final wording. The implementation owner owns interactive mechanics and
states. Curriculum owners own learning programmes. Production owns delivered
artifact proof.

Claim `source-mapped`, `relation-rendered`, `procedure-sequence-inspected`,
`access-equivalent-inspected`, or `comprehension-tested for the named task and
participants` only when that evidence exists. Do not claim general learning,
retention, transfer, accessibility conformance, safe operation, regulatory
compliance, curriculum quality, or universal clarity from a render, expert
review, completion rate, or unprompted model judgment.
