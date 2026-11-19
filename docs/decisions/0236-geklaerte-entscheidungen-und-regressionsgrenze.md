---
format_version: 1
id: ADR-0236
status: accepted
created: 2026-11-14
accepted: 2026-11-14
scope: suite/skills
---

# Geklärte Entscheidungen ausführen und Verschlechterungen vor der Auslieferung beheben

## Decision

Der Eigentümer hat am 2026-11-14 die nach dem unabhängigen Review zusammengefassten Änderungen beauftragt:

- Code und die gemeinsamen Review-Regeln nutzen Auftrag, Projektregeln, akzeptierte Entscheidungen und Konventionen, bevor sie eine wesentliche Frage stellen. Gewöhnliche Implementierungsentscheidungen innerhalb dieser Grenzen trifft der Agent selbst.
- Ein ausdrücklich verlangter Vertragswechsel ist die Erlaubnis für genau diesen Wechsel. Unabhängige Garantien und gesonderte Aktionsfreigaben bleiben erhalten. Ein bekannter Schutzverstoß ist nicht dadurch behoben, dass der Agent ihn im Bericht nennt; er korrigiert ihn im erlaubten Umfang oder lässt die betroffene Arbeit offen.
- Handoff überträgt die Erlaubnis, begonnene Nutzerarbeit wie beauftragt zu korrigieren oder zu ersetzen. Unbeteiligte uncommittete Arbeit bleibt erhalten. Das Erstellen der Übergabe ändert weiterhin keine Aufgaben-Datei.
- ADR-0231 bleibt unverändert: sinnvolle Tests für neues Verhalten, Fail-first nur in den dort genannten Fällen und vorhandene Tests vor und nach einem Refactoring.
- Bei Änderungen zur Verbesserung des Modellverhaltens vergleicht die Freigabe den genauen Kandidaten mit dem Stand ohne Skill und dem bisher ausgelieferten Stand, je Zielmodell und Aufgabenart. Bestätigte schwere oder reproduzierbare Verschlechterungen blockieren den betroffenen Kandidaten bis zur Korrektur oder Rücknahme; Gewinne anderswo gleichen sie nicht aus. Ausführungsfehler, ungültige Bewertungen und nicht geladene Skills belegen keine Modellwirkung. Unabhängige Abnahmeaufgaben ergänzen die bekannten Entwicklungsfälle.

## Problem

Vorhandene Messungen zeigen sowohl unnötige Rückfragen als auch mangelhafte Ergebnisse trotz erfolgreicher automatischer Bewertung. Überbreite Entscheidungsregeln und Durchschnittswerte können diese Unterschiede verdecken.

## Drivers

- Aufgaben vollständig im bereits erlaubten Umfang erledigen.
- Schutzanforderungen erhalten und normale Implementierungsentscheidungen nicht zu Freigabefragen machen.
- Tatsächliche Ergebnisse statt bloßer Regelbefolgung beurteilen.

## Considered alternatives

- Alle Rückfragen abschaffen: würde wirklich offene Entscheidungen und Freigaben übergehen.
- Nur den Mittelwert vergleichen: würde einzelne schwere Verschlechterungen ausgleichen.
- Für jede Skill-Ausführung neue Listen und Prüfphasen verlangen: würde zusätzlichen Aufwand ohne nachgewiesenen Nutzen erzeugen.

## Consequences

Diese Regeln versprechen keine Nichtverschlechterung für jede künftige Aufgabe. Quellprüfung und technische Tests belegen die Umsetzung, keine verbesserte Modellwirkung. Die Änderung erteilt keine Freigabe für Modellaufrufe, Push, Veröffentlichung oder Installation. Freigabeprüfungen gehören zur Entwicklung und Auslieferung der Skills, nicht als zusätzliche Phase in jede ihrer späteren Aufgaben.

## Confirmation

Code, der gemeinsame Code-Qualitätstext und die Handoff-Vorlage stimmen über bereits erteilte Autorität und offene Entscheidungen überein. Die Testgrenze aus ADR-0231 bleibt erhalten. Die gebauten Pakete enthalten die kanonischen Änderungen und bestehen die passenden technischen Prüfungen. Eine Wirkungsabnahme nutzt gültige vergleichbare Läufe mit gpt-6.1-sol und Claude Opus 5.5, beide medium, einschließlich unabhängiger Aufgaben; bekannte Schäden und unklare Unterschiede bleiben einzeln sichtbar.

## Revisit when

Ein Agent fragt eine bereits entschiedene Frage erneut, behandelt einen gemeldeten Schutzverstoß als erledigt, friert begonnene Nutzerarbeit ein oder die Auswertung verdeckt eine Verschlechterung.
