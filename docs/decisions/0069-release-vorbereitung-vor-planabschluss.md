---
format_version: 1
id: ADR-0069
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/release-ownership
supersedes: ADR-0068
---

# Release lokal vorbereiten und Veröffentlichung gesperrt halten

## Decision

PLAN-0012 wird zur lokalen Vorbereitung aktiviert. PLAN-0011 wird als draft zurückgestellt; seine pausierten W-001 und W-002 sowie ihre Nachweise bleiben erhalten. Veröffentlichung setzt weiterhin dessen vollständige Abnahme und die Releasegates voraus. PLAN-0012 bleibt alleiniger Besitzer der durch ADR-0068 ersetzten Releasearbeit aus PLAN-0002/W-010 und W-011.

## Problem

Externe Blockaden von PLAN-0011 verhindern bisher auch unabhängige lokale Releasevorbereitung.

## Drivers

- Der Nutzer bestätigt den vorgezogenen Beginn von PLAN-0012.
- Offene Host-Policy und Plattform-CI werden nicht als erledigt ausgegeben.

## Considered alternatives

- Vollständig warten: Bewahrt die alte Reihenfolge und blockiert unabhängige Vorbereitung.
- Lokal vorbereiten: Ermöglicht Fortschritt bei unveränderter Veröffentlichungssperre.

## Consequences

- W-001 inventarisiert den aktuellen Entwicklungsstand samt offenen Abnahmen.
- Quellen bleiben bis W-008 veränderlich; betroffene Nachweise müssen zum finalen Stand passen.
- Diese Reihenfolge autorisiert weder eine Umgehung der Host-Policy noch vorzeitige GitHub-Veröffentlichung.

## Confirmation

1. Prüfe aktive Auswahl PLAN-0012/W-001 und unverändert pausierte PLAN-0011/W-001 und W-002.
2. Prüfe den Erhalt aller bisherigen Nachweise.
3. Prüfe vor W-009 den Abschluss von PLAN-0011 und sämtliche Releasegates.

## Revisit when

Der Nutzer ändert die Veröffentlichungsvoraussetzungen oder die offenen Abnahmen sind erfüllt.
