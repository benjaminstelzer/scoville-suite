---
format_version: 1
id: PLAN-0026
status: draft
created: 2026-09-30
updated: 2026-10-01
---

# Workflow unter Luna Medium mit Zwischenfragen und Rückkehr prüfen

## Goal

Den vollständigen technischen und realen Workflow-Test mit Luna 6 Medium in
allen getesteten Rollen wiederholen. Zwischenfragen und eine später freigegebene
Blockierung dürfen Auftrag, Rückkehr, offene Fragen oder Abschluss nicht verlieren.
ADR-0124 enthält Modellwahl, Simulationsauftrag und Grenzen.
Zusätzlich die native Ask-Agentenfreigabe nach ADR-0132 übernehmen und prüfen.

## Non-goals

Keine neuen Chats, Anwendung des Workflow-Ausführungsskills im aufrufenden Chat,
Installation, Veröffentlichung, Commits oder Änderungen produktiver Modellpaare.
Keine erfundenen Transportausfälle oder universelle Zuverlässigkeitsbehauptung.

## Work items

### W-001 Die vollständige Luna-Abnahme liefert belegte Ergebnisse und korrigierte Befunde

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0124, ADR-0125, ADR-0126]
Outcome: Der aktuelle Build ist unter den beauftragten Modell- und Störbedingungen geprüft, mit erhaltenen Fehlern und Nachweisgrenzen.
Acceptance: Die vollständigen deklarierten technischen Tests und aktuelle Paketprüfungen laufen erneut. Runner, Manager, Worker, Korrektur-Worker und Reviewer verwenden nachweislich gpt-6-luna/medium. Ein isolierter realer Lauf nutzt gebaute Aufträge, READY/START, Review und Korrektur, Frage/Antwort, Stopp/Wiederaufnahme, direkte Übergaben und gezielte Laufberichte. Mindestens drei simulierte Statusfragen treffen den aktiven Runner in verschiedenen Phasen; Antworten erfinden keinen Fortschritt und lösen keine doppelte Arbeit, verlorene Frage oder falschen Abschluss aus. Ein tatsächlich begonnener Punkt wird wegen eines fehlenden Moduls pausiert, ein späterer Punkt implementiert es, der Koordinator kehrt anschließend zum ursprünglichen Punkt zurück und beendet dessen restliche Arbeit. Ein separater sauberer Lauf liest vor Abschluss den Bericht mit dem vereinbarten Satz. Native Negativfälle und Simulationen werden getrennt ausgewiesen. Bestätigte Implementierungsprobleme werden automatisch in ihrer kanonischen Quelle behoben und betroffene Fälle erneut geprüft. Nicht erzeugbare Hostfehler bleiben ungetestet.
Steps:
1. [status: done] Gebaute Pakete und gültige Testprofile mit isolierten Luna-Modellpaaren vorbereiten; vollständige technische Tests wiederholen.
2. [status: done] Reale native Rollen und Statusfragen ausführen, tatsächliche Ereignisse und Dateien sichern, Abschluss und Rückkehr unabhängig prüfen.
3. [status: done] Bestätigte Probleme korrigieren, erforderliche Fälle wiederholen und abschließende Quellen-, Build- und Plan-Nachweise festhalten.
Evidence: 280 Tests/4 Builds, native Übergaben, STOP/Resume und Abschluss geprüft; Abweichungen erhalten. Siehe ../../../../../temp/2026-10-01-workflow-agent-capacity/report.md.

### W-002 Der Runner lädt während des Laufs keine weiteren Skills

Status: todo
Depends on: []
Blocked by: []
Decisions: [ADR-0125]
Outcome: Scoville Code begrenzt die aktive Runner-Rolle auf die erlaubten Scoville-Skills, ohne Implementierungsrollen zu sperren.
Acceptance: Die Codex-Code-Quelle definiert die Runner-Grenze für den aktiven Ablauf einschließlich Pause, Wiederaufnahme und Managerwechsel. Der Runner benutzt keine zusätzlichen Skills oder Code-Engineering-Routen. Planarbeit und Planinhalte bleiben beim Manager. Eine neue tatsächliche Runner-Abnahme konsumiert die aktualisierte gebaute Regel und hält sie bei Statusfragen ein. Generierte Pakete bleiben quellentreu, bestehende aktive Testkopien unverändert. Die genaue erlaubte Liste wird mit einer eingehenden Nutzerklärung abgeglichen.
Instructions: Abnahme erst nach Klärung der erlaubten Runner-Skillliste.
Steps:
1. [status: done] Vorhandene Code-Runner-Grenze und Workflow-Einstiegsreferenz im aktuellen Codex-Build abgleichen.
2. [status: done] Mit einem tatsächlichen Luna-Runner und Zwischenfragen prüfen, Ergebnisse und Nachweisgrenzen sichern.
Evidence: Luna-Runner mit Statusfragen und Managerwechsel geprüft; erlaubte Skillliste für die finale Abnahme noch ungeklärt.

### W-003 Native Ask-Berater beenden ihre Turns ohne wartende Routinequittungen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0132]
Outcome: Ask übernimmt den bestätigten nativen Abschluss und begrenzten Kapazitätsweg ohne verlorene Antworten oder doppelte Berater.
Acceptance: Gebauter Beraterprompt beendet die vollständige Antwort als nativen Final. Der Aufrufer wartet auf den tatsächlichen Abschluss und quittiert keinen abgeschlossenen Berater. Nur eindeutige Kapazitätsablehnung ohne erzeugten Agenten erlaubt einmalige Bereinigung eigener abgeschlossener Berater und einen Start mit unveränderten Argumenten. Unsichere Starts und Bereinigungsfehler verhindern Retry. Antworten und notwendige Folgefragen bleiben erhalten. Native Luna-Prüfung, vollständige technische Tests und alle vier Build-Varianten bestehen. Astra Medium prüft alle Abschlusswege; bestätigte Befunde werden korrigiert und nachgeprüft. Nicht erzeugte Hostfehler bleiben ausdrücklich ungetestet.
Steps:
1. [status: done] Native Ask-Referenzen und kanonische README-Fragmente ergänzen; gebauten Prompt im nativen Verbraucher verwenden.
2. [status: done] Bereinigung und Folgenachricht an bekannten Handles prüfen; Astra Medium prüfen lassen und belegte Befunde korrigieren.
3. [status: done] Technische Tests und vier aktuelle Build-Varianten prüfen; tatsächlich ausgeführte Pfade und Grenzen festhalten.
Evidence: 268 Tests/4 Builds, native Ask-Finals/Folgefrage/Drain bestanden; Astra ohne Befund. Refusal/Retry ungetestet. Siehe ../../../../../temp/2026-10-01-workflow-agent-capacity/report.md.
