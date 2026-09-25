---
format_version: 1
id: ADR-0042
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: ask/naming-and-distribution
superseded_by: ADR-0054
---

# Scoville Ask benennen, zuordnen und einzeln anbieten

## Decision

Der Nutzer legt `scoville-ask-for-codex` als Namen des zusammengeführten Skills fest. Er gehört zur Scoville Codex Suite und wird zusätzlich in der allgemeinen Suite-README unter Scoville einzeln installierbar angeboten, mit dem Hinweis „Codex online“. Dies ergänzt ADR-0013 um eine ausdrücklich beauftragte Ausnahme vom ausschließlichen Suite-Angebot für Ask; die Workflow-Distribution bleibt unverändert.

Neue native ASK-Aufgaben heißen exakt `<Titel der aufrufenden Aufgabe> ASK-TASK`, ohne Nummerierung, Modellnamen oder weitere Zusätze. Soweit der Host die Sortierung unterstützt, stehen sie direkt über der aufrufenden Aufgabe.

## Problem

Die bisherige Planung nennt `scoville-ask`, schließt die Einzelinstallation aus und legt die gewünschte Zuordnung in der Sidebar nicht fest.

## Drivers

- Der Auftrag vom 2026-09-25 verlangt erkennbare Zugehörigkeit zur ursprünglichen Aufgabe.
- Die allgemeine README soll auch den einzeln verfügbaren Codex-Skill auffindbar machen.

## Considered alternatives

- Bisheriger Name und ausschließliches Suite-Angebot: entspricht dem bisherigen Plan, erfüllt den neuen Auftrag nicht.
- Neuer Name mit zusätzlicher Einzelinstallation: erfüllt den Auftrag und benötigt getrennte Regeln für Katalogsichtbarkeit und Paketmitgliedschaft.

## Consequences

- Gleichnamige ASK-Aufgaben werden weiterhin über Task-IDs und Handles zugeordnet, niemals allein über ihren Titel.
- Fehlende Sidebar-Sortierung bleibt eine belegte Hostgrenze; sie verhindert den ASK-Aufruf nicht.
- Die allgemeine Suite erhält einen Katalogeintrag, aber kein zusätzliches Laufzeitmitglied.
- Der Entwicklungsstopp und die Reihenfolge aus ADR-0016 bleiben bestehen. Diese Planpflege veröffentlicht oder installiert nichts.

## Confirmation

1. Prüfe exakte Titel und ID-Zuordnung bei einem und mehreren Beratern sowie unterstützte und fehlende Sidebar-Sortierung.
2. Prüfe Codex-Suite-Mitgliedschaft, Ausschluss aus dem allgemeinen Laufzeitpaket und den Einzelinstallationsweg aus dessen README einschließlich „Codex online“.

## Revisit when

Der Codex-Host seine Sortiermöglichkeiten ändert oder der Nutzer Namen, Sichtbarkeit oder Distribution neu festlegt.
