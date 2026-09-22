# Discovery-only scope v6

Design04 exposed conflicting v3 prompt directions: metadata-only applicability
versus applying the full Skill with READ requests. The runner correctly rejected
the unknown path. Preserve that attempt as protocol FAIL, semantic unassessed;
it does not demonstrate a defect in the unseen Skill core.

For discovery cases only, replace the generic v3 application/READ paragraph:

> Decide only applicability and the owner or next action from the supplied
> discovery metadata. Do not execute the scenario, apply the full workflow,
> or request files. State missing scenario facts as unknown.

Keep exact built frontmatter, original case and discovery question. Do not add
the expected dispatch, owner or artifact. Application cases keep their existing
wrapper and hash-checked READ protocol. The runner and its path rejection stay
unchanged.

Qualify Design04 once before continuing its remaining application cases.
Record prepared-prompt hashes in a supplement to the current package manifest.
Use this separation for later unstarted discovery cases. Earlier accepted
discovery results retain their original wrapper provenance; no blanket rerun.
