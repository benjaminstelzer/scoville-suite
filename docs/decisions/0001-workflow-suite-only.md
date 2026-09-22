---
format_version: 1
id: ADR-0001
status: accepted
created: 2026-09-21
accepted: 2026-09-21
scope: suite/workflow-distribution
---

# Workflow ausschließlich als Suite-Bestandteil

## Decision

Der Nutzer bestimmt: Scoville Workflow erhält kein eigenständiges Repository. Er bleibt in der Scoville Suite integriert und steht mit einer eigenen Beschreibung ganz oben in deren README.

## Problem

Die bisherige Einzelrepository-Zuordnung bildet die gewünschte Sonderrolle des Workflows nicht ab.

## Drivers

- Der Workflow orchestriert die Zusammenarbeit der Suite-Skills.
- Die Workflow-Beschreibung muss vor den übrigen Skill-Beschreibungen stehen.
- Codex-only-Kompatibilität bleibt erkennbar.

## Considered alternatives

- Eigenes Workflow-Repository: entspricht der bisherigen Zuordnung, widerspricht aber der aktuellen Nutzerentscheidung.
- Ausschließliche Suite-Auslieferung: erhält einen gemeinsamen Veröffentlichungsort, benötigt gesonderte Build- und Testzuordnung.

## Consequences

- Manifest, Links und Veröffentlichungsprüfungen dürfen kein Workflow-Einzelrepository verlangen oder erzeugen.
- Der Workflow-Test prüft den vorgesehenen Suite-Auslieferungspfad statt eines Einzelrepository-Pakets.
- Diese Entscheidung löst keine Veröffentlichung aus und ändert laufende Installationen nicht.

## Confirmation

1. Suite-README zeigt die eigene Workflow-Beschreibung vor den übrigen Mitgliedern.
2. Builds und Veröffentlichungsprüfungen kennen den Workflow nur als Suite-Bestandteil.
3. Luna-Tests verwenden dessen tatsächlichen Suite-Release-Pfad.

## Revisit when

Der Nutzer verlangt ausdrücklich wieder eine eigenständige Workflow-Veröffentlichung.
