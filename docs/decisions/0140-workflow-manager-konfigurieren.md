---
format_version: 1
id: ADR-0140
status: accepted
created: 2026-10-02
accepted: 2026-10-02
scope: workflow/model-defaults
supersedes: ADR-0121
---

# Manager-Modell im Projekt festlegen

## Decision

Der Nutzer legt gpt-6.1-sol mit medium als Manager-Default fest. Setup und
`.scoville/config.json` unterstützen `workflow.manager.model` und
`workflow.manager.reasoning`. Eine ausdrückliche Wahl für einen Lauf hat Vorrang
vor Projektwerten und Paketdefaults. Nachfolger behalten das gestartete Paar.
Execute-/Review-Routen, Ask-SOL und Legacy-Pinning aus ADR-0121 bleiben unverändert.

## Problem

Manager erben bisher die Runner-Einstellung und lassen sich nicht dauerhaft
über Setup auswählen.

## Drivers

- Explizite Nutzerwahl für Konfiguration und Default.
- Ein Manager-Wechsel darf die Modellwahl eines laufenden Workflows nicht ändern.

## Considered alternatives

- Runner-Vererbung behalten: erfüllt die gewünschte Projekteinstellung nicht.

## Consequences

Bestehende Projekte ohne Manager-Eintrag verwenden den neuen Default.
Ungültige Werte stoppen die betroffene Operation mit Diagnose. Die tatsächliche
Host-Unterstützung bleibt beim Start zu prüfen. Setup startet keinen Workflow.

## Confirmation

Setup-Speicherung durch den gebauten Starthelper konsumieren. Default,
Teilüberschreibungen, ausdrückliche Wahl, Nachfolger und abgelehnte Eingaben
prüfen. Lokale Paketdateien mit dem Build vergleichen.

## Revisit when

Der Nutzer andere Manager-Defaults festlegt oder der Host das Paar ablehnt.
