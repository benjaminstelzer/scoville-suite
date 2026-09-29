# Claude-Code- und Codex-CLI-Fähigkeiten für PLAN-0019

Probe am 2026-09-28 mit Claude Code 2.1.283, Hauptmodell `claude-opus-5-5`.
Probeprojekt: Wegwerfprojekt unter `<workspace-root>/temp/`, Subagenten in `.claude/agents/`, PreToolUse-Hook
auf Bash protokolliert die Hook-Eingabe. "Interaktiv" ist eine normale Sitzung im Standardmodus, "headless" ist
`claude -p` aus dieser Sitzung.

## Claude Code

| Eigenschaft | Aufruf | Beobachtung |
| --- | --- | --- |
| Start eines Subagenten interaktiv | `Agent` ohne Vorder-/Hintergrundangabe | Läuft im Hintergrund ("Async agent launched"), Abschluss kommt als Task-Benachrichtigung. Das interaktive Agent-Schema hat nur `description`, `isolation`, `model`, `prompt`, `subagent_type`. |
| `Agent` in einem Hintergrund-Subagenten | `probe-nester` mit `tools: Agent, Read, Bash` | Werkzeuge `Agent, Read, Bash, SubagentHandback`. Er startete `probe-leaf` (Tiefe 2) im Hintergrund, erhielt dessen Abschlussbenachrichtigung und gab `LEAF-OK` zurück. Meta: `requestShape: background`, `spawnDepth` 1 und 2. |
| Headless | `claude -p` mit demselben Nester | Agent-Schema hat `run_in_background`, der Nester startete den Leaf im Vordergrund. `subagent_stats`: foreground 2, max_depth 2. |
| Fortsetzung | `SendMessage` an die agentId | Setzt den beendeten Subagenten fort, er kennt das zuvor gegebene Token. Adressierung über `description` scheitert ("No agent named ... is reachable"). |
| Modell pro Aufruf | `Agent` mit `model: "haiku"` | Transkript `model: claude-haiku-4-5-20251001`. Das interaktive Schema erlaubt für `model` nur `sonnet`, `opus`, `haiku`, `fable`, also Familien statt fester Versionen. |
| Effort im Frontmatter | `effort: low` in Projekt- und Plugin-Agent | Hook-Feld `effort.level` = `low`, sonst `medium` (Sitzungswert). Transkripte beider Agents zeigen `"effort":"low"`. Beim Haiku-Aufruf `effort` = null. Nur `low` beobachtet, `xhigh` und `max` nur aus der CLI-Hilfe. Frontmatter-Effort zusammen mit `model`-Override nicht geprüft. |
| Hook-Identität | Projekt-Hook PreToolUse auf Bash | In Subagenten gesetzt: `agent_id`, `agent_type`. `transcript_path` zeigt immer auf das Haupttranskript, `agent_transcript_path` ist null. |
| Transkripte | Dateisystem | Haupt: `~/.claude/projects/<projekt-slug>/<session_id>.jsonl`. Subagenten flach, auch verschachtelte: `.../<session_id>/subagents/agent-<agent_id>.jsonl` plus `.meta.json` (`parentAgentId`, `spawnDepth`, `requestShape`, `model`). |
| Kontextgröße | letzte Assistant-Zeile | `message.usage` mit `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens`. Kein Feld zum Kontextfenster im Transkript. `claude -p --output-format json` meldet `modelUsage.<modell>.contextWindow` = 1000000. |
| Umgebung | `env` per Bash in Hauptsitzung und Subagent | Beide haben `CLAUDE_CODE_SESSION_ID` mit der ID der Hauptsitzung und `CLAUDE_EFFORT`. Keine agentId und kein Transkriptpfad. Auch eine interaktive Sitzung setzt `CLAUDE_CODE_SESSION_ID`. |
| Kontextfenster je Modell | `claude -p --model <familie oder ID> --output-format json "/context"` | `num_turns` 0, Kosten 0. Der `result`-Text nennt Modell-ID und Fenster, etwa `**Tokens:** 30.2k / 200k (15%)`. Beobachtet: `haiku` und `claude-haiku-4-5-20251001` 200k, `sonnet`, `opus` und `fable` 1m. Formatierter Text mit gerundeten Werten, keine dokumentierte Schnittstelle. Hook-Eingaben enthalten kein Fenster. |
| Frische Sitzungen | `claude --help`, `claude agents --help` | `claude --bg` startet eine Hintergrundsitzung und gibt eine ID aus, `claude agents --json` listet Sitzungen, dazu `attach`, `logs`, `stop`, `respawn`. `SendMessage` und `ListAgents` erreichen laut Werkzeugbeschreibung auch andere Sitzungen. Nichts davon gestartet. |
| Dynamic Workflows | Skill `workflow-authoring` | In der Probesitzung nicht verfügbar, `agent()`-Optionen nicht beobachtet. |
| Kompaktierung durch das Modell | headless: Modell soll `compact` über `Skill` aufrufen | `tool_use_error`: "compact is a built-in CLI command, not a skill". Kein Werkzeug löst Kompaktierung aus. Laut Doku auch kein Hook (nicht beobachtet). |
| Kompaktierung durch den Aufrufer | `claude -p --resume <id> "/compact"` | Läuft ohne Antwort-Turn (`num_turns` 0), die Zusammenfassung ist aber ein Modellaufruf (0,34 USD bei 36k Tokens). Transkript erhält `compact_boundary` mit `compactMetadata.trigger` = `manual` und `preTokens`. Nur der Sender des Prompts kann kompaktieren, also Nutzer oder Treiberskript. |
| Inhalt nach Kompaktierung | headless: Skill mit 40 Regeln per `/probe-persist`, Merkwort, `/compact`, dann Rückfrage ohne Werkzeuge | Die Zusammenfassung (`isCompactSummary`) hat Abschnitte für Anliegen, alle Nutzernachrichten, offene Aufgaben, aktuelle Arbeit und nächsten Schritt. Sie enthielt Regel 37 wörtlich und das Merkwort, die Rückfrage wurde vollständig beantwortet. Sie nennt den Pfad des vollständigen Transkripts von vor der Kompaktierung. Den Skill-Text hängt Claude Code nicht wörtlich neu an, wohl aber Umgebung, Projektanweisungen und Agent-Liste. |
| `disable-model-invocation: true` | interaktiv: `Skill`-Werkzeug; headless: Skill-Liste erfragen | Interaktiv verweigert das Modell den Aufruf. Headless fehlen solche Skills in der Liste, nur `probe-plugin:probe-visible` erscheint. Der Nutzer kann sie per Slash-Befehl aufrufen. |
| `${CLAUDE_SKILL_DIR}` | headless: `claude -p "/probe-skill"`, `"/probe-plugin:probe-visible"`, `"/probe-plugin:probe-plugin-skill"` | Wird in Projekt- und Plugin-Skills durch das absolute Skill-Verzeichnis mit `/` als Trenner ersetzt, auch bei `disable-model-invocation: true`. In Git Bash braucht ein Slash-Argument `MSYS_NO_PATHCONV=1`, sonst kommt `<Git-Installationsordner>/<skill>` an. Interaktiv nicht geprüft. |
| Plugin-Agents | `--plugin-dir`, `agents` mit Einzeldateien | Geladen als `probe-plugin:probe-plugin-agent`, antwortete. `claude plugin validate` besteht (Warnung: kein author). Laut Doku ignorieren Plugin-Agents `permissionMode`, `hooks` und `mcpServers` (nicht beobachtet). Ob ein Plugin-Agent im Hintergrund `Agent` behält, ist nicht geprüft. |
| Plugin-Skills aus `./packages/<name>` | headless, `--plugin-dir`, Manifest `skills: ["./packages/<name>"]`, Layout `packages/<name>/<name>/SKILL.md` | `probe-visible` und `probe-plugin-skill` antworten per Nutzeraufruf `/probe-plugin:<skill>`. Modell-aufrufbar erscheint nur `probe-plugin:probe-visible`. `probe-member` (`disable-model-invocation`) wurde nicht aufgerufen. |
| Skill-Preload in Subagenten | Agent-Frontmatter `skills: [probe-skill]` bei `disable-model-invocation: true` | Offen, nicht Teil der Acceptance. Schritt in Probe 2 auf Nutzerwunsch ausgelassen. |
| Plugin-CLI | `claude plugin --help` | `validate`, `install`, `marketplace`, `list`, `enable`/`disable`, `update`, `uninstall`, `details`, `eval`, `tag`, `init`, `prune`. |
| Plugin-Evals | `claude plugin eval --help` | Fälle als `case.yaml` oder `prompt.md` mit Gradern unterhalb des Plugins, dazu `--model`, `--json`, `--max-cost-usd`, `--judge-model` (Standard `haiku`) und eine Vergleichsrunde ohne Plugin. Ohne `--no-publish` wird ein HTML-Bericht veröffentlicht. Nicht ausgeführt. |

## Codex CLI

Erste Probe mit `codex-cli 0.154.0`, zweite am selben Tag mit `codex-cli 0.158.0-alpha.2.1`. Ort und Version der
ausführbaren Datei hängen von der Installation ab. Die Tabelle gilt für 0.158. Angaben zu 0.154 stammen aus der ersten
Auswertung, deren Rohdaten überschrieben sind. Arbeitsverzeichnis ist ein leerer Ordner, Schreibversuche folgen einer
Anweisung im Prompt.

| Eigenschaft | Aufruf | Beobachtung |
| --- | --- | --- |
| Read-only-Ausführung | `codex exec - --sandbox read-only --json --skip-git-repo-check -C <dir> -c model_reasoning_effort=low` | Prompt per stdin. Schreiben per Shell scheiterte, Datei nicht angelegt, Exit 0, 13 s (0.154: 137 s). |
| `apply_patch` read-only | wie oben, Anweisung `apply_patch` statt Shell | Abgelehnt: "patch rejected: writing is blocked by read-only sandbox". |
| JSONL-Ereignisse | `--json` | `thread.started` (`thread_id`), `turn.started`, `item.started`, `item.completed` (`item.type` `agent_message`, `command_execution` oder `web_search`, Text in `item.text`), `turn.completed` (`usage`: `input_tokens`, `cached_input_tokens`, `cache_write_input_tokens`, `output_tokens`, `reasoning_output_tokens`). Die Antwort ist die letzte `agent_message`. |
| Fehler | Resume einer unbekannten Sitzung | Exit 1, keine JSONL-Zeile, Grund nur in stderr (`Error: thread/resume: ... no rollout found for thread id <id>`). `error`- oder `turn.failed`-Ereignisse kamen in keinem Lauf vor. stderr enthält auch bei Exit 0 `WARN`-Zeilen und ist kein Fehlersignal. |
| Resume read-only | `codex exec resume <id> - --json --skip-git-repo-check -c sandbox_mode="read-only"` | Schreiben scheiterte, Datei nicht angelegt, gleiche `thread_id`. |
| Resume ohne Override | dasselbe ohne `-c sandbox_mode=...`, nach read-only-Start | Schreiben gelang, Datei angelegt. Resume übernimmt die Sandbox des Starts nicht. |
| Resume-Arbeitsverzeichnis | wie oben | `resume` kennt kein `-C` (0.154: Exit 2). Das Verzeichnis kommt vom Prozess-Arbeitsverzeichnis. |
| `--ephemeral` | `exec` mit `--ephemeral` | Läuft und liefert eine `thread_id`. Resume dieser ID scheitert mit Exit 1 ("no rollout found"). |
| `--ignore-user-config` | `exec` mit `--ignore-user-config` | Läuft, Anmeldung bleibt erhalten. |
| Websuche | `exec` mit `--ignore-user-config`, Prompt verlangt eine Suche | Ohne Option aktiv (`item.type` `web_search`). `-c web_search="live"` und `codex --search exec` ebenso. `-c web_search="disabled"` schaltet sie ab. `exec` selbst hat kein `--search`. |
| Websuche beim Resume | Start mit `web_search="disabled"`, Resume ohne Option und mit `-c web_search="live"` | Beide Male keine Websuche. Die Einstellung gilt ab Start und lässt sich per Resume nicht ändern. |
| Werkzeuge mit Außenwirkung | Modell listet seine Werkzeuge, `exec` read-only | Mit und ohne `--ignore-user-config` sichtbar: 169 `mcp__codex_apps__*`-Werkzeuge, darunter `github_create_commit`, `github_merge_pull_request`, `sites_deploy_site_version`. Ohne `--ignore-user-config` zusätzlich MCP-Server der Nutzerkonfiguration (`node_repl`, `cua_repl`). Laut Hilfe gilt die Sandbox für Shell-Befehle, Aufrufe dieser Werkzeuge nicht geprüft. `--disable apps` entfernt alle `codex_apps`-Werkzeuge, `collaboration.*` bleibt auch mit `--disable multi_agent`. |
| Werkzeuge beim Resume | Start mit `--disable apps --ignore-user-config --ignore-rules`, Resume mit und ohne diese Optionen | Ohne Wiederholung sind 169 `codex_apps`-Werkzeuge, `node_repl` und `cua_repl` wieder da. Mit wiederholten Optionen keine. Resume übernimmt diese Start-Optionen nicht. |
| Unteragent | read-only-Start wie oben, Modell startet per `collaboration.spawn_agent` einen Unteragenten mit Schreibauftrag | Unteragent meldet "shell command was blocked by the read-only policy", Datei nicht angelegt. |
| MCP-Server | `codex --help` | Die Befehlsliste von 0.158 enthält kein `mcp-server`. Eine Anbindung von Codex als MCP-Server entfällt. |
| Optionen | `codex exec --help`, `codex exec resume --help` | `exec`: `-s/--sandbox`, `-C/--cd`, `-m`, `--ephemeral`, `--ignore-user-config`, `--ignore-rules`, `-o`, `--output-schema`, `--enable`/`--disable <feature>`. `resume`: kein `--sandbox`, kein `-C`, dafür `-c`, `-m`, `--last`, `--json`, `--ephemeral`, `--ignore-user-config`, `--ignore-rules`, `--enable`/`--disable <feature>`, `--skip-git-repo-check`. |

## Folgen für die Decisions

- ADR-0104: Der Blocker aus der Doku besteht in 2.1.283 nicht, Hintergrund-Nesting ist aber undokumentiert und für
  Plugin-Agents unbelegt. Gezielte Kompaktierung geht nur für den Sender des Prompts. Entschieden: Die Hauptsitzung
  koordiniert ohne Rollover, Worker und Reviewer laufen auf Tiefe 1.
- ADR-0105: Modell pro Aufruf und Effort im Frontmatter wirken, auch im Plugin-Agent. Bei Haiku ist Effort null,
  W-003 prüft Effort je Modellfamilie. Plugin-Agents und Plugin-Skills laden aus dem `packages/<name>/<name>/`-Layout,
  `${CLAUDE_SKILL_DIR}` wird ersetzt.
- ADR-0107: Der Adapter löst den Codex-Pfad auf, wiederholt bei jedem Resume alle Start-Einschränkungen samt
  `-c sandbox_mode="read-only"`, lässt dort `-C` weg und nutzt das Prozessverzeichnis. Websuche ist ohne `-c web_search="disabled"` an und wird beim Start
  festgelegt. `--disable apps` entfernt Werkzeuge mit Außenwirkung. `--ephemeral` schließt Folgefragen aus. Erfolg
  heißt Exit 0 und nicht leere letzte `agent_message`.
- Kontext-Checkpoint: Nutzung ist aus dem eigenen Transkript lesbar, das Fenster nicht. Es kommt nach ADR-0114 per
  `/context` aus dem Dispatch-Helper. Sein Transkript findet ein Subagent über `CLAUDE_CODE_SESSION_ID` im Ordner `subagents/` der eigenen
  Sitzung anhand seiner Auftragsdatei. W-006 belegt das zuerst an einem laufenden Subagenten.
