---
format_version: 1
id: ADR-0234
status: accepted
created: 2026-11-14
accepted: 2026-11-14
scope: suite/workflow
---

# Workflow: Step-Review gilt als Abschluss bei einem einzigen Step

## Decision

Binding sections: complete

Hat ein Work Item genau einen Step und hat dessen bestandenes Step-Review die gesamte Acceptance des Work Items geprüft, gilt dieses Review als Abschluss-Review. Ein weiterer Reviewer-Lauf entfällt.

Work Items mit mehreren Steps behalten ihr eigenes Abschluss-Review durch einen frischen Reviewer. Dasselbe gilt für ein Work Item mit einem Step, dessen Step-Review nicht die gesamte Acceptance abgedeckt hat.

## Problem

Scoville Workflow verlangte für jedes Work Item nach den Step-Reviews ein eigenes Abschluss-Review. Bei einem einzigen Step sehen beide Reviews denselben Diff und dieselbe Acceptance am unveränderten Stand. Ein Review mit Opus 5.5 am 2026-11-13 meldete das als Lauf, der nur um des Ablaufs willen geschieht.

## Drivers

- Der Eigentümer will keine Prüfschritte ohne eigenen Erkenntniswert.
- Das Abschluss-Review soll finden, was zwischen mehreren Steps verloren ging; bei einem Step gibt es das nicht.

## Considered alternatives

- Abschluss-Review für jedes Work Item: ein zweiter unabhängiger Blick, zum Preis eines weiteren Laufs über denselben Stand.

## Consequences

Bei Work Items mit einem Step entfällt der zweite unabhängige Blick. Ein Mangel, den das Step-Review übersieht, wird dort nicht mehr von einem zweiten Reviewer gefunden.

## Confirmation

SKILL.md und operations.md von Scoville Workflow nennen die Regel. Die Gesamtprüfung der Suite besteht.

## Revisit when

Work Items mit einem Step werden mit Mängeln abgeschlossen, die ein zweites Review gefunden hätte, oder der Nutzer will die Grenze verschieben.
