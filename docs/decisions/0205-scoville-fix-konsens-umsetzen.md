---
format_version: 1
id: ADR-0205
status: accepted
created: 2026-10-09
accepted: 2026-10-09
scope: suite/workflow-fixes
---

# Beobachtung stoppen und abgestimmte Fixes umsetzen

## Decision

Der Nutzer beauftragt am 2026-10-09 den Stopp der EMPCO-Überwachung und die Umsetzung des beidseitigen Fixkonsenses aus PLAN-0047. Technische Tests laufen gezielt unter Windows und Linux.

## Problem

Wiederholte Aufruf- und Planfeldfehler trotz vorhandener Regeln; die Konsensvorschläge sind noch nicht umgesetzt.

## Drivers

Bestehende Argument-, Lese-, Rollen- und Ausgabegarantien erhalten; nur kanonische Quellen ändern.

## Considered alternatives

Weitere unveränderte Beobachtung: durch den ausdrücklichen Nutzerstopp ausgeschlossen.

## Consequences

Automation und Beobachtungsplan enden mit ausgewiesener historischer Auditlücke. Die lokale Umsetzung autorisiert keine Installation, Veröffentlichung oder EMPCO-Eingriffe.

## Confirmation

Gezielte Windows-/Linux-Prüfungen der geänderten Verträge und Abgleich der erzeugten Suitekopien; Modellverständlichkeit bleibt ohne Modelltest offen.

## Revisit when

Die Umsetzung verletzt eine erhaltene Garantie oder gezielte Prüfungen zeigen eine abweichende Ursache.
