---
format_version: 1
id: ADR-0211
status: accepted
created: 2026-10-10
accepted: 2026-10-10
scope: viewer/publication
---

# Plan Viewer als eigenständige Anwendung

## Decision

projects/scoville-plan-viewer ist die einzige gepflegte Viewer-Quelle; benjaminstelzer/scoville-plan-viewer besitzt Builds und Releases. Alle Skills, auch scoville-plan, werden ohne Releases gepusht.

## Problem

Die Desktopanwendung und der Plan-Skill besitzen unterschiedliche Build- und Veröffentlichungszyklen.

## Drivers

- Unabhängige Pflege ohne doppelte Quellkopien und Prüfungen.
- Erhaltene Quellhistorie, Planformat-Kompatibilität und geprüfte Plattformdownloads.

## Considered alternatives

- Viewer innerhalb der Suite belassen: vom Nutzer zugunsten eines eigenständigen Repositorys ersetzt.

## Consequences

Viewer-Code und sein Gate gehören zum eigenen Projekt. Paket- und Runtimeprüfungen bleiben im Skillbuild. Keine zusätzliche Viewer-Quellkopie in der Suite; bestehende Tags und Git-Historie bleiben erhalten.

## Confirmation

Getrennte Quellen-, Build- und Veröffentlichungsziele sowie die Planformat-Kompatibilität prüfen. Lokale Einstellungen erhalten.

## Revisit when

Eine Änderung am gemeinsamen Planformat erfordert eine ausdrücklich gewählte Kompatibilitätsgrenze.
