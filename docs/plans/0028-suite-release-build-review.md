---
format_version: 1
id: PLAN-0028
status: draft
created: 2026-10-01
updated: 2026-10-01
---

# Aktualisierte Suiten prüfen, veröffentlichen und installieren

## Goal

Aktuelle Suite- und Einzel-Skill-Builds einschließlich Plan und Viewer mit Astra Medium prüfen, Befunde automatisch korrigieren und im selben Review-Kontext nachprüfen. Die ergänzten Planpflege-, Viewer- und Workflow-Regeln umsetzen. Danach zuerst lokale Codex-/Claude-Skills aktualisieren und die laufenden Empco-/Fluid-Base-Sessions informieren; GitHub-Releases zuletzt. ADR-0133 hält den ursprünglichen Auftrag und die Grenzen fest.

## Non-goals

Keine neuen Marketplace-Plugins, fremden Repository-Änderungen, lokalen nativen Viewer-Builds oder Ausführung von Scoville Workflow. PLAN-0026 behält seine offene Skilllistenklärung.

## Work items

### W-001 Quellen, Pakete und Viewer bestehen die unabhängige Release-Prüfung

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0133]
Outcome: Aktuelle geprüfte Quellen und Builds mit passenden CI-Viewer-Dateien liegen vor.
Acceptance: Astra Medium prüft Build-/Exportwege, alle README-Kompositionen, Stimme, Lesefluss und Release-Anhänge. Bestätigte Befunde sind korrigiert und im selben Astra-Kontext erneut geprüft. Technische Tests, Profil-/Paket-/Quellenprüfungen bestehen. Viewer 1.4.0 kommt ausschließlich aus erfolgreicher Actions-Matrix für alle vier Plattformen, stimmt mit aktuellen Quellen überein und hat geprüfte Checksummen. Der Release-Verbraucher übernimmt die Gate-Ausgabe unverändert. Bekannte Nachweisgrenzen bleiben benannt.
Instructions: []
Steps:
1. [status: done] Astra-Erstreview und Remote-Ausgangszustand sichern.
2. [status: done] Findings korrigieren, Viewer in Actions bauen und die Release-Prüfung mit ihrem echten Verbraucher testen.
3. [status: done] Vollständige Pakete und README-Varianten bauen, Quellen sichern und Astra im selben Kontext nachprüfen lassen.
Evidence: Astra Medium bestätigt Korrekturen im selben Kontext. 286 technische Tests, vier CI-Plattformen und alle Release-Gates bestanden. Nachweise: temp/2026-10-01-suite-release-review/report.md.

### W-002 GitHub enthält nur geprüfte aktuelle Releases

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0133]
Outcome: Geänderte öffentliche Distributionen sind vollständig veröffentlicht und rückprüfbar.
Acceptance: Vollständiger Tree-Abgleich bewahrt Git-Historie, Sichtbarkeit und Profilgrenzen. Funktional geänderte Ziele bekommen neue zutreffende Versionshinweise, unveränderte keine künstliche Version. Plan und beide Suiten enthalten die identischen zwölf geprüften Viewer-Anhänge direkt. Remote-Dateien und heruntergeladene Release-Anhänge stimmen bytegenau mit dem freigegebenen Build überein. Abgedeckte frühere Releases/Versionstags werden erst nach Sicherung und Abnahme des neuen Releases entfernt.
Instructions: []
Steps:
1. [status: done] Geprüfte Exporte mit den öffentlichen Trees vergleichen und die Versionen festlegen.
2. [status: done] Kandidaten veröffentlichen, Release-Anhänge hochladen und Remote-Hashes prüfen.
3. [status: done] Abgedeckte alte Releases/Versionstags entfernen und Endzustand dokumentieren.
Evidence: Sieben Remote-Audits bestanden. Zwölf abgelöste Releases/Tags entfernt. Aktuelle Pakete und Viewer-Hashes geprüft. Nachweise: temp/2026-10-01-suite-release-review/remote-audit-final.json.

### W-003 Lokale Codex- und Claude-Suiten stimmen mit dem Release überein

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0133]
Outcome: Beide bestehenden Installationspfade enthalten ihre aktuelle vollständige Suite.
Acceptance: Aktive Leser sind beendet oder der Nutzer hat eine konkrete koordinierte Ausnahme genehmigt. Bestehende Einstellungen und fremde Skills bleiben erhalten, alte Suite-Pakete sind gesichert. Codex hat acht, Claude fünf aktuelle Mitglieder einschließlich Project Context Cleanup. Installationsinventar und Hashes stimmen mit den verifizierten Paketen überein. Feste öffentliche Workspace-Distributionen sind ebenfalls synchron.
Instructions: []
Steps:
1. [status: done] Schreibruhe prüfen, alte Pakete und Einstellungen sichern.
2. [status: done] Beide Suiten am bisherigen Installationspfad ersetzen und vollständig rückprüfen.
Evidence: Alle 8 Codex-/5 Claude-Mitglieder hashgeprüft; öffentliche Kopien synchron. Empco und Fluid Base informiert. temp/2026-10-01-workflow-plan-state/installation-final.json.

### W-004 Ergänzte Plan- und Workflow-Regeln sind umgesetzt und geprüft

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0133]
Outcome: Skills und Viewer zeigen den tatsächlichen Arbeitsstand und verhindern Namenskollisionen ohne Nutzerfrage.
Acceptance: Plan bleibt standalone. Vor Schreibfreigabe sind Work Item und tatsächlich gestartete Steps gespeichert; sequenzielle Übergänge, Pausen, Wiederaufnahme und Nachfolger bleiben konsistent. Viewer bietet jeden Work-Status einschließlich Paused und Cancelled. Der Runner nennt seinen Chat SC-WFL PLAN-xxxx. Neue native Agenten erhalten automatisch eindeutige Namen; bekannte Kapazitätswiederholungen behalten identische Argumente, unklare Starts bleiben gesperrt. Astra Medium bestätigt die Korrekturen im selben Review-Kontext. Tests und verifizierte öffentliche Pakete bestehen; Viewer 1.4.1 stammt aus erfolgreicher Vier-Plattform-CI.
Instructions: []
Steps:
1. [status: done] Planpflege und sequenzielle Step-Grenzen implementieren und mit Astra prüfen.
2. [status: done] Viewer-Statusauswahl ergänzen, Frontend prüfen und native Downloads in CI bauen.
3. [status: done] Runner-Titel und eindeutige Agentennamen implementieren, Regression prüfen und Astra-Findings korrigieren.
4. [status: done] Geprüfte Quellen sichern und alle betroffenen Suite-/Einzelpakete neu bauen.
Evidence: Astra bestätigt alle drei Ergänzungen. Workflow 50 Tests bestanden; Viewer-CI 36856214450 erfolgreich. Weitere Nachweise: temp/2026-10-01-workflow-plan-state/report.md.

### W-005 Neue Skill-Releases folgen der lokalen Aktualisierung

Status: paused
Depends on: [W-003, W-004]
Blocked by: []
Decisions: [ADR-0133]
Outcome: Plan und beide Suiten enthalten öffentlich die lokal installierten, geprüften Änderungen.
Acceptance: Nur funktional geänderte Ziele erhalten neue Versionen. Vollständige Remote-Trees sowie Uploadstatus, Namen, Größen und GitHub-SHA-256-Digests entsprechen den freigegebenen Paketen. Release-Anhänge werden nach dem Upload nie erneut heruntergeladen; die Regel steht in AGENTS.md und gilt für Entwürfe und Endaudit. Alle drei Releases enthalten dieselben geprüften Viewer-1.4.1-Downloads. Abgelöste Releases und Versionstags werden erst nach Sicherung und Abnahme entfernt. Workflow bleibt ausschließlich Mitglied der öffentlichen Codex-Suite.
Instructions: []
Steps:
1. [status: done] Freigegebene Kandidaten und Viewer-Provenienz vor Veröffentlichung prüfen.
2. [status: in_progress] Drei Releases veröffentlichen und Remote-Inhalte vollständig rückprüfen.
3. [status: todo] Abgelöste Releases bereinigen und Plan samt Projektstatus abschließen.
Evidence: []

### W-006 Externe Reviews begründen einen geprüften Fixplan

Status: paused
Depends on: []
Blocked by: []
Decisions: [ADR-0133]
Outcome: Bestätigte Fehler sind korrigiert; begründete weitere Änderungen haben klare Planpunkte statt ungeprüfter Übernahme externer Vorschläge.
Acceptance: Zwei unabhängige Astra-High-Berater prüfen W1-W6 des Workflow-/Plan-Reviews und A1-A4 des Ask-Reviews gegen aktuelle Quellen, Testnachweise und verbindliche Nutzeranforderungen. Release-Schritte bleiben ausdrücklich ausgeschlossen. Befunde nennen Folge, Nachweisgrenze und kleinste Korrektur. Bestätigte Fehler werden automatisch behoben und im selben Review-Kontext nachgeprüft; erforderliche größere Änderungen erhalten eigenständige Outcomes und Acceptance. Änderungen an Runtime-Paketen werden vor Veröffentlichung gebaut, geprüft, lokal aktualisiert und den autorisierten laufenden Sessions mitgeteilt.
Instructions: After PLAN-0029 completes, resume PLAN-0028 W-006/step-3, then W-005/step-2.
Steps:
1. [status: done] Externen Review mit Astra High gegen Quellen und Nachweise prüfen.
2. [status: done] Aus beiden Antworten PLAN-0029 erstellen und separat mit Astra High prüfen.
3. [status: in_progress] Plan-Findings korrigieren und den freigegebenen Umsetzungsstand festhalten.
Evidence: Auftrag ergänzt: Astra High, keine Release-Prüfung. Quelle: Nutzeranhang Eingefügter Text.txt. Nachweise: temp/2026-10-01-workflow-plan-state/external-review-question.txt.
