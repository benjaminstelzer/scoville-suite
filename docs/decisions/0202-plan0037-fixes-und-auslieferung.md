---
format_version: 1
id: ADR-0202
status: accepted
created: 2026-10-08
accepted: 2026-10-08
scope: suite/empco-findings
---

# PLAN-0037 beheben und ausliefern

## Decision

Der Nutzer autorisiert die Umsetzung der gesammelten allgemeinen Fehler, gezielte Nachtests, lokale Updates für Codex und Claude und abschließende GitHub-Releases. Opus 5.5/xhigh entwickelt Lösungen; Astra/high prüft diese vor Änderungen. Dieselbe Opus-Session und Astra/high nehmen die Fixes und anschließend Testergebnisse ab. Dies ersetzt die bisherige reine Sammlung und den Sol-Review für die Umsetzung.

## Problem

Wiederholte Fehler betreffen Texttransport, Aufträge, Zustandsnachweise und unnötige Verwaltung. Vorhandene Regeln und lokale EMPCO-Korrekturen lösen deren allgemeine Ursachen nicht ausreichend.

## Drivers

Entwicklung vor Verwaltung; vollständige Informationsübertragung, Rollenrechte und Multi-OS erhalten. EMPCO bleibt bis zur verifizierten Auslieferung pausiert; dort keine Änderungen oder Tests ausführen.

## Considered alternatives

Weiter nur sammeln: lässt die bestätigten Ursachen ungelöst. Ursachengerechte Fixes mit gezielter Abnahme: ausdrücklich beauftragt.

## Consequences

PLAN-0037 führt Fixarbeit und Auslieferung fort. Ungeklärte H-001-Originalquelle bleibt sichtbar. Nach geprüftem lokalem Update und verifiziertem GitHub-Release verlangt der Nutzer die Nachricht an den bestehenden EMPCO-Manager: neue Skills laden und den gestoppten Workflow fortsetzen.

## Confirmation

Beide verlangten Reviewer prüfen Lösungen, Fixes und Nachtestergebnisse; Build, Installationen und GitHub-Releases werden tatsächlich verifiziert.

## Revisit when

Neue Findings verlangen eine Änderung der Freigabegrenzen oder des vereinbarten Ergebnisses.
