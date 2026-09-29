---
format_version: 1
id: ADR-0103
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: suite/build-profiles
---

# Claude-Code-Ausgabe als drittes Buildprofil

## Decision

Der Nutzer beauftragt eine zusätzliche Claude-Code-Ausgabe im bestehenden Buildkonzept. Das Buildprofil `claude` erzeugt eine eigene Claude-Suite aus denselben Quellen wie `general` und `codex`. Code, Plan, UI und Handoff sowie ihre README-Fragmente bleiben gemeinsam. Unterschiede entstehen nur über Profilblöcke und profilgefilterte Dateien.

Neu sind Workflow for Claude und Ask for Claude. Ask for Claude spiegelt Ask for Codex: Die Claude-CLI-Route des Originals wird zur Codex-CLI-Route ("Ask Codex"). Setup gilt für beide Hosts. Workflow bleibt je Host suite-only. Der nie begonnene Entwurf PLAN-0015 wird gelöscht und durch PLAN-0019 ersetzt. Sein Inhalt bleibt in der Git-Historie. Diese Decision ergänzt ADR-0013.

## Problem

Workflow und Ask gibt es nur für Codex. Der Entwurf PLAN-0015 lag vor ADR-0101 und ADR-0102 und setzte einen Coordinator-Subagenten voraus, den interaktives Claude Code im Standard-Fork-Modus nicht unterstützt.

## Drivers

- Nutzerauftrag vom 2026-09-28: zusätzlicher Claude-Build, Buildkonzept und gemeinsame READMEs bleiben, Ask Codex als Variante von Ask Claude.
- Gemeinsame Fachregeln werden einmal gepflegt.
- Codex- und General-Ausgabe ändern sich nur durch angenommene Decisions.

## Considered alternatives

- Eigene Claude-Kopien der Member: einfache Trennung, doppelte Pflege.
- Claude-Member im Profil `general`: `general` muss für andere Hosts portabel bleiben.

## Consequences

Der Builder verliert seine festen `codex`-Annahmen und kennt drei Profile. Die Scope-Regeln in den AGENTS.md-Dateien, ADR-0001 und ADR-0079 gelten zusätzlich für die Claude-Suite. Sichtbarkeit und Veröffentlichung entscheidet der Nutzer erst im Release-Gate.

## Confirmation

Alle drei Profile bauen aus demselben Quellenstand. General und Codex sind bytegleich zu ihrem letzten Build, soweit keine Decision eine Änderung annimmt. Die Claude-Suite enthält genau Code, Plan, UI, Handoff, Workflow for Claude, Ask for Claude und Setup. Ihre READMEs entstehen aus den gemeinsamen Fragmenten.

## Revisit when

Die gemeinsame Quelle bildet echte fachliche Unterschiede zwischen Codex und Claude Code nicht mehr ab.
