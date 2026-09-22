# Gemini evaluation results

Inputs: gemini-evaluation-manifest.json and gemini-execution.md. Not release approval.

## Current package r2

Inputs: `gemini-evaluation-manifest-r2.json`; discovery transport unchanged.
Author verified all 206 package hashes, receipt hashes and frozen test files.

| Cases | SOL grade | Author review | Evidence |
| --- | --- | --- | --- |
| code-01–05 | pass | confirmed | workspace temp/2026-09-21-suite-gemini-evaluation/code-r2-01/ through code-r2-05/ |
| code-06 | pass | confirmed Core-only | workspace temp/2026-09-21-suite-gemini-evaluation/code-r2-06/ |
| code-07 | pass | confirmed after supervisor correction | workspace temp/2026-09-21-suite-gemini-evaluation/code-r2-07-v2-01/ |
| code-08–12 | pass | confirmed | workspace temp/2026-09-21-suite-gemini-evaluation/code-r2-08/ through code-r2-12/ |
| code-13–14 | pass | confirmed | workspace temp/2026-09-21-suite-gemini-evaluation/code-r2-13/ through code-r2-14/ |
| code-15 | invalid run | confirmed prohibited tool request; permission denied | workspace temp/2026-09-21-suite-gemini-evaluation/code-r2-15/ |

14/300 accepted on r2. The author checked each exact prompt, answer and native
stream: only user-input/agent-response steps, successful completed result,
correct Medium model and request-review mode. Supervisor records stopped job
trees. Case 04 now correctly activates for engineering planning; negative and
opt-out cases remain correct. Reference continuation is qualified below.

Under `gemini-transport-v2.md`, case 06 selected Core-only without requests.
Case 07 requested Change and Validation text correctly. Its second turn kept
conversation identity but the supervisor rejected a DONE `system_message`
metadata event. The raw stream contains no tool payload; the summary's
`tool_steps: 1` conflates an unapproved step with a tool. This is an observed
supervisor classification defect, not evidence of a tester tool call. The
process tree stopped; no completed answer exists for that aborted run.

The corrected supervisor allows only the observed DONE system-message metadata
schema; tools, permissions and unknown schemas still stop the run. Fresh pilot
`code-r2-07-v2-01` completed two turns in conversation
`1afde6d9-0213-4a0f-abb9-76b57d0c5b59`: requested Change and Validation,
received their verified package text (CRLF normalized to LF), then answered correctly. Author reviewed
prompts, answer and both native streams: exact Medium model, same identity,
complete SUCCESS, no tool steps, stopped trees. Together with Core-only case
06 this qualifies v2 reference transport, not general runtime isolation.
Supervisor SHA256: `6986a2bc10e16df167e3a3a826096ae677f433f7b41b31ff345cffe85fab327c`.

Author reviewed 08–10 prompts, answers and native streams. Cases 08–09
distinguish Core-only test classification from the hypothetical implementation's
Change/Validation routes; their Develop/Normal and Structural judgments match
the keys. They requested no reference text, so those cases prove route naming,
not reference loading. Case 10 requested both references, retained High risk
for migration audit and forbade live execution. All completed with the exact
Medium model, no tools or trailing events and stopped process trees.
Cases 11–12 also match the fixed keys: blocked implementation remains Develop,
and centrality alone does not raise risk. Neither claims performed work.
Cases 13–14 preserve evidence limits and fix scope. Author checked both turns,
case text, requested package text, identity and clean completed streams; no
tools or trailing events. Stubbed consumer compatibility remains unverified;
unrelated style cleanup is excluded.

## Execution stopped at code-15

Conversation `04a16fe1-46c0-4551-8c74-c66ef1dfc86f` requested native
`run_command` to enumerate an installed Skill outside the supplied package.
The full stream records ACTIVE then ERROR with permission denied. No execution
of that command is established. The supervisor stopped its job tree; the empty
SUCCESS result does not override the failed current turn. No case answer exists.
Cases 16–25 and Handoff were not started. Do not retry this resource access.

Read-only CLI help exposes plan/sandbox but no tool-disable flag; MCP controls
do not establish removal of native tools. A tool-free transport remains
unverified. Do not continue model runs by merely strengthening the prompt or
loosening the event filter. Preserve the current package and all failed evidence.

## Historical package r1

| Case | SOL grade | Author review | Native model | Evidence |
| --- | --- | --- | --- | --- |
| code-01 | pass | confirmed | gemini-3.8-flash-medium | workspace temp/2026-09-21-suite-gemini-evaluation/code-01/ |
| code-02 | pass | confirmed | gemini-3.8-flash-medium | workspace temp/2026-09-21-suite-gemini-evaluation/code-02/ |
| code-03 | pass | confirmed | gemini-3.8-flash-medium | workspace temp/2026-09-21-suite-gemini-evaluation/code-03/ |
| code-04 | fail | confirmed: engineering planning wrongly excluded | gemini-3.8-flash-medium | workspace temp/2026-09-21-suite-gemini-evaluation/code-04/ |
| code-05 | pass | confirmed | gemini-3.8-flash-medium | workspace temp/2026-09-21-suite-gemini-evaluation/code-05/ |
| code-06 | pass | confirmed: Core-only classification | gemini-3.8-flash-medium | workspace temp/2026-09-21-suite-gemini-evaluation/code-06/ |
| code-07 | semantic pass | pending: no reference continuation exercised | gemini-3.8-flash-medium | workspace temp/2026-09-21-suite-gemini-evaluation/code-07/ |

Author verified exact discovery prompt, answer and complete native stream:
conversation `1a739f88-a22e-41e4-93d1-cfb1b10c798e`, one init, one completed turn,
one SUCCESS result, no tools or permissions requested. Correctly rejects
activation for the conceptual binary-search question. Process cleanup is recorded.

Native model selects the requested Medium variant; argv requests effort medium.
No separate effort field or backend attestation is claimed. Runtime usage:
14,456 input tokens, 235 output tokens, 202 thinking tokens, 14,691 total;
thinking is not added again. Do not infer prices or savings from this sample.

5/300 accepted on the first Gemini package; SOL verdicts are retained in raw summaries. All other Gemini
cases remain unaccepted. Earlier Luna runs do not count toward this matrix.

Author checked cases 02–05 prompts, answers and native stream projections.
All have the correct model, successful completion and no tool steps. Case 04
wrongly treats planning without implementation as out of scope. Canonical Code
description now explicitly includes engineering Plan entries without code
changes. The rebuilt r2 public package is frozen separately in
`gemini-evaluation-manifest-r2.json`; discovery regressions are recorded above.
Initial Code passes do not count as r2 passes.

Author reviewed 06–07 prompts, answers and native stream steps. Both completed
without tool calls. Case 06 correctly needs no references. Case 07 names Change
and Validation but requests no text. Its wrapper forbids performing the
hypothetical work and asks for references only if needed before answering;
this does not alone establish a Skill defect. Same-conversation reference
delivery remains untested and must be qualified separately. Code results must
be repeated against the corrected package; these initial runs remain historical.
