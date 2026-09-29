---
format_version: 1
id: ADR-0108
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: suite/claude-distribution
---

# Namen der Claude-Code-Suite

## Decision

Der Nutzer legt fest: Die Suite des Profils `claude` heißt `scoville-suite-for-claude-code` und liegt im Repository `benjaminstelzer/scoville-suite-for-claude-code`. Der Plugin-Name ist `scoville-suite`. Die neuen Member folgen dem Suffix: `scoville-workflow-for-claude-code` und `scoville-ask-for-claude-code`.

## Problem

ADR-0105 schlug `scoville-suite-for-claude` mit Plugin-Namen `scoville` vor.

## Drivers

- Nutzerentscheidung vom 2026-09-28.
- Der Name nennt den Host, den Workflow und Adviser-Subagenten voraussetzen.

## Considered alternatives

- `scoville-suite-for-claude` mit Plugin `scoville`: kürzer, aber ungenauer Host.

## Consequences

Plugin-Skills heißen `/scoville-suite:<skill>`. Festes Distributionsziel ist `<workspace-root>/skills/public/scoville-suite-for-claude-code/`.

## Confirmation

Build, Plugin-Manifest, Member-Ordner, README-Links und Distributionsziel verwenden diese Namen.

## Revisit when

Claude Code ändert Namensräume oder Namensregeln für Plugins.
