---
format_version: 1
id: ADR-0162
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
---

# Opus-Abnahme vor den Modelltests

## Decision

Vor dem ersten Modelltest erhält der Nutzer einen Prompt für ein externes
Opus-5.5-Review der Test-Runner und aller geänderten Skills. Nach der lokalen
Vorbereitung und dem Astra-Review stoppen, bis diese Prüfung und Abnahme vorliegt.
Opus hat direkten Dokumentzugriff und benötigt kein Archiv.

## Problem

Das freigegebene Laufbudget soll erst mit geprüften Runnern und Skills genutzt werden.

## Drivers

Ausdrücklicher Nutzerauftrag vor Beginn der Modelltests.

## Considered alternatives

Sofortige Modelltests würden den gewünschten Review-Zeitpunkt überspringen.

## Consequences

ADR-0161 bleibt als Budgetfreigabe bestehen. Bis zur Opus-Abnahme werden keine
Luna-Testläufe oder Sol-Auswertungen gestartet. Lokale modellfreie Prüfung und
das bereits beauftragte Astra-Review der Änderungen bereiten die Übergabe vor.

## Confirmation

Der Review-Prompt benennt Quellen, Pakete, Ausgangsstand, Runner, Testdaten,
Prüfauftrag und unverifizierte Fähigkeiten ohne versteckten Chat-Kontext.

## Revisit when

Opus Ergebnisse liefert oder der Nutzer die Reihenfolge ändert.
