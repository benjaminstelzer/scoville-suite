---
format_version: 1
id: ADR-0133
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: suite/release
---

# Suiten nach Astra-Prüfung veröffentlichen und lokal ersetzen

## Decision

Der Nutzer beauftragt Astra Medium für Build-Prozess, Einzel-Skills, README-Aufbau, Stimme und Lesefluss. Bestätigte Befunde werden automatisch behoben und in derselben Astra-Session nachgeprüft. Nach bestandenen Gates sind GitHub-Releases und lokale Codex-/Claude-Suite-Updates ausdrücklich genehmigt. Viewer-Binaries entstehen nur in GitHub Actions und werden direkt an Plan und beide Suite-Releases angehängt.

## Problem

Ein Paketcheck allein bindet Viewer-Anhänge nicht an den aktuellen Quellstand oder eine erfolgreiche Plattform-Matrix.

## Drivers

- Scoville Plan und weitere Suite-Mitglieder wurden aktualisiert.
- Release-Dateien müssen zum aktuellen Quellstand passen.

## Considered alternatives

- Alte Viewer-Dateien neu benennen: falsche Version und Herkunft.

## Consequences

Private Quellen bleiben kanonisch. Publiziert werden geprüfte profilgefilterte Exporte. Bestehende Historie, Sichtbarkeit, Pfade und Einstellungen bleiben erhalten. Aktive Installationsleser werden vor dem Austausch berücksichtigt. Keine neue Marketplace-Verteilung.

## Confirmation

Astra-Nachprüfung, komplette Paket-/Testnachweise, CI-/Quell-/Hash-Abgleich und Remote-Downloadprüfung vor lokaler Installation.

## Revisit when

Ein Gate scheitert oder aktive Leser einen sicheren Installationswechsel verhindern.
