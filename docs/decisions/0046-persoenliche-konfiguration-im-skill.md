---
format_version: 1
id: ADR-0046
status: deprecated
created: 2026-09-25
accepted: 2026-09-25
scope: suite/personal-configuration
---

# Persönliche Konfiguration im Skill behalten

## Decision

Der Nutzer legt den jeweiligen Skill-Ordner als Ort persönlicher Konfiguration fest. Mitgelieferte Defaults und persönliche Dateien bleiben getrennt. Updates erhalten persönliche Einstellungen. Modelle werden zwischen Läufen geändert; für Änderungen während eines laufenden Auftrags wird ausdrücklich keine zusätzliche Snapshot-, Hash- oder Eskalationsbindung eingeführt.

## Problem

Workflow-Defaults werden in der Installation bearbeitet; ein Update kann diese Wahl ersetzen. Das Review schlägt dafür unnötig komplexe Absicherung laufender Modellwechsel vor.

## Drivers

- Einstellungen sollen direkt im Skill auffindbar sein.
- Komplexitätsersparnis hat beim theoretischen Konfigurationswechsel während eines Laufs Vorrang.

## Considered alternatives

- Datei außerhalb des Skills: vom Nutzer ausgeschlossen.
- Defaults direkt bearbeiten: persönliche Werte sind updategefährdet.
- Getrennte persönliche Datei im Skill: gewählter Ort; Updateprozess muss sie ausdrücklich bewahren.

## Consequences

- ASK behält config.json. Workflow kann assets/workflow.local.toml verwenden; erhaltene Plan-Profile analog assets/prompting.local.toml.
- Rangfolge bleibt explizite Anfrage/Step vor Projekt vor persönlicher Datei vor Defaults.
- Updates dürfen persönliche Dateien weder überschreiben noch als veraltete Paketdateien entfernen.
- Die Bedienregel benennt das Ende eines laufenden Auftrags als sicheren Änderungszeitpunkt. Vorhandene klare Fehler bei trotzdem inkompatiblem Zustand reichen aus.

## Confirmation

1. Prüfe Rangfolge, ungültige Werte und Modellwechsel zwischen Läufen.
2. Simuliere ein Update über den tatsächlichen Installations-/Synchronisationsweg und belege unveränderte persönliche Dateien.
3. Stelle sicher, dass keine neue Laufzeitbindung für Konfigurationsänderungen eingeführt wird.

## Revisit when

Ein praktischer Bedarf an Konfigurationswechseln innerhalb eines laufenden Auftrags entsteht.
