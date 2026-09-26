---
format_version: 1
id: ADR-0092
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: workflow/coordinator-rollover
supersedes: ADR-0090
---

# Archivierung ohne Nachprüfung

## Decision

Die nachrichtenbasierte Selbstarchivierung bleibt. Der Nachfolger übernimmt und fordert den Vorgänger zur Selbstarchivierung auf. Dieser prüft den Absender gegen seinen erzeugten Nachfolger und ruft set_thread_archived einmal für die eigene ID als letzte Aktion auf. Alle Vorgänger-Projektwrites enden vor create_thread. Der Nachfolger sichert seine eigene ID.

Auf ausdrückliche Nutzerkorrektur entfällt die Überprüfung der Archivierung. Workflow und Ask verlangen keine nachgelagerte Bestätigung, Statusabfrage, externe Wiederholung oder Abschlusskontrolle. Bestehende Archivierungsrechte und Voraussetzungen bleiben erhalten.

## Problem

Selbstarchivierung unterbricht auf dem getesteten Host den eigenen Turn. Eine anschließende Bestätigung erzeugt eine unnötige Abhängigkeit.

## Drivers

- Schlanker Ablauf ohne waits und zusätzliche Kontrollaufrufe.
- Archivierung weiterhin ausführen; finalen Coordinator sichtbar lassen.

## Considered alternatives

- Externe Abschlussbestätigung: möglich, vom Nutzer als unnötig verworfen.

## Consequences

Fehlende Archivierungsbestätigungen blockieren die Abnahme nicht. Ein ausdrücklich zurückgegebener Toolfehler wird benannt. Historische Nachweise bleiben erhalten, sind aber keine Pflicht für neue Läufe.

## Confirmation

Der reale SOL-6-Medium-Lauf führt Übernahme und Archivierungsaufruf ohne nachgelagerte Prüfungen aus. Es wird kein Archivierungszustand nachgeprüft.

## Revisit when

Der Nutzer verlangt eine gesonderte Archivierungskontrolle.
