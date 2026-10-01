---
format_version: 1
id: ADR-0137
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: plan0029/ui-skill-test
---

# UI-Skill-Defekt prüfen statt Testprodukt reparieren

## Decision

Der Nutzer stoppt die Linden-Reparatur durch Luna ausdrücklich. Das Testprojekt
ist kein Produktauftrag. Ziel ist, den übersehenen Badge-Fehler im UI-Skill zu
finden und dessen Prüfregel zu korrigieren. Die begonnene gemeinsame
Komponentenänderung wird nicht weiter ausgeführt oder als bestandener Test
gewertet. Der gebaute Skill wird am erhaltenen Original read-only nachgeprüft.

## Problem

Der erste UI-Test übersah die innere Textausrichtung. Eine Reparatur seiner
Oberfläche würde allein nicht belegen, dass der Skill den Fehler erkennt.

## Drivers

- Ausdrücklicher Stopp der Produktkorrektur.
- Fehlbefund erhalten und Skill-Verhalten unabhängig prüfen.

## Considered alternatives

- Fixture fertig reparieren: widerspricht dem aktuellen Nutzerauftrag.

## Consequences

W-006 behält seine übrigen Tests. Der gestoppte Komponentenänderungsfall bleibt
mit seinen ungeprüften Edits als abgebrochener Versuch erhalten. W-015 prüft
die Skill-Korrektur. Ein bestandener Audit beweist keine fehlerfreie spätere
Implementierung und keinen kausalen Gewinn allein durch neue Formulierungen.

## Confirmation

Tatsächliche Referenzlektüre und übersehene Prüfbeziehung des ersten Laufs
auswerten. Frischer Luna-Medium-Audit liest den gebauten Skill, findet den
erhaltenen Fehler ohne vorgegebene Diagnose und ändert keine Produktdateien.

## Revisit when

Der Nutzer einen weiteren Implementierungstest ausdrücklich beauftragt.
