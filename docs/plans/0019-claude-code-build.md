---
format_version: 1
id: PLAN-0019
status: draft
created: 2026-09-28
updated: 2026-10-05
---

# Claude-Code-Build der Suite

## Goal

Die Suite erhält nach ADR-0103 als `scoville-suite-for-claude-code` (ADR-0108) eine Claude-Code-Ausgabe als drittes Buildprofil `claude` aus denselben Quellen wie `general` und `codex`. Code, Plan, UI, Handoff und ihre README-Fragmente bleiben gemeinsam. Workflow for Claude und Ask for Claude übertragen die fachlichen Regeln der Codex-Member auf native Claude-Code-Mittel. Ask for Claude fragt Claude-Advisers als Subagenten und Codex über die Codex CLI. Setup gilt für beide Hosts. Pakete entstehen nur über den Builder. General- und Codex-Ausgabe ändern sich nur durch angenommene Decisions.

Die versionsgebundene Grundlage steht in der [Fähigkeitsmatrix](../../development/claude-code/capabilities.md). Claude-Code-Fakten stammen aus code.claude.com vom 2026-09-28 und werden in W-001 an installierten Versionen belegt.

## Non-goals

Keine Verhaltensänderung an Workflow for Codex, Ask for Codex oder am Plan-Format. Auto-Compaction wird weder abgeschaltet, verschoben noch per PreCompact-Hook blockiert. Keine Agent-Teams und keine Worktree-Isolation im Normalablauf. Keine eigenständigen Pakete für Workflow for Claude. Keine Veröffentlichung vor W-009.

## Work items

### W-001 Claude-Code- und Codex-CLI-Verträge sind belegt und die Richtungen entschieden

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0104, ADR-0105, ADR-0106, ADR-0107, ADR-0109]
Outcome: Die tragenden Host-Eigenschaften sind an installierten Versionen belegt, und ADR-0104 bis ADR-0107 sind entschieden.
Acceptance: `development/claude-code/capabilities.md` nennt je Eigenschaft Version, Befehl und Beobachtung, getrennt für interaktiv mit Standard-Fork-Modus und `claude -p`. Claude Code: `Agent` in Vorder- und Hintergrund-Subagenten und Verschachtelung; Abschlussbenachrichtigung ohne Statusabfragen; Subagent endet nach seiner Antwort; Fortsetzung per `SendMessage`; `model` pro Aufruf und `effort` im Frontmatter wirken; Kontextgröße und Modellfenster von Hauptsitzung und Subagent sind aus dem eigenen Transkript mit eindeutiger Identität lesbar; ob Claude selbst eine frische Sitzung starten und deren Ergebnis empfangen kann; Optionen von `agent()` in Dynamic Workflows; ein Plugin lädt Skills aus `packages/<name>` und Agent-Dateien aus Member-Ordnern; `disable-model-invocation` und `${CLAUDE_SKILL_DIR}` wirken. Codex CLI: `codex exec -` mit `--json --sandbox read-only`; JSONL-Felder für Sitzung, Antwort, Nutzung und Fehler; Resume mit `-c sandbox_mode="read-only"` kann nicht schreiben; `--ephemeral`; Anmeldung mit `--ignore-user-config`; Schalter für Websuche. ADR-0104 bis ADR-0107 sind angenommen, abgelehnt oder überarbeitet.
Steps:
1. In einem Wegwerfprojekt unter `<workspace-root>/temp/` jede Eigenschaft prüfen und in `development/claude-code/capabilities.md` festhalten.
2. ADR-0104 bis ADR-0107 mit den Befunden aktualisieren und dem Nutzer zur Entscheidung vorlegen.
Evidence: development/claude-code/capabilities.md belegt alle Punkte außer `${CLAUDE_SKILL_DIR}` interaktiv und `agent()`-Optionen, offen nach ADR-0109. ADR-0104 bis 0107 angenommen.

### W-002 Builder erzeugt das Profil claude aus gemeinsamen Quellen

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0103, ADR-0105, ADR-0108]
Outcome: `suite.json` und `../shared/build` bauen `general`, `codex` und `claude`. Das Profil `claude` enthält vorerst Code, Plan, UI und Handoff.
Acceptance: Profileinstellungen steuern Layout, featured_member und Host-Label. Die Profilmenge kommt aus `suite.json`. Profilblöcke erlauben mehrere Profile, etwa `{{ profile: codex claude }}`. Katalog- und Mitgliedertexte nennen den Host des Profils. `agents/openai.yaml` fehlt im Profil `claude`. Plan-, README- und Installationstexte sind im Profil `claude` vollständig. Ein Test gegen den Claude-Build lässt Codex-Nennungen nur an einer Allowlist von Stellen zu. General und Codex sind bytegleich zu ihrem Referenzbuild aus demselben Ausgangscommit. `development/tests/test_build_suite.py` prüft alle drei Profile. Unbekannte Profile und Blöcke scheitern weiter mit konkreter Diagnose.
Steps:
1. [status: todo] Referenzbuilds von `general` (standalone und suite) und `codex` aus einem sauberen Checkout des Ausgangscommits erzeugen und ihre Receipts außerhalb des Repositorys sichern.
2. [status: todo] `build_suite.py` und `export_suite.py` verallgemeinern: Profil-Settings `layout`, `featured_member` und `host`; Standalone-Filter über `standalone_profiles` jedes Profils; `profile_text` mit Profilmenge und Mehrfachauswahl; Host-Label in `suite.catalog` und `suite.members`. `fragments.md`, `sync_suite_sources.py` und die Quellhashes nachführen.
3. [status: todo] `suite.json` um `claude` ergänzen, `openai.yaml`-Einträge auf `general` und `codex` beschränken und jeden bestehenden `{{ profile: codex }}`-Block auf `codex claude` erweitern oder um einen `claude`-Block ergänzen.
4. [status: todo] Alle Profile bauen, Hashes mit den Referenzbuilds vergleichen und die Tests erweitern, auch die Profilblock-Suche in `members/scoville-plan/development/tests/test_routing_contract.py`.
Evidence: []

### W-003 Die Claude-Suite ist als Plugin installierbar

Status: todo
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0105, ADR-0108]
Outcome: Der `claude`-Build erzeugt Plugin- und Marketplace-Manifest und Agent-Dateien aus Vorlagen.
Acceptance: Build und Export des Profils `claude` enthalten an der Suite-Wurzel `.claude-plugin/plugin.json` und `marketplace.json`, abgeleitet aus dem aufgelösten Manifest. Andere Profile enthalten keine Plugin-Dateien. Dateieinträge können eigene Variablen tragen, und eine Vorlage erzeugt je Effortstufe eine Agent-Datei. `claude plugin validate` besteht. Headless mit `claude -p --plugin-dir <build>` erscheinen alle Skills und Agents, ohne dass das Nutzerprofil geändert wird. Je Modellfamilie zeigt eine Agent-Variante mit Modell-Override Modell und Effort im Transkript. Familien, bei denen Effort nicht wirkt, sind festgehalten.
Steps:
1. [status: todo] Im Builder Dateivariablen je Eintrag und die Manifestgenerierung an der Suite-Wurzel ergänzen, im Export übernehmen und testen.
2. [status: todo] Einen lokalen Build validieren, per `--plugin-dir` laden und Effort je Modellfamilie prüfen.
Evidence: []

### W-004 Claude liest eigene Konfigurationsabschnitte

Status: todo
Depends on: [W-002, W-003]
Blocked by: []
Decisions: [ADR-0112, ADR-0114]
Outcome: Codex und Claude lesen eigene Abschnitte derselben `.scoville/config.json`.
Acceptance: Codex-Werte, -Defaults und -Diagnosen bleiben unverändert, `scoville_config.py` bleibt bytegleich. Claude-Abschnitte werden nach ADR-0112 über `scoville_claude_config.py` gelesen und gemergt. Eine Modelltabelle gibt es nicht (ADR-0114). Ungültige Claude-Werte melden Fundstelle, erwarteten Wert und kleinste Korrektur, auch Effort-Werte ohne Wirkung für die Modellfamilie (W-003) und Codex-Werte wie `ultra`. Der Helper ist mit gültigen und ungültigen Eingaben getestet. Die Tests mit den Settings-Lesern folgen in W-005 und W-006.
Steps:
1. [status: todo] `../shared/runtime/scoville_claude_config.py` auf Basis von `read_config()` anlegen, nur im Profil `claude` ausliefern und testen.
Evidence: []

### W-005 Ask for Claude holt Zweitmeinungen über Subagenten und Codex CLI

Status: todo
Depends on: [W-003, W-004]
Blocked by: []
Decisions: [ADR-0105, ADR-0107, ADR-0112]
Outcome: `members/scoville-ask-for-claude-code` führt Modus, Frage, Adviser-Auswahl und Synthese wie Ask for Codex aus, mit Claude-Subagenten und Codex CLI.
Acceptance: Adviser-Subagenten haben keine Schreibwerkzeuge, laufen parallel und liefern ihre Antwort als letzte Nachricht. Folgefragen behalten Modell und Sitzung. Web nur per opt-in. Angeforderte Modelle werden nicht still ersetzt. `ask_codex.py` startet read-only mit `--disable apps` und `web_search="disabled"` außer bei opt-in. Jedes Resume wiederholt alle Start-Einschränkungen samt `-c sandbox_mode="read-only"`, ein Test prüft die Werkzeugliste auch nach dem Resume. Ein Codex-Unteragent kann nicht schreiben. `ask_codex.py` beendet bei Timeout die Prozessfamilie und meldet fehlende Anmeldung, ungültiges JSON oder leere Antwort als Fehler mit Diagnose. `references/codex.md` nennt die bei `customizations=true` sichtbaren MCP-Server der Nutzerkonfiguration. `references/adviser.md` und `configuration.md` sind gemeinsame Quellen mit Ask for Codex, `configuration.md` unterscheidet `ask.claude` (Claude-CLI-Route unter Codex) und `claude.ask`. Ask for Codex verhält sich unverändert, geänderte Codex-Bytes folgen ADR-0112. Jeder Helper läuft im ersten Aufruf ohne Usage-Fehler, und seine Ausgabe funktioniert ohne Reparatur im nächsten Schritt.
Instructions: Die Adviser-Vorlage berücksichtigt die W-001-Befunde zu Werkzeugen und Effort.
Steps:
1. [status: todo] Member anlegen: SKILL.md mit `disable-model-invocation: true`, `references/claude-native.md`, `references/codex.md`, `config.default.json`, Adviser-Vorlage und `suite.json`-Einträge. Gemeinsame Referenzen per Dateieintrag aus Ask for Codex mit Profilblöcken.
2. [status: todo] `ask_codex.py` aus `ask_claude.py` ableiten und die Routen in `ask.py` und `ask_settings.py` je Host unterscheiden.
3. [status: todo] Helper und Konsultation mit einem Claude- und einem Codex-Adviser samt Folgefrage testen.
Evidence: []

### W-011 Function-Hook-Mods für Workflow for Claude sind geprüft und entschieden

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0104, ADR-0114]
Outcome: Belegt ist, welche Claude-Code-Mods (Function Hooks) Kontextmessung, Wiederaufnahme nach Compaction, Rollengrenzen und Skill-Ladesignale zuverlässig liefern. Eine Decision legt ihren Einsatz im Profil `claude` fest; die Ladesignale dienen auch den Claude-Testläufen aus PLAN-0034 W-001.
Acceptance: `development/claude-code/capabilities.md` nennt je Eigenschaft Claude-Code-Version, Ladeweg (`--plugin-dir` interaktiv, `claude -p` mit `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`, `CLAUDE_CODE_PLUGIN_DIRS` in einer Desktop-Sitzung, Marketplace-Installation) und Beobachtung mit Transkriptstelle: `turn.complete` liefert `usage` mit `agentId` je Subagent; `$.session.usage()` liefert Füllstand und Fenster der Hauptsitzung; `session.compact` feuert für Hauptsitzung und Subagent mit Auslöser und nimmt ergänzte Anweisungen für die Zusammenfassung an, ohne sie zu blockieren; `$.session.append` erreicht den Coordinator nach einer Compaction; `$.session.messages({ agentId })` liest die letzte Antwort eines Subagenten; `tool.call` trägt die `agentId` und lehnt Schreibwerkzeuge je Rolle ab; `skill.prompt` meldet jedes Laden eines Skills. Nicht belegte Eigenschaften sind als unverifiziert markiert. Eine Decision legt fest, ob das Profil `claude` einen optionalen Mod ausliefert, welche geplanten Helper er ersetzt (`inspect_claude_context.py`, Transkript-Leser, `/context`-Parser) und dass alle Skills ohne Mod korrekt bleiben.
Instructions: Nur in einem Wegwerfprojekt unter `<workspace-root>/temp/` mit eigenem `CLAUDE_CONFIG_DIR` prüfen; kein Mod im Nutzerprofil, Auto-Compaction weder blockieren noch verschieben.
Steps:
1. [status: todo] Die Typdeklaration der installierten Version mit `/plugin-types` gegen die genannten Ereignisse und Aufrufe abgleichen und einen minimalen Probe-Mod anlegen, der `claude plugin validate` besteht.
2. [status: todo] Den Probe-Mod interaktiv und headless mit einem Coordinator sowie einem schreibenden und einem lesenden Plugin-Subagenten ausführen, je eine Compaction von Hauptsitzung und Subagent auslösen und die Beobachtungen in `capabilities.md` eintragen.
3. [status: todo] Laden über Marketplace-Installation und Desktop-Sitzung sowie die Abschaltbarkeit durch Richtlinien prüfen und festhalten.
4. [status: todo] Eine Decision zum Mod-Einsatz mit Empfehlung anlegen und ihre Auswirkungen auf W-003, W-006 und W-008 benennen.
Evidence: []

### W-006 Workflow for Claude führt einen Plan mit Subagenten aus

Status: todo
Depends on: [W-003, W-004, W-011]
Blocked by: []
Decisions: [ADR-0104, ADR-0105, ADR-0111, ADR-0112, ADR-0114]
Outcome: `members/scoville-workflow-for-claude-code` führt wie Workflow for Codex eine Einheit nach der anderen mit Worker, Review und Worker-Handoff aus. Die Hauptsitzung koordiniert nach ADR-0104.
Acceptance: Step-Gruppen, Routen, Review-Rhythmus (ADR-0102), Ergebnisse (ADR-0101), ein einziger Schreiber, Plan- und Commit-Hoheit des Coordinators, Split beim dritten Handoff und die Worker-Schwelle 60 gelten wie bei Codex. Der Coordinator hat keinen Rollover und keine Schwelle. Den Laufstand `.scoville/claude-workflow.md` schreibt der Dispatch-Helper bei jedem Dispatch vor dem `Agent`-Aufruf: Skill-Pfad, Plan und Einheit, Rolle, Auftragsdatei des laufenden Subagenten, Worker-Nummer, Handoff-Zähler und Review-Basis. Scope, Nutzerentscheidungen und nächste Aktion trägt die native Kompaktierungszusammenfassung, der Coordinator schreibt den Laufstand nie von Hand. Er ersetzt unter Claude die Regel ohne separaten Cursor aus ADR-0101. Nach einer Auto-Compaction wird der Coordinator ohne Nutzeraktion auf Laufstand und Skill verwiesen und liest beide neu. Fehlt dann das Ergebnis des eingetragenen Subagenten, liest ein Helper dessen letzte Antwort aus seinem Transkript, statt einen neuen Schreiber zu starten. Ein Dispatch besteht aus höchstens einem Helper- und einem Agent-Aufruf. Der Auftrag entsteht als Datei unter `.scoville/assignments/` und wird nie im Coordinator-Kontext ausgegeben. Es gibt kein Polling und keine Zustell- oder Archivschicht. Der Coordinator schreibt nicht, solange ein Worker läuft, und Nutzeranweisungen für laufende Arbeit gehen wie bei Codex an den Worker. Worker übergeben an natürlichen Grenzen über ihrer Schwelle. Modell-ID und Fenster ermittelt der Dispatch-Helper je Modellfamilie per `/context` und schreibt sie in den Auftrag (ADR-0114). Das Transkript eines Subagenten finden Helper über `CLAUDE_CODE_SESSION_ID` im Ordner `subagents/` der eigenen Sitzung anhand seiner Auftragsdatei. Der Dateiname liefert die agentId. Ein Handoff beendet den Subagenten. Worker und Reparaturworker schreiben ihren Fortsetzungsstand nach `.scoville/claude-worker-handoff.md` und melden dem Coordinator nur Handoff, Einheit und einen enthaltenen geprüften Produktfix. Reviewer übergeben in ihrer Antwort. Der Coordinator startet für denselben Restauftrag einen frischen Subagenten derselben Rolle und Route mit Verweis auf die Datei, nie `SendMessage` an den Vorgänger. Er liest die Datei nur für den Split beim dritten Handoff oder bei einem Nutzereingriff. Laufstand, Auftrags- und Handoff-Dateien sind per `.scoville/.gitignore` von Git ausgeschlossen, `config.json` bleibt versionierbar. Fehlende Telemetrie wird gemeldet, nie geschätzt. Worker und Reviewer haben kein `Agent`-Tool. Reviewer folgen ADR-0111: `Bash` für Tests und Checkpoint, danach Diff-Kontrolle durch den Coordinator. Worker geben `needs_user_decision` zurück statt zu fragen. Jeder Helper ist mit seinem tatsächlichen Konsumenten getestet.
Steps:
1. [status: todo] Frühprobe mit einem Plugin-Agent in einem Wegwerfprojekt unter `<workspace-root>/temp/`: Ein laufender Subagent findet sein Transkript über `CLAUDE_CODE_SESSION_ID` und seine Auftragsdatei und liest `usage`. Geprüft werden außerdem `SendMessage` an einen laufenden Subagenten, `TaskStop`, ein Plugin-Hook `SessionStart` mit Matcher `compact` und headless das Warten auf Hintergrund-Subagenten. Ergebnisse in `development/claude-code/capabilities.md`.
2. [status: todo] SKILL.md mit `disable-model-invocation: true`, `references/` und `assets/workflow.toml` aus Workflow for Codex portieren und die Host-Werkzeuge nach der Frühprobe ersetzen.
3. [status: todo] Helper anlegen: `build_dispatch_prompt.py` schreibt Auftragsdatei und Laufstand ohne Zustellzeilen, ein Helper liest die letzte Antwort eines Subagenten aus dessen Transkript, `resolve_model_pair.py` liefert zusätzlich den Agenttyp sowie Modell-ID und Fenster per `/context`, `check_context_checkpoint.py` mit `inspect_claude_context.py` liest das Transkript des Workers, `select_context.py` kommt per Dateieintrag aus Plan.
4. [status: todo] Worker- und Reviewer-Vorlagen und `suite.json`-Einträge ergänzen und die Helper testen.
Evidence: []

### W-010 Setup konfiguriert beide Hosts

Status: todo
Depends on: [W-004, W-005, W-006]
Blocked by: []
Decisions: [ADR-0112, ADR-0114]
Outcome: Setup im Profil `claude` zeigt und speichert `claude.ask` und `claude.workflow` mit Claude-Defaults. Setup im Profil `codex` verhält sich unverändert.
Acceptance: `setup.py` ist nach ADR-0112 gemeinsam erweitert. Im Profil `claude` nutzt Setup die Defaults von Ask und Workflow for Claude, bietet Modellfamilien und die regulären Effortstufen wie ADR-0067 an und nennt keine reine Codex-Zugehörigkeit. Codex-Werte, -Defaults, -Diagnosen und -Verhalten bleiben unverändert, auch mit vorhandenem `claude`-Abschnitt. Ungültige Eingaben melden Fundstelle, erwarteten Wert und kleinste Korrektur. Jeder geänderte Helper ist mit gültigen und ungültigen Eingaben und seinem tatsächlichen Konsumenten getestet.
Steps:
1. [status: todo] In `members/scoville-setup` Dateieinträge je Profil, Profilblöcke in SKILL.md und den Claude-Teil in `setup.py` ergänzen.
2. [status: todo] Setup in beiden Profilen mit gültigen und ungültigen Eingaben gegen die echten Settings-Leser testen.
Evidence: []

### W-007 READMEs und Regeln beschreiben die Claude-Suite

Status: todo
Depends on: [W-005, W-006, W-010]
Blocked by: []
Decisions: [ADR-0103, ADR-0105, ADR-0108, ADR-0113]
Outcome: Suite- und Member-READMEs der Claude-Suite entstehen aus gemeinsamen Fragmenten, und die Workspace-Regeln kennen die Claude-Suite.
Acceptance: `suite-intro.md`, `suite-install.md` und die gemeinsamen README-Bausteine haben `claude`-Blöcke. `codex-limitations.md` ist als Host-Grenzen-Fragment mit Claude-Block umbenannt. Die beiden neuen Member haben Fragmentordner mit den kanonischen Abschnitten; hostneutrale Workflow-Abschnitte nutzen beide Workflow-Member gemeinsam. General- und Codex-READMEs ändern sich nur um beabsichtigte Querverweise. `<workspace-root>/AGENTS.md`, `<workspace-root>/skills/AGENTS.md` und `AGENTS.md` nennen die Claude-Suite, ihr festes Distributionsziel und native Claude-Code-Mittel; der veraltete Pfad `skills/private/ask-suite-for-codex` ist entfernt. `../shared/luna-release-gate.md` nennt das Claude-Gate nach ADR-0113 mit `claude plugin eval` und `--no-publish` und das dritte Sync-Ziel. Texte folgen den README-Stilregeln. `--check-readmes` besteht für alle Profile.
Steps:
1. [status: todo] README-Fragmente und Profilblöcke ergänzen, mit `benjaminstelzer-imitate-me` formulieren, falls verfügbar, und für alle Profile prüfen.
2. [status: todo] Die drei AGENTS.md-Dateien und die Gate-Beschreibung anpassen.
Evidence: []

### W-008 Die Claude-Suite ist einzeln und Ende-zu-Ende geprüft

Status: todo
Depends on: [W-007, W-010]
Blocked by: []
Decisions: [ADR-0104, ADR-0109, ADR-0111, ADR-0113, ADR-0114]
Outcome: Helper, Ask und Workflow sind in Claude Code interaktiv und headless gemessen.
Acceptance: Jeder Helper des Profils `claude` wird mit `claude -p` und Sonnet 5 (ADR-0113) im ersten Versuch ohne `--help` und ohne Usage-Fehler genutzt. Der `/context`-Parser liest das Fenster jeder Modellfamilie. Ein interaktiv aufgerufener Claude-Member löst seine Helper-Pfade über `${CLAUDE_SKILL_DIR}` korrekt auf (ADR-0109). Ein Fixture mit mindestens drei Steps läuft interaktiv mit Standard-Fork-Modus und headless: Worker, Review, Korrektur, schwellenausgelöster Worker-Handoff mit niedriger Testschwelle für mindestens zwei Modellfamilien, eine erkannte Reviewer-Änderung, Nutzereingriff, Stopp und Wiederaufnahme sowie eine Ask-Konsultation. Nach einer Kompaktierung des Coordinators zwischen Ergebnisempfang und nächstem Dispatch setzt er aus `.scoville/claude-workflow.md` ohne doppelten Schreiber und ohne verlorenes Ergebnis oder Review fort. Der Auslöser der Kompaktierung ist benannt. Das Kontextwachstum des Coordinators pro Einheit ist gemessen. Harte Grenzen: keine Auto-Compaction in Worker-Transkripten bei Standardschwelle, keine Statusabfragen auf laufende Subagenten, nie zwei schreibende Subagenten, Dispatch mit höchstens zwei Tool-Aufrufen, Helper lesen nur Transkripte der eigenen Sitzung. Das Release-Gate nach ADR-0113 läuft als Eval-Suite per `claude plugin eval --model sonnet --json --no-publish` und ist erfüllt oder vom Nutzer ausdrücklich ausgenommen. Messwerte und Grenzen stehen mit Transkriptstellen in `development/claude-code/results.md`.
Steps:
1. [status: todo] Gate-Fälle als Eval-Suite unter `development/claude-code/evals/` anlegen, nur für den Lauf in einen lokalen Build kopieren und dort ausführen.
2. [status: todo] Headless-Messwerte aus `subagent_stats` der JSON-Ausgabe nehmen und `development/luna-tests/analyze_workflow_rollouts.py` nur für Tool-Aufrufe pro Dispatch und `compact_boundary` anpassen.
3. [status: todo] Helpertests und Fixture-Läufe ausführen und die Ergebnisse festhalten.
Evidence: []

### W-009 Die Claude-Suite wird nach Freigabe veröffentlicht

Status: todo
Depends on: [W-008]
Blocked by: []
Decisions: [ADR-0103, ADR-0108, ADR-0112]
Outcome: Die verifizierte Claude-Suite liegt im festen Distributionsziel und ist nach Nutzerfreigabe veröffentlicht.
Acceptance: Der Nutzer hat Sichtbarkeit und Veröffentlichung entschieden. Der Build liegt unter `<workspace-root>/skills/temp/release/` und ist nach `<workspace-root>/skills/public/scoville-suite-for-claude-code/` synchronisiert. Eine frische Plugin-Installation in einem leeren Profil über ein eigenes `CLAUDE_CONFIG_DIR` funktioniert. General und Codex werden in W-009 nicht eigens neu veröffentlicht. Ihre durch PLAN-0019 geänderten Bytes gehen mit dem nächsten regulären Release (ADR-0112). Ein Push umfasst den GitHub-Release nach `skills/AGENTS.md`.
Instructions: Nach W-008 die Veröffentlichungsfreigabe beim Nutzer einholen.
Steps:
1. [status: todo] Freigabe einholen, `--profile claude --layout suite` bauen, prüfen und synchronisieren.
2. [status: todo] Frische Installation prüfen und nach Push-Auftrag Release und Verifikation abschließen.
Evidence: []
