---
format_version: 1
id: ADR-0036
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: workflow/role-result-protocol
---

# Zeilenprotokoll für Rollenresultate

## Decision

Executor, Reviewer und Repair schreiben kein Ergebnis-JSON mehr. Sie liefern `SCOVILLE_RESULT_V1` mit bekannten Feldern in fester Reihenfolge. Ein paketierter Helper validiert das Protokoll fail-closed und stellt dem Coordinator die gleiche semantische Struktur wie bisher bereit.

## Problem

Die manuelle JSON-Erzeugung macht einfache Rollenresultate unnötig fehleranfällig. Ein vorheriger Modellpilot konnte das einfache Zeilenformat in allen 24 Läufen auswertbar erzeugen, während das JSON-basierte Evaluatorformat nur in 4 von 24 Läufen syntaktisch gültig war.

## Drivers

- Modelle sollen kurze, klare Ergebnisregeln befolgen können, ohne JSON-Syntax zu erzeugen.
- Rollen-, Status-, Längen- und Finding-Grenzen müssen maschinell und fail-closed erhalten bleiben.
- Exakte Delivery-Bytes, Identität und Compaction-Recovery dürfen sich nicht lockern.
- Coordinator-interne strukturierte Daten dürfen weiterhin JSON verwenden, wenn sie vom Helper erzeugt werden.

## Considered alternatives

- Ergebnis-JSON beibehalten: erhält den bisherigen Transport, aber auch die beobachtete Syntaxfehlerquelle.
- Freie Prosa tolerant reparieren: wäre einfacher für Modelle, würde jedoch unbekannte oder unvollständige Resultate erraten.
- Festes Zeilenprotokoll streng parsen: entfernt manuelle JSON-Syntax und bewahrt die maschinellen Grenzen.

## Consequences

- Die erste Zeile lautet exakt `SCOVILLE_RESULT_V1`; danach folgen bekannte einzeilige Felder in rollenabhängig fester Reihenfolge.
- `finding=` darf höchstens achtmal vorkommen. Summary, Finding und gesamte Prosa behalten feste Zeichenlimits.
- Unbekannte, doppelte, fehlende, ungeordnete oder rollenwidrige Felder werden abgelehnt und nicht repariert.
- Der Helper wird Bestandteil jedes Workflow-Pakets und ist der kanonische Besitzer der Ergebnisvalidierung.
- Vorhandene Delivery-, Recovery-, Review-, Repair- und Archivierungsverträge bleiben erhalten.

## Confirmation

1. Parser- und Rollenfehlerfälle bestehen als direkte Helpertests.
2. Delivery- und Compactiontests belegen den bytegenauen Transport und die Wiederherstellung des unveränderten Zeilenresultats.
3. Ein frischer Build besteht die bestehenden Workflow-, Suite-, Paket- und Exportprüfungen.
4. Astra Medium prüft den gebauten Kandidaten gegen Skillwriter, Workflowintention und die erhaltenen Protokollgrenzen.

## Revisit when

Ein Host ein natives typisiertes Rollenresultat bereitstellt oder reale Läufe zeigen, dass das feste Zeilenprotokoll die erforderliche Semantik nicht zuverlässig transportiert.
