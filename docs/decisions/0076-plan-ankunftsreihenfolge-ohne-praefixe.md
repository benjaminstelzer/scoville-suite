---
format_version: 1
id: ADR-0076
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/plan-order
---

# Neue Aufgaben ohne Warteschlangenpräfixe anhängen

## Decision

Neue Aufgaben werden in Ankunftsreihenfolge angehängt. Nur ausdrückliche Priorität erlaubt eine andere gültige Position. Keine neuen Deferred/Prioritized-Titelpräfixe schreiben. Historische Prioritäten und Rückkehranweisungen bleiben auch nach Wiederaufnahme verbindlich.

## Problem

Die bisherige Präfix-Warteschlange ergänzt eigene Erzeugungsregeln.

## Drivers

- Abhängigkeiten und gestartete Historie bleiben erhalten.
- Der Nutzer beauftragt diese Richtung in PLAN-0013 und bestätigt dessen Aktivierung.

## Considered alternatives

- Präfixe fortführen: Sichtbare Herkunft mit zusätzlicher Schreibmechanik.
- Authored order nutzen: Einfachere neue Records; historische Präfixe müssen weiterhin gelesen werden.

## Consequences

Unmittelbare Umleitung und ausdrücklich gewünschte Rückkehr stehen in Next action.

## Confirmation

Prüfe zwei neue Aufgaben sowie explizite und historische Priorität mit Wiederaufnahme an tatsächlichen Edits.

## Revisit when

Die Dokumentreihenfolge kann eine benötigte neue Priorität nicht eindeutig darstellen.
