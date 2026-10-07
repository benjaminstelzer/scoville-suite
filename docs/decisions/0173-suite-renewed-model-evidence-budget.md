---
format_version: 1
id: ADR-0173
status: proposed
created: 2026-10-05
scope: suite/evaluation
---

# Budget für neue Nachweise nach W-016

## Decision

Vorgeschlagen: höchstens 50 weitere Luna-high-Versuche, Gesamtgrenze 641.
Das gemeinsame Register bewahrt alle bisherigen Versuche. Keine getrennten
Pools und keine zusätzliche automatische Erweiterung. Sol 6.1/high bewertet
weiterhin verblindet in Gruppen nach ADR-0161.

## Problem

W-016 ändert fünf Skills und die gemeinsamen Schreibregeln aller acht Skills.
Die bisherigen Modellnachweise nehmen den neuen Stand nicht ab. Beim Vorschlag
sind 579 von 591 Luna-Versuchen gezählt, zwölf bleiben. Der externe Reviewauftrag
verlangt eine Rückfrage vor Modelltests bei unzureichendem Restbudget.

## Drivers

Gezielte erneute Skill-Fälle und native Workflow-Funktion sollen Fehler finden
und Korrekturen belegen. Runner-Benachrichtigung, Recovery und Pflichtreviews
bleiben erforderlich. Kosten sind keine Abnahmebedingung.

## Considered alternatives

Beim Rest von zwölf bleiben: gezielt innerhalb der Grenze prüfen, weitere
Pflichtnachweise offenlassen und W-014 nicht vollständig abnehmen.

## Consequences

Neue Modellläufe erst nach der tatsächlichen Nutzerentscheidung. Lokale Tests,
Runtime-CI und übrige autorisierte Arbeiten laufen unabhängig weiter. Keine
Installation oder Veröffentlichung. Native Hostfehler und fehlende Nachweise
werden nicht als Skill-PASS gewertet.

## Confirmation

Die Frage wurde dem Nutzer vor dem Start vorgelegt. Der Nutzer vertagt die
Budgetentscheidung bis zum finalen Änderungsstand; bis dahin keine neuen
Modelltests. Nach einer Entscheidung Budgetregister und betroffene Plan-Verweise
konsistent aktualisieren.

## Revisit when

Die gezielte erneute Abnahme oder notwendige Korrekturen die beschlossene Grenze
erreichen. Ohne neue Freigabe keine Überschreitung.
