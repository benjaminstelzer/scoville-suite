---
format_version: 1
id: ADR-0010
status: accepted
created: 2026-09-22
accepted: 2026-09-22
scope: suite/evaluation
---

# WordPress-Fünfertest ergänzt das Release-Gate

## Decision

Die ausdrücklich beauftragten fünf WordPress-Fälle ergänzen ADR-0008 für das neue Mitglied. SOL Medium koordiniert Luna Medium. Bestehende Ergebnisse gelten nur für unveränderte geprüfte Eingaben und Laufzeitdateien.

## Problem

ADR-0008 entstand vor der Aufnahme des WordPress-Skills und enthält dessen separat beauftragte Fälle noch nicht.

## Drivers

- Der Nutzer verlangt fünf verschiedene Aufgaben unter SOL mit Luna als Ausführer.
- Mindestens ein Fall prüft korrektes Spacing.
- Der spätere vollständige Release umfasst dieses Mitglied.

## Considered alternatives

- Separater Fünfersatz: erhält den ausdrücklich beauftragten Umfang und die eingefrorenen Soll-Ergebnisse.
- Aufnahme in bestehende UI-Fälle: würde den verlangten eigenständigen WordPress-Test nicht abbilden.

## Consequences

- `development/luna-tests/wordpress-cases.md` mit IDs 01 bis 05 und `wordpress-expected.md` ergänzen die 64 ausgewählten Fälle.
- `wordpress-sol-results.md` bleibt tatsächliche historische Evidenz, keine pauschale Freigabe späterer Änderungen.
- Unveränderte Laufzeitdateien erfordern keine Wiederholung allein wegen äußerer README-Änderungen. Deren Fakten und Paketbestand werden statisch geprüft.

## Confirmation

1. Prüfe Paket- und Eingabehashes gegen den eingefrorenen WordPress-Lauf.
2. Bestätige fünf semantische Ergebnisse sowie Modell und Effort aus den Belegen.
3. Prüfe den finalen Buildbestand und neue README-Texte vor Veröffentlichung.

## Revisit when

WordPress-Laufzeitdateien, Fallvorgaben oder Modelltransport ändern sich.
