---
format_version: 1
id: PLAN-0033
status: completed
created: 2026-10-02
updated: 2026-10-02
---

# Workflow anhand des Astra-Reviews vereinfachen

## Goal

Die drei beauftragten Vereinfachungen reduzieren doppelte Übergaberegeln und mechanische Modell- und Fortschrittsübertragung. Workflow bleibt Codex-only mit Pflichthelpern, erfolgreicher WORKING_ON-Zustellung vor Schreibfreigabe, gespeichertem Startzustand und unveränderten Übergabegates.

## Non-goals

Keine Veröffentlichung, erneute Umsetzung von PLAN-0032 oder Änderung fremder Arbeit.

## Work items

### W-001 Kompakter Workflow mit direkt nutzbaren Helper-Ausgaben

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Ein gemeinsames Managerprotokoll, interne Modellauflösung im Dispatch-Builder und gespeicherte Plan-Projektion für Fortschritt sind gebaut, getestet und lokal installiert.
Acceptance: Regeln sind gegenüber dem gesicherten Ausgangsstand insgesamt kürzer und widerspruchsfrei. Native Consumer verwenden erfolgreiche Ausgaben unverändert. Ungültige Aufrufe liefern konkrete Diagnosen und korrigierte Aufrufe funktionieren. Ein serieller nativer Workflow im Projekt test mit ausschließlich GPT-6 Luna/Medium erhält Fortschritts-, Modell- und Übergabegarantien; Konfiguration ist wiederhergestellt, Testrollen und Nachweise sind gesichert und aufgeräumt.
Instructions: []
Steps:
1. [status: done] In members/scoville-workflow-for-codex die gemeinsame Protokollreferenz und beide Helper-Vereinfachungen mit betroffenen Anweisungen und Paketverträgen umsetzen.
2. [status: done] Gebaute Helper mit tatsächlichen Consumern und korrigierten Fehlerfällen prüfen; Kürzung und erhaltene Grenzen gegen den gesicherten Ausgangsstand belegen.
3. [status: done] Im gespeicherten Projekt test seriell mit neuem Luna/Medium-Runner prüfen, getestetes Paket installieren, ursprüngliche Konfiguration wiederherstellen und Testrollen archivieren.
Evidence: 56 Tests, Paketprüfung und native Consumer bestanden; lokal installiert. Details: members/scoville-workflow-for-codex/development/test-results/2026-10-02-workflow-simplification.md
