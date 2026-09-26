---
format_version: 1
id: ADR-0086
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/overhead-ausgangsmessung
---

# Reproduzierbare Ausgangswerte statt ungeklärter historischer Zählungen

## Decision

W-001 darf mit der korrigierten reproduzierbaren Ausgangstabelle abgeschlossen werden. Historische Abweichungen werden offen dokumentiert; die alten Nebenwerte müssen nicht exakt rekonstruiert werden.

## Problem

Die Kernwerte stimmen überein, einzelne Nebenwerte haben unklare oder falsch bezeichnete Zählregeln.

## Drivers

- Nutzer bestätigt diese Korrektur ausdrücklich am 2026-09-26.
- Workflow-Umsetzung bleibt Schwerpunkt.

## Considered alternatives

- Alle historischen Werte rekonstruieren: verzögert die Umsetzung ohne geklärte Zähldefinition.

## Consequences

Das explizite Rollout-Manifest und Analyseskript liefern die Vergleichsbasis. W-001 bewahrt seinen gestarteten Auftrag und nennt diese Freigabe in Evidence.

## Confirmation

Ausgangsmessung erneut ausführen und Abweichungen in development/luna-tests/token-overhead-implementation.md behalten.

## Revisit when

Die Auswahl der Vergleichsläufe oder die dokumentierte Zählregel nachweislich falsch ist.
