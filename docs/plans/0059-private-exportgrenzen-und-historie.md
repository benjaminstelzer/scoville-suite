---
format_version: 1
id: PLAN-0059
status: cancelled
created: 2026-10-29
updated: 2026-10-29
---

# Private Exportgrenzen und bereinigte Veröffentlichung

## Goal

Die zwei freigegebenen Nachträge zu PLAN-0058 korrigieren und geschützte private Projektnamen aus öffentlichen Exporten sowie erreichbarer Veröffentlichungshistorie entfernen. Aktuelle Skills und ihre notwendigen Referenzen, Helper, Tests und Buildquellen bleiben vollständig. Veraltete lokale Berichte werden entfernt; noch vorhandene Dateien gehen auf ausdrücklichen Nutzerwunsch nach Desktop/_delete. Keine zusätzlichen Backups. Die private Bestandsaufnahme wird nicht verlinkt oder exportiert. ADR-0226 ergänzt die öffentliche Recordregel von ADR-0225.

Quellenkorrektur, accountweite öffentliche Bestandsaufnahme, lokale Bereinigungskandidaten sind autorisiert. Vor Veröffentlichung, Force-Push und Tagänderungen werden konkrete Diffs, Prüfergebnisse, alte/neue Referenzen und Folgen zur ausdrücklichen Freigabe vorgelegt. Nur main veröffentlichen; vorhandene Tags ausschließlich nach eigener Freigabe behandeln.

## Non-goals

- PLAN-0058 nicht wieder öffnen; nur den ausdrücklich genehmigten Berichtsnachtrag ergänzen.
- Keine Installation, Modelltests, neuen Tags oder Releases.
- Keine Änderungen an fremden Klonen oder Forks und keine eigenständig gesendete Supportanfrage.
- Keine Archivierungsinfrastruktur oder zweite feste Exportausschlussliste.

## Work items

### W-001 Metadaten und nachträgliche Freigabe berichtigen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0225]
Outcome: Kompatibilität und Reviewbericht entsprechen den freigegebenen Aussagen.
Acceptance: Plan verliert nur die irreführende Restformulierung; gleichartige Kompatibilitätsangaben sind geprüft. Cleanup bleibt unverändert. Der Bericht enthält ausschließlich den datierten Nachtrag zur nachträglichen Mainloop-Freigabe.
Instructions: []
Steps:
1. [status: done] Plan-Frontmatter und Kompatibilitätsquellen prüfen und das bestätigte Muster korrigieren; den Berichtsnachtrag vom 2026-10-29 ergänzen. Fertig nach engem Diffreview und Plan-Membertests.
Evidence: ["Plan 124 ausgeführt, 1 skip; Kompatibilitätsquellen und enger Diff geprüft. Nur Plan-Metadaten und autorisierter Berichtsnachtrag geändert."]

### W-002 Exportgrenze am bestehenden Owner schützen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0226]
Outcome: Aktuelle öffentliche Quellen und Pakete enthalten keine geschützten Namen oder entfernten Altberichte.
Acceptance: Veraltete lokale Treffer und Altberichte sind entfernt; Paket- und README-Abhängigkeiten bleiben vollständig. Verwaiste Links sind an ihrer Quelle bereinigt. Namensliste und Detailaudit bleiben privat und unverlinkt. Der vorhandene Exporttest erkennt vergessene Ausschlüsse ohne reale Namen in Testdaten.
Instructions: []
Steps:
1. [status: done] Kanonische Pfade und Inhalte inventarisieren, autorisierte Altdateien entfernen und ihre Links bereinigen. Nur den Namensschutz am vorhandenen Exportowner ergänzen; keine Erweiterung für gelöschte Evidenzpfade. Fertig nach Gegenfällen für vergessene Treffer und unzulässige Abhängigkeiten.
2. [status: done] Neutralen ADR und neue Changelog-Einträge pflegen, Shared-Kopien regenerieren; Plan-Membertests, Exporttests und check_all.py ausführen. Fertig bei bestandenen Checks vor dem Quellencommit.
Evidence: ["check_all: 12 bestanden, 0 Fehler; 480 Python-Tests ausgeführt, 7 übersprungen. Exportgegenfälle und Recordlinks geprüft; 36 Altdateien entfernt."]

### W-003 Öffentliche Historie erfassen und lokal bereinigen

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0226]
Outcome: Private Bestandsaufnahme und lokale Bereinigungskandidaten liegen vor.
Acceptance: Alle öffentlichen Kontorepos einschließlich zurückgezogener Repos sind auf Git-Objekte, Referenzen, Releases/Assets, Issues, PRs und Forks untersucht. Keine zusätzlichen Sicherungen; bereits angelegte Inventurkopien dienen nur der Vorbereitung und werden anschließend aufgeräumt. Kandidaten entfernen ausgeschlossene Pfade und neutralisieren Resttreffer; Grenzen außerhalb schreibbarer Git-Referenzen bleiben ausdrücklich offen.
Instructions: Keine Remoteänderungen. Detailbelege ausschließlich privat speichern.
Steps:
1. [status: done] Öffentliche Repos und GitHub-Oberflächen erfassen; Fertig nach dokumentierter Reichweite und Referenzen ohne zusätzliche Backupanforderung.
2. [status: done] Zentral bauen und geprüfte Exporte mit filter-repo in lokalen Arbeitskopien vorbereiten. Fertig nach Suche über erreichbare Objekte, Paket-/README-Prüfung und Planvalidator beider Exportprofile; Tagbehandlung separat vorlegen.
Evidence: ["10 Repos inventarisiert; 4 main-Kandidaten ohne Namenstreffer. 4 Builds/Paketprüfungen und 2 Planprofile bestanden. Installer- und Hostcachegrenzen offen dokumentiert."]

### W-004 Konkrete Veröffentlichung freigeben und prüfen

Status: cancelled
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0225, ADR-0226]
Outcome: Ausschließlich der ausdrücklich freigegebene Stand ist veröffentlicht und seine erreichbare Remotehistorie nachgeprüft.
Acceptance: Nutzer erhält Diff, Checks, betroffene Repos, Commitzahlen, alte/neue HEADs, Tagvorschlag, ungültige Hashverweise und Auswirkungen auf Klone/Forks. Erst nach konkreter Freigabe erfolgen Push und freigegebene Tagaktionen. Frische Remoteprüfung und vorbereitete Supportanfrage nennen verbleibende Grenzen ohne Löschgarantie.
Instructions: []
Steps:
1. [status: done] Vollständige Freigabevorlage und Supporttext erstellen; Fertig nach Prüfung gegen lokale Kandidaten und unveränderte Remoteausgangsstände.
2. [status: done] Nach ausdrücklicher Freigabe nur genehmigte Referenzen veröffentlichen und frische Klone vollständig prüfen. Fertig nach belegter Remoteprüfung und ehrlichem Abschluss je Auftragspunkt.
Evidence: Vier Stände veröffentlicht, Tags gelöscht und Remote geprüft. Nutzer beendet die Support-Nachverfolgung; vollständige Entfernung alter GitHub-Objekte bleibt unbestätigt.
