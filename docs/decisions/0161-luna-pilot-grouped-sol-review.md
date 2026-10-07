---
format_version: 1
id: ADR-0161
status: superseded
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
superseded_by: ADR-0166
---

# 150 Luna-high-Testläufe mit gebündelter Sol-Bewertung

## Decision

Das Testbudget beträgt insgesamt 150 Testläufe mit gpt-6-luna auf high.
gpt-6.1-sol auf high bewertet die Ergebnisse gemeinsam am Ende oder als
vollständige Gruppe pro Test. Kein abwechselnder Ablauf aus einzelnem Test
und einzelnem Review. Verblindung und getrennte Erwartungen bleiben erhalten.

## Problem

ADR-0150 ließ Pilotbudget und Bewertungsablauf offen.

## Drivers

Ausdrückliche Nutzerentscheidung während der Vorbereitung von W-001.

## Considered alternatives

Einzelreviews nach jedem Lauf entsprechen nicht dem gewünschten Ablauf.

## Consequences

Kontrollen, Wiederholungen und fehlgeschlagene Transportversuche werden innerhalb
der 150 Testversuche gezählt, damit keine zusätzlichen Testläufe entstehen.
Bewertungen laufen separat mit Sol. Die Astra-High-Reviews der umgesetzten
Planpunkte bleiben bestehen. Zunächst wird W-001 vorbereitet. Diese Entscheidung
startet W-014 nicht und genehmigt weder Claude-Testbudget, native Workflow-/Ask-
Proben, CI-Push noch die vollständige Matrix.

## Confirmation

Ein gemeinsames Laufregister belegt höchstens 150 gestartete Testversuche,
Luna/high und gesammelte Sol/high-Bewertungsaufträge mit vollständigen Gruppen.
Unbekannte tatsächliche Modell- oder Effort-Telemetrie bleibt unbekannt.

## Revisit when

Mehr Läufe, ein anderes Modell oder native Proben benötigt werden.
