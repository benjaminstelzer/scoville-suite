---
format_version: 1
id: PLAN-0040
status: completed
created: 2026-10-08
updated: 2026-10-08
---

# Geprüfte Skillklarheit ausliefern

## Goal

Die in PLAN-0039 abgenommenen Korrekturen als konsistente Pakete für Codex und Claude lokal installieren und auf den freigegebenen GitHub-Zielen veröffentlichen. Danach den wartenden EMPCO-Workflow über das Update informieren.

## Non-goals

Keine neue Modelltestkampagne, keine Wiederholung unveränderter Nachweise und keine Änderungen am EMPCO-Projekt. Private Quellen, Einstellungen und fremde Änderungen bleiben geschützt.

## Work items

### W-001 Veröffentlichungsfähige Pakete erzeugen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0204]
Outcome: Die Pakete stammen aus sauberen Quellen und erfüllen die vorhandenen Build- und Runtime-Verträge.
Acceptance: Runtime-CI passt zu Paket- und Testbytes. Profile, benötigte Dateien und Kompatibilitätsangaben stimmen. Unveränderte Viewer-Dateien haben gültige Herkunft. Ein zusätzlicher Nachweis exakt unter Python 3.11 ist nicht erforderlich.
Instructions: []
Steps:
1. [status: done] In suite.json die Veröffentlichungssätze bestimmen, die abgenommenen Quellen sichern und gemeinsame Snapshots sowie README-Projektionen erzeugen. Nutzerrelevante Änderungen versionieren. PLAN-0039-Nachweise übernehmen.
2. [status: done] Den passenden privaten Runtime-CI-Snapshot ausführen. Unter skills/temp/release die vier Profile aktualisieren und erforderliche Paket-, Metadaten-, README- und Viewerprüfungen durchführen. Geänderte Checks auf Windows und Linux ausführen.
Evidence: Quelle dc5c7c5; PLAN-0039 abgenommen. Runtime-CI 37781090182: Windows/Linux/macOS PASS. Vier Profile und 19 Pakete auf Windows/WSL gültig; README und Viewer-Herkunft geprüft.

### W-002 Lokale Skills aktualisieren

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Codex und Claude verwenden die jeweils passenden geprüften Pakete.
Acceptance: Installierte Dateien stimmen vollständig mit dem passenden Build überein. Persönliche Anpassungen und Einstellungen bleiben erhalten. Codex enthält keine manuellen Python-Fallbacks.
Instructions: []
Steps:
1. [status: done] Bestehende Installationen auf lokale Abweichungen prüfen. Codex unter `<Codex home>/skills` und Claude unter `<Claude home>/skills` aktualisieren. Die festen öffentlichen Suiteverzeichnisse aus geprüften Exporten synchronisieren.
2. [status: done] Dateibestand und Bytes der Installationen mit den Paketen vergleichen und die tatsächliche lokale Verfügbarkeit prüfen.
Evidence: Acht Codex- und fünf Claude-Skills bytegleich in den Hostverzeichnissen verfügbar. Keine lokalen Abweichungen; Einstellungen erhalten. Öffentliche Verzeichnisse exportgleich; Laden im nächsten Turn.

### W-003 GitHub-Update veröffentlichen

Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: []
Outcome: Alle geänderten freigegebenen Distributionen sind veröffentlicht und besitzen einen verifizierten aktuellen Release.
Acceptance: Remote-Dateien, Sichtbarkeit, Commit, Tag und Assets stimmen mit dem jeweiligen Kandidaten überein. Erforderliche Viewer-Anhänge stehen direkt an Plan und beiden Suiten. Pro aktualisiertem Ziel bleibt ein aktueller Release samt Versionstag erhalten.
Instructions: []
Steps:
1. [status: done] Die vollständigen geänderten Manifestziele über ihre normalen Branches veröffentlichen. Bestehende Historie bewahren, Releasekopie aus CHANGELOG und gebauter README erzeugen, Assets und Checksummen anhängen.
2. [status: done] Remote-Zustand prüfen, danach ersetzte Releases und Versionstags sowie ersetzte Stagingarchive entfernen. Unveränderte Ziele nicht erneut veröffentlichen.
Evidence: Sieben Repos: Remote-Bestände, Tags und Anhänge stimmen; Publikationsaudits PASS. Viewer direkt an Plan und beiden Suiten. Je ein Release/Tag; ersetzte Stagingarchive entfernt.

### W-004 EMPCO über das fertige Update informieren

Status: done
Depends on: [W-002, W-003]
Blocked by: []
Decisions: []
Outcome: Der wartende EMPCO-Workflow erhält die Information zum abgeschlossenen Skillupdate und zur Fortsetzung.
Acceptance: Der bekannte Workflowthread erhält die Aufforderung, die neuen lokalen Skills vollständig zu laden und die autorisierte Arbeit fortzusetzen. Kein Eingriff in seine Projektdateien.
Instructions: []
Steps:
1. [status: done] Den Zustand von Thread 01a116ce-ac9b-77f0-a6cc-db641fb26f4b lesen und nach erfolgreicher Auslieferung die vom Nutzer beauftragte Update-/Fortsetzungsnachricht senden.
Evidence: EMPCO war idle am sicheren Stopp; Thread 01a116ce-ac9b-77f0-a6cc-db641fb26f4b erhielt Update- und Fortsetzungsauftrag. Neuladen und bestehende Übernahmegates ausdrücklich benannt.
