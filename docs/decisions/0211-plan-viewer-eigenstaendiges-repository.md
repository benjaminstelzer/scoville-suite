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

Der Nutzer beauftragt die lokale und öffentliche Trennung. projects/scoville-plan-viewer ist die einzige gepflegte Viewer-Quelle; benjaminstelzer/scoville-plan-viewer besitzt Builds und Releases. Alle Skills, auch scoville-plan, werden ohne Releases gepusht. Diese Wahl ersetzt ADR-0210s Ausnahme für das Plan-Skillrepository.

## Problem

Die Desktopanwendung und der Plan-Skill besitzen unterschiedliche Build- und Veröffentlichungszyklen.

## Drivers

- Unabhängige Pflege ohne doppelte Quellkopien und Prüfungen.
- Erhaltene Quellhistorie, Planformat-Kompatibilität und geprüfte Plattformdownloads.

## Considered alternatives

- Viewer innerhalb der Suite belassen: vom Nutzer zugunsten eines eigenständigen Repositorys ersetzt.

## Consequences

Viewer-Code und sein Gate ziehen aus der Suite um. Paket- und Runtimeprüfungen bleiben im Skillbuild. Alte Downloads bleiben bis zum geprüften Ersatz verfügbar. Danach werden zehn alte Skill-Releaseobjekte entfernt; Tags und Git-Historie bleiben erhalten. EMPCO bleibt unberührt.

## Confirmation

Extrahierte Quellen vergleichen; eigenständige Actions, Downloads, Kompatibilitätsprobe, Reviewer-Konsens und Remote-Struktur prüfen. Lokale Einstellungen erhalten.

## Revisit when

Eine Änderung am gemeinsamen Planformat erfordert eine ausdrücklich gewählte Kompatibilitätsgrenze.
