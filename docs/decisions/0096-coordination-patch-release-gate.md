---
format_version: 1
id: ADR-0096
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/coordination-patch-release
---

# Gezielte Abnahme für die Korrektur-Releases

## Decision

Der Nutzer nimmt beide Suites v2.0.1 und Ask v1.0.1 vom vollständigen
45-Fall-Luna-Gate aus. Gezielt ausgeführte Tests, Astra-High-Review,
Build-, Paket- und Remoteprüfungen bleiben erforderlich.

## Problem

Die Ausnahme ADR-0081 galt nur für den vorherigen Release.

## Drivers

- Nutzerantwort: Ja, gleiche Ausnahme für diese Korrektur-Releases.
- Die Korrektur betrifft Nachrichtenverträge und Suite-Portabilitätsprüfungen.

## Considered alternatives

- Vollständiges Luna-Gate: für diesen Patch vom Nutzer nicht gewählt.
- Gezielte Abnahme: bestehende Review- und Testnachweise ergänzen die Releaseprüfungen.

## Consequences

Kein vollständiger Luna-Pass wird behauptet. Andere Releases erhalten keine
automatische Ausnahme. Der Nutzer bestätigt zuletzt den ursprünglichen Umfang
einschließlich des Ask-Einzel-Releases. Veröffentlichung bleibt an die übrigen Gates gebunden.

## Confirmation

Prüfe Tests, Astra-Nachprüfung, saubere Builds, Remote-Bäume und Releaseassets.

## Revisit when

Der Releaseumfang oder die Nutzerentscheidung ändert sich.
