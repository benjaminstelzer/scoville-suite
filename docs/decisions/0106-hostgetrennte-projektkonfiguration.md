---
format_version: 1
id: ADR-0106
status: superseded
created: 2026-09-28
accepted: 2026-09-28
scope: suite/configuration
superseded_by: ADR-0112
---

# Hostgetrennte Projektkonfiguration

## Decision

Nutzerentscheid: `.scoville/config.json` behält `ask` und `workflow` für Codex unverändert. Claude liest eigene Abschnitte `claude.ask` und `claude.workflow`. `claude.workflow` hat die Routentabelle aus ADR-0105 und nur `worker_percent` (ADR-0104). Ein eigener kanonischer Helper `shared/runtime/scoville_claude_config.py` liest diese Abschnitte über `read_config()` aus `scoville_config.py` und wird nur im Profil `claude` ausgeliefert. `scoville_config.py` und die Codex-Pakete bleiben bytegleich.

## Problem

Beide Hosts können dasselbe Projekt nutzen. Ein Codex-Preset wie `astra` mit `route: native` ist unter Claude ungültig, und Claude-Modellfamilien sind unter Codex ungültig.

## Drivers

- Ein kanonischer Owner je Konfigurationslogik.
- Keine stille Ersetzung ungültiger Werte.
- Kein Codex-Release ohne Verhaltensänderung.

## Considered alternatives

- Gemeinsame Abschnitte: Presets kollidieren zwischen Hosts.
- `section()` in `scoville_config.py` erweitern: Logik an einer Stelle, aber geänderte Codex-Bytes und ein Codex-Release ohne Verhaltensänderung.
- Claude-eigene Kopie von `scoville_config.py`: Konfigurationslogik doppelt gepflegt.

## Consequences

Setup zeigt und speichert beide Hosts. Veröffentlichte Codex-Pakete ignorieren einen `claude`-Abschnitt beim Lesen, und das Codex-Setup erhält ihn beim Speichern (geprüft am 2026-09-28). Das Profil `claude` enthält eine Helper-Datei mehr.

## Confirmation

Tests lesen eine Datei mit beiden Abschnitten aus beiden Hosts. Codex-Werte, -Diagnosen und -Paketbytes bleiben unverändert. Ungültige Claude-Werte melden Fundstelle, erwarteten Wert und kleinste Korrektur.

## Revisit when

Ein Host braucht projektübergreifende Einstellungen oder die Abschnitte driften fachlich auseinander.
