---
format_version: 1
id: PLAN-0036
status: completed
created: 2026-10-06
updated: 2026-10-06
---

# Recovery-Auftragsdateien und Goal-first-Skill-Korrekturen

## Goal

Code und Plan halten Umsetzung und das verlangte Ergebnis im Vordergrund.
Tests, Reviews und Buchführung dienen einer konkreten Entscheidung oder einem
benannten Risiko. Gebündelte Profiländerungen und Nachweise sowie gültige
bestehende Freigaben verhindern unnötige Wiederholungen. W-002 behebt diesen
Skill-Fehler gemäß ADR-0197 vor den weiteren Recovery-Tests.

Recovery-Continuations sollen dieselbe vollständige Auftragsdatei-Übergabe wie
frische Workflow-Children nutzen. Eine kurze native Nachricht verweist auf die
Datei, ohne erforderliche Informationen aus dem Auftrag zu entfernen. Der
Nachfolger liest und behält den vollständigen Auftrag vor HANDOFF_ACCEPTED
und wartet vor Projektarbeit auf TAKEOVER_COMPLETE seines tatsächlichen Managers.
Das vermeidet den beobachteten großen Inline-Transfer, garantiert aber allein
weder vollständiges Lesen noch erfolgreiche Übernahme.

Ausführung vor der finalen Suite-Abnahme gemäß ADR-0196. PLAN-0035 und seine
eingefrorenen Nachweise bleiben unverändert; der frühere Recovery-v2-FAIL wird
nicht als PASS umgedeutet. Kanonische Quellen liegen in dieser Suite und
../shared. Ausgelieferte Inhalte bleiben Englisch.

## Non-goals

- Keine neue unabhängige Receipt-/Release-Regel neben native_task_arguments.
- Keine abgeschnittene oder inhaltlich unvollständige Übergabe und keine
  automatische Erhöhung von Ausgabe- oder Modellbudgets.
- Kein Wiederholen bereits erledigter Work-Item-Verfahren im Recovery-Auftrag.
- Keine Plattformzertifizierung aus einer lokalen Consumer-Probe.
- Kein Source-Commit, Push, CI-Lauf, Installation oder Veröffentlichung ohne
  konkrete Freigabe. Kein lokales Rust.

## Work items

### W-002 Goal-first-Regeln gegen Prüf- und Buchführungsrituale

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0197]
Outcome: Code und Plan führen zuerst zur verlangten Entwicklung und begrenzen Nachweisverwaltung, Prüfungen und Rückfragen auf ihren konkreten Zweck.
Acceptance: Astra/high bewertet die externe Analyse vor Änderungen. Code nennt Umsetzung als Vorrang und benennt Anlässe für Tests, Reviews und Wiederholungen ohne neue Quoten oder Ersatzmetriken. Plan bündelt zusammengehörige Profiländerungen, verlangt keine Profilvalidierung für reine externe Berichtsänderungen und nutzt einen owning Bericht je Work Item mit vollständigen Rohdaten. Bestehende passende Freigaben und Nachweise werden wiederverwendet; unbekannte materielle Entscheidungen und notwendige Nachtests bleiben verbindlich. Gezielte praktische Prüfung und Sol6.1/high-Blockreview bewerten den finalen Skill-Auftrag und weisen Grenzen aus.
Instructions: []
Steps:
1. [status: done] Astra/high-Ergebnis der externen Ritualanalyse übernehmen, reale Skill-Lücken von Ausführungsfehlern trennen und die kleinsten kanonischen Regelkorrekturen umsetzen.
2. [status: done] Das geänderte Verhalten mit gezielter praktischer Skill-Verwendung prüfen. Nur wenn Mechanik geändert wurde, deren tatsächlichen Consumer und fehlerhaften sowie korrigierten Aufruf prüfen. Bestehende unveränderte Nachweise wiederverwenden.
3. [status: done] Den finalen Fixblock durch Sol6.1/high über Ask prüfen lassen, bestätigte korrigierte Fehler gezielt nachtesten und Ergebnis im bestehenden Bericht festhalten.
Evidence: Goal-first-Regeln umgesetzt und praktisch mit Luna geprüft; Astra- und Sol-Reviews durchgeführt. Erforderliche Prüf- und Freigabegrenzen erhalten.

### W-001 Recovery-Aufträge vollständig vor Übernahme lesen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0196]
Outcome: Recovery-Create liefert direkt verwendbare native Argumente mit vollständiger atomarer Auftragsdatei und unverändertem Übernahmevertrag.
Acceptance: Recovery --format create verwendet die bestehende assignment_path-/publish_assignment-Mechanik. Direkte Prompt-Ausgabe bleibt erhalten. UTF-8, eindeutige absolute Pfade, atomare Veröffentlichung und kein Überschreiben funktionieren mit Leerzeichen und Unicode. Der vollständige bisherige Auftrag erhält Rolle, Modell/Effort, tatsächliche IDs, verbleibende Arbeit, geltende Einschränkungen und Nachweisgrenzen. Fehler liefern keinen erfolgreichen Dispatch. Tatsächliche native Executor- und Read-only-Reviewer-Nachfolger lesen den vollständigen Auftrag vor HANDOFF_ACCEPTED und beginnen erst nach authentifiziertem TAKEOVER_COMPLETE. Fehlende wesentliche Fakten, unzugängliche oder unvollständig gelesene Datei sowie fehlende/falsche Freigabe erlauben keine gültige Übernahme oder Projektarbeit. Gezielte Tests und Sol 6.1/high-Blockreview sind belegt; Plattform- und Beobachtungsgrenzen bleiben ausgewiesen.
Instructions: []
Steps:
1. [status: done] In members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py Recovery-Create an die vorhandene Auftragsdatei-Mechanik anbinden. ../shared/runtime/native_task_arguments.py bleibt Owner des Übernahmevertrags. Direkte Ausgabe und tatsächliche Dispatch-Parameter erhalten.
2. [status: done] Vollständige Inhalte, Unicode-/Leerzeichenpfade, Rolle/Modell/Effort/IDs, Kollision und Veröffentlichungsfehler mit dem tatsächlichen Datei-Consumer prüfen. Ungültigen und korrigierten Aufruf belegen. Python-Plattformnachweise durch konkret freigegebene Actions führen.
3. [status: done] Native Executor- und Reviewer-Fortsetzung mit tatsächlichem vollständigem Lesen, Receipt, Manager-Release, ausschließlich verbleibender Arbeit, geltenden Grenzen und finaler Lieferung prüfen. Relevante negative Lese-/Fakten-/Release-Pfade prüfen und Grenzen ausweisen.
4. [status: done] Nötige Workflow-Dokumentation beim bestehenden Owner anpassen, Paketprojektionen prüfen und Sol 6.1/high pro Testblock einholen. Bestätigte korrigierte Fehler gezielt nachtesten; vollständige Nachweise behalten.
Evidence: Vollständige Recovery-Dateiübergabe, native Consumer und Nachtests bestanden; Actions und Paketprojektionen geprüft. Sol-Review durchgeführt.
