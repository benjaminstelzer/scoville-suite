---
format_version: 1
id: ADR-0008
status: accepted
created: 2026-09-21
accepted: 2026-09-21
scope: suite/evaluation-coverage
supersedes: ADR-0007
---

# Testumfang auf 64 Fälle begrenzen

## Decision

Der Nutzer begrenzt Code auf maximal 20 Fälle und halbiert die danach ausstehenden 88 Nicht-Code-Fälle auf 44. Insgesamt werden 64 Fälle ausgewählt.

## Problem

Der bisherige Testumfang verbraucht dem Nutzer zu viele Tokens.

## Drivers

- Code bleibt der wichtigste Skill.
- Alle Skills und Ask-Templatebasen bleiben vertreten.

## Considered alternatives

- 113 Fälle behalten: vom Nutzer wegen Tokenverbrauch verworfen.
- Reduzierte Auswahl: weniger Abdeckung bei unveränderten Bewertungsmaßstäben.

## Consequences

- `development/luna-tests/selected-cases.json` enthält 20 Code-Fälle, je fünf für die sieben weiteren Scoville-Sets, je zwei für Design Generate/Critique/Repair und je einen für die drei Ask-Templatebasen.
- Die konkrete Auswahl ist eine Umsetzungsentscheidung: bestehende Grenzfälle und unterschiedliche Aufgabenstufen bleiben erhalten; Ask verwendet je den kombinierten Fall25.
- Frühere Läufe und der vollständige Korpus bleiben erhalten. Gestrichene Fälle werden nicht nachgeholt; notwendige Fehlerregressionen sind keine neuen Fall-IDs.
- Modell, SOL-Koordination, Autorenabnahme, unveränderte Soll-Ergebnisse und Veröffentlichungssperre bleiben bestehen.

## Confirmation

1. Prüfe 20 eindeutige Code-IDs und 44 Nicht-Code-IDs gegen den vorhandenen Korpus.
2. Führe nur ausgewählte Fälle aus und prüfe sie gegen die finalen Paketbytes.
3. Bewahre gestartete W-018-Felder als Historie; dessen Next action nennt diese Korrektur.

## Revisit when

Der Nutzer ändert das Tokenbudget oder den Testumfang.
