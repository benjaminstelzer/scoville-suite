# Review consumer results - 2026-10-02

The reviewed changes clarify contrast, reflow, task emphasis, measurement
evidence, UI language and WordPress classification. The existing WordPress
version gate remains unchanged. Large-text thresholds now include CSS pixels.

The general standalone UI candidate built and passed package verification.
Local runtime Markdown links passed inspection. Skill Creator's validator
rejects the existing `compatibility` field in both baseline and candidate.
No installation or publication was performed.

## Fresh consumers

Each consumer used GPT-6 Luna at medium effort without inherited history.

| Consumer | Observed result |
| --- | --- |
| `/root/ui_routing_consumer` | Language and source-only limits were correct. Unknown host placement was incorrectly classified as supported. |
| `/root/ui_routing_retest` | After clarifying the existing status mapping, all six targeted fields in both cases were correct. This does not establish minimal or complete prohibition lists. |
| `/root/ui_candidate_consumer` | Desktop and failure/retry worked. Narrow captures clipped, final narrow edits were unverified, and contrast/320px evidence was missing. Failed acceptance. |
| `/root/linden_implementation` | Reused the original repair-shop brief with working Playwright setup. Desktop, long-name detail and failure/retry were observed. Detail reflow measured 320px and 390px with equal document widths. Calculated status-text contrast was 5.08–6.30:1. |

The final Linden run is **not a complete pass**. Independent keyboard inspection
found that queue links remove the outline and indicate focus only through a
background change. Computed colors `#f5f7f1` and `#fffdf7` yield **1.061:1**,
below the applicable 3:1 requirement. The consumer's 6.52:1 focus calculation
covers other controls and does not cover these links. Final 320px queue reflow
and a complete keyboard task were also unverified. The tested app is preserved
without a post-test repair. No extra Skill rule was added for behavior already
required by Validation.

## Evidence and limits

Workspace artifacts are under `temp/2026-10-02-ui-review/`: the baseline,
initial assessment and routing reports, plus `linden-retest/consumer/REPORT.md`
with final images, raw CLI output and input hashes. Independent focus evidence
is in `linden-retest/tooling/queue-focus-review.log` and its screenshot.

The Linden candidate came from dirty source revision
`00bc56b6800aad276950da39cf85c3334172cbd6`. Validation SHA-256:
`e57c2c9ffb2d7558f5af6b13ed2d5d2b98307f0ee6b7233305d7dc061c18d9ef`.
Final app SHA-256:
`a6c9ac1d621b9b7e8ff77db902406c27238ba55e1b635b7e31c9d363c2f15a48`.

There was no matched no-Skill control or Claude implementation run. These are
bounded observations, not evidence of a general reliability improvement or
complete accessibility conformance.

After these runs, Validation was clarified to exercise the affected primary
flow by keyboard with visible focus and check reflow for each affected view.
This small wording change received source and package checks, not a new model
run. The results and hashes above describe the earlier tested candidate.
