---
format_version: 1
id: ADR-0126
status: superseded
created: 2026-10-01
accepted: 2026-10-01
scope: workflow/agent-capacity
superseded_by: ADR-0135
---

# Bestätigte Kapazitäts-Workarounds prüfen und einbauen

## Decision

Der Nutzer beauftragt reale Tests und Integration der recherchierten Workarounds.
Die Übergabe wartet auf Empfang und Vorgängerabschluss. Bei eindeutig abgelehntem
Kapazitätsstart ohne neuen Agenten darf der Runner seine bekannten abgeschlossenen
Manager einmal schreibinaktiv wecken, Nachrichten abarbeiten lassen und nach
bestätigtem Abschluss genau einen erneuten Startversuch erlauben.
Unklare Starts und weiterhin erschöpfte Kapazität bleiben blockiert.

## Problem

Ein abgeschlossener Agent mit wartenden Nachrichten kann einen nativen Platz
belegen. Empfangsbestätigungen nach seinem Abschluss begünstigen diesen Zustand.

## Drivers

- Ausdrücklicher Test- und Integrationsauftrag.
- Beobachteter Kapazitätsfehler im Luna-Lauf bei beendeten Managern.
- Begrenzte Wiederherstellung ohne doppelte Schreiber oder verlorene Übergaben.

## Considered alternatives

- Parallelitätsgrenze erhöhen: behandelt die Nachrichtenfolge nicht.
- Unklare Starts wiederholen: kann doppelte Agenten und Schreiber erzeugen.

## Consequences

Modellpaare, Parallelitätsgrenze und produktive Konfiguration bleiben erhalten.
Der Runner erhält nur Steuerdaten und weckt keine abgeschlossenen Reviewer.
Das bestehende Projekt, der Auftrag und sein Laufbericht bleiben erhalten.
Fehlende Close-Werkzeuge werden weder erfunden noch als getestet ausgegeben.

## Confirmation

Luna-Medium-Test mit tatsächlicher Nachrichtenverarbeitung und anschließendem
nativen Spawn, aktualisierter Übergabe, Negativfällen und vollständigen
technischen sowie Paketprüfungen. Testresultate und Hostgrenzen getrennt festhalten.

## Revisit when

Der Host bestätigt keine eindeutigen Start- oder Abschlusszustände oder bietet
einen überprüfbaren anderen Lebenszyklus an.
