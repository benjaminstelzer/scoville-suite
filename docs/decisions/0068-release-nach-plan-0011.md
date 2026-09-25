---
format_version: 1
id: ADR-0068
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: suite/release-ownership
superseded_by: ADR-0069
---

# Releasearbeit folgt als eigener Plan nach PLAN-0011

## Decision

PLAN-0012 besitzt die verbleibende Release-Migration und Veröffentlichung. Er wird erst nach erfolgreichem Abschluss von PLAN-0011 aktiviert und ersetzt die offenen Releasepunkte PLAN-0002/W-010 und W-011.

## Problem

Die alten Releasepunkte decken die später ergänzten Namens-, Migrations-, README-, Privat-Skill- und Assetanforderungen nicht vollständig ab und würden neben einem neuen Plan einen zweiten Besitzer schaffen.

## Drivers

- Der Nutzer verlangt einen neuen Plan aus dem vollständigen Release-Audit.
- PLAN-0011 soll vor dem neuen Plan erfolgreich beendet sein.
- Abgeschlossene Arbeit und Evidenz aus früheren Plänen bleiben erhalten.
- Der Release braucht einen einzigen aktuellen Besitzer.

## Considered alternatives

- PLAN-0002 weiter ausbauen: Bewahrt die alte Stufenstruktur, vermischt aber überholte Releaseannahmen mit dem erweiterten Auftrag.
- PLAN-0012 nach PLAN-0011 verwenden: Hält den finalen Releaseumfang zusammen und lässt frühere Implementierungshistorie unverändert.

## Consequences

- PLAN-0002/W-010 und W-011 werden als ersetzte offene Arbeit beendet.
- PLAN-0012 wiederholt keine durch Evidenz abgeschlossene Implementierung.
- Vor Aktivierung von PLAN-0012 muss PLAN-0011 erfolgreich abgeschlossen und der finale Quellenstand erneut geprüft sein.
- Diese Entscheidung veröffentlicht oder installiert noch nichts.

## Confirmation

1. Prüfe PLAN-0011 auf `completed` und vollständige Abschlussnachweise.
2. Prüfe PLAN-0002/W-010 und W-011 auf den Verweis zu dieser Entscheidung und ihren ersetzten Status.
3. Prüfe PLAN-0012 auf den vollständigen Releaseumfang und einen eindeutigen ersten Arbeitspunkt.

## Revisit when

Der Nutzer ändert die Reihenfolge oder nimmt einen Teil der Releasearbeit aus PLAN-0012 heraus.
