---
format_version: 1
id: ADR-0118
status: accepted
created: 2026-09-29
accepted: 2026-09-29
scope: suite/release-gate
---

# Feste CLI-Testreihe als Release-Anforderung entfernen

## Decision

Nutzerauftrag: "die testreihe benötigen wir nicht mehr und sollte als anforderung entfernt werden".
Die feste 45-Fälle-Luna-CLI-Reihe entfällt dauerhaft als Release-Voraussetzung.
Kataloge und bisherige Ergebnisse bleiben als optionale Testmaterialien erhalten.
Änderungsbezogene technische und angeforderte Modell-/Workflowtests bleiben
maßgeblich. Build-, Kompatibilitäts-, Autorisierungs- und Remoteprüfungen bleiben.

## Problem

Die alte Pauschalprüfung blockierte die Veröffentlichung trotz erfolgreicher
gezielter Tests. Die aktuelle CLI fügt Host-Tools in den isolierten Testkontext ein.

## Drivers

- Der Nutzer hat die zusätzliche Testreihe ausdrücklich abgewählt.
- Tatsächliche Tests und Grenzen korrekt dokumentieren, keine fiktiven Passes.

## Considered alternatives

- Nur diesen Release ausnehmen: entspricht nicht der dauerhaften Nutzeranweisung.

## Consequences

Die kanonische Shared-Regel und die Publikationsregeln verwenden den
änderungsbezogenen Prüfumfang. Vorhandene Testergebnisse bleiben Evidenz,
keine neuen Ausführungsfreigaben.

## Confirmation

Aktive Regeln verlangen keine feste Fallzahl, CLI oder Tester-/Koordinator-Kombination.

## Revisit when

Der Nutzer eine neue verbindliche Release-Teststrategie festlegt.
