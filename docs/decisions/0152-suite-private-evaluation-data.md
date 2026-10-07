---
format_version: 1
id: ADR-0152
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation-data
---

# Dauerhafter Ort deutscher und privater Testdaten

## Decision

Alle Testprojekte, privaten Cases, Testbuilds, Modellläufe und Rohbelege liegen im vorhandenen Codex-Projekt `test` unter `<Desktop>/test/plan0034/`. Bestehende Testdaten bleiben erhalten. Kanonische Regressionstests und portable Testeinstiege bleiben gemäß dessen Projektregeln in ihren Quell-Repositories. Das Suite-Repository enthält Daten-IDs, Hashes und knappe Ergebnisse, keine absoluten lokalen Pfade oder privaten deutschen Testanfragen.

## Problem

development/ wird öffentlich exportiert; private Testdaten brauchen einen getrennten, wiederauffindbaren Ort.

## Drivers

Ausdrückliche Nutzerwahl vom 04.10.2026: Projekt `test` auf dem Desktop. Veröffentlichbare relative development.tests-Pfade bleiben erhalten.

## Considered alternatives

Workspace-Temp oder state/scoville-evaluations wurden zugunsten des vorhandenen Testprojekts verworfen.

## Consequences

Das portable Testinterface meldet fehlende private Daten ausdrücklich als unverifiziert. Eingefrorene Daten erhalten Hashes; geänderte Cases einen neuen Datensatz. Keine Commits, Pushes oder Installation sind damit freigegeben.

## Confirmation

Reproduktion über dokumentierten Datenpfad-Parameter und geprüfte Hashes; Export enthält keine privaten Rohdaten.

## Revisit when

Der Nutzer ein dauerhaftes privates Test-Repository oder Löschung der Nachweise verlangt.

