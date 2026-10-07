---
format_version: 1
id: PLAN-0025
status: completed
created: 2026-09-30
updated: 2026-09-30
---

# Workflow zeigt Auftrag und bewahrt relevante Laufhinweise

## Goal

Die kanonische Workflow-Version zeigt den beauftragten Umfang und aktuellen
Punkt bei Wechseln und bewahrt gezielte Nutzerfragen und Probleme in einer
Markdown-Datei pro Lauf. Vollständige technische und reale native Tests prüfen
den aktuellen Workflow einschließlich der zuletzt korrigierten Dispatch- und
Übergabewege. ADR-0123 enthält Anzeige, Bericht und Testautorisierung.

## Non-goals

Keine neuen Chats, Anwendung des Workflow-Skills durch den aufrufenden Chat,
Installation, Veröffentlichung oder Änderung der gewählten Modellpaare.
Keine Routineprotokolle oder neue externe Laufzeit.

## Work items

### W-001 Der Runner zeigt den aktuellen Auftrag und gibt den gezielten Bericht aus

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0123]
Outcome: Fortschrittsanzeige und Laufdatei arbeiten über Managerwechsel und Wiederaufnahme gemäß Nutzerauftrag.
Acceptance: Gebaute Workflow-Helper und ihre echten Verbraucher zeigen Working on und freien Scope nur beim ersten Punkt oder Projekt-/Plan-/Punktwechsel. Jeder Lauf hat einen einzigartigen vollständigen Markdown-Pfad direkt unter .scoville, angezeigt vor Managerstart. Manager erhalten dieselbe Datei und protokollieren nur Nutzerfragen, deswegen angehaltene Punkte und Probleme mit nötiger Nutzerprüfung; Klärungen bewahren die ursprüngliche Frage ohne falschen Offenstatus. Normale Fortschritte und Tests füllen die Datei nicht. Ein erfolgreich abgeschlossener problemloser Lauf erhält exakt No issues occurred during this run. Abschluss setzt akzeptierten Auftrag und lesbaren Bericht voraus; Stopp, offene abhängige Fragen und Dateifehler erzeugen keinen Abschluss. Ungültige Helper-Aufrufe erzeugen verständliche Fehler ohne Teilerfolg und ihre korrigierten Aufrufe funktionieren direkt. README-Quellen, Manifest und Paketprojektion enthalten die neuen Verträge.
Steps:
1. [status: done] In members/scoville-workflow-for-codex/ einen kleinen Report-/Anzeigehelper und die notwendigen Start-, Manager-, Übergabe- und Kindverträge umsetzen; suite.json registriert jeden Helper und jede Paketdatei.
2. [status: done] Erfolgs-, Wiederholungs-, Frage-/Klärungs-, Stopp-, Pfad- und Fehlerfälle am gebauten Paket mit tatsächlichen Folgeverbrauchern prüfen und kanonische README-Fragmente regenerieren.
Evidence: Anzeige, Reporthelper und Paketprojektionen geprüft; unabhängiges Astra-Review bestätigte die Quelle.

### W-002 Der aktuelle Workflow besteht die vollständige technische und reale Abnahme

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0123]
Outcome: Der tatsächliche Workflow-Lauf arbeitet mit der neuen Anzeige und Laufdatei korrekt, mit belegten Grenzen der Hosttests.
Acceptance: Alle deklarierten Workflow-, Suite- und Shared-Tests bestehen. Alle vier aktuellen Paketvarianten und README-Projektionen stimmen mit der Quelle überein. Ein isolierter realer Lauf im gespeicherten Testprojekt nutzt das gebaute Paket und native Subagenten mit echtem READY/START, dateibasiertem Auftrag, Review/Korrektur, Punktwechsel, Nutzerfrage samt Antwort, Stopp/Wiederaufnahme und direkter Managerübergabe bei bestätigter Schreibruhe. Gemessene Grenzen verwenden tatsächlich zugeordnete frische Hosttelemetrie, Kinder beenden ihre vollständige Zuordnung. Der Runner unterdrückt doppelte Anzeigen und gibt am echten Abschluss dieselbe Laufdatei aus. Ein separater problemloser realer Abschluss enthält den vereinbarten Satz. Unbekannter Spawn, falsches oder fehlendes READY, fehlgeschlagenes START sowie widersprüchliche Übernahme werden durch real erzeugbare Fälle und kontrollierte Negativprüfungen getrennt ausgewiesen; nicht erzeugbare Transportzustände werden nicht als live bestanden behauptet. Die korrigierte aktuelle Quelle erhält eine unabhängige Astra-Medium-Prüfung, deren bestätigte Probleme automatisch korrigiert werden. Keine Tests schreiben außerhalb ihrer Fixture oder verändern laufende Projekte.
Steps:
1. [status: done] Vollständigen technischen Quellenlauf ausführen; Paketbestände, Helper und README-Ausgaben am einzigen aktuellen Build unter skills/temp/release/ prüfen.
2. [status: done] Isolierte Fixture im Testprojekt vorbereiten und die gebauten Manager- und Kindaufträge unverändert in native Werkzeugaufrufe übernehmen. Ereignisse, wirkliche Dateiänderungen, Kontrollzustände, Telemetrie und Grenzen in temp/2026-09-30-workflow-feedback/ sichern.
3. [status: done] Unabhängige Prüfung und erforderliche Korrekturen abschließen, betroffene fehlgeschlagene Fälle wiederholen und den finalen Build sowie Plan-Nachweise aktualisieren.
Evidence: Native Anzeige, Fragen, Stopp, Übergaben und sauberer Abschluss belegt. Kontrollierte Negativfälle beweisen keine nicht erzeugbaren Transportzustände.
