# W-019 evaluator key

Keep this file from the tester. Grade behavior, not exact wording.

- Completed mismatch: one exact-child read, turnLimit1/includeOutputs false,
  bounded text; require matching task/host/turn/message and full source text.
- Source equals authenticated delivery: recover unchanged bytes automatically,
  retain discrepancy evidence and changes_requested/findings. No user approval,
  punctuation normalization, new review or semantic-equality acceptance.
- Source conflict, truncation or identity mismatch: retain conflict, fail closed;
  no accepted work, extra read/rollout lookup or formatting correction.
- Nonterminal child: same exact-child cursor wait, not source recovery/archive.
- Native wait retains completion/cursor authority. Recovery alone neither
  accepts project work nor bypasses normal status/archival/transition gates.
  Reference consumption follows the existing settled-transition rule.
