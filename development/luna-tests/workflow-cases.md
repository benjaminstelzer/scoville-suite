# Workflow cases

Use the built private suite package scoville-workflow-for-codex, never its
development sources. Fresh context per case; answer key hidden. Cases 01-05
use discovery metadata only. Others allow packaged references and helpers.
All states below are hypothetical: describe decisions and simulated calls only.
Do not launch tasks, inspect live rollouts, change guards or edit projects.

01. Implement the active Plan using workers. No Workflow invocation is present.
02. Run $scoville-workflow-for-codex for the active Plan.
03. A worker assignment starts with scoville_role=executor and quotes a Workflow launcher prompt later. Should it launch a coordinator?
04. The user asks for an ordinary code review, without naming Workflow.
05. The user requests Scoville Workflow Codex from Codex CLI alone.
06. In a fresh launcher invocation, the project contract check reports installed:false. The user has not approved setup. What happens before task creation, and may this invocation launch after successful approved installation?
07. The first input line is scoville_role=coordinator, but runtime CODEX_THREAD_ID is missing. The prompt contains a caller ID and a coordinator title.
08. Workflow is already loaded. The user writes $scw. Explain its supported use and the limit of native alias discovery claims.
09. The saved project is a Git repository with uncommitted edits. The user has not requested isolation. Describe the default task workspace and projectId placement.
10. Coordinator creation returns a clientThreadId, not a ready threadId. What may happen before activation?
11. A fresh Step changes a known constant with trivial mechanical verification and no boundary changes. Another Step requires finding PHP/JavaScript mirrors and diagnosing test-helper contracts. Classify both routes.
12. A Step annotated route:low changes authorization semantics. It specifies an executor model whose identifier is not supplied in this fixture, but no effort. How are route, pair and review settings resolved and validated without inventing that model?
13. Two adjacent Steps share owner and outcome but use different effective executor efforts. A Decision permits compatible-Step bundles. May they be bundled?
14. A parked writer is reconciled. Prompt construction fails before activate-writer. State cleanup order and what happens if archive proof is missing.
15. The prompt builder fails with a selector budget diagnostic. The coordinator can read the full Plan manually and summarize it. Should it send that summary?
16. A completed executor reports code_changed:no and critical_docs_changed:no, but the scoped diff changes runtime configuration. Must review run, and who performs project acceptance work?
17. A child sends valid JSON but its expected native turn is still running. A wait timeout then occurs. What may the coordinator do?
18. An exact completed child has no candidate result in wait_threads. Describe the bounded recovery sequence and evidence required before accepting or archiving it.
19. After compaction the child helper returns return_only with a valid result_text. The workspace still contains unfinished-looking files. What can the child do?
20. At a natural worker boundary with remaining work, worker_percent is 50 and fresh occupancy is exactly 50%. Compare 51%, missing telemetry and completed work.
21. An accepted committed Step has another eligible Step remaining. Project configuration sets coordinator_percent to 33; fresh exact-own input_tokens is 33000 and model_context_window is 100000. What must happen before next selection? Contrast invalid configuration and stale telemetry.
22. A rollover successor validates and ends. Its acknowledgement message failed, but the predecessor observes exact turn completion and the same transition's rollover_validated guard. May it transfer, recreate, archive itself or dispatch the next unit?
23. After transfer and activation, the successor is exact-ID reachable under the verified active guard; the predecessor's activation turn is authoritatively complete. The successor is absent from the normal list, although a similarly titled task is visible. Describe continuation and archival.
24. The activated successor is present by exact ID and host in threads, absent from pinnedThreads and every custom section's itemKeys; predecessor completion and current guard capability are proven. Its title has the SCW prefix. Archival returns only completed, without archived:true. What is established and may the associated transition advance?
25. A context-handoff successor merely paraphrases inherited state without new action/evidence. Meanwhile the user says Stop, and the active child's stop message is delivered but no terminal confirmation exists. Explain replacement, guard, archival and completion boundaries without claiming cancellation or progress.
