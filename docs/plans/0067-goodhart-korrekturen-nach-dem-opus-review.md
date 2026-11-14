---
format_version: 1
id: PLAN-0067
status: active
created: 2026-11-14
updated: 2026-11-14
current_item: W-002
---

# Goodhart-Korrekturen nach dem Opus-Review

## Goal

Die Befunde des Reviews vom 2026-11-13 (sechs Prüfer, Opus 5.5 xhigh) an den Quellen beheben: Regeln, bei denen der Prozess zum Ziel wird, missverständliche Sätze, Widersprüche und Beispiele, die aus Messaufgaben stammen. Owner sind members/ und ../shared/. Schutzregeln, Helper- und Datenformatverträge bleiben erhalten. Die Aussagen des Berichts zu PLAN-0066 über die zweite Messreihe werden richtiggestellt. Ergebnisse stehen im [Bericht](../testing/0067-goodhart-korrekturen-nach-dem-opus-review.md).

Lokale Commits sind freigegeben. Pushs einschließlich privater CI, Exporte in öffentliche Repositories und lokale Installation brauchen jeweils eine ausdrückliche Freigabe.

## Non-goals

- Keine Aussage über Modellwirkung ohne Messung an Aufgaben, deren Ersteller weder die Skills noch die bisherigen Aufgaben kannte.
- Keine neue Prüf-, Listen- oder Berichtspflicht als Korrektur.
- Keine Änderung an Helper-Logik, Feldnamen oder Ausgabeformaten.

## Work items

### W-001 Befunde an den Quellen beheben

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0232, ADR-0233, ADR-0234]
Outcome: Die bestätigten Befunde sind in den Skilltexten, Referenzen, gemeinsamen Regeln und Prompttexten der Helfer behoben; offen gelassene Befunde stehen mit Grund im Bericht.
Acceptance: Jeder Befund der sechs Prüfberichte ist im Bericht als behoben, verworfen oder offen geführt. Die drei Entscheidungen sind in Plan, UI und Workflow umgesetzt. Kein Beispiel der Skilltexte wiederholt Szenario oder Werte einer Messaufgabe. Der Bericht zu PLAN-0066 nennt die Grenzen der zweiten Messreihe. `python development/check_all.py` besteht.
Instructions: []
Steps:
1. [status: done] Korrekturen je Skill-Gruppe an members/ und ../shared/ ausführen und jede Änderung am Diff prüfen; fertig, wenn jeder Befund eine Einordnung hat.
2. [status: done] Tests an geänderte Formulierungen anpassen, Snapshot synchronisieren und die Gesamtprüfung ausführen; fertig bei bestandener Gesamtprüfung.
3. [status: done] Bericht unter docs/testing schreiben und den Bericht zu PLAN-0066 richtigstellen; fertig, wenn beide Berichte die Grenzen der Messung nennen.
Evidence: check_all 12/12; Suche nach 18 entfernten Beispielen ohne Treffer; Bericht führt jeden Befund; offen: 12 Befunde für den Eigentümer; keine Modellläufe.

### W-002 Ausliefern nach Freigabe

Status: in_progress
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der korrigierte Stand ist in den Ziel-Repositories veröffentlicht und lokal installiert.
Acceptance: Die private Laufzeit-CI hat für die geänderten Python-Helfer bestanden. `release_suite.py publish` meldet alle Ziele als geprüft. Die installierten Skills entsprechen dem veröffentlichten Stand.
Instructions: Push der privaten CI, Veröffentlichung und lokale Installation brauchen je eine eigene Freigabe des Nutzers.
Steps:
1. [status: done] Nach Freigabe die Laufzeit-CI pushen und ihr Ergebnis abwarten; fertig bei sechs bestandenen Jobs.
2. [status: todo] Nach Freigabe mit release_suite.py vorbereiten und veröffentlichen; fertig, wenn published.json alle Ziele als geprüft führt.
3. [status: todo] Nach Freigabe die installierten Skills aktualisieren; fertig, wenn sie dem Auslieferungsstand entsprechen.
Evidence: Laufzeit-CI Run 43568849307 auf Commit 032df8d: sechs von sechs Jobs bestanden (Windows, macOS, Linux; Python 3.11 und 3.x).
