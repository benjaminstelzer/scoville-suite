---
format_version: 1
id: ADR-0182
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/runtime-ci
---

# Privater Runtime-Testsnapshot für PLAN-0035

## Decision

Der Nutzer gibt am 05.10.2026 den vorbereiteten Snapshot mit Input-SHA-256
f34aea564ef4ca27c65ef5951c72258ceeb38b09ac38ff9546ec34ebb1d488b6 frei:
einen Commit im separaten Testcheckout, Push auf plan0035-runtime-final im
privaten Repository benjaminstelzer/scoville-runtime-ci und die dadurch
startende Matrix mit sechs Jobs, jeweils höchstens zehn Minuten.

## Problem

Aktuelle Paketnachweise erfordern die Runtime-Matrix. ADR-0178 und PLAN-0035
verlangen eine konkrete Freigabe für den nötigen privaten Testsnapshot-Push.

## Drivers

Windows, macOS und Linux werden jeweils mit Python 3.11 und 3.x geprüft.
Der vorgelegte Umfang umfasst 36 geänderte von 295 Dateien, keine neuen
oder gelöschten Dateien. Das Zielrepository bleibt privat.

## Considered alternatives

Freigabe vertagen: lokale Vorbereitung fortsetzen, Runtime-CI offenlassen.

## Consequences

Die Freigabe gilt für diesen Snapshot und diese Matrix. Sie umfasst keine
Suite-Quellcommits, Veröffentlichung, Installation oder Viewer-Kompilierung.
Mechanische CI ersetzt keine nativen Luna-Consumer oder Sandbox-Nachweise.

## Confirmation

Commit, Inputhash, Joblinks und Resultate unter PLAN-0035 sichern. Die genaue
Paketbindung durch den Build-Helper prüfen, bevor CI als Nachweis zählt.

## Revisit when

Ein veränderter Snapshot oder zusätzlicher CI-Lauf benötigt eine neue Freigabe.
