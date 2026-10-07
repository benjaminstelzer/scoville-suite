# Instruction writing

When authoring AI-consumed content, read [the runtime writing rules](prompting/common.md).
This includes AGENTS.md, Skills, plans, references, prompts, schemas, examples,
errors and tool output. The following rules add authoring and packaging guidance.

- Write every shipped Skill file in English, including metadata, assets and
  script messages. Runtime documents and supplied user data follow the user's
  or project's language. English descriptions must still support German requests.
- Begin a Skill description with its capability, then its trigger in English
  user words and a relevant boundary with a neighboring Skill. About 500
  characters is a guide, never an acceptance gate. Keep UI metadata consistent.
- Keep purpose, routing and essential constraints in SKILL.md. Put conditional
  exceptions in references, unless routing or an observed regression requires
  them in the body. State when to read each reference.
- Name the action, exact inputs, result and failure action. Place prerequisites
  before calls and checks after them. Move deterministic payload, ID and branch
  assembly into helpers when this prevents an identified error.
- Check instructions against code and their original intended behavior. For
  changed complex workflows, test realistic use with Luna when authorized.
  Otherwise report comprehension as unverified. Word counts and stronger-model
  review are not Luna proof.

Before publication, apply the [release validation rules](luna-release-gate.md).
