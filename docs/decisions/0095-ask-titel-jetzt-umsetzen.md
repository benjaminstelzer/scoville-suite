---
format_version: 1
id: ADR-0095
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: ask/chat-titles
supersedes: ADR-0091
---

# Ask-Titel jetzt in PLAN-0014 umsetzen

## Decision

W-015 bleibt in PLAN-0014 und wird auf ausdrücklichen Nutzerauftrag jetzt
umgesetzt. Neue native Titel verwenden S-ASK, die Modell-ID in Großbuchstaben
und einen normalen Bindestrich als Trenner. Technische Modellparameter und
bestehende Follow-up-Identitäten bleiben erhalten.

## Problem

Die bisherige zeitliche Zurückstellung verhindert den Planabschluss.

## Drivers

- Nutzerauftrag: „Im 14er Plan und gleich umsetzen“.

## Considered alternatives

- Separater Entwurfsplan: vom Nutzer nicht gewählt.

## Consequences

Die Zurückstellung aus ADR-0091 endet; das dort gewählte Titelschema bleibt.

## Confirmation

Neuer nativer Ask-Chat mit SOL 6 Medium, korrektem Titel und tatsächlicher
Rückzustellung. Bestehende Chats werden nicht umbenannt.

## Revisit when

Der Nutzer ein anderes Titelschema verlangt.
