---
format_version: 1
id: ADR-0159
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
supersedes: ADR-0158
---

# Claude-Aufrufe sind erlaubt

## Decision

Claude darf aus diesem Auftrag aufgerufen werden. Eine spätere unabhängige
Nutzerprüfung bleibt möglich, ist aber nicht mehr die einzige Claude-Teststrecke.

## Problem

ADR-0158 untersagte Claude-Modellläufe durch diesen Auftrag.

## Drivers

Ausdrückliche Nutzerfreigabe: „Claude darf aufgerufen werden“.

## Considered alternatives

Die ausschließliche externe Nutzerprüfung entspricht nicht mehr der Freigabe.

## Consequences

Die Freigabe ändert weder die Astra-High-Reviews nach jedem Planpunkt noch den
Stopp vor W-001. Modelltests beginnen weiterhin nach den Skill-Änderungen in
W-014. Offene Budget- und Live-Testentscheidungen bleiben wirksam.

## Confirmation

Spätere Ergebnisse nennen Paketstand, Cases, Modell, Effort und Grenzen.
Lokale Tests mit Doubles werden nicht als Claude-Modellnachweis gewertet.

## Revisit when

Der Nutzer die Freigabe oder die Zuständigkeit für Tests ändert.
