---
format_version: 1
id: ADR-0098
status: accepted
created: 2026-09-27
accepted: 2026-09-27
scope: workflow/orchestration
supersedes: ADR-0064
---

# Kontextreserve mit 40 und 60 Prozent erproben

## Decision

Die vom Nutzer gewählten Defaults sind Koordinator ab 40 Prozent und Worker, Reviewer sowie Reparaturworker strikt über 60 Prozent. Projektüberschreibungen bleiben erhalten. Der übrige in ADR-0064 dokumentierte Ablauf bleibt unverändert gültig, soweit spätere Decisions ihn nicht bereits ersetzt haben. Diese Ablösung ändert ausschließlich die Schwellenwahl.

## Problem

Die bisherigen 25 Prozent liegen nahe am gemeldeten Startkontext eines Koordinators. Die bisherigen 75 Prozent lassen Workern wenig Reserve für umfangreiche Abschnitte.

## Drivers

- Der Nutzer will 40/60 ausdrücklich erproben.
- Der Ablauf soll schlank bleiben und sichere Fortsetzung erhalten.

## Considered alternatives

- 25/75 behalten: vom Nutzer für diesen Versuch abgelöst.
- Zusätzliche Wächter oder harte Kontextgarantien: nicht erforderlich und nicht belegt.

## Consequences

Vergleichsoperatoren, native Compaction, geordnete Arbeit und Übergaben bleiben erhalten. Die Schwellen sind Auslöser an Checkpoints und garantieren keine maximale Belegung. Bestehende Projektkonfigurationen werden nicht geändert. Installierte Helper lesen Defaults bei jedem Aufruf; ein lokales Update kann deshalb auch den nächsten Checkpoint eines laufenden Chats beeinflussen.

## Confirmation

Grenzfälle, Overrides und ungültige Werte prüfen. Gezielten Luna-High-Lauf und finales Astra-Medium-Review auswerten. Reale Kontextsprünge erst im nächsten beauftragten Workflow beobachten.

## Revisit when

Ein echter Lauf zeigt weiterhin unnötige Wechsel oder zu wenig Kontextreserve.
