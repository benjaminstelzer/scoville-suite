---
format_version: 1
id: ADR-0074
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/plan-editing
---

# Vorlage und Validator tragen gewöhnliche Planpflege

## Decision

SKILL.md und references/edit.md bilden den häufigen Schreibweg mit Work-Item-Vorlage. Maschinenprüfbare Formatregeln bleiben beim Validator. General behält den vollständigen manuellen Fallback ohne Python; Codex verlangt Python 3.11+ und Validator.

## Problem

Die häufige Planpflege lädt derzeit mehrere überlappende Format- und Operationsreferenzen.

## Drivers

- Weniger Anleitung bei gleicher Gültigkeit bestehender Records.
- Der Nutzer beauftragt diese Richtung in PLAN-0013 und bestätigt dessen Aktivierung.

## Considered alternatives

- Bisherige Referenzen: Bewahren Verhalten mit wiederholter Lektüre.
- Vorlage und Validator: Kürzerer Standardweg mit eigenem manuellem General-Fallback.

## Consequences

Semantische Autorität und Nachweise bleiben Modellaufgabe; ein Formatpass beweist keine Erfüllung.

## Confirmation

Vergleiche vier Standardwege und prüfe General/Codex sowie bestehende Fixtures.

## Revisit when

Validator oder manuelle Formatprüfung decken eine erforderliche Regel nicht ab.
