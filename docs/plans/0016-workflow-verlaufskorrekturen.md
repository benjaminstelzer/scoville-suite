---
format_version: 1
id: PLAN-0016
status: completed
created: 2026-09-26
updated: 2026-09-26
---

# Workflow nach dem DIVI-Verlauf gezielt korrigieren

## Goal

Der Codex-Workflow liefert verlässliche Prüfergebnisse, hält Rollen und Fortsetzungsdaten korrekt und vermeidet doppelte Aufträge sowie wiederholtes Kontextladen. Grundlage ist die lesende Analyse von DIVI PLAN-0012, Managern #5–#7 und Workern #6–#8 am 2026-09-26. Korrekturen bleiben klein und nutzen bestehende native Werkzeuge. Bereits funktionierende Nachrichten, geordnete Steps und Kontextübergaben bleiben erhalten. PLAN-0014 bleibt abgeschlossene Historie.

## Non-goals

- Keine neue Orchestrierung, Cursor-Schemata, Validatoren, Polling-, Bestätigungs- oder Recovery-Schicht.
- Keine Änderung der Kontextschwellen, kein Pflicht-Rollover nach nativer Kompaktierung und keine Archivierungsnachprüfung.
- Keine Bearbeitung laufender DIVI-Chats oder Produktdateien, keine globale Zeilenendenmigration.
- Keine Änderung der Ask-Routen, von PLAN-0015 oder der projektspezifischen konsolidierten Review-Regel.
- Keine Installation in reguläre Skills, Veröffentlichung oder Releasefreigabe.

## Work items

### W-001 Prüfungen erhalten ihren tatsächlichen Fehlerstatus

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0084, ADR-0089]
Outcome: Ein später erfolgreicher Shell-Befehl verdeckt keine fehlgeschlagene Pflichtprüfung. Kleine Quelländerungen lösen keine dateiweite Zeilenendenkorrektur aus.
Acceptance: Ein isolierter Versuch mit fehlgeschlagener Prüfung und nachfolgend erfolgreichem Befehl bleibt als Fehler erkennbar; eine erfolgreiche Prüfung bleibt erfolgreich. Ein kleiner Edit an einer Datei mit gemischten Zeilenenden verändert nur die beauftragten Zeilen. Die ausführende Rolle erkennt beide Fälle ohne Reparatur der Helper-Rückgabe. Keine neue Shell-Abstraktion entsteht.
Steps:
1. Prüfe die betroffenen bestehenden Regeln unter members/scoville-code/scoville-code/references/ und den Workflow-Dispatch gegen die beobachteten Befehlsfolgen. Präzisiere beim zuständigen Owner kurz: Einzelstatus auswerten oder bei Fehler abbrechen; vorhandene Zeilenenden außerhalb des Edits erhalten. Berücksichtige im Fixture bereits gemischte Repository-Zeilenenden und aktiviertes core.autocrlf; ändere keine globale Git-Konfiguration. Kopiere diese Regeln nicht in alle Skills.
2. Prüfe beide Fehlerfälle in einem isolierten Fixture mit den dokumentierten Aufrufen und dem tatsächlich konsumierenden Agenten. Halte Aufruf, Einzelstatus und unveränderte Dateibereiche als knappe Evidenz fest.
Evidence: SOL 6 Medium erkannte Exit 7 und 0 und erreichte nach dem begrenzten Edit zweimal Exit 0. Bytevergleich und Testnachweis unter development/luna-tests/workflow-fixplan16-evidence.md.

### W-002 Manager hält Rollen und aktuellen Laufzeiger eindeutig

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0084, ADR-0092]
Outcome: Der Manager delegiert Quellkorrekturen und hält einen kleinen widerspruchsfreien Wiederaufnahmestand im bestehenden Markdown-Laufzeiger.
Acceptance: Im isolierten Ablauf übernimmt der Manager keine Produktänderung, auch keine mechanische Zeilenendenkorrektur. Eine notwendige Korrektur geht an die zuständige Worker-Rolle nach dem vorhandenen Verfahren. Nach Dispatch stimmen Rollen-Zähler, Einheit, aktive Task-ID und nächste Aktion überein. Nach Rollover setzt der Nachfolger anhand des aktuellen Standes fort, ohne erledigte Arbeit oder eine bereits angelegte Task zu wiederholen. Historische Ergebnisse bleiben in ihren vorhandenen Belegen verfügbar, überholte aktive Angaben werden ersetzt statt angehängt.
Steps:
1. Präzisiere members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md und die betroffenen Dispatch-/Rollover-Regeln nur an den vorhandenen Zuständigkeits- und Schreibstellen. Behalte das einfache Cursor-Format bei.
2. Prüfe Dispatch, Ergebnisübernahme und Rollover mit einem absichtlich veralteten Cursor-Feld sowie einer notwendigen Quellkorrektur. Belege eindeutigen Folgezustand und eingehaltene Rollen ohne zusätzlichen Kontrollaufruf.
Evidence: SOL 6 Medium besteht Rollenprobe und native Fortsetzung; Abschlusscursor nach gezielter Korrektur eindeutig. Nachweis unter development/luna-tests/workflow-fixplan16-evidence.md.

### W-003 Aufträge und Übernahmen verbrauchen nur nötigen Kontext

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0084, ADR-0089, ADR-0093]
Outcome: Ein vollständiger Auftrag gelangt einmal direkt vom Builder zum nativen Start; der Manager liest nur benötigte, noch fehlende Informationen.
Acceptance: Das Toolprotokoll enthält keine zusätzliche vollständige Builder-Ausgabe vor create_thread. Der erzeugte Auftrag wird ohne manuelle Rekonstruktion oder Kürzung übergeben. Work Item, zugewiesene Einheit, notwendige Goals/Non-goals, geltende ADR-Vorgaben, Abhängigkeitsergebnisse und tatsächliche Nachrichtenautorisierung bleiben erhalten. Zusatzkontext wiederholt keine bereits enthaltene Checkpoint- oder Zustellregel. Unveränderte Verträge und identische Auswahlen werden nicht erneut geladen; Vorgängerchats nur für eine benannte fehlende Information. Erforderliche Hostmeldungen und Fortschrittswarteaufrufe bleiben erhalten, ohne laufende Prozessnarration.
Steps:
1. Bewahre die bereits korrekte direkte Build-und-Start-Codezelle in references/operations-dispatch.md. Entferne nur belegte Kontextwiederholungen und gleiche operations.md, operations-rollover.md sowie scripts/build_dispatch_prompt.py damit ab; kein neuer Dispatch-Wrapper.
2. Prüfe einen Erstauftrag und eine Fortsetzung mit einem real konsumierenden Agenten. Vergleiche den tatsächlich übergebenen Auftrag mit dem Builder-Ergebnis und kontrolliere den Toolverlauf auf Doppel-Ausgaben, wiederholte Auswahl und unnötige Vorgängerlektüre.
Evidence: Fünf native Dispatches ohne zusätzliche Auftragsausgabe; Rohprotokoll korrigiert früheren Doppel-Ausgabebefund. Nachweis unter development/luna-tests/workflow-fixplan16-evidence.md.

### W-004 Gemeinsamer Ablauf bestätigt Korrekturen und Kosten

Status: done
Depends on: [W-001, W-002, W-003]
Blocked by: []
Decisions: [ADR-0084, ADR-0092, ADR-0093]
Outcome: Ein kurzer isolierter Modelllauf zeigt, dass die Korrekturen zusammen funktionieren und den Ablauf nicht aufblähen.
Acceptance: Ein zusammenhängender Versuch umfasst geordnete Arbeit, einen sichtbaren Prüffehler, eine Worker-Korrektur, Ergebniszustellung, Kontextübergabe und Fortsetzung. Kein zweiter gleichzeitiger Schreiber, keine verfrühte Abnahme und keine doppelte Erledigung. Das verwendete Modell und die Denktiefe sind dokumentiert. Verfügbare Tokenwerte, Auftrag-/Rückgabelängen, doppelte Ausgaben/Leseaufrufe und Übergabedauer werden mit klarer Zählweise berichtet; Kontextbelegung gilt nicht als Gesamtkosten. Fehlende Telemetrie bleibt unbekannt. Geänderte Helper-Ausgaben werden direkt verwendet. Struktur- und relevante bestehende Tests bestehen; verbleibende Modell- oder Hostgrenzen sind ausdrücklich benannt.
Steps:
1. Baue einen isolierten Kandidaten aus den kanonischen Quellen. Verwende ein kleines Fixture für den gemeinsamen Versuch; wiederhole keine unveränderten Einzelprüfungen und führe keinen vollständigen Release-Gate-Lauf aus.
2. Werte die tatsächlichen Aktionen und Ausgaben gegen W-001 bis W-003 aus. Halte Befunde und Kosten knapp unter development/luna-tests/ fest. Behebe nur nachgewiesene Abweichungen und wiederhole nur betroffene Fälle.
Evidence: Native SOL-6-Medium-Prüfungen mit Reviews bestanden; Bytevergleich und Fortsetzung korrekt. Kosten und Testgrenzen unter development/luna-tests/workflow-fixplan16-evidence.md.
