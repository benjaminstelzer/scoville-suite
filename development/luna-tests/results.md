# Luna evaluation results

Frozen inputs: evaluation-manifest.json. This is not release approval.

| Case | SOL grade | Author review | Native model / effort | Evidence |
| --- | --- | --- | --- | --- |
| code-01 | pass | confirmed | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-01/ |
| code-02 | pass | confirmed | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-02/ |
| code-03 | pass | confirmed | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-03/ |
| code-04 | pass | confirmed | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-04/ |
| code-05 | pass | confirmed | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-05/ |
| code-06 | pass | confirmed | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-06/ |
| code-06-v2 | pass | confirmed; same case, not an extra count | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-06-v2/ |
| code-07 | pass | rejected: unnecessary Planning read | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-07/ |
| code-07-v2 | pass | guided pass confirmed; v1 defect remains open | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-07-v2/ |
| code-08 | fail | inconclusive: ambiguous route question | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-08/ |
| code-08-v2 | pass | guided pass confirmed; v1 over-read remains open | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-08-v2/ |
| code-09 | fail | pass: hypothetical check is not actual check selection | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-09/ |
| code-10 | pass | confirmed | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-10/ |
| code-11 | pass | confirmed; metadata-only follow-up | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-11/ |
| code-12 | fail | confirmed: unnecessary reads and Set-Clipboard | gpt-5.6-luna / medium | workspace temp/2026-09-21-suite-luna-evaluation/code-12/ |

9/300 cases accepted. Remaining cases are pending, not passing.
Author inspected the retained prompt, answer, metadata and exact native
session identity/model/effort projection. This pilot proves its discovery
decision only, not general Skill comprehension or live integration behavior.
For code-02–05 the author also checked raw prompts and answers, native task IDs
and model/effort against the frozen criteria. The Code package/test hashes match.
Cases 02–04 correctly activate Code within the hypothetical scope; case 05
honors opt-out. Later cases remain under SOL evaluation.
Case 06 correctly stays Core-only and Normal. The author checked its prompt,
answer and native identity/settings; the recorded tool call reads only runtime
identity and the built core, not references or keys.
See transport-v2.md for the versioned wrapper clarification and required reruns.
Neither code-07 nor code-08 counts as accepted.
Code-08 native tools also read all three references together with the core,
including unnecessary Planning. This separate execution defect is confirmed;
the route-answer ambiguity does not excuse it.
Code-06-v2 preserves Core-only behavior. Native reads and settings are checked.
Transport v2 explicitly directs core-first reading; a pass under that guidance
alone cannot establish that the v1 unnecessary-reference behavior is repaired.
Code-07-v2 reads core, Change and Validation in the correct order, with no
Planning read. It also makes one unnecessary no-op shell call. Its guided pass
is confirmed from native calls/settings and the answer; case acceptance stays
open pending correction or an uncoached resolution of the v1 finding.
Code-08-v2 correctly names Change and Validation; native reads/settings match.
It also makes an unnecessary `Write-Output ready` call. Original over-read
remains unresolved. Source clarification and pending rebuild are recorded in
code-reference-finding.md.

Code-09 author disagrees with SOL's missing-Validation-read failure: the answer
only proposes hypothetical focused compatibility validation, selecting no
concrete check and judging no actual evidence. Core supplies its correct
Structural/routing classification. Transport v2 requires reads needed for the
evaluation answer, not every reference named for later hypothetical work.
Code-10 correctly retains High for a read-only migration audit. The author
checked both prompts, answers and native task identities/settings/tool reads.

Execution stop after code-12: the author verified a native `Set-Clipboard`
call and its output without reported error. This exceeded the simulation
boundary. Clipboard contents were not read or restored. All Luna children are
terminal; code-13 onward has not started. Resume only after tool-level isolation
is established, not merely stronger prompt wording. Existing results remain
historical; no publication approval is implied.
Code-11 retains Develop while stopping edits for the unresolved decision. The
author checked its prompt, answer, reference reads and both native Luna Medium
turns. The second turn retrieves only the omitted task ID; it does not alter
the case answer or expose grading feedback.
