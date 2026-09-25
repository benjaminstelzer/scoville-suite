---
format_version: 1
id: ADR-0075
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/plan-decisions
---

# Neue Decisions einzeln überführen

## Decision

Neue accept/reject-Übergänge erfolgen einzeln mit anschließender Strukturprüfung. Keine neuen Decision-Batches schreiben. Bestehende transition_batch-Felder und ihre Integritätsprüfungen bleiben erhalten.

## Problem

Batch-Erzeugung belastet die Anleitung für seltene Decision-Übergänge.

## Drivers

- PLAN-0013 beauftragt den Wegfall der Batch-Schreibmechanik ohne Migration.
- Der Nutzer beauftragt diese Richtung in PLAN-0013 und bestätigt dessen Aktivierung.

## Considered alternatives

- Batch-Schreiben behalten: Zusätzliche Koordination mehrerer Übergänge.
- Einzelübergänge: Einfacher Ablauf; kein neues gruppiertes Übergangsprotokoll.

## Consequences

Historische Batch-Lesbarkeit ist weiterhin verbindlich.

## Confirmation

Prüfe negative Batch-Integritätsfälle und tatsächlich neu geschriebene Einzelübergänge.

## Revisit when

Ein beauftragter Prozess benötigt wieder ein gemeinsames Übergangsprotokoll.
