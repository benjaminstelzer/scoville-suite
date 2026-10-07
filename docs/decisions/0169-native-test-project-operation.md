---
format_version: 1
id: ADR-0169
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/evaluation
---

# Native Workflow-Tests im Testprojekt bedienen

## Decision

Die erneute Nutzerfreigabe zur vollständigen Bedienung des Testprojekts erlaubt
native Test-Chats und deren interne Koordination. Die Workflow-Funktionstests
laufen mit angewiesenen Dateigrenzen und nachträglicher Prüfung der beobachteten
Zugriffe. Technische Dateisystemisolation wird dadurch nicht nachgewiesen.

## Problem

Der Desktop bietet den nativen Workflow-Verbraucher, aber keine hier
qualifizierte Dateisystemisolation. Die Methodenfrage hielt weitere Läufe an.

## Drivers

Der Nutzer: „Du darfst das Test Projekt vollständig bedienen mit allen
erlaubnissen die du brauchst“. Vollständige Workflow-Tests und 15/15-Prozent-
Schwellen sind bereits beauftragt.

## Considered alternatives

Auf technische Isolation warten würde die erlaubten nativen Funktionsprüfungen
weiter anhalten. Die gewählte Methode liefert Funktions- und Zugriffsspuren,
aber keinen Nachweis einer technischen Zugriffssperre.

## Consequences

Testdaten und Schreibzugriffe bleiben im Testprojekt. Kandidaten sind nur
lesbar zu verwenden; Bewertungsdaten, echte Projekte und Zugangsdaten bleiben
außerhalb des Testauftrags. Beobachtete Grenzverletzungen bleiben Befunde.
Budgetgrenzen, gesonderte CI-Push-Freigabe und Veröffentlichungsregeln ändern
sich nicht. Andere Testarten erhalten keine pauschale Methodenfreigabe.

## Confirmation

Native Identitäten, tatsächliche Dateiänderungen und verfügbare Zugriffsspuren
pro Fallgruppe bewerten. Fehlende oder verschlüsselte Spuren unverifiziert
lassen. Keine Sicherheits- oder Isolationsabnahme aus Funktionsresultaten ableiten.

## Revisit when

Eine Prüfung technische Isolation voraussetzt oder die beobachteten Zugriffe
keine zuverlässige funktionale Bewertung erlauben.
