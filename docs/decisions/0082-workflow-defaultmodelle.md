---
format_version: 1
id: ADR-0082
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/model-defaults
---

# Bestätigte Workflow-Defaults übernehmen

## Decision

Die vom Nutzer bestätigten Paare gelten als neue Workflow-Defaults:

| Route | Execute | Reasoning | Review | Reasoning |
| --- | --- | --- | --- | --- |
| ultra_low | gpt-6-sol | medium | gpt-6-sol | high |
| low | gpt-6-sol | high | gpt-6-sol | xhigh |
| medium | gpt-5.6-sol | medium | gpt-5.6-sol | high |
| high | gpt-6-astra | medium | gpt-6-astra | high |
| ultra_high | gpt-6-astra | high | gpt-6-astra | xhigh |

Die Nutzerbezeichnung xhigh meint hier die bestehende Route ultra_high.
Das zuvor verlangte Ask-SOL-Preset bleibt gpt-5.6-sol mit high.

## Problem

Die bisherigen Defaults entsprachen nicht der final bestätigten Modellbelegung.

## Drivers

- Explizite Tabelle und Bestätigung des Nutzers.

## Considered alternatives

- Alle SOL-Routen auf 5.6: Durch die spätere Tabelle ersetzt.

## Consequences

Kanonische Konfiguration und ihre Build- und Installationsprojektionen müssen übereinstimmen. Projektbezogene Overrides bleiben erhalten.

## Confirmation

Konfiguration mit der Tabelle vergleichen und Workflow- sowie Setup-Tests ausführen.

## Revisit when

Der Nutzer andere Defaultpaare festlegt.
