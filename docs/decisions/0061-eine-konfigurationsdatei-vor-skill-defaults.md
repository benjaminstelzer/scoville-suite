---
format_version: 1
id: ADR-0061
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/project-configuration
supersedes: ADR-0051
---

# Eine Konfigurationsdatei überschreibt Skill-Defaults

## Decision

.scoville/config.json überschreibt die importierten mitgelieferten Skill-Defaults. Fehlende Werte verwenden den jeweiligen Default. Eine zusätzliche persönliche Konfigurationsebene entfällt. Der nur in der Suite enthaltene Setup-Skill zeigt und bearbeitet ausschließlich diese Datei auf ausdrücklichen Auftrag.

## Problem

Die Unterscheidung persönlicher und projektbezogener Konfiguration erzeugt vom Nutzer ausdrücklich abgelehnte Komplexität.

## Drivers

- Genau eine bearbeitbare Konfigurationsdatei vor den Skill-Defaults.
- Defaults werden wie Modellvorgaben importiert statt in Anleitungen dupliziert.

## Considered alternatives

- Persönliche und projektbezogene Dateien: zusätzliche Rangfolge und Zielwahl.
- Eine Datei vor Defaults: gewählte einfache Auflösung.

## Consequences

- Die bisherige persönliche Ebene aus ADR-0046 und die mehrstufige Setup-Bedienung aus ADR-0056 werden aufgegeben. Keine neuen workflow.local.toml-Dateien.
- Ask und Workflow behalten ihre vorhandenen Einstellungsstrukturen unter ask und workflow. Ein gemeinsamer Loader liest nur die gewählte Projektwurzel; keine Elternsuche oder Überwachung.
- Explizite Aufruf-/Step-Parameter bleiben einmalige Auftragsvorgaben und werden nicht gespeichert. Setup bietet keine weiteren Konfigurationsebenen an.
- Ohne Datei gelten Defaults. Lesen und Start erzeugen keine Datei. Ungültige Werte werden gemeldet. Setup erhält nicht betroffene Werte.
- Bestehende persönliche Dateien nicht löschen: vorhandene Abweichungen beim Übergang anzeigen und gezielt übernehmen; danach keine versteckte weitere Ladeebene.
- Claude-Timeout hat den importierten Default 3600 Sekunden und ist über Setup überschreibbar. Keine Hashes oder Konfigurations-Snapshots. Einstellungen zwischen Läufen ändern.
- Setup startet keine Workflows und übernimmt keine Installation, Updates oder laufende Überwachung. Ask und Workflow benötigen keinen vorherigen Setup-Aufruf.

## Confirmation

1. Prüfe fehlende Datei, partielle Overrides und ungültige Werte über die tatsächlichen Verbraucher.
2. Prüfe Setup-Änderung und unveränderte fremde Werte sowie Lesen ohne Dateierzeugung.
3. Prüfe erhaltene Altdateien ohne weitere Ladeebene und einmalige Aufrufparameter ohne Speicherung.

## Revisit when

Der Nutzer ausdrücklich wieder mehrere Konfigurationsebenen benötigt.
