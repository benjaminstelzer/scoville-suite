---
format_version: 1
id: ADR-0006
status: superseded
created: 2026-09-21
accepted: 2026-09-21
scope: suite/evaluation-coverage
supersedes: ADR-0005
superseded_by: ADR-0007
---

# Ask auf drei Fälle und Design auf Routinen begrenzen

## Decision

Der Nutzer reduziert Ask auf drei Fälle je Templatebasis und Design auf einen Fall je Design-Routine. Code behält 25; die übrigen sieben Sets behalten je zehn Fälle. Die genaue Bedeutung von Design-Routine ist vor dessen Auswahl zu klären.

## Problem

Die unmittelbar vorherige Zehnerregel entspricht nicht mehr der gewünschten Gewichtung von Ask und Design.

## Drivers

- Ask soll nur drei Durchläufe erhalten.
- Design soll je Routine einmal geprüft werden.

## Considered alternatives

- Zehn je Ask-Basis und Design: durch die neue Nutzervorgabe ersetzt.
- Drei je Ask-Basis und routinenbezogene Design-Auswahl: gewählte Begrenzung; Design benötigt eine eindeutige Routinenzuordnung.

## Consequences

- Ask verwendet je Basis die festen Fälle 01, 06 und 25 für Aktivierung, Defaults und komplexen Fehlerfall.
- `development/luna-tests/selected-cases.json` sperrt Design bis zur Klärung: 30 Fachroutinen oder drei Arbeitsmodi.
- Außer Design sind 104 Fälle ausgewählt. Kataloge, Soll-Ergebnisse, Modellwahl und Beleganforderungen bleiben erhalten.

## Confirmation

1. Prüfe je drei Ask-IDs sowie unveränderte Code- und übrige Auswahlen.
2. Kläre Design und erfasse die Zuordnung vor dessen Ausführung.
3. Akzeptiere ausschließlich ausgeführte ausgewählte Fälle mit SOL- und Autorenprüfung.

## Revisit when

Der Nutzer präzisiert Design-Routine oder ändert den Testumfang.
