---
format_version: 1
id: ADR-0232
status: accepted
created: 2026-11-14
accepted: 2026-11-14
scope: suite/plan
---

# Plan: kleine Zusatzarbeit direkt erledigen

## Decision

Binding sections: complete

In einem Projekt mit Planungsprofil erledigt der Agent Arbeit direkt und ohne Plan-Eintrag oder Helper-Lauf, wenn alle drei Bedingungen gelten:

1. Kein Work Item deckt sie ab.
2. Der Nutzer hat nicht verlangt, sie zu planen oder zu verfolgen.
3. Sie wird in der laufenden Sitzung fertig.

Das gilt auch für Zusatzbitten während eines laufenden Work Items. Ein Work Item entsteht für solche Arbeit nur, wenn der Nutzer sie verfolgt haben will, wenn sie jetzt nicht fertig wird oder wenn eine Regel des Projekts einen Eintrag verlangt.

Das bloße Vorhandensein eines Planungsprofils löst den Plan-Skill nicht aus. Auslöser sind eine Plan-Anfrage, Arbeit an einem vorhandenen Work Item und ausdrücklich verlangte dauerhafte Planung.

## Problem

Der Plan-Skill hängte jede neu verlangte Arbeit als eigenes Work Item mit Outcome, Acceptance und Steps an und reihte sie hinter das laufende Item ein. Eine Zusatzbitte von wenigen Sekunden wurde so zu einem Eintrag mit Validierung, und die Bitte wartete. Die Ausnahme für kleine Aufgaben war zirkulär formuliert („small tasks needing no durable Plan") und nahm nur einen neuen Plan aus, nicht ein neues Work Item. Ein Review mit Opus 5.5 am 2026-11-13 meldete das als Fall, in dem die Aufzeichnung zum Ziel wird.

## Drivers

- Der Eigentümer will keine Verfahren, die jede kleine Änderung mittragen muss.
- Ein Plan dient dem Wiederaufnehmen unterbrochener Arbeit; Arbeit, die in der Sitzung endet, braucht das nicht.
- Die Git-Historie hält fest, was geändert wurde.

## Considered alternatives

- Jede neu verlangte Arbeit als Work Item: lückenlose Spur im Plan, aber Verwaltungsaufwand und Wartezeit für Kleinigkeiten.
- Direkt erledigen und eine Zeile in Evidence des laufenden Work Items ergänzen: kein neues Item, aber weiter eine Pflichtzeile für jede Kleinigkeit.

## Consequences

Kleine Zusatzarbeiten stehen nur in der Git-Historie und nicht im Plan. Ob etwas in der Sitzung fertig wird, schätzt der Agent; stellt sich die Arbeit als größer heraus, legt er dann ein Work Item an.

## Confirmation

Die Beschreibung, der Eingangssatz, die Regeln 3, 5 und 7 von Scoville Plan und der passende Abschnitt in authoring.md nennen die drei Bedingungen. Die Gesamtprüfung der Suite besteht.

## Revisit when

Zusatzarbeiten gehen verloren oder werden doppelt gemacht, weil sie in keinem Plan stehen, oder der Nutzer will die Grenze verschieben.
