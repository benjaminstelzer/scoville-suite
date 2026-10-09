---
format_version: 1
id: PLAN-0053
status: active
created: 2026-10-09
updated: 2026-10-09
current_item: W-005
---

# Kurzen Workflow-Abschluss ausliefern und neuen EMPCO-Lauf beobachten

## Goal

Den kurzen Workflow-Abschluss ausliefern, seine Anwendung beobachten und die ausdrücklich beauftragten offenen Skillfixes gegen Informationsverlust und doppelte Arbeit umsetzen.

## Non-goals

Keine EMPCO-Projektänderungen, Tests, Stopps oder Nachrichten an dessen Kinder. Nur die beauftragten Runner-Nachrichten zur Änderung und Neuladung. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Keine allgemeinen Fortschrittsmeldungen aus der Beobachtung. Keine automatischen Skillfixes oder Releases aus Beobachtungsbefunden.

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

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der neue EMPCO-Lauf setzt nach geklärter Startup-Sperre fort; die ausgelieferte Skillvorgabe verhindert pauschale rückwirkende Agentnachweise.
Acceptance: Neue Aktivierung verlangt keine alten Agent-IDs oder Abschaltnachweise; konkrete konkurrierende Writer und Same-run-Recovery bleiben abgesichert; Runner erhält Nutzerkorrektur und lokalen Reloadstand; neuer Build, lokale Pakete, Push und Release verifiziert.
Instructions: []
Steps:
1. [status: done] Tatsächlichen Runnerstart und eingefügten Auftrag prüfen, Ursache belegen und Nutzerkorrektur an denselben Runner zur Fortsetzung übermitteln.
2. [status: done] Neue Aktivierung und Same-run-Recovery in Workflow-SKILL.md und references/operations.md knapp unterscheiden, Folgen prüfen und Quellen committen.
3. [status: done] Neuen Build unter skills/temp/release verifizieren, lokal aktualisieren und Reloadnachricht zustellen; geänderte GitHub-Ziele pushen und passendes neues Release samt Assets prüfen.
Evidence: Workerstart belegt; 13 lokale Skills aktualisiert, Reload zugestellt. v2.4.12 / 9162fda samt 14 Assets verifiziert: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-002 Anwendung im neuen Lauf beobachten

Status: paused
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Neue bestätigte Scoville-Defekte und wiederholte Anwendungsfehler sind mit Ursache, kleinstem Fixvorschlag und Sichtbarkeitsgrenze dokumentiert.
Acceptance: Tatsächliche Aktionen des benannten neuen Laufs einschließlich Rollen, geladener Regeln, Übergaben, Reviews, zielgerechter Checks und Planfortschritt geprüft; neue relevante Befunde durch Ask mit Sol 6.1/high bewertet; Nutzer nur bei neuen bestätigten Ablauffehlern, notwendiger Entscheidung, Beobachtungsfehler oder Abschluss informiert; bei Laufende oder Nutzerstopp Schlussbewertung und Automation gelöscht.
Instructions: Beobachtung während der ausdrücklich beauftragten Auslieferung pausieren; danach W-002 fortsetzen.
Steps:
1. [status: done] Automation alle fünf Minuten für Thread 01a120d7-5fcf-7122-b741-76eb3a203fc5 einrichten. Erstes Fenster ab Startturn 01a120d7-6328-79c3-bc8e-adf922ea306e tatsächlich prüfen; danach nur neue relevante Ereignisse. Aktuellen Stand unter temp/2026-10-09-empco-abschluss-beobachtung/state.json überschreiben.
2. [status: in_progress] Neue relevante Befunde gebündelt über Scoville Ask beurteilen und knapp in docs/testing/0053-empco-abschluss-befunde.md erfassen. Ohne neue Befunde keine Konsultation oder Planänderung.
3. [status: todo] Nur diesen Lauf bis Ende oder Nutzerstopp beobachten, tatsächlich geprüften Umfang abschließend bewerten und Automation löschen.
Evidence: Vier Anwendungsfehler geprüft; Quellenfixes abgenommen. Kein weiterer Ritualbefund. Wirkung und Auslieferung offen: [Befunde](../testing/0053-empco-abschluss-befunde.md).

### W-004 Offene Skillfixes und Wiederverwendung umsetzen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die offenen Klarstellungen verlangen Wiederverwendung unveränderter Ergebnisse und erhalten vollständige Prozessinformationen, Reader-Aufrufe und begründete Prüfgrenzen; ihre praktische Wirkung bleibt ungeprüft.
Acceptance: Sol 6.1/high und Opus 5.5/high haben den gemeinsamen Entwurf und die Änderungen geprüft; erfolgreiche unveränderte Checks und Reviews werden wiederverwendet, notwendige neue Nachweise bleiben erhalten; kanonische Quellen und generierte Kopien stimmen überein; relevante Checks bestehen, ungeprüfte Wirkung ist benannt.
Instructions: Kein neuer Releaseauftrag.
Steps:
1. [status: done] Bestehende Reviewer zu Wiederverwendung und den drei offenen Konsensfixes konsultieren und ihre Ergebnisse austauschen.
2. [status: done] Code validation.md und SKILL.md sowie shared/runtime/native_output.md, document_reader.md und native_task_arguments.py gezielt ändern; betroffene Kopien aus kanonischen Quellen erzeugen.
3. [status: done] Betroffene Struktur und Reader-Ausgabe prüfen; Änderungen von denselben Reviewern gegenprüfen und offene Grenzen knapp im Befundbericht aktualisieren.
Evidence: Sol/Opus nehmen Patch an; Sync und Reader-Test bestehen. Validatorgrenze, Luna-Wirkung und Auslieferung: [Befunde](../testing/0053-empco-abschluss-befunde.md).

### W-005 Abgenommene Skillfixes ausliefern

Status: in_progress
Depends on: [W-004]
Blocked by: []
Decisions: []
Outcome: Die abgenommenen Fixes sind gebaut, lokal installiert und auf den geänderten GitHub-Zielen veröffentlicht.
Acceptance: Quellen und Paketprojektionen stimmen überein; lokale Skills entsprechen dem Build bei erhaltenen Einstellungen; alle manifestierten Ziele verglichen, geänderte mit passender Version veröffentlicht; Remote-Bäume, Tags und erforderliche Assets verifiziert. Keine ungetestete Luna- oder Live-Wirkung behauptet.
Instructions: []
Steps:
1. [status: in_progress] Quellen und Versionsnotizen committen, einzigen Releasebuild aktualisieren und betroffene Paket-/Kompatibilitätsgrenzen prüfen; unveränderte Runtime- und Viewer-Nachweise wiederverwenden.
2. [status: todo] Lokale Codex-/Claude-Skills aus geprüften Paketen aktualisieren und bytegleich prüfen, persönliche Einstellungen erhalten.
3. [status: todo] Geänderte manifestierte GitHub-Ziele pushen und Releases mit passenden Assets veröffentlichen; Remote-Bytes und Ersatzreleases vor Bereinigung prüfen.
Evidence: []
