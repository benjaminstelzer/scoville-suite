---
format_version: 1
id: PLAN-0042
status: completed
created: 2026-10-08
updated: 2026-10-08
---

# Workflow-Abschlussausgabe korrigieren

## Goal

Die in PLAN-0041 gesammelten Verbesserungen nach Sol-6.1/high-Review umsetzen: vollständiger Workflow-Abschluss ohne unnötige Reportübertragung und sachliche Diagnose möglicher Kürzung.

## Non-goals

Keine EMPCO-Änderungen oder Agentennachrichten. Keine Releases oder Installation. Keine Änderung von Freigaben oder Checkerbudgets; keine Reviewarchive oder zusätzlichen Prüfrituale.

## Work items

### W-001 Abschlussantwort und Ausgabediagnose korrigieren

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der Abschluss überträgt nur benötigte Statusfelder; der vollständige Report bleibt separat lesbar und Fehler werden anhand beobachteter Fakten benannt.
Acceptance: Ein großer Report verändert die Größe der complete-Antwort nicht; read erhält den vollständigen Report. Speicher- und Ausgabefehler bleiben sichtbar. Gezielte Checks bestehen unter Windows und Linux.
Instructions: []
Steps:
1. [status: done] Sol 6.1/high prüft PLAN-0041 und seine Fixvorschläge gegen kanonische Quellen und betroffene Verbraucher.
2. [status: done] Bestätigte Fixes in Workflow-Helper und Aufrufanleitung sowie shared/prompting/common.md umsetzen; Reportassertionen auf read umstellen und generierte Shared-Kopien synchronisieren.
3. [status: done] Abschluss mit großem Report und erhaltenen Fehlergrenzen im bestehenden CLI-Harness unter Windows und WSL/Linux prüfen; Diff und Planstruktur kontrollieren.
Evidence: [Sol 6.1/high prüfte den Plan; Quellenkorrektur und Migration der Testverbraucher übernommen. Externe Verbraucher nicht geprüft., complete liefert nur Reportpfad und vollständigen Status. read behält den vollständigen Report. Gesicherte Aufrufe und evidenzgebundene Kürzungsdiagnose umgesetzt; Shared-Snapshots regeneriert., test_run_feedback.py: 19 Tests unter Windows und 19 unter WSL/Linux bestanden. Große Historie verändert Abschlussantwort nicht; Report und Fehlergrenzen bleiben erhalten., Linux-Test benötigt vorhandenen Node-Pfad für unveränderten Encoderfall. Skill-Creator-Prüfer lehnt vorhandenes compatibility-Feld auf beiden OS ab; Paketbau im CLI-Harness erfolgreich., Keine Release- oder Installationsänderung. Neue Formulierungen selbst geprüft; kein zusätzlicher Luna-Verständnistest.]
