---
format_version: 1
id: PLAN-0051
status: completed
created: 2026-10-09
updated: 2026-10-09
---

# Abgenommene Skills lokal und auf GitHub ausliefern

## Goal

Den abgenommenen Stand aus PLAN-0048 bis PLAN-0050 bauen, zuerst lokal installieren, EMPCO zur sicheren Wiederaufnahme anleiten und danach GitHub-Push und Releases abschließen.

## Non-goals

Keine neue Skillentwicklung, pauschalen Testserien, neuen Viewer-Binaries oder EMPCO-Produktaktionen. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Die Nachricht an den bestehenden EMPCO-Thread ist ausdrücklich beauftragt.

## Work items

### W-001 Abgenommenen Stand ausliefern

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Lokale Skills und alle geänderten deklarierten GitHub-Ziele enthalten denselben geprüften Stand; EMPCO setzt mit neuem Manager am bestätigten Planschritt fort.
Acceptance: Releasebuild aus committed Quellen strukturell und gegen seine Quellen verifiziert; Codex-/Claude-Skills bytegleich installiert und persönliche Anpassungen erhalten; EMPCO-Neuladung und Wiederaufnahme am tatsächlichen Schritt auf Grundlage der ausdrücklichen Nutzerbestätigung zur Worker-Ruhe bestätigt; alle geänderten deklarierten Ziele gepusht und neue Releases samt benötigten Assets remote verifiziert; ersetzte Releases und Versionstags erst danach entfernt; bestehende passende Windows-/Linux-Nachweise korrekt wiederverwendet und Grenzen benannt.
Instructions: []
Steps:
1. [status: done] Ziele und Änderungen prüfen, Versionen und Changelogs aktualisieren, passende vorhandene Abnahmen zuordnen, Quellen committen und den einzigen Releasebuild verifizieren.
2. [status: done] Alle vorhandenen lokalen Suite-Skills aktualisieren und verifizieren; EMPCO nach ausdrücklicher Crash-Recovery-Freigabe beim tatsächlichen verbleibenden Schritt wieder aufnehmen lassen.
3. [status: done] Parallel zur EMPCO-Wiederaufnahme geänderte Distributionen pushen und releasen; Remote-Dateien, Tags, Assets und anschließende Bereinigung prüfen.
Evidence: 320 Builddateien, 13 lokale Installationen und sieben Releases verifiziert; EMPCO-Manager 3 bestätigt W-370/Schritt 3. Nachweis: [Auslieferung](../testing/0051-skills-auslieferung.md).
