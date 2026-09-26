---
format_version: 1
id: ADR-0093
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: workflow/dispatch
---

# Zusammenhängende Steps in Reihenfolge bearbeiten

## Decision

Kleine zusammengehörige Steps dürfen einen Worker-Auftrag bilden. Die Reihenfolge bleibt innerhalb und zwischen Aufträgen erhalten. Ein Auftrag umfasst einen Step, einen zusammenhängenden Bereich oder den ganzen Planpunkt. Review prüft diesen Auftrag.

Der Worker erhält den vollständigen Planpunkt als Kontext und den eindeutig benannten Auftrag. Der Coordinator ergänzt nur relevante Goals, Non-goals, geltende ADR-Vorgaben und benötigte Abhängigkeitsergebnisse. Dafür genügt supplemental-context; keine neue Auswahlmechanik.

Rollover erfolgt bei Kontextbedarf an einer sinnvollen Arbeitsgrenze. Die Übergabe nennt erledigte Teile, Änderungen, tatsächliche Checks, offene Arbeit und den nächsten Schritt. Der Nachfolger setzt denselben Auftrag fort.

## Problem

Ein Worker pro kleinem Step wiederholt Kontext und Einarbeitung. Zu knapper Kontext verliert Anforderungen; unklarer Umfang verleitet zum Vorwegnehmen anderer Arbeit.

## Drivers

- Einfacher nativer Ablauf mit wenig Tokenaufwand.
- Ausreichender Kontext und verbindliche Reihenfolge.

## Considered alternatives

- Jeder Step einzeln: unnötiger Aufwand bei kleinen zusammengehörigen Arbeiten.
- Immer ganzer Planpunkt: unnötig starr bei großen eigenständigen Abschnitten.

## Consequences

Diese Nutzerentscheidung ersetzt die frühere Einzel-Step-Pflicht für neue Dispatches. Historische Abnahmen bleiben erhalten. Keine neuen Statusmodelle, Gruppierungsfelder oder Helper. Bestehende Bereiche wie W-001/steps-1-4 werden verwendet.

## Confirmation

SOL 6 Medium bearbeitet eine Gruppe in Reihenfolge und setzt nach einem Rollover nur die Restarbeit fort. Der nächste Bereich startet erst nach Annahme des vorherigen.

## Revisit when

Eine konkrete Fehlzuordnung oder verlorene Restarbeit wird beobachtet.
