---
format_version: 1
id: ADR-0178
status: superseded
created: 2026-10-05
accepted: 2026-10-05
scope: suite/platform-acceptance
superseded_by: ADR-0183
---

# Windows, macOS und Linux in der Schlussabnahme

## Decision

Auf ausdrücklichen Nutzerauftrag vom 05.10.2026 müssen alle ausgelieferten
Helper, Pfade und Aufrufe unter Windows, macOS und Linux funktionieren.
W-002 belegt insbesondere native Auftragsdateipfade und Sandbox-Lesbarkeit
je System. W-007 und W-009 enthalten diese Voraussetzung als Abschlusscheck.
Plattformtests werden nach Möglichkeit über GitHub Actions ausgeführt und
je Betriebssystem ausgewiesen. Ein Windows-PASS ersetzt keinen anderen Nachweis.

## Problem

Lokale Windows-Prüfungen allein können nicht die plattformübergreifende
Funktionsfähigkeit der ausgelieferten Helper und Pfade belegen.

## Drivers

- Explizite Nutzeranforderung für alle drei Betriebssysteme.
- Tatsächliche nächste Verbraucher und korrektes Quoting auf dem Zielsystem.

## Considered alternatives

- Nur lokale Windows-Tests: decken Linux-/macOS-Verhalten nicht ab.

## Consequences

Tests prüfen plattformgerechte Temp-Verzeichnisse, Pfadformate, Trennzeichen,
Leerzeichen, Unicode und Shell-Quoting. GitHub Actions kann mechanische Runtime-
und Portabilitätsprüfungen belegen; modellfreie Tests ersetzen keine erforderlichen
nativen Luna-Consumer-Proben. Fehlende Systemnachweise bleiben offen.
Der Nutzer beauftragt Actions-Tests im aktivierten Plan, keine Veröffentlichung,
Installation oder Quell-Pushes. Ein erforderlicher privater Testsnapshot-Push
braucht seine konkrete Freigabe. Vor Aktivierung läuft keine CI dieses Plans.

## Confirmation

W-007/W-009 weisen Matrix, Source-Stand, Job-/Laufergebnis und Nachweisgrenzen
aus. W-002 weist zusätzlich erfolgreiche native Lektüre je System aus.

## Revisit when

Ein Zielsystem, dessen Sandbox oder erforderliche Actions-Ausführung fehlt.
