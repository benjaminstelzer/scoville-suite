---
format_version: 1
id: ADR-0180
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/plan0035-evaluation-selection
---

# Neue gezielte Restabnahme innerhalb von achtzig Versuchen

## Decision

Der Nutzer erlaubt für PLAN-0035/W-009 eine neue, vorab begründete gezielte
Auswahl innerhalb des unveränderten Gesamtlimits von 80 Luna-high-Versuchen.
Ausgelassene Fälle bleiben ausdrücklich unverifiziert. Die alten 49 Varianten
werden nicht automatisch als aktuelle vollständige Auswahl übernommen.

## Problem

Die alte Auswahl umfasst 49 Varianten mit 147 initialen Läufen. Änderungen
können alte Nachweise invalidieren. Ihre pauschale Wiederholung passt nicht in
das neue Gesamtbudget, das auch Helper und native Workflow-Proben enthält.

## Drivers

Ausdrückliche Nutzerantwort: „Neue gezielte Auswahl innerhalb von 80 erlauben“.

## Considered alternatives

Bestehende Abnahme beibehalten und offenlassen: vom Nutzer nicht gewählt.

## Consequences

W-009 pinnt seine neue Auswahl und unveränderte Erwartungen vor Ausführung.
Für ausgewählte übertragene Cases bleiben drei bewertbare Läufe, fünf bei
gemischtem Urteil und die übrigen fachlichen Anforderungen erhalten. Keine
Vollmatrix-Abnahme aus der Auswahl ableiten. Alle Versuche einschließlich
Korrekturen bleiben im gemeinsamen neuen Register. Freigabegrenzen und
Windows-, macOS-, Linux- sowie native Desktop-Nachweise bleiben verbindlich.

## Confirmation

Auswahl, Auslassungen, Mindestbedarf und Korrekturreserve vor Modelltests
festhalten. Verblindete Sol-6.1-high-Gruppenbewertung und Reviews je Arbeitspunkt.

## Revisit when

Der ausgewählte Mindestbedarf oder Korrekturen nicht mehr in 80 Versuche passen.
