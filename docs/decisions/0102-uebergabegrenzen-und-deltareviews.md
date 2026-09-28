---
format_version: 1
id: ADR-0102
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: workflow/boundaries
---

# Übergabegrenzen und Deltareviews

## Decision

Der beauftragte Opus-5.5-Review ergänzt den Workflow: Nach übernommenem Worker-Handoff prüft der Koordinator seinen Kontext vor dem Nachfolgerstart und übergibt bei Bedarf zuerst sich selbst. Beim dritten Handoff desselben Steps oder derselben Gruppe teilt er nur die offenen Restpunkte in geordnete Steps desselben Work Items auf. Erledigte Teile und Evidence bleiben erhalten, Ziel und Acceptance unverändert.

Projektvorgaben zum Review-Rhythmus gehen vor. Sonst werden ungeprüfte Produktänderungen an der nächsten geprüften Grenze früher geprüft, wenn Folgearbeit darauf aufbaut, sie umfangreich testet oder ein im Work Item gefundener Produktfehler korrigiert wurde. Ein solcher Fix endet nach gezielten Checks vor der Fortsetzung eines größeren Test-Steps. Zwischenreviews prüfen das ungeprüfte Delta und betroffene Acceptance. Das Abschlussreview verwendet vorherige Bewertungen für unveränderte Teile. Diese Ergänzung präzisiert den Default aus ADR-0099; ADR-0101 bleibt gültig.

Fachfremde Nutzeraufträge dürfen beim einzigen aktiven Schreiber bleiben, werden aber in Plan und Commit getrennt ausgewiesen oder separat committed.

## Problem

Die bisherigen Regeln lassen lange Steps ohne Koordinator-Checkpoint oder Review weiterlaufen. Plan verbietet bislang auch die reine Aufteilung offener Arbeit gestarteter Steps.

## Drivers

- Externer Review und ausdrücklicher Umsetzungsauftrag vom 2026-09-28.
- Schlanker Ablauf ohne neue Zustandsdateien, Schwellen oder Bestätigungen.

## Considered alternatives

- Review nach jeder Gruppe: unnötiger Aufwand für reine Tests und Nachweise.
- Nur am Work-Item-Ende prüfen: spätes Feedback kann umfangreiche Folgetests entwerten.

## Consequences

Die bestehenden Übergaben tragen auch die für eine Step-Aufteilung nötigen Fakten. 40/60, Archivierung und Auto-Compaction bleiben unverändert. Laufende DIVI-Chats und Projektdateien bleiben unberührt. Beauftragt sind Tests und lokale Installation, keine Veröffentlichung.

## Confirmation

Workflow-, Suite-, Shared-, Plan-, Ask- und Setup-Tests sowie gezielte Offline-Modellfälle mit GPT-6 Luna High und GPT-6 SOL Medium. Gebaute Pakete vor lokaler Installation vergleichen.

## Revisit when

Aufteilungen verlieren Restarbeit oder Reviews wiederholen unveränderte geprüfte Teile.
