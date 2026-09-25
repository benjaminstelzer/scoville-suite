---
format_version: 1
id: ADR-0056
status: deprecated
created: 2026-09-25
accepted: 2026-09-25
scope: suite/setup
---

# Scoville Setup verwaltet vorhandene Konfiguration

## Decision

Scoville Setup wird ein kleiner bei Bedarf aufgerufener Skill zum Anzeigen, Prüfen und ausdrücklich beauftragten Speichern von Einstellungen. Er verwendet die Dateien und Ladeverträge aus ADR-0051. ASK und Workflow lesen ihre Einstellungen selbst und benötigen keinen vorherigen Setup-Aufruf.

## Problem

Persönliche Vorgaben und projektbezogene Einstellungen brauchen einen verständlichen gemeinsamen Bedienungsweg.

## Drivers

- Der Nutzer bestätigt einen eng begrenzten Konfigurations-Skill.
- Einrichtungstext soll normale ASK- und Workflowaufrufe nicht belasten.

## Considered alternatives

- Einrichtung in jedem ausführenden Skill erklären: wiederholte Anleitung und zusätzlicher Ladeumfang.
- Separater Setup-Skill: eine gezielt geladene Anleitung für die vorhandenen Konfigurationsdateien.

## Consequences

- Persönliche projektübergreifende Vorgaben bleiben im jeweiligen Skill-Ordner. Projektwerte stehen in .scoville/config.json der ausgewählten Projektwurzel.
- Ohne Projektdatei gelten persönliche Vorgaben vor mitgelieferten Defaults. Setup erklärt die wirksame Rangfolge und prüft Werte mit bestehenden Verbraucherverträgen.
- Nur ausdrücklich gewünschte dauerhafte Einstellungen werden gespeichert. Einmalige Overrides, bloßes Lesen und Workflowstarts erzeugen keine Projektdatei.
- Setup legt auf Auftrag nur benötigte Werte an oder ergänzt sie und erhält fremde Einstellungen. Keine weitere Konfigurationsdatei und keine eigene Ladelogik.
- Installation, Updates, Workflowausführung und laufende Überwachung gehören nicht zu Setup.

## Confirmation

1. Prüfe Anzeigen ohne vorhandene Projektdatei: wirksame Werte erklären und keine Datei erzeugen.
2. Prüfe beauftragte persönliche und projektbezogene Änderungen sowie ungültige Werte mit den bestehenden ASK-/Workflowverbrauchern.
3. Prüfe einmalige Overrides ohne Speicherung und normalen ASK-/Workflowstart ohne vorheriges Setup.

## Revisit when

Ein weiterer Skill tatsächlich Einstellungen benötigt, die die vorhandenen Konfigurationsverträge nicht abbilden.
