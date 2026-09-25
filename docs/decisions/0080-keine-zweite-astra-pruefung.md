---
format_version: 1
id: ADR-0080
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/release-review
---

# Keine zweite Astra-Prüfung nach den Releasekorrekturen

## Decision

Der Nutzer verlangt keine Nachprüfung und lehnt eine neue Astra-Aufgabe ab. W-011 behält den vollständigen ersten Review und die beiden Befunde. Die Korrekturen werden lokal geprüft; eine zweite unabhängige Abnahme wird nicht behauptet.

## Problem

Der erste Berater-Chat ist archiviert. Die Korrekturprüfung würde eine neue Aufgabe erfordern.

## Drivers

- Nutzeranweisung: keine nachprüfung.
- Bestätigung: Nein, vorerst keine neue Prüfung.

## Considered alternatives

- Neue Astra-Medium-Aufgabe: Vom Nutzer abgelehnt.
- Lokale Korrekturprüfung: Bewahrt die vorhandenen Befunde und setzt die freigegebene Releasearbeit fort.

## Consequences

- Keine weitere Berateraufgabe wird gestartet.
- Die gestartete Acceptance von W-011 bleibt als Historie erhalten; seine Evidence nennt diese Ausnahme.
- Sonstige Release-, Paket- und Remoteprüfungen bleiben erforderlich.

## Confirmation

- Prüfe Workflow-Freigabe und Handoff-Version lokal.
- Bewahre Review, Korrekturcommit, Receipts und die fehlende zweite unabhängige Abnahme.

## Revisit when

Der Nutzer verlangt eine weitere unabhängige Prüfung.
