---
format_version: 1
id: ADR-0194
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/instruction-correction
---

# Einmaligen Entwurfshinweis bewahren und Handoff gezielt blockieren

## Decision

Nach Erklärung und Empfehlung beider Änderungen bestätigt der Nutzer:
„ja setze das so um“. Den einmaligen Non-goal über das Anlegen des Entwurfs
aus PLAN-0035 in dessen verlinkte Evidence verschieben. Handoff blockiert bei
unbekanntem Ziel; unbekannte Acceptance verlangt Klärung, wenn die nächste
Handlung davon abhängt. Astra/high prüft vor Source-Änderungen die Befunde
und die Erhaltung der ursprünglichen Handoff-Absicherung.

## Problem

Ein historischer Entwurfshinweis erreicht jeden Worker als Non-goal. Die
Handoff-Regel blockiert auch eindeutige erlaubte Schritte, deren Ergebnis
nicht von der noch unbekannten Acceptance abhängt.

## Drivers

Historie und Freigabegrenzen bewahren. Nur entscheidungsrelevante fehlende
Informationen erzwingen eine Rückfrage. Externes Review, Punkte 2c und 11:
development/plan-evidence/0035-w009-external-review-2026-10-06.txt.

## Considered alternatives

Beide Regeln behalten: kein Bedeutungswechsel, aber unnötige Unsicherheit
und Rückfragen. Die gewählte engere Regel erlaubt keinen Abschluss ohne
bekannte und belegte Acceptance.

## Consequences

Alle anderen Non-goals, erforderlichen Checks und Freigabegrenzen bleiben.
Historische FAILs erhalten ihren ursprünglichen Maßstab. Der unveränderte
Handoff-Fall mit unbekanntem Ziel und unbekannter Acceptance bleibt zu prüfen.
Die optionalen externen Vorschläge aus Punkt 12 sind dadurch nicht freigegeben.

## Confirmation

Astra-Ergebnis, Source-Diff, erhaltenen Entwurfshinweis und gezielten
Handoff-Nachtest in W-009 sichern. Die Nutzerentscheidung ist keine Testabnahme.

## Revisit when

Die engere Handoff-Regel einen erforderlichen Stopp verlieren würde.
