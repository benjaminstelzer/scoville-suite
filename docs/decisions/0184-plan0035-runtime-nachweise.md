---
format_version: 1
id: ADR-0184
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/runtime-ci
---

# Gezielter privater Runtime-Nachweislauf

## Decision

Der Nutzer bestätigt die Freigabe für den notwendigen privaten Nachlauf: genau einen Commit und Push des vorbereiteten Snapshots mit Input-SHA256 `0913349b75d90cc33c4cb7d6f58c3731c6ef36e5aaf0a1fde458b078b83c5f05` im separaten privaten Testcheckout nach `benjaminstelzer/scoville-runtime-ci`, Branch `plan0035-runtime-final`, ausführen. Dadurch genau eine unveränderte Actions-Matrix mit sechs Jobs starten, je höchstens zehn Minuten.

## Problem

W-003 und W-005 fehlen tatsächliche Actions-Nachweise ihrer neuen Budgetkorrektur- und ID-Modi. Der frühere genehmigte Lauf enthält diese Tests nicht. ADR-0182 gilt nur für seinen früheren Snapshot.

## Drivers

Nutzerklarstellung: „Welche Freigabe brauchst du, ich hab dir doch alle Freigaben gegeben?“ Die bereits angefragte konkrete CI-Aktion wird damit als freigegeben bestätigt.

Windows und WSL bestehen die ergänzten 16 Runtime-Tests. Sol 6.1/high hält die Ergänzungen für bereit. Sämtliche 291 Paketdateien sind unverändert. Im Testcheckout ändern sich nur `tests/test_runtime_helpers.py` und `runtime-input.json`.

## Considered alternatives

Freigabe vertagen: lokale Vorbereitung fortsetzen; vollständige Abnahme W-003, W-005 und deren Nachfolger bleibt offen.

## Consequences

Windows, macOS und Linux jeweils mit Python 3.11 und 3.x prüfen. Keine Suite-Quellcommits, Installation, Veröffentlichung oder Viewer-Kompilierung. Für weitere notwendige Nachläufe den bestehenden Auftrag und diese Freigabeklarstellung berücksichtigen, statt bereits erteilte Freigaben erneut einzuholen. Materielle Umfangsänderungen bleiben gesondert zu beurteilen.

## Confirmation

Exakten Commit, Inputhash, sechs Joblinks und tatsächliche Resultate sichern. Paketbindung prüfen und dieselben Sol-Adviser um vollständige Abschlussreviews bitten. Vorbereitung: `development/plan-evidence/0035-runtime-ci-gap.md` und `0035-runtime-ci-gap-proposal.json`.

## Revisit when

Die Tests oder der Snapshot ändern sich, die Matrix scheitert oder ein weiterer CI-Lauf nötig wird.
