---
format_version: 1
id: ADR-0136
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: ask/native-agent-capacity
supersedes: ADR-0132
---

# Ask bewahrt Antworten ohne Kapazitätsbereinigung

## Decision

Die ausdrückliche Entfernung aus ADR-0135 umfasst auch Ask. Der automatische
Drain-/Recovery-/Retry-Weg und reine Bereinigungsturns entfallen. Eine
Kapazitätsablehnung lässt nicht gestartete Berater offen, erhält Diagnose,
Antworten und exakte Handles und erzeugt keine Ersatzberater oder Ersatzchats.

Die übrigen Abschlussregeln bleiben: vollständigen nativen Final akzeptieren,
keine Routinequittung danach, fehlende Finals offen halten und notwendige
Folgefragen an denselben Handle mit denselben Einstellungen richten. Claude
CLI behält seinen eigenen Sessionvertrag.

## Problem

Der frühere Ask-Vertrag übernahm den unzuverlässigen Kapazitäts-Workaround.
Ein neuer Bereinigungs-Final bestätigt keine freigegebenen Hostplätze.

## Drivers

- Vollständige Entfernung in beiden angebundenen Skills.
- Unabhängige Antworten und echte Folgefragen erhalten.

## Considered alternatives

- Begrenzten Retry behalten: zusätzliche Turns ohne belegte Fehlerbehebung.

## Consequences

ADR-0132 und seine Tests bleiben erhaltene Historie. Aktive Anweisungen,
gemeinsame Quellen, Buildregistrierung und Dokumentation verwenden den neuen
Fehlervertrag. Der ursprüngliche Ask-Ergebnis-/Follow-up-Test bleibt relevant.

## Confirmation

Gebauter Beraterprompt und native Delivery behalten Abschluss und Folgefragen.
Kapazitätsablehnung führt zu offener Beratung mit erhaltenen Ergebnissen,
ohne Bereinigungsauftrag oder automatischen Retry. Paket-/Consumerprüfungen
prüfen die geänderten Quellen, ohne einen Hostfehler vorzutäuschen.

## Revisit when

Ein belegter neuer Hostvertrag wird ausdrücklich beauftragt.
