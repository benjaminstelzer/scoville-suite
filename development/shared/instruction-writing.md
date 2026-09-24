# Instruction writing

Keep AI-consumed project content short, precise and free of hidden context.
[prompting/common.md](prompting/common.md) owns shared writing requirements.
Plan writing and additional Workflow instructions use its selected low, medium
or high depth profile. Other instructions remain understandable by Codex Luna. This includes AGENTS.md, Skills, plans, references,
prompts, schemas, examples, errors and tool output.

- Use the shortest wording that preserves the required behavior.
- Name the action, exact inputs, result and failure action. Keep prerequisites
  before the call and checks after it.
- Use one term per concept. Prefer concrete fields and commands over prose.
- State each rule once at its owner. Load only the current operation's contract.
- Move deterministic choices into helpers. Do not make the model reconstruct
  payloads, IDs or branching rules that code can determine.
- Remove repeated rationale, generic warnings and examples that add no necessary
  decision. Never remove authorization, identity checks or recovery conditions
  merely to shorten text.
- Check instructions against code. For changed complex workflows, test realistic
  use with Luna when authorized and available. Otherwise report comprehension
as unverified. Word counts and stronger-model review are not Luna proof.

Before publication, apply [luna-release-gate.md](luna-release-gate.md).
