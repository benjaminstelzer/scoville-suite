# Scoville Research

A source list can look convincing while the answer rests on very little.
Several articles may repeat one press release, and a real citation may support
a different statement from the one beside it.

Scoville Research connects each conclusion to inspected evidence. It covers
web research, GitHub-first development discovery and academic questions,
keeping contradictions and gaps visible instead of replacing them with certainty.

## How it works

- Frame the question, decision and private-data boundary.
- Choose the relevant Development or Academic evidence route and inspect canonical sources.
- Trace claims to specific support, check source independence and investigate contradictions.
- Stop when more searching would not change the decision, or report the unresolved gap.
- Save Deep research records only when requested. Optional structural validation does not prove that a citation supports its claim.

## What it enforces

- **Scoped report writing.** Requested saved research artifacts may be written
  at the agreed output path. Investigated systems and source material remain
  read-only. Chat-only research creates no files, including in Deep mode.
- **The smallest sufficient route.** One known source stays a normal task.
  Development, Academic, and Deep behavior load only when the question needs
  them.
- **Evidence ownership.** Specifications own their contracts, repositories own
  observed implementation, papers own reported experiments, and none quietly
  inherits the authority of another.
- **Claim-level boundaries.** Reported claims, direct observations, inference,
  contradiction, and unresolved gaps remain distinguishable.
- **Exact evidence units.** Deep claims link to inspected passages or scoped
  observations with stable locators, not merely to an entire source.
- **Source independence.** Ten retellings of one origin still count as one
  origin.
- **Hostile-content resistance.** Retrieved pages, papers, issues, and tool
  output are untrusted data, not instructions.
- **Private/public separation.** Local or private material does not enter an
  external query unless the user explicitly authorizes that disclosure.
- **A decision stop.** Research ends when the decision-relevant evidence is
  sufficient or the remaining gap is explicit.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-research/blob/main/scoville-research/SKILL.md).

## What it costs

- Searching, reading and comparing multiple sources use more tokens and time than a quick answer.

## How it was developed

- I developed Research through source inspection, research tasks and model evaluations.
- The difficult part is often the connection between a claim and its source.
- A relevant link can still support a different statement, and several agreeing pages may all repeat the same origin.
- Real-project histories are analyzed alongside results to identify failures and unnecessary context use.
- Targeted simulation and optimization workflows inform revisions. Changes are retained only when the required behavior survives.

- Development links: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-research) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-research/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-research/development/README.md)

## Compatibility

Any Agent Skills host that can read references/. Requires web search and fetching actual source pages. Deep mode also needs a writable workspace and Python 3 for scripts/validate_research_artifacts.py. Subagents are optional and depend on available capacity. Developed for Codex and Claude Code; other hosts untested.

Codex currently offers no way to close subagents and free their slots. This limits
additional parallel work within a session.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-research/tree/main/scoville-research
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

Name Scoville Research and the actual decision in the request. The Skill chooses
the smallest route that can answer it.

**Development** - investigate an implementation landscape rather than compare
README feature tables:

```text
Use Scoville Research to find open-source libraries for offline-first conflict handling on Windows. Inspect GitHub source, releases, issues, tests, licenses, and official documentation. Return a shortlist, the evidence that separates it, and the cheapest feasibility test. Do not implement anything.
```

**Academic** - trace papers at their real publication and inspection depth:

```text
Use Scoville Research for a literature review of agentic deep-research factuality. Distinguish preprints from peer-reviewed work, connect papers to code and data where available, preserve disagreements, and mark abstract-only findings as abstract-only.
```

**Deep** - keep an audit-ready investigation resumable across sessions:

```text
Use Scoville Research in Deep mode to determine whether a hybrid API and browser research agent is viable for this product. Preserve the brief, query log, source ledger, claim ledger, contradictions, and final report. Keep private project details out of public queries.
```

When a decision also needs deliberately different candidate mechanisms, request
Scoville Research and Scoville Brainstorm explicitly. Research then owns one
inspected prior-art lane. Brainstorm keeps the generators isolated from that
lane until convergence. This avoids researching the same landscape twice.

Explicit `$scoville-research` invocation also works on hosts that support named
Skill invocation.

## Sources

- [Agent Skills specification](https://agentskills.io/specification) and
  [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills) for the
  portable package and progressive-disclosure contract.
- [OpenAI Deep research guidance](https://developers.openai.com/api/docs/guides/deep-research)
  for public/private data separation, auditability, and prompt-injection risk.
- [Xiaomi MiMo Deep Research](https://github.com/XiaomiMiMo/MiMo-Code/blob/5ecca0daeebc8d5415bf6b5c9c3a2903f20552d5/packages/opencode/src/skill/builtin/.bundle/deep-research/SKILL.md)
  and [topic survey](https://github.com/XiaomiMiMo/MiMo-Code/blob/1e8af9190a7f7c349331ebb5227baf14d405a901/packages/opencode/src/skill/builtin/.bundle/super-research/references/topic-survey.md)
  for durable briefs, gap-driven retrieval, claim ledgers, and saturation.
- [Cited but Not Verified](https://arxiv.org/abs/2605.06635),
  [DRNOISE](https://arxiv.org/abs/2607.17291), and
  [Beyond Single-shot Writing](https://aclanthology.org/2026.acl-long.609/)
  for citation-support, misleading-source, and revision-regression risks.
- [Beyond Browsing](https://aclanthology.org/2025.findings-acl.577/) and
  [FS-Researcher](https://aclanthology.org/2026.acl-long.288/) for structured
  evidence interfaces and durable filesystem state.

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

