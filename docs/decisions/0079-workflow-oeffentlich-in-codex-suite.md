---
format_version: 1
id: ADR-0079
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/workflow-publication
---

# Workflow öffentlich nur in der Codex-Suite freigeben

## Decision

Der Nutzer gibt Scoville Workflow ausdrücklich zur öffentlichen Veröffentlichung ausschließlich in `scoville-suite-for-codex` frei. Das widersprechende Verbot in der Workspace-AGENTS.md entfällt. Workflow bleibt Codex-only und erhält kein eigenständiges öffentliches Paket.

## Problem

Die Workspace-Regel untersagte öffentliche Verteilung trotz der Suite-Freigabe in den Repository-Unterlagen. Astra meldete diesen Widerspruch in W-011.

## Drivers

- Nutzerantwort: Ja, öffentlich nur in der Codex-Suite freigeben.
- Nutzerauftrag: Das Verbot aus AGENTS.md entfernen.

## Considered alternatives

- Workflow privat halten: Vom Nutzer nicht gewählt.
- Öffentliche Codex-Suite: Entspricht der ausdrücklichen Freigabe und erhält die Profilgrenze.

## Consequences

- Workspace- und Repository-Regel nennen denselben Veröffentlichungsumfang.
- General und Standalone enthalten weiterhin keinen Workflow.
- Die Freigabe ersetzt keine Releaseprüfung und erlaubt keine Veröffentlichung anderer privater Quellen.

## Confirmation

- Prüfe die übereinstimmenden AGENTS.md-Regeln und die Profilinventare.
- Lass die Korrektur in der laufenden Astra-Prüfung nachprüfen.

## Revisit when

Ein eigenständiges Workflow-Paket oder ein anderes Hostprofil soll veröffentlicht werden.
