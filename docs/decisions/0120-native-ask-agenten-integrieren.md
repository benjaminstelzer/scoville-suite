---
format_version: 1
id: ADR-0120
status: accepted
created: 2026-09-30
accepted: 2026-09-30
scope: ask/native-route
supersedes: ADR-0085
---

# Native Ask-Berater als Agenten integrieren

## Decision

Der Nutzer beauftragt die Integration der überarbeiteten Ask-Version in die
kanonische Suite und den aktuellen Build. Native Codex-Berater laufen als
unabhängige, lesende Subagenten mit frischem Kontext und dem konfigurierten
Modell und Effort. Rückfragen und Folgeaufträge behalten den exakten Handle.
Der Caller sammelt vollständige Antworten und meldet fehlende Ergebnisse.
Unbekannte Kapazität oder ein unklarer Start erlauben keinen Ersatzspawn.

Separate Codex-Berater-Chats, Titel, Pinning und Archivierung entfallen.
Bestehende Pin-Werte bleiben lesbar und wirkungslos. Neue Änderungen werden
von Setup abgewiesen. Die Claude-CLI-Route und unmittelbar brauchbare
Helper-Ausgaben bleiben erhalten. Die Hostgrenzen gelten weiter.

## Problem

ADR-0085 schreibt eine native Chat-Route vor, die der beauftragten neuen
Implementierung widerspricht.

## Drivers

- Ausdrücklicher Integrationsauftrag und bestätigtes Astra-Medium-Review.
- Bestehende Nutzerarbeit, Einstellungen und Quellhistorie erhalten.

## Considered alternatives

- Alte Chat-Route weiter ausliefern: widerspricht dem Integrationsauftrag.

## Consequences

Ask braucht native Zusammenarbeit und verfügbare Agentenkapazität. Der
lesende Auftrag ist keine vom Host erzwungene Schreibsperre. Die Integration
erteilt keine Veröffentlichungsgenehmigung.

## Confirmation

Ask-, Setup-, Shared- und Paketprüfungen sowie vorhandene reale Beratungs-
und Folgefragen auswerten. Beobachtete Modelltelemetrie getrennt angeben.

## Revisit when

Der Host ändert Agentenkapazität, Rückgaben oder Fortsetzung.
