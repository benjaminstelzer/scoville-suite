---
format_version: 1
id: ADR-0071
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/installation-migration
---

# Neuinstallation und vollständige Altbereinigung trennen

## Decision

Die öffentliche Anleitung zeigt zuerst eine kurze Neuinstallation. Ein getrennter Upgrade-Auftrag für Nutzer früherer Scoville- oder Ask-Suites entfernt alle bekannten früheren Suite-Skill-IDs samt Einstellungen sofern vorhanden und installiert danach das gewählte vollständige Profil frisch aus dessen GitHub-Repository.

## Problem

Ein gemeinsamer Installationsblock verbirgt die Neuinstallation und kann alte umbenannte Skills parallel zur neuen Suite aktiv lassen.

## Drivers

- Der Nutzer verlangt die Neuinstallation als wichtigste und erste Anleitung.
- `scoville-code-anti-ai-slop` bleibt neben `scoville-code` bestehen wenn nur der neue Name installiert wird.
- Die fünf Ask-Einzel-Skills fehlen in der bisherigen allgemeinen Entfernungsliste.

## Considered alternatives

- Ein gemeinsamer Auftrag: Ist kurz aber belastet Neuinstallationen mit Migrationsarbeit und macht profilabhängige Lücken wahrscheinlicher.
- Nur geänderte Namen entfernen: Lässt gleich benannte ältere Paketstände und weitere frühere Suite-Mitglieder zurück.
- Zwei Anleitungen mit vollständiger Alt-ID-Liste: Hält die Neuinstallation kurz und macht den Upgrade-Fall vollständig.

## Consequences

- Beide Suite-READMEs erhalten dieselbe vollständige Alt-ID-Liste unabhängig vom Zielprofil.
- Fehlende Einträge werden übersprungen und fremde Skills bleiben unangetastet.
- Persönliche Einstellungen der entfernten Altinstallationen werden ohne Sicherung oder Übernahme gelöscht.

## Confirmation

1. Prüfe in beiden gerenderten Suite-READMEs die Reihenfolge Neuinstallation vor Upgrade.
2. Vergleiche die Upgrade-Liste mit der früher veröffentlichten Scoville-Suite und den fünf Ask-IDs.
3. Führe isolierte Fälle für vollständigen Altbestand fehlende Einträge und einen fremden Skill aus.

## Revisit when

Eine frühere unterstützte Suite erhält weitere installierbare Skill-IDs oder parallele Profile werden ausdrücklich unterstützt.
