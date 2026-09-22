# Suite comprehension release gate

Tester selected in Scoville Suite ADR-0003: LUNA Medium via Codex CLI.

Before publishing either suite or its members:

1. Build the release packages under `E:/Dropbox/AI Projects/skills/public`.
   Preserve existing checkouts and changes. Workflow uses the suite package
   path, not an individual repository. Until release approval, test its same
   relative path in private staging.
2. ADR-0008 selects at most 20 Code cases and 44 non-Code cases: 64 total.
   Use only the fixed IDs and Design mode groups in
   Scoville Suite `development/luna-tests/selected-cases.json`, in listed order.
   Preserve the full catalogs and hidden keys. Write expected
   routing, judgments and required behavior before execution. Ask needs one
   representative each for single, paired and Claude-only templates.
3. A `gpt-5.6-sol` coordinator with `medium` reasoning runs the cases using
   `gpt-5.6-luna` with `medium` effort. Confirm actual model/effort evidence.
   Do not substitute a model or claim requested settings prove execution.
4. Each case gets a fresh context, the built package and necessary task inputs.
   Keep expected answers and earlier responses hidden from the tester. Test routing
   with discovery metadata before loading a Skill. For execution cases, allow
   its packaged references and helpers. Never use private development sources.
   Simulate external actions. Do not contact providers or mutate live state.
   The selected model transport is allowed; providers mentioned inside cases
   are simulated. Verify execution restrictions before dispatch; never enable
   automatic tool approval for these tests. Require verified tool-free execution.
   Preserve earlier runs; Gemini results are not Luna passes.
5. SOL records observed answers and compares them with the fixed expectations.
   The author reviews the evidence. Record package hashes, case IDs, model and
   effort, results and gaps. Missing cases or unresolved wrong routing,
   judgments or comprehension block publication.
6. Fix sources, rebuild and rerun affected cases and regressions. Publish only
   the tested bytes. A changed package invalidates affected evidence.

Keep reusable cases and a concise result matrix with the owning suite. Raw
responses and execution traces stay in workspace `temp/`. Theoretical tests
do not prove live integrations. Passing this gate does not authorize publishing.
