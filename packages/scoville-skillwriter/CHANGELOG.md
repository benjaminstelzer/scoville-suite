# Changelog

## 2026-11-25 - The README no longer states a test result

I took yesterday's sentence out again. The one test showed no difference with and without the Skill, which tells a reader nothing.

## 2026-11-24 - The test result names both models

The README states the test result in one sentence for Claude Opus 5.5 and Sol. On its one task both models did as well without the Skill, and the README says so.

## 2026-11-23 - A shorter README

I rewrote the README. It now says what the Skill does, how to call it, what it needs and where it stops, and leaves out how the suite is built. The Skill itself is unchanged. The requirements name `gpt-6.2-sol` instead of `gpt-6.1-sol`.

## 2026-11-23 - "Preserve the intention" without the repeated list

"Preserve the intention" repeated the list of what a revision preserves from the shared writing rules. It now names only what it adds: the intended outcome, the activation boundaries, and that a preserved property changes only when the user explicitly asks.

## 2026-11-20 - Clearer structure

Reading and regenerating sources have their own section. How to report an evaluation stands once, in the entry point.

## 2026-11-19 - One wording per rule

Sentences that repeated the table or the entry point are removed from the Skill and its evaluation reference.

## 2026-11-19 - Revising an existing Skill

Save the original instructions before a revision. The writing guidance names the target models. The validation section covers the exception for older validators.

## 2026-11-18 - Shorter source check

- Each rule is stated once. The final check asks whether the work does what the Skill requires instead of listing the rules again. Not tested with models yet.

## 2026-11-15 - Rules that contradicted each other

- A field the Agent Skills specification allows, such as `compatibility`, stays when the skill-creator's validator rejects it. This exception now stands where the skill-creator's authority over format validation is stated.
- A rule that holds only until something happens states that end in the rule; the warning against expiring dates no longer covers it.
- A prompt that points to a source still states directly the permissions and stops that govern the recipient's work.
- Shared rules: a reply uses the language of the request, while a record or file you edit keeps the language it is written in. Files saved with `--publish-full` are delivered output, so cleanup leaves them in place. A rule that holds only until something happens states that end in the rule.

## 2026-11-14 - Distinguish execution from task results

- Record the exact Skill revision or hashes and the files actually loaded.
- Separate failed calls, invalid scoring and incomplete runs from task outcomes; evaluate a handoff through the receiver's work as well as the prompt.
- Inspect individual regressions by model and task type even when the average improves. A different artifact needs a concrete defect before it counts as worse.

## 2026-11-14 - Goodhart corrections

- Evaluation: a re-run of the failing case shows only that the repair matches that case; judge the effect on cases the repair was not written against.
- Run a model only when you ask for it or the report claims model behavior, and a comparative evaluation only on request.
- Writing rules: no rule that every rule must be a checkable step, and no list duty as the model example.
- Shared rules: a final report after a small change no longer loads the writing reference, a test runner's console summary is not machine data, and a complete copy of a reference in context counts as read.

## 2026-11-12 - Concrete instructions and release command

- State each rule as a trigger, an action and a result the agent can check itself, and remove statements that reach the same reader twice.
- Reword the shared writing, machine-data, shell and output-delivery rules the same way.

## 2026-11-11 - Size check for placed components and tested models

- Name the tested models and the minimum reasoning effort in the README.

## 2026-11-10 - Leaner instructions and Plan validator fixes

- Add the findings of the Fable 5.2 prompting guide on prohibitions, stop rules and exceptions.
- Correct source descriptions against their pages, name the Tessl study and set the review date to 2026-11-10.

## 2026-10-30 - Shared criteria and focused helper fixes

- Describe the general development cycle and relevant authoring lessons.

## 2026-10-29 - Follow-up corrections

- Keep Skill Creator activation conditional on Skill authoring, scope structural validation to Skill packages and identify current technical tests.

## 2026-10-29

- Simplify the authoring workflow while preserving revision baselines and read-only reviews.
- Integrate instruction and consumer checks into the existing source review.
- Limit Skill Creator to Skill authoring in the default prompt, and keep vendor advice separate from measured evidence.
- Separate technical host requirements from the scoped Codex tests with `gpt-6.1-sol` / `low`; current Claude behavior remains unverified.

## 2026-10-28 - Review corrections

- Load the shared instruction-design criteria for reviews as well as drafting and revision.

## 2026-10-28

- Introduce Scoville Skillwriter as a public standalone Skill and Suite member.
- Bundle the common frontier-model writing rules from their Shared source.
- Preserve conditional evaluation for explicitly required additional target models.
