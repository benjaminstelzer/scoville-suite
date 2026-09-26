---
format_version: 1
id: ADR-0083
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/workflow-overhead
---

# Release bis zur Overhead-Korrektur zurückstellen

## Decision

Vor Veröffentlichung werden die Workflow-Regressionen anhand aktueller und archivierter Sessions sowie der Git-Historie untersucht und korrigiert. Worker erhalten nur den exakten zugewiesenen Planpunkt und nötige kurze Zusatzinformation. Der Coordinator delegiert und übernimmt Ergebnisse ohne laufende Überwachung oder wiederholte Statusmeldungen. Rollenbefugnisse und erforderliche Ergebnisprüfung bleiben erhalten.

Alle in der Suite verwendeten Helper-Aufrufe werden gegen ihre tatsächlichen Argumentverträge geprüft. Jeder Helper erhält einen ausgeführten Test mit gpt-6-luna und medium. Die frühere Ausnahme vom allgemeinen 45-Fall-Gate ersetzt diese neue Prüfung nicht.

## Problem

Die aktuelle DIVI-Session lädt Kontext mehrfach und erzeugt vermeidbare Modellaufrufe sowie doppelte Statusmeldungen. Fehlerhafte Helper-Aufrufe erhöhen den Aufwand zusätzlich.

## Drivers

- Explizite Nutzervorgaben zum minimalen Worker-Auftrag und zur Coordinator-Rolle.
- Nutzer verlangt historische Sessionvergleiche und Luna-6-Medium-Tests für jeden Helper.
- Die Suite ist laut Nutzer mit diesem Overhead nicht veröffentlichungsreif.

## Considered alternatives

- Nur Statusmeldungen kürzen: Behebt weder mehrfachen Kontext noch Aufruffehler.
- Unverändert veröffentlichen: Vom Nutzer ausgeschlossen.

## Consequences

W-009 bleibt bis zur Korrektur pausiert. Bereits vorbereitete lokale Kandidaten sind keine Releasefreigabe. Laufende DIVI-Arbeit wird nicht ungefragt verändert oder fortgesetzt.

## Confirmation

Historische Befunde mit Quellenständen verbinden. Finalen Dispatch prüfen und jeden inventarisierten Helper mit Luna 6 Medium testen. Tatsächliche Ausführung von Simulation und reiner Verständnisprüfung unterscheiden.

## Revisit when

Die Befunde behoben und die neuen Prüfungen vollständig dokumentiert sind.
