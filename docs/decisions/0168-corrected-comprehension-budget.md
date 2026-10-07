---
format_version: 1
id: ADR-0168
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/evaluation
supersedes: ADR-0167
---

# 200 zusätzliche Läufe zur Fehlerkorrektur

## Decision

Der Nutzer erlaubt bis zu 200 weitere Testversuche zur Fehlerkorrektur und
deren Prüfung. Beim Beschluss sind 391 Versuche erfasst: 294 Suite und 97
Workflow. Die neue Gesamtgrenze beträgt 591. Die 200 Plätze sind gemeinsam
für beide Bereiche verfügbar. Die bisherigen Restplätze werden nicht zusätzlich
aufgeschlagen. Alle bisherigen Versuche bleiben im selben Register erhalten.

Die vollständigen Workflow-Funktionstests mit 15/15-Prozent-Schwellen und
ihre Nachweisanforderungen aus ADR-0167 bleiben bestehen. Luna/high und
gesammelte Sol-6.1-high-Gruppenreviews bleiben unverändert.

## Problem

Die bisherigen Grenzen ließen notwendige Korrekturen und deren erneute
Modellprüfung offen. Tests sollen Fehler finden und ihre Behebung belegen.

## Drivers

Nutzer: „Das Budget kann auf 200 Nachläufer angehoben werden um Fehler zu
korrigieren“. Diese Präzisierung begrenzt das unmittelbar zuvor verlangte
Ignorieren des alten Budgets.

## Considered alternatives

Die zuvor vorgeschlagenen starren Suite-Erhöhungen sind nicht gewählt.
Unbegrenzte Wiederholungen entsprechen nicht der jüngsten Präzisierung.

## Consequences

Kontrollen, Transportfehler und Wiederholungen zählen mit. Fehler zuerst
diagnostizieren und gezielt beheben, dann betroffene Nachweise erneuern.
Erwartungen, Auswahl und Bestehensregeln werden nicht an Ergebnisse angepasst.
CI-Push richtet sich nach der gesonderten Nutzerfreigabe, nicht nach dem Budget.

## Confirmation

Das gemeinsame Register erhält ADR-0168 und Grenze 591, ohne alte Versuche zu
entfernen. Neue Versuche und vollständige Gruppenurteile werden belegt.

## Revisit when

200 zusätzliche Versuche reichen nicht für die erforderlichen Korrekturen
und deren Nachweise.
