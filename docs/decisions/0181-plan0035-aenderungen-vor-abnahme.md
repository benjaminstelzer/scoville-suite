---
format_version: 1
id: ADR-0181
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/plan0035-execution-order
---

# Änderungen vor der gemeinsamen Consumer-Abnahme

## Decision

Der Nutzer beauftragt die empfohlene Reihenfolge: W-002 mit offenen Nachweisen
pausieren. Zuerst W-003, W-004, W-005, W-008, W-006 und W-016 umsetzen und
je Arbeitspunkt über Ask mit gpt-6.1-sol/high reviewen. Bestätigte Fehler beheben.
Danach W-002 am finalen Stand fortsetzen und W-007 sowie W-009 abnehmen.
Weitere Luna-Modelltests erst nach diesen Änderungen. W-015 bleibt zuletzt.

## Problem

W-002 ist lokal geprüft, benötigt aber native Consumer- und Plattformnachweise.
Zwischenstände würden unnötige Modelltest-Wiederholungen verursachen.

## Drivers

Ausdrückliche Nutzerantwort: „Setze das so um“ auf die Reihenfolgeempfehlung.

## Considered alternatives

W-002 vollständig abnehmen, bevor weitere Änderungen beginnen: nicht gewählt.

## Consequences

Lokale Umsetzung und Review ersetzen keine fehlende Acceptance. Betroffene
Punkte dürfen mit offener späterer Consumer-Abnahme pausiert werden, während
die unabhängigen Änderungen weitergehen. W-002 wird danach fortgesetzt.
Alle Pflichtnachweise und insgesamt höchstens 80 Luna-high-Versuche bleiben
verbindlich. Keine Freigabe für Push, CI, Installation oder Veröffentlichung.
Die Planbearbeitung erfolgt direkt, ohne Workflow-Aktivierung oder -Abbruch.

## Confirmation

Pausen, offene Nachweise und Rückkehr im Plan sichern. Vor W-007 alle
Abhängigkeiten vollständig abnehmen. W-015 erst nach W-007 und W-009.

## Revisit when

Freigaben, Testumgebungen oder Restbudget die gewählte Abnahme verhindern.
