---
format_version: 1
id: ADR-0153
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/adviser-prompts
---

# Schreibregelwerk für Adviser-Aufträge und Antworten

## Decision

Das Regelwerk gilt für vom Skill formulierte Auftragsrahmen und die Adviser-Antworten. Die Nutzerfrage, Zitate, technische Schnittstellen und verborgene Erwartungsschlüssel werden nicht stilistisch umgeschrieben. Asks adviser.md behält seinen Ergebnisvertrag; native und Claude-Pfade verwenden dieselbe Regelquelle.

## Problem

Die gemeinsame Datei allein klärt nicht, ob sie die Frage, die Antwort oder beides steuert.

## Drivers

Gleicher Bedeutungs- und Ergebnisvertrag beider Adviser-Wege; unverfälschte Nutzereingaben.

## Considered alternatives

Nur Auftragsrahmen: Antworten bleiben stilistisch ungeregelt. Nutzerfrage ebenfalls umschreiben: Risiko veränderter Bedeutung oder verlorener Details.

## Consequences

W-007 und W-013 integrieren die gewählte Reichweite; sie ändern keine Adviser-Rollen oder externe Sendeberechtigungen.

## Confirmation

Beide Helper-Ausgaben unverändert an tatsächliche Consumer geben; wörtliche Fragen und technische Nutzdaten bleiben erhalten.

## Revisit when

Ein realer Adviser-Case durch das Regelwerk Bedeutung oder Ergebnisstruktur verliert.

