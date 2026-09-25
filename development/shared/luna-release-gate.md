# Suite comprehension release gate

Tester selected in Scoville Suite ADR-0003 and ADR-0011: Luna 6 Medium via
Codex CLI. The coordinator's model is not a test acceptance input.

Before publishing either suite or its members:

1. Build release packages only under `E:/Dropbox/AI Projects/skills/temp/release`.
   Keep exactly one current release build. Replace obsolete candidates only
   after their readers finish; never create dated or numbered sibling builds.
   Preserve existing checkouts and changes. Synchronize verified suite exports
   to `skills/public/scoville-suite` and `skills/public/scoville-suite-for-codex`. Workflow uses the suite package
   path, not an individual repository. Until release approval, test its same
   relative path in private staging.
2. ADR-0011 selects five cases for each of six Scoville Skills and one
   representative of each of the three generated Ask types: 45 total.
   Use the fixed IDs in
   Scoville Suite `development/luna-tests/selected-cases.json`, in listed order.
   Preserve the full catalogs and hidden keys. Write expected
   routing, judgments and required behavior before execution. Keep the three
   Ask types separate: single, paired and Claude-only.
3. Run each case using `gpt-6-luna` with `medium` effort. Confirm actual
   model and effort from the native session record. Do not substitute a model
   or claim requested settings prove execution.
4. Each case gets a fresh context, the built package and necessary task inputs.
   Keep expected answers and earlier responses hidden from the tester. Test routing
   with discovery metadata before loading a Skill. For execution cases, allow
   its packaged references and helpers. Never use private development sources.
   Simulate external actions. Do not contact providers or mutate live state.
   The selected model transport is allowed; providers mentioned inside cases
   are simulated. Verify execution restrictions before dispatch; never enable
   automatic tool approval for these tests. Luna uses no native action tools.
   A bounded runner may execute a hash-verified packaged helper with validated,
   harmless inputs and return its actual output in the same case.
   Preserve earlier runs; Gemini results are not Luna passes.
5. Record observed answers and compare them with the fixed expectations.
   Review the answers semantically. Record package hashes, case IDs, model and
   effort, results and gaps. Missing cases or unresolved wrong routing,
   judgments or comprehension block publication.
6. Fix sources, rebuild and rerun affected cases and regressions. Publish only
   the tested bytes. A changed package invalidates affected evidence.

Keep reusable cases and a concise result matrix with the owning suite. Raw
responses and execution traces stay in workspace `temp/`. Theoretical tests
do not prove live integrations. Passing this gate does not authorize publishing.
