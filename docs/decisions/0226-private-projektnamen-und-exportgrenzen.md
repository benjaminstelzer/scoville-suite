---
format_version: 1
id: ADR-0226
status: accepted
created: 2026-10-29
accepted: 2026-10-29
scope: suite/source-export
---

# Geschützte private Projektnamen

## Decision

Binding sections: complete

Geschützte private Projektnamen werden nie exportiert; ihre Liste bleibt privat. Veraltete Dateien mit solchen Namen werden auf Nutzerauftrag auch lokal entfernt. Der Fokus liegt auf vollständigen aktuellen Skills mit ihren benötigten Quellen und Tests, nicht auf historischen Berichten. Öffentliche Records enthalten neutrale Bezeichnungen und verlinken keine privaten Detailaudits. Paket- und README-Abhängigkeiten dürfen nicht durch Ausschluss verborgen werden. Dies begrenzt die öffentliche Recordregel von ADR-0225.

Öffentliche Historie wird nach Prüfung des lokalen Kandidaten bereinigt; der Nutzer verzichtet ausdrücklich auf Backups. Veröffentlichung, Force-Push und Änderungen oder Löschung vorhandener Tags benötigen die ausdrückliche Nutzerfreigabe für die vorgelegten Referenzen. Keine neuen Tags oder Releases.

## Problem

Historische Entwicklungsevidenz kann private Projektinformationen in öffentliche Distributionen und deren Historie übertragen.

## Drivers

- Ausdrücklicher Nutzerauftrag zur privaten Aufbewahrung und historischen Bereinigung.

## Considered alternatives

- Altberichte lokal aufbewahren und den Exportfilter dafür erweitern: vom Nutzer zugunsten der Entfernung und einer einfachen aktuellen Suite verworfen.

## Consequences

Der vorhandene Exporttest prüft Pfade und Inhalte gegen eine nicht exportierte Namensliste. Links auf entfernte Altberichte werden an ihrer Quelle bereinigt. Git-Umschreibung ändert Commit-IDs; fremde Klone, Forks und hostseitige Referenzen benötigen getrennte Behandlung.

## Confirmation

Exporttests, Build, README-Prüfung, check_all.py und Planvalidator bestehen. Bereinigte lokale und nach Freigabe frisch geklonte öffentliche Historien werden über erreichbare Objekte untersucht. Zugriffslücken bleiben dokumentiert.

## Revisit when

Der Nutzer ändert Schutzumfang oder Veröffentlichungsbefugnisse.
