---
format_version: 1
id: ADR-0099
status: accepted
created: 2026-09-27
accepted: 2026-09-27
scope: workflow/dispatch
supersedes: ADR-0093
---

# Review am Ergebnis und schmale Plananpassungen

## Decision

Die am 2026-09-27 beauftragte Umsetzung von PLAN-0018 übernimmt den projektspezifischen Review-Rhythmus. Ohne abweichende Vorgabe erfolgt das unabhängige Review am vollständigen Planpunkt. Steps bleiben geordnet und dürfen wie in ADR-0093 zusammengefasst werden. Nach geprüften Gruppen darf Arbeit weitergehen, während Schlussreview und endgültige Abnahme offen bleiben. Nur abgenommene Änderungen werden committed.

Ein verfügbarer Worker kann verwandte Folgeaufträge oder Korrekturen übernehmen, wenn Modell und Kontext passen. Reviewer bleiben unabhängig. Rollover führt dieselbe Arbeit fort und erhält offene Reviews. Die 40/60-Schwellen aus ADR-0098 bleiben unverändert.

Gestartete Planpunkte dürfen angenommene ADR-Verweise ergänzen und nachweislich rein formale Angaben korrigieren, ohne Ersatzpunkte anzulegen. Alte Entscheidung und Änderungsgrund bleiben nachvollziehbar. Materielle Änderungen benötigen weiterhin ausdrückliche Entscheidung. Evidence hält Ergebnisse und einen genauen Berichtsverweis statt Versuchsprotokollen fest.

## Problem

Ein Review je Dispatch widerspricht dem DIVI-Vertrag und wiederholt Kontext. Unveränderliche ADR-Listen erzeugten Ersatzpunkte; lange Evidence-Listen wiederholen den Ablauf bei jedem Lesen.

## Drivers

- Ausdrücklicher Umsetzungsauftrag für PLAN-0018, beginnend beim DIVI-Projektvertrag.
- Weniger Aufwand bei gleicher Abnahme und nachvollziehbaren Entscheidungen.

## Considered alternatives

- Zusätzlicher Leichtmodus: unnötige Verzweigung im selben Ablauf.
- Prüfungen oder Historie streichen: verliert erforderliche Nachweise.

## Consequences

Review-Grenzen sind von Worker-Grenzen getrennt. Aufgaben können weiterlaufen, ohne fälschlich als abgenommen zu gelten. Keine automatischen Retry-Schleifen und keine parallelen Source-Schreiber. Historische akzeptierte Befunde und frühere ADR-Verweise bleiben erhalten.

## Confirmation

Gezielte SOL-6-Medium-Fälle prüfen geordnete Gruppen, ein Abschlussreview, Korrektur, Rollover und schmale Planänderungen. Astra Medium prüft den finalen Regelstand und Befunde unabhängig.

## Revisit when

Ein Review-Scope verliert unreviewte Änderungen oder eine formale Änderung verändert die fachliche Abnahme.
