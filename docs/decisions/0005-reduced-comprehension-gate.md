---
format_version: 1
id: ADR-0005
status: superseded
created: 2026-09-21
accepted: 2026-09-21
scope: suite/evaluation-coverage
superseded_by: ADR-0006
---

# Code vollständig und übrige Testsets reduziert prüfen

## Decision

Die neue Nutzervorgabe ersetzt die bisherige Fallzahl: Scoville Code behält 25 Fälle; jeder andere Scoville-Skill und jede Ask-Templatebasis erhält 10. Gesamtumfang: 135 Fälle.

## Problem

Der bisherige Umfang von 300 Fällen gewichtet alle Skills gleich, obwohl der Nutzer Code priorisiert.

## Drivers

- Code ist laut Nutzer der wichtigste Skill.
- Die anderen Läufe sollen auf zehn reduziert werden.

## Considered alternatives

- 25 je Set: größere Abdeckung, widerspricht der neuen Vorgabe.
- 25 für Code und 10 je anderem Set: priorisiert Code bei geringerer Breitenabdeckung.

## Consequences

- Die ursprünglichen Kataloge und Soll-Ergebnisse bleiben unverändert erhalten.
- `development/luna-tests/selected-cases.json` legt die zunehmend anspruchsvolle Auswahl vor den übrigen Läufen fest.
- SOL Medium, LUNA Medium, gebaute Pakete und unabhängige Autorenprüfung bleiben gemäß ADR-0003 unverändert.
- Nicht ausgewählte Fälle zählen weder als bestanden noch als fehlend im reduzierten Gate.

## Confirmation

1. Prüfe 25 eindeutige Code-IDs und je zehn vorhandene IDs in den anderen elf Sets.
2. Prüfe alle 135 ausgewählten Fälle gegen unveränderte Soll-Ergebnisse und aktuelle Paket-Hashes.
3. Berichte historische Läufe getrennt vom aktuellen Gate; keine Veröffentlichungsfreigabe ableiten.

## Revisit when

Der Nutzer ändert den Umfang erneut oder ein Fehler verlangt zusätzliche gezielte Regressionen.
