# Codex CLI comprehension execution

Use this procedure only for theoretical Skill-comprehension checks. It does not
prove that a project action, browser flow or host integration was executed.

1. Build the intended package through `development/build_suite.py` and record
   its receipt and package hashes.
2. Select cases from `selected-cases.json`. Keep the prompts and expected
   results separate. Use a fresh context for every case.
3. Pin the requested model and reasoning effort. Record the host-visible model,
   effort, prompt, package, references and runner identity for every run.
4. Disable project mutation and external actions. Serve only requested package
   text and record transport failures separately from semantic failures.
5. Grade the complete answer against the hidden expected result. A protocol
   pass is not a semantic pass. Retain failed attempts and never repair the key
   to fit an answer.
6. Record a concise result summary in the repository only when it remains useful
   to a current release. Keep prompts, events and full answers in workspace temp.

Any change to tested instructions invalidates the affected result. Rebuild and
repeat only the affected cases and required regressions.
