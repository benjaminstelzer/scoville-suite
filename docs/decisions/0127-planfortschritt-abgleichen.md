---
format_version: 1
id: ADR-0127
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: plan/reconciliation
---

# Planfortschritt auf Korrekturauftrag mit Nachweisen abgleichen

## Decision

Nutzerauftrag: Scoville Plan erhält einen kurzen Ablauf für „Überprüfe und
korrigiere den Plan“. Der Agent prüft Work Items und Steps anhand Evidence und
relevanter Originalnachweise und trägt sicher belegten Fortschritt nach.
Das gilt für alte statuslose Steps und vergessene Updates nach Abbruch oder Fehler.

## Problem

Gespeicherte Statuswerte können hinter tatsächlicher Arbeit zurückbleiben.
Eine optionale Annotation allein korrigiert bestehende Pläne nicht.

## Drivers

- Nachträge anhand beobachteter Tatsachen statt vermutetem Fortschritt.
- Kurze bedingt geladene Anleitung ohne zweiten Fortschrittsspeicher.

## Considered alternatives

- Alte Steps pauschal markieren: erfindet Fortschritt bei unvollständiger Evidence.

## Consequences

Ein reiner Prüfauftrag bleibt lesend; der Korrekturauftrag erlaubt begrenzte
Nachträge. Done eines Work Items braucht vollständige beobachtete Acceptance
und erforderliche Reviews. Teilchecks, Abbruch und Fehler werden nicht als
Gesamtabschluss oder cancelled interpretiert. Historische Abnahme bleibt
historisch; neue Nachweislücken ändern sie nicht automatisch. Unklare Tatsachen
bleiben als Lücken sichtbar. Scope, Reihenfolge, ausdrückliche Stops und
belegte Effekte bleiben erhalten. Plan und Index werden konsistent validiert.

## Confirmation

Isolierte Altpläne, Teilfortschritt, vergessene Updates, Fehler und offene
Nachweise durch den Ablauf sowie echten Validator und Selector prüfen.

## Revisit when

Ein Nachtrag historische Tatsachen oder eine materielle Nutzerentscheidung erfordert.
