# Scoville Setup

Save the Scoville settings for your project in one file. Setup shows the effective values and changes only what you ask it to save.

## How it works

- Reads `.scoville/config.json` from the selected project root, with imported Ask and Workflow defaults for missing values.
- Uses the same loader and validation as the consumers before saving requested changes.

## What it enforces

- Saves settings only on explicit request and preserves unrelated values.
- Rejects invalid values before writing.
- Changes configuration between runs, without starting or supervising a workflow.

## What it costs

- Reads the defaults and project configuration and runs local validation. You choose which settings to retain. No model calls are made by the helper.

## How it was developed

- Built from the shared configuration contract introduced for Ask and Workflow.
- Package tests exercise showing settings, explicit changes, invalid inputs and the actual consumers.

- Development links: [Source](https://github.com/benjaminstelzer/scoville-suite-for-codex/tree/main/members/scoville-setup) | [Tests](https://github.com/benjaminstelzer/scoville-suite-for-codex/tree/main/members/scoville-setup/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite-for-codex/blob/main/members/scoville-setup/development/README.md)

## Compatibility

Included only in the Codex Suite. Requires Python 3.11+ and a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0 or newer. Native model availability is checked by Ask or Workflow on use. The local configuration helper starts no host tasks.

## Install

Setup is included with the Codex Suite. It has no standalone distribution.
Install the complete suite from [its own packages](https://github.com/benjaminstelzer/scoville-suite-for-codex/tree/main/packages).
Partial installation is not supported. Every suite member must be installed
and enabled.

## How to use

Ask Scoville Setup to show the settings for this project, or tell it which values to save. You can configure Ask advisers, model and effort, Claude budget, timeout, persistence, customizations and web tools. Workflow supports model/reasoning pairs for each route and the coordinator/worker context rollover percentages.

The helper returns the effective values. A one-time choice remains in the request or Plan Step unless you ask to save it. Setup is included only in the Codex Suite. Ask and Workflow work without running Setup first.

## Sources

- Imported Ask and Workflow defaults and their configuration validators are the settings contract.
- [Scoville Suite source](https://github.com/benjaminstelzer/scoville-suite-for-codex).

## License

MIT. See [LICENSE](LICENSE).
