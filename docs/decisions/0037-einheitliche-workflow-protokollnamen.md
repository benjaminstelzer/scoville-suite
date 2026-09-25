---
format_version: 1
id: ADR-0037
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: workflow/protocol-naming
---

# Einheitliche Namen für Workflow-Protokolle

## Decision

Der Dispatch-Vertrag heißt `SCOVILLE_DISPATCH_V1`. Das Ergebnisprotokoll behält den Namen `SCOVILLE_RESULT_V1`.

## Problem

Der bisherige Name `scoville-workflow-v1` folgte einem anderen Schema als das Ergebnisprotokoll und machte Richtung und Funktion des Vertrags nicht unmittelbar sichtbar.

## Drivers

- Beide Protokolle brauchen ein gemeinsames, leicht unterscheidbares Namensschema.
- Der Name muss Richtung und Version direkt zeigen.
- Die Umbenennung darf keine Autoritäts-, Identitäts-, Delivery- oder Recovery-Regel ändern.

## Considered alternatives

- `scoville-workflow-v1` beibehalten: vermeidet die Umbenennung, erhält aber das uneinheitliche Schema.
- Beide Protokolle neu benennen: schafft Einheitlichkeit, ändert aber unnötig den bereits eingeführten Ergebnisvertrag.
- Nur den Dispatch-Vertrag in `SCOVILLE_DISPATCH_V1` umbenennen: vereinheitlicht das Schema mit der kleinsten Vertragsänderung.

## Consequences

- Vollständige Dispatch-Prompts tragen `dispatch_contract=SCOVILLE_DISPATCH_V1`.
- Native Kontextprüfung und Tests erkennen ausschließlich den neuen Namen. Es gibt keinen Legacy-Zweig.
- `SCOVILLE_RESULT_V1` und seine Feldregeln bleiben unverändert.

## Confirmation

1. Prompt- und Native-Kontexttests prüfen den neuen Dispatch-Namen und lehnen den alten Namen als vollständigen Dispatch ab.
2. Workflow-, Suite-, Build-, Paket- und Exportprüfungen bestehen mit dem neuen Namen.
3. Die Quellprüfung findet den alten Namen nur noch in historischen oder gebundenen Baseline-Artefakten.

## Revisit when

Ein gemeinsamer maschinenlesbarer Umschlag beide Richtungen ohne getrennte Protokollkennungen zuverlässig abbildet.
