# Gemini evaluation

ADR-0002 replaces the subject model, not the 300 authored cases or hidden keys.
SOL Medium coordinates; the author reviews grades. Keep Luna evidence separate.

Use `gemini-3.8-flash-medium` and `--effort medium` through agy with plan mode,
sandbox, stream-json, slash expansion disabled and no permission bypass.
Each case has a fresh conversation and disposable working directory. Do not
attach existing projects. Supply exact text from verified built packages.

Discovery cases receive frontmatter only. Other cases receive core and may
request named packaged references as text; SOL supplies only the requested
allowlisted file from that same package. Such continuation stays in the case's
conversation, supplies no grading feedback and exposes no expected answer.
The tester names hypothetical actions; it does not execute them. No shell,
browser, filesystem, clipboard, provider, delegation or other tool calls.
Record requested reference names so selective routing remains testable.

The supervisor preserves raw streams, aborts on tools/permission events and
verifies process-tree termination. This monitor is not universal isolation;
do not equate an emitted event with pre-execution interception. The observed
permission-denial probe covers one write boundary only.

Before accepting a run, inspect the full stream including trailing events:
one init, consistent conversation identity, complete current turn, one successful
result, no unexpected actions/errors. Native model must match the exact Medium
variant. Record requested effort separately from observed fields; never invent
a missing effort field or backend attestation. Missing evidence stays open.

Freeze package, receipt, case/key and transport hashes before the batch. A pilot
may qualify only its explicitly checked inputs. No automatic retries or silent
substitution. Fix sources, rebuild and rerun affected cases and regressions.
All 300 final cases must pass before publication can be considered separately.
