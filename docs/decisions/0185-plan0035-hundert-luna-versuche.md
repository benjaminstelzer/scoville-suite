---
format_version: 1
id: ADR-0185
status: superseded
created: 2026-10-05
accepted: 2026-10-05
scope: suite/helper-evaluation
supersedes: ADR-0175
superseded_by: ADR-0187
---

# Bis zu hundert Luna-high-Versuche mit Schwerpunkt Workflow und Plan

## Decision

Der Nutzer erweitert bei Bedarf das Gesamtlimit für PLAN-0035 auf 100 gpt-6-luna/high-Versuche. Weniger Luna-Fälle für Ask, mehr für Workflow und Plan; die übrigen Fälle auf Code, UI, Setup, Handoff und Cleanup verteilen. Das Limit ist eine Obergrenze, kein Verbrauchsziel. Bereits verbrauchte acht Versuche bleiben enthalten.

## Problem

Die restlichen Skill-/Workflow-Nachweise und gezielten Korrekturwiederholungen benötigen eine tragfähige Verteilung innerhalb eines ausdrücklich genehmigten Gesamtbudgets.

## Drivers

Nutzer: „Wie können 100 Luna Läufe machen wenn das nötig ist. Weniger für ask, mehr für Workflow und Plan. Der Rest aufgeteilt“.

## Considered alternatives

Beim bisherigen 80er-Limit bleiben: entspricht nicht der neuen Nutzerentscheidung.

## Consequences

Dasselbe Register weiterführen, jeden Versuch vor Start reservieren, keine Einträge oder Fehlschläge löschen. Frische Luna-Kinder zählen mit. Sol-Pflichtreviews und andere Modelle sind keine Luna-Versuche. Fachliche Wiederholungsregeln, unveränderte Erwartungen, gezielte Nachtests jedes Fixes und übrige Freigabegrenzen bleiben erhalten. Historische Budgets und Tests werden nicht rückwirkend umgeschrieben.

## Confirmation

Aktive Plan-Grenzen und Register auf 100 aktualisieren; acht vorhandene Einträge unverändert erhalten. Gemeinsamen CLI-/Native-Registerzugriff und harten Stopp bei 100 gezielt prüfen. Konkrete Auswahl und Rollenbedarf vor W-009-Modellstarts festlegen, Auslassungen unverifiziert ausweisen.

## Revisit when

Auswahl, gemischte Urteile oder Korrekturen voraussichtlich mehr als 100 Versuche erfordern.
