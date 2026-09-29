---
format_version: 1
id: ADR-0105
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: suite/claude-distribution
---

# Claude-Suite als Plugin mit generierten Agent-Varianten

## Decision

Nutzerentscheid: Der `claude`-Build erzeugt an der Suite-Wurzel `.claude-plugin/plugin.json` und `marketplace.json`. `skills` verweist auf `./packages/<member>`, `agents` auf die Agent-Dateien in den Member-Ordnern. Suite-, Plugin- und Member-Namen folgen ADR-0108. Weil `effort` nur im Agent-Frontmatter wirkt, erzeugt der Builder je Rolle aus einer Vorlage eine Agent-Datei pro Effortstufe `low`, `medium`, `high`, `xhigh` und `max`. Rollen sind Worker (auch für Reparaturen), Reviewer, Adviser und Adviser mit Web. Der Coordinator ist die Hauptsitzung (ADR-0104) und hat keine Agent-Datei. Die Routentabelle hat wie bei Codex je Route `execute` und `review` mit Modell und Effort. Der Helper wählt die Agent-Datei nach dem Effort und übergibt das Modell pro Aufruf.

## Problem

Skills können keine Subagent-Definitionen mitbringen. Claude Code lädt sie nur aus Plugins, `.claude/agents/` oder `~/.claude/agents/`. Das Agent-Tool nimmt `model` pro Aufruf nur als Familie `opus`, `sonnet`, `haiku` oder `fable`, aber kein `effort`. Mit Claude Code 2.1.283 belegt: Plugin-Skills aus `./packages/<name>` mit `packages/<name>/<name>/SKILL.md`, Plugin-Agents aus Member-Ordnern, `${CLAUDE_SKILL_DIR}` in Plugin-Skills und `effort` im Agent-Frontmatter ([capabilities](../../development/claude-code/capabilities.md)).

## Drivers

- Ein Installationsschritt und native Updates.
- Bestehendes `packages/<name>/<name>/`-Layout bleibt.
- Routentabelle mit Modell und Effort wie bei Codex.

## Considered alternatives

- Skills plus manuelle Kopie nach `~/.claude/agents/`: zwei Installationswege, keine Updates.
- Nur Modell pro Route, Effort erbt die Sitzung: 15 Agent-Dateien weniger, Routen weniger steuerbar als bei Codex.

## Consequences

Plugin-Agents ignorieren `permissionMode`, `hooks` und `mcpServers`, Schreibschutz entsteht über `tools`. Skills heißen im Plugin `/scoville-suite:<skill>`. Routen nennen eine Modellfamilie, keine feste Modellversion. Codex-Effortwerte `none`, `minimal` und `ultra` sind unter Claude ungültig und werden mit Diagnose abgelehnt. Der Builder braucht Dateivariablen je Eintrag und Manifestgenerierung an der Suite-Wurzel.

## Confirmation

`claude plugin validate` besteht. Eine frische Installation in einem leeren Claude-Code-Profil findet alle Skills und Agents. Der Effort einer Agent-Variante ist im Transkript beobachtbar.

## Revisit when

Das Agent-Tool akzeptiert `effort` oder feste Modellversionen pro Aufruf, oder Skills können Agent-Dateien selbst ausliefern.
