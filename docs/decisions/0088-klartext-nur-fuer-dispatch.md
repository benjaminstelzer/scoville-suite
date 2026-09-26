---
format_version: 1
id: ADR-0088
status: superseded
created: 2026-09-26
accepted: 2026-09-26
scope: suite/uebergabeformat
supersedes: ADR-0087
superseded_by: ADR-0089
---

# Klartext ausschließlich für Dispatch und Ergebnisübergaben

## Decision

Nur Dispatch-Aufträge, Übergaben und Worker-/Adviser-Ergebnisse müssen Klartext verwenden. Ask Claude bleibt ausgenommen. Technische Parameter, Konfiguration, Diagnosen und sonstige Helper-Daten dürfen JSON bleiben. Ihre Schnittstellen werden nicht wegen dieser Formatregel verändert.

## Problem

ADR-0087 und W-011 hatten die Nutzerkorrektur zu weit auf allgemeine Helper-Rückgaben ausgedehnt.

## Drivers

- Nutzer stellt ausdrücklich klar: Es geht rein um Dispatch-Übergaben und Rückgaben.

## Considered alternatives

- Allgemeines JSON-Verbot: verändert unnötig technische Schnittstellen.

## Consequences

Ask resolve behält JSON. Der Dispatch-Builder liefert Klartext. Die überschießende Vorgabe im gestarteten W-011 wird nicht ausgeführt; Evidence hält diese Korrektur fest.

## Confirmation

Klartext-Dispatch mit Unicode und originalen Rollenresultaten prüfen; technische Ask- und Claude-JSON-Ausgaben bleiben maschinell lesbar.

## Revisit when

Ein anderer Inhalt tatsächlich als Dispatch oder Ergebnisübergabe verwendet wird.
