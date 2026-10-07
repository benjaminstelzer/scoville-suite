---
format_version: 1
id: ADR-0146
status: superseded
created: 2026-10-04
accepted: 2026-10-04
scope: suite/instruction-quality
superseded_by: ADR-0154
---

# Präzisierungen für den Plan zur Skill-Qualität

## Decision

Der Nutzer beauftragt PLAN-0034 auf Grundlage des geprüften Änderungsprompts und der vorgeschlagenen Präzisierungen: Budget vor Ausführung schätzen; bei uneinheitlichen Ergebnissen beide Versionen auf fünf Gesamtläufe ergänzen; am Endstand alle invalidierten Nachweise erneuern; zulässige gemeinsame Skill-Aktivierung nicht als Verwechslung werten; Zusammenführung erhält Semantik. General umfasst fünf Skills, der Sprachtest benötigt eine ergänzende Sichtprüfung. Beauftragt sind Planerstellung und der vorgesehene unabhängige Review, nicht die Umsetzung.

## Problem

Der Ausgangsprompt ließ die Reihenfolge von Budgetfreigabe und Baseline sowie einige Vergleichs- und Abnahmebedingungen offen.

## Drivers

Erhaltene Intention und Schutzregeln; aussagefähige Vergleiche; ausdrücklicher Stopp vor Umsetzung.

## Considered alternatives

Unveränderte Formulierung: Risiko unklarer Freigaben, ungleicher Laufzahlen und veralteter Nachweise.

## Consequences

PLAN-0034 bleibt draft; die Umsetzung benötigt eine spätere ausdrückliche Freigabe. Ein statistischer Rückgang bleibt bis zur Klärung offen und löst keine automatische Textänderung aus.

## Confirmation

Plan-Review und Strukturprüfung kontrollieren den dokumentierten Vertrag; sie belegen noch keine Skill-Wirkung.

## Revisit when

Der Nutzer Testumfang, Freigabegrenzen oder Abnahmeregeln ändert.

