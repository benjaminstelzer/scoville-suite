# Sources and evaluation

Reviewed 2026-10-28. Keep empirical findings, vendor guidance and local
requirements apart. Record the tested model and host before transferring a
conclusion; a recent publication may test older models. None of these sources
tests this Skillwriter package.

## Vendor guidance

OpenAI and Anthropic publish Skill and prompt guidance as documentation and
engineering posts, not as controlled studies. Treat model-specific advice as
measured on that model and re-check it on others.

**OpenAI**

- [GPT-6 Astra model guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra):
  stronger instruction following and more sensitivity to unclear or conflicting
  guidance, which can make the model pause early. Audit Skills and AGENTS.md,
  state precedence (user request over Skill guidance), set autonomy explicitly,
  define done by the user's goal, keep testing proportionate to the change.
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
  (2026-09-11): overly specific step-by-step recipes now hinder results. Use
  short trigger-specific descriptions and a minimal root document that routes to
  references. Remove blanket pre-reading and self-check rules, review strong
  ask-first language, define completion before starting. Guidance written for
  other models may overconstrain Astra.
- [Build skills (Codex)](https://learn.chatgpt.com/docs/build-skills): one job per
  Skill; description with scope and boundaries, key use case and trigger words
  first in case hosts shorten it; instructions by default, scripts only for
  deterministic behavior or external tooling; test trigger behavior.
- [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)
  (2026-01-22): define observable success, inspect traces and artifacts, test
  explicit, implicit and negative activation.

**Anthropic**

- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices):
  assume the model is capable and add only missing context; match freedom to
  fragility; third-person what-and-when description; `SKILL.md` body under 500
  lines with references one level deep; build evaluations and a no-Skill
  baseline before extensive writing; test with every model you plan to use.
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices):
  explain why a rule exists so the model can generalize; say what to do rather
  than what not to do; examples steer format reliably. Aggressive language such
  as "CRITICAL: You MUST" causes overtriggering on current models; write "Use
  this tool when...".
- [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5):
  effort, not prompt wording, controls thinking; remove "think carefully" lines;
  state the completion condition and name the early stops to avoid and the stops
  you want.
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
  and [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1):
  verification instructions carried over from older prompts cause
  over-verification; clarify complete delivery and scope; avoid unrequested
  additions.

## Empirical research

- [A Framework for Evaluating Agentic Skills at Scale](https://arxiv.org/html/2606.17819)
  (2026-06, KDD workshop; 19 configurations in Claude Code, Codex CLI and
  OpenHands): goal completion was near saturation while instruction following
  varied widely (Opus 4.8: 88.0 with Skill, 59.8 without). Gains were largest for
  Skills encoding concrete workflows, smallest for general principles. Measure
  instruction following separately from success.
- [SkillForgeBench](https://arxiv.org/html/2610.14918v1) (2026-10; 842 tasks, eight
  models in OpenHands): under strict scoring Skills helped stronger models most
  (Opus 4.8 +19.2, Haiku 4.5 +5.8); process rubrics were harder than
  deliverables. The Tessl framework above found smaller models within a family
  often gained more, so test the target models instead of assuming a direction.
- [SLBench](https://arxiv.org/abs/2607.09016) (2026-07; Codex and Claude Code, six
  backbones): about 70% of 5,000 public Skills contain logical relations such as
  preconditions, constraints and fallbacks; violations caused unsafe outcomes in
  up to 70% of cases. Failures came from capability gaps and low-salience Skill
  text. Make conditions and fallbacks visible where they apply.
- [HANDBOOK.md](https://arxiv.org/abs/2607.25398) (2026-07, COLM workshop): on long
  policy-driven tasks the strongest model passed 36.2% under strict grading.
  Agents let plausible in-environment requests override policy, acted against
  checks they had run, lost rule details and reported compliance they had not
  achieved. Inspect actions, not self-reports.
- [SkillsBench 1.1](https://www.skillsbench.ai/blogs/skillsbench-1-1) (2026-06; 87
  tasks, 18 configurations): curated Skills raised mean success, some tasks
  regressed, and self-generated Skills fell below the no-Skill baseline in three
  configurations. Include a no-Skill baseline.
- [SkillRevise, v4](https://arxiv.org/html/2606.01139v4) (EMNLP 2026 Findings):
  execution-based diagnosis and bounded revision beat one-shot generation,
  including GPT-5.5 and Opus 4.7. Repair observed failures; keep acceptance cases
  separate from tuning.
- [SkillAlign](https://arxiv.org/html/2609.07255v1) (EMNLP 2026): presentation
  changed outcomes with content held fixed; compact structured views often
  helped, full text sometimes won. Test selection and presentation, not length
  alone.
- [Skill Following](https://arxiv.org/html/2609.00549v1) (2026-09, preprint):
  comparing different task subsets misstated benefit. Compare the same tasks
  with and without Skills and report actual retrieval.
- [Skill-Use](https://arxiv.org/abs/2608.04828) (2026-08, preprint; eight models,
  two hosts): activation, compliance and boundaries failed separately, and
  results depended on the host.
- [Evaluating AGENTS.md, v3](https://arxiv.org/html/2602.11988v3) (2026-09; GPT-5.2,
  Sonnet 4.5): repository context did not generally improve success and raised
  cost. Test each added requirement.
- [What Keeps Agent Skills from Being Reusable?](https://arxiv.org/html/2608.08453v1)
  (2026-08): routing, content and resource defects are common in 138,133 files.
  Use defect checks as structural diagnostics, not as task-outcome evidence.

## Compare outcomes

Use this protocol when the user requests a comparative evaluation or the work
claims improved effectiveness. Package validation and reading the instructions
do not demonstrate better model performance.

- Select realistic tasks that expose the changed behavior and preserved correct
  work, including writing and rewriting when both apply. Keep development
  examples separate from final acceptance cases; repeat runs when variance
  matters.
- Run the same tasks for the no-Skill or simple-prompt baseline, the previous
  version and the candidate. Keep conditions comparable and change one factor
  where practical. Record confounders and separate transport failures from model
  errors.
- Record model version, host, effort, prompts, Skill versions and tools. Keep
  inputs, traces, outputs and failed runs; handle text encoding explicitly.
- Measure separately: activation (explicit, implicit, negative), required
  procedure, boundaries and permissions, task success. Inspect actual actions and
  artifacts.
- Report rescued failures and new regressions, plus time, tokens or cost where
  available. Distinguish overall results from the subset where the Skill was
  actually loaded.
- Diagnose a concrete failure, repair it narrowly and re-run affected cases
  within the agreed budget. Keep the version the outcomes support. A claim of
  effectiveness on both OpenAI and Anthropic models requires comparable tests on
  both.
