---
format_version: 1
id: ADR-0087
status: superseded
created: 2026-09-26
accepted: 2026-09-26
scope: suite/uebergabeformat
superseded_by: ADR-0088
---

# Klartext für Scoville-Übergaben

## Decision

Scoville-Übergaben, Aufträge und agentenseitig gelesene Helper-Rückgaben verwenden Klartext statt JSON. Ask Claude bleibt ausdrücklich ausgenommen. Native Tool-Argumente, gespeicherte Konfiguration und interne maschinelle Verarbeitung bleiben unverändert.

## Problem

Die laufende Umsetzung führte Prompt-JSON und JSON-Zusatzaufträge ein. Der Nutzer stoppt diese Richtung wegen früherer Probleme mit JSON-Übergaben.

## Drivers

- Explizite Nutzerkorrektur: kein JSON für Übergaben in der Scoville-Suite.
- Explizite Ausnahme: Ask Claude.

## Considered alternatives

- JSON durch den Agenten umformen: erzeugt die ausdrücklich unerwünschte Nacharbeit.

## Consequences

W-011 korrigiert zuerst den Dispatch-Builder und die begonnenen nativen Ask-Rückgaben. Danach wird W-006 fortgesetzt. Frühere Abschlussbelege bleiben historische Beobachtungen, keine Freigabe für die verworfene JSON-Richtung.

## Confirmation

Builder-Ausgabe und Reviewer-Zusatzauftrag werden als unveränderter Klartext weiterverwendet. Ask Claude behält seine vorhandene JSON-Schnittstelle.

## Revisit when

Der Nutzer ausdrücklich ein anderes Übergabeformat beauftragt.
