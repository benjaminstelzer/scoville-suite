---
format_version: 1
id: ADR-0170
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/runtime-ci
supersedes: ADR-0151
---

# Private CI für korrigierte Teststände ausführen

## Decision

Korrigierte, lokal geprüfte Testsnapshots dürfen im privaten Repository
benjaminstelzer/scoville-runtime-ci committet und gepusht werden. Die sechs
Runtime-CI-Jobs dürfen laufen. Für weitere Korrektursnapshots desselben
Testauftrags ist keine erneute Einzelzustimmung nötig.

## Problem

Die frühere Freigabe betraf nur den Snapshot bd26c0b4. Neue Skill-Korrekturen
erfordern einen CI-Nachweis für die neuen Paketbytes.

## Drivers

Nach Erklärung der offenen privaten CI-Freigabe bestätigt der Nutzer:
„Ja du hat alle Freigaben die nötig sind um die skills zu verbessern“.

## Considered alternatives

Erneut nach jedem Snapshot zu fragen widerspricht dieser Freigabe.

## Consequences

Testdaten und Vorbereitung bleiben unter Desktop/test. Vor dem Push die
Snapshot-Inhalte und lokalen Checks prüfen. Keine Zugangsdaten oder privaten
Modellantworten in den Snapshot übernehmen. Quellen bleiben uncommittet.
Veröffentlichung, Installation und Änderungen am Release-Staging sind für
diese Prüfung nicht erforderlich und werden nicht ausgeführt.

## Confirmation

Snapshot-Hash, Commit und zugehörige CI-Ergebnisse mit Paket- und Test-Hashes
belegen. Ein älterer grüner Lauf ersetzt keinen Nachweis für neue Paketbytes.

## Revisit when

Zielrepository oder Umfang der externen Übertragung geändert werden soll.
