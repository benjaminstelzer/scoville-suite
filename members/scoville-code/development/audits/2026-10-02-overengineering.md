# Scoville Code: research and revision audit

Date: 2026-10-02. Scope: the full Scoville Code entrypoint, all four references,
canonical README fragments and retained evaluation cases. This audit is
development evidence, not an instruction to load during normal Skill use.

## Intent and authority

The user wants complete, maintainable implementations without speculative
compatibility, repeated scans, unnecessary recursion, defensive layers or
frameworks. The user authorized the researched changes, removal of unsupported
prescriptive work rules, a final comparison with the research, and retention of
this audit. No publication or commit was requested.

Two subsequent clarifications govern this revision:

- Keep the Greenfield base and naming defaults so new projects start with a
  consistent layout. This is an explicit user convention, not a claim that the
  layout experimentally improves code. Ecosystem requirements retain precedence.
- Preserve the protection against unsuccessful repair loops. The old two-attempt
  trigger had not caused observed problems. A more general progress-based rule is
  acceptable, but its effectiveness must not be assumed from its wording.

The reported Empco example motivates the scope. Its project code and Plan were
not inspected in this audit. The earlier external reviews are background, not
scientific evidence.

## How to interpret the evidence

The studies test different models, tasks, prompts and quality proxies. Most do
not test repository maintenance over many months. No cited study tests this
Skill or establishes its exact wording as optimal for current Codex or Claude.
Absence of a relevant paper is not evidence that a rule is harmful. User choices,
authorization, privacy and actual data guarantees do not require an experiment
to remain binding. Distinguish measured findings, our inference and project policy.

The source ledger retains limitations as well as positive findings. Statistics
refer only to each paper's experimental setup. ArXiv-only entries are treated as
preprints here. Recheck versions before relying on these findings in a new revision.

## Sources and implications

**R1. [RobuNFR](https://arxiv.org/html/2503.22851v1), 2025 preprint.**
Explicit nonfunctional requirements produced model-dependent tradeoffs.
Readability instructions did not uniformly reduce correctness: GPT-4o and
Claude 3.5 differed. The prominent reliability loss concerns error-handling
requirements, not an isolated test of human understandability. Readability and
reliability use proxy metrics, including lint conventions and exception density.
Implication: do not assume a broad readability or robustness instruction improves
code, and do not optimize the number of guards or exceptions as a quality target.

**R2. [ECCO: Can We Improve Model-Generated Code Efficiency Without Sacrificing
Functional Correctness?](https://aclanthology.org/2024.emnlp-main.859/), EMNLP 2024.**
Several efficiency-oriented generation and refinement methods improved cost
metrics while lowering functional correctness. Execution feedback often helped
preserve correctness better than unsupported natural-language refinement.
Implication: investigate actual repeated work and relevant cost questions with
focused evidence. This does not prove a one-pass rule or a recursion ban.

**R3. [Revisiting the Impact of Pursuing Modularity for Code
Generation](https://aclanthology.org/2024.findings-emnlp.676/), EMNLP Findings 2024.**
Modular examples and training data did not consistently improve generated
solution correctness. The experiments are not a comparison of human maintenance
costs or real repository boundaries. Implication: do not use module counts,
function counts or file size as a substitute for actual ownership and contracts.

**R4. [Modularization is Better: Effective Code Generation with Modular
Prompting](https://arxiv.org/abs/2503.12483), 2025 preprint.**
Structured modular reasoning improved benchmark results in the studied settings.
The evaluated reasoning method differs from R3's demonstrations and training
data. Its results do not establish that more production files or an obligatory
decomposition workflow improve a small change. Implication: permit useful
encapsulation without mandating general frameworks or a second consumer.

**R5. [ClarifyGPT](https://www.eecs.yorku.ca/~wangsong/papers/fse24.pdf), FSE 2024.**
Targeted clarification improved code generation on ambiguous tasks. In one
GPT-4 MBPP-sanitized setting the pass rate rose from 70.96% to 80.80%. The human
study used ten participants and reference test examples, limiting transfer to
open-ended product decisions. Implication: ask about actual unresolved contract
choices. No direct study of speculative prerelease legacy support was found.
The compatibility rule therefore remains a user-authorized product-scope policy.

**R6. [ClarifyCodeBench](https://arxiv.org/html/2607.00711v2), 2026 preprint.**
Models often missed key clarification questions. Clarification still left a
performance gap to complete specifications. Implication: name concrete question
triggers such as existing saved data and unresolved support, rather than asking
on every edit or assuming that reasoning alone resolves ambiguity.

**R7. [Are LLMs reliable code reviewers? Systematic overcorrection in requirement
conformance judgement](https://link.springer.com/article/10.1007/s10515-026-00638-5),
Automated Software Engineering, 2026.**
In the studied GPT-4o setting, rejecting correct HumanEval implementations rose
from 26.2% with direct judgement to 73.2% with explanation and repair instructions.
Models differed. Reviewers did not execute tests, and the authors acknowledge
that prompt variants may also change the implicit review rubric.
Implication: review against requirements and concrete consequences, accept no
findings as a complete result, and require evidence before corrective work.
This does not justify ignoring actual unnecessary mechanisms or missing guards.

**R8. [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v2), 2026 preprint,
version 2.** Generated context files increased average costs by 20% and 23% in
the two benchmark settings. Their average success-rate reductions were not
statistically significant. Developer files also lacked a significant gain over
no context, while outperforming generated files. Length alone did not explain
the results. Implication: examine work induced by instructions, not merely word
count. The paper evaluates repository context files, not Scoville Skills, and
does not establish that removing safety or project-specific rules helps.

**R9. [On the risk of coding before testing: An empirical study on LLM-based
test generation workflow](https://arxiv.org/abs/2607.05139), 2026 preprint.**
Tests generated after faulty code could repeat its errors. Reported fault
detection was approximately 14%, versus 25% for independently generated tests.
The experiment selected faulty implementations and is not a mandate for TDD or
separate test agents. Implication: derive expected results from the requested
behavior or independent contract for all tests, not only integration boundaries.

**R10. [Is Self-Repair a Silver Bullet for Code
Generation?](https://arxiv.org/abs/2306.09896), ICLR 2024.**
Self-repair gains were limited and dependent on feedback quality and evaluation
cost. The study does not establish an optimal two-attempt threshold.
Implication: require a supported next attempt and stop ineffective repetition.
The user's favorable experience with the former two-attempt rule is separate
project evidence. Retain that baseline if the generalized rule regresses.

**R11. [SlopCodeBench](https://arxiv.org/html/2603.24755v1), 2026 preprint.**
Successive changes exposed structural deterioration. Anti-slop prompts improved
some initial metrics without reliably stopping later drift or improving
correctness. Static structure metrics are not direct measurements of human
maintainability. Implication: compare actual implementation and follow-up changes,
not only review answers, and do not claim that this revision solves long-term drift.

**R12. [EvalPlus: Is Your Code Generated by ChatGPT Really Correct? Rigorous
Evaluation of Large Language Models for Code
Generation](https://arxiv.org/abs/2305.01210), NeurIPS 2023.**
Stronger test inputs exposed incorrect solutions accepted by smaller suites.
Implication: meaningful behavioral coverage matters more than a green result
alone. This does not require a universal test quota, broad matrix or benchmark
suite for every project edit.

**R13. [Beyond Functional Correctness: Investigating Coding Style Inconsistencies
in Large Language Models](https://doi.org/10.1145/3715749), FSE 2025.**
In its prompt experiment, DeepSeekCoder-6.7B generated ten samples for each of
20 selected tasks. Baseline correctness was 67.0%, versus 57.5%, 68.5%, 37.5%
and 39.0% for four style-guided prompts. The detailed prompts combined
readability, conciseness and robustness. This is neither an isolated test of
human understandability nor proof that every readability instruction harms
current frontier models. Together with R1 it motivates testing concrete rules
instead of assuming a broad quality slogan works.

## Disposition of the existing Skill

| Area | Final decision and basis |
| --- | --- |
| Activation, authority, role boundaries and canonical owners | Retain. These define permission and ownership, not measured optimization claims. |
| Advise/Explore/Develop/Harden | Retain as descriptions of requested outcomes. No risk label selects broader work. |
| Reference routing | Replace special risk overrides and detailed classification routes with current-operation routing. R8 motivates testing reduced induced work, not an assumed accuracy gain. |
| Normal/Structural/High taxonomy | Remove. Name the actual failure and affected boundary instead. No evidence for the exact classification machinery was found. |
| Cache approval | Remove the cache-specific approval gate. Assess actual benefit and validity; ordinary material-choice rules still govern real behavior/cost decisions. |
| Direct processing and runtime costs | Strengthen the existing direct-processing criterion, retain targeted checks and allow useful recursion or multiple passes. R2. |
| Compatibility | Require an existing requirement or evidenced affected use. Clarify a real unresolved break; do not invent support or re-ask an authorized change. User intent, indirectly supported by R5/R6. |
| Safeguards, boundary validation and integrity | Retain requirement/consequence-based protection. Trust unchanged validated properties, not raw data's annotation. R1 supplies caution, not proof of the exact threshold. |
| Kapselung / encapsulation | Permit a real responsibility or state boundary with one consumer. Remove the blanket second-consumer rule. R3/R4 do not support mandatory fragmentation. |
| 2,000-line ceiling and special layout prescriptions in Change | Remove the ceiling and mandatory subsystem-directory prescriptions. Keep ownership and affected-consumer checks. No exact threshold is established. |
| Greenfield layout and names | Preserve unchanged at the user's explicit clarification. They provide consistent starting structure, with project/toolchain precedence and no empty scaffolding. |
| Review findings | Retain scope/maintenance findings for unnecessary machinery; require its actual burden or consequence. No forced improvements or findings. R7. |
| Validation | Extend independent expected results to all behavior tests. Preserve real-boundary and negative-path evidence, proportionate checks and permission limits. R9/R12. |
| Repair loops | Keep the progress-based stop and, after review correction, the two-unsuccessful-corrections reassessment checkpoint. Fresh output does not reset it. Stop without a supported next approach; preserve host caps and acceptance. The numeric checkpoint rests on user experience, not an optimum established by R10. |
| Planning and records | Retain one owner and behavior-complete outcomes without mandatory plans for small work. No paper proves this exact workflow. |
| Completion | Consolidate duplicated final-inspection steps. Preserve final-tree evidence and truthful reporting. |

## Initial verification and limits

The initial revised core, references and expanded family text were compared
with this source ledger and the pre-edit instructions. That self-check missed
stale evaluation wording and an ambiguous repair-loop exception, addressed in
the correction below. Its claim that all obsolete expectations were removed
was too broad. At that checkpoint, project-conventions.md and
planning-and-decisions.md were byte-identical to that baseline. Subsequent
Handoff-owned changes to Planning are outside this research revision.
Historical changelogs and plans are records, not current instructions.

Three GPT-6 Luna Medium consumers used a simple instruction, the prior Skill
and the candidate Skill. Each implemented a field collector, then extended
selection and replaced an explicitly disposable format. Each passed all 22
independent checks across the two steps, used one traversal for selection and
added no legacy decoder, recursion or framework. All preserved required input
validation. These are three small task chains, not 66 distinct project tasks.

A third read-only step assessed real unresolved compatibility, a correct
two-pass implementation, a pointless parse retry and an unsupported symptom
patch. Both Skill versions identified the pointless retry; the simple condition
did not. All accepted the correct two-pass code and recognized the need to
resolve compatibility and investigate the unsupported patch. No candidate
advantage over the prior Skill was demonstrated. The loop scenario tested a
stated next-action decision, not an actual prolonged repair loop. Single-consumer
encapsulation, long-term drift and human maintenance remain unmeasured here.

General standalone, general suite and Codex suite package projections passed
the canonical builder's payload and local-link checks. The generic Skill Creator
validator rejects the pre-existing `compatibility` frontmatter field in both
baseline and candidate. It is therefore not reported as passing. The field was
preserved rather than changing an unrelated format contract to silence the check.
No Claude comparison or full release/publication gate was performed.

The accompanying [verification record](../test-results/2026-10-02-research-revision.json)
records the initial revision hashes, package checks, model outcomes and remaining
limits. The retained evaluation cases describe expectations, not completed tests.
Prior local review comparisons did not establish superiority of the earlier
safeguard revisions. The new small comparison also cannot establish general
superiority, human maintainability, model-family equivalence or an optimal prompt.

For later revisions, keep a real behavioral baseline and compare with a simple
instruction under the same model, effort, tools and input. Exercise both the
failure and a correct counterexample. Include follow-up requirements, existing
data obligations, a necessary guard and an unnecessary mechanism. Derive
acceptance independently of generated code. Record unfavorable results and
costs when measurable. Do not add more Skill machinery solely because a paper
describes a more elaborate workflow.

## Review correction, 2026-10-02

The user authorized the following narrow corrections after an external review:

- Retain the general evidence-based repair stop and restore reassessment after
  two unsuccessful corrections of the same failure or evidenced cause. Different
  inputs, fresh failure output and green existing tests do not reset it. This is
  a practical checkpoint supported by user experience, not a paper-derived limit.
- Remove stale same-check routing language and clarify the data-import case:
  actual responsibility and project conventions matter, not a dedicated folder.
  Align repair cases with the restored checkpoint.
- Replace the residual "High risk" wording with "Risk". Trigger cost analysis
  on plausible material runtime, memory or I/O effects, including fixed-size
  inputs with costly repeated I/O.
- Add a misuse counterexample to single-consumer encapsulation: the real parser
  boundary is useful, but hypothetical registries, strategies and factories are
  not justified. The runtime encapsulation rule remains unchanged.
- Restore validation.md to its original LF line endings. Preserve the
  Greenfield defaults and the existing direct-package identity check.

The [correction verification](../test-results/2026-10-02-review-correction.json)
records scoped source review, package checks and installation comparisons.
The earlier model results above remain historical results for their recorded
instructions. No new model-performance claim or prolonged repair-loop result
is made for this correction. The new and adjusted cases remain evaluation inputs.
