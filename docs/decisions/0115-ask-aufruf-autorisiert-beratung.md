---
format_version: 1
id: ADR-0115
status: accepted
created: 2026-09-29
accepted: 2026-09-29
scope: ask/authorization
---

# Ask-Aufruf umfasst Chats und auftragsbezogene Kommunikation

## Decision

Ausdrückliche Nutzerentscheidung vom 29.09.2026: Wer Scoville Ask aufruft, autorisiert die zur angeforderten Beratung benötigten Berater-Chats sowie die Kommunikation zwischen aufrufendem Chat und diesen Beratern. Dafür wird keine separate Bestätigung verlangt. Dies umfasst Auftrag, notwendige Rückfragen, Antworten, Ergebniszustellung und gezielte Wiederherstellung fehlgeschlagener Zustellung innerhalb derselben Beratung.

## Problem

Beim Review von PLAN-0020 wurde trotz beauftragter Beratung und bestätigtem Berater-Chat die Rückmeldung mangels separat formulierter Nachrichtenfreigabe zurückgehalten.

## Drivers

- Der Nutzer verlangt einen vollständigen Ask-Ablauf ohne zusätzliche Chat- oder Nachrichtenfreigaben.

## Considered alternatives

- Separate Zustimmung für Erstellung und Rückmeldung: zerlegt den beauftragten Ablauf in unnötige Freigabeschritte.

## Consequences

Ask dokumentiert seinen Aufruf als vollständigen Beratungsauftrag und trägt den tatsächlichen Nutzerauftrag samt verifizierter Rückadresse in die Berater-Anweisung. Die native Route aus ADR-0085 bleibt erhalten. Bloße Erwähnungen aktivieren Ask nicht. Nutzerbeschränkungen und konkrete höherrangige Host-Sperren bleiben verbindlich; der Skill kann keine Berechtigung gegen sie erteilen. Andere Empfänger, zusätzliche Beratungen, Produktänderungen und automatische Archivierung sind nicht mitautorisiert.

## Confirmation

Ein gezielter nativer Aufruf erstellt den angeforderten Berater und liefert dessen Ergebnis an den aufrufenden Chat ohne zweite Freigabe. Gegenfälle prüfen Nichtaufruf, ausdrückliche Einschränkung und eine technische Zustellstörung. Diese Prüfungen stehen noch aus.

## Revisit when

Der Aufrufumfang ist uneindeutig oder der Host verlangt eine darüber hinausgehende konkrete Autorisierung.
