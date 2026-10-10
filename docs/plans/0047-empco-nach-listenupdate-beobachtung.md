---
format_version: 1
id: PLAN-0047
status: cancelled
created: 2026-10-08
updated: 2026-10-09
---

# EMPCO nach dem Listenupdate beobachten

## Goal

Neue Probleme im fortgesetzten EMPCO-Workflow SC-WFL PLAN-0001 alle fünf Minuten prüfen und allgemeine Verbesserungen für Workflow, Plan und Code sammeln. Nur neue Ablauffehler mitteilen; keine allgemeinen Fortschrittsmeldungen.

## Non-goals

Keine Änderungen, Tests, Stopps oder Agentennachrichten im EMPCO-Projekt. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Keine Skilländerungen, Commits oder Veröffentlichungen.

## Work items

### W-001 Neue Workflow-Probleme beobachten

Status: cancelled
Depends on: []
Blocked by: []
Decisions: [ADR-0205]
Outcome: Neue relevante Befunde und kleinste allgemeine Fixvorschläge sind knapp festgehalten.
Acceptance: Tatsächliche neue Aktionen und geladene Regeln wurden verglichen; bestätigte Befunde nennen Quelle, Wirkung, zuständigen Skill und offene Grenzen; bei Ende ist der beobachtete Umfang abgeschlossen und die Automation gelöscht.
Instructions: []
Steps:
1. [status: cancelled] Alle fünf Minuten neue Aktionen der tatsächlichen Manager, Worker und Reviewer in `<EMPCO project>` lesen; Rollen, unabhängige Reviews, Informationsübertragung, Findings, Ergebnisprüfungen und Planfortschritt mit den geladenen Regeln vergleichen.
2. [status: done] Nur neue relevante Befunde gebündelt über Scoville Ask mit Sol 6.1/high prüfen; bestätigte Probleme samt Fixvorschlägen in einem knappen, in Evidence verlinkten Befundbericht sammeln.
3. [status: done] Beim Ende oder Nutzerstopp eine knappe Schlussbewertung schreiben und die Automation löschen.
Evidence: Nutzerstopp; Automation gelöscht. Historische Auditlücke bleibt offen. Fixkonsens in PLAN-0048 übernommen. [Befunde](../testing/0047-empco-beobachtungsbefunde.md).
