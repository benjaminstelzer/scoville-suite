# Claude-Code-Build der Scoville Suite: Analyse

Umsetzung: PLAN-0019 mit ADR-0103 bis ADR-0113. Diese Analyse ist ein Arbeitsstand vor den Entscheidungen. Bei Abweichungen gelten ADRs, Plan und capabilities.md, etwa bei Namen, Agent-Adressierung, Schwellen und Reviewer-Werkzeugen. Namen nach ADR-0108: Suite `scoville-suite-for-claude-code`, Plugin `scoville-suite`.

Korrektur nach W-001: In Claude Code 2.1.283 behalten Hintergrund-Subagenten mit `Agent` in `tools` das Agent-Tool und können Subagenten starten. Der Blocker in Abschnitt 3.1 besteht damit nicht, siehe [capabilities](../development/claude-code/capabilities.md). ADR-0104 wählt trotzdem die Hauptsitzung als Coordinator ohne Rollover, Laufstand in `.scoville/claude-workflow.md`. Abschnitt 3 ist insoweit überholt. Der Entwurf PLAN-0015 ist gelöscht, Verweise darauf beziehen sich auf seinen Stand in der Git-Historie.

Stand: 2026-09-28. Quellen: `skills/private/scoville-suite` (suite.json, members, docs),
`skills/private/shared/build`, PLAN-0015, ADR-0001/0013/0079/0085/0101/0102 und die
Claude-Code-Doku (Subagents, Skills, Plugins, Hooks, Workflows) vom selben Tag.
Codex-CLI-Fakten: learn.chatgpt.com Non-interactive mode, openai/codex#40149.

## Ergebnis

Das Buildkonzept trägt ein drittes Profil `claude` ohne Strukturbruch. `suite.json`
kennt bereits Profile, profilgefilterte Mitglieder und Dateien, `{{ profile: }}`-Blöcke
und README-Fragmente. Nötig sind:

1. ein Profil `claude` mit Suite `scoville-suite-for-claude`,
2. zwei neue Member `scoville-workflow-for-claude` und `scoville-ask-for-claude`,
3. `scoville-setup` für beide Hosts,
4. eine Handvoll Generalisierungen im Builder, der heute an mehreren Stellen `codex` hart kodiert,
5. ein generiertes Plugin-Manifest an der Suite-Wurzel, weil Claude Code Subagent-Dateien
   nur über Plugins (oder `~/.claude/agents/`) ausliefert.

Code, Plan, UI und Handoff bleiben gemeinsame Quellen mit gemeinsamen READMEs.

**Ein Befund blockiert PLAN-0015 in seiner jetzigen Form:** In interaktiven Sitzungen ist
Fork-Modus Standard. Dann laufen alle Subagenten im Hintergrund, und Hintergrund-Subagenten
verlieren das `Agent`-Tool. Ein Coordinator-Subagent könnte dort keine Worker starten.
Headless (`claude -p`) ist Fork-Modus aus, dort würde der Test also bestehen und interaktiv
scheitern. Das muss W-001 zuerst belegen, bevor Workflow gebaut wird (siehe unten).

```text
                    gemeinsame Quellen (members/, development/readme/, shared/)
                                          |
             +----------------------------+----------------------------+
             |                            |                            |
     --profile general            --profile codex              --profile claude  (neu)
     scoville-suite               scoville-suite-for-codex     scoville-suite-for-claude
     Code Plan UI Handoff         + Workflow for Codex         + Workflow for Claude
     (portabel, Fallbacks)        + Ask for Codex              + Ask for Claude
                                  + Setup                      + Setup
                                                               + .claude-plugin/ (generiert)
```

## 1. Profil und Manifest

`suite.json`:

```json
"profiles": {
  "general": {"name": "scoville-suite", "repository": "benjaminstelzer/scoville-suite"},
  "codex":   {"name": "scoville-suite-for-codex", "repository": "benjaminstelzer/scoville-suite-for-codex"},
  "claude":  {"name": "scoville-suite-for-claude", "repository": "benjaminstelzer/scoville-suite-for-claude",
              "layout": "suite", "featured_member": "scoville-workflow-for-claude", "host": "Claude Code"}
}
```

Mitglieder im Profil `claude` (7, wie Codex):

| Member | Quelle | Profile |
| --- | --- | --- |
| scoville-code, -plan, -ui, -handoff | unverändert gemeinsam | alle |
| scoville-workflow-for-claude | neu | `["claude"]`, `distribution: suite` |
| scoville-ask-for-claude | neu | `["claude"]`, zunächst `distribution: suite` |
| scoville-setup | gemeinsam, Dateien je Profil | `["codex", "claude"]` |

Dateiebene: `agents/openai.yaml` bekommt in Code/Plan/UI/Handoff `profiles: ["general", "codex"]`.
Claude Code liest sie nicht. Das Codex-Flag `allow_implicit_invocation: false` wird in den
Claude-Membern zu `disable-model-invocation: true` im SKILL.md-Frontmatter.
Setup erhält Dateieinträge je Profil (Workflow- und Ask-Defaults aus dem jeweiligen Host-Member).

## 2. Builder-Änderungen (`shared/build/build_suite.py`, `export_suite.py`)

Heute hart kodiert und für `claude` zu verallgemeinern:

| Stelle | Heute | Änderung |
| --- | --- | --- |
| `load()` Profil-Settings | nur `name`, `repository`, `readme` erlaubt | `layout`, `featured_member`, `host` zulassen |
| Default-Layout | `suite` nur bei `profile == 'codex'` | aus Profil-Setting `layout` |
| Standalone-Filter | nur `codex` in `standalone_profiles` | für jedes Profil mit `layout: suite` |
| `featured_member` | global, fällt bei `claude` weg | pro Profil |
| `profile_text()` | erlaubt `{general, codex}` | Profilmenge aus `suite.json`; Mehrfachauswahl `{{ profile: codex claude }}` |
| `suite.catalog` | Text "Ask your Codex host" | Host-Label aus Profil |
| `suite.members` | "Codex desktop required" | Host-Label |
| Dateien je Variante | eine Quelle, ein Ziel, Variablen pro Member | optionale `variables` pro Dateieintrag (für Agent-Varianten, s. 4.3) |
| Suite-Wurzel | nur `packages/`, suite.json, README | `.claude-plugin/plugin.json` und `marketplace.json` aus dem aufgelösten Manifest generieren |

Mehrfachauswahl ist der entscheidende Punkt für die Plan-Texte: Die rund 15 bestehenden
`{{ profile: codex }}`-Blöcke meinen meist "Python ist Pflicht", nicht "Codex". Wo der Text
hostneutral ist, wird daraus `{{ profile: codex claude }}`. Wo er Codex nennt (etwa Plan-
`compatibility`), kommt ein eigener `claude`-Block dazu. Die Codex-Ausgabe bleibt dabei
bytegleich, weil sich nur die Blockauswahl ändert, nicht der Codex-Text.

Das Paketziel muss im Member-Ordner liegen (`payload()` prüft das). Agent-Dateien gehören
also nach `scoville-workflow-for-claude/agents/*.md`. Das Plugin-Manifest verweist darauf:

```json
{
  "name": "scoville",
  "skills": ["./packages/scoville-code", "./packages/scoville-plan", "...", "./packages/scoville-setup"],
  "agents": ["./packages/scoville-workflow-for-claude/scoville-workflow-for-claude/agents/scoville-worker-high.md", "..."]
}
```

`skills` ergänzt den Standardscan und akzeptiert Ordner mit `<name>/SKILL.md`, passt also
direkt auf das bestehende `packages/<name>/<name>/`-Layout. `agents` braucht einzelne
`.md`-Dateien. Installation: `/plugin marketplace add benjaminstelzer/scoville-suite-for-claude`,
dann `/plugin install scoville@...`. Der Pluginname `scoville` hält die Namensräume kurz
(`/scoville:scoville-plan`).

Warum Plugin statt Skills plus `~/.claude/agents/`: ein Installationsschritt, native Updates,
keine zweite Kopierroute. Plugin-Agents ignorieren `permissionMode`, `hooks`, `mcpServers`.
Der Reviewer bleibt trotzdem schreibgeschützt über `tools: Read, Grep, Glob, Bash`.

Tests: `test_build_suite.py` um `('claude', 7)` erweitern und einen Regressionstest ergänzen,
der die Codex- und General-Dateihashes gegen die letzten Receipts vergleicht.

## 3. Workflow for Claude

### 3.1 Architektur-Blocker aus der Doku

| Annahme in PLAN-0015 | Doku 2026-09-28 |
| --- | --- |
| Coordinator läuft als Subagent und startet Worker | Verschachtelung bis Tiefe 3 möglich, aber nur mit `Agent`-Tool |
| Vordergrund-Coordinator blockiert die Hauptunterhaltung | Fork-Modus ist interaktiv Standard: alle Subagenten laufen im Hintergrund, Claude kann keinen Vordergrund anfordern |
| Hintergrund-Worker melden sich per Benachrichtigung | stimmt |
| - | Hintergrund-Subagenten verlieren `Agent` |

Folge: Die Architektur "schlanke Hauptunterhaltung, Coordinator als Subagent" funktioniert
interaktiv nur mit abgeschaltetem Fork-Modus oder `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.
Beides ändert das Verhalten der ganzen Sitzung des Nutzers.

Drei Varianten für die W-001-Entscheidung:

| | A: Hauptsitzung koordiniert | B: Coordinator-Subagent (PLAN-0015) | C: Dynamic Workflow als Treiber |
| --- | --- | --- | --- |
| Nähe zum Codex-Original | hoch ("calling task coordinates") | mittel | gering |
| Worker/Reviewer | Hintergrund-Subagenten, Abschlussbenachrichtigung, kein Polling | gleich | `agent()` im Skript |
| Coordinator-Rollover | nicht nativ automatisch: Handoff in `.scoville/workflow.md`, Auto-Compaction als Netz, frische Sitzung durch Nutzer | frischer Coordinator-Subagent | entfällt: jede Coordinator-Entscheidung ist ein frischer Agent |
| Nutzerfragen | direkt (AskUserQuestion) | über Hauptsitzung | beendet den Lauf, Wiederaufnahme nötig |
| Voraussetzung | keine | Fork-Modus aus | Workflows aktiviert, Freigabeprompt, `agent()` mit Modell/Effort/Agenttyp |
| Risiko | ADR-0063 fordert automatischen Coordinator-Rollover | interaktiv blockiert | Zustand je Entscheidung neu lesen, Kosten |

Empfehlung: A als Basis. Sie hat die wenigsten Unbekannten und entspricht dem Codex-Ablauf.
Die Coordinator-Last pro Unit ist klein, weil Auftrag und Ergebnis kurz sind und der Auftrag
als Datei entsteht. W-001 prüft zusätzlich, ob Claude selbst eine frische Hintergrundsitzung
starten kann (Agent View, Cross-Session-Messaging). Falls ja, wird daraus der automatische
Coordinator-Nachfolger. C bleibt Kandidat für eine spätere Version, wenn `agent()` Modell,
Effort und eigene Agenttypen belegt unterstützt.

### 3.2 Abbildung der Codex-Operationen

| Codex (heute) | Claude Code |
| --- | --- |
| `create_thread` mit prompt, title, model, thinking | `Agent` mit `subagent_type`, `description` (Titel), `name`, `model` |
| Titel `S-WORK-#n-W-001/STEPS-1-3` | `description`/`name` gleich |
| Ergebnis per `send_message_to_thread`, `RESULT NOT DELIVERED` | letzte Antwort des Subagenten, entfällt |
| Archivierung, `set_thread_archived` | entfällt, Subagent endet |
| Rückfrage an Worker | `SendMessage` an Agent-ID/Name |
| Stopp | `TaskStop` |
| Rollover-Nachfolger bestätigt Empfang beim Vorgänger | entfällt, Vorgänger ist beendet |
| `CODEX_THREAD_ID` + Rollout-JSONL | Transkript unter `~/.claude/projects/...`, Identität über Auftragsmarker oder Hook-Feld `agent_id` (W-001) |
| Nutzerentscheidung im Worker | AskUserQuestion fehlt in Subagenten: `needs_user_decision` zurückgeben |

Die gesamten Abschnitte "Archive", "Native answer delivery" und die Empfangsbestätigungen
fallen weg. Genau diese Teile erzeugen im Codex-Build den meisten Aufwand.

### 3.3 Dateien des neuen Members

| Datei | Herkunft |
| --- | --- |
| SKILL.md | neu, Struktur wie Codex, `disable-model-invocation: true`, `${CLAUDE_SKILL_DIR}` für Helper-Pfade |
| references/operations*.md | aus Codex portiert, Host-Werkzeuge ersetzt (Tabelle 3.2) |
| assets/workflow.toml | eigene Defaults (Claude-Modelle, Effort `low`...`max`, 40/60) |
| scripts/build_dispatch_prompt.py | Rolleninhalt übernehmen, Zustell-, Archiv- und Thread-ID-Zeilen streichen, Auftrag als Datei schreiben |
| scripts/check_context_checkpoint.py + inspect_claude_context.py | Telemetrie aus Claude-Transkript (`usage` inkl. Cache-Tokens), gleiche Schwellenlogik |
| scripts/resolve_model_pair.py, workflow_settings.py | fast unverändert, liefert zusätzlich `subagent_type` |
| scripts/select_context.py | wie heute aus scoville-plan |
| agents/scoville-worker-<effort>.md, scoville-reviewer-<effort>.md | generiert aus je einer Vorlage (4.3) |

Die Rollenregeln in `build_dispatch_prompt.py` sind zu etwa 80 Prozent hostneutral. Zwei Wege:

- **Kopie im Claude-Member** (empfohlen für den ersten Release): Codex bleibt bytegleich.
  Kosten: doppelte Pflege von Auswahl- und Rollenlogik.
- **Gemeinsamer Kern in `shared/runtime/`** mit hostspezifischen Zeilen: eine Quelle, aber
  ein Codex-Release mit geänderten Helper-Bytes. Sinnvoll als zweiter Schritt.

### 3.4 Effort pro Route

Das Agent-Tool nimmt `model` pro Aufruf, `effort` nur im Frontmatter. Die Routentabelle
(Modell plus Effort) braucht daher je Rolle eine Agent-Datei pro Effortstufe:
`scoville-worker-{low,medium,high,xhigh,max}`, dasselbe für Reviewer. Der Builder erzeugt
sie aus einer Vorlage mit Dateivariablen. Einfachere Alternative: nur Modell pro Route,
Effort erbt die Sitzung. Das spart zehn Dateien, bricht aber mit der Codex-Konfiguration.

### 3.5 Überholte Punkte in PLAN-0015

PLAN-0015 stammt vom 2026-09-26 und liegt vor PLAN-0016 bis 0018. Anzupassen:

- `SCOVILLE_RESULT_V1` ist durch ADR-0101 ersetzt: normale Nachricht mit Status.
- Fixer-Rolle und `S-FIXR` entfallen (ADR-0101): Korrektur ist ein neuer Worker.
- "Reparaturgrenze drei" ist durch Ursachenprüfung nach zwei gescheiterten Korrekturen ersetzt.
- Step-Gruppen (ADR-0093), Review-Rhythmus (ADR-0102) und Step-Split beim dritten Handoff fehlen.
- `.scoville/assignments/` bleibt sinnvoll: Der Auftrag wird nie in den Coordinator-Kontext gedruckt.
- W-001 muss zuerst den Fork-Modus-Befund prüfen, interaktiv und headless getrennt.

## 4. Ask for Claude

### 4.1 Spiegelung des Originals

```text
Ask for Codex (Original)                 Ask for Claude (neu)
route native     -> Codex-Chat           route native    -> Claude-Subagent (scoville-adviser-*)
route claude-cli -> ask_claude.py        route codex-cli -> ask_codex.py   ("Ask Codex")
```

Die native Route wird deutlich einfacher als bei Codex. ADR-0085 schließt Subagenten für
Codex aus, weil Codex kein `close_agent` hat. Das gilt für Claude Code nicht: Hintergrund-
Subagenten laufen parallel, melden sich per Benachrichtigung, enden selbst und lassen sich
per `SendMessage` fortsetzen. Damit entfallen `native-delivery.md`, Rückgabe-Thread,
Titel-Pflicht in der Sidebar, Archivierung und die Chat-Autorisierung. Das braucht eine
eigene ADR für den Claude-Host.

### 4.2 Dateien

| Datei | Umgang |
| --- | --- |
| SKILL.md | neu, gleicher Ablauf (Modus, Frage, Sammeln, Synthese), native Schritte über `Agent` |
| references/adviser.md | gemeinsam per Dateieintrag aus Ask for Codex; letzter Satz zur Zustellung als Profilblock |
| references/configuration.md | gemeinsam mit Profilblöcken für Routen und CLI-Abschnitt |
| references/codex.md | neu, Gegenstück zu claude.md |
| references/claude-native.md | neu, ersetzt native.md und native-delivery.md |
| scripts/ask.py, ask_settings.py | Routenmenge heute hart `{native, claude-cli}`; siehe 4.4 |
| scripts/ask_codex.py | neu, Gegenstück zu ask_claude.py |
| config.default.json | eigene Defaults |
| agents/scoville-adviser-<effort>[-web].md | generiert; Tools Read, Grep, Glob, Web-Variante zusätzlich WebSearch, WebFetch |

### 4.3 Ask-Codex-Adapter

Aufruf, analog zu `ask_claude.py`:

```text
codex exec - --json -m <model> -c model_reasoning_effort=<effort>
           --sandbox read-only --disable apps --skip-git-repo-check -C <cwd>
           -c web_search="disabled"            # opt-in: "live"
           [--ephemeral]                       # session_persistence=false, keine Folgefragen
           [--ignore-user-config --ignore-rules]  # customizations=false, Anmeldung bleibt
Folgefrage (cwd = Prozessverzeichnis, kein -C):
           codex exec resume <thread_id> - --json -c sandbox_mode="read-only"
```

Befunde aus W-001 ([capabilities](../development/claude-code/capabilities.md)), die in Adapter und Doku gehören:

- `codex exec resume` akzeptiert kein `-s/--sandbox` und schreibt ohne Override trotz read-only-Start
  (belegt, vgl. openai/codex#40149). `-c sandbox_mode="read-only"` bei jedem Resume ist Pflicht.
- Websuche ist in `codex exec` standardmäßig an und gilt ab Start. Das Resume kann sie nicht umschalten.
- Ohne `--disable apps` sieht auch ein read-only-Adviser App-Werkzeuge mit Außenwirkung.
- Antwort und Sitzung kommen aus dem JSONL-Strom: `thread.started` liefert die ID, die letzte
  `agent_message` die Antwort, `turn.completed` die Nutzung. Fehler kamen nur als Exit-Code und stderr.
- Codex liegt je nach Installation an verschiedenen Orten. Der Adapter nutzt PATH mit konfiguriertem Vorrang.
- Kein Budgetlimit wie `--max-budget-usd`. Es bleibt nur `timeout_seconds`.
- Die Prozessgruppen- und Timeout-Logik aus `ask_claude.py` ist wiederverwendbar.

### 4.4 Konfiguration

`.scoville/config.json` kann von beiden Hosts im selben Projekt gelesen werden. Ein Preset
`astra` mit `route: native` ist unter Claude ungültig. Deshalb getrennte Abschnitte:
Codex behält `ask` und `workflow` unverändert, Claude liest `claude.ask` und
`claude.workflow` (Name ist Entscheidung). `scoville_config.section()` erlaubt heute nur
`ask` und `workflow` und wird erweitert. Weil diese Datei auch in Codex-Pakete kopiert wird,
ändert das Codex-Bytes. Byte-Gleichheit erreicht man nur mit einer Claude-eigenen Kopie oder
einer Profilauswahl im Builder für `.py`-Dateien. Entschieden (ADR-0106): eigener Helper
`scoville_claude_config.py` auf Basis von `read_config()`, nur im Profil `claude`, Codex bleibt bytegleich.

## 5. READMEs

Gemeinsam bleiben: alle Fragmente von Code, Plan, UI, Handoff, `name-origin.md`, `shared/readme/*`.
Anpassungen über Profilblöcke:

- `suite-intro.md`: Block `claude` mit Titel "Scoville Suite for Claude Code" und Tabelle.
  Die Zeile "Claude Code or other Agent Skills hosts: Scoville Suite" zeigt dann auf die
  Claude-Suite, die allgemeine Suite bleibt für andere Hosts.
- `suite-install.md`: Block `claude` mit Plugin-Installation.
- `codex-limitations.md`: in `host-limitations.md` umbenennen, Block `claude` (Fork-Modus,
  Plugin-Agent-Grenzen).
- `suite-requirements.md`, `skill-installation-contract.md`, `scoville-install.md`: Blöcke
  auf `codex claude` erweitern oder Claude-Block ergänzen.
- Neue Fragmentordner `development/readme/scoville-workflow-claude/` und `scoville-ask-for-claude/`.
  Hostneutrale Abschnitte (etwa "What it enforces") können beide Workflow-Member als
  gemeinsame Datei referenzieren; der Export behält geteilte Fragmente bereits.

## 6. Regeln und Entscheidungen, die geändert werden müssen

| Ort | Heute | Nötig |
| --- | --- | --- |
| `<workspace-root>/AGENTS.md` | Workflow Codex-only, zwei feste Ziele | Claude-Workflow nur in `scoville-suite-for-claude`, Ziel `skills/public/scoville-suite-for-claude/`; veralteter Pfad `ask-suite-for-codex` entfernen |
| `skills/AGENTS.md` | "Prefer native Codex capabilities" | gleiche Regel für Skills mit Claude im Namen |
| `scoville-suite/AGENTS.md` | Workflow Codex-only, `close_agent`-Check | Profil `claude` nennen; Check bleibt Codex-spezifisch |
| ADR-0013 | zwei Profile, Revisit bei weiterem Host | neue ADR "drittes Profil claude" |
| ADR-0001/0079 | Workflow nur Codex-Suite | neue ADR für Workflow for Claude in eigener Suite |
| ADR-0085 | Subagenten kein Ask-Ersatz | neue ADR: gilt nur für Codex |
| ADR-0063 | automatischer Coordinator-Rollover Pflicht | je nach Variante A bestätigen oder einschränken |

## 7. Reihenfolge

1. W-001 Spike (installierte Claude-Code- und Codex-CLI-Version): Fork-Modus und `Agent` im
   Hintergrund, Transkriptzugriff, Effort-Varianten, frische Sitzung durch Claude,
   `codex exec` read-only inkl. Resume. Danach Entscheidungen A/B/C, Plugin, Konfig-Abschnitte.
2. Builder verallgemeinern, Profil `claude` nur mit Code/Plan/UI/Handoff bauen, Codex und
   General auf Bytegleichheit prüfen.
3. Setup für beide Hosts.
4. Ask for Claude (kleiner, gut testbar, liefert Adviser-Agent und Codex-Adapter).
5. Workflow for Claude.
6. `claude -p`-Helpertests und interaktiver Ende-zu-Ende-Lauf (Fork-Modus an!), dann Release-Gate.

## Offene Entscheidungen

- Coordinator-Architektur A, B oder C.
- Namen: `scoville-suite-for-claude` oder `-for-claude-code`; Pluginname `scoville`.
- Effort-Varianten als Agent-Dateien oder nur Modell pro Route.
- Konfigurationsabschnitte für Claude und ob Codex dafür eine neue Helper-Version erhält.
- Ask for Claude zunächst suite-only (Adviser-Agents brauchen das Plugin).
