# Instruction writing

When authoring AI-consumed content or public copy, read
[the runtime writing rules](prompting/common.md). AI-consumed content includes
AGENTS.md, Skills, plans, references, prompts, schemas, examples, errors and tool
output. Public copy includes READMEs, CHANGELOGs and release notes.
For reusable instructions and agent-facing prompts, also apply
[agent instruction design](prompting/instruction-design.md); it owns the shared
frontier-model writing and diagram rules. The following guidance adds packaging
and project-specific authoring requirements.

- Write every shipped Skill file in English, including metadata, assets and
  script messages. Runtime documents and supplied user data follow the user's
  or project's language. English descriptions must still support German requests.
- Public copy uses repository-relative paths or placeholders, never author
  usernames, drive letters, local checkout or session paths, or host observations.
  Runtime diagnostics still name the actual paths and conditions needed for repair.
- Begin a Skill description with its capability, then its trigger in English
  user words and a relevant boundary with a neighboring Skill. About 500
  characters is a guide, never an acceptance gate. Keep UI metadata consistent.
- Keep purpose, routing and essential constraints in SKILL.md. Put conditional
  exceptions in references, unless routing or an observed regression requires
  them in the body. State when to read each reference.
- For an operation, state the inputs, preconditions, result and failure action
  that affect correctness or permissions. Keep stable facts and ownership rules
  declarative. Name a concrete observation for required checks. Use a helper for
  deterministic payload, ID or branch assembly when it prevents an identified error.
- Check changed instructions against the owning code or contract and intended
  behavior. Use proportionate checks. Source review and file length do not prove
  model comprehension or improved effectiveness. Apply the
  [release-validation rules](luna-release-gate.md) for model-test settings and
  evidence requirements, and before publication.
