---
format_version: 1
id: PLAN-0048
status: completed
created: 2026-10-09
updated: 2026-10-09
---

# Abgestimmte Scoville-Aufruf- und Planfeldfixes umsetzen

## Goal

Den beidseitigen Opus-5.5/high- und GPT-6.1/xhigh-Konsens aus [PLAN-0047](../testing/0047-empco-beobachtungsbefunde.md) in den kanonischen Quellen umsetzen und gezielt unter Windows und Linux prüfen.

## Non-goals

Keine EMPCO-Änderungen, Tests oder Agentennachrichten. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Keine Installation, Commits oder Veröffentlichungen. Keine Validator-, Evidence- oder Host-Routingfixes ohne belegte Suiteursache.

## Work items

### W-001 Sichere Aufrufe und klare Planfeldabnahme bereitstellen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0205]
Outcome: Die abgestimmten Aufruf- und Feldregeln sind in ihren Quellen umgesetzt und ihre geänderten technischen Verträge geprüft.
Acceptance: Fertige Readerbefehle bewahren Lesestufen und Argumente; Windows-Startfehler liefern Diagnose und Nichtnullstatus, erfolgreiche Kinder lassen die Shell weiterlaufen; erwartete Hashwerte sind budgetiert ohne Artefaktänderung prüfbar, vollständiges Lesen bleibt erforderlich; Planfelder sind im bestehenden Abnahmeschritt klar zugeordnet; betroffene technische Verträge bestehen auf Windows und Linux; generierte Kopien entsprechen ihren Quellen.
Instructions: []
Steps:
1. [status: done] Kanonische shared/runtime/native_task_arguments.py und check_text_size.py sowie Workflow scripts/build_manager_handoff.py nach dem Konsens anpassen; Argumentquotierung, Fehlerstatus, Readerstufen und übrige Checkermodi bewahren.
2. [status: done] shared/runtime/document_reader.md, check_text_size-fallback.md, python_discovery.md, shared/prompting/common.md und Plan references/edit.md knapp anpassen; gemeinsame Suitekopien über sync_suite_sources.py erzeugen.
3. [status: done] Geänderte Aufruf-, Hash- und Readerverträge gezielt unter Windows und Linux prüfen, betroffene Verbraucher und finalen Diff prüfen und Ergebnisse festhalten.
Evidence: Acht Tests je System bestanden; [Umsetzung und Grenzen](../testing/0048-scoville-aufruf-fixes.md). Luna-Wirkung unbestätigt.
