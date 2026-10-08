---
format_version: 1
id: PLAN-0043
status: completed
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

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Codex und Claude verwenden die aktualisierten, eigenständigen Pakete.
Acceptance: Build und Paketstruktur stimmen mit den kanonischen Quellen überein; passende Runtime-CI besteht. Lokale Pakete stimmen bytegleich mit dem Build überein; persönliche Anpassungen bleiben erhalten.
Instructions: []
Steps:
1. [status: done] Quellen und Versionen sichern, Pakete bauen und installieren.
2. [status: done] Sol 6.1/high und Astra/high prüfen die finalen generierten Skills vor der erneuten lokalen Installation.
Evidence: [Shared-Testvergleich; Readertext und Ask-Lieferausnahme korrigiert. Windows/Linux-Nachtests und Runtime-CI 37798132556 bestanden., Sol 6.1/high und Astra/high prüften den finalen Stand ohne relevante Findings. Alle acht Codex- und fünf Claude-Pakete bytegleich installiert; persönliche Einstellungen erhalten.]

### W-002 EMPCO neu laden und fortsetzen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der bestehende EMPCO-Thread nimmt seinen lokalen Auftrag mit aktualisierten Skills wieder auf.
Acceptance: Neuladen und tatsächliche Wiederaufnahme sind im Thread beobachtet; bestehende Freigabegrenzen bleiben erhalten.
Instructions: []
Steps:
1. [status: done] Autorisierte Nachricht senden und Wiederaufnahme beobachten.
Evidence: [Neuladen und Managerstart bestätigt: 01a11c1b-0e01-7583-a22a-8b630c392ed5. Sol 6.1/medium; bestehende Remote-Sperren und Abnahmekriterien erhalten.]

### W-003 GitHub veröffentlichen

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Alle geänderten öffentlichen Distributionsziele enthalten das Update.
Acceptance: Veröffentlichte Dateien, annotierte Tags und Release-Assets stimmen mit dem geprüften Stand überein; Sichtbarkeit und Historie bleiben erhalten.
Instructions: []
Steps:
1. [status: done] Geänderte Ziele veröffentlichen und Remote-Ergebnis verifizieren.
Evidence: [Sieben Releases veröffentlicht; Remote-Dateien und annotierte Tags sowie alle Asset-Prüfsummen verifiziert. Suite 2.4.5; Codex-Suite 2.4.6. Vorversionen und alte Staging-Archive entfernt.]
