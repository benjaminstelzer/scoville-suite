---
format_version: 1
id: ADR-0228
status: accepted
created: 2026-10-30
accepted: 2026-10-30
scope: suite/source-export
supersedes: ADR-0225
---

# Publikationsgrenzen und einmalige Installationsfreigabe

## Decision

Binding sections: complete

Ab PLAN-0058 werden Folgepläne und alle von ihnen verlinkten Audits und Decisions öffentlich exportiert. Sie stehen nicht in private_records. Nicht verlinkte private Audits und Modelllaufprotokolle bleiben ausgeschlossen. PLAN-0057 und seine Audits bleiben privat. Der bestehende Export und Planvalidator bleiben zuständig; der exportierte Index und alle Planlinks müssen auflösen. ADR-0226 begrenzt den Export zum Schutz privater Namen.

Nach geprüften Änderungen und Build erhält der Nutzer den konkreten Exportinhalt und die Prüfergebnisse. Erst seine neue ausdrückliche Freigabe autorisiert Veröffentlichung auf main. Keine neuen Tags oder Releases. Keine lokale Installation; allein die nachfolgend dokumentierte einmalige Freigabe für PLAN-0060 ist ausgenommen.

Für PLAN-0060 hatte der Nutzer die frühere Installationssperre ausdrücklich durch die Anweisung „mache dann den Build, github push und das lokale update“ ersetzt. Diese Freigabe deckte die dort ausgelieferte Änderung und die Aktualisierung der vorhandenen lokalen Skillkopien ab. Sie ist keine pauschale Freigabe für spätere Pläne oder Installationen. Diese Decision ergänzt den bislang fehlenden dauerhaften Nachweis der bereits erteilten Ausnahme; sie eröffnet PLAN-0060 nicht erneut.

## Problem

Der abgeschlossene Auslieferungsbericht hielt die Nutzerfreigabe fest, während die verlinkte Publikationsdecision weiterhin eine ausnahmslose Installationssperre nannte.

## Drivers

- Ausdrückliche Nutzeranweisung zur Auslieferung und lokalen Aktualisierung von PLAN-0060.
- Widerspruchsfreie Fortsetzung anhand veröffentlichter Records.

## Considered alternatives

- Nur den Bericht als Ausnahme behalten: lässt die bindende Decision widersprüchlich.

## Consequences

Vor jeder Veröffentlichung neue öffentliche Pläne und Audits auf Zugangsdaten, persönliche Pfade und Drittnamen prüfen. Funde und Veröffentlichungsscope dem Nutzer vorlegen. Paketblöcke der kanonischen Quellen, private Testdaten und benötigte Shared-Geschwisterstruktur bleiben Grenzen der Online-Arbeit. Andere Aufträge erhalten durch die dokumentierte Ausnahme keine zusätzliche Befugnis.

## Confirmation

Exportinhalt und Links mit dem bestehenden Planvalidator prüfen. Der alte Record verweist auf diesen Ersatz; die Dokumentation von PLAN-0060 benennt die nachgetragene Ausnahme. Remote nach Freigabe verifizieren.

## Revisit when

Der Nutzer ändert Öffentlichkeit, Freigabegrenze oder Umfang der Online-Fortsetzung.
