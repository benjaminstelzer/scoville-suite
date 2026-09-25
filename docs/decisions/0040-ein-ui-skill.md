---
format_version: 1
id: ADR-0040
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/ui-package
---

# Ein UI-Skill mit bedingt geladenem WordPress-Adapter

## Decision

Der Nutzer beauftragt einen einzigen Skill `scoville-ui` ohne Anti-AI-Slop im Namen und die entsprechende Build-Anpassung, parallel zur laufenden Code- und Plan-Arbeit. Allgemeine UI-Regeln und WordPress-Adapter werden gemeinsam ausgeliefert. WordPress-Referenzen werden nur für passende Oberflächen geladen.

## Problem

Der bisherige PLAN-0006 und ADR-0015 gingen von zwei selbständigen Paketen aus. Der aktuelle Auftrag vereinigt ihre Auslieferung und Zuständigkeit.

## Drivers

- Ein Skill und ein UI-Abnahmeprozess je Oberfläche.
- WordPress-Surface-Grenzen, Versionsverträge, Classic-Verhalten und i18n bleiben erhalten.
- Fremde parallele Änderungen bleiben erhalten.

## Considered alternatives

- Zwei Pakete mit gemeinsamen Quellen: entspricht der bisherigen Planung, erfüllt aber den neuen Auftrag nicht.
- Ein Core mit lokalen Adaptern: ein Installationsziel und selektive Referenzladung.

## Consequences

- Die Paketentscheidung ersetzt die Zwei-Paket-Annahme für die noch nicht begonnenen Arbeiten. ADR-0015 bleibt als Grundlage der gemeinsamen Qualitätsanforderungen erhalten.
- Eine gemeinsame Quelle im UI-Member genügt bei nur einem Verbraucher. Ein zusätzlicher Shared-Export ist nicht nötig.
- W-006 setzt die unabhängig prüfbare Zusammenführung zuerst um. Die vorbereitende Vergleichsarbeit W-001 und ihre Prüfpflichten bleiben erhalten. Die unveränderlichen Felder von W-001 bewahren den damaligen Auftrag.
- Installation, Repository-Veröffentlichung und Umbenennung auf GitHub sind nicht Teil dieser Änderung. Historische Member-Aufzeichnungen und Git-Historie bleiben erhalten.

## Confirmation

1. Baue Standalone/general sowie Suite/general und Suite/codex mit genau einem UI-Member.
2. Prüfe lokale Referenzauflösung, Metadaten, WordPress-Routing und den isolierten Build.
3. Halte die noch offenen praktischen Vergleiche getrennt von Paketprüfungen fest.

## Revisit when

Ein Adapter verlangt widersprüchliche gemeinsame Regeln oder lädt unnötige Plattformreferenzen.
