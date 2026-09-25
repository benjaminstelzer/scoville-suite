---
format_version: 1
id: ADR-0039
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: code/integrity-guards
---

# Testschutz auf weiterhin erforderliche Garantien beziehen

## Decision

Empfohlen ist, die Abschwächung weiterhin erforderlicher Garantien zum Erreichen grüner Tests zu verbieten. Veraltete Assertions oder Validatorregeln dürfen nur als Folge einer ausdrücklich autorisierten Vertragsänderung angepasst werden. Der neue Vertrag braucht angemessene Nachweise.

## Problem

Das pauschale Schwächungsverbot unterscheidet nicht zwischen verschleierter Regression und einer beauftragten Änderung bisheriger Anforderungen.

## Drivers

- Bestehende Sicherheits-, Datenschutz- und Integritätsgrenzen bleiben bindend.
- Eine allgemeine Änderungsbitte belegt keinen Verzicht auf solche Garantien.

## Considered alternatives

- Pauschales Verbot erhalten: schützt einfach vor Greenwashing, blockiert möglicherweise legitime Vertragsänderungen.
- Anpassungen an explizite Vertragsänderungen binden: bildet den Auftrag genauer ab, erfordert jedoch einen belastbaren Autorisierungsbeleg.

## Consequences

- W-003 bleibt bis zur ausdrücklichen Annahme blockiert.
- Der Agent muss zwischen entfallener Anforderung und unerfüllter Anforderung unterscheiden.
- Unklare Autorisierung stoppt nur die davon abhängige Änderung und ist kein Anlass, Nachweise abzuschwächen.

## Confirmation

Prüfe Fälle mit beauftragter Verhaltensänderung, unverändert erforderlicher Assertion und vermeintlich aufgehobener Sicherheitsgrenze. Nur der erste Fall erlaubt eine entsprechende Anpassung bei erhaltener Nachweispflicht.

## Revisit when

Die Regel erlaubt stillschweigende Garantieverluste oder verhindert belegbar autorisierte Änderungen.
