---
format_version: 1
id: ADR-0157
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/execution
---

# Testfallkorrektur und anschließende Fortsetzung

## Decision

Nach Vorlage und Einordnung des externen Opus-5.5-Reviews beauftragt der Nutzer
die Korrektur von W-002 und die anschließende Fortsetzung. W-002 wird zur
Korrektur seiner unvollständigen Abnahme wieder aufgenommen. Danach gelten
wieder W-003 bis W-013 und der Stopp vor W-001 gemäß ADR-0156.
Jeder umgesetzte Arbeitspunkt erhält einen Ask-Review durch Astra high.

## Problem

Der externe Review zeigt trotz bestandener lokaler Checks und Astra-Prüfung
Lücken in eingefrorenen Umgebungen, Erwartungen und Abdeckung.

## Drivers

Nutzerantwort „danach weiter machen“ nach der vorgeschlagenen Korrektur von W-002.

## Considered alternatives

Bei W-003 fortfahren ohne Case-Korrektur ließe die bestätigten Abnahmelücken offen.

## Consequences

Die frühere Nutzerpause nach W-002 entfällt. Frühere Datensätze und Prüfergebnisse
bleiben erhalten; ein neuer Datensatz begründet seine Änderungen vor Modelltests.
Bestehende Budget-, Live-, Commit-, Installations- und Veröffentlichungsgrenzen
bleiben unverändert. Ein weiterer externer Opus-Review wird nicht automatisch gestartet.

## Confirmation

Korrigierter, eingefrorener Katalog mit lokalem Nachweis und Astra-Review vor
Skill-Änderungen. Danach beobachtete Umsetzung bis W-013, W-001 bleibt ungestartet.

## Revisit when

Der Nutzer den Umfang oder den Stopp erneut ändert.
