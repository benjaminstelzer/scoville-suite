---
format_version: 1
id: ADR-0227
status: accepted
created: 2026-10-29
accepted: 2026-10-29
scope: ask/validation
---

# Claude-Transportnachweis für PLAN-0060

## Decision

Binding sections: complete

Für die in PLAN-0060 geänderte Claude-Promptübergabe genügt der vorhandene aufzeichnende CLI-Platzhalter anstelle eines echten Claude-Modellaufrufs. Der Test ersetzt resolve_claude_command und prüft ab dieser Grenze den Aufruf sowie die unveränderte Übergabe von Prompt, Nutzerfrage und technischen Daten; PATH-Suche und Behandlung von .ps1 bleiben ungeprüft. Dies begrenzt ausschließlich den Consumer-Nachweis aus ADR-0153 für diesen Plan; dessen fachliche Schreib- und Rollenregeln bleiben erhalten. Die Nutzerentscheidung erlaubt keinen Claude-Modelllauf. Modelltests bleiben bei gpt-6.1-sol / low.

## Problem

Ein echter Claude-Empfängertest wäre mit dem vorgeschriebenen Sol-Testmodell nicht ausführbar.

## Drivers

- Ausdrückliche Nutzerentscheidung für den Transporttest.

## Considered alternatives

- Ausnahme für einen echten Claude-Empfängertest: nicht gewählt.

## Consequences

Der Transportnachweis ist keine Claude-Verhaltensabnahme. Testbericht, README und Abschluss nennen Claude-Verhalten ausdrücklich ungeprüft; ein Sol-Test ersetzt diesen fehlenden Nachweis nicht.

## Confirmation

Die erzeugte Claude-Helperausgabe durch den bestehenden Test in test_claude_recipe.py an den aufzeichnenden Platzhalter übergeben. Vollständigkeit, unveränderte Eingaben und Ergebniszuordnung prüfen; keinen externen Modellaufruf starten.

## Revisit when

Ein weiterer Plan einen Claude-Empfängernachweis benötigt oder der Nutzer einen echten Modelllauf gesondert freigibt. Die Ausnahme geht nicht automatisch auf weitere Pläne über.
