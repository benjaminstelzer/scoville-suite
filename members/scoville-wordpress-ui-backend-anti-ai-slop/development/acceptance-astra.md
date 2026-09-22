# F01 acceptance deferred

2026-09-11: source changes authorized; acceptance explicitly deferred by the user.
SKILL.md and references/routing.md now require inspecting accessible ownership
evidence before asking. At deferral, no tests, model probes or runtime checks had run.

Pending cases:
- Source identifies PHP/Core: resolve it without a question.
- Relevant runtime remains unknowable: ask one specific question and withhold
  dependent recommendations while continuing independent checks.
- Source-only audit completes without requiring a browser.
- Excluded host surfaces remain excluded; preserve source/measurement/view order.

These are four small new instruction probes, not existing routing fixtures.
Do not resume or mark done the separate USER-DEFERRED-TESTS Work Item W-002.
Identify the actual loaded package/version when observing behavior. Resume these
cases only on user request; record results and limits rather than assuming a pass.

## 2026-09-12 partial acceptance

Three fresh Astra Low supplied-text probes resolved a visible PHP/Core settings
page without a question, asked one renderer question while assessing button
wording independently, and excluded an editor metabox. The source-only response
did not demand a browser and preserved evidence gaps. No actual source read,
runtime or source/measurement/view ordering was tested. Full F01 acceptance
remains open; the separate W-002 was not resumed or changed.
Tested SKILL.md SHA-256:
`e13f0739de4dd1d8fe8afb5dc81336c11e656673c842967bc8921863615becef`.
Cross-Skill method and limits: Scoville Code's
`development/astra-acceptance-2026-09-12.md`.
