---
format_version: 1
id: ADR-0011
status: accepted
created: 2026-09-24
accepted: 2026-09-24
scope: suite/evaluation-coverage
supersedes: ADR-0008
---

# Jeden Skill mit Luna 6 Medium prüfen

## Decision

Der Nutzer legt fünf verschiedene Fälle je Scoville-Skill und je generiertem Ask-Typ fest: zehn Scoville-Skills und drei Ask-Typen ergeben 65 Fälle. Der Tester ist `gpt-6-luna` mit `medium`; das Modell des koordinierenden Agents ist kein Abnahmekriterium.

## Problem

Das bisherige Release-Gate verlangt eine ältere Fallauswahl und Modelle der 5.6-Generation.

## Drivers

- Jeder Scoville-Skill soll an fünf Aufgaben verständlich sein.
- Bei Ask genügt je ein Vertreter von Single, Paired und Claude-only, weil Varianten dieselbe Vorlage verwenden.
- Der Nutzer verlangt Luna 6 Medium und eine Wiederholung nach belegten Fehlern.

## Considered alternatives

- Bisherige 64 Fälle plus WordPress-Ergänzung: bewahrt alte Belege, bildet aber den neuen Fünfersatz je Typ nicht ab.
- Neuer fester 65-Fall-Satz: deckt jeden verlangten Typ gleichmäßig ab; frühere Ergebnisse bleiben historische Belege.

## Consequences

- `development/luna-tests/selected-cases.json` hält die neuen IDs; Soll-Texte bleiben vom Tester getrennt.
- Ein Fall gilt nur mit nativ bestätigtem Luna-6-Medium-Kontext, passenden endgültigen Paketbytes und inhaltlicher Prüfung. Ein Protokoll-PASS allein genügt nicht.
- Externe Aktionen bleiben simuliert. Ein begrenzter Runner darf harmlose, verifizierte Paket-Helper ausführen und deren tatsächliche Ausgabe zurückgeben; Luna erhält keine nativen Aktionstools.
- Die ältere Auswahl und WordPress-Ergänzung bleiben als Historie erhalten. Dieser Verständnistest beweist keine Live-Integration und ersetzt keine übrigen Release-Prüfungen.

## Confirmation

1. Prüfe 13 Gruppen mit je fünf eindeutigen IDs gegen Korpus und verborgene Soll-Texte.
2. Prüfe pro ausgewähltem Lauf nativen Modell-/Effort-Beleg, Paketgleichheit und inhaltliches Ergebnis; wiederhole Fälle nach Paketänderungen.
3. Validiere beide Suite-Builds und ihre weiteren Release-Gates vor einem Push oder Release.

## Revisit when

Der Nutzer ändert Tester, Umfang oder die erforderliche Ausführungstiefe.
