# Luna 6 Medium: 65-case comprehension pass

The user selected five cases for each of ten Scoville Skills and one
representative of each of the three generated Ask types (ADR-0011). All 65
selected fresh Codex CLI sessions completed with native `gpt-6-luna` / `medium`
evidence, matched the final package bytes, and passed semantic review against
the hidden case expectations. A protocol pass alone was never counted as a
semantic pass. Earlier failed revisions remain in the task-temp raw evidence.

| Type | Selected IDs | Final result |
| --- | --- | --- |
| Brainstorm | 01, 06, 12, 18, 25 | 5/5 |
| Code | 02, 07, 12, 20, 25 | 5/5 |
| Design | 04, 09, 12, 24, 25 | 5/5 |
| Handoff | 01, 06, 09, 15, 25 | 5/5 |
| Plan | 01, 07, 08, 24, 25 | 5/5 |
| Research | 01, 07, 10, 15, 25 | 5/5 |
| Scribe | 01, 04, 07, 15, 25 | 5/5 |
| UI | 01, 04, 08, 17, 25 | 5/5 |
| Workflow | 02, 11, 12, 20, 21 | 5/5 |
| WordPress UI | 01, 02, 03, 04, 05 | 5/5 |
| Ask single (SOL) | 01, 06, 09, 17, 25 | 5/5 |
| Ask paired (Claude + SOL) | 01, 06, 09, 17, 25 | 5/5 |
| Ask Claude-only | 01, 06, 09, 17, 25 | 5/5 |

The tested Scoville receipt SHA-256 was
`e75150748592be2e444bc9c6413fe23dc462b2806a19bfabd928b5578a3fae9d`;
the Ask receipt SHA-256 was
`b251d96fd1d3906af40aa0bce38cfd1ba1d520b92ea1dcbe49cac742eea01766`.
The exact selected run and per-case package comparison are in workspace
`temp/2026-09-23-luna6-suite-comprehension/final-selection.json`. Raw prompts,
events and answers stay there, outside the repository.

Three Ask `task_title` calls ran through a strict runner allowlist and returned
their actual JSON to Luna. Workflow model-pair helper output was separately
checked against Luna's route decisions. No provider, live task or project
mutation was performed. A tool-enabled CLI pilot could not read the package
because the local execution policy blocked shell commands. These results prove
bounded instruction comprehension, not Desktop task creation or live delivery.

The final fixes clarified Code High-risk planning, Workflow checkpoint
references, Ask title-helper input, Claude configuration-only questions, and
paired delivery status and recovery. Rebuilt packages and affected cases were
retested until no selected semantic failure remained. Scoville's 23 suite
tests, Ask's 8 suite tests and its package tests passed; both final package-set
checks were valid.
