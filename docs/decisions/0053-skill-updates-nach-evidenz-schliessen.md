---
format_version: 1
id: ADR-0053
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/plan-closure
---

# Umgesetzte Skill-Updates nach Evidenz schließen

## Decision

Der Nutzer beauftragt den Abschluss des UI-Plans und den Abgleich aller bisherigen Skill-Änderungspläne mit der tatsächlichen Umsetzung. Veraltete Statusfelder werden anhand der vorhandenen Nachweise korrigiert.

## Problem

Parallel umgesetzte Änderungen blieben wegen der gemeinsamen aktiven Planroute als draft oder todo stehen. Der UI-Plan enthält zusätzlich eine durch den späteren sichtbaren SOL-Lauf überholte Testsperre.

## Drivers

- Tatsächliche Umsetzung und vorhandene Abnahme bestimmen den Abschluss.
- Fehlende Tests oder Veröffentlichung werden nicht durch Statuspflege als durchgeführt ausgegeben.

## Considered alternatives

- Alle Records unverändert lassen: abgeschlossene Änderungen erscheinen weiter als offene Implementierung.
- Alle offenen Punkte als bestanden markieren: würde neue Reviewarbeit und ausstehende Veröffentlichungen falsch darstellen.

## Consequences

- Die bisherigen UI-, Plan- und Handoff-Updatepläne werden geschlossen. Bekannte nicht erfüllte Teilabnahmen bleiben ausdrücklich erkennbar.
- Die offene Handoff-Validatorfrage liegt bereits in PLAN-0011/W-007. Die verbliebene ASK-Altquellenbereinigung liegt dort in W-013. Diese Restpunkte werden nicht zusätzlich als bestandene alte Arbeit geführt.
- PLAN-0002 behält die gesonderten Veröffentlichungspunkte. PLAN-0011 und seine offenen Decisions bleiben neue Arbeit.
- Historische Member-Profile und Testfixtures sind keine zusätzlichen aktiven Suite-Aufträge und bleiben als Historie erhalten.

## Confirmation

1. Gleiche jeden geschlossenen Punkt mit seinen Quellen und vorhandenen Ergebnisberichten ab.
2. Dokumentiere Statusdrift und verbleibende Grenzen in `docs/skill-update-closure-2026-09-25.md`.
3. Prüfe den abschließenden nativen Planbestand und den idle-Index, ohne Produkttests erneut auszuführen.

## Revisit when

Neue Nachweise zeigen eine nicht dokumentierte Lücke im abgeschlossenen Änderungsumfang.
