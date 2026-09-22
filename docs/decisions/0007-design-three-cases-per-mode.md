---
format_version: 1
id: ADR-0007
status: superseded
created: 2026-09-21
accepted: 2026-09-21
scope: suite/evaluation-coverage
supersedes: ADR-0006
superseded_by: ADR-0008
---

# Design mit drei Fällen je Arbeitsmodus prüfen

## Decision

Der Nutzer bestimmt für Design je drei Fälle für Generate, Critique und Repair: neun insgesamt. Code behält 25, die drei Ask-Templatebasen je drei und die übrigen sieben Sets je zehn. Gesamtumfang: 113 Fälle.

## Problem

Die vorherige Formulierung „je Routine“ ließ die Design-Abdeckung offen.

## Drivers

- Alle drei Design-Arbeitsmodi sollen gleich vertreten sein.
- Die zuvor reduzierten Ask- und übrigen Testumfänge bleiben bestehen.

## Considered alternatives

- Ein Fall je Fachroutine: nicht die gewählte Modusabdeckung.
- Drei Fälle je Arbeitsmodus: explizite Nutzervorgabe.

## Consequences

- `development/luna-tests/selected-cases.json` ordnet Generate die Fälle 09/10/12, Critique 04/17/24 und Repair 06/21/25 zu.
- Aufgaben und Soll-Ergebnisse bleiben unverändert; jede Gruppe steigt von grundlegender Anwendung zu komplexerer Bewertung.
- SOL Medium, LUNA Medium, öffentliche Build-Pakete und unabhängige Autorenprüfung bleiben erforderlich. Workflow wird weiterhin privat geprüft.

## Confirmation

1. Prüfe drei eindeutige Design-Fälle je Modus und 113 Fälle insgesamt.
2. Prüfe die festgelegten Fälle gegen die aktuellen Pakete und unveränderten Soll-Ergebnisse.
3. Zähle nur durch SOL und Autor akzeptierte Fälle; leite keine Veröffentlichungsfreigabe ab.

## Revisit when

Der Nutzer ändert den Umfang oder ein Fehler verlangt gezielte Regressionen.
