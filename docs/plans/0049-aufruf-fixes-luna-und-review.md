---
format_version: 1
id: PLAN-0049
status: completed
created: 2026-10-09
updated: 2026-10-09
---

# Aufruf-Fixes mit Luna und den ursprünglichen Reviewern prüfen

## Goal

Die Änderungen aus PLAN-0048 gezielt mit Luna 6/Medium auf Verständlichkeit prüfen und von den ursprünglichen Konsensreviewern beurteilen lassen.

## Non-goals

Keine vollständige Suite-Testmatrix, Installation, Commits, Veröffentlichung oder EMPCO-Aktionen. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Verständnisantworten sind kein Nachweis realer Workflow-Ausführung.

## Work items

### W-001 Verständlichkeit und Umsetzung der Aufruf-Fixes bewerten

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0206]
Outcome: Die neuen Regeln haben konkrete Luna-Ergebnisse und eine Umsetzungskontrolle durch ihre ursprünglichen Reviewer.
Acceptance: Alle geänderten Regelbereiche sind anhand vorab festgelegter Kriterien geprüft; vollständige Antworten und tatsächliche Reviewerbefunde sind ausgewertet; bestätigte Defekte sind korrigiert oder offen benannt; keine pauschale Wirkungsgarantie aus Stichproben.
Instructions: []
Steps:
1. [status: done] Sechs unabhängige Fallgruppen mit je drei Windows-/Linux-Szenarien und getrennten Erwartungskriterien aus dem aktuellen Quellenstand vorbereiten; frische Luna-6/Medium-Agenten starten.
2. [status: done] Sol-6.1/Xhigh-Agent ask_sol0047_consensus und Opus-5.5/High-Session b89b0e56-0d55-45ba-9df2-2bbe6ce859fe über Scoville Ask mit dem tatsächlichen Diff prüfen lassen.
3. [status: done] Antworten ohne nachträgliche Abschwächung der Kriterien bewerten; relevante bestätigte Defekte innerhalb des Fixumfangs korrigieren und nur betroffene Prüfungen und Reviews wiederholen.
4. [status: done] Ergebnisse, Reviewerabnahmen und offene Grenzen knapp festhalten; Plan und Index entsprechend tatsächlicher Abnahme abschließen.
Evidence: 36 Luna-Fälle ausgewertet; Fixes und Nachproben von Sol/Opus abgenommen, relevante Windows/Linux-Checks bestanden. Grenzen: docs/testing/0049-aufruf-fixes-luna-und-review.md.
