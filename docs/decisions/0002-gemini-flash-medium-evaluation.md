---
format_version: 1
id: ADR-0002
status: superseded
created: 2026-09-21
accepted: 2026-09-21
scope: suite/evaluation-model
superseded_by: ADR-0003
---

# Gemini Flash Medium als Tester

## Decision

Der Nutzer ersetzt den Tester durch `gemini-3.8-flash-medium` mit `medium` über die vorhandene Antigravity-CLI. SOL Medium bleibt Koordinator; der auftraggebende Agent schreibt Soll-Ergebnisse und prüft die Bewertung.

## Problem

Die bisherigen nativen LUNA-Läufe sind nach einem Zwischenablage-Schreibzugriff gestoppt; der Nutzer bevorzugt den bereits verwendeten CLI-Zugang.

## Drivers

- Der Nutzer erwartet eine schnellere und günstigere Testausführung.
- `agy models` listet das exakt gewünschte Modell; `--effort medium` ist verfügbar.

## Considered alternatives

- LUNA über Codex: bisherige Ergebnisse vorhanden; Host-Isolation blieb unbewiesen.
- Gemini über Antigravity: bestehender Transport in `Z:/Projekts/AI/skills/private/gemini-worker`; dessen Implementierungsstarter gewährt zu weitreichende Rechte für theoretische Tests.

## Consequences

- Alle 300 Fälle bleiben erforderlich. Gemini-Ergebnisse werden getrennt von LUNA ausgewiesen; alte Befunde bleiben erhalten.
- Der Wechsel beweist weder geringere Kosten noch ausreichende Isolation. Keine automatische Tool-Freigabe, globalen Änderungen oder simulierten Zustandsänderungen.
- W-014 bleibt historische LUNA-Spezifikation; sein gestarteter Inhalt wird nicht umgeschrieben. Ein Nachfolgepunkt muss die neue Testausführung übernehmen.

## Confirmation

1. Weise CLI-Modell und Effort sowie sichere Ausführungsgrenzen vor dem Test nach.
2. Teste gebaute Pakete mit unveränderten vorab geschriebenen Aufgaben und Soll-Ergebnissen; dokumentiere versionierte Transportänderungen.
3. Bestätige vollständige Fallabdeckung und korrigierte Fehler unabhängig von SOLs Bewertung; keine Veröffentlichung durch diesen Test.

## Revisit when

Das gewählte Modell ist nicht verfügbar oder der Nutzer ändert Tester beziehungsweise Testumfang.
