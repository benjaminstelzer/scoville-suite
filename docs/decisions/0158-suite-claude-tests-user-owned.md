---
format_version: 1
id: ADR-0158
status: superseded
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
superseded_by: ADR-0159
---

# Claude-Testausführung liegt beim Nutzer

## Decision

Der Nutzer testet Claude später unabhängig in Claude selbst. Dieser Codex-Auftrag
führt keine Claude-Testläufe aus. Die passenden Cases und Erwartungen bleiben
für die externe Prüfung erhalten; Modell und Laufbudget werden hier nicht gewählt.

## Problem

Die bisherige Planung sah auch eine agentenseitig ausgeführte Claude-Teststrecke vor.

## Drivers

Ausdrückliche Nutzeranweisung vom 04.10.2026.

## Considered alternatives

Claude über diesen Codex-Auftrag testen widerspricht der gewählten unabhängigen Prüfung.

## Consequences

Codex- und externe Claude-Nachweise werden getrennt geführt. Fehlende externe
Ergebnisse bleiben unverifiziert und erlauben keine vollständige gemeinsame
Abnahme. Lokale Paket-, Daten- und Helper-Tests sind keine Claude-Modellläufe.
Die beauftragten Astra-Reviews und der Umsetzungsstopp vor W-001 bleiben bestehen.

## Confirmation

Keine Claude-Modellläufe durch diesen Auftrag; externe Ergebnisse nennen bei
späterer Übernahme ihren geprüften Paketstand, Cases, Modell, Effort und Grenzen.

## Revisit when

Der Nutzer die Zuständigkeit oder die gemeinsame Abnahme ändert.
