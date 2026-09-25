---
format_version: 1
id: ADR-0041
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/ui-validation
---

# WordPress-Backend-Grenze und delegierte Prüfung

## Decision

Der WordPress-Adapter greift nur bei Entwicklung oder Prüfung einer plugin-eigenen Backend-UI in `wp-admin`. Der Nutzer beauftragt WordPress-Testinstallationen unter `C:/xampp_lite_8_5/www` sowie die Tests durch SOL-6-High-Subagenten. Vor Teststart muss eine neue sichtbare Astra-High-Aufgabe den Skill abnehmen.

## Problem

Der zusammengeführte Skill braucht einen eindeutigen Adapterauslöser und eine verbindliche Reihenfolge für Review und praktische Prüfung.

## Drivers

- Pluginentwicklung allein aktiviert keine WordPress-UI-Regeln.
- Installation und Tests werden nicht vom Hauptagenten durchgeführt.

## Considered alternatives

- Adapter für jede WordPress-Aufgabe: würde Frontendgestaltung und reine Pluginlogik unzutreffend dem Backendvertrag unterstellen.
- Tests vor der Abnahme: widerspricht der ausdrücklich beauftragten Reihenfolge.

## Consequences

- Themes, Sitefrontends und Frontendausgaben von Plugins verwenden die allgemeine UI-Route. Reine Backendlogik gehört nicht zum UI-Skill.
- Die Astra-Abnahme bewertet Instruktionen und Paketinhalt. Sie ersetzt keine Runtime-Evidenz.
- Der aktuelle Vergleich verwendet SOL 6 High. Historisch vorgesehene Medium-Läufe gelten nicht als durchgeführt.
- Der Testinstallationsauftrag betrifft WordPress. Eine Installation des Skills oder Veröffentlichung bleibt außerhalb des Auftrags.

## Confirmation

1. Prüfe die Abgrenzung in `members/scoville-ui/scoville-ui/SKILL.md` und `references/wordpress/adapter.md` sowie den gebauten Paketen.
2. Sichere die Astra-Freigabe für die finalen Bytes vor Beginn der SOL-Prüfungen.
3. Dokumentiere Modell, Paketidentität und tatsächlich ausgeführte Prüfungen in `development/ui-evaluation.md` und dem Ergebnisbericht.

## Revisit when

Der Nutzer erweitert die unterstützten WordPress-Oberflächen oder ändert Prüfer und Reihenfolge ausdrücklich.
