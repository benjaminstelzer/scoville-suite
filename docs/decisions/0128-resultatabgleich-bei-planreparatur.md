---
format_version: 1
id: ADR-0128
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: plan/repair-evidence
---

# Planpunkte und Steps mit ihren Arbeitsresultaten abgleichen

## Decision

Nutzerpräzisierung zu ADR-0127: Die ausgelagerte Planreparatur prüft ganze
Work Items und Steps. Genügt Evidence nicht, prüft der Agent die jeweiligen
Arbeitsresultate gegen die Anforderungen, etwa Code und Tests oder Texte und
Dokumente. Er führt nötige gezielte Checks aus.

## Problem

Nach einem Abbruch können Arbeitsresultate weiter sein als die gespeicherten
Nachweise. Reine Evidence-Auswertung lässt diesen Stand offen.

## Drivers

- Tatsächlichen aufgabenspezifischen Stand rekonstruieren.
- Resultatabgleich nur in der ausdrücklich geladenen Prüfroutine.

## Considered alternatives

- Nur Evidence lesen: übersieht nicht dokumentierte Ergebnisse.

## Consequences

Die Existenz eines Ergebnisses beweist keine vollständige Acceptance oder
erforderliches Review. Fehlende Arbeit und Prüfung werden konkret festgehalten.
Planreparatur bearbeitet Records, nicht die Arbeitsresultate; nötige inhaltliche
Korrekturen bleiben beauftragte Umsetzung. Historische Abnahme, belegte Effekte
und ausdrückliche Stops bleiben erhalten.

## Confirmation

Altpläne mit unvollständiger Evidence und vorhandenen Code- und Textresultaten
prüfen; Teilumsetzung, fehlende Checks und vollständige Nachweise unterscheiden.

## Revisit when

Der Stand ohne materielle Nutzerentscheidung oder Live-Zugriff nicht rekonstruierbar ist.
