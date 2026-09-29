---
format_version: 1
id: PLAN-0022
status: completed
created: 2026-09-29
updated: 2026-09-29
---

# Geprüfte Helper- und Workflow-Änderungen veröffentlichen

## Goal

Die vom Nutzer beauftragten offenen Commit-/Push-/Release-Schritte für den
abgeschlossenen Stand aus PLAN-0020/0021 durchführen und remote verifizieren.

## Non-goals

PLAN-0019 bleibt draft. Kein eigenständiges Workflow-Repository, keine Änderung
der Sichtbarkeit, keine neue Viewer-Version, keine Veröffentlichung fremder Arbeit.

## Work items

### W-001 Release-Kandidat und Zielmenge sind geprüft

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0118]
Outcome: Kanonische Quellen, Versionen, Testnachweise und unveränderte Viewer-Assets sind publikationsbereit.
Acceptance: Manifest-Ziele und Remote-Zustand erfasst. Geänderte Pakete geprüft, Nutzerwahl Luna 6 High beibehalten, Testergebnisse und Grenzen dokumentiert. Changelogs nennen tatsächliche Änderungen; sauberer Source-Commit und profilgetrennte Exporte liegen vor.
Steps:
1. Ziele, Releasehistorie und Asset-Provenienz prüfen.
2. Versionsangaben und Nachweise ergänzen, gültige Pakete aus committed Quellen bauen.
Evidence: fa6a684; vier Build-Varianten validiert. Release-Inventar, Viewer-Provenienz und Tests unter temp/2026-09-29-suite-release und docs/plan0021-evidence.md.

### W-002 Betroffene Ziele sind veröffentlicht und verifiziert

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Geänderte autorisierte Distributionen liegen mit korrekten Releases auf GitHub.
Acceptance: Remote-Trees entsprechen Exporten; Tags, Release-Inhalte, heruntergeladene Assets und Sichtbarkeit geprüft. Unveränderte Ziele übersprungen. Fixed public projections entsprechen den Exporten. Alte Release-Artefakte erst nach gesichertem Ersatz gemäß Release-Vertrag bereinigt.
Steps:
1. Distributionen committen/pushen und annotierte Tags mit Releases erzeugen.
2. Remote-Bytes und Assets prüfen, vorhandene Releasehistorie sichern und finalen Zustand dokumentieren.
Evidence: docs/plan0022-release-evidence.md: vier Releases und Remote-Assets verifiziert; lokale Codex-/Claude-Skills und public-Projektionen synchronisiert.
