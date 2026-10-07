---
format_version: 1
id: ADR-0199
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/build-checks
---

# Technische Buildprüfungen statt Prosa-Gates

## Decision

Der Nutzer verlangt, Build- und Release-Hürden auf bestimmte Wörter oder
Prosaformulierungen zu entfernen. Geprüft werden technische Struktur,
Dateivollständigkeit, Referenzen, Imports und Paketzuordnung. Redaktionelle
Wortlisten, Satzfragmente und willkürliche Textvorkommen sind keine Abnahmehürde.
Die bereits beauftragten praktischen Skill- und Helper-Nachweise bleiben bestehen.

Nutzerpräzisierung vom 06.10.2026: Technisch notwendige Konsistenzprüfungen,
etwa für maßgebliche Versionsangaben, brauchen keine zusätzliche ausdrückliche
Nutzervorgabe. Ihr Vertrag muss unabhängig vom Test bestehen und für ein
tatsächliches Programm, einen Build oder eine Host-Schnittstelle erforderlich
sein. Anleitungstext ist kein technischer Vertrag. Exakte Prosa wird nur auf
ausdrückliche Nutzervorgabe geprüft. Die gemeinsame Regel steht nach Opus-Beratung
und Astra/high-Vorprüfung allein in Code `references/validation.md`.

## Problem

Ein Workflow-Test scheiterte allein am alten Fehlermeldungssatz, obwohl der
Helper seine neue Eingabemöglichkeit korrekt nannte. Weitere Buildtests prüften
bestimmte Anleitungsformulierungen statt ihre technische Aussage.

## Drivers

- Nutzerkorrektur vom 06.10.2026: Diese zusätzlichen Wortlauttests waren nicht
  beauftragt und sollen den Fortschritt nicht weiter blockieren.

## Considered alternatives

- Satzprüfungen nach jeder Textänderung anpassen: erhält die unnötige Hürde
  und liefert keinen Verhaltensnachweis. Vom Nutzer verworfen.

## Consequences

Inhaltliche Skill-Anforderungen werden durch tatsächliche Verwendung und
gezielte fachliche Bewertung beurteilt. Technische Ausgabeformate, unveränderte
vollständige Datenübertragung und die Herkunft generierter Dateien bleiben
prüfbare Verträge. Historische Ergebnisse werden nicht umgeschrieben.

## Confirmation

Die maschinell erfassten Prüfstellen gegen ihre technischen Verträge beurteilen,
Prosa-Gates entfernen und die verbleibenden relevanten Prüfungen über Actions
ausführen. Diese Entscheidung behauptet noch keinen bestandenen Nachtest.

## Revisit when

Ein neues externes Format einen konkreten maschinenlesbaren Inhalt verlangt.
