---
format_version: 1
id: PLAN-0043
status: active
current_item: W-001
created: 2026-10-08
updated: 2026-10-08
---

# Abschlussfix ausliefern

## Goal

Die geprüften Korrekturen aus PLAN-0042 lokal installieren, EMPCO zum Neuladen und Fortsetzen auffordern und nach beobachteter Wiederaufnahme veröffentlichen.

## Non-goals

Keine zusätzlichen EMPCO-Freigaben oder Änderungen seiner Abnahmekriterien. Keine neuen Skillfunktionen oder Wiederholung erledigter Testkampagnen.

## Work items

### W-001 Pakete bauen und lokal installieren

Status: in_progress
Depends on: []
Blocked by: []
Decisions: []
Outcome: Codex und Claude verwenden die aktualisierten, eigenständigen Pakete.
Acceptance: Build und Paketstruktur stimmen mit den kanonischen Quellen überein; passende Runtime-CI besteht. Lokale Pakete stimmen bytegleich mit dem Build überein; persönliche Anpassungen bleiben erhalten.
Instructions: []
Steps:
1. [status: in_progress] Quellen und Versionen sichern, Pakete bauen und installieren.
Evidence: []

### W-002 EMPCO neu laden und fortsetzen

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der bestehende EMPCO-Thread nimmt seinen lokalen Auftrag mit aktualisierten Skills wieder auf.
Acceptance: Neuladen und tatsächliche Wiederaufnahme sind im Thread beobachtet; bestehende Freigabegrenzen bleiben erhalten.
Instructions: []
Steps:
1. [status: todo] Autorisierte Nachricht senden und Wiederaufnahme beobachten.
Evidence: []

### W-003 GitHub veröffentlichen

Status: todo
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Alle geänderten öffentlichen Distributionsziele enthalten das Update.
Acceptance: Veröffentlichte Dateien, annotierte Tags und Release-Assets stimmen mit dem geprüften Stand überein; Sichtbarkeit und Historie bleiben erhalten.
Instructions: []
Steps:
1. [status: todo] Geänderte Ziele veröffentlichen und Remote-Ergebnis verifizieren.
Evidence: []
