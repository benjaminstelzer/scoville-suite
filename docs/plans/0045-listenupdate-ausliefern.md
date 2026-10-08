---
format_version: 1
id: PLAN-0045
status: active
created: 2026-10-08
updated: 2026-10-08
current_item: W-001
---

# Listenupdate ausliefern

## Goal

Den abgenommenen Stand aus PLAN-0044 für Codex und Claude lokal installieren, EMPCO zum Neuladen und Fortsetzen auffordern und anschließend die geänderten GitHub-Pakete veröffentlichen.

## Non-goals

Keine zusätzlichen EMPCO-Freigaben oder geänderten Abnahmekriterien. Keine neuen Skillfunktionen oder Wiederholung abgeschlossener Testkampagnen.

## Work items

### W-001 Pakete bauen und lokal installieren

Status: in_progress
Depends on: []
Blocked by: []
Decisions: []
Outcome: Alle lokalen Scoville-Pakete für Codex und Claude enthalten das Update.
Acceptance: Pakete stimmen mit den abgenommenen Quellen überein; passende Runtime-CI besteht. Installierte Dateien stimmen bytegleich mit dem Build überein; persönliche Anpassungen bleiben erhalten.
Instructions: []
Steps:
1. [status: in_progress] Quellen und Versionen sichern, Pakete bauen, überprüfen und installieren.
Evidence: []

### W-002 EMPCO informieren

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: EMPCO erhält den Auftrag, die neuen Skills zu laden und seinen Workflow fortzusetzen.
Acceptance: Nachricht zugestellt; tatsächlicher Ausgang beobachtet und bestehende Freigabegrenzen erhalten.
Instructions: []
Steps:
1. [status: todo] Thread 01a116ce-ac9b-77f0-a6cc-db641fb26f4b über das Update informieren und seine Reaktion beobachten.
Evidence: []

### W-003 GitHub veröffentlichen

Status: todo
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Alle geänderten öffentlichen Distributionsziele enthalten das Update.
Acceptance: Remote-Dateien, annotierte Tags und Release-Assets stimmen mit dem geprüften Stand überein; Sichtbarkeit und Historie bleiben erhalten.
Instructions: []
Steps:
1. [status: todo] Geänderte Manifestziele veröffentlichen, Remote-Ergebnis überprüfen und ersetzte Releases bereinigen.
Evidence: []
