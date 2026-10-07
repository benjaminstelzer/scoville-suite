---
format_version: 1
id: ADR-0175
status: superseded
created: 2026-10-05
accepted: 2026-10-05
scope: suite/helper-evaluation
superseded_by: ADR-0185
---

# Eigenes Budget von achtzig Luna-high-Testversuchen

## Decision

PLAN-0035 erlaubt höchstens 80 Modelltest-Versuche insgesamt mit gpt-6-luna/high,
einschließlich Korrekturen und gegebenenfalls Viewer-Testversuchen. Sol-6.1/high-
Bewertungen und Astra-high-Pflichtreviews sind keine Luna-Testversuche.
Jeder Versuch wird vor Start in development/plan-evidence/0035-model-test-budget.json
reserviert. Reservierungen werden nicht gelöscht; gescheiterte, abgebrochene
und ungültige Versuche zählen mit. Nicht gestartete Reservierungen bleiben
konservativ belegt, bis ihr tatsächlicher Nichtstart nachgewiesen wurde.
Das Register bleibt unabhängig von PLAN-0034 und erweitert dessen Budget nicht.

Bei erschöpftem oder absehbar unzureichendem Budget vor dem nächsten Versuch
stoppen und den Nutzer mit Verbrauch, Restbedarf und Begründung fragen. Keine
automatische Erhöhung und kein PASS durch Weglassen gescheiterter Fälle.
Modelltests erst nach Abschluss von PLAN-0034 und Aktivierung von PLAN-0035.

## Problem

Mechanische Helper-Erweiterungen brauchen echte Verbraucherbelege und
Korrekturläufe ohne unbegrenzte oder mit PLAN-0034 vermischte Versuche.

## Drivers

- Ausdrückliche Nutzerentscheidung vom 05.10.2026: maximal 80 eigene Versuche.
- Gruppierte, verblindete Sol-Bewertung und Astra-Review je Arbeitspunkt.

## Considered alternatives

- Das Register von PLAN-0034 mitnutzen: widerspricht der getrennten Grenze.
- Bei Fehlschlägen automatisch erhöhen: widerspricht der Nutzerentscheidung.

## Consequences

Fallauswahl und notwendige Wiederholungen werden innerhalb der Grenze geplant.
Unvollständige Abnahme bleibt offen. Das Budget erlaubt keine CI-Pushes,
Veröffentlichung oder Aktivierung. Rohartefakte bleiben im Desktop-Testprojekt,
Ergebnisse und genaue Verweise in PLAN-0035 und dessen Evidence-Berichten.

## Confirmation

Vor dem ersten Versuch getrenntes leeres Register, Reserve-vor-Start und
Gesamtzählung prüfen. Alle Ergebnisse, Fehler und Abbrüche bleiben zuordenbar.
Diese Decision bestätigt keine schon erfolgten Tests.

## Revisit when

Die nötige Fallauswahl oder Korrekturen reichen voraussichtlich nicht in 80 Versuchen.
