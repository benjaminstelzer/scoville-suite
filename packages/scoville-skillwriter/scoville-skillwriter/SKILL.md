---
name: scoville-skillwriter
description: Write, simplify or review Skill instructions and reusable model prompts. Use with the host's skill-creator for Skill authoring, not for ordinary prose or executing Skills.
compatibility: "Agent Skills host with filesystem access and the host's skill-creator for Skill authoring: OpenAI's in Codex, Anthropic's in Claude Code. Standalone prompts need no skill-creator. No runtime scripts or network access required."
---

# Skillwriter

Write, simplify or review instructions while preserving their intended
behavior. Read [Agent instruction design](references/instruction-design.md)
unless its complete unchanged text is in context; apply its rules.

All Skills in this suite are installed and enabled together. Use the
Skill that owns a concern without checking its availability, and load only the
instructions the task needs.
Do not use a Skill that needs explicit activation before it is activated, or
one the user excluded.

## Choose the artifact and its owner

For Skill authoring, load the host's `skill-creator`: OpenAI's in Codex,
Anthropic's in Claude Code. It decides structure, metadata, packaging and
format validation. Leave the host's Skill Creator files intact. Skillwriter
decides wording. If no `skill-creator` is available, draft
the wording and report packaging as unverified. Standalone prompts need no
Skill package.

## Choose the mode

| Request | Route |
| --- | --- |
| Review | Apply the source checks and report findings and proposed changes without edits. |
| New Skill or prompt | Draft it, then apply the source checks. |
| Revision | Before the first edit, preserve the exact affected state in a Git revision that contains it or a temporary workspace copy. Keep it through the final comparison. Revise within scope and apply the source checks. |

A concrete revision request authorizes its changes. A review edits nothing.
Ask only for material changes to outcome, scope or boundaries that the request
or prior approval leaves open. Dropping an approval stop is material. Clarifying
the wording while keeping the requirement is within an authorized wording change.
Continue work independent of the open decision.

## Preserve the intention

Keep the intended outcome, scope, activation boundaries, facts, permissions,
required behavior and acceptance criteria unless the user explicitly asks to
change them.

Read the files needed to understand the change and its effects: `SKILL.md`,
references, included fragments and imported prompts. Do not reread
text that is still completely in context and has not changed. Identify the
affected consumers of shared text before changing it. Edit the source and
regenerate derived copies through their build path.

## Check the sources

Review the instructions and affected consumers once. Apply these checks to
the assigned scope in a review and to the resulting text after writing:

- the text does what this Skill and Agent instruction design require and
  agrees with the files that define authorization, activation and handoffs;
- each new or changed diagram parses with a Mermaid renderer or parser when
  one is installed and execution is authorized; otherwise report syntax as
  unverified;
- for a revision, the diff against the baseline holds every approved change
  and no other change to meaning, behavior or boundaries.

For a writing task, correct deviations within the authorized scope and recheck
affected findings.
Report unresolved mismatches. This one review is the whole authoring review;
write no separate certificate.

## Validate and evaluate

For Skill authoring, validate the package structure through the available
Skill Creator. A draft made without it keeps packaging unverified.
If a validator rejects a field the Agent Skills specification allows, such
as `compatibility`, keep the field. Complete the checks it skipped with the
project's validator or by direct inspection. Report what remains unverified.

Choose checks by what the change can affect. Run a model only when the user
authorizes model testing and the requested check or claim needs the result.
Use the required models and settings. Limit claims about model behavior to
the available results. Add model-specific detail for failures specific to a model.

| Change | Check |
| --- | --- |
| Wording or layout with unchanged required behavior | Clarity, consistency and preserved meaning against the baseline |
| Required behavior or output | The affected outcome and preserved boundaries |
| Activation or scope | Explicit and implicit activation, plus adjacent requests that must not activate |

Run a comparative evaluation only when the user requests one, following
[sources and evaluation](references/sources-and-evaluation.md); without one,
claim no improved effectiveness. Read that reference also
before citing vendor advice or research; it holds model-specific findings for
pruning prohibitions and stop rules and for low reasoning effort.

Report activation, procedural compliance, boundaries and task success
separately for what was tested. Name what remains unverified among your claims.
Shorter text, higher effort or self-reported success do not prove improvement.
A claim that a model follows the instructions requires a run with that model on
a task the change was not written against; a re-run of the task that prompted
the change shows only that the change fits that task.
