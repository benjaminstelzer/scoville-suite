---
format_version: 1
id: ADR-0230
status: accepted
created: 2026-11-13
accepted: 2026-11-13
scope: suite/ui
---

# UI rendert nur bei verlangter Prüfung und bei ungeklärtem visuellem Mangel

## Decision

Binding sections: complete

Scoville UI wendet beim Umsetzen einer Änderung die Regeln im Code an. Das bloße Umsetzen löst kein Rendern, Nachmessen oder Bedienen der laufenden Oberfläche aus; was nicht gerendert oder bedient wurde, steht im Bericht als ungeprüft.

Gerendert, gemessen und bedient wird in genau zwei Fällen:

1. Der Nutzer verlangt ein Review, ein Audit, einen gerenderten Check oder einen Nachweis.
2. Ein gemeldeter visueller Mangel lässt sich aus dem Quelltext nicht erklären. Dann darf der Agent rendern, um die Ursache zu finden. Erklärt der Quelltext den Mangel, wird er dort behoben, ohne zu rendern.

Die Ausnahme in Punkt 2 bleibt bestehen. Sie betrifft die Diagnose eines gemeldeten Mangels und macht Rendern nicht zum Bestandteil jeder Änderung. Eine Regel, eine Referenz oder ein Helfer von Scoville UI darf Rendern, Messen oder Bedienen nicht darüber hinaus zur Voraussetzung des Umsetzens machen.

## Problem

Ein unabhängiger Review zu PLAN-0066 sah in der Ausnahme für ungeklärte visuelle Mängel einen möglichen Konflikt mit der Vorgabe, beim Umsetzen nicht zu rendern. Die übrigen Render- und Messauslöser beim Umsetzen wurden entfernt; für diese Ausnahme war eine Entscheidung des Nutzers nötig.

## Drivers

- Frühere Fassungen ließen Modelle jede Änderung rendern und nachmessen, mit zwei- bis dreifacher Laufzeit und entsprechenden Kosten.
- Ohne die Ausnahme könnte der Agent bei einem Mangel, den der Quelltext nicht erklärt, nur melden, dass er ohne Rendern nicht zu klären ist.

## Considered alternatives

- Ausnahme streichen: verhindert jedes Rendern außerhalb einer verlangten Prüfung, lässt aber gemeldete Mängel ohne erkennbare Ursache im Quelltext ungeklärt.

## Consequences

Die Layoutqualität einer umgesetzten Änderung ist ohne verlangte Prüfung nicht gerendert belegt. Ein Fixauftrag kann Rendern auslösen, wenn der Quelltext den gemeldeten Mangel nicht erklärt. Bei der Messung der Skill-Wirkung zählt ein Anstieg der Browserstarts beim bloßen Umsetzen als Rückschritt.

## Confirmation

In den Anweisungen von Scoville UI prüfen, dass kein Leseweg des Umsetzens Rendern, Messen oder Bedienen verlangt und dass die Zeile zu Validation in der SKILL.md beide Fälle nennt. In Modellläufen der Umsetzungsaufgaben die Browserstarts zählen.

## Revisit when

Der Nutzer will Rendern beim Umsetzen ausweiten oder die Ausnahme für ungeklärte Mängel streichen, oder Modellläufe zeigen, dass die Ausnahme regelmäßig zum Rendern gewöhnlicher Änderungen führt.
