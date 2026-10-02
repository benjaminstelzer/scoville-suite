---
format_version: 1
id: PLAN-0031
status: completed
created: 2026-10-02
updated: 2026-10-02
---

# Workflow-Manager über Setup konfigurieren

## Goal

Das Manager-Modell und Reasoning lassen sich pro Projekt speichern. Der Default
ist gpt-6.1-sol mit medium.
Fragen und Abschlussmeldungen bleiben im zuständigen Workflow-Lauf.

## Non-goals

Keine Änderung der Worker-/Reviewer-Routen oder laufender Modellpaare. Kein
GitHub-Release und keine zusätzlichen Testagenten in diesem Thread.

## Work items

### W-001 Manager-Einstellung wird beim Start verwendet

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0140]
Outcome: Setup, Projektkonfiguration und Workflow-Start verwenden dieselbe Manager-Einstellung.
Acceptance: Gebaute Helper prüfen Default, gespeicherte Teilüberschreibungen, ausdrückliche Laufwahl und unveränderte Nachfolgerwahl. Fehler erzeugen keine Startargumente oder Konfigurationsänderung. Lokale Setup-/Workflow-Pakete entsprechen dem verifizierten Build; beide bestehenden Workflows sind informiert.
Instructions: []
Steps:
1. [status: done] Konfiguration, Setup und Start-/Nachfolgervertrag in den kanonischen Member-Quellen ergänzen.
2. [status: done] Gebaute Setup-Ausgabe im Starthelper konsumieren und gültige sowie fehlerhafte Varianten prüfen.
3. [status: done] Verifizierte lokale Pakete installieren, Fluid Base und EMPCO über das Update informieren und Ergebnis committen.
Evidence: Gebaute Helper geprüft; Setup 8 und Workflow 18 Dateien lokal identisch, beide Hinweise zugestellt. ../../../temp/2026-10-02-manager-configuration/assessment.md

### W-002 Nachrichten bleiben im zugehörigen Workflow

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0139]
Outcome: Die tatsächlichen Regeln und Startargumente binden Nachrichten an den ursprünglichen Runner und zuständigen Manager.
Acceptance: Initialstart, Nachfolger, Kinder, Fragen, Antworten und Abschlussbericht sind gegen fremde Runner-/Projektidentitäten geprüft. Belegte Lücken werden korrigiert. Regelprüfung und Helpernachweise werden von einer nicht ausgeführten nativen Laufabnahme unterschieden.
Instructions: []
Steps:
1. [status: done] Empfängerbindung und Berichtpfade im vollständigen betroffenen Vertrag prüfen, getrennte Projekt-/Runneridentitäten in Helpertests verwenden und Befund festhalten.
Evidence: Zwei Projektidentitäten geprüft, fremder Bericht abgelehnt; Regelbindung ausdrücklich, kein neuer Agentenlauf. ../../../temp/2026-10-02-manager-configuration/assessment.md
