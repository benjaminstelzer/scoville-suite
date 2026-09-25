---
format_version: 1
id: ADR-0072
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: suite/public-export
superseded_by: ADR-0073
---

# Interne Dokumente nicht exportieren

## Decision

Die öffentlichen Suite-Exporte enthalten weder den privaten `docs/`-Baum noch `PROJECT_INDEX.md`.

## Problem

Plan-Evidence und interne Prüfberichte enthalten zulässige maschinenspezifische Pfade die nicht veröffentlicht werden sollen.

## Drivers

- Der Nutzer erlaubt persönliche Pfade nur solange `docs/` privat bleibt.
- `PROJECT_INDEX.md` würde ohne die privaten Pläne auf fehlende Dateien verweisen.
- Installierbare Pakete und öffentliche Entwicklungsquellen benötigen diese internen Datensätze nicht.

## Considered alternatives

- Interne Dokumente weiter exportieren: Bewahrt die bisherige Vollkopie veröffentlicht aber private Evidence.
- Nur persönliche Pfade redigieren: Erzeugt eine zweite Pflegepflicht für interne historische Nachweise.
- `docs/` und `PROJECT_INDEX.md` ausschließen: Hält die privaten Aufzeichnungen kanonisch und den öffentlichen Export geschlossen.

## Consequences

- Der private Quellenstand bleibt vollständig und besitzt weiterhin das native Planprofil.
- Export-Receipts und Public-Inventare enthalten keine Dateien unter `docs/` und keinen Projektindex.
- Öffentliche Suite-Repositories sind kein fortsetzbares Abbild des internen Planprofils.

## Confirmation

1. Baue beide Voll-Exporte mit `development/shared/build/export_suite.py`.
2. Prüfe Receipts und Dateibäume auf die Abwesenheit von `docs/` und `PROJECT_INDEX.md`.
3. Vergleiche alle übrigen Exportdateien und Pakete mit dem finalen Quellenstand.

## Revisit when

Interne Plan- oder Prüfdokumente sollen ausdrücklich Teil einer öffentlichen Distribution werden.
