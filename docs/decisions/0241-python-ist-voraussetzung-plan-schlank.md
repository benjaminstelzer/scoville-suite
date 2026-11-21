---
format_version: 1
id: ADR-0241
status: accepted
created: 2026-11-20
accepted: 2026-11-20
scope: suite/runtime
---

# Python ist Voraussetzung; Plan beschreibt seine Struktur einmal

## Decision

Binding sections: complete

Python 3.11 oder neuer ist Voraussetzung für jeden Skill der Suite, der Hilfsprogramme mitbringt. Es gibt in keinem Skill und in keinem Profil einen manuellen Ersatzweg ohne Python. Findet die Python-Ermittlung keinen passenden Interpreter, fehlt ein Skript oder scheitert ein Hilfsprogramm, hält der Agent den betroffenen Vorgang an und meldet die Ursache mit der Diagnose des Hilfsprogramms. Er erledigt die Arbeit eines Hilfsprogramms nie von Hand.

Für Scoville Plan gilt zusätzlich:

- Die Skripte `validate_profile.py` und `select_context.py` sind die einzige Beschreibung der Struktur von Plänen und Entscheidungen. Was sie erzwingen oder ausgeben, wird im Text nicht ein zweites Mal erklärt; wo eine Meldung oder Ausgabe dafür nicht reicht, wird sie selbst verständlich gemacht. Feldnamen und Aufbau der Ausgabe bleiben, weil Workflow und der Plan Viewer sie lesen.
- Die Lese- und Reparaturregeln für abgeschaffte Formate entfallen: das Feld `Next action` und unmarkierte Schritte, die Titelpräfixe `Deferred` und `Prioritized` mit historischer Priorität und Rückkehrvermerken, Stapel-Metadaten in Entscheidungen. Das Prüfprogramm akzeptiert sie weiter; der Skill beschreibt sie nicht mehr.
- Plan ist der meistgenutzte Skill: Er wird auf den Alltag gekürzt (Plan anlegen, nach Unterbrechung fortsetzen, Schritt abschließen, Entscheidung festhalten, prüfen). Seltene Abläufe stehen in einer Referenz, die nur auf ausdrücklichen Wunsch geladen wird. Eine gekürzte Fassung gilt erst als fertig, wenn sie diese Aufgaben mit beiden Testmodellen nicht schlechter löst als die Fassung davor.

## Problem

Die allgemeine Fassung führte zu jedem Hilfsprogramm eine Ersatzdatei, die dessen Verhalten in Prosa wiederholte. Jede Formatregel von Plan stand dadurch dreimal: im Prüfprogramm, in der Beschreibung und in der Ersatzdatei. Von rund 13.350 Wörtern des Plan-Skills dient etwa ein Drittel dem Alltag; der Rest beschreibt Werkzeuge ein zweites Mal, Formate, die der Skill selbst abgeschafft hat, und Einzelfälle.

## Drivers

- Nutzerentscheidungen vom 2026-11-20: keine Ersatzwege mehr in der gesamten Suite; Altformate streichen; Plan schlank und funktional; die Erklärung der Ausgabefelder in die Skripte verlagern.
- ADR-0240: eine Formulierung je Regel.

## Considered alternatives

- Ersatzdateien nur im Plan-Skill streichen: lässt in jedem anderen Skill dieselbe Doppelung und zwei Regeln für dieselbe Lage.
- Altformate in einer selten geladenen Referenz behalten: Die eigenen Pläne enthalten sie nicht mehr; die Pflege bliebe.

## Consequences

Die öffentliche allgemeine Fassung verspricht keinen Betrieb ohne Python mehr; ihre Kompatibilitätsangaben nennen Python 3.11 als Voraussetzung. Wer Pläne im alten Format hat, findet im Skill keine Anleitung mehr, sie zu lesen oder umzustellen. Änderungen an mitgelieferten Skripten verlangen vor einer Veröffentlichung einen neuen Lauf der Laufzeitprüfung.

## Confirmation

Die Gesamtprüfung der Suite besteht nach dem Entfernen der Ersatzdateien; kein mitgeliefertes Skript ist dabei geändert. Für den gekürzten Plan-Skill: Gesamtprüfung, die Tests der Skripte mit ihrem Abnehmer in Workflow und ein Modellvergleich der Alltagsaufgaben mit gpt-6.2-sol und Claude Opus 5.5 auf medium, alte gegen neue Fassung.

## Revisit when

Ein unterstützter Host bringt kein Python 3.11 mit, oder der Modellvergleich zeigt, dass eine Alltagsaufgabe mit der gekürzten Fassung schlechter gelöst wird.
