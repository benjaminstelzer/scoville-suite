---
format_version: 1
id: ADR-0109
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: plan/claude-code-build
---

# W-001 schließt mit zwei begründet offenen Belegen

## Decision

Nutzerentscheid: W-001 gilt als abgenommen, obwohl zwei Acceptance-Belege fehlen. `${CLAUDE_SKILL_DIR}` ist nur headless belegt, für Projekt- und Plugin-Skills. Die Optionen von `agent()` in Dynamic Workflows sind nicht beobachtet, weil die Funktion in der Probesitzung nicht verfügbar war.

## Problem

Die Acceptance von W-001 verlangt beide Belege. Der interaktive Beleg braucht eine Nutzereingabe, `agent()` war nicht verfügbar.

## Drivers

- Die Ersetzung hängt nicht vom Aufrufweg ab, die Headless-Belege decken Projekt- und Plugin-Skills ab.
- ADR-0104 verwirft Dynamic Workflow, `agent()` entscheidet nichts mehr.

## Considered alternatives

- Interaktiven Beleg durch den Nutzer nachholen: ein Befehl, verzögert aber den Abschluss ohne Einfluss auf eine Entscheidung.
- W-001 offen lassen: blockiert W-002 ohne Nutzen.

## Consequences

W-008 belegt `${CLAUDE_SKILL_DIR}` interaktiv mit, weil die Helper-Pfade der Claude-Member daran hängen.

## Confirmation

W-008 ruft einen Claude-Member interaktiv auf, und seine Helper-Pfade lösen korrekt auf.

## Revisit when

Ein interaktiver Aufruf liefert einen anderen Skill-Pfad als headless.
