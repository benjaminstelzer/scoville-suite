---
format_version: 1
id: ADR-0134
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: suite/native-tests
---

# Verbleibende native Tests nach dem Agentenstopp

## Decision

Der Nutzer beauftragt echte Tests im gespeicherten Projekt `test`: zuerst
Workflow, dann Ask, Code, Plan, Project Context Cleanup und UI, jeweils seriell.
Alle Testrollen verwenden ausschließlich `gpt-6-luna/medium`. Der echte
Workflow darf vier oder fünf gleichzeitig aktive Agenten benötigen, aber keine
zehn oder zwanzig. Ein eigener Testchat in diesem Projekt ist damit autorisiert.
Die ursprüngliche Akzeptanz von W-006 bleibt verbindlich.

## Problem

Die früheren Tests liefen teilweise außerhalb der gespeicherten Projektzuordnung
und mehrere Fälle parallel. Reworker, Zwischenfragen, ein begonnener blockierter Punkt und ein fehlendes
Ask-Final sind nativ noch nicht belegt. Der beobachtete Kapazitätsfehler wurde
nicht durch Drain und identischen Retry weitergeprüft. Dafür ist kein Close-Tool
nötig. Nachweise: temp/2026-10-01-plan-0029/w6-completion-audit.md.

## Drivers

- Gesamten Plan mit belastbarer Evidenz abschließen.
- Serielle Ausführung und kleine tatsächliche Agentenzahl einhalten.
- Teiltests nicht als vollständige Akzeptanz ausgeben.

## Considered alternatives

- Echte serielle Tests: erhalten die Akzeptanz, benötigen weitere native Agenten.
- Akzeptanz ausdrücklich begrenzen: ermöglicht Abschluss mit benannten ungetesteten Fällen.
- Offen lassen: erhält beide Vorgaben, verhindert den beauftragten Gesamtabschluss.

## Consequences

Die neue Anweisung ersetzt den Agentenstopp nur für diese Testausführung und
die frühere Beschränkung auf keinen neuen Sidebar-Chat nur für den beauftragten
Testchat. Produktionssettings und Quellzuständigkeiten bleiben erhalten.
W-006 bleibt bis zu den vollständigen Nachweisen offen. Fehlende Hostfehler
bleiben ausdrücklich ungetestet, statt durch Simulation als nativ belegt zu gelten.

## Confirmation

Gespeicherte Projektzuordnung, tatsächliche Modell-/Effort-Metadaten, serielle
Phasen und Agentenzahl belegen. Fehlende Fälle im Desktop-Testprojekt ausführen
und echte Rollen, Zustände, Ergebnisse und Hostgrenzen behalten.

## Revisit when

Der Nutzer ändert die Testvorgaben oder die Hostmöglichkeiten ändern sich.
