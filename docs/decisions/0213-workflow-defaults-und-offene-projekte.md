---
format_version: 1
id: ADR-0213
status: accepted
created: 2026-10-10
accepted: 2026-10-10
scope: workflow/model-defaults
supersedes: ADR-0140
---

# Vereinbarte Modelle als Defaults und in offenen Projekten verwenden

## Decision

Der Nutzer bestätigt die später vereinbarte Suite-Projektzuordnung als neue Skilldefaults und verlangt dieselbe Zuordnung in allen offenen Projekten:

| Stufe | Umsetzung | Review |
| --- | --- | --- |
| ultra_low | gpt-6-luna / medium | gpt-6-luna / high |
| low | gpt-6.1-sol / low | gpt-6.1-sol / medium |
| medium | gpt-6.1-sol / high | gpt-6.1-sol / high |
| high | gpt-6.1-sol / xhigh | gpt-6-astra / high |
| ultra_high | gpt-6-astra / high | gpt-6-astra / xhigh |

Manager: gpt-6.1-sol / high. Kontextschwellen, Ask-Einstellungen und sonstige Projektwerte bleiben erhalten. Explizite Modellvorgaben und bereits gestartete Rollen werden nicht rückwirkend ersetzt. Bestehende Zugriffsausschlüsse bleiben bindend.

## Problem

Die spätere Projektzuordnung wurde nicht als Paketdefault übernommen. Das Zurücksetzen auf die gebündelten Werte stellte daher die ältere Zuordnung her.

## Confirmation

Workflow besitzt die Defaultquelle; Setup und Distributionen werden daraus gebaut. Aufgelöste Defaultpaare und gespeicherte Einstellungen der ermittelten offenen Projektwurzeln mit den tatsächlichen Verbrauchern prüfen. Bestehenden Paketbuild und lokale Installationspfade nutzen; geprüfte geänderte Distributionen ohne neue Releases veröffentlichen.
