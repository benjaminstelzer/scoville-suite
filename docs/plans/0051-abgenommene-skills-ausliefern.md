---
format_version: 1
id: PLAN-0051
status: active
created: 2026-10-09
updated: 2026-10-09
current_item: W-001
---

# Abgenommene Skills lokal und auf GitHub ausliefern

## Goal

Den abgenommenen Stand aus PLAN-0048 bis PLAN-0050 bauen, zuerst lokal installieren, EMPCO zur sicheren Wiederaufnahme anleiten und danach GitHub-Push und Releases abschließen.

## Non-goals

Keine neue Skillentwicklung, pauschalen Testserien, neuen Viewer-Binaries oder EMPCO-Produktaktionen. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Die Nachricht an den bestehenden EMPCO-Thread ist ausdrücklich beauftragt.

## Work items

### W-001 Abgenommenen Stand ausliefern

Status: in_progress
Depends on: []
Blocked by: []
Decisions: []
Outcome: Lokale Skills und alle geänderten deklarierten GitHub-Ziele enthalten denselben geprüften Stand; EMPCO erhält die sichere Wiederaufnahme-Anleitung.
Acceptance: Releasebuild aus committed Quellen strukturell und gegen seine Quellen verifiziert; Codex-/Claude-Skills bytegleich installiert und persönliche Anpassungen erhalten; EMPCO-Nachricht mit Neuladung und bestätigter Schreiber-Ruhe als Startbedingung zugestellt; alle geänderten deklarierten Ziele gepusht und neue Releases samt benötigten Assets remote verifiziert; ersetzte Releases und Versionstags erst danach entfernt; bestehende passende Windows-/Linux-Nachweise korrekt wiederverwendet und Grenzen benannt.
Instructions: []
Steps:
1. [status: in_progress] Ziele und Änderungen prüfen, Versionen und Changelogs aktualisieren, passende vorhandene Abnahmen zuordnen, Quellen committen und den einzigen Releasebuild verifizieren.
2. [status: todo] Alle vorhandenen lokalen Suite-Skills aktualisieren und verifizieren; dem EMPCO-Thread die Neuladung und sichere Wiederaufnahme am tatsächlichen Stand mitteilen.
3. [status: todo] Parallel zur EMPCO-Wiederaufnahme geänderte Distributionen pushen und releasen; Remote-Dateien, Tags, Assets und anschließende Bereinigung prüfen.
Evidence: PLAN-0049 und PLAN-0050 enthalten technische und Verständnisabnahmen. Aktueller Auslieferungsnachweis: docs/testing/0051-skills-auslieferung.md.
