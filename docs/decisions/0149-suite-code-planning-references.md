---
format_version: 1
id: ADR-0149
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/skill-ownership
---

# Code nutzt Plan- und Handoff-Regeln im Suite-Layout

## Decision

Code verweist im Suite-Layout nur für bereits anwendbare gemeinsame Belange auf eng begrenzte Plan-/Handoff-Referenzen. Handoff bleibt ausdrücklich aktivierungspflichtig. Standalone bleibt eigenständig. Übernahme nur mit erhaltener Semantik und begründeten Routenkosten. Scheitern die zugehörigen Cases in W-014, wird der Verweis zurückgenommen.

## Problem

Mehrfache Planungs- und Übergabetexte können auseinanderlaufen; Verweise können aber Aktivierung oder Kontextkosten verändern.

## Drivers

Harte Suite-Kopplung; keine neue implizite Handoff-Aktivierung; vollständige eigenständige Standalone-Ausgabe.

## Considered alternatives

Getrennte Texte behalten: höhere Pflegekosten, aber unveränderte Ladewege. Vollständige Geschwistertexte laden: unnötige Tokens und zu breite Aktivierung.

## Consequences

W-005 setzt die am 04.10.2026 freigegebenen Verweise um und misst die Routen statisch; nicht sicher vereinheitlichbare Stellen bleiben gemeldet getrennt.

## Confirmation

Gemeinsame Aktivierung, ausdrücklicher Transfer, kleine Aufgaben und Varianten mit/ohne Plan anhand derselben Cases prüfen.

## Revisit when

Ein Referenzweg mehr Kontext kostet oder eine Aktivierungsgrenze verletzt.

