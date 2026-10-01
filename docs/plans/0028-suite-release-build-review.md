---
format_version: 1
id: PLAN-0028
status: active
created: 2026-10-01
updated: 2026-10-01
current_item: W-001
---

# Aktualisierte Suiten prüfen, veröffentlichen und installieren

## Goal

Aktuelle Suite- und Einzel-Skill-Builds einschließlich Plan und Viewer mit Astra Medium prüfen, Befunde automatisch korrigieren und im selben Review-Kontext nachprüfen. Erst danach auf GitHub veröffentlichen und die lokalen Codex-/Claude-Installationen ersetzen. ADR-0133 hält den Auftrag und die Grenzen fest.

## Non-goals

Keine neuen Marketplace-Plugins, fremden Repository-Änderungen, lokalen nativen Viewer-Builds oder Ausführung von Scoville Workflow. PLAN-0026 behält seine offene Skilllistenklärung.

## Work items

### W-001 Quellen, Pakete und Viewer bestehen die unabhängige Release-Prüfung

Status: in_progress
Depends on: []
Blocked by: []
Decisions: [ADR-0133]
Outcome: Aktuelle geprüfte Quellen und Builds mit passenden CI-Viewer-Dateien liegen vor.
Acceptance: Astra Medium prüft Build-/Exportwege, alle README-Kompositionen, Stimme, Lesefluss und Release-Anhänge. Bestätigte Befunde sind korrigiert und im selben Astra-Kontext erneut geprüft. Technische Tests, Profil-/Paket-/Quellenprüfungen bestehen. Viewer 1.4.0 kommt ausschließlich aus erfolgreicher Actions-Matrix für alle vier Plattformen, stimmt mit aktuellen Quellen überein und hat geprüfte Checksummen. Der Release-Verbraucher übernimmt die Gate-Ausgabe unverändert. Bekannte Nachweisgrenzen bleiben benannt.
Instructions: []
Steps:
1. [status: done] Astra-Erstreview und Remote-Ausgangszustand sichern.
2. [status: in_progress] Findings korrigieren, Viewer in Actions bauen und die Release-Prüfung mit ihrem echten Verbraucher testen.
3. [status: todo] Vollständige Pakete und README-Varianten bauen, Quellen sichern und Astra im selben Kontext nachprüfen lassen.
Evidence: Vier Erstbefunde, CI-Lauf 36815153138 gestartet. Nachweise unter temp/2026-10-01-suite-release-review im Workspace.

### W-002 GitHub enthält nur geprüfte aktuelle Releases

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0133]
Outcome: Geänderte öffentliche Distributionen sind vollständig veröffentlicht und rückprüfbar.
Acceptance: Vollständiger Tree-Abgleich bewahrt Git-Historie, Sichtbarkeit und Profilgrenzen. Funktional geänderte Ziele bekommen neue zutreffende Versionshinweise, unveränderte keine künstliche Version. Plan und beide Suiten enthalten die identischen zwölf geprüften Viewer-Anhänge direkt. Remote-Dateien und heruntergeladene Release-Anhänge stimmen bytegenau mit dem freigegebenen Build überein. Abgedeckte frühere Releases/Versionstags werden erst nach Sicherung und Abnahme des neuen Releases entfernt.
Instructions: []
Steps:
1. [status: todo] Geprüfte Exporte mit den öffentlichen Trees vergleichen und die Versionen festlegen.
2. [status: todo] Kandidaten veröffentlichen, Release-Anhänge hochladen und Remote-Hashes prüfen.
3. [status: todo] Abgedeckte alte Releases/Versionstags entfernen und Endzustand dokumentieren.
Evidence: []

### W-003 Lokale Codex- und Claude-Suiten stimmen mit dem Release überein

Status: todo
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0133]
Outcome: Beide bestehenden Installationspfade enthalten ihre aktuelle vollständige Suite.
Acceptance: Aktive Leser sind beendet oder der Nutzer hat eine konkrete koordinierte Ausnahme genehmigt. Bestehende Einstellungen und fremde Skills bleiben erhalten, alte Suite-Pakete sind gesichert. Codex hat acht, Claude fünf aktuelle Mitglieder einschließlich Project Context Cleanup. Installationsinventar und Hashes stimmen mit den verifizierten Paketen überein. Feste öffentliche Workspace-Distributionen sind ebenfalls synchron.
Instructions: []
Steps:
1. [status: todo] Schreibruhe prüfen, alte Pakete und Einstellungen sichern.
2. [status: todo] Beide Suiten am bisherigen Installationspfad ersetzen und vollständig rückprüfen.
Evidence: []
