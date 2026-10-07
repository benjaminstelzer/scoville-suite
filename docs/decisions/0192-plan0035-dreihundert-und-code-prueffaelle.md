---
format_version: 1
id: ADR-0192
status: superseded
created: 2026-10-06
accepted: 2026-10-06
scope: suite/evaluation
supersedes: ADR-0187
superseded_by: ADR-0198
---

# 300 Gesamtversuche und drei unabhängige Code-Prüffälle

## Decision

Nutzerauftrag: „Mache ingesamt. 300 Luna Budget. Lasse Opus 5.5 nochmal 3
unabhängige Prüffälle für Code schreiben und damit testen. Lasse die Tests von
Astra Medium überprüfen ob sie korrekt sind.“ Für ganz PLAN-0035 gelten damit
höchstens 300 Luna/high-Reservierungen einschließlich aller bisherigen Zeilen,
nativen Rollen und Korrekturläufe. Keine alten Reservierungen umwidmen.

Opus 5.5/high erstellt drei voneinander unabhängige praktische Code-Fälle.
Astra/medium prüft Aufgaben, Fixtures, Erwartungen und ausführbare Prüfungen
vor Luna-Starts. Testaufbaufehler vorab korrigieren und erneut prüfen lassen.
Sol6.1/high bewertet die tatsächlichen Ergebnisse pro Block. Bestätigte
Skill-Fehler korrigieren und den betroffenen Fall nachtesten.

## Problem

Die bisherige Grenze ist mit 120 Reservierungen erreicht. Weitere Pflichtproben
und gezielte Code-Nachweise fehlen. Abstrakte Code-FAILs bleiben historische
Ergebnisse; der neue Auftrag entscheidet ADR-0190 nicht ausdrücklich.

## Drivers

Skill-Qualität durch reale Anwendung prüfen. Unabhängige Aufgaben und korrekte
Testverträge vor Ausführung sichern. Mehr Budget ist kein Verbrauchsziel.

## Considered alternatives

120 oder die vorgeschlagenen 130 behalten: entsprechen nicht der neuen
ausdrücklichen Nutzerwahl. 300 erlauben: schafft Nachtestreserve, ohne
Prüfkriterien oder Freigabegrenzen zu schwächen.

## Consequences

Dasselbe Register und dessen Validierung auf 300 mit dieser Authority umstellen.
Alle 120 bisherigen Einträge vollständig erhalten. Neue Fälle vorab einfrieren,
dreimal je unabhängiger Variante prüfen, bei gemischtem Urteil fünfmal gemäß
bestehendem Testvertrag. Keine künstlichen identischen Varianten. W-015 zuletzt.
Keine Installation, Veröffentlichung, Suite-Source-Pushes oder lokale Viewer-
Kompilierung autorisiert. Die Ask-Beobachtungsgrenze bleibt gesondert offen.

## Confirmation

Vor neuen Starts den harten Stopp, falsche Authority, Historienerhalt und die
gemeinsame Zählung tatsächlicher Rollen nachtesten. Opus-Antwort, Astra-Urteil,
eingefrorene Fälle, Pakethashes, native Profile und vollständige Sol-Blockurteile
in den bestehenden W-009-Nachweisen sichern. Historische FAILs nicht umwerten.

## Revisit when

Der konkrete Bedarf 300 überschreiten würde oder ein Prüfkriterium geändert
werden müsste. Vor der abhängigen Ausführung entscheiden.
