---
format_version: 1
id: ADR-0003
status: accepted
created: 2026-09-21
accepted: 2026-09-21
scope: suite/evaluation-model
supersedes: ADR-0002
---

# Rückkehr zu LUNA über Codex CLI

## Decision

Der Nutzer ersetzt Gemini über Antigravity durch `gpt-5.6-luna` mit `medium` über Codex CLI. SOL Medium bleibt Testkoordinator; der Autor prüft die Ergebnisse.

## Problem

Der Gemini-Test stoppte nach einem verweigerten Shell-Aufruf; sein Transport garantiert keine toolfreie Ausführung.

## Drivers

- Der Nutzer lehnt einen Gemini-API-Wechsel ab und verlangt Codex CLI.
- Die ursprüngliche Verständlichkeitsanforderung zielt auf LUNA.

## Considered alternatives

- Codex CLI: gewählter Zugang; Toolgrenzen vor neuen Tests prüfen.
- Gemini API: vom Nutzer abgelehnt; keine Einrichtung oder Zugangsbeschaffung.
- Antigravity CLI: gestoppt; Ergebnisse bleiben historische Evidenz.

## Consequences

- Die 300 Aufgaben und Soll-Ergebnisse bleiben unverändert; gebaute Pakete werden erneut mit LUNA geprüft.
- Frühere Gemini-Erfolge ersetzen keine LUNA-Tests. Abgebrochene Testpunkte bleiben erhalten.
- Keine globalen Rechteänderungen, automatische Toolfreigaben oder Veröffentlichung. CLI-Anmeldung ist kein Nachweis sicherer Ausführung.

## Confirmation

1. Prüfe vorhandene CLI und tatsächliche Toolgrenzen vor einem begrenzten Piloten.
2. Belege natives Modell und Effort sowie aktuelle Paket-Hashes je Testlauf.
3. Bestätige vollständige fehlerfreie Fallabdeckung durch SOL und Autor vor einer separat autorisierten Veröffentlichung.

## Revisit when

LUNA Medium ist nicht verfügbar oder sichere CLI-Testgrenzen lassen sich nicht nachweisen.
