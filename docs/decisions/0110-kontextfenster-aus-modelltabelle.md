---
format_version: 1
id: ADR-0110
status: superseded
created: 2026-09-28
accepted: 2026-09-28
scope: workflow/claude-context
superseded_by: ADR-0114
---

# Kontextfenster für Claude-Worker aus einer Modelltabelle

## Decision

Nutzerentscheid: Der Worker-Checkpoint unter Claude bestimmt das Kontextfenster aus einer Modelltabelle in `claude.workflow`. Sie hat Defaults je Modell-ID und ist im Projekt überschreibbar. Die Modell-ID liest der Checkpoint aus dem Worker-Transkript (`message.model`). Defaults werden per `claude -p --model <familie> --output-format json` aus `modelUsage.<modell>.contextWindow` gemessen. Ein Modell ohne Eintrag gilt als fehlende Telemetrie und wird mit Diagnose gemeldet, nie geschätzt.

## Problem

Claude-Code-Transkripte enthalten die Nutzung, aber kein Kontextfenster. Die Fenster unterscheiden sich je Modell stark. Ohne Fenster löst `worker_percent` nie einen Handoff aus. W-001 wurde geschlossen, ohne dass ADR-0109 diese Lücke nennt.

## Drivers

- Der Worker-Handoff ist unter Claude der einzige Rollover (ADR-0104).
- Prozent-Schwellen wie bei Codex (ADR-0098).
- Fehlende Telemetrie wird gemeldet, nie geschätzt.

## Considered alternatives

- Absolute Tokenschwelle je Modellfamilie: kein Fenster nötig, aber keine Prozent-Parität mit Codex.
- Ohne bekanntes Fenster kein Handoff: der Worker-Handoff fiele praktisch aus.

## Consequences

Ein neues Modell braucht einen Tabelleneintrag. Setup zeigt die Tabelle. Aliasse wie `opus` lösen sich im Transkript zu einer Modell-ID auf, die Tabelle ist deshalb nach Modell-ID geschlüsselt.

## Confirmation

W-004 testet Tabelle, Überschreibung und die Diagnose für ein unbekanntes Modell. W-008 zeigt einen schwellenausgelösten Worker-Handoff für mindestens zwei Modellfamilien.

## Revisit when

Transkript oder Hook-Eingabe liefern das Kontextfenster selbst.
