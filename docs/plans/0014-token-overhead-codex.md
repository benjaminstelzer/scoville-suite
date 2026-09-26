---
format_version: 1
id: PLAN-0014
status: completed
created: 2026-09-26
updated: 2026-09-26
---

# Token-Overhead der Suite in Codex mit nativen Mitteln beseitigen

## Goal

Codex steuert Workflow und die in Scoville integrierten Ask-Skills direkt mit seinen Aufgabenwerkzeugen. Native Ask-Adviser behalten jeweils einen eigenen Chat. Worker erhalten einen vollständigen kompakten Auftrag. Der Coordinator wartet ohne Polling und übernimmt Ergebnisse aus Nachrichten. Der bestehende Laufdatensatz hält den nötigen Wiederaufnahmestand; es gibt höchstens einen schreibenden Task. Erforderliche Verhaltensregeln bleiben erhalten. Dieser Entwurf konkretisiert PLAN-0012 W-017; Installation und Veröffentlichung bleiben im dortigen Ablauf. Die Helper-Abnahme umfasst auf ausdrückliche Erweiterung alle Skills unter skills/private einschließlich benjaminstelzer-github; Skills ohne Helper werden im Inventar ausgewiesen. Die historische [Analyse](../token-overhead-analyse-2026-09-26.md) liefert die Ausgangswerte, die verbindlichen Zielkriterien stehen hier.

## Non-goals

- Keine neue Orchestrierungs-, Recovery- oder Bestätigungsschicht, keine Handle-Wrapper und keine zusätzlichen Laufzeitbelege.
- Keine ungeordnete oder überlappende Bearbeitung. Neue Dispatches dürfen gemäß ADR-0093 zusammenhängende Steps gruppieren.
- Keine Änderung am Plan-Format oder der Claude-CLI-Route. SCOVILLE_RESULT_V1 behält seine sachlichen Pflichtinformationen; kosmetische Abweichungen erfordern keine Korrekturrunde.
- Keine Änderung an laufenden Sessions, regulär installierten Skills oder Projektdateien von DIVI5; isolierte Testinstallationen sind erlaubt.
- Keine Veröffentlichung oder zweite Releasefreigabe durch diesen Plan. W-010 übergibt die Nachweise an PLAN-0012 W-017.
- Keine starre Tokenquote und kein pauschales Verbot gezielter Statusabfragen zur Wiederaufnahme.
- Kein Überschreiben des unkommittierten ADR-0083-Entwurfs ohne vorherigen Abgleich in W-001.

## Work items

### W-001 Ausgangsstand und laufender Entwurf sind abgeglichen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0083, ADR-0084]
Outcome: Der unkommittierte ADR-0083-Entwurf ist gegen die Befunde P1 bis P9 eingeordnet und die Ausgangsmessung ist reproduzierbar gesichert.
Acceptance: Für jede Datei des Entwurfs ist festgehalten, welcher Befund adressiert wird und welcher offen bleibt. Das Analyseskript und seine Auswahl der drei Läufe liegen im Entwicklungsordner und liefern die Tabelle aus Abschnitt 2 der Analyse erneut. Keine laufende Session wurde verändert.
Steps:
1. Vergleiche die unkommittierten Änderungen in members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md, references/operations.md, references/operations-dispatch.md, references/operations-rollover.md und scripts/build_dispatch_prompt.py mit den Befunden der Analyse und ergänze deren Statusspalte.
2. Lege das Rollout-Analyseskript unter development/luna-tests/ ab, das Tool-Aufrufe nach Name, Warteabstände, Meldungsarten, input_tokens, Ausgaben über 10k Zeichen, Doppel-Lesen, Helper-Fehler und Dispatch-Dauer zählt, und prüfe es gegen die drei Läufe der Analyse.
Evidence: [ADR-0086 erlaubt korrigierte Ausgangswerte; development/luna-tests/token-overhead-implementation.md dokumentiert Entwurfsabgleich und reproduzierte Kernwerte.]

### W-002 Coordinator wartet idle und wird vom Worker geweckt

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0083, ADR-0084]
Outcome: Ein kleiner realer Versuch bestätigt Ergebniszustellung und Aufwecken, bevor der normale Workflow auf direkte Nachrichten umgestellt wird.
Acceptance: Ein isolierter Worker beendet seine Arbeit, sendet einmal SCOVILLE_RESULT_V1 mit send_message_to_thread an den Coordinator und liefert danach dieselbe Final-Antwort ohne weitere Arbeit. Der zuvor beendete Coordinator-Turn wird durch die Nachricht fortgesetzt; Task-ID und Einheit stimmen. operations.md verlangt im Normalablauf weder Polling noch read_thread oder wait_threads. Ergebnis und nächste Aktion werden vor Annahme oder Archivierung gesichert. Ein fehlgeschlagener Versand bleibt in der Worker-Final-Antwort sichtbar; Wiederaufnahme folgt W-005. Ein weitergeleiteter Stopp gilt erst nach beobachtetem Stillstand als wirksam. Hostpflichten für Fortschrittsmeldungen bleiben erhalten, unnötige Meldungen entfallen.
Steps:
1. Prüfe mit einem isolierten nativen Task Erstellung, Turn-Ende, Nachricht und Aufwecken. Sichere Task-IDs und Ergebnis unter development/luna-tests/suite-simplification-comparison.md. Bei fehlendem Nachweis bleibt die Umstellung offen.
2. Ersetze nach bestandenem Versuch in members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md den normalen Warte- und Leseablauf durch direkte Nachrichtenübernahme. Passe scripts/build_dispatch_prompt.py an; ein fehlgeschlagener Versand löst keine automatische Wiederholung aus.
3. Stelle die in e5fe414 entfernten Regeln gegen Polling, wiederholte Kommentare und Sichtbarkeitsprüfungen kurz in operations.md und im Worker-Prompt wieder her, soweit sie mit den aktuellen Hostvorgaben vereinbar sind.
Evidence: [development/luna-tests/token-overhead-implementation.md: Zwei native Zustellproben bestanden; direkte Übernahme umgesetzt; acht Workflow-Vertragstests bestanden.]

### W-003 Workflow ruft native Aufgabenwerkzeuge ohne Zwischenschichten auf

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0083, ADR-0084]
Outcome: create_thread, set_thread_archived, set_thread_title und send_message_to_thread werden direkt verwendet; task_lifecycle.py und parse_role_result.py sind nicht mehr im Laufzeitpfad von Workflow.
Acceptance: Kein Workflow-Kommunikationsschritt verlangt task_lifecycle.py, creation_result, verify_archive, match_delivery oder Shell-/Encoding-Übergaben. Prompt-Erzeugung und create_thread erfolgen ohne Ausgabe des vollständigen Prompts an das Modell. Archivierung prüft die Antwort direkt auf die erwartete Task-ID und archived:true. Wenige Anweisungssätze erhalten die vollständige SCOVILLE_RESULT_V1-Prüfung: Kopf, Rolle, Status, Pflichtfelder einschließlich Review-Indikatoren, Feldreihenfolge, zulässige Wiederholungen und Größenlimits. Ungültige Ergebnisse werden nicht angenommen. parse_role_result.py bleibt höchstens für Tests und Diagnose.
Steps:
1. Entferne in references/operations.md, references/operations-dispatch.md und SKILL.md unter members/scoville-workflow-for-codex/scoville-workflow-for-codex/ alle Lifecycle-Helper-Operationen und ersetze sie durch die direkten nativen Aufrufe mit einem kurzen Beispiel für die gemeinsame Code-Zelle.
2. Entferne task_lifecycle.py und task_lifecycle.md aus den shared_helpers von Workflow in suite.json, sofern kein verbleibender Laufzeitaufruf sie braucht, und halte parse_role_result.py aus dem beschriebenen Ablauf heraus.
3. Prüfe die direkte Ergebnisannahme mit einem gültigen Ergebnis sowie fehlenden Pflichtfeldern und unzulässigem Status. Erhalte die bestehende Fehlerbehandlung ohne neue Bestätigungskette.
Evidence: [Direkte native Aufrufe dokumentiert; Lifecycle-Manifestabhängigkeit und Builder-Parserimport entfernt; acht Workflow-Vertragstests bestanden.]

### W-004 Worker erhält nur seinen Step und wird schnell erstellt

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0083, ADR-0084]
Outcome: Jeder Worker erhält genau seinen Step mit den nötigen Abnahmekriterien und Einschränkungen; Codex erstellt und verwaltet den Task direkt.
Acceptance: Der Auftrag enthält unveränderten Step-Text, relevantes Outcome und Acceptance, nötige Abhängigkeitsfakten und Entscheidungssätze. Reviewer erhalten zusätzlich das Worker-Ergebnis, Reparatur- und Rollover-Aufträge ihre nötigen Befunde beziehungsweise Restarbeit. Kein vollständiger Plan oder Decision-Record wird übertragen oder nachgeladen. Ein verbleibender Builder stellt nur den Auftrag zusammen; er verwaltet keine Tasks, Zustellungen oder Archivierungen. Modell und Reasoning kommen aus der bestehenden Konfiguration. Prompt und deterministische Zwischenergebnisse werden nicht wiederholt ausgegeben. Jeder Step bleibt ein eigener Worker.
Steps:
1. Beschränke members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py auf die kompakte Auftragszusammenstellung. Leite bekannte Pfade ab und dokumentiere unvermeidbare Eingaben vollständig; füge keine Lifecycle- oder Modellauflösungsschicht hinzu.
2. Dokumentiere in references/operations-dispatch.md den direkten create_thread-Aufruf mit dem Auftrag und dem bestehenden konfigurierten Modellpaar. Entferne doppelte Prompt-Ausgaben und unnötige Zwischenschritte.
3. Prüfe einen Step, dessen entscheidende Anforderung ausschließlich in Acceptance steht, und einen Reviewer-Auftrag. Beide müssen ohne Nachladen des Plans vollständig verständlich sein. Projekt- und Code-Regeln bleiben anwendbar.
Evidence: [Builder liefert direktes Prompt-JSON mit Outcome und Acceptance; gebündelter Selector und acht Vertragstests einschließlich Unicode und CRLF bestanden.]

### W-005 Kleiner Laufdatensatz ermöglicht Rollover und Wiederaufnahme

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0083, ADR-0084]
Outcome: Der bestehende Laufdatensatz reicht zur Fortsetzung ohne vollständiges Lesen des Vorgängers oder neue Recovery-Helper.
Acceptance: .scoville/workflow.md hält aktive Task-ID mit nötiger Hostzuordnung, zugewiesenen Step, zuletzt gesichertes Ergebnis und nächste Aktion sowie unverzichtbare bestehende Laufidentität und Rollenzähler. Normale Übergaben lesen keine Vorgängerkonversation. Nach Unterbrechung oder fehlender Zustellung ist ein gezielter Abgleich des bekannten Tasks mit read_thread oder einer Statusabfrage erlaubt; keine periodische Schleife und kein Ersatz-Task bei ungeklärter Erstellung. Ein bereits gesichertes Ergebnis wird nicht erneut angenommen. Der Vorgänger sichert nach create_thread nur die tatsächliche Nachfolger-ID und endet; der Nachfolger schreibt erst nach beobachtetem Vorgängerende; Worker beenden ihre Arbeit vor der Ergebnisnachricht. Automatischer Coordinator- und Worker-Rollover bleiben erhalten, ohne zwei schreibende Tasks.
Steps:
1. Kürze members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations-rollover.md auf Skill-Aufruf, Laufdatensatz und Vorgänger-ID. Sichere die Fortsetzung vor create_thread und danach ausschließlich die zurückgegebene Nachfolger-ID; archiviere den beendeten Vorgänger einmal direkt.
2. Beschreibe in references/operations.md die Wiederaufnahme anhand des kleinen Laufdatensatzes. Fehlende Zustellung und unklarer Taskstatus erlauben gezielte native Abfragen; ungelöster Zustand bleibt sichtbar und blockiert weitere schreibende Tasks.
Evidence: [operations-rollover.md und operations.md behalten kleinen Laufdatensatz; direkte Ergebnisübernahme und einmalige Übernahmeprüfung ohne Vorgängerchat; reale Gesamtprüfung folgt W-009.]

### W-011 Übergaben verwenden Klartext mit Ausnahme von Ask Claude

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0087]
Outcome: Die verworfene JSON-Übergabe ist aus dem Builder und den begonnenen nativen Ask-Rückgaben entfernt.
Acceptance: AGENTS.md hält die Regel fest. Builder-Aufträge und optionale Zusatzdateien sind Klartext; keine JSON-Wrapper im Prompt oder in der Ausgabe. Native Ask-Konfiguration wird agentenseitig als Klartext zurückgegeben. Ask Claude behält seine JSON-Schnittstelle. Direkte Weiterverwendung einschließlich Unicode und Zeilenumbrüchen ist geprüft.
Steps:
1. Korrigiere build_dispatch_prompt.py und operations-dispatch.md auf Klartextausgabe und Klartextdateien für Rollenresultate sowie Restarbeit; passe die betroffenen Vertragstests an.
2. Korrigiere die native resolve-Rückgabe von ask.py und die Aufrufdokumentation auf Klartext, ohne Ask Claude zu ändern. Prüfe die gezielten Ausgabeverträge.
Evidence: [ADR-0088 begrenzt die Formatkorrektur auf Dispatch; acht Workflow-Tests und drei Claude-Timeouttests bestanden; technische Ask-JSON-Rückgabe erhalten.]

### W-006 Integrierte Ask-Skills nutzen eigene native Chats

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0083, ADR-0084, ADR-0085]
Outcome: Die in Scoville integrierten nativen Ask-Skills verwenden eigene Codex-Chats mit direkter Kommunikation und ohne zusätzliche Lifecycle-Schicht.
Acceptance: Die integrierten Ask-Quellen unter members/scoville-ask-for-codex und ihre gemeinsamen Helper sind erfasst und angepasst. Jeder native Adviser erhält einen eigenen Chat über create_thread und antwortet mit send_message_to_thread; Subagenten sind kein Ersatz. Hostvorgaben für ausdrückliche Chatbeauftragung werden eingehalten, ein fehlender Auftrag wird benannt. Es gibt keine prepare-, creation_result-, match_delivery-, verify_archive- oder Encoding-Schicht und keine Warteschleife. Der Aufrufer ordnet Antworten dem bekannten Adviser und seiner Frage zu und erhält einzelne Fehler sowie bestehende Follow-up- und Archivierungsrechte. Fehlende Antworten erlauben einen gezielten Abgleich des bekannten Tasks ohne automatische Neuerstellung. Die Modellprüfung erfolgt durch den Host; Fehler werden gemeldet, nie durch ein anderes Modell ersetzt. ask.py claude und der Titel Ask <Modell> · <Aufrufertitel> bleiben unverändert.
Steps:
1. Erfasse die integrierten Ask-Quellen anhand von suite.json und gemeinsame Helper in ../shared; ändere deren kanonische Quellen statt generierter Kopien. Ersetze in members/scoville-ask-for-codex/scoville-ask-for-codex/SKILL.md und references/native.md den prepare-, creation_result- und Warteablauf durch direkten create_thread-Aufruf je Adviser mit adviser.md-Rolle und Frage und idle Warten auf die Adviser-Nachrichten.
2. Beschränke scripts/ask.py im nativen Weg auf das Auflösen der Konfiguration und entferne den Pflichtaufruf von list_models.py vor jedem Dispatch.
Evidence: [Native Ask verwendet direkte eigene Chats; Auflösung startet keinen Katalogprozess; Lifecycle-Abhängigkeit entfernt; 21 Ask-Tests einschließlich Claude-Route bestanden.]

### W-007 Verbleibende Helper haben eindeutige kurze Verträge

Status: done
Depends on: [W-004, W-006]
Blocked by: []
Decisions: [ADR-0083, ADR-0084, ADR-0085, ADR-0089]
Outcome: Jeder verbleibende Helper lässt sich ohne --help korrekt aufrufen und liefert ein direkt verwendbares Ergebnis oder eine eindeutige Diagnose.
Acceptance: Jeder Helper aus Scoville einschließlich der integrierten Ask-Skills hat einen kurzen Rückgabevertrag mit dokumentierter nächster Verwendung. Rückgaben benötigen keine modellseitige Reparatur, Ergänzung fehlender Pflichtinformationen, unnötige Umformatierung oder wiederholte Nachfrage; dokumentiertes Auslesen und Parsen bleibt erlaubt. Agenten müssen keine JSON-Anfragen oder Übergaben manuell schreiben. Helper-JSON darf gelesen werden; Konfiguration und technische Parameter dürfen JSON bleiben. Ask Claude bleibt erhalten. select_context.py hat --format mit Default json. Jede Aufrufstelle in Workflow, Ask, Plan und Setup ist kopierbar vollständig und besteht einen automatischen Signaturabgleich gegen argparse. Die Doku von task_lifecycle.md benennt Felder mit exaktem Namen, falls die Datei für Ask-Tests erhalten bleibt. Die Legacy-guard.json-Regel ist aus SKILL.md entfernt.
Steps:
1. Setze in members/scoville-plan/scoville-plan/scripts/select_context.py den Default von --format auf json und passe die zugehörigen Tests an.
2. Ergänze unter development/tests einen Test, der alle dokumentierten Helper-Aufrufe in Laufzeit-Markdown und Worker-Prompt gegen die argparse-Signaturen prüft, und entferne die Legacy-guard.json-Anweisung aus members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md.
Evidence: [Helper-Verträge und Setup-Serialisierung dokumentiert; zwei Signaturtests sowie 31 Suite- und 55 Shared-Tests bestanden; private-helper-inventory.md erfasst Quellen.]

### W-008 Jeder Helper besteht einen Luna-6-Medium-Einzeltest

Status: done
Depends on: [W-005, W-007]
Blocked by: []
Decisions: [ADR-0083, ADR-0084, ADR-0085, ADR-0089]
Outcome: Jeder verbleibende Helper wird von gpt-6-luna medium nur mit den Skill-Anweisungen korrekt aufgerufen.
Acceptance: Der korrigierte Kandidat ist vor den Tests gebaut und isoliert installiert; Paketstand und Testinstallation sind benannt. Jeder verbleibende Laufzeithelper und seine dokumentierten Aufrufarten aus Workflow, den integrierten Ask-Skills, Plan und Setup sind inventarisiert und mit gpt-6-luna medium tatsächlich ausgeführt. Dazu gehören, soweit verbleibend, Builder, Modellauflösung, Checkpoint, Selector, Validator, ask.py resolve und claude sowie setup.py show und set. Grenzen: erster Aufruf korrekt, null --help, null Usage-Fehler, keine zusätzliche Encoding-Schicht für Kommunikation. Jeder Fall führt den dokumentierten Folgeschritt mit der tatsächlichen Rückgabe ohne modellseitige Reparatur oder Ergänzung aus; ein erfolgreicher Helper-Aufruf allein genügt nicht. Bei gültigen Eingaben führt jede erforderliche Reparatur von Text oder Code durch den Agenten zum Nichtbestehen; der tatsächliche nächste Verbraucher muss die unveränderte Ausgabe verwenden können. Eindeutige Diagnosen bei ungültigen Eingaben werden als Fehler behandelt und nicht zu Erfolg umgedeutet. Ergebnisse und Rohdaten stehen mit Task-ID im Vergleichsdokument.
Steps:
1. Baue den korrigierten Codex-Kandidaten mit development/build_suite.py unter skills/temp/release/ im Workspace und installiere ihn isoliert. Die integrierten Ask-Skills gehören zu diesem Kandidaten. Verändere keine reguläre Skill-Installation.
2. Lege je inventarisierter Aufrufart einen Fall für development/luna-tests/run_codex_cli_case.py an. Führe ihn mit der isolierten Paketversion, ihrer Skill-Anweisung und gpt-6-luna medium aus.
3. Werte die Läufe mit dem Analyseskript aus W-001 aus und trage Paketstand, Aufrufe, Fehler und Tokens in development/luna-tests/suite-simplification-comparison.md ein. Nach relevanten Korrekturen neu bauen und betroffene Prüfungen wiederholen.
Evidence: development/luna-tests/suite-simplification-comparison.md und private-helper-inventory.md ordnen Luna-Helpertests und finale SOL-Verbraucher zu; nativer Gruppenlauf samt beiden Rollovern bestanden.

### W-009 Nativer Ablauf und gezielte Wiederaufnahme sind belegt

Status: done
Depends on: [W-005, W-008]
Blocked by: []
Decisions: [ADR-0083, ADR-0084, ADR-0085, ADR-0089, ADR-0092, ADR-0093]
Outcome: Der geprüfte Kandidat belegt einen vollständigen nativen Ablauf und eine gezielte Wiederaufnahme mit weniger Coordinator-Arbeit.
Acceptance: Ein reales Fixture mit mindestens drei Steps zeigt Delegation, Idle, Aufwecken, Ergebnisannahme, Review, nachrichtenbasierten Coordinator-Rollover ohne Warteabfrage gemäß ADR-0092 und Worker-Rollover sowie native Fälle der integrierten Ask-Skills mit tatsächlich eigenen Adviser-Chats. Unterschiedliche native Aufrufverträge werden jeweils ausgeübt; identische gemeinsame Implementierungen brauchen keine doppelten Tests. Ein gezielter Unterbrechungsfall zeigt Stopp und Wiederaufnahme bei ausstehender Ergebniszustellung: vorhandenes Ergebnis sichern, keinen doppelten Worker erstellen und keine Arbeit doppelt annehmen. Beobachtet werden höchstens ein schreibender Task, keine periodischen Warteabfragen, keine doppelten Ausgaben: Der vollständige Builder-Auftrag erscheint nicht erst im Coordinator-Modellkontext und wird anschließend erneut für create_thread ausgeschrieben, keine unnötigen Planinhalte und keine Helper-Usage-Fehler. Gezielte Recovery-Abfragen werden separat ausgewiesen. Nach gesichertem Ergebnis wird die Archivierung für beendete Worker und Reviewer sowie übernommene Vorgänger-Coordinator ausgelöst. Gemäß ADR-0092 entfallen Archivierungsbestätigung und Nachprüfung. Der abschließende Coordinator bleibt sichtbar. Tatsächliche Dispatch- und Rückgabetexte enthalten nur den benötigten Planpunkt und minimalen notwendigen Zusatzkontext; vollständige Pläne oder Vorgängerchats werden nicht übertragen. Ein vergleichbarer Ausgangs- und Kandidatenlauf mit gleichem Fixture und Modellpaar zeigt weniger Coordinator-Modellaufrufe; Input, Dispatch-Dauer und Auftragsgröße werden ohne starre Tokenquote berichtet. Zusätzliche Nutzerfragen werden getrennt ausgewertet.
Steps:
1. Verwende den isolierten Kandidaten aus W-008. Führe den normalen Fixture-Ablauf und einen gezielten Unterbrechungsfall aus; dokumentiere tatsächliches Hostverhalten und Grenzen statt simulierten Erfolg.
2. Vergleiche einen isolierten Ausgangsstand und den Kandidaten mit demselben Fixture und Modellpaar. Werte mit dem Skript aus W-001 aus und ergänze docs/token-overhead-analyse-2026-09-26.md um Ergebnisse und getrennte Recovery-Aufrufe. Ersetze dort überholte Zielgrenzen durch Verweise auf diesen Plan; historische Messwerte bleiben erhalten.
Evidence: docs/token-overhead-analyse-2026-09-26.md: gleicher SOL-Vergleich 84 auf 41 Coordinator-Aufrufe; native Übergaben, Rollover und gezielte Wiederaufnahme belegt; Grenzen separat dokumentiert.

### W-012 Alle geänderten Skills sind mit SOL 6 Medium geprüft

Status: done
Depends on: [W-009]
Blocked by: []
Decisions: [ADR-0092, ADR-0093]
Outcome: Jeder durch PLAN-0014 geänderte Skill hat einen realistischen ausgeführten Test mit gpt-6-sol und medium.
Acceptance: Der finale isolierte Paketstand wird getestet. Workflow umfasst native Delegation und Ergebnisübernahme; Ask umfasst eigene Chats; Plan umfasst seine geänderten Helper-Aufrufe. Weitere tatsächlich geänderte Skills werden aufgenommen. Aufträge und Rollenresultate erfordern kein manuell geschriebenes JSON; technische Parameter und automatisch erzeugte Helper-Daten dürfen JSON sein. Reale Folgeschritte verwenden Helper-Rückgaben ohne Reparatur. Task-IDs, Modell-/Effort-Nachweise, Ergebnisse und Grenzen sind gesichert; Fehler bleiben offen.
Steps:
1. Ermittle die geänderten Skills aus dem tatsächlichen Diff und formuliere je Skill einen realistischen Fall im bestehenden isolierten Testbereich.
2. Führe die Fälle mit gpt-6-sol medium aus; prüfe Dateien, Tool-Aufrufe und Ergebnisse, sichere die Nachweise und korrigiere belegte Fehler vor gezielter Wiederholung.
Evidence: development/luna-tests/suite-simplification-comparison.md ordnet Workflow, Ask, Plan und Setup den finalen SOL-Tests zu; 104 Paketdateien bytegleich zum geprüften Staging.

### W-010 Nachweise gehen an den bestehenden Releaseplan zurück

Status: done
Depends on: [W-009, W-012]
Blocked by: []
Decisions: [ADR-0083, ADR-0084]
Outcome: PLAN-0012 W-017 erhält die Korrektur- und Testnachweise; der bestehende Releaseablauf bleibt alleiniger Owner für reguläre Installation und Veröffentlichung.
Acceptance: Ergebnisse aus W-008 und W-009 sind mit Paketstand, Task-IDs und Fundstellen den Kriterien von PLAN-0012 W-017 zugeordnet. Offene Kriterien und dessen nächste Aktion sind ausdrücklich benannt. W-017 wird erst nach seiner vollständigen Acceptance abgeschlossen; W-009 des Releaseplans wird nicht übersprungen oder vorzeitig fortgesetzt. Dieser Plan verändert keine regulär installierten Skills und erteilt keine Veröffentlichungsgenehmigung.
Steps:
1. Fasse die Nachweise und verbleibenden Grenzen in docs/token-overhead-analyse-2026-09-26.md zusammen und ordne sie PLAN-0012 W-017 zu.
2. Ergänze dort Evidence und Next action nach den Plan-Regeln, ohne gestartete Aufträge umzuschreiben. Reguläre Installation erfolgt erst an einer sicheren inaktiven Grenze unter W-017; Veröffentlichung bleibt bis zu dessen Abschluss und den bestehenden Releasegates gesperrt.
Evidence: PLAN-0012 W-017 verweist auf docs/token-overhead-analyse-2026-09-26.md und die SOL-/Luna-Nachweise; sichere reguläre Installation sowie bestehende Releasegates bleiben dort offen.

### W-013 Alle privaten Skill-Helper bestehen die Verbraucherprüfung

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die Helper-Abnahme deckt sämtliche kanonischen Skills unter skills/private ab.
Acceptance: Ein vollständiges Inventar ordnet jedem Skill seine Runtime-Helper und dokumentierten Aufrufarten zu oder weist ihn als helperfrei aus. Auch benjaminstelzer-github mit audit_publication.py sowie check_repository_structure.py und verify_suite_build.py ist geprüft. Gültige Ausgaben werden unverändert im tatsächlichen Folgeschritt verwendet. Agentenseitige Reparaturen sind Fehler. Luna 6 Medium darf reine Helpertests ausführen; geänderte Skills behalten die SOL-6-Medium-Prüfung. Die Suite-Fertigstellung hat Vorrang und zusätzliche Helpertests laufen parallel; fehlende Voraussetzungen und ungetestete Pfade bleiben ausdrücklich offen. Keine Veröffentlichung oder reguläre Installation erfolgt durch diese Tests.
Steps:
1. Erfasse kanonische Skills und Helper im gesamten privaten Verzeichnis; ordne gemeinsam erzeugte Kopien ihrem Owner zu.
2. Prüfe alle zusätzlich gefundenen Helper mit isolierten Fixtures und tatsächlichen Verbrauchern; sichere Befehle sowie Ergebnisse und Modellnachweise.
3. Korrigiere belegte Defekte an ihren kanonischen Quellen und wiederhole betroffene Tests.
Evidence: development/luna-tests/private-helper-inventory.md: alle Laufzeitpfade zugeordnet; echter sauberer Testbuild besteht release-Verifier; Live-Familienabweichungen als externe Releasegrenze dokumentiert.

### W-014 Coordinator-Rollover archiviert den Vorgänger per Nachricht

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0092]
Outcome: Die neue Nutzerkorrektur ersetzt die gestartete frühere Wartevereinbarung durch native Übernahme und Selbstarchivierung.
Acceptance: Der Vorgänger schreibt nach create_thread nicht mehr ins Projekt. Der Nachfolger sichert seine eigene ID und fordert per Nachricht die Selbstarchivierung des richtigen Vorgängers an. Der reale SOL-6-Medium-Test zeigt null Rollover-Warteabfragen und den einmaligen Selbstarchivierungsaufruf. Eine Bestätigung oder Nachprüfung ist gemäß ADR-0092 nicht erforderlich.
Steps:
1. Korrigiere operations-rollover.md und operations.md ohne neue Helper oder Laufzeitschicht.
2. Baue den Kandidaten und prüfe den echten nativen Rollover einschließlich Absenderidentität und Archivierungsaufruf ohne Nachprüfung.
Evidence: development/luna-tests/suite-simplification-comparison.md: PLAN-0003 belegt Übernahme und einmalige Selbstarchivierung ohne Rollover-waits, Bestätigung oder Nachprüfung.

### W-015 Ask-Chattitel verwenden S-ASK und Großbuchstaben

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0091, ADR-0095]
Outcome: Ask-Titel passen zum einheitlichen Erscheinungsbild der Workflow-Chats.
Acceptance: Neu erzeugte native Ask-Chats beginnen mit S-ASK. Die Modell-ID steht in Großbuchstaben; der bisherige mittlere Punkt ist durch einen normalen Bindestrich ersetzt. Beispiel: S-ASK GPT-6-ASTRA - Plan überprüfen. Modellparameter und bestehende Follow-up-Identitäten ändern sich dadurch nicht.
Steps:
1. Nach der aktuellen Suite-Abnahme die kanonische Ask-Titelanweisung und betroffene Tests aktualisieren; abgeleitete Dateien bauen.
2. Den tatsächlichen Titel eines neuen Ask-Chats prüfen, ohne laufende Chats umzubenennen.
Evidence: development/luna-tests/ask-title-final.md belegt SOL-Medium-Prüfung des echten Titels und native Rückzustellung; 18 Ask-Tests und Paketprüfung bestehen.

### W-016 Workflow, Plan und Ask gegen die Projektregeln prüfen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0093]
Outcome: Workflow, Plan und Ask entsprechen den geltenden Projektregeln für schlanke Skills.
Acceptance: Die kanonischen Anweisungen und dokumentierten Helper-Abläufe aller drei Skills sind gegen die anwendbaren AGENTS.md-Regeln geprüft. Für Codex-Skills werden zuerst passende native Bordmittel berücksichtigt; vorhandene Fähigkeiten werden nicht nachgebaut. Übergaben und Rückgaben enthalten nur nötigen Kontext. Absicherungen richten sich nach konkreten Folgen und verwenden die einfachste wirksame und effizienteste Lösung. Reguläre Archivierung bleibt vorgesehen; seltene harmlose Restfehler rechtfertigen keine teure Kontrollmechanik. Helper-Rückgaben bleiben direkt nutzbar und Agenten müssen kein JSON manuell schreiben. Befunde benennen Fundstelle, Auswirkung und kleinste sinnvolle Korrektur; offene Abweichungen bleiben sichtbar. Dies ist ausschließlich eine Prüfung: Findings dem Nutzer mitteilen und keine daraus abgeleiteten Änderungen ohne seine ausdrückliche Freigabe umsetzen.
Steps:
1. Prüfe die aktuellen kanonischen Workflow-, Plan- und Ask-Anweisungen samt verwendeten Helpern gegen die geltenden Projektregeln und verfügbaren Codex-Bordmittel.
2. Teile dem Nutzer konkrete Abweichungen und kleinste sinnvolle Korrekturen knapp mit; unterscheide notwendige Absicherungen von vermeidbarer Komplexität. Keine Befunde selbstständig umsetzen.
Evidence: development/luna-tests/project-rules-review.md dokumentiert mitgeteilte Findings, ausdrückliche Freigaben und geprüfte Korrekturen; finale SOL-Paketzuordnung in suite-simplification-comparison.md.

### W-017 Plan und Step-Gruppen sind kurz erklärt und im Titel sichtbar

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0094]
Outcome: Nutzer erkennen den ausgeführten Plan, die Step-Gruppen und den Grund ihrer Zusammenfassung.
Acceptance: Die Startmeldung nennt Plan, Gruppen und Grund in ein bis zwei Sätzen. Native Worker-, Reviewer- und Repair-Titel zeigen den gesamten zugewiesenen Step-Bereich, auch bei einem ganzen Planpunkt mit Steps. SOL 6 Medium prüft die Anweisungen; der native Kandidatenlauf belegt Meldung und tatsächlich erzeugte Titel. Kein zweiter Bericht oder neuer Helper entsteht.
Steps:
1. Ergänze Plan planning-granularity.md sowie Workflow SKILL.md und operations.md knapp; baue den isolierten Kandidaten.
2. Prüfe Formulierung und Titelregeln mit SOL 6 Medium sowie die tatsächliche native Meldung und Chat-Erstellung im Kandidatenvergleich.
Evidence: development/luna-tests/suite-simplification-comparison.md: native Startmeldung in zwei Sätzen; Worker-, Reviewer- und Repair-Titel zeigen STEPS-1-3; keine nachträgliche Titelkorrektur.

### W-018 Astra Medium prüft alle Änderungen vor Planabschluss

Status: done
Depends on: [W-015]
Blocked by: []
Decisions: []
Outcome: Eine unabhängige Schlussprüfung deckt alle Änderungen aus PLAN-0014 ab.
Acceptance: Astra Medium prüft Quellen und Abnahmebelege auf materielle Fehler und Lücken. Schlanke native Abläufe und direkt nutzbare Helper-Ausgaben stehen im Mittelpunkt. Findings sind vor Planabschluss ausgewertet und notwendige Korrekturen gezielt geprüft.
Steps:
1. Native Ask-Prüfung mit gpt-6-astra medium ausführen und Antwort sichern.
2. Befunde verifizieren und berechtigte Fehler mit der einfachsten ausreichenden Lösung beheben.
Evidence: development/luna-tests/astra-final-review.md belegt zwei behobene Findings; Astra ohne materiellen Restbefund; SOL-Verbrauchertest aller drei Ausgabepfade bestanden.
