---
format_version: 1
id: ADR-0081
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/release-2-0-0
---

# Den vollständigen Luna-Lauf für diesen Release ausnehmen

## Decision

Der Nutzer hebt das 45-Fall-Luna-Gate für den vorliegenden PLAN-0012-Release ausdrücklich auf. ADR-0011 bleibt für spätere Releases unverändert. Es wird kein bestandener vollständiger Modelllauf behauptet.

## Problem

Für die finalen Paketbytes liegt kein vollständiges 45-Fall-Ergebnis vor.

## Drivers

- Nutzerentscheidung: 45-Fall-Gate für diesen Release aufheben.

## Considered alternatives

- Alle 45 Fälle ausführen: Für diesen Release nicht gewählt.
- Begrenzte Ausnahme: Behält vorhandene gezielte Nachweise und übrige Releaseprüfungen.

## Consequences

- Der fehlende vollständige Luna-Lauf blockiert diesen Release nicht.
- Paketintegrität, bekannte Korrekturen, GitHub-Preflight und Remoteprüfung bleiben erforderlich.
- Frühere oder gezielte Modellfälle werden nicht zu einem vollständigen Pass umgedeutet.

## Confirmation

- Nenne die Ausnahme im Releaseinventar.
- Prüfe die unveränderten übrigen Releasebedingungen.

## Revisit when

Der nächste Release vorbereitet wird.
