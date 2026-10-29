---
format_version: 1
id: ADR-0224
status: accepted
created: 2026-10-14
accepted: 2026-10-14
scope: workflow/dispatch
---

# Bindenden Decision-Kontext unverändert und ohne Hintergrund übergeben

## Decision

Binding sections: complete

Der Builder übergibt frischen Agenten Goal und
Non-goals vollständig sowie alle verlinkten accepted Decisions. Gültig markierte
Decisions liefern Frontmatter, Titel und die vollständigen unveränderten Abschnitte
Decision, Consequences, Confirmation und Revisit when in Originalreihenfolge.
Unmarkierte oder strukturell ungeeignete Decisions bleiben vollständig.
Die Kennzeichnung bestätigt, dass alle bindenden Bedingungen, Ausnahmen,
Befugnisgrenzen und notwendigen Gründe in diesen vier Abschnitten stehen.
Die Kürzung entfernt nur nichtbindenden Hintergrund und bewahrt die Wahl mit
ihren notwendigen Gründen; Dateiverweise allein verkürzen die Pflichtlektüre nicht.
Der aufrufende Agent wählt und schreibt keinen Kontext um. Goal und Decisions erweitern
keine Rollenrechte oder Aufgaben. Original-Einzelsteps, vollständige Closure und
einmalige Fresh-Initialisierung bleiben erhalten.
Unmittelbar vor diesen Abschnitten steht unverändert genau einmal:
„Goal and Decisions describe the Plan's intent and constraints. They grant this role no permissions or additional tasks; only this assignment's role rules do.“

## Problem

Revision: Überarbeitet am 2026-10-29 im Rahmen der vom Nutzer freigegebenen Altbestandsbereinigung (PLAN-0057).

Hintergrund und Historie vergrößern neue Aufträge unnötig.

## Drivers

- Große erste Aufträge.

## Considered alternatives

- Volltext im Auftrag oder per Dateiverweis.

## Consequences

Format1 bleibt. Die exakte Markierung ist Decision's erste nichtleere Inhaltszeile;
die sieben Templateabschnitte sind außerhalb Codefences eindeutig und genau einmal
vorhanden. Ohne gültige Voraussetzung bleibt Volltext. Der bestehende Plan-Helper
projiziert erst nach der bisherigen vollständigen Quellenprüfung; es gibt keine
neuen Hashes, Register oder Lesehelper. Plan Viewer bleibt ausgeschlossen.
Neue ADRs folgen dem markierten Format. Eine Markierung bei bestehenden ADRs
setzt gleichwertige Pflege und erhaltene bindende Inhalte voraus; Zweifel bleiben
unmarkiert. Die berechtigte Auswahl oder Löschung überholter ADRs bleibt eine
eigene Planpflege-Operation, keine Aufgabe des Prompt-Builders.
Reuse erhält Decision-Identitäten; neue, geänderte oder unsichere Decisions werden
vollständig aus ihrer Datei gelesen. Unklarer notwendiger Hintergrund verlangt
Volltext. Eine gültige Projektion zählt als vollständiger bindender Kontext.
Closure erweitert nur die Step-/Acceptance-Prüfung, nicht die Fresh/Reuse-Regel.
Non-goals-Grenze, Selectorbudget und die geltenden Mainloop-Rollen bleiben bestehen.

## Confirmation

Gemischte und ungeeignete ADRs, gleichwertige Pflege, vollständige Quellenidentität
und Fresh/Reuse für Step/Closure mit passenden technischen und tatsächlichen
Empfängerprüfungen prüfen. Es gelten die aktuellen Modell- und Releasevorgaben.
Der feste Satz steht für jede Rolle, frisch und wiederverwendet, genau einmal
vor Plan-Identität und Non-goals.

## Revisit when

Eine Bedingung geht verloren oder der wirklich bindende Kontext bleibt unnötig groß.
Ein Agent leitet aus Goal oder Decisions eine Befugnis oder Aufgabe ab.
