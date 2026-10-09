---
format_version: 1
id: PLAN-0053
status: active
created: 2026-10-09
updated: 2026-10-09
current_item: W-003
---

# Kurzen Workflow-Abschluss ausliefern und neuen EMPCO-Lauf beobachten

## Goal

Den Workflow-Abschluss auf eine knappe Zusammenfassung mit Reportlink umstellen, lokal und auf GitHub ausliefern und die Anwendung im neu gestarteten EMPCO-Lauf alle fünf Minuten beobachten.

## Non-goals

Keine EMPCO-Projektänderungen, Tests, Stopps oder Nachrichten an dessen Kinder. Nur die beauftragten Runner-Nachrichten zur Änderung und Neuladung. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Keine allgemeinen Fortschrittsmeldungen aus der Beobachtung. Neue Befunde zunächst sammeln, keine automatischen Skillfixes oder Releases.

## Work items

### W-001 Abschlussvorgabe ausliefern

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der geprüfte Build enthält die kurze Abschlussvorgabe, ist lokal installiert und auf geänderten GitHub-Zielen veröffentlicht; der neue EMPCO-Runner kennt die Änderung.
Acceptance: Abschluss nennt knapp den tatsächlich erledigten Umfang und wichtige offene Grenzen mit klickbarem Reportlink; vollständiger Reportread, Quieszenz und unmittelbare Problemweitergabe bleiben erhalten; alle Manifestziele verglichen, nur geänderte veröffentlicht; lokale Pakete und Remote-Dateien entsprechen dem Build; neue Releases, Tags und notwendige Assets verifiziert.
Instructions: []
Steps:
1. [status: done] Abschlussregeln in Workflow-SKILL.md und references/run-feedback.md prüfen, passende Changelogversion eintragen und Quellen committen. Bestehende Abschlusseinträge von PLAN-0052 erhalten.
2. [status: done] Einzigen Build unter skills/temp/release aktualisieren, betroffene Paketprojektionen und Metadaten prüfen, unveränderte Laufzeit- und Viewer-Nachweise wiederverwenden und lokale Installationen aktualisieren.
3. [status: done] Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5 auf Host local zur Neuladung informieren, geänderte Distributionen pushen und Releases veröffentlichen. Remote-Bytes und Assets vor Ersatzrelease-Bereinigung prüfen.
Evidence: 13 Skills bytegleich; Runner informiert. v2.4.11 / 112f698 mit Dateien und 14 Assets verifiziert; ein Release/Tag. Details: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-003 Neuen Lauf von alter Übernahme unterscheiden

Status: in_progress
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der neue EMPCO-Lauf setzt nach geklärter Startup-Sperre fort; die ausgelieferte Skillvorgabe verhindert pauschale rückwirkende Agentnachweise.
Acceptance: Neue Aktivierung verlangt keine alten Agent-IDs oder Abschaltnachweise; konkrete konkurrierende Writer und Same-run-Recovery bleiben abgesichert; Runner erhält Nutzerkorrektur und lokalen Reloadstand; neuer Build, lokale Pakete, Push und Release verifiziert.
Instructions: []
Steps:
1. [status: done] Tatsächlichen Runnerstart und eingefügten Auftrag prüfen, Ursache belegen und Nutzerkorrektur an denselben Runner zur Fortsetzung übermitteln.
2. [status: in_progress] Neue Aktivierung und Same-run-Recovery in Workflow-SKILL.md und references/operations.md knapp unterscheiden, Folgen prüfen und Quellen committen.
3. [status: todo] Neuen Build unter skills/temp/release verifizieren, lokal aktualisieren und Reloadnachricht zustellen; geänderte GitHub-Ziele pushen und passendes neues Release samt Assets prüfen.
Evidence: Startup-Sperre auf Nutzerkorrektur aufgehoben; W-386/step-1 gemeldet. Ursache und Grenze: [Befunde](../testing/0053-empco-abschluss-befunde.md).

### W-002 Anwendung im neuen Lauf beobachten

Status: todo
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Neue bestätigte Scoville-Defekte und wiederholte Anwendungsfehler sind mit Ursache, kleinstem Fixvorschlag und Sichtbarkeitsgrenze dokumentiert.
Acceptance: Tatsächliche Aktionen des benannten neuen Laufs einschließlich Rollen, geladener Regeln, Übergaben, Reviews, zielgerechter Checks und Planfortschritt geprüft; neue relevante Befunde durch Ask mit Sol 6.1/high bewertet; Nutzer nur bei neuen bestätigten Ablauffehlern, notwendiger Entscheidung, Beobachtungsfehler oder Abschluss informiert; bei Laufende oder Nutzerstopp Schlussbewertung und Automation gelöscht.
Instructions: []
Steps:
1. [status: todo] Automation alle fünf Minuten für Thread 01a120d7-5fcf-7122-b741-76eb3a203fc5 einrichten. Erstes Fenster ab Startturn 01a120d7-6328-79c3-bc8e-adf922ea306e tatsächlich prüfen; danach nur neue relevante Ereignisse. Aktuellen Stand unter temp/2026-10-09-empco-abschluss-beobachtung/state.json überschreiben.
2. [status: todo] Neue relevante Befunde gebündelt über Scoville Ask beurteilen und knapp in docs/testing/0053-empco-abschluss-befunde.md erfassen. Ohne neue Befunde keine Konsultation oder Planänderung.
3. [status: todo] Nur diesen Lauf bis Ende oder Nutzerstopp beobachten, tatsächlich geprüften Umfang abschließend bewerten und Automation löschen.
Evidence: []
