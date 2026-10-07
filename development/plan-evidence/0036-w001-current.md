# PLAN-0036/W-001: aktueller Stand

Vorbereitung begonnen nach Nutzerentscheidung ADR-0196.
W-002 ist nach Astra/high, gezielter Luna-Probe und Sol6.1/high PASS abgeschlossen.
Recovery-Umsetzung wieder aufgenommen; Scope bleibt erhalten.
PLAN-0035/W-009 ist pausiert, seine laufenden Steps und Nachweise bleiben.
Nach Abschluss dieses Plans zurück zu W-009; W-015 bleibt zuletzt.

Die [Astra/high-Designprüfung](0035-w009-external-followup-astra-high-review.json)
fordert vollständiges Lesen vor Receipt und Manager-Release vor Arbeit.
Der bestehende shared Owner bleibt der einzige Übernahmevertrag.
Alle Luna/high-Starts werden vorab im gemeinsamen 300er-Register reserviert.
Aktuell 174 Reservierungen, 170 berichtete Starts. Keine neuen Starts durch
Aktivierung. Source-Baseline, Implementierung und gezielte Nachweise folgen.

## Priorisierte Ritualkorrektur

Die neue Nutzeranweisung und Astra-Prüfung sind im owning Bericht
[W-002](0036-w002-current.md) festgehalten. Danach diese Recovery-Umsetzung fortsetzen.

## Umsetzung und gebündelter Runtime-Nachlauf

Recovery --format create nutzt nun denselben vollständigen atomaren Dateiweg
wie frische Children. Die kurze Nachricht verlangt vollständiges Lesen und
Behalten vor Receipt; unzugängliches oder unvollständiges Lesen bleibt blocked.
Direkte Prompt-Ausgabe und der shared Übernahmevertrag bleiben erhalten.
Read-only für Reviewer gilt in Nachricht und vollständigem Auftrag.
Dokumentation angepasst. Zwei gezielte Runtime-Tests prüfen vollständigen
Datei-Consumer, direkte Ausgabe, Unicode/Leerzeichen, Rolle/Paar, ungültigen
Format-Aufruf mit Korrektur und Überschreibschutz. Bestehende Atomic-Publish-
Nachweise werden wiederverwendet, keine neue Mechanik.

Notwendiger privater Actions-Nachlauf nach ADR-0184, zusammen mit den
bereits abgeschlossenen W-002-Projektionen. Suite-Source weder committed
noch gepusht; keine Installation oder Veröffentlichung.
Privater Snapshot: `5b3835f5ce9a7e360bf8529298aeecd4112eff73`, Input-SHA256 `0a20d56418b83fa92226bf15fc99dcccfe5f4de71c5748518055fdf1f8730d0b`.
Geänderte Pfade: `packages/codex-suite/scoville-code/scoville-code/references/validation.md`, `packages/codex-suite/scoville-plan/scoville-plan/SKILL.md`, `packages/codex-suite/scoville-plan/scoville-plan/references/edit.md`, `packages/codex-suite/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations-dispatch.md`, `packages/codex-suite/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py`, `packages/general-standalone/scoville-code/scoville-code/references/validation.md`, `packages/general-standalone/scoville-plan/scoville-plan/SKILL.md`, `packages/general-standalone/scoville-plan/scoville-plan/references/edit.md`, `packages/general-suite/scoville-code/scoville-code/references/validation.md`, `packages/general-suite/scoville-plan/scoville-plan/SKILL.md`, `packages/general-suite/scoville-plan/scoville-plan/references/edit.md`, `runtime-input.json`, `tests/test_runtime_helpers.py`.
Matrix unverändert; tatsächliches Resultat noch offen.

EMPCO-Regeln zugestellt und vom Runner als an den aktuellen Manager weitergegeben bestätigt.
Erster Runtime-Nachlauf 37429486780: FAIL im neu geschriebenen direkten Prompt-Test, native Create-Parameter waren dort unzulässig. Keine Produktänderung zur Korrektur; Testaufruf korrigiert. Vollständiger Rohlog im Workspace temp/2026-10-06-plan0036/runtime-failure-37429486780.log.
Gezielter korrigierter Nachlauf: privater Commit `b3c42b1f56faf5cd39008474da4d3adb3af0bc64`, Input `a7639950533af261d0c09ac9e7a1bafca15184b5f2470a515c9597a68950dd52`. Nur Test und Input geändert.
Native Vorbereitung: eine erste Reservierung erhalten, kein Start; beim zweiten Reserve-Aufruf blockierte ein Windows-Dateizugriff die atomare Register-Ersetzung. Keine Modelle gestartet. Alte Reservierung zählt weiterhin; keine Rückerstattung oder Umwidmung.

## Native Consumer und Routing-Korrektur

Executor hat vollständige Fakten übernommen, falsche native Release-Herkunft
nicht zum Schreiben verwendet und erst nach echtem Root-Manager-Release die
verbleibende Zeile geschrieben. Initiale checked.txt blieb unverändert.
Unlesbare Datei und fehlende essentielle Fakten stoppten vor Receipt und Arbeit.
Valid Reviewer scheiterte beim falsch gewählten Chat-API mit Invalid conversation
root und blieb korrekt schreibinaktiv; historischer FAIL bleibt erhalten.

Astra/high bestätigt den Ausführungsfehler und eine gezielte Präzisierung:
shared takeover_instruction benennt jetzt collaboration.send_message und
collaboration.wait_agent und native Agent-Handles. Protokoll und Gates unverändert.
Kompletter Befund: 0036-w001-native-routing-astra-review.json.
Nur der gescheiterte valide Reviewer wird neu geprüft. Kein Wiederholen der
anderen unveränderten nativen Beobachtungen. Aktuell 181 Reservierungen;
letzte Retest-Reservierung vor Start. Source weiterhin ohne Commit/Push.
Finaler privater Runtime-Snapshot: `411cb1ef96811d1a10527b407d857d52c45c676a`, Input `6e74208eb57627be8113a1e51b03edeaa1c4789eb4d0c6632e42809e1228c946`. Vorige korrigierte Matrix 37429999685 bestand sechs Jobs, ihre Bytebindung bleibt historisch.

## Finaler gebündelter Nachweis

Sechs tatsächliche Luna/high-Finals samt Kontexten, nativen IDs, vollständigen
Antworten, Usage und Dateiständen: Workspace
`temp/2026-10-06-plan0036/recovery-native/native-results.json`.
Finale Matrix 37430738098: **6/6 PASS**, Windows/macOS/Linux jeweils Python
3.11 und 3.x, 19 Runtime-Tests. Commit und Input stimmen mit aktuellem Kandidaten
überein. Komplette Jobdaten in runtime-final-result.json neben den nativen
Rohdaten. Kein nativer macOS-Consumer oder allgemeine Compliance behauptet.
181 gemeinsame Reservierungen, 176 berichtete Starts; alle ungenutzten bleiben
gezählt. Finaler Sol6.1/high-Review prüft diesen Block jetzt einmal zusammen.

Vier finale temporäre Exporte mit tatsächlicher Runtime-Bindung zu Actions
37430738098 gebaut und --check-packages bestanden. Verzeichnis im Workspace:
`temp/2026-10-06-plan0036/final-packages`. Keine Veröffentlichung oder Installation.

## Abschluss

W-001 abgeschlossen. Vollständiger tatsächlicher Sol6.1/high-Blockreview: **PASS** in 0036-w001-sol-review.json. Kanonische Umsetzung, relevante native Consumer, Fehlerpfade, korrigierter Nachtest und final gebundene 6/6-OS-Matrix sind angenommen. Vier Exporte und Paketchecks bestehen. Endlicher nativer Einzelfall, keine universelle Modell- oder macOS-Agentengarantie. PLAN-0036 abgeschlossen; Rückkehr zu PLAN-0035/W-009 nach ADR-0196. W-015 bleibt zuletzt.
