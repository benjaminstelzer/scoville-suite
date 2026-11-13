---
format_version: 1
id: ADR-0231
status: accepted
created: 2026-11-13
accepted: 2026-11-13
scope: suite/code
---

# Fail-first nur bei Fehlerbehebung und teurem Verhalten

## Decision

Binding sections: complete

Scoville Code verlangt einen Test, der vor der Änderung scheitert, nur in zwei Fällen:

1. Fehlerbehebung: Der scheiternde Test ist die Nachstellung des Fehlers und entsteht vor der Korrektur.
2. Verhalten, dessen Fehler teuer ist, etwa Geld, Berechtigungen, Datenverlust oder Sicherheit, oder wenn der Auftrag es verlangt.

Für alle anderen Änderungen gilt kein Fehlschlag-Lauf. Neues Verhalten bekommt einen Test an der Stelle der Regel; der Agent prüft durch Lesen, dass er das verlangte Ergebnis auf dem echten Codepfad prüft. Verhaltenserhalt nutzt die vorhandenen Tests vorher und nachher. Änderungen ohne Laufzeitverhalten bekommen die passende Quell-, Typ-, Lint- oder Build-Prüfung und keinen Test.

Unverändert bleibt für jede Änderung mit Test: den beweisenden Test beim Namen nennen, die Tests so ausführen, wie das Projekt sie ausführt, und belegen, dass er dabei gelaufen ist.

Eine Regel der Suite verlangt eine Liste, eine Berichtszeile oder einen zusätzlichen Lauf nur, wo ein belegter oder gemessener Ausfall zeigt, dass das Modell den Schritt sonst auslässt. Eine Dokumentationspflicht für jede Änderung ist kein zulässiges Mittel, um eine Regel prüfbar zu machen.

## Problem

Fail-first war als allgemeine Pflicht schon einmal in der Suite und wuchs zu einem aufwendigen Verfahren. Mit PLAN-0066 stand es wieder als Pflicht für jede Änderung in Regel 12; ein Review beanstandete das für Verhaltenserhalt und reine Textänderungen. Der Nutzer entschied, dass es nicht allgemein gelten soll, und überließ die genaue Grenze dem Agenten.

## Drivers

- Bei gewöhnlichem neuem Verhalten ist ein Test vor der Änderung selbstverständlich rot; der zusätzliche Lauf sagt nichts aus und greift in den Arbeitsstand ein.
- Bei einer Fehlerbehebung kostet der scheiternde Test nichts extra, weil der Fehler ohnehin nachgestellt wird.
- In den Messungen zu PLAN-0066 schrieben die Modelle auch ohne Skill meist einen aussagekräftigen Test; sie scheiterten daran, ihn zu benennen und zu bemerken, dass er nicht ausgeführt wurde.

## Considered alternatives

- Fail-first für jedes neue oder korrigierte Verhalten: verhindert selten etwas, das die Leseprüfung nicht auch findet, und macht jede Änderung zum Verfahren.
- Fail-first nur für teures Verhalten, ohne Fehlerbehebung: lässt den Fall aus, in dem der Test am ehesten am Fehler vorbeigeht.

## Consequences

Bei gewöhnlichem neuem Verhalten ist nicht durch einen Lauf belegt, dass der Test ohne die Änderung scheitert. Ein Test, der aus dem falschen Grund besteht, wird dort nur durch Lesen entdeckt. Berichte enthalten keine Zeile je Funktion mehr, sondern nur, was zutrifft.

## Confirmation

In den Aufgaben zu PLAN-0066 mit kleinem Auftrag, Kapselung, Architektur-Review, neuem Projekt und roten Tests bleibt das Ergebnis gegenüber dem Stand mit allgemeinem Fail-first erhalten. Bei der Fehlerbehebungsaufgabe entsteht ein scheiternder Test vor der Korrektur.

## Revisit when

Modellläufe oder ein Vorfall zeigen Tests für neues Verhalten, die ohne die Änderung bestehen, oder der Nutzer will die Grenze verschieben.
