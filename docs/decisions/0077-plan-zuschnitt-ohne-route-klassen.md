---
format_version: 1
id: ADR-0077
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/plan-granularity
---

# Plan beschreibt Zuschnitt ohne Route-Klassen-Kriterien

## Decision

Plan enthält eine kurze Work-Item-/Step-Checkliste ohne Definitionen von ultra_low bis ultra_high. Workflow owns operations-dispatch.md als Besitzer der Route-Kriterien. Bestehende route- und execute-Annotationen bleiben unverändert.

## Problem

Doppelte Route-Kriterien koppeln Plan an Workflow-Dispatch.

## Drivers

- Plan beschreibt Ergebnisgrenzen und konkrete Steps mit erforderlichen Pfaden.
- Der Nutzer beauftragt diese Richtung in PLAN-0013 und bestätigt dessen Aktivierung.

## Considered alternatives

- Kriterien doppelt führen: Wiederholte Pflege mit Driftgefahr.
- Workflow als Besitzer: Plan bleibt auf Zuschnitt begrenzt.

## Consequences

Steps mit deutlich unterschiedlichem Risiko bleiben getrennt.

## Confirmation

Vergleiche operations-dispatch.md mit dem Ausgang und prüfe Annotationserhalt.

## Revisit when

Die Zuständigkeit für Workflow-Routing wird ausdrücklich geändert.
