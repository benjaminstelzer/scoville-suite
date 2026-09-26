# Ask paired expected results

Evaluator-only. Source: built ask-claude-and-sol-for-codex/SKILL.md,
especially Dispatch in parallel, Continue the pair, Optional Claude deadline
and Present the result. Grade decisions, not exact wording or call-name recall.
Difficulty: 01-05 discovery; 06-12 setup; 13-17 delivery/failure;
18-23 continuation; 24-25 combined evidence and authority.

01. Activate Claude+SOL paired Skill; independent read-only consultation.
02. Do not activate paired Skill; SOL-only owner.
03. Generic two-opinion request does not select this Skill. Resolve provider choice.
04. Claude+Astra paired owner, not Claude+SOL substitution.
05. Eligible: consultation is not restricted to code.
06. Fable `claude-fable-5-1`/medium, USD 10 ceiling, persistence enabled and customizations disabled; SOL `gpt-5.6-sol`/high in a fresh normal project task titled `S-ASK GPT-5.6-SOL - Cache review`. The Fable CLI route creates no native task.
07. Explicit choices win independently: SOL medium; Claude opus/max. Do not copy one lane's settings to the other.
08. Prepare one body first. Create SOL without awaiting its answer, then immediately pipe the same body to Claude; SOL additionally receives its fixed role and verified return destination. Retain both handles.
09. Exclude caller draft/analysis and either adviser's answer from the other prompt. Use the prepared question and relevant raw evidence; do not bias the still-running lane.
10. Run independently authorized Claude; report SOL project_task_unavailable. No CLI, subagent, own opinion, API or model substitution for SOL. A Claude answer yields partial, not complete.
11. Never guess the return destination. SOL unavailable; independently authorized Claude may proceed.
12. Retain pending handle and reconcile boundedly. clientThreadId is not a usable threadId. Do not recreate pending creation or block the independent Claude lane.
13. Receipt is not an answer. Preserve Claude's result; SOL delivery unresolved. Use permitted wait/message delivery recovery, never read_thread. Do not claim complete.
14. Sender alone is insufficient. Require matching consultation reference and reviewed scope; do not accept as this review. Seek matching delivery through the retained task.
15. Apply failure archival rule to SOL, retain observed failure, let Claude finish, report applicable configuration change and ask before applying it. No automatic SOL retry or request for approval inside adviser task.
16. Keep successful SOL task unarchived. Completion, silence and delivery are not archive consent; preserve handles/settings for follow-up.
17. Explicit consent authorizes one archive call for that exact task. Report an explicit tool error honestly; no retry, confirmation message, archival check, deletion or replacement chain.
18. Prepare one new follow-up body/reference; same verified return task. Message retained unarchived SOL and immediately resume exact Claude session. Pass each lane's retained model/effort explicitly; do not reset defaults or cross-feed answers.
19. Resume only exact Claude session with retained settings. Do not contact SOL merely because its handle exists.
20. Do not unarchive SOL or replace it and call it continuation. Continue surviving Claude lane; report partial availability.
21. Stop before follow-up dispatch until retained metadata establishes settings or user explicitly chooses new ones. Do not silently reset or omit unknown overrides under the single-template rule.
22. Partial: SOL answer plus Claude timeout/error. No success answer for Claude, automatic retry or budget increase. Retain known session ID without asserting interrupted turn was saved. Direct-child kill is not whole-process-tree or remote-job cancellation proof.
23. Failed: neither returned an answer. Preserve both actual errors; do not retry unchanged authentication/capacity failure or manufacture substitutes.
24. Attribute both answers separately before synthesis and preserve disagreement. Advice grants no authority to edit safeguards or publish; verify consequential claims before an independently authorized action.
25. Neither lane is complete. Preserve SOL's truncated content and use one targeted native status query or `read_thread` call for that known task and only the missing answer/state. Report Claude timeout, retained ID and uncertain interrupted-turn persistence; resume only on explicit follow-up request. Preserve lane-specific settings/errors with no polling, replacement, publication or inferred authority.
