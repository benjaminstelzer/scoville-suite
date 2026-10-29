---
format_version: 1
id: ADR-0225
status: accepted
created: 2026-10-29
accepted: 2026-10-29
scope: suite/source-export
---

# Öffentliche Folgepläne mit ausdrücklicher Veröffentlichungsfreigabe

## Decision

Binding sections: complete

Ab PLAN-0058 werden Folgepläne und alle von ihnen verlinkten Audits und Decisions öffentlich exportiert. Sie stehen nicht in private_records. Nicht verlinkte private Audits und Modelllaufprotokolle bleiben ausgeschlossen. PLAN-0057 und seine Audits bleiben privat. Der bestehende Export und Planvalidator bleiben zuständig; der exportierte Index und alle Planlinks müssen auflösen.

Nach geprüften Änderungen und Build erhält der Nutzer den konkreten Exportinhalt und die Prüfergebnisse. Erst seine neue ausdrückliche Freigabe autorisiert Veröffentlichung auf main. Keine Tags, Releases oder lokale Installation.

## Problem

Eine Online-Sitzung kann ohne Plan und verlinkte Records den Arbeitsstand nicht zuverlässig fortsetzen.

## Drivers

- Explizite Nutzerentscheidung im Folgeauftrag.

## Considered alternatives

- Alle Arbeitsrecords privat halten: verhindert die gewünschte Fortsetzung aus dem Repository.

## Consequences

Vor jeder Veröffentlichung neue öffentliche Pläne und Audits auf Zugangsdaten, persönliche Pfade und Drittnamen prüfen. Funde dem Nutzer vorlegen, nicht still exportieren. Paketblöcke der kanonischen Quellen, private Testdaten und benötigte Shared-Geschwisterstruktur bleiben Grenzen der Online-Arbeit; diese Grenzen offen nennen.

## Confirmation

Exportinhalt und sämtliche Links mit dem vorhandenen Planvalidator prüfen; sensible Inhalte und Veröffentlichungsscope vor der Freigabe vorlegen. Remote erst nach Freigabe verifizieren.

## Revisit when

Der Nutzer ändert Öffentlichkeit, Freigabegrenze oder Umfang der Online-Fortsetzung.
