---
format_version: 1
id: ADR-0112
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: suite/configuration
supersedes: ADR-0106
---

# Hostgetrennte Konfiguration mit gemeinsam erweiterten Helpern

## Decision

Nutzerentscheid: `.scoville/config.json` behält `ask` und `workflow` für Codex unverändert. Claude liest `claude.ask` und `claude.workflow` über `shared/runtime/scoville_claude_config.py` auf Basis von `read_config()` aus `scoville_config.py`. `scoville_config.py` bleibt bytegleich. `claude.workflow` hat die Routentabelle aus ADR-0105, die Modelltabelle aus ADR-0110 und nur `worker_percent` (ADR-0104). Die Helper `setup.py`, `ask.py` und `ask_settings.py`, die auch in Codex-Pakete gehen, werden gemeinsam um die Claude-Routen erweitert. Codex verhält sich unverändert. Die geänderten Codex-Bytes gehen mit dem nächsten regulären Codex-Release.

## Problem

ADR-0106 sicherte bytegleiche Codex-Pakete zu. `setup.py`, `ask.py` und `ask_settings.py` kodieren die Hosts hart und werden auch in Codex-Pakete kopiert.

## Drivers

- Ein kanonischer Owner je Logik, keine doppelte Setup- oder Ask-Logik.
- Keine stille Ersetzung ungültiger Werte.
- Kein eigener Codex-Release nur wegen geänderter Bytes.

## Considered alternatives

- Claude-Varianten der drei Helper per Dateieintrag je Profil: Codex bleibt bytegleich, aber die Logik von Setup und Ask wird teilweise doppelt gepflegt.
- Gemeinsame Konfigurationsabschnitte: Presets kollidieren zwischen den Hosts.

## Consequences

Codex-Pakete ändern ihre Bytes, nicht ihr Verhalten. Tests müssen das unveränderte Codex-Verhalten zeigen. Veröffentlichte Codex-Pakete ignorieren einen `claude`-Abschnitt beim Lesen (Laufzeittest am 2026-09-28), und das Codex-Setup erhält ihn beim Speichern (Quelltextprüfung von `merge`).

## Confirmation

Tests lesen eine Datei mit beiden Abschnitten aus beiden Hosts. Codex-Werte, -Diagnosen und -Verhalten bleiben unverändert. Ungültige Claude-Werte melden Fundstelle, erwarteten Wert und kleinste Korrektur.

## Revisit when

Ein Host braucht projektübergreifende Einstellungen oder die Abschnitte driften fachlich auseinander.
