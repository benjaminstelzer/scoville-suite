---
format_version: 1
id: ADR-0201
status: accepted
created: 2026-10-07
accepted: 2026-10-07
scope: suite/viewer-build
---

# Privater Viewer-Build und native Desktop-Gegenprobe

## Decision

Der Nutzer erteilt mit „Freigeben und fortsetzen“ die angefragte separate Freigabe: den vorbereiteten 63-Dateien-Snapshot mit Manifest-SHA256 `80d9ba264907adfc0ef888fdaa8fd31466c46e1fbb42c850946d3944a15f40f3` einmal im privaten Repository `benjaminstelzer/scoville-runtime-ci`, neuer Branch `plan0035-viewer-final`, committen und pushen. Die vier nativen Actions-Builds und der Checksum-Job sind beauftragt. Danach Artefakte herunterladen, prüfen, ausschließlich den aktuellen Viewer-Build unter `skills/temp/release/viewer/` behalten und die isolierte portable Windows-Gegenprobe durchführen.

## Problem

W-015 verlangt den Nachweis im tatsächlichen Desktop-WebView. Die Browserprobe ersetzt ihn nicht. Die bisherige Runtime-Freigabe aus ADR-0184 schloss Viewer-Kompilierung aus.

## Drivers

Die Frontend-Korrektur und ihre sechs Bedienbedingungen bestehen. Sol 6.1/high bestätigt den Stand für den nativen Build. Die konkrete Vorbereitung steht in `development/plan-evidence/0035-w015-native-build-proposal.md`.

## Considered alternatives

Freigabe vertagen: Die native Gegenprobe und der Planabschluss bleiben offen.

## Consequences

Native Kompilierung erfolgt ausschließlich in Actions für Windows x64, Linux x64, macOS Apple Silicon und Intel, je bis 45 Minuten, Checksum-Job bis zehn Minuten. Ein frischer isolierter Snapshot-Checkout enthält nur die 63 freigegebenen Dateien, damit keine alten Runtime-Workflows zusätzlich starten. Der Viewer-Download ist die begrenzte Ausnahme von der bisherigen Release-Staging-Sperre. Keine kanonischen Source-Commits oder Pushes, lokale Rust-Installation, Installation oder Veröffentlichung sind freigegeben.

## Confirmation

Commit, Jobs, terminale Ergebnisse, vollständige Artefaktliste und Checksum-Prüfung behalten. Die native Gegenprobe am tatsächlich heruntergeladenen Binary bindet Source und portable Fixture. Sol prüft den vollständigen W-015-Nachweis.

## Revisit when

Der konkrete Buildumfang oder die Veröffentlichung geändert werden soll.
