---
format_version: 1
id: ADR-0179
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/plan0035-execution
---

# PLAN-0035 aktivieren und Sol-6.1-high-Reviews verwenden

## Decision

Der Nutzer aktiviert PLAN-0035 und beauftragt seine Ausführung. Nach jedem
Arbeitspunkt prüft Ask mit gpt-6.1-sol/high. Bestätigte Fehler werden behoben.
Diese Modellwahl ersetzt die Astra-Pflichtreviews des Entwurfs für diesen Plan.
Die verblindeten Sol-Gruppenbewertungen bleiben erhalten. Alle neuen Nachweise
gehören PLAN-0035. Insgesamt höchstens 80 gpt-6-luna/high-Testversuche.
W-015 beginnt zuletzt, erst nach vollständiger Abnahme von W-007 und W-009.

## Problem

Der Entwurf war noch nicht aktiviert und sah Astra-Pflichtreviews vor.

## Drivers

Ausdrücklicher Ausführungsauftrag vom 05.10.2026.

## Considered alternatives

Astra weiter als Pflichtreview verwenden: widerspricht der aktuellen Modellwahl.

## Consequences

Bestehende Freigabegrenzen bleiben verbindlich. Keine automatische Freigabe für
Commit, Push, CI, Installation, native Viewer-Kompilierung oder Veröffentlichung.
Fehlende Pflichtnachweise bleiben offen. Alte Testbudgets werden nicht übernommen.

## Confirmation

Plan aktivieren, Index zuletzt schreiben und das vollständige Profil validieren.
Review-Handles und Ergebnisse je Arbeitspunkt sichern. Luna-Versuche vor Start
im eigenen Register reservieren.

## Revisit when

Der Nutzer Modelle, Umfang, Freigaben oder Testbudget ändert.
