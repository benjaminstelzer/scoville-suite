---
format_version: 1
id: ADR-0116
status: proposed
created: 2026-09-29
scope: workflow/deployment
---

# Auslieferung als begrenzter Worker-Auftrag

## Decision

Empfehlung: Ein Worker übernimmt vorbereitete, autorisierte Auslieferungen
einschließlich ihrer nötigen Checks. Der Manager bestimmt Umfang und Freigaben,
bewertet Ergebnisse und pflegt Plan und autorisierte Commits. Migrationen
gehören nur bei vorhandener konkreter Autorisierung zum Auslieferungsauftrag.

## Problem

Bei W-315 bereitete Worker 14 Pakete vor, während Manager 5 wesentliche Upload-
und Migrationsarbeit ausführte. Das war autorisiert, ließ aber die Grenze
zwischen Koordination und operativer Arbeit unklar.

## Drivers

- Ein eindeutig zuständiger Schreiber und ein kleiner Koordinatorkontext.
- Auslieferungsfehler müssen mit tatsächlich abgeschlossenen Effekten übergeben werden.

## Considered alternatives

- Manager liefert aus: weniger Übergabe, aber zusätzliche operative Arbeit und
  Fehlerdiagnose im Koordinator; Produktkorrekturen benötigen weiterhin Worker.
- Worker liefert aus: ein weiterer begrenzter Auftrag, dafür eindeutige
  Ausführungsverantwortung und derselbe Wiederaufnahmeweg wie andere Arbeit.

## Consequences

Der Auftrag enthält Ziel, geprüfte Pakete, Freigabegrenzen und entscheidende
Checks. Ein partieller Fehler führt zu einem faktischen Ergebnis mit offenen
Schritten, nicht zu blindem Wiederholen. Produktkorrekturen folgen dem
bestehenden Review-Rhythmus. Auslieferung ersetzt keine funktionale Abnahme.
Diese Vorlage ändert noch keine Rollenregel und verlangt kein neues Tracking.

## Confirmation

Nach Annahme einen normalen Upload und einen partiellen Fehler als begrenzte
Fälle prüfen: keine zweite Schreibinstanz, kein doppelter Upload bereits
abgeschlossener Teile, keine Migration außerhalb des Auftrags.

## Revisit when

Eine Auslieferung benötigt zwingend eine nur im Manager verfügbare Fähigkeit.
