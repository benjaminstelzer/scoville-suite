---
format_version: 1
id: ADR-0165
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/execution
supersedes: ADR-0163
---

# Gesamten Umbau unabhängig prüfen und den Plan ausführen

## Decision

Der gesamte bisherige Umbau erhält ein unabhängiges Review durch gpt-6-astra
mit high und frischem Kontext. Bestätigte Fehler werden korrigiert. Anschließend
wird PLAN-0034 einschließlich W-014 und W-015 bis zur erfüllten Abnahme verfolgt.

## Problem

Die bisherige Begrenzung auf W-001 und der Ausschluss weiterer Reviews gelten
für diesen neuen Auftrag nicht mehr.

## Drivers

Ausdrücklicher Nutzerauftrag: gesamtes Astra-high-Review, Fehlerbehebung und
Zielsetzung zur Planausführung.

## Considered alternatives

Ein erneuter Stopp allein an der alten W-001-Grenze würde dem Auftrag widersprechen.

## Consequences

Die Abhängigkeiten und Acceptance-Kriterien bleiben erhalten. Die 150 Luna-high-
Versuche und gruppierte Sol-6.1-high-Bewertung gelten weiter. Modellkosten sind
nach ADR-0164 kein Testhindernis. Konkrete externe Voraussetzungen und gesonderte
Freigaben für CI-Push, native Proben und zusätzliche Versuche bleiben zu klären.
Der Auftrag enthält keine Veröffentlichung oder automatische Installation.

## Confirmation

Review und bestätigte Korrekturen sind belegt. Der Plan endet erst mit erfüllter
Abnahme; fehlende Pflichtnachweise bleiben sichtbar offen.

## Revisit when

Umfang, Modelle, Versuchslimit oder externe Freigaben geändert werden.
