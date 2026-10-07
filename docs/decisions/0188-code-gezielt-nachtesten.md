---
format_version: 1
id: ADR-0188
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/code-evaluation
---

# Code bis zum belastbaren Nachweis gezielt korrigieren

## Decision

Der Nutzer erlaubt mehrere Korrektur- und Nachtestdurchlaeufe fuer Code als zentrales Suite-Element. Die bisherige Dreirundengrenze gilt fuer Code nicht mehr. Eine unabhaengige Opus-5.5-Zweitmeinung ueber Ask soll das konkrete Standalone-Problem untersuchen.

## Problem

Die ersten beiden Code-Ueberarbeitungen bestehen die ausgewaehlte Standalone-Verstaendnisprobe nicht. Regeln sind vorhanden, Antworten lassen notwendige Fortsetzungsdetails aus. Ein weiterer blinder Textumbau ohne Ursachenpruefung liefert keinen belastbaren Skill-Nachweis.

## Drivers

Code muss im tatsaechlichen Einsatz funktionieren. Tests dienen seiner Qualitaet und pruefen jede bestaetigte Korrektur gezielt nach.

## Considered alternatives

Nach drei Revisionen Code als nicht angenommen melden: Der Nutzer priorisiert stattdessen weitere notwendige Durchlaeufe. Ein unverifizierter Stand darf weiterhin nicht als bestanden gelten.

## Consequences

Code innerhalb der genehmigten 120 Luna-high-Versuche priorisieren; Mehrbedarf vor dem naechsten Versuch konkret vorlegen. Andere Skills behalten ihre Grenzen. Eingefrorene Erwartungen, Wiederholungsregeln und Freigabegrenzen bleiben erhalten. Opus beraet read-only und ersetzt weder Luna-Nachweis noch Sol-Blockreview. Keine Installation oder Veroeffentlichung.

## Confirmation

Nutzerauftrag: "Code darf mehrere durchlaeufe haben, als zentrales Element der Suite ist es enorm wichtig dass dieser skill funktioniert". Danach ausdruecklich Opus 5.5 fuer eine Zweitmeinung zu diesem Problem erlaubt. Ursachen, Aenderung, gezielter Nachtest und gebuendeltes Sol-Urteil im W-009-Nachweis sichern.

## Revisit when

Die konkrete Restabnahme das Gesamtbudget ueberschreiten wuerde oder eine Aenderung der Pruefkriterien erforderlich wird.
