# DIVI5: ten completed workflow units

Status: complete read-only analysis; collected 2026-09-21, 20:31–20:56 UTC.
Collection began with G16 active; later live progress does not change selection.
No DIVI5 files, live tasks or installed Skills were changed for this audit.

## Selection

Freeze the chain at G16 coordinator `01a0c591-3027-75b0-9787-ed18fcef6128`,
workflow `01a0c128-2f34-7903-a601-43c6dec5c151`, PLAN-0012. Walk exact
predecessor IDs from incoming rollover messages, then verify accepted-unit
boundaries. The ten units below happen to correspond to G6–G15; this is not an
assumption that every generation completes exactly one unit. Exclude ongoing
G16 W-017/step-4. Earlier attempts belonging to an included unit remain in scope.

| Generation | Accepted unit | Coordinator task ID |
| --- | --- | --- |
| G6 | W-015/step-1 | 01a0c38f-4a13-7a10-a76f-135c840427c7 |
| G7 | W-015/step-2 | 01a0c3b6-7b70-7590-9d18-50e147a71e0d |
| G8 | W-015/step-3 | 01a0c3d1-11a6-7ad2-8f01-dabf6713f211 |
| G9 | W-015/step-4 | 01a0c49d-8bed-7d01-ab6f-419597c5613e |
| G10 | W-016/step-1 | 01a0c4be-f1ad-7873-b97c-1dc99e7466fb |
| G11 | W-016/step-2 | 01a0c4d7-c6d3-7961-834d-e5a7ca714cc0 |
| G12 | W-016/step-3 | 01a0c51f-2dcc-7ae2-9964-079fac25d31e |
| G13 | W-017/step-1 | 01a0c535-8faf-74a2-81d1-b18e5400a74b |
| G14 | W-017/step-2 | 01a0c54c-d2d9-7c20-a63d-8aca539fc910 |
| G15 | W-017/step-3 | 01a0c577-4022-7a73-9148-10cdb9b48d9b |

## Token interpretation

Native `token_count.info.last_token_usage.input_tokens / model_context_window`
is the installed checkpoint's occupancy measure. It measures the latest model
request input, not cumulative work or independently measured host memory.
All ten coordinators ran SOL Medium with windows of 258,400 tokens;
initial inputs are 26,810–26,821
(about 10.4%). The effective installed settings are coordinator 33% (`>=`) and
worker 66% (`>`). Coordinator checks occur after accepted-unit completion and
commit, before selecting the next unit. A peak above 33% during a unit does not
alone establish a missed rollover.

Every recorded boundary check returned `rollover` at threshold 33%. G6–G15
samples were respectively 166,721 / 147,815 / 189,815 / 187,418 / 140,037 /
161,021 / 157,415 / 137,501 / 175,152 / 123,347 input tokens: 47.73–73.46%
of the window. The threshold works as a boundary decision, not a 33% hard cap.

| Coordinator | Peak request input | Peak/window | Cumulative input | Cached subset | Output |
| --- | ---: | ---: | ---: | ---: | ---: |
| G6 | 176,490 | 68.30% | 19,376,908 | 19,028,224 | 42,812 |
| G7 | 154,222 | 59.68% | 12,864,862 | 12,589,440 | 30,054 |
| G8 | 209,417 | 81.04% | 28,960,842 | 27,391,104 | 61,717 |
| G9 | 195,355 | 75.60% | 18,682,592 | 18,298,112 | 44,633 |
| G10 | 150,125 | 58.10% | 11,651,778 | 11,361,280 | 23,660 |
| G11 | 169,622 | 65.64% | 11,292,120 | 10,963,968 | 30,125 |
| G12 | 170,026 | 65.80% | 10,721,832 | 10,395,520 | 29,721 |
| G13 | 145,478 | 56.30% | 9,695,587 | 9,433,600 | 24,045 |
| G14 | 185,688 | 71.86% | 16,751,847 | 16,385,536 | 35,525 |
| G15 | 132,905 | 51.43% | 9,660,499 | 9,405,184 | 25,467 |

Cumulative columns use one final counter snapshot per session, never a sum of
successive cumulative snapshots. Cache is already included in input; reasoning
is included in output. Do not add either subset again or infer monetary cost.
All ten coordinators independently reconcile summed per-response usage, final
thread counters and final token_count counters for input, cache, output and
reasoning output. Record counts equal unique response IDs: G6–G15 respectively
156/115/208/143/100/91/87/86/129/97. No resume turn is counted again through
cumulative snapshots. No compaction event or request-input
drop greater than 5,000 was observed in the ten coordinator sessions; absence
of that signal is not proof about unrecorded host behavior.

Across the selection, coordinators account for 149,658,867 input tokens
(145,251,968 cached; 4,406,899 uncached) and 347,759 output tokens. Children
account for 45,588,018 input (41,938,560 cached; 3,649,458 uncached) and
194,029 output. These are summed processing volumes across distinct sessions,
not retained context or prices. Cache shares are 97.06% and 91.99%. The last
coordinator's peak (51.43%) is below the G8 maximum (81.04%), but the sequence
is not monotonic and work differs: no controlled efficiency improvement is
established. G8 includes failure/reviews/repair; G14 includes interruption.

## Dispatch and rollover sizes

Characters after decoding the host input envelope, not token estimates.
Activation/review range excludes short parking prompts and later follow-up.
Rollover is parking + validation + activation sent to the next generation.

| G | Child activation/review range | Rollover characters | Completed coordinator turn |
| --- | ---: | ---: | --- |
| 6 | 9,987–11,403 | 1,560 | 01a0c392-bfa5-7b12-b480-33ab0ba1279f |
| 7 | 10,078–10,507 | 1,560 | 01a0c3ba-46a3-7463-a353-cb1f23e01e40 |
| 8 | 10,084–11,602 | 1,560 | 01a0c519-e2d6-72e3-93c1-e1ae82cd85d1 |
| 9 | 9,937–10,522 | 1,564 | 01a0c4a3-6e2f-78b0-9402-f017674b8c3d |
| 10 | 28,855–28,855 | 1,568 | 01a0c4c2-a6c0-77f1-b446-d1a012d38cba |
| 11 | 28,999–28,999 | 1,568 | 01a0c51a-2ae0-7a22-8251-fe68755efd75 |
| 12 | 28,877–28,877 | 1,568 | 01a0c525-3ea9-73f3-9ee9-011de9a488e9 |
| 13 | 16,877–16,877 | 1,568 | 01a0c53b-7ef3-7e03-b771-c9dc484bc1f1 |
| 14 | 16,386–16,927 | 1,568 | 01a0c57e-127c-7152-84e6-5e895f9716d8 |
| 15 | 16,841–16,841 | 1,568 | 01a0c57f-4f34-7db2-9b80-178bf2a21785 |

## Measured payloads and findings

G15 to G16 rollover sends 481/715/372 characters for parking/validation/activation:
1,568 total without host envelopes, 1,964 with them. The messages carry identity,
paths, transition/guard state and accepted boundary, not copied work history.
Character counts are not token counts.

G15 executor activation is 16,841 characters: 7,563 of role/delivery contract,
13 for the field marker and 9,265 encoded Plan context. ADR-0020 accounts for
6,170 decoded characters. The context contains only the selected step and no
Plan Evidence. Complete referenced Decisions are required by the current
selector; their size does not authorize dropping binding context.

G10 W-016/step-1 activation is 28,855 decoded characters: 7,555 of contract,
13 for the marker and 21,287 of context. Its two required Decisions contribute
15,830 and 2,202 decoded characters. Only step1 is selected and Plan Evidence
is absent. This explains the larger dispatch without establishing redundant
history. Any future reduction must preserve the Decision contract.

Three identical prompt-builder calls returned exactly the same 16,841-character
output before one child send. Two extra copies add 33,682 output characters.
A further 17,257-character lifecycle wrapper is distinct, not byte-identical.
This is unnecessary coordinator context growth, not an oversized rollover.

G16 validation reads the full operations reference and then ranges after output
truncation. Installed operations.md is 90,867 characters/1,357 lines; the current
suite source is 93,326/1,385. API-projected outputs are capped, so these file sizes
do not establish exact native token contribution. The larger source is not yet
installed: these runs cannot prove the new suite's live behavior.

G15 executor `01a0c583-b8c7-76b0-94db-e97c8660f4a5`, completed work turn
`01a0c587-3dd9-7b60-acd9-4e6011ed430b`, actually ran SOL Medium. Its native
peak was 75,402/258,400 (29.18%); cumulative input 1,362,638, cache 1,263,232,
output 5,778. Its completed result reports no source/critical-document change;
this audit does not independently rerun its plugin rendering checks.

G6 executor `01a0c395-83f6-73e0-bc3d-cf51df97b3f3` peaked at 69.33%, but
its actual checkpoint returned `continue` at 159,302/258,400 (61.65%). Only
three later samples exceed 66%, followed by terminal completion. The contract
checks natural boundaries while material work remains; this peak alone does
not prove a missing handoff.

G8 executor `01a0c3d6-cdc2-7473-8eb1-84b8c7ce2a1e`, work turn
`01a0c3d9-e5eb-77f1-843c-b060f263b5ff`, failed with `server_overloaded`:
"Selected model is at capacity. Please try a different model." Exact host read
confirms `failed`. Native `task_complete` contains that error and no final
message: event-name matching alone would incorrectly count it as successful.

## Child inventory and usage

Native final counters; cache is a subset of input. All recorded windows are
258,400. Terminal result is not inferred from a task_complete event. Roles are
E=executor, V=reviewer, R=repair; suffix numbers identify the role attempt.
Executors/repairs ran SOL Medium except the two G9 parking-only Terra Medium
tasks. Reviewers ran Astra Low except G7 V1 (SOL High) and G8 V3 (Astra Medium).
This is native turn metadata, not merely requested settings.

| G / role | Task ID | Last terminal turn ID | Result | Peak % | Input / cache / output |
| --- | --- | --- | --- | ---: | --- |
| 6 / E1 | 01a0c395-83f6-73e0-bc3d-cf51df97b3f3 | 01a0c397-f910-7ad0-a310-d8909d23627e | completed | 69.33 | 5,588,529 / 5,275,776 / 26,560 |
| 6 / V1 | 01a0c3a6-827a-7682-bd1d-b36bb94b06ef | 01a0c3a6-83a4-7820-93bc-93037b69897a | changes_requested | 26.10 | 660,488 / 567,040 / 2,421 |
| 6 / R1 | 01a0c3a9-c5eb-7591-bbc9-67ee1aeefa19 | 01a0c3ab-1cc4-75c3-8230-4e24c49c4ab2 | completed | 32.92 | 1,632,714 / 1,489,536 / 8,076 |
| 6 / V2 | 01a0c3b2-aa99-7d70-8758-882b7858a799 | 01a0c3b2-abcc-7d32-87ea-57707515f7ff | pass | 18.00 | 313,051 / 259,200 / 1,337 |
| 7 / E1 | 01a0c3bc-806b-7391-80c6-73f447a04e36 | 01a0c3be-5b0d-7341-9d03-995c5cb89a63 | completed | 61.34 | 3,736,936 / 3,441,664 / 12,509 |
| 7 / V1 | 01a0c3c8-b90c-7f32-8242-97c0079513c8 | 01a0c3c8-ba59-7d42-9ac7-300ecf5b43b3 | pass | 38.60 | 1,749,950 / 1,575,168 / 10,119 |
| 8 / E1 | 01a0c3d6-cdc2-7473-8eb1-84b8c7ce2a1e | 01a0c3d9-e5eb-77f1-843c-b060f263b5ff | failed: capacity | 32.42 | 532,472 / 394,368 / 2,782 |
| 8 / E2 | 01a0c3e5-51a8-7e70-ad53-314795a1be71 | 01a0c3e7-7a23-7061-a2ad-536736631cea | completed | 61.53 | 4,389,086 / 4,076,160 / 25,280 |
| 8 / V1 | 01a0c3fa-53e2-73a1-9f9e-a5a1be803249 | 01a0c3fa-5582-7e31-bcf3-00f884076741 | changes_requested | 25.54 | 551,816 / 457,728 / 2,037 |
| 8 / V2 | 01a0c486-ce2b-7442-a7da-8885fa15658c | 01a0c486-cf7f-7ad0-bce1-adc72a7d1e80 | changes_requested | 28.68 | 806,147 / 695,552 / 3,432 |
| 8 / R1 | 01a0c493-57e6-7113-bda3-3d8fdd8ad0e8 | 01a0c495-93c7-7601-b496-ba1287f154e4 | completed | 27.17 | 827,593 / 712,960 / 4,750 |
| 8 / V3 | 01a0c499-2e2d-70c0-bab8-725098dc3704 | 01a0c499-2fe3-7150-80a8-ddf23916dffc | pass | 22.31 | 415,480 / 332,928 / 1,940 |
| 9 / E1 | 01a0c4a6-3258-76e2-bec4-6fb1cdc6edb2 | 01a0c4a6-33fc-7212-ad76-3defb1866d17 | parking only | 10.34 | 26,722 / 2,816 / 77 |
| 9 / E2 | 01a0c4a7-af17-7de1-aa3c-d31bf94686bc | 01a0c4a7-b0b5-7ef3-946e-82b91ea31130 | parking only | 10.34 | 26,718 / 2,816 / 69 |
| 9 / E3 | 01a0c4aa-0769-75d0-b9e6-2fb45628d6a4 | 01a0c4ab-a02d-74d3-a164-deed0df460d0 | completed | 54.60 | 5,953,356 / 5,687,680 / 23,179 |
| 9 / V1 | 01a0c4b9-b045-74d2-b4c7-356fb578d168 | 01a0c4b9-b219-7473-8e7c-3acd1c2747d7 | pass | 24.78 | 580,518 / 491,520 / 1,982 |
| 10 / E1 | 01a0c4c5-b872-7743-b010-6bbc46095d73 | 01a0c4c7-d2d2-7c63-9bad-9948e089c474 | completed | 53.56 | 4,438,304 / 4,181,888 / 14,529 |
| 11 / E1 | 01a0c4e3-c378-72b1-bf4d-0b7133151156 | 01a0c51a-8ae3-75e2-afb6-8b7ac3dce567 | completed | 58.74 | 3,599,638 / 3,285,120 / 10,782 |
| 12 / E1 | 01a0c52a-4bbc-77b2-b639-a400b1a5db24 | 01a0c52d-573c-73a1-9275-2e76e55a74a4 | completed | 20.75 | 479,967 / 397,696 / 2,584 |
| 13 / E1 | 01a0c53f-bb2c-7f31-8388-b505165225ee | 01a0c542-5d7b-7162-ac68-bd657ab366d0 | completed | 47.19 | 1,808,554 / 1,604,096 / 7,489 |
| 14 / E1 | 01a0c556-5394-70d1-a987-1c051b85ae30 | 01a0c55b-15ff-73a2-94cc-3e5d984ffbbe | completed | 57.98 | 5,452,174 / 5,172,864 / 24,079 |
| 14 / V1 | 01a0c570-dbf8-7542-bf3d-626a6dd4e400 | 01a0c570-dd4f-7a90-8df2-adb9d1e4a0cd | pass | 23.58 | 655,167 / 570,752 / 2,238 |
| 15 / E1 | 01a0c583-b8c7-76b0-94db-e97c8660f4a5 | 01a0c587-3dd9-7b60-acd9-4e6011ed430b | completed | 29.18 | 1,362,638 / 1,263,232 / 5,778 |

All 23 child records reconcile unique-response usage with final event counters.
The inventory was checked against coordinator native create_thread completion
records and dispatch identities, not task titles alone. Parking-only tasks count
as overhead, not completed work. Failed attempts retain their usage.

## Recommendations and limits

1. Retain one generated dispatch payload and reuse it unchanged; avoid repeated
   full output from generation and message preparation. Preserve identity and
   schema checks. Quantify tokens only with matched native requests.
2. Split coordinator operation reads by phase, preserving complete required
   rules and clear routing for smaller models. Do not merely truncate rules.
3. If 33% must become a hard ceiling, define a safe in-unit coordinator-transfer
   contract separately. The present accepted-boundary contract cannot guarantee
   it. Do not transfer a live writer or weaken acceptance to meet a percentage.
4. Keep rollout claims separate from source/test claims. G14 needed the user's
   accidentally closed coordinator restored; G8 had proven result-projection
   mismatches. Successful continuation is not proof of unattended stability.

No recommendation is implemented by this read-only Work Item. The ten accepted
boundaries and valid rollovers show continuation in this sample, not universal
stability. Task-list visibility still prevented some predecessor archival;
source recovery and the renamed package are not yet installed in these runs.
No missing count was replaced with zero, and no pricing or token savings are
inferred from character lengths. Final acceptance concerns this audit only.
Temporary extraction/evidence: workspace
`temp/2026-09-21-divi5-ten-runs/`; native logs remain under
`C:/Users/benja/.codex/sessions/` and `archived_sessions/` with exact task IDs above.
