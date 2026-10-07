---
format_version: 1
id: PLAN-0017
status: completed
created: 2026-09-27
updated: 2026-09-27
---

# Kontextreserve und klare Workflow-Quellen

## Goal

Weniger unnötige Koordinatorwechsel und mehr Kontextreserve für Worker durch kleine Änderungen am bestehenden nativen Workflow. Die Defaults 40/60 werden erprobt. Änderungen aus dem unabhängigen DIVI5-Review werden nur übernommen, wenn sie die sichere Fortsetzung erhalten.

## Non-goals

- Keine neue Orchestrierung, Polling-, Bestätigungs- oder Prüferschicht.
- Keine Änderung laufender DIVI5-Chats, ihrer Konfiguration oder Produktdateien.
- Keine garantierte Kontextobergrenze oder Compaction-Vermeidung. Laufzeit, Aufrufanteile und Kontextsprünge sind Beobachtungswerte, keine harte Abnahme.

## Work items

### W-001 Kontextreserve ohne zusätzliche Ablaufkomplexität

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Koordinatoren wechseln ab 40 Prozent, Worker über 60 Prozent. Umfangreiche Ausgaben werden gezielt gelesen und zusammengehörige Zustandsänderungen gebündelt.
Acceptance: Grenzfälle 39/40 und 60/61, Projektüberschreibungen und ungültige Werte sind getestet. Aufträge verlangen einen Checkpoint vor voraussichtlich umfangreichem Kontextzuwachs ohne doppelten Direktcheck. Vollständige große Ausgaben und Exitstatus bleiben erhalten. Startabsicht und Kind-Handle bleiben über create_thread hinweg gesichert; beim Koordinator-Rollover erfolgen danach keine Vorgänger-Schreibzugriffe. Astra Medium prüft den Diff und notwendige Befunde sind behoben.
Steps:
1. Defaults, öffentliche Beschreibungen, Setup-Test und den ungestarteten Claude-Plan angleichen.
2. Checkpoint- und Ausgaberegeln knapp ergänzen; Zustandsänderungen ohne feste Patchzahl bündeln.
3. Grenzfälle testen, Review auswerten und Befunde beheben.
Evidence: Kontextgrenzen, Paketfunktionen und Fehlerausgabe gezielt geprüft. Unabhängiges Astra-Review fand keine offenen Befunde; ADR-0098 berücksichtigt.

### W-002 Eindeutige Quellen und aktuelle Prüfungen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Veraltete Build-Kopien und ungenutzte Lifecycle-Dateien verwirren keine Agenten mehr. Tests prüfen die geltenden Verträge.
Acceptance: Suite-, Shared-, Ask-, Plan-, Setup- und Workflow-Tests bestehen. README- und Quellprüfungen bestehen. Private packages/ ist keine versionierte zweite Quelle; öffentliche Pakete werden weiter erzeugt. Entfernte Lifecycle-Dateien haben keine Laufzeitverbraucher.
Steps:
1. Veraltete README-Assertions an die freigegebenen Aussagen anpassen.
2. Private packages/ und ungenutzte Lifecycle-Dateien entfernen, kanonische Quellen und Historie behalten.
3. Betroffene Prüfungen ausführen.
Evidence: Betroffene Suite-, Shared- und Member-Checks sowie Quell-, README- und Buildprüfungen bestanden.

### W-003 Geprüfte Builds lokal und auf GitHub bereitstellen

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Lokale Skills und autorisierte GitHub-Ziele enthalten die geprüften Änderungen.
Acceptance: Beide Editionen bauen aus sauberem HEAD. Installierte Dateien stimmen mit dem jeweiligen Build überein. GitHub-Dateien stimmen mit den autorisierten Exporten überein; unveränderte Ziele erhalten keinen Release. Ausstehende Veröffentlichungsgates bleiben ausdrücklich sichtbar.
Steps:
1. Versionshinweise pflegen, sauber committen und beide Editionen bauen.
2. Betroffene lokale Installationen aktualisieren und Bytes vergleichen.
3. Geprüfte Änderungen unter geltenden Veröffentlichungsgates pushen und remote prüfen.
Evidence: Builds, lokale Installationen und beide Remote-Suitebäume gegen Exporte geprüft; Luna-Nachtest und unabhängiges Astra-Review durchgeführt.
