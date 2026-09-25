---
format_version: 1
id: ADR-0044
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/ui-validation
---

# Kompakte UI-Prüfung innerhalb von 30 Minuten

## Decision

Der Nutzer begrenzt den aktuellen Testauftrag auf maximal 30 Minuten und verlangt geringen Aufwand. Die Ausführung bleibt bei SOL 6 High nach der Astra-Abnahme.

## Problem

Der vorbereitete Vergleich mit 36 Armen würde voraussichtlich mehrere Stunden beanspruchen.

## Drivers

- Zeitgrenze und gezielte Prüfung haben Vorrang vor vollständiger Fallabdeckung.

## Considered alternatives

- Vollständige Matrix: überschreitet den neuen Zeitrahmen.
- Repräsentative Stichprobe: prüft die wichtigsten Wege mit ausdrücklich begrenzter Aussagekraft.

## Consequences

- Zwei vorhandene Classic-/React-Fälle werden mit je drei Vergleichsarmen geprüft, ergänzt um gezielte Routing- und Runtimechecks.
- Nicht ausgeführte Fälle bleiben ungetestet. Der Auftrag verlangt keinen vollständigen 36-Arme-Nachweis und keine Überlegenheitsbehauptung.
- Laufzeitbegrenzungen und fehlende Nachweise werden im Ergebnisbericht benannt. Die Tests enden spätestens um 10:30 UTC am 2026-09-25.

## Confirmation

1. Halte die begrenzte Auswahl vor Ausführung in `development/ui-evaluation.md` fest.
2. Berichte ausgeführte Fälle, Ergebnisse und verbleibende Grenzen innerhalb des Zeitrahmens.

## Revisit when

Ein konkreter Befund verlangt weitere Prüfung und der Nutzer beauftragt diese gesondert.
