---
name: scoville-scribe-anti-ai-slop
description: Guardrail for requested wording artifacts and transformations such as drafting, editing, source summaries, localization, source-exact work, wording audits, and reader-facing interface text. Use when wording itself is the deliverable or an independently constrained segment. Do not use for ordinary conversation, explanations, status, domain results, final framing, or uninvoked fixed insertion merely because they contain text. If Scoville Plan is available and applicable to native planning records, Plan alone owns their writing, rewriting, and wording audits under its own writing rules, even if it must first be loaded. Do not apply Scribe writing rules to those records. Preserve facts, meaning, terms, behavior, schemas, attribution, and exact text.
compatibility: "Any Agent Skills host that can read references/. No scripts, no network, no subagents. Whole-file Source-exact work needs a byte-preserving file read and write that keeps encoding, line endings and trailing whitespace (not a line-splitting shell reader). Developed for Codex and Claude Code; other hosts untested."
---

# Scoville Scribe Anti-AI-Slop

Write effective artifact text without changing truth, meaning, canonical terms,
or behavior, and without filler.

**Explicit opt-out:** load no references; use no Skill-directed tool; change no
text; make no Skill-derived claim. Report higher-authority requirements to use
Scribe.

## Activate only for text artifacts

If Scoville Plan is installed, available, and applicable to native Plans, Work
Items, or Decisions, route the record to Plan and load Plan if needed. Plan
alone owns their wording and fidelity under its own writing rules. Do not
activate, load, or apply Scribe to those records, including rewriting, wording
audits, and follow-up transformations. A request to use Scribe does not override
Plan's writing rules for these records. If Scribe is already active for another
segment, keep it scoped there. Unrelated prose in a mixed task may still use
Scribe.

If Plan is absent, unavailable, or inapplicable, use Scribe's normal activation
rules and preserve the existing record owner's format and lifecycle. Never
require, install, or simulate Plan to do that work.

Only when Plan is absent, unavailable, or inapplicable may Scribe handle native
record wording. In that case, keep fixed short fields Core-only within Scribe
and route independently requested continuous prose through Prose. Preserve the
record owner's permitted edits, format, and lifecycle. If context does not show
whether the target is a fixed short field or continuous prose, determine the
target segment first. Ask only if the remaining ambiguity materially changes
the output.

Activate Scribe when wording itself is a requested deliverable or transformation
target: drafting, editing, rewriting, summarizing supplied source material,
localizing, source-exact work, wording or fidelity audit, named-audience or
named-genre copy, publication-ready or paste-ready text, explicit reuse, or
reader-facing interface text.

Do not activate Scribe for ordinary answers, analysis, explanations, status or
progress recaps, domain review findings, research answers, final framing, or a
domain owner's normal record merely because the result contains prose. Chat,
file, commit, or other delivery alone neither activates nor suppresses Scribe.
Incidental comments, docstrings, commit messages, and pull-request text remain
with Code; explicitly requested drafting or rewriting of those artifacts adds
Scribe, with Code retained when engineering truth must be derived or verified.

Classify mixed tasks per segment. A domain owner's normal result does not add
Scribe without an independent wording or fidelity trigger. A referential
follow-up transformation of an active artifact reactivates Scribe; a pivot to
ordinary explanation does not inherit it. Fully supplied fixed insertion with
no wording, fidelity, terminology, behavior, or interface judgment does not
activate Scribe unless the user explicitly invokes it.

For Source-exact extraction or reproduction, preserve the requested boundary
and that span's whitespace and newline state. When markers occupy their own
lines, the separator newline before the end marker is not part of the selected
span unless the boundary explicitly includes it. For whole-file Source-exact or
opt-out passthrough, read and write the file through a byte-preserving path that
keeps encoding, line endings, and trailing whitespace intact; never through a
reader that splits lines, normalizes newlines, or re-encodes text. Serialize
directly. Fixed insertion copies the supplied string exactly.

## Resolve authority and scope

Resolve compatible host, project, request, and Scribe constraints per segment
during writing:

| Concern | Ordered authority |
|---|---|
| Current truth | Verified behavior; supplied facts |
| Target truth | Engineering evidence before completion/publication |
| Terms | Explicit user terms; glossaries; shared strings; established same-concept usage |
| Form | Explicit requirements; house style; genuine voice samples; surface/genre conventions |

Report material conflicts. Behavior outranks terms; facts outrank style. Resolve
only output-affecting reader, allowed facts/claims, voice, language, genre, form,
and integrity. Ask only when an unknown changes output materially.

Within its permitted scope, Scribe owns wording/meaning and minimal targeted
read-only term/text inspection. Plan-owned records remain outside that scope.

The Plan ownership rule above applies even when Plan is not yet active.

Finding another Skill in this family does not make it installed, active, applicable, or required. If that Skill is absent or inactive, ignore it. Do not require, install, simulate, or reimplement it. If it is active and applicable, let it handle only its stated concern while this Skill continues its own authorized work. An opt-out applies only to the Skill the user excluded, not to independently authorized work.

Relevant neighboring owners:

- `scoville-plan`: native Plans, Work Items, Decisions, and their wording.
- `scoville-code-anti-ai-slop`: engineering scope, behavior, risk, and validation.
- `scoville-design-anti-ai-slop`: visual definition and art direction.
- `scoville-ui-anti-ai-slop`: interface mechanics, states, accessibility, and rendered proof.

Reuse sibling evidence; without Plan, preserve owner format/lifecycle
and edit permitted wording only. Never infer behavior from copy. Fixed
source-exact rendering does not trigger UI.

After safety and explicit constraints, serve the artifact reader's required
knowledge, decision, or action. Change text only for a binding request or
convention, a concrete defect, or that outcome. Match detail; include required
causal links and boundaries, plus useful examples.

## Verify explanatory substance

Apply this check to explanatory text in every route, including short help,
articles, reports, onboarding, and manuals. Voice and house style do not waive
it. Judge sentences in their reading order using the audience knowledge already
established and the preceding text, not facts known only to the writer or
explanations that appear later.

- Identify the concrete subject and referents. Can the reader tell what is
  activated, changed, connected, or meant by "it" and "these values"?
- Identify the information gained. A sentence must explain a relevant fact,
  relationship, distinction, or consequence. Remove empty orientation rather
  than making it sound more specific with unsupported detail.
- Introduce necessary concepts and controls before relying on them. An exact
  interface label can identify a control without explaining its purpose.
  Explain only the unfamiliar knowledge needed for the next point.
- For an instruction, check the affected object, location, prerequisites,
  required input or choice, and expected result as applicable. For "review",
  "check", or "adjust", state what to look for and how that observation guides
  the decision. Do not invent universal criteria where judgment is contextual.
- Make required causal links and scope explicit. The reader must be able to
  follow why the stated result follows and which cases it covers.

The surrounding passage may supply these answers. Do not force every sentence
to repeat them, expand clear labels, or turn non-instructional prose into a
procedure. Assess direct-entry sections against their own stated prerequisites.
Protected quotations, fixed insertions, and deliberate ambiguity retain their
existing boundaries.

For each defect, formulate the unanswered reader question, locate the missing
answer, and repair it from permitted facts. If those facts are unavailable,
report the gap instead of inventing a bridge. Re-read the revision against the
same question and check that voice edits did not remove the answer. In an audit,
report location, question, reader effect, and correction direction. In drafting
or editing, perform this check silently unless findings are requested. A
punctuation, keyword, or term-presence check is not evidence of comprehension.

## Select mode and references per segment

Route by the requested transformation and target artifact surface. Neither the integrity
floor nor comparison against facts, requirements, behavior, or a glossary
selects Fidelity; add it only for an explicit Fidelity operation below. Combine
routes only when each route independently triggers for the same segment.

Selecting exact tokens from a structured requirements record is not
Source-exact extraction/reproduction. A stepwise non-interface procedure stays
Core-only unless a Fidelity-row trigger independently applies.

If a route or profile report is requested, use the selected references for
that report. If no reference route is selected, report `CORE_ONLY`. Otherwise
report exactly the selected routes in the order of the reference-route table
below.

| Mode | Core rule |
|---|---|
| Fixed insertion | Fully supplied wording plus fixed structure, with no wording, fidelity, terminology, behavior, or interface judgment: insert and load no reference despite surface triggers. Extraction/reproduction is Source-exact. |
| Structured grouping | Retain every enumerated item and unresolved lifecycle choice; load no reference. |
| Draft | Use only permitted facts/claims. |
| Edit | Make the smallest sufficient change. Claim-preserving rewrite is Edit. |
| Audit | Report location, problem, reader effect, correction direction. Rewrite only if asked; follow the subject's route. |

Reference routes:

| Read | Before or for |
|---|---|
| [Fidelity](references/fidelity-modes.md) | Adaptation; material summary; localization; Source-exact extraction/reproduction; audits of those outputs; controlled variants; regulated or author-owned drafting/editing. |
| [Interface](references/interface-text.md) | Writing, changing, auditing, or comparing any non-Fixed-insertion user-facing GUI/CLI string, error, notification, transactional message, accessible text, metadata, or behavior-bound procedure. Product-generated email uses Interface. Editorial, personal, and newsletter prose follows prose routing unless behavior-bound. User-facing localization also needs Fidelity. |
| [Prose](references/prose-patterns.md) | Continuous artifact prose; independently requested substantive rationale; requested natural, human-sounding, or anti-slop artifact writing. Use Prose instead of Fidelity for continuous claim-preserving rewrites unless Fidelity also triggers. Exclude domain-owned normal records, format-owned fixed short records, and behavior-bound interface procedures. A non-interface artifact procedure triggers Prose only when the task allows its explanatory wording to be changed independently of the prescribed steps. Audit artifact prose claims with Prose unless Fidelity triggers. |

Classify mixed artifacts only far enough to route each segment correctly.

## Preserve integrity

Never invent or silently change: names; numbers, dates, units; links, citations;
attribution, quotations, exact-text boundaries; schemas, technical terms;
negation, modality, conditions, exceptions; first-person experience, identity,
relationships, opinions, feelings; product capabilities, causes, guarantees,
timelines, actions, or verified runtime behavior. Mark hypotheses/examples as
hypothetical. Preserve unresolved deliberate ambiguity.

Behavior-bound text states the supported current state. Describe a requested
future state only in the artifact intended to represent that state. Do not
present the target as verified current behavior; the owning engineering workflow
must verify it before completion or publication. Preserve
procedure prerequisites, order, inputs, warnings, commands, placeholders, and
expected results unless request or verified behavior changes them.

High-risk legal, medical, financial, safety, privacy, or publication claims need
appropriate authoritative sources and qualified review; editing is neither.

Preserve strong passages and demonstrated register. Never diagnose AI
authorship, promise detector evasion, or vary canonical terms for style. Beyond
explicit constraints and the punctuation house style below, do not invent
universal word, punctuation, sentence-length, or formatting bans. Apply routine
guidance silently. Disclose only host-required non-obvious actions,
pauses, scope changes, external effects, or material risk.

## Punctuation house style

Build newly written or edited natural-language text, including interface copy,
around complete sentences and grammatical clauses, primarily using periods
and commas. Do not use em dashes (U+2014), en dashes (U+2013), or semicolons (`;`).

Rewrite affected sentences, not just their punctuation. Integrate asides into
the main clause, connect related ideas grammatically, or split a thought into
self-contained sentences while preserving its logical relationships. Do not
keep the old construction by swapping in other marks, including hyphens,
colons, parentheses, commas, or periods.

If a sentence genuinely needs a dash, use only the ASCII hyphen (`-`) and use
it sparingly. Keep necessary compound-word hyphens and required list markers.

Preserve punctuation inside exact quotations, Source-exact or fixed-insertion
content, code, commands, URLs, identifiers, and canonical names. These rules
govern newly written prose and prose within the requested edit scope, not
protected source text or syntax. Leave existing text outside that scope
unchanged. The rules apply across languages and do not imply that punctuation
proves AI authorship.

## Complete

Before return, verify reader outcome through the explanatory-substance check
where applicable, touched integrity items, each segment's
surface/fidelity route, requested language/format/length/mode, sentence-first
punctuation house style within the requested writing or edit scope, and removal
of unrequested process commentary. Report unresolved factual/project conflicts.
Audit-only means no edit.
