# Local installation — 2026-09-22

User requested a safe DIVI5 stop, local Skill updates and a new coordinator.
This is local testing, not GitHub publication or release qualification.

- G26 `01a0c6fe-a311-7463-9c51-c52c70ca79fc` stopped after
  `W-020/step-2`, HEAD `ca89ac95ffea0fb1911cde69ef3cd1e14a813040`.
  Guard revision 325 was `rollover_pending`, with no writer or successor.
- Installed builds: workspace `temp/2026-09-22-local-skill-update/{scoville,ask}`.
  Every receipt file hash checked before installation; every installed source
  file hash checked afterwards. All 24 suite/host inventories matched exactly,
  except the intentionally retained personal Ask configuration.
- Codex: 15 Suite Skills plus maintained GitHub and voice Skills (17).
- Claude: nine compatible Scoville Skills plus GitHub and voice (11).
  No Codex-only Workflow or Ask package installed in Claude.
- Removed old discovery names `wordpress-backend-ui` on both hosts and
  `scoville-workflow-codex` on Codex before installing replacements.
  Original directories remain recoverable under workspace
  `state/2026-09-22-local-skill-update/{codex,claude}`.
- Preserved Codex `ask-claude-for-codex/config.json` byte-for-byte.
  Workflow configuration differs only by the requested coordinator title
  migration to `SCW COORD`; model choices and 33/66 thresholds are unchanged.
- Unrelated Skills and host configuration were not changed.

Restart uses the existing `g26-w020-step2-to-g27` transition. The predecessor
must reconcile, transfer and activate it using the installed
`scoville-workflow-for-codex` contract. No direct guard mutation or new acquire.

Restart confirmed: G27 `01a0c725-88d5-70e3-84e7-bdf9632feceb` owns
`coordinator_active` at guard revision 329, with no pending rollover. Its
validation confirmed `W-020/step-3` as the next unit. Predecessor activation
turn `01a0c722-3364-79a0-a43b-77a5aea45ab5` completed successfully.
Archival is successor-owned and is not claimed by this installation record.
