---
name: scoville-ask-for-codex
description: Ask one or more configured advisers for independent read-only advice or reviews from Codex, through native Codex tasks or Claude CLI. Use when the user requests an ASK consultation, a second opinion, or a review by specified advisers. Ordinary questions to the current assistant do not trigger a consultation.
---

# Scoville Ask for Codex

Collect independent answers in the calling task. A review asks each adviser to
assess the same evidence; a general consultation combines independent answers
into a synthesis. The caller owns any subsequent changes. Advisers never repair
the subject or delegate the consultation.

## Choose the consultation

Infer `review` or `consultation` from the actual question; an explicit mode wins.
“Could this patch lose data?” is a review even without “for review”. If the
intended outcome is ambiguous, clarify before dispatch. Do not ask again when
the request already establishes the mode, advisers or permission.

Resolve settings with `scripts/ask.py`, using explicit request overrides above
applicable project settings, personal `config.json`, then
[config.default.json](config.default.json). Select exactly the requested
advisers, routes, models and efforts. Adviser IDs identify results; optional
display names never change native task titles. Read
[configuration and helper inputs](references/configuration.md) for resolution,
migration or the first helper invocation.

Python 3.11+, the bundled helpers and Codex online are required. Before native
dispatch, `scripts/list_models.py` obtains the current `model/list` catalog.
Validate every requested model and effort against it and the current host's
task-creation capabilities. A catalog entry does not guarantee a successful
task start. Report missing capabilities, invalid settings or helper errors;
never substitute another model, route, subagent or manually built payload.

## Ask and collect

1. Prepare a self-contained question, expected scope, requirements and raw
   evidence. Include paths and working-tree scope only when relevant. Exclude
   the caller's verdict, intermediate reasoning, previous adviser answers,
   unrelated history and secrets from fresh consultations.
2. Resolve the verified calling task ID and its exact current title, plus the
   saved project for native advisers. Never infer identity from title or
   recency. Read [native task operation](references/native.md) for native
   advisers, or [Claude operation](references/claude.md) for CLI advisers.
3. Run `ask.py` operation `prepare` with one unique consultation reference.
   Retain each returned entry and creation-unknown handle before dispatch.
   Invoke each selected adviser only once through its returned arguments or
   request, within the user's existing authorization and the host's rules.
   Advisers can run independently. Do not create a native task where the host
   requires an explicit new-task request that the user has not given.
4. Keep each result bound to adviser ID, consultation reference, scope and
   task/session handle. Wait for actual completion, answer status questions
   briefly and keep waiting. A receipt or partial delivery is not an answer.
   Continue collecting successful advisers after another fails; report that
   failure without an automatic replacement or unchanged retry.
5. Present answers with material evidence and limits. For a consultation,
   synthesize agreement, differences and useful conclusions without inventing
   consensus. No mandatory second exchange round. For reviews, distinguish
   findings from untested concerns and verify findings before authorized fixes.

Retain requested and actually reported model/effort separately; unavailable
telemetry is unknown. Keep successful native adviser tasks open for follow-ups.
Resume exact retained handles with their previous settings unless explicitly
overridden; identify a newly authorized fresh consultation as fresh.

{{ include: family.contract }}
