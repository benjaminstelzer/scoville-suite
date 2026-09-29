---
format_version: 1
id: ADR-0113
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: suite/release-gate
---

# Release-Gate der Claude-Suite mit Sonnet 5

## Decision

Nutzerentscheid: Das Release-Gate der Claude-Suite testet die Claude-Member und die Profilblöcke `claude` per `claude -p` mit Sonnet 5. Gemeinsame Texte deckt weiterhin das bestehende Luna-Gate ab. `../shared/luna-release-gate.md` nennt das Claude-Gate und das dritte Sync-Ziel.

## Problem

Das Luna-Gate testet über die Codex CLI und kennt nur die Sync-Ziele der beiden bestehenden Suiten. Für Ask und Workflow for Claude gibt es keine Fälle.

## Drivers

- Claude-Texte sollen vom Host geprüft werden, der sie ausführt.
- Gemeinsame Texte nicht doppelt prüfen.

## Considered alternatives

- Luna auch für Claude-Texte: prüft Claude-Anweisungen mit dem falschen Host.
- Haiku als Tester: kleinstes Modell, vom Nutzer nicht gewählt.

## Consequences

Ask und Workflow for Claude brauchen eigene Gate-Fälle. Die Helpertests in W-008 laufen mit Sonnet 5.

## Confirmation

W-008 hält die bestandenen Sonnet-5-Fälle mit Transkriptstellen fest.

## Revisit when

Nutzer führen die Claude-Suite überwiegend mit einem kleineren Modell aus.
