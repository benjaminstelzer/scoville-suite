---
format_version: 1
id: ADR-0107
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: ask/claude-host
---

# Ask for Claude mit Adviser-Subagenten und Codex CLI

## Decision

Nutzerentscheid: Die native Route startet schreibgeschützte Adviser-Subagenten mit `Read`, `Grep` und `Glob`, Webzugriff nur als opt-in-Variante. Mehrere Advisers laufen parallel, ihre Antwort ist die letzte Nachricht, Folgefragen nutzen `SendMessage`. Das Modell ist eine Familie, der Effort kommt aus der Agent-Datei (ADR-0105). Eine verlangte feste Modellversion wird gemeldet, nicht ersetzt. Die Route `codex-cli` nutzt `ask_codex.py` analog zu `ask_claude.py` mit `codex exec - --json --sandbox read-only --disable apps`. `--disable apps` entfernt App-Werkzeuge mit Außenwirkung wie GitHub-Commits oder Site-Deployments, die sonst auch read-only sichtbar sind. Websuche ist in `codex exec` standardmäßig an. Der Adapter setzt `-c web_search="disabled"` und nur bei opt-in `"live"`. Die Einstellung gilt ab Start, eine Folgefrage erbt sie. Jede Folgefrage setzt `-c sandbox_mode="read-only"`, weil `codex exec resume` kein `--sandbox` akzeptiert und ohne Override schreiben kann. `resume` kennt kein `-C`, das Arbeitsverzeichnis kommt vom Prozess. Mit `session_persistence=false` (`--ephemeral`) gibt es keine Folgefragen, Ask meldet das. Codex wird über den PATH gefunden, ein konfigurierter Pfad hat Vorrang. Erfolg heißt Exit 0 und nicht leere letzte `agent_message`. stderr allein ist kein Fehler. Ask for Claude ist zunächst suite-only. Der Subagent-Ausschluss aus ADR-0085 gilt nur für Codex.

## Problem

Codex-Advisers brauchen eigene Chats, weil Codex kein `close_agent` hat. Claude-Subagenten enden selbst, melden sich per Benachrichtigung und lassen sich fortsetzen. Zustellvertrag, Titel und Archivierung sind unter Claude unnötig. Die Codex-CLI-Befunde stammen aus `codex-cli` 0.154 und 0.158 ([capabilities](../../development/claude-code/capabilities.md)).

## Drivers

- Nutzerauftrag: Ask Codex als Variante von Ask Claude.
- Advisers bleiben read-only und unabhängig vom Urteil des Aufrufers.
- Webzugriff standardmäßig aus (ADR-0047).

## Considered alternatives

- Nur Codex CLI: keine Claude-Zweitmeinung mit anderem Modell.
- Claude CLI als Subprozess für Claude-Advisers: zusätzlicher Prozess ohne Vorteil gegenüber Subagenten.

## Consequences

`native.md` und `native-delivery.md` haben kein Claude-Gegenstück. Codex CLI kennt kein Budgetlimit, nur `timeout_seconds` begrenzt den Aufruf. Adviser-Agents brauchen das Plugin aus ADR-0105.

## Confirmation

Parallele Advisers liefern unabhängige Antworten. Eine Folgefrage behält Modell und Sitzung. Adviser-Subagenten und Codex-Resume können nicht schreiben. Codex-Advisers sehen ohne opt-in weder Websuche noch `codex_apps`-Werkzeuge. Ein von einem Codex-Adviser über `collaboration.spawn_agent` gestarteter Unteragent kann nicht schreiben. Timeout, fehlende Anmeldung und leere Antwort enden als Fehler mit Diagnose.

## Revisit when

Codex CLI akzeptiert `--sandbox` beim Resume, ändert Web- oder App-Defaults, oder Claude Code ändert Lebensdauer und Fortsetzung von Subagenten.
