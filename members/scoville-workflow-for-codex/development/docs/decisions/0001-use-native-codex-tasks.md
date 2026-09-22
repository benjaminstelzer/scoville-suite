---
format_version: 1
id: ADR-0001
status: superseded
created: 2026-09-14
accepted: 2026-09-14
scope: project/orchestration
superseded_by: ADR-0007
---

# Use native Codex tasks for the workflow

## Decision

Implement `scoville-workflow-codex` entirely with normal native Codex coordinator, executor, repair, and reviewer tasks. Continue an executor or reviewer with the same task ID after a user decision without counting a repair or archiving it; allow the first attempt plus at most two actual repairs; archive each terminal child task plus the coordinator after the requested Plan completes.

## Problem

The CLI workflow cannot naturally relay and answer intermediate worker questions, while its runner, process, state, installation, and polling layers add behavior and overhead that ordinary manually opened Codex tasks do not have.

## Drivers

- Match the behavior of opening one normal Codex task per Plan unit with a short handoff.
- Preserve the worker's conversation when a required user decision interrupts work.
- Keep the coordinator out of project execution while retaining Plan ownership and a simple reviewed commit.
- Avoid accumulating completed worker and reviewer tasks in the sidebar.
- Minimize narration, repeated context, polling, and coordination tokens.

## Considered alternatives

- Keep the CLI runner and add session resume: preserves CLI isolation but retains transport, lifecycle, runtime, and polling infrastructure.
- Use a hybrid of CLI and native tasks: expands routing and state reconciliation without improving the native path requested here.
- Use only native Codex tasks: provides direct task messaging and archival through existing host controls with the least custom infrastructure.

## Consequences

The Skill depends on native project-task creation, waiting, messaging, and archival controls. Task IDs become the workflow identity; normal project instructions project-relevant personal memory Skills plugins and apps remain available without configuration or packet allowlists; user decisions resume the same conversation; terminal task cleanup is explicit. Host-enforced commentary may still appear but Skill prompts keep it minimal. The separate CLI workflow remains independent and unchanged by this Decision.

## Confirmation

Inspect one explicit bounded fixture containing separate executor and reviewer user decisions. Confirm identical respective task IDs across each decision fresh reviewer identity same saved checkout terminal child archival final coordinator archival sparse transitions and absence of CLI/runtime files.

## Revisit when

Reconsider if native task controls cannot preserve same-checkout execution, same-task continuation, reliable wait results, or verified archival.
