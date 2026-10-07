---
format_version: 1
id: ADR-0164
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
---

# Modellkosten blockieren den begrenzten Test nicht

## Decision

Modellkosten spielen für den Test keine Rolle. Die zusätzlichen Eingabe-Tokens
der Schreibregeln sind kein Grund für eine Änderung oder weitere Kostenfreigabe
vor diesem Test. Die Grenze von 150 Luna-high-Testversuchen bleibt erhalten.

## Problem

Opus v4 verlangte eine Kostenentscheidung vor dem Teststart.

## Drivers

Ausdrückliche Nutzerklärung zu den erläuterten Modell- und Kontextkosten.

## Considered alternatives

Die Schreibregeln nur zur Kostensenkung zu ändern ist für diesen Test unnötig.

## Consequences

Der aktuelle Regelumfang bleibt bestehen. Datei- und Routendeltas werden
weiterhin transparent dokumentiert. Die Entscheidung ersetzt weder fachliche
Abnahme noch Hostqualifizierung, native Freigaben oder das Versuchslimit.

## Confirmation

Der Bericht trennt statische Token-Proxys, tatsächliche Usage und Geldkosten.
Keine weiteren Testversuche werden aus fehlendem Kostendruck abgeleitet.

## Revisit when

Der Nutzer Umfang oder Budgetgrenze ändert.
