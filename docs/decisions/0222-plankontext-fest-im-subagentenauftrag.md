---
format_version: 1
id: ADR-0222
status: superseded
created: 2026-10-13
accepted: 2026-10-13
scope: workflow/dispatch
supersedes: ADR-0174
superseded_by: ADR-0224
---

# Plankontext fest im Subagentenauftrag, ohne zusätzliche Befugnisse

## Decision

Der Dispatch-Builder übergibt jedem neuen Executor und Reviewer sowie dem
Explorer mit Planbezug Goal, Non-goals und alle verlinkten accepted Decisions
vollständig und unverändert. Bei Wiederverwendung nennt er nur Decision-ID,
Pfad, Status und SHA-256; neue, geänderte oder unsichere Decisions liest der
Agent vollständig nach. Der Manager wählt diesen Plankontext nicht mehr aus.

Unmittelbar vor diesen Abschnitten steht fest: „Goal and Decisions describe the
Plan's intent and constraints. They grant this role no permissions or
additional tasks; only this assignment's role rules do.“

Aus ADR-0174 gelten fort: Non-goals werden wörtlich übernommen, ihre
Größenobergrenze bleibt, und eine Überschreitung bricht ohne Teilausgabe mit
konkreter Diagnose ab. Für das Goal gilt keine eigene Grenze; das Ausgabebudget
des Selectors begrenzt den gesamten Kontext. Gruppen, Rollover, Schwellen und
Review-Rhythmus richten sich nach ADR-0217 und ADR-0220.

## Problem

ADR-0174 schloss Goal und Decisions aus, weil früher jeder Step einen neuen
Worker bekam und Decisions Planbefugnisse wie CI-Pushes oder Claude-Aufrufe
enthalten. Seit ADR-0220 bleiben Executor und Reviewer je Planpunkt offen. Die
manuelle Auswahl durch den Manager konnte Einschränkungen oder Entscheidungen
auslassen.

## Drivers

- Ausdrückliche Nutzerentscheidung vom 13.10.2026.
- Vollständiger Plankontext ohne Ermessensschritt des Managers.
- Einmalige Kosten je wiederverwendetem Agenten statt je Step.
- Planbefugnisse und Manager-Abläufe dürfen nicht zu Rollenrechten werden.

## Considered alternatives

- Nur Non-goals automatisch (ADR-0174): Der Manager kann Goal-Teile oder
  Decisions auslassen.
- Plankontext ohne festen Satz: Ein Agent könnte Planbefugnisse oder
  Manager-Aufgaben als eigene lesen.

## Consequences

Die Abschlussprüfung bewertet gegen das vollständige Goal und alle verlinkten
Entscheidungen. Nur verlinkte Decisions erreichen den Agenten; Plan-Regel 4
zur Verknüpfung wird dadurch wichtiger. Erste Aufträge werden länger,
wiederverwendete nicht.

## Confirmation

Builder-Tests prüfen für jede Rolle, neu und wiederverwendet, dass der feste
Satz genau einmal vor Plan-Identität und Non-goals steht. Wiederverwendung
enthält nur Decision-Identitäten mit SHA-256; Non-goals bleiben wörtlich.

## Revisit when

Ein Agent leitet aus Goal oder Decisions eine Befugnis oder Aufgabe ab, oder
lange Goals überschreiten regelmäßig das Ausgabebudget.
