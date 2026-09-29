---
format_version: 1
id: ADR-0114
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: workflow/claude-context
supersedes: ADR-0110
---

# Kontextfenster für Claude-Worker per `/context`

## Decision

Nutzerentscheid: Beim ersten Einsatz einer Modellfamilie im Lauf ermittelt der Dispatch-Helper per `claude -p --model <familie> --output-format json "/context"` die aufgelöste Modell-ID und ihr Kontextfenster. Er legt beides im Laufverzeichnis ab und schreibt es in die Auftragsdatei. Der Worker-Checkpoint liest das Fenster aus dem Auftrag und die Nutzung aus seinem Transkript. Ist die Ausgabe nicht lesbar oder weicht die Modell-ID im Transkript ab, meldet er fehlende Telemetrie mit Diagnose und schätzt nie. Eine Modelltabelle gibt es nicht.

## Problem

Transkripte und Hook-Eingaben enthalten kein Kontextfenster. ADR-0110 brauchte deshalb feste Werte je Modell, die bei jedem neuen Modell gepflegt werden müssen.

## Drivers

- Keine festen Werte, das Fenster soll für das jeweilige Konto stimmen.
- Der Worker-Handoff ist unter Claude der einzige Rollover (ADR-0104).
- Höchstens ein Helper-Aufruf pro Dispatch, fehlende Telemetrie wird nie geschätzt.

## Considered alternatives

- Modelltabelle mit Defaults (ADR-0110): stabil, aber zu pflegen.
- `/context` mit Tabelle als Reserve: mehr Mechanik für einen seltenen Formatwechsel.

## Consequences

`/context` läuft ohne Modellaufruf und ohne Kosten, liefert aber formatierten Text statt einer dokumentierten Schnittstelle, mit gerundeten Werten wie `200k` oder `1m`. Ändert sich das Format, fällt der Worker-Handoff aus, bis der Parser angepasst ist, und die Auto-Compaction bleibt das Netz. Der erste Dispatch je Familie dauert einige Sekunden länger. Die in ADR-0112 genannte Modelltabelle in `claude.workflow` entfällt.

## Confirmation

Ein Helpertest liest `/context` für jede Modellfamilie, und das Release-Gate führt ihn aus. Nicht lesbare Ausgabe und abweichende Modell-ID enden mit Diagnose. W-008 zeigt einen schwellenausgelösten Worker-Handoff für mindestens zwei Modellfamilien.

## Revisit when

Transkript oder Hook-Eingabe liefern das Fenster, Claude Code bietet eine strukturierte Abfrage, oder das Format von `/context` ändert sich wiederholt.
