---
format_version: 1
id: ADR-0004
status: accepted
created: 2026-09-21
accepted: 2026-09-21
scope: workflow/result-transport
---

# Reine Darstellungsfehler automatisch behandeln

## Decision

Bei nachweislich reinem Byte-/Projektionsproblem soll der Workflow die Darstellung automatisch korrigieren oder das gültige Ergebnis übernehmen, statt erneut den Nutzer zu fragen.

## Problem

Gemeldete Doppelpunkt-Veränderungen in finalen Host-Projektionen blockieren den Ergebnisvergleich.

## Drivers

- Ausdrückliche Nutzerentscheidung im Ursprungschat 01a0c3d1-11a6-7ad2-8f01-dabf6713f211.
- Originalbelege und fachliche Fehler müssen erhalten bleiben.

## Considered alternatives

- Bei jedem Byteunterschied nachfragen: vom Nutzer für reine Darstellungsfehler abgelehnt.
- Beliebige semantische Ähnlichkeit akzeptieren: belegt weder Originalinhalt noch Identität.
- Nachgewiesene Transportabweichung automatisch behandeln: gewählte Richtung; verlässliche Belegquelle noch zu bestimmen.

## Consequences

- Keine Rückfrage bei bewiesener reiner Darstellungskorrektur innerhalb desselben Ergebnisses.
- Tatsächliche Inhaltskonflikte, fehlende Belege und materielle Prüfbefunde bleiben bestehen; changes_requested wird nicht zu pass.
- Keine Befugnis zu DIVI5-Änderungen oder Eingriffen in laufende Aufgaben.

## Confirmation

1. Vergleiche beide gemeldeten Zustellungen mit verfügbaren unveränderten Originalen und Host-Projektionen.
2. Prüfe automatische Behandlung reiner Darstellung sowie Ablehnung echter Inhaltskonflikte und unbelegter Gleichheit.
3. Baue geänderte Pakete neu und wiederhole betroffene Tests vor Freigabe.

## Revisit when

Die verfügbaren Quellen erlauben keine verlässliche Unterscheidung von Darstellung und Inhalt.
