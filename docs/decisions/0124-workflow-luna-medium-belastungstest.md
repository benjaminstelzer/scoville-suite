---
format_version: 1
id: ADR-0124
status: accepted
created: 2026-09-30
accepted: 2026-09-30
scope: workflow/model-test
---

# Workflow mit Luna Medium und Zwischenfragen testen

## Decision

Der Nutzer beauftragt den vollständigen Test mit Luna 6 Medium für Runner,
Manager, Worker, Korrektur-Worker und Reviewer. „Lina“ wird im Kontext der
vorherigen Modellliste als Luna verstanden. Native Testagenten sind autorisiert.
Simulierte Nutzerfragen zum Stand sollen den Ablauf unterbrechen, ohne ihn
abzubrechen. Ein begonnener Punkt wartet auf eine später implementierte Funktion
und wird nach deren Freigabe ausdrücklich wieder aufgenommen.

## Problem

Die bisherige Abnahme verwendete unterschiedliche Modelle. Sie beweist nicht,
dass Luna Medium bei Zwischenfragen und einer Rückkehr zu pausierter Arbeit
Auftrag, Fortschritt und offene Fragen zuverlässig behält.

## Drivers

- Expliziter Modell-, Test- und Simulationsauftrag.
- Bestehendes Testprojekt und native Agenten statt neuer Chats.
- Keine Anwendung des Workflow-Ausführungsskills durch den aufrufenden Chat.

## Considered alternatives

- Nur technische Tests wiederholen: prüft weder Modellverhalten noch Rückkehr.

## Consequences

Modellpaare und Kontextgrenzen werden nur in isolierten Testprojekten gesetzt.
Alle getesteten Rollen verwenden gpt-6-luna mit medium. Eine interne spätere
Funktion wird als beobachtete Laufblockierung mit autorisiertem Rücksprung
getestet, nicht als ungültige rückwärts gerichtete Depends-on-Kante.
Kontrollierte Fehler und Nachrichten bleiben als Simulation gekennzeichnet.

## Confirmation

Technische Tests wiederholen. Gebaute Aufträge in tatsächlichen nativen Rollen
ausführen. Modell und Effort, Zwischenfragen, Schreibruhe, Review/Korrektur,
Stopp/Wiederaufnahme, direkte Übergaben, Blockierung/Rückkehr, Anzeige und beide
Berichtsabschlüsse anhand tatsächlicher Ereignisse und Dateien abgleichen.

## Revisit when

Ein bestätigter Fehler eine Korrektur oder Wiederholung des betroffenen Falls
erfordert oder Hostzustände keinen belastbaren Nachweis zulassen.
