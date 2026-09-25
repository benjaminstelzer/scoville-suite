# WordPress SOL results

Tested the frozen `build-r1` package on 2026-09-22. These are theoretical
Skill-comprehension tests, not evidence of WordPress UI execution.

## Frozen evidence

- Model and effort: `gpt-5.6-luna`, `medium`.
- Cases: `62596d0f0d58b4c208554fd882407b142165bca1da6554274d0e20e0a6b365e0`.
- Hidden key: `0ed15e2ca8419e7b5d2d832d00b8047aecdc8280095a9920905c3dc20e14575a`.
- Runner: `4cb9ea0f660c3bfee33f3d555a7549998e78c89a1e8ec2ddad85038488725519`.
- Process-lifetime helper: `be98b0e5590389a96ace79a4dd5572cb36c4c19214371a78628adbe87cca7d32`.
- Build receipt: `6c7b2863c70ec110746fd672efec151f9bcb0797ff1125d565f01c70ed3310ee`.
- Pinned catalog: `0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0`.
- Pinned CLI: `bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226`.

All hashes matched before execution. Each output directory was absent. The
prompts and hidden key remained separate. The five frozen argument arrays were
run once each, sequentially, without substitution or retry.

## Results

| ID | Prompt SHA256 | Turns | Protocol | SOL semantic | Finding |
| --- | --- | ---: | --- | --- | --- |
| `wp-01` | `8933da962a56b5edd7bdbfa03b4c228b3e5cea5bd58a232ecfa950471091f708` | 3 | PASS | PASS | Correct source-only spacing audit, Core ownership, rejection of scale-only, React and authored-WPDS recommendations, and honest rendered limits. The suggested browser check is conditional and later; the answer could have named source inspection more explicitly as the immediate next action, but it does not block the source verdict. |
| `wp-02` | `96543510ca394ccb3c08bb1a4b2717087c03c9329eaad3399975e9aac4958507` | 3 | PASS | PASS | Bounds the fix to the workflow region, preserves Core shell and specialized controls, assigns new gaps to the parent, removes the hidden child from layout, covers accessible recovery/focus, checks the portal at its destination, and separates source, measurement and rendered validation. The extra i18n guidance applies to newly introduced recovery text and does not expand the target surface. |
| `wp-03` | `1cd6ada5585b25d0a1a160d4ae0e7ed74f6f1581ff0821a7adcca9b359e304c6` | 3 | PASS | PASS | Correct Network Admin hybrid ownership, complete plural phrases, one literal domain, JS translation binding, accessible error association, 7.0 fallback and 7.1 loading checks. Correctly excludes catalogs, RTL proof, React migration and a full-suite audit. |
| `wp-04` | `18e6f10ce74ec518e560350708dac8ea455212c2c635f9ba5a46c85e6bcf757c` | 1 | PASS | PASS | Routes A to general UI and B to independent concept work, excludes the WordPress specialist, and does not claim implementation or verification. |
| `wp-05` | `d076c785083ef37b5ca3178b49de6ecd55d3759943a9daa10ca30a99bf2e8fe0` | 1 | PASS | PASS | Excludes the specialist for SlotFill, metabox and theme frontend; assigns each host surface and refuses to prescribe the plugin-page shell or spacing matrix. It does not invent an unsupported supplied-Skill owner. |

Native evidence contains one matching session ID per case and 11 turn contexts,
all `gpt-5.6-luna` with `medium` effort. Every invocation exited zero with empty
stderr, no timeout, cleanup error, stream error, tool action or trailing action.
The only diagnostic was the expressly permitted disabled Code Mode message.
All 19 served-reference records matched the corresponding built-file SHA256.
`wp-04` and `wp-05` were discovery-only and served no references.

Protocol and SOL semantic grades above are independent. The author separately
reviewed all five complete answers, all 11 native contexts and the original
event files, and accepted all five. No result authorizes publication.
