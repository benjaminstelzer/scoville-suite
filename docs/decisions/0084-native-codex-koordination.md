---
format_version: 1
id: ADR-0084
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/native-codex-koordination
---

# Native Codex-Koordination mit kleinem Wiederaufnahmestand

## Decision

Codex erstellt Tasks und übermittelt Ergebnisse direkt über native Werkzeuge. Der bestehende Laufdatensatz hält nur nötige Fortsetzungsdaten. Gezielte Wiederaufnahmeabfragen sind erlaubt, Polling und zusätzliche Lifecycle- oder Recovery-Schichten entfallen. Ein Builder stellt höchstens den kompakten vollständigen Auftrag zusammen. Erforderliche Ergebnisprüfungen bleiben erhalten.

## Problem

Kommunikationshelper, wiederholte Ausgaben und Kontextladen erhöhen Aufwand und Fehleranfälligkeit.

## Drivers

- Nutzer bestätigt den schlanken Ablauf am 2026-09-26.
- Helper dürfen keine regelmäßige Korrektur ihrer Rückgaben durch den Agenten erfordern.

## Considered alternatives

- Zusätzliche Wrapper und Bestätigungsketten: erhöhen den zu beseitigenden Aufwand.
- Recovery-Abfragen vollständig verbieten: lässt fehlende Zustellungen ungeklärt.

## Consequences

PLAN-0014 konkretisiert die Korrekturen für PLAN-0012 W-017. Reguläre Installation und Veröffentlichung bleiben im bestehenden Releaseablauf. ADR-0083 und seine Helpertests bleiben gültig.

## Confirmation

Kleiner nativer Zustellversuch vor der Umstellung. Isolierten Kandidaten vor Helpertests bauen und installieren. Normalablauf und gezielte Wiederaufnahme tatsächlich prüfen; Coordinator-Aufrufe vergleichbar messen, ohne starre Tokenquote.

## Revisit when

Der Host unterstützt den geprüften Nachrichtenablauf nicht oder ein verbleibender Helper erzeugt mehr Nacharbeit als Nutzen.
