---
format_version: 1
id: ADR-0090
status: superseded
created: 2026-09-26
accepted: 2026-09-26
scope: workflow/coordinator-rollover
superseded_by: ADR-0092
---

# Nachfolger fordert Selbstarchivierung per Nachricht an

## Decision

Auf ausdrücklichen Nutzerwunsch übernimmt der Nachfolger ohne Warteabfrage und fordert den Vorgänger per Nachricht zur Selbstarchivierung auf. Der Vorgänger beendet alle Projektwrites vor create_thread; der Nachfolger trägt seine eigene ID ein. Der Vorgänger prüft den tatsächlichen Absender gegen den erzeugten Nachfolger und bestätigt erst nach erfolgreicher Selbstarchivierung. Keine Pollschleife oder weitere Orchestrierung.

## Problem

Die beobachtete Sofortabfrage des Nachfolgers blockierte Übernahme und Archivierung, während der Vorgänger noch seinen Handle sicherte. Der Nutzer wählte ausdrücklich Nachrichten statt waits.

## Drivers

- Schlanker Ablauf ohne unnötige Warteaufrufe und ohne konkurrierende Projektwrites.
- Vollständige Archivierung gehört zur Abnahme.

## Considered alternatives

- Ein begrenzter Warteaufruf: vom Nutzer durch die Nachrichtenroute ersetzt.

## Consequences

Der tatsächliche Nachfolger-Handle wird durch den Nachfolger im bestehenden Laufdatensatz gesichert. Bei unklarer Erstellung bleibt eine gezielte Wiederaufnahme nötig; keine blinde Neuerstellung. Fehlende Archivierungsbestätigung bleibt offen.

## Confirmation

Ein realer Rollover mit SOL 6 Medium zeigt Übernahme ohne wait_threads, eine Selbstarchivierung des richtigen Vorgängers und deren bestätigten Empfang. Nur der finale Coordinator bleibt sichtbar.

## Revisit when

Der Host erlaubt nach Selbstarchivierung keine Bestätigung oder die native Nachrichtenzustellung scheitert.
