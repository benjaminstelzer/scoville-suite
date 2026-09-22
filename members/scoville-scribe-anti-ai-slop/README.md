# Scoville Scribe Anti-AI-Slop

A rewrite can sound better and say something different. "May reduce latency"
becomes "will improve performance", or a summary loses the condition that made
the result true. Smooth prose does not repair a changed claim.

Scoville Scribe drafts, edits, summarizes, localizes and audits requested text.
It improves clarity while preserving meaning, evidence, terminology and the
author's position. It also checks whether an explanation gives the reader
enough information to understand and act.

## How it works

- Identify the requested transformation, audience, source facts and canonical terms.
- Route each segment to the relevant prose, interface or fidelity guidance.
- Make the smallest useful revision and compare it against claims, conditions and source boundaries.
- Check referents, introduced concepts and causal links from the reader's perspective.
- Keep ordinary conversation outside the Skill. Scoville Plan owns its own records when applicable.

## What it enforces

- **Facts survive the edit.** Numbers, quotations, conditions, attribution,
  modality, and uncertainty keep their meaning.
- **Canonical terms stay canonical.** A setting named `Padding` keeps that name
  so the reader can find it in the product.
- **Working strings keep working.** Placeholders, ICU branches, access keys,
  shortcuts, schemas, and accessible names retain their contracts.
- **Behavior-bound text stays true.** Interface labels, help, errors, and
  procedures describe supported behavior rather than desired fiction.
- **The author's position survives.** Voice may improve without inventing
  certainty, experience, identity, or conclusions.
- **Prose is built around sentences.** Rewrite sentences that rely on em
  dashes, en dashes, or semicolons instead of mechanically replacing the marks.
  Structure newly written or edited prose primarily with periods and commas,
  using `-` only sparingly when a dash is genuinely needed. Existing text outside
  the requested edit scope stays unchanged, as do exact quotations, protected
  source text, and technical syntax.
- **The requested operation stays narrow.** An audit reports. An edit changes
  the smallest real defect. Source-exact output remains exact.
- **Filler does not stand in for meaning.** Check unearned contrasts, vague
  authority, inflated significance, and decorative formatting. Interface copy
  names the actual action and state without unsupported reassurance or
  celebration. These are contextual editing checks, not authorship detection.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/blob/main/scoville-scribe-anti-ai-slop/SKILL.md).

## What it costs

- Source comparison and revision use additional tokens and time.

## How it was developed

- Scribe grew through writing tasks where an apparently better sentence changed the meaning.
- I examine the source, the final text and the task history together to find missing conditions, altered terms and explanations that still leave the reader guessing.
- Those cases guide changes to the instructions.
- Real-project histories are analyzed alongside results to identify failures and unnecessary context use.
- Targeted simulation and optimization workflows inform revisions. Changes are retained only when the required behavior survives.

- Development links: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-scribe-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-scribe-anti-ai-slop/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-scribe-anti-ai-slop/development/README.md)

## Compatibility

Any Agent Skills host that can read references/. No scripts, no network, no subagents. Whole-file Source-exact work needs a byte-preserving file read and write that keeps encoding, line endings and trailing whitespace (not a line-splitting shell reader). Developed for Codex and Claude Code; other hosts untested.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

## How to use

Name Scoville Scribe when wording must improve without changing its factual or
technical contract:

```text
Use Scoville Scribe to tighten this release note while preserving every claim, version number, condition, and uncertainty. Keep the existing product terminology.
```

```text
Use Scoville Scribe to localize these interface strings into German. Preserve placeholders, access keys, ICU branches, and the distinction between labels, help text, and errors.
```

```text
Use Scoville Scribe in Source-exact mode to extract the text between the named markers. Preserve the selected bytes and return nothing else.
```

Explicit `$scoville-scribe-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Sources

- [W3C Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name)
  for visible control text and accessible names.
- [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/)
  for selector branches, runtime values, and localization contracts.
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/word-choice/use-technical-terms-carefully)
  for consistent product terminology.
- [Reinhart et al.](https://doi.org/10.1073/pnas.2422455122) and
  [Wang et al.](https://aclanthology.org/2025.findings-emnlp.532/) for limits of
  LLM style imitation and authorship inference.
- [Peter Yang's no-ai-slop](https://github.com/petergyang/no-ai-slop) for
  reader-first editing and skepticism toward word-list detectors.

## Family

- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns engineering scope, implementation, risk, and validation.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans, Work Items, Decisions, and lifecycle state.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns wording, terminology, factual meaning, and source fidelity.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns framework-aligned implementation, interface mechanics, accessibility, and rendered evidence, with a standalone design fallback.
- [WordPress UI Backend](https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop) owns plugin-owned WordPress admin interfaces, platform components, spacing, accessibility and internationalization.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns visual definition, art direction, design systems, critique, and repair.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active work to another agent or session.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web, GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores materially different mechanisms before selection.
- [Workflow Codex](https://github.com/benjaminstelzer/scoville-suite) coordinates explicit Plan execution through native Codex project tasks.

## License

MIT. See [LICENSE](LICENSE).

