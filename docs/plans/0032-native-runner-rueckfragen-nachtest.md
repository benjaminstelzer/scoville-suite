---
format_version: 1
id: PLAN-0032
status: completed
created: 2026-10-02
updated: 2026-10-02
---

# Rückfragen im tatsächlichen Workflow nachtesten

## Goal

Den aktuell installierten Workflow im gespeicherten Testprojekt mit gpt-6-luna
und medium für alle Testrollen auf sichtbare Worker-Rückfragen und Blocker prüfen.
Statusmeldungen durch einen Helper einheitlich mit fetter Titelzeile und
vollständiger Projekt-/Plan-/Step-Zuordnung hervorheben. Opus-Review und weitere
Kürzungsmöglichkeiten durch Astra Medium prüfen lassen.

## Non-goals

Keine Eingriffe in Live-Projekte, keine neue Weiterleitungsarchitektur oder
GitHub-Veröffentlichung. Root-Subagenten nur für das ausdrücklich beauftragte
Astra-Review. Keine parallelen Testläufe.

## Work items

### W-001 Sichtbare Rückfrage und Stillstandsgrund sind nativ nachgewiesen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0139]
Outcome: Ein wirklicher Workflow-Lauf liefert nachvollziehbare Frage-, Blocker- und Wiederaufnahmemeldungen im ursprünglichen Test-Runner.
Acceptance: Native Modellmetadaten bestätigen Luna Medium. Worker → Manager → Runner wird anhand tatsächlicher Nachrichten mit sichtbarer Frage, Grund, Planpunkt und wartender Arbeit geprüft. Ein anderer Blocker am selben Step bleibt sichtbar. Testantwort und bereitgestellte Voraussetzung setzen nur wartende Arbeit fort. Ergebnisse, Grenzen und Rollen-IDs sind gesichert; ursprüngliche Testkonfiguration ist wiederhergestellt und abgeschlossene Testrollen sind inaktiv.
Instructions: []
Steps:
1. [status: done] Neues Testprojekt-Szenario, eingefrorene Paketbytes und ausschließlich Luna-Medium-Einstellungen vorbereiten und validieren.
2. [status: done] Den echten Workflow seriell ausführen; native Übermittlung und tatsächliche Runner-Ausgabe vor Antworten und Wiederaufnahme sichern.
3. [status: done] Nachweise auswerten, Konfiguration wiederherstellen, abgeschlossene Tests aufräumen und Ergebnis committen.
Evidence: Worker-Frage sichtbar und Fortsetzung nativ geprüft; Konfiguration wiederhergestellt und abgeschlossene Testrollen archiviert.

### W-002 Statusmeldungen sind eindeutig zugeordnet und einheitlich formatiert

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0139, ADR-0141]
Outcome: Der Helper erzeugt fertige Statusmeldungen mit Projekt, Plan und Planpunkt/Step in fetter Titelzeile und normalem Fragetext.
Acceptance: Gebaute Helper-Ausgabe funktioniert unverändert im Consumer und tatsächlichen seriellen Luna-Medium-Lauf. Astra Medium prüft das Opus-Review und weitere sinnvolle Helper anhand des tatsächlichen Skills. Die Nachrichtenroute bleibt erhalten. Geprüftes Paket ist lokal installiert; autorisierte Live-Runner sind über das Update informiert.
Instructions: []
Steps:
1. [status: done] Zentrale Regel ergänzen und Paket prüfen.
2. [status: done] Darstellung im nächsten tatsächlichen Workflow-Lauf prüfen und Ergebnis sichern.
3. [status: done] Präzisierte Formatierung in run_feedback.py verlagern, doppelte Regeln ersetzen und gebaute Ausgabe im Consumer prüfen.
4. [status: done] Astra Medium prüft Opus-Befunde und weitere Helper zur Kürzung des tatsächlichen Skills.
5. [status: done] Endgültige Darstellung im seriellen Luna-Medium-Lauf prüfen, Nachweise sichern und Testkonfiguration wiederherstellen.
6. [status: done] Geprüftes Paket lokal installieren, autorisierte Runner informieren und Änderungen committen.
Evidence: Statusdarstellung nativ geprüft und Paket lokal installiert; autorisierte Runner informiert. Astra-Review durchgeführt.
