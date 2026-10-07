---
format_version: 1
id: ADR-0163
status: superseded
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
superseded_by: ADR-0165
---

# Opus-Befunde ohne weitere Review-Runde korrigieren

## Decision

Nach dem externen Opus-v4-Bericht werden bestätigte Befunde lokal korrigiert und
geprüft. Kein weiteres Astra-, Sol- oder Opus-Review dieser Korrekturen starten.

## Problem

Die angekündigte erneute Astra-Nachprüfung ist nicht mehr gewünscht.

## Drivers

Ausdrückliche Nutzeranweisung: „kein weiteres review“.

## Considered alternatives

Die zuvor geplante Astra-Runde widerspricht der aktuellen Anweisung.

## Consequences

Diese Anweisung ersetzt die zusätzliche Review-Pflicht für diese Korrekturrunde.
Lokale Tests bleiben erforderlich. Die offenen Startvoraussetzungen aus Opus v4
und das Budget von 150 Luna-high-Testversuchen bleiben bestehen. Es gibt keine
neue Freigabe für native Proben, CI, Installation oder Veröffentlichung.

## Confirmation

Der Korrekturbericht nennt tatsächliche lokale Nachweise und offene Grenzen,
ohne eine weitere unabhängige Abnahme zu behaupten.

## Revisit when

Der Nutzer ausdrücklich ein weiteres Review beauftragt.
