---
format_version: 1
id: PLAN-0015
status: draft
created: 2026-09-26
updated: 2026-09-26
---

# Scoville Workflow für Claude Code mit nativen Subagenten

## Goal

Die Suite erhält eine Claude-Code-Ausgabe, in der dasselbe vereinfachte Prinzip wie nach PLAN-0014 gilt. Die Hauptunterhaltung ist nur ein schlanker Starter; der Coordinator läuft selbst als Subagent, und jeder Step wird von einem eigenen Worker-Subagenten darunter erledigt, der nur seinen Step erhält, sein Ergebnis als abschließende Antwort zurückgibt und danach endet. Die Kontextschwellen der Suite bleiben der Kern: Der Coordinator übergibt an einer akzeptierten Einheit ab 25 Prozent, Worker, Reviewer und Fixer über 75 Prozent an einen frischen Subagenten, jeweils bevor Auto-Compaction nötig wird. Auto-Compaction bleibt unverändert als Sicherheitsnetz eingeschaltet. Warten, Zustellung und Schließen übernimmt Claude Code selbst: Ein Vordergrund-Subagent blockiert ohne Modellaufrufe, ein Hintergrund-Subagent meldet sich mit einer Abschlussbenachrichtigung. Behalten wird nur, was nötig ist: nie mehr als ein schreibender Subagent gleichzeitig, verlässliche Ergebnisübernahme und sichere Wiederaufnahme. Grundlage sind die Befunde aus der [Codex-Analyse](../token-overhead-analyse-2026-09-26.md) und die umgesetzten Korrekturen aus PLAN-0014. Claude-Code-Fakten stammen aus code.claude.com/docs/en/sub-agents, abgerufen am 2026-09-26 (Abschnitte Frontmatter, Vorder- und Hintergrund, Verschachtelung, Kontext, Wiederaufnahme, Auto-Compaction), und werden in W-001 gegen die installierte Version geprüft.

## Non-goals

- Keine Nachbildung der Codex-Aufgabenwerkzeuge, keine eigene Warteschleife, kein Polling, keine Titel-, Handle- oder Archivierungsschicht.
- Auto-Compaction wird weder abgeschaltet noch in ihrer Schwelle verändert; DISABLE_COMPACT, CLAUDE_AUTOCOMPACT_PCT_OVERRIDE und CLAUDE_CODE_AUTO_COMPACT_WINDOW bleiben unberührt.
- Keine neue Hauptsitzung per claude -p aus einer Shell als Coordinator-Nachfolger.
- Kein Step-Bündeln: jeder Step bleibt ein eigener Subagent.
- Keine Änderung am Plan-Format, am Ergebnisformat SCOVILLE_RESULT_V1 oder an den Codex-Paketen.
- Keine Agent-Teams und keine Worktree-Isolation im Normalablauf; verschachtelt wird nur Coordinator-Subagent über Worker-Subagent, Worker selbst starten keine Subagenten.
- Keine Veröffentlichung vor bestandenem Release-Gate W-010.

## Work items

### W-001 Claude-Code-Verträge sind geprüft und offene Richtungen entschieden

Status: todo
Depends on: []
Blocked by: []
Decisions: []
Outcome: Alle Claude-Code-Eigenschaften, auf denen der Ablauf beruht, sind an der installierten Version belegt, und die offenen Richtungsfragen liegen als Decisions vor.
Acceptance: Belegt sind je mit Version und Beobachtung: Vordergrund-Subagent blockiert ohne Modellaufrufe des Aufrufers; Hintergrund-Subagent liefert eine Abschlussbenachrichtigung; der Subagent endet nach seiner Antwort; ein Coordinator-Subagent kann Worker-Subagenten starten und wartet auf deren Ergebnis, auch wenn sie im Hintergrund laufen; ein Subagent ohne Agent-Tool kann nicht verschachteln; Agent-Parameter für Modell und Frontmatter-Feld effort wirken; Frontmatter tools, disallowedTools, skills, maxTurns und omitClaudeMd wirken; ein Helper findet das eigene Subagent-Transkript unter ~/.claude/projects/<projekt>/<session>/subagents/ über einen eindeutigen Auftragsmarker und liest daraus die aktuelle Kontextgröße und das Modellfenster; Auto-Compaction greift nur als Sicherheitsnetz. Ebenfalls belegt ist, ob eine Compaction mit Fokusanweisung an einem gewählten sicheren Punkt ohne Nutzereingabe ausgelöst werden kann, etwa durch /compact als Eingabe im Headless- oder SDK-Betrieb oder durch Claude selbst; laut Dokumentation vom 2026-09-26 ist /compact ein Nutzerbefehl, und der PreCompact-Hook kann eine Compaction nur blockieren, nicht auslösen. Fünf proposed Decisions sind angenommen, abgelehnt oder überarbeitet: Verteilung als Plugin oder als Skills plus Agent-Dateien, technischer Schreibschutz des Reviewers, Coordinator als Subagent unter schlanker Hauptunterhaltung gegenüber gezielter Compaction an sicheren Punkten, Ask-Äquivalent für Claude Code und Projektanweisungen im Subagenten.
Steps:
1. Prüfe in einem Wegwerf-Projekt mit claude -p und interaktiv jede genannte Eigenschaft der installierten Claude-Code-Version, darunter zwei Verschachtelungsebenen im Vorder- und Hintergrund und das Auffinden des eigenen Transkripts per Marker, und halte Version, Befehl und beobachtetes Ergebnis in development/claude-code/capabilities.md fest.
2. Lege unter docs/decisions/ fünf proposed Decisions an: Plugin gegenüber Skills plus ~/.claude/agents (Plugin-Subagenten ignorieren permissionMode, hooks und mcpServers), Reviewer-Schreibschutz über tools ohne Edit und Write oder permissionMode plan, Coordinator-Rollover über frische Coordinator-Subagenten gegenüber vom Modell ausgelöster Compaction an akzeptierten Einheiten falls Schritt 1 diese belegt, Ask über Claude-Subagenten mit Modellwahl und optional Codex über die Codex-CLI als einzige Ausnahme, sowie omitClaudeMd gegenüber vollständigen Projektanweisungen im Subagenten.
Evidence: []
Next action: Ein Wegwerf-Projekt anlegen und den Vordergrund-Subagenten mit Nutzungsmessung prüfen.

### W-002 Build erzeugt ein eigenes Claude-Code-Profil

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der Suite-Build erzeugt ein Profil claude mit den portablen Skills, dem neuen Workflow-Member und den Subagent-Definitionen in der entschiedenen Verteilungsform.
Acceptance: suite.json und der Builder kennen das Profil claude. Code, Plan, UI und Handoff werden im allgemeinen Inhalt übernommen. Der neue Member scoville-workflow-for-claude und die Subagent-Dateien sind enthalten, die Codex-Member Workflow-for-Codex und Ask-for-Codex nicht. Pakete sind LF-normalisiert und reproduzierbar gebaut. Die Codex-Profile bleiben bytegleich.
Steps:
1. Ergänze suite.json und development/shared/build/build_suite.py um das Profil claude mit Mitgliederliste, Zielpfaden für Skills und Subagent-Dateien und README-Fragmenten unter development/readme/.
2. Lege members/scoville-workflow-for-claude/ mit Quellordner, development/tests und README-Fragmenten an und prüfe mit dem bestehenden Buildtest, dass beide Codex-Profile unverändert bleiben.
Evidence: []
Next action: Die Profilstruktur in suite.json für claude entwerfen.

### W-003 Coordinator, Worker, Reviewer und Fixer sind native Subagent-Definitionen

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Vier Subagent-Dateien legen Rolle, Werkzeuge, vorab geladene Skills und Rückgabevertrag fest.
Acceptance: scoville-coordinator hat Agent, TaskStop, SendMessage, Read, Grep, Glob, Edit, Write, Bash beziehungsweise PowerShell und Skill, lädt scoville-workflow-for-claude und scoville-plan vorab und gibt an der Rollover-Grenze context_handoff mit Verweis auf den Laufdatensatz zurück. scoville-worker und scoville-fixer haben Read, Grep, Glob, Edit, Write, Bash beziehungsweise PowerShell und Skill, aber kein Agent; sie laden scoville-code vorab. scoville-reviewer hat keine Schreibwerkzeuge und kein Agent und ist gemäß Decision technisch schreibgeschützt. Jeder Systemprompt enthält nur Rollenregeln, das Verbot, Plan-, Workflow- oder Handoff-Skills und andere Plan-Punkte zu laden, höchstens eine kurze Meldung pro Phase und die Pflicht, SCOVILLE_RESULT_V1 als letzte Antwort zurückzugeben. needs_user_decision wird zurückgegeben, weil Subagenten AskUserQuestion nicht haben.
Steps:
1. Schreibe unter members/scoville-workflow-for-claude/ die Dateien agents/scoville-coordinator.md, agents/scoville-worker.md, agents/scoville-reviewer.md und agents/scoville-fixer.md mit Frontmatter name, description, tools, disallowedTools, skills und dem kurzen Rollen-Systemprompt.
2. Übernimm Rückgaberegeln, Meldungsgrenzen und die Checkpoint-Regel an natürlichen Grenzen aus dem nach PLAN-0014 geltenden Codex-Worker-Prompt, ohne Zustellnachricht und Delivery-Referenz.
Evidence: []
Next action: Die Werkzeuglisten je Rolle gegen die in W-001 belegten Hintergrund-Werkzeuge abgleichen.

### W-004 Auftrag entsteht als Datei und der Dispatch braucht zwei Aufrufe

Status: todo
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Ein Helper schreibt den Auftrag eines Steps in eine Datei und liefert nur Pfad, Subagent-Typ, Beschreibung, Modell und Effort; der Coordinator übergibt dem Agent-Tool nur diesen Pfad.
Acceptance: Die Auftragsdatei unter .scoville/assignments/ enthält den unveränderten Step-Text, Status der direkten Abhängigkeiten, ID und Entscheidungssatz relevanter Decisions und optional kurze Zusatzfakten. Der Coordinator gibt den Auftrag weder aus noch tippt er ihn ab. Die Beschreibung folgt S-WORK-#n-W-NNN/STEP-N, S-REVW oder S-FIXR. Ein Dispatch besteht aus höchstens einem Helper-Aufruf und einem Agent-Aufruf. .scoville/assignments/ bleibt lokal und wird nach Ergebnisübernahme gelöscht.
Steps:
1. Ergänze den Dispatch-Builder aus PLAN-0014 um die Ausgabe für Claude Code, die die Auftragsdatei schreibt und ein JSON mit path, subagent_type, description, model und effort ausgibt, und lege ihn als Skript des neuen Members ab.
2. Beschreibe in der Coordinator-Referenz von scoville-workflow-for-claude den Aufruf als ein kopierbarer Befehl und einen Agent-Aufruf mit dem Prompt „Führe den Auftrag in <path> aus“.
Evidence: []
Next action: Die Ausgabeform des Codex-Builders nach PLAN-0014 W-004 übernehmen und um die Datei ergänzen.

### W-005 Coordinator-Ablauf nutzt nur Agent-Tool und native Rückgabe

Status: todo
Depends on: [W-004]
Blocked by: []
Decisions: []
Outcome: SKILL.md und eine Referenz von scoville-workflow-for-claude beschreiben den vollständigen Ablauf: Die Hauptunterhaltung startet einen Coordinator-Subagenten, dieser wählt den Step, startet den Worker, übernimmt das Ergebnis, steuert Review und Reparatur, schreibt den Plan fort und committet.
Acceptance: Die Hauptunterhaltung startet nur Coordinator-Subagenten, gibt deren kurze Rückmeldungen und Nutzerfragen weiter und liest weder Plan noch Transkripte. Der Coordinator startet nie zwei schreibende Subagenten gleichzeitig und startet einen Reviewer erst nach Ende des Workers. Er wartet ohne TaskOutput-, Monitor- oder sonstige Statusabfragen: im Vordergrund blockiert der Aufruf, im Hintergrund kommt die Abschlussbenachrichtigung. Das Ergebnis ist die letzte Antwort des Subagenten; ein Transkript wird nicht gelesen. Es gibt keinen Archivierungsschritt. Ein Stopp nutzt TaskStop für den aktiven Subagenten. Reparaturgrenze drei, Review-Pflicht bei Code und kritischer Doku und Plan-Hoheit des Coordinators bleiben wie nach PLAN-0014.
Steps:
1. Schreibe members/scoville-workflow-for-claude/scoville-workflow-for-claude/SKILL.md mit Aktivierung, dem kurzen Starterteil für die Hauptunterhaltung, Rollen, Konfiguration und Verweis auf eine einzige Ablaufreferenz für den Coordinator-Subagenten.
2. Schreibe references/operations.md mit dem Kernablauf auf Basis des nach PLAN-0014 geltenden Codex-Ablaufs, ersetze dort alle Codex-Aufgabenwerkzeuge durch Agent, TaskStop und die native Rückgabe und übernimm die wiederhergestellten Regeln gegen Polling und Dauerkommentare.
Evidence: []
Next action: Den Codex-Ablauf nach PLAN-0014 Schritt für Schritt auf Claude-Code-Werkzeuge abbilden.

### W-006 Kontextschwellen lösen frische Subagenten vor jeder Compaction aus

Status: todo
Depends on: [W-005]
Blocked by: []
Decisions: []
Outcome: Erreicht eine Rolle ihre Schwelle, arbeitet sie bis zum nächsten sicheren Punkt weiter und erhält dort einen frischen Kontext, sodass Auto-Compaction im Normalablauf nicht eintritt; die Wiederaufnahme funktioniert ohne Lesen alter Transkripte. Sichere Punkte sind für den Coordinator akzeptierte Einheiten und für Arbeitsrollen natürliche Grenzen mit gesichertem Zwischenstand.
Acceptance: Ein Checkpoint-Helper für Claude Code findet das eigene Subagent-Transkript über den Auftragsmarker und meldet rollover für den Coordinator an einer akzeptierten Einheit ab der konfigurierten Schwelle, Default 25 Prozent, und context_handoff für Worker, Reviewer und Fixer an natürlichen Grenzen über der Schwelle, Default 75 Prozent. Der Coordinator-Subagent gibt dann context_handoff an die Hauptunterhaltung zurück, die sofort einen frischen Coordinator-Subagenten mit Verweis auf .scoville/workflow.md startet; ein Worker-Handoff führt zu einem frischen Worker für den Rest. Fehlende oder unklare Messwerte werden gemeldet und nie geschätzt. .scoville/workflow.md enthält Lauf, Rollenzähler, aktuelle Einheit, aktiven Subagenten mit Agent-ID, Reparaturzähler und nächste Aktion. Ein mit maxTurns oder API-Fehler abgebrochener Subagent wird einmal per SendMessage fortgesetzt, sonst übernimmt ein frischer Subagent den Rest. Falls W-001 eine ohne Nutzereingabe ausgelöste Compaction mit Fokusanweisung belegt und die Decision sie wählt, ersetzt sie am sicheren Punkt den frischen Coordinator-Subagenten; der Fokus bewahrt dann nur Laufdatensatz, aktuelle Einheit und nächste Aktion. Auto-Compaction bleibt in jedem Fall als Sicherheitsnetz eingeschaltet und wird nicht per PreCompact-Hook blockiert.
Steps:
1. Portiere check_context_checkpoint.py aus scoville-workflow-for-codex als Skript des neuen Members, das statt Codex-Rollouts das eigene Subagent-Transkript per Marker liest und dieselben Schwellen und Ausgaben verwendet.
2. Beschreibe in references/operations.md von scoville-workflow-for-claude Checkpoint, Coordinator-Rollover über die Hauptunterhaltung, Worker-Handoff, Laufdatensatz, Wiederaufnahme nach Neustart und die einmalige Fortsetzung abgebrochener Subagenten.
Evidence: []
Next action: Den Transkriptmarker und die Nutzungsfelder aus W-001 in den Checkpoint-Helper übernehmen.

### W-007 Modellwahl ist über dieselbe Projektkonfiguration einstellbar

Status: todo
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Routen werden für Claude Code auf Modell und Effort abgebildet und in .scoville/config.json gepflegt.
Acceptance: Das Claude-Profil liefert Defaults für execute und review je Route mit Claude-Modellalias oder voller Modell-ID und Effort low bis max sowie die Kontextschwellen coordinator_percent 25 und worker_percent 75. .scoville/config.json kann sie unter einem eigenen Abschnitt für Claude überschreiben, ohne die Codex-Werte zu berühren. Scoville Setup zeigt und speichert beide Abschnitte. Ungültige Werte melden einen Fehler statt ersetzt zu werden.
Steps:
1. Lege die Defaults als assets/workflow.toml von scoville-workflow-for-claude an und erweitere die gemeinsame Konfigurationsladung um den Claude-Abschnitt.
2. Erweitere members/scoville-setup/ um Anzeige und Speichern des Claude-Abschnitts und passe dessen Tests an.
Evidence: []
Next action: Den Namen des Konfigurationsabschnitts und die Effort-Werte aus W-001 festlegen.

### W-008 Ask hat ein natives Claude-Code-Gegenstück

Status: todo
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Gemäß der Ask-Decision aus W-001 holt Claude Code unabhängige Zweitmeinungen über einen schreibgeschützten Adviser-Subagenten mit gewähltem Modell.
Acceptance: Ein Subagent scoville-adviser ohne Schreibwerkzeuge erhält eine eigenständige Frage ohne Urteil des Aufrufers und gibt die Antwort als letzte Nachricht zurück. Mehrere Advisers laufen parallel, weil sie nicht schreiben. Die Modellwahl kommt aus der Konfiguration oder der Anfrage und wird nicht still ersetzt. Falls die Decision einen externen Codex-Adviser erlaubt, läuft er ausschließlich über die Codex-CLI als einzige Ausnahme.
Steps:
1. Lege den Adviser-Subagenten und einen schlanken Ask-Skill für das Claude-Profil an, der Modus, Frage und Advisers bestimmt und die Antworten zusammenführt.
2. Falls entschieden, ergänze den Codex-CLI-Aufruf als eigene kurze Referenz mit festen Argumenten und Zeitgrenze.
Evidence: []
Next action: Nach der Ask-Decision aus W-001 den Umfang des Claude-Ask-Skills festlegen.

### W-009 Einzel- und Ende-zu-Ende-Tests halten harte Grenzen ein

Status: todo
Depends on: [W-006, W-007, W-008]
Blocked by: []
Decisions: []
Outcome: Helper und Subagenten sind einzeln und im vollständigen Ablauf in Claude Code gemessen.
Acceptance: Jeder Helper im Claude-Profil wird mit claude -p und dem kleinsten Zielmodell im ersten Versuch ohne --help und ohne Usage-Fehler aufgerufen. Ein Fixture mit mindestens drei Steps läuft interaktiv und headless mit Worker, Review, Reparatur, je einem schwellenausgelösten Coordinator- und Worker-Rollover mit niedrigen Testschwellen, einem abgebrochenen und fortgesetzten Subagenten, Stopp und Wiederaufnahme sowie einer Ask-Konsultation. Harte Grenzen: null Auto-Compaction-Ereignisse in Coordinator- und Worker-Transkripten bei Standardschwellen, null Statusabfragen auf laufende Subagenten, nie zwei schreibende Subagenten gleichzeitig, jeder Subagent endet nach seiner Rückgabe, Worker höchstens eine Meldung pro Phase, Dispatch höchstens zwei Tool-Aufrufe, kein Lesen fremder Subagent-Transkripte außer dem eigenen durch den Checkpoint-Helper. Gemessen werden Coordinator-Aufrufe und Input pro Step aus den Transkripten.
Steps:
1. Passe das Rollout-Analyseskript aus PLAN-0014 W-001 an die Claude-Code-Transkripte der Hauptsitzung und unter subagents/ an und prüfe es an einem kurzen Probelauf.
2. Führe die Helper-Einzeltests und den Fixture-Lauf aus und trage Messwerte und jede harte Grenze mit Transkriptzeile in docs/claude-code-subagenten-nachweis.md ein.
Evidence: []
Next action: Das Analyseskript für Transkripte unter ~/.claude/projects anpassen.

### W-010 Release erst nach eingehaltenen Grenzen

Status: todo
Depends on: [W-009]
Blocked by: []
Decisions: []
Outcome: Das Claude-Code-Profil wird nur veröffentlicht, wenn W-009 alle Grenzen einhält und Installation und Nutzung dokumentiert sind.
Acceptance: Eine Checkliste belegt jede harte Grenze mit Transkriptzeile. README-Fragmente beschreiben Installation für Claude Code in der entschiedenen Verteilungsform, Aktivierung und Konfiguration. Bei einer verletzten Grenze bleibt die Veröffentlichung gesperrt und der Befund wird als neuer Work Item geplant.
Steps:
1. Erstelle die Release-Checkliste in docs/claude-code-subagenten-nachweis.md aus W-009 und entscheide die Freigabe nur bei vollständig eingehaltenen Grenzen.
2. Erzeuge die README-Projektionen des Claude-Profils über den Builder und prüfe eine frische Installation in einem leeren Claude-Code-Benutzerprofil.
Evidence: []
Next action: Nach W-009 die Grenzwerte in die Checkliste übertragen.
