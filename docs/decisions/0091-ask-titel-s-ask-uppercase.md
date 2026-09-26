---
format_version: 1
id: ADR-0091
status: superseded
created: 2026-09-26
accepted: 2026-09-26
scope: ask/chat-titles
superseded_by: ADR-0095
---

# Ask-Titel später an Workflow-Schreibweise angleichen

## Decision

Der Nutzer verlangt als vorgemerkte spätere Änderung das Kürzel S-ASK, die Modell-ID in Großbuchstaben und einen normalen Bindestrich statt des mittleren Punkts. Jetzt nur planen, nicht implementieren.

## Problem

Die bisherige Ask-Schreibweise weicht von Workflow-Titeln ab.

## Drivers

- Explizite Nutzeranweisung während der Suite-Abnahme.

## Considered alternatives

- Sofort umbenennen: widerspricht der ausdrücklichen zeitlichen Vorgabe.

## Consequences

Der aktuelle Runtime-Vertrag und laufende Chats bleiben unverändert. Spätere neue Titel verwenden beispielsweise S-ASK GPT-6-ASTRA - Plan überprüfen; technische Modell-IDs bleiben unverändert.

## Confirmation

Späterer nativer Titeltest nach der aktuellen Suite-Abnahme.

## Revisit when

Der Nutzer ein anderes Titelschema vorgibt.
