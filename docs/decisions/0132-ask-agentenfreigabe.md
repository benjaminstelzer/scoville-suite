---
format_version: 1
id: ADR-0132
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: ask/native-agent-capacity
---

# Native Ask-Agenten über denselben begrenzten Weg freigeben

## Decision

Der Nutzer übernimmt die Workflow-Freigabelogik ausdrücklich auch für Ask.
Der Berater beendet seinen Turn mit der vollständigen nativen Antwort. Der
Aufrufer wartet auf diesen Abschluss und schickt keine Routinequittung danach.
Bei eindeutig abgelehntem Kapazitätsstart ohne erzeugten Agenten darf Ask nur
seine eigenen bestätigten abgeschlossenen Berater mit vollständigen Antworten
einmal schreibinaktiv wecken. Nach tatsächlichem Bereinigungsabschluss folgt
höchstens ein erneuter Start mit denselben Argumenten.

## Problem

Wartende Nachrichten können einen beendeten Berater resident halten.
Ein gespeicherter Handle oder ein zugestelltes Followup beweist keine freie
Kapazität und keinen Turn-Abschluss.

## Drivers

- Ausdrücklicher Nutzerauftrag zur gleichen Agentenfreigabe in Ask.
- Vollständige unabhängige Antworten und notwendige Folgefragen erhalten.
- Keine doppelten Berater durch unklare Starts.

## Considered alternatives

- Unklare Starts erneut ausführen: kann doppelte Beratungen erzeugen.
- Handles oder Antworten verwerfen: verliert Ergebnisse und Folgefragen.

## Consequences

Ask behält Ergebnisse, Handles, Modelle und Efforts. Nur der eindeutige
Kapazitätsfehler erlaubt diesen einmaligen Bereinigungsweg. Andere Fehler,
STOP oder unsichere Zustände verhindern den Retry. Claude CLI bleibt unter
seinem eigenen Sessionvertrag.

## Confirmation

Gebauten nativen Beraterprompt unverändert verwenden, tatsächlichen Final und
begrenzten Bereinigungs-Turn prüfen. Kapazitätsablehnung und erneuten Spawn nur
als ausgeführt bezeichnen, wenn sie nativ beobachtet wurden. Astra Medium prüft
alle Ask-Abschlusswege und den Abgleich mit Workflow.

## Revisit when

Der Host bietet einen überprüfbaren Close-Vertrag oder andere Residency-Regeln.
