---
format_version: 1
id: ADR-0210
status: accepted
created: 2026-10-10
accepted: 2026-10-10
scope: suite/publication
---

# GitHub-Releases nur für den Plan Viewer

## Decision

Auf ausdrückliche Nutzeranweisung veröffentlicht nur scoville-plan ein GitHub-Release für den Plan Viewer. Andere Skill-Releases werden entfernt. Normale Skilländerungen werden geprüft, gebaut, lokal installiert und gepusht, ohne Releasepflicht. Git-Tags und Commit-Historie bleiben erhalten. Die EMPCO-Überwachung ist auf Nutzerwunsch beendet.

## Problem

Releasepflicht und doppelte Viewer-Downloads in Suite-Releases erhöhen den Pflegeaufwand für kleine Skilländerungen.

## Drivers

- Ein gepflegter Downloadort für Viewer-Anwendungen und Installer.
- Bestehende Paket-, Runtime-, Sichtbarkeits- und Remote-Nachweise erhalten.

## Considered alternatives

- Release bei jedem Skill-Push: vom Nutzer verworfen.

## Consequences

Skillinstallation erfolgt weiter aus den veröffentlichten Paketverzeichnissen. Viewer-Releases behalten ihre eigenen Versions-, Herkunfts- und Assetprüfungen. Fremde Produkt-Releases bleiben außerhalb der Änderung.

## Confirmation

Branch-Publikationsaudit ohne Release, erhaltene Fehlerdiagnosen, unabhängige Patchreviews, gezielte Luna-Proben und neun leere Releaseinventare bei unverändertem Plan-Release prüfen.

## Revisit when

Eine neue ausdrücklich gewählte Verteilungsform benötigt eigene Release-Downloads.
