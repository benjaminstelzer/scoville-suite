---
format_version: 1
id: ADR-0078
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/plan-validation
---

# Viewer-Test ausnehmen und Astra-Review vor Nachmessung verlangen

## Decision

Der Nutzer nimmt den Viewer-Test aus PLAN-0013 ausdrücklich aus. Vor der Nachmessung in W-007 prüft eine frische Astra-Medium-Aufgabe die Umsetzung gegen den Plan. Relevante Befunde werden vor der Nachmessung behoben.

## Problem

Rust ist auf diesem Host nicht verfügbar; zusätzlich verlangt der Nutzer eine unabhängige Prüfung vor dem Vergleich.

## Drivers

- Nutzeranweisung: Der Viewer wird nicht getestet.
- Nutzeranweisung: Astra Medium vor W-007s Nachmessung.

## Considered alternatives

- Rust installieren: Vom Nutzer nicht gewünscht.
- Viewer ungeprüft lassen und Grenze offen berichten: Entspricht der ausdrücklichen Ausnahme.

## Consequences

- Die Python- und Modellprüfungen bleiben verpflichtend.
- Es entsteht kein Viewer-Laufnachweis und keine Behauptung geprüfter Viewer-Kompatibilität.
- Die ursprüngliche Acceptance des gestarteten W-006 bleibt als Historie erhalten; seine Evidence nennt diese autorisierte Ausnahme.

## Confirmation

- Halte fehlende Viewer-Prüfung ausdrücklich fest.
- Bewahre Astra-Auftrag und Ergebnis samt Task-ID vor der Nachmessung.

## Revisit when

Der Nutzer beauftragt den Viewer-Test erneut oder der Review findet eine Änderung an dessen Leselogik.
