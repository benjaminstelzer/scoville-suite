---
format_version: 1
id: ADR-0237
status: accepted
created: 2026-11-15
accepted: 2026-11-15
scope: suite/skills
---

# Wiederholte Arbeit an realistischen Mengen messen und Wiederverwendung begrenzen

## Decision

Binding sections: complete

Der Eigentümer hat am 2026-11-15 entschieden:

- **Maßstab für wiederholte Arbeit:** Maßgeblich ist, welche Mengen die tatsächlichen Aufrufer der Anwendung übergeben können, dazu Auftrag und Projektregeln. Eine Abfrage, ein Netzaufruf, ein Dateizugriff oder ein Parse je Element wird schon bei mäßigen Mengen beseitigt. Arbeit im Speicher über wenige Elemente ist kein Mangel. Eine Größe, die kein realer Aufrufer erreicht, ist kein Maßstab, weder im Skill noch in der Bewertung eines Messlaufs.
- **Grenze der Wiederverwendung:** Vorhandene Logik wird bevorzugt, außer ihre Nutzung macht die Arbeit auf einer großen Menge quadratisch, wiederholt Abfragen, Lesen oder Parsen je Element oder verlangt mehr Hüllen, Caches und Anpassungen als eine schlichte Umsetzung. Dann wird die einfachere Fassung neu geschrieben; das ist keine verbotene zweite Implementierung.
- **Leseprüfung statt Nachweisverfahren:** Der Code-Skill verlangt vom Autor keine instrumentierte Zählung der Arbeit und keine Gegenfassung mehr. Die Regeln sind Prüfungen am gelesenen Quelltext. Messen gehört zu einem Auftrag oder einer Projektregel, die ausdrücklich eine Messung verlangt.
- **Gezielte Fragen mit Ortsangabe:** Der Autor beantwortet drei Fragen zum betroffenen Pfad (wiederholte Arbeit, erneut geladener Wert, erhaltener Zustand) mit Datei und Zeile und nennt die Antworten im Abschlussbericht. Diese Berichtszeilen sind die Ausnahme von der Regel gegen Berichtspflichten, weil Messläufe den Schritt ohne sie ausgelassen haben.

## Problem

Der Code-Skill war in sechzehn Fassungen gegen dieselben Diagnosefälle geschärft worden und verlangte zuletzt, eine Arbeitsgrenze durch Zählen am Einstiegspunkt samt Gegenfassung zu beweisen. Im Vergleich blieb die als quadratisch gewertete Arbeit in beiden Armen, die Modellzeit lag mit Skill beim rund Zweieinhalbfachen. Die Rohspuren zeigten zwei Ursachen: Ein Modell verwendete einen empfohlenen Projekthelfer je Schlüssel weiter, und die Bewertung maß einen Speicher-Durchlauf mit 576 Anfragen und Verschachtelungstiefen von mehreren Hundert, während der einzige Aufrufer die Bausteine einer Seite übergibt.

## Drivers

- Verständlicher, wartbarer Code ohne unnötige Komplexität hat Vorrang vor einer rechnerischen Schranke, die keine reale Nutzung erreicht.
- Die Komplexitätsregel ist seit dem 2026-11-12 eine Leseprüfung und lädt nicht zu Messen oder Instrumentieren ein.
- Eine Berichtspflicht braucht einen gemessenen Ausfall des Schritts.

## Considered alternatives

- Jede vermeidbare Wiederholung über gemeinsam genutzte Daten beseitigen, auch bei kleinen realen Mengen: besteht die bisherige Arbeitsprüfung, verlangt aber gemerkte Ergebnisse je Knoten und Zyklenbehandlung.
- Wiederholte Ein- und Ausgabe immer, Speicherarbeit nur bei belegten großen Mengen beseitigen: liegt nahe an der Entscheidung, lässt aber offen, woran „groß" gemessen wird.

## Consequences

- Die Arbeitsprüfung des Diagnosefalls R2 mit 576 Anfragen gilt als Kontext und nicht mehr als Abnahmekriterium. Abnahmerelevant sind dort die ursprüngliche Skalierungsprobe mit Abfragen und Parsen, die Funktion, der später gelesene Wert und die Parserformen.
- Die Mitgliedersuche im Diagnosefall N1 ist bei den Teilnehmerzahlen einer Wohngemeinschaft kein Mangel.
- Ein Modell kann eine Menge zu Unrecht für klein halten. Die Regel verlangt deshalb, die tatsächlichen Aufrufer zu lesen.

## Confirmation

Die gemeinsamen Code-Kriterien und der Code-Skill nennen den Maßstab, die Grenze der Wiederverwendung und die drei Fragen. Die Gesamtprüfung der Suite besteht. Vergleichsläufe mit gpt-6.1-sol und Claude Opus 5.5 gegen Läufe ohne Skills prüfen Funktion, später gelesenen Wert, erhaltenen Zustand und Modellzeit.

## Revisit when

Ein Modell lässt wiederholte Abfragen oder Parsen je Element stehen, hält eine wachsende Menge für klein, schreibt neu, wo der vorhandene Helfer gepasst hätte, oder die drei Berichtszeilen ändern das Ergebnis nicht.
