---
format_version: 1
id: ADR-0190
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/code-evaluation
---

# Code-Standalone an Paket und tatsächlicher Fortsetzung prüfen

## Decision

Den vorhandenen Standalone-Fall als Testaufbaugrenze behalten,
nicht mehr als Pflicht zur spontanen vollständigen Verfahrenswiedergabe abnehmen.
Stattdessen vollständige gebündelte Guidance anhand der tatsächlichen Paketdateien
und praktische Fortsetzung anhand des vorhandenen 2/2-Vertrags prüfen. Erhaltene
Nutzerentscheidungen samt Herkunft, aktuelle Zustandsabklärung, Wiederverwendung
gültiger Arbeit, vorhandener Record-Owner und unveränderte Tests bleiben Pflicht.
Nach Erklärung und Empfehlung bestätigt der Nutzer ausdrücklich:
„Ja, Empfehlung gemäß ADR-0190 übernehmen“.

## Problem

Given nennt nur den installierten Standalone-Skill; Expect fordert vollständige
Planungs-/Fortsetzungsguidance. Sol bewertet deren fehlende Wiedergabe als FAIL.
Opus bestätigt Paketvollständigkeit und sieht einen Aufgabenrahmenkonflikt.
Weitere Source-Umschreibungen sind durch diese Antworten nicht gestützt.

## Drivers

Skill-Qualität und erforderliche Fortsetzungsfakten belegen. Die bisherigen
0/3-Gruppen und der praktische 1/2-Stand bleiben erhalten, nicht umbewertet.

## Considered alternatives

Spontane vollständige Wiedergabe weiter verlangen: unveränderter Maßstab,
Code bleibt ohne bestandenen Pflichtnachweis. Paket plus praktische Fortsetzung:
bindet die Prüfung an die nutzbare Fähigkeit, ändert aber die Abnahmehürde.

## Consequences

Nur die Nachweisrolle dieses Code-Falls wird geändert; originale Case-Datei,
Erwartung und historische Ergebnisse bleiben unverändert. Kein allgemeines
Code-PASS aus Source-Lektüre, kein Ersatz für einen fehlenden Wirkungsnachweis.
Andere Cases, Sol-Blockreviews und Freigabegrenzen bleiben. Für das aktuelle
Gesamtbudget gilt ADR-0192 mit 300 Reservierungen. Historische FAILs werden
nicht umbewertet; Paketprüfung allein begründet keine Wirkungsabnahme.

## Confirmation

Die Nutzerentscheidung ist oben festgehalten. Paket-Guidance, tatsächliche
unveränderte Erwartungen, native Fortsetzung, Artefakte und Sol-Gruppenurteil prüfen.
0035-w009-code-current-opus-cause.json und 0035-w009-code-revision6-review.json
bewahren die unabhängigen unterschiedlichen Bewertungen.

Der gezielte Nachtest von Code7 besteht den unveränderten praktischen 2/2-Vertrag
mit vollständigem Sol-Blockreview: 0035-w009-code-revision7-continuation-review.json.
Beide Records erhalten Nutzerattribution und bestätigten Status getrennt vom
Testergebnis. Der Snapshot berichtet die Nutzerbestätigung; ein ursprünglicher
Nutzerturn und ausdrücklich benannte Transportherkunft sind damit nicht belegt.
Dieser PASS erfüllte vor der Nutzerentscheidung nicht die alte Wiedergabehürde.
Er trägt nach der ausdrücklichen Entscheidung den praktischen Teil dieses
begrenzten Maßstabs. Seine belegten Grenzen bleiben erhalten.

## Revisit when

Die neue praktische Abnahme offen bleibt oder ein weiterer Maßstab geändert
werden müsste.
