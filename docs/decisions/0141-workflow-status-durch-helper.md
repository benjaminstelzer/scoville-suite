---
format_version: 1
id: ADR-0141
status: accepted
created: 2026-10-02
accepted: 2026-10-02
scope: workflow/status-display
---

# Statusmeldungen durch den vorhandenen Helper erzeugen

## Decision

Auf Nutzerauftrag erzeugt run_feedback.py die vollständigen Statusmeldungen.
Die fette Titelzeile nennt Status, Projekt, Plan und Planpunkt/Step. Die Frage
und Erläuterungen darunter sind normal gesetzt. Das ersetzt die zuerst
beauftragte fette Frage. Beispiele: Working on und Decision needed, jeweils
gefolgt von Projekt → PLAN-NNNN → W-NNN/step-N.

Workflow bleibt Codex-only mit verpflichtenden Helpern, ohne Fallback. Der
Runner übernimmt die erzeugte Ausgabe unverändert. Fragen und Blocker behalten
ihre aktuelle Empfängerbindung, Wartebedingungen und unabhängige Weiterleitung.

## Problem

Manuell formatierte Meldungen unterscheiden sich, und Rückfragen ohne Projekt
sind bei mehreren laufenden Workflows schwer zuzuordnen.

## Drivers

- Einheitliche, auffällige Statuszeilen mit vollständiger Zuordnung.
- Weniger Formatierungsregeln und keine Rekonstruktion durch den Runner.

## Considered alternatives

- Formatierungsanweisungen im Runner: wiederholte Modellentscheidung.

## Consequences

Der bestehende Helper liefert Nachricht und Anzeigetext. Das verändert weder
Übernahme noch Fortschrittsfreigabe. Diese Vorschläge aus dem Opus-Review sind
noch keine angenommenen Änderungen. Astra Medium prüft das Review und weitere
sinnvolle Helper zur Kürzung anhand des tatsächlichen Skills.

## Confirmation

Gebautes Paket im tatsächlichen Consumer und seriell im Testprojekt mit Luna
Medium prüfen. Astra-Ergebnis und nicht ausgeführte Fälle getrennt festhalten.

## Revisit when

Weitere sichtbare Workflow-Statusarten eine neue Darstellung benötigen.
