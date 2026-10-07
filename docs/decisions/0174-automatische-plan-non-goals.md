---
format_version: 1
id: ADR-0174
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: workflow/dispatch
supersedes: ADR-0099
---

# Plan-Non-goals automatisch, sonstiger Dispatch-Vertrag erhalten

## Decision

Die am 2026-09-27 beauftragte Umsetzung von PLAN-0018 übernimmt den projektspezifischen Review-Rhythmus. Ohne abweichende Vorgabe erfolgt das unabhängige Review am vollständigen Planpunkt. Steps bleiben geordnet und dürfen wie in ADR-0093 zusammengefasst werden. Nach geprüften Gruppen darf Arbeit weitergehen, während Schlussreview und endgültige Abnahme offen bleiben. Nur abgenommene Änderungen werden committed.

Ein verfügbarer Worker kann verwandte Folgeaufträge oder Korrekturen übernehmen, wenn Modell und Kontext passen. Reviewer bleiben unabhängig. Rollover führt dieselbe Arbeit fort und erhält offene Reviews. Die 40/60-Schwellen aus ADR-0098 bleiben unverändert.

Gestartete Planpunkte dürfen angenommene ADR-Verweise ergänzen und nachweislich rein formale Angaben korrigieren, ohne Ersatzpunkte anzulegen. Alte Entscheidung und Änderungsgrund bleiben nachvollziehbar. Materielle Änderungen benötigen weiterhin ausdrückliche Entscheidung. Evidence hält Ergebnisse und einen genauen Berichtsverweis statt Versuchsprotokollen fest.

Für PLAN-0035 gilt zusätzlich die ausdrückliche Entscheidung vom 05.10.2026:
Der Dispatch-Builder übernimmt ausschließlich die Plan-Non-goals wörtlich aus
der Selector-Ausgabe für Executor, Reviewer, Korrektur und Recovery. Goal und
Decisions werden nicht automatisch übernommen. Der Manager bestimmt weiterhin
relevante Goal-Teile, geltende ADR-Vorgaben, Berechtigungen und Abhängigkeitsergebnisse.
Diese Ergänzung ersetzt die Beschränkung auf supplemental-context aus ADR-0093
nur für Non-goals. Die übrigen Regeln von ADR-0099 gelten unverändert in ihrem
ursprünglichen Scope; historische Modell- und Schwellenangaben setzen keine
neuen Modelle, Projektschwellen oder Testbudgets für PLAN-0035.

Aus ADR-0093 bleiben erhalten: Kleine zusammengehörige Steps dürfen einen
Auftrag bilden, die Reihenfolge bleibt innerhalb und zwischen Aufträgen erhalten.
Ein Auftrag umfasst einen Step, einen zusammenhängenden Bereich oder den ganzen
Planpunkt. Der Worker erhält den vollständigen Planpunkt und den eindeutig
benannten Auftrag; Recovery führt nur dessen verbliebene Arbeit fort.
Rollover erfolgt bei Kontextbedarf an einer sinnvollen Arbeitsgrenze. Der Handoff
nennt Erledigtes, Änderungen, tatsächliche Checks, offene Arbeit und den nächsten
Schritt. Der Nachfolger setzt denselben Auftrag fort. Historische Abnahmen bleiben
erhalten, bestehende Bereiche wie W-001/steps-1-4 bleiben nutzbar. Keine neuen
Statusmodelle oder Gruppierungsfelder; diese Decision beauftragt nur die benannte
Erweiterung des vorhandenen Dispatch-Builders.

## Problem

Ein Review je Dispatch widerspricht dem DIVI-Vertrag und wiederholt Kontext. Unveränderliche ADR-Listen erzeugten Ersatzpunkte; lange Evidence-Listen wiederholen den Ablauf bei jedem Lesen.

Zu wenig Kontext verliert Anforderungen; unklarer Umfang verleitet zum
Vorwegnehmen. Nur Einschränkungen dürfen automatisch weitergegeben werden.
Decision-Abschnitte können CI-Pushes oder Claude-Aufrufe erlauben, die ein Worker
nicht als eigene Befugnis übernehmen darf. Die Nutzerangaben von 119 Non-goals-
Wörtern und 681 Wörtern in 13 ADRs sind historische Messangaben des Auftrags,
keine hier neu geprüften Nachweise und keine feste Implementierungsgrenze.

## Drivers

- Ausdrücklicher Umsetzungsauftrag für PLAN-0018, beginnend beim DIVI-Projektvertrag.
- Weniger Aufwand bei gleicher Abnahme und nachvollziehbaren Entscheidungen.

- Einfacher nativer Ablauf mit wenig Tokenaufwand, ausreichendem Kontext und
  verbindlicher Reihenfolge, wie in ADR-0093.
- Ausdrückliche Nutzerentscheidung: automatische Einschränkungen, keine Erlaubnisse.

## Considered alternatives

- Zusätzlicher Leichtmodus: unnötige Verzweigung im selben Ablauf.
- Prüfungen oder Historie streichen: verliert erforderliche Nachweise.

- Jeden Step einzeln dispatchen: wiederholt Einarbeitung bei kleinen Gruppen.
- Immer den ganzen Punkt dispatchen: zu starr für große eigenständige Abschnitte.
- Decisions automatisch übernehmen: verteilt möglicherweise Manager-Befugnisse.

## Consequences

Review-Grenzen sind von Worker-Grenzen getrennt. Aufgaben können weiterlaufen, ohne fälschlich als abgenommen zu gelten. Keine automatischen Retry-Schleifen und keine parallelen Source-Schreiber. Historische akzeptierte Befunde und frühere ADR-Verweise bleiben erhalten.

Die Non-goals erhalten eine begründete Größenobergrenze. Bei Überschreitung
bricht der Builder ohne Teilausgabe mit konkreter Diagnose ab. Keine weitere
automatische Auswahlmechanik, keine Übernahme von Goal oder Decisions.

## Confirmation

Gezielte SOL-6-Medium-Fälle prüfen geordnete Gruppen, ein Abschlussreview, Korrektur, Rollover und schmale Planänderungen. Astra Medium prüft den finalen Regelstand und Befunde unabhängig.

PLAN-0035/W-004 prüft verlustlose Non-goals in sämtlichen Dispatch-Routen,
Grenzwerte und Rollenbefugnisse mit tatsächlichen Verbrauchern. Die geordneten
Gruppen und Rollover-Restarbeit bleiben erhalten. Historische SOL-6-Medium- und
Astra-Medium-Prüfaufträge aus ADR-0093/0099 sind keine aktuellen Testresultate;
PLAN-0035 verwendet seine eigenen Modelle, Reviews und sein Budget.

## Revisit when

Ein Review-Scope verliert unreviewte Änderungen oder eine formale Änderung verändert die fachliche Abnahme.

Eine automatische Einschränkung geht verloren, wird zur Erlaubnis oder verursacht unverhältnismäßigen Kontextaufwand.
