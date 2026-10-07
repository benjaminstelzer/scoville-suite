---
format_version: 1
id: ADR-0172
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/instruction-clarity
---

# Verbleibende dichte Skilltexte vor der erneuten Abnahme klären

## Decision

Die Nutzerfreigabe erweitert den bisherigen W-013-Umfang um Punkte 1–19 des
externen Reviews. W-016 hat Vorrang vor weiteren Modellläufen von W-014.
Danach W-014 an seinem erhaltenen Stand fortsetzen, einschließlich der
beauftragten Runner-Benachrichtigungsprobe.

Textänderungen erhalten Bedeutung, Bedingungen, Ausnahmen, Berechtigungen,
Reihenfolge, technische Literale und Profilblöcke. Zwei funktionale
Abweichungen werden korrigiert: Child-Recovery wartet mit begrenzten Aufrufen
bis Freigabe, STOP oder BLOCKED; neue Create-Dispatches verlangen eine
Auftragsdatei. Recovery-Dispatches behalten ihren bestehenden Kontextweg.

## Problem

Das externe Review zeigt weitere dichte Stellen in Plan, UI, Ask, Setup und
Workflow sowie zwei abweichende Helper- und Recovery-Verträge.

## Drivers

Luna soll die Anweisungen beim ersten Lesen verstehen. Pflichtreviews und
Workflow-Funktion bleiben verbindlich. Veraltete Nachweise nehmen den neuen
Textstand nicht ab.

## Considered alternatives

Nur funktionale Punkte korrigieren: wurde angeboten; der Nutzer wählte
zusätzlich die Textüberarbeitung und den gemeinsamen Satz.

## Consequences

Betroffene Modellnachweise am neuen Stand erneuern; historische Ergebnisse
erhalten. Bestehendes Budgetregister und private CI-Freigaben gelten weiter.
Keine Installation oder Veröffentlichung.

## Confirmation

Alle 19 Punkte, Semantikvergleich und Datei-/Routendeltas aufzeichnen. Lokale
Tests, Builds und unabhängiges Astra-high-Review vor neuen Luna-high-Läufen;
deren Bewertung erfolgt verblindet in Gruppen mit Sol 6.1/high.

## Revisit when

Ein Textvergleich eine Bedeutungsänderung zeigt oder das verbleibende
Testbudget die notwendigen Wiederholungen nicht mehr abdeckt.
