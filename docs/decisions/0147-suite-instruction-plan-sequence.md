---
format_version: 1
id: ADR-0147
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/build-order
---

# Reihenfolge gegenüber PLAN-0019

## Decision

PLAN-0034 vor PLAN-0019 W-002 umsetzen. Währenddessen keine parallelen Änderungen an gemeinsamen Build-/Skill-Quellen. PLAN-0019 übernimmt danach die dokumentierten neuen general-Blöcke und den aktualisierten Ausgangsstand.

## Problem

Beide Pläne ändern Profilblöcke, Build-Quellen und AGENTS.md. Die Vergleichsbasis darf sich nicht unbemerkt verschieben.

## Drivers

Derzeit bestehen nur general/codex; PLAN-0019 ist draft und W-002 noch todo.

## Considered alternatives

PLAN-0019 zuerst: erfordert vor Beginn eine bewusste Neufassung der Zwei-Profil-Matrix von PLAN-0034. Parallele Umsetzung: konkurrierende Quellen und ungültige Testgrundlagen.

## Consequences

Der Nutzer hat PLAN-0034 bis einschließlich W-013 zur Umsetzung ausgewählt. Neue Claude-Regeln werden hier nicht vorweggenommen.

## Confirmation

Freigegebene Reihenfolge und unveränderte Quellenbasis vor der ersten Änderung prüfen.

## Revisit when

PLAN-0019 W-002 bereits begonnen wurde oder der Nutzer Claude priorisiert.

