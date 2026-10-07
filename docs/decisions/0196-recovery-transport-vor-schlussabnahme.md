---
format_version: 1
id: ADR-0196
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/recovery-transport-and-order
---

# PLAN-0036 vor der finalen Suite-Abnahme ausführen

## Decision

Der Nutzer korrigiert die vorgeschlagene Reihenfolge ausdrücklich:
„ja der Plan 0036 sollte aber vor der finalne Abnahme ausgeführt werden“.
PLAN-0035/W-009 pausieren, PLAN-0036 aktivieren und dessen ausgearbeitete
Recovery-Datei-Übergabe ausführen. Danach PLAN-0035 am erhaltenen W-009-Stand
wieder aufnehmen und betroffene finale Nachweise erneuern. W-015 bleibt zuletzt.
Das gemeinsame 300er-Luna/high-Budget und bestehende Freigabegrenzen bleiben.

## Problem

Eine vollständige Inline-Recovery-Ausgabe wurde beim Caller-Capture gekürzt.
Der geprüfte Folgeplan vermeidet diesen großen Transfer durch eine vollständige
Auftragsdatei. Die bisher vorgeschlagene Umsetzung nach PLAN-0035 wäre für dessen
finale Abnahme zu spät.

## Drivers

Vollständige Übergabe vor Übernahme prüfen, ohne historische FAILs umzuwerten,
geprüfte Arbeit zu wiederholen oder den bestehenden Übernahmevertrag zu duplizieren.

## Considered alternatives

PLAN-0036 nach PLAN-0035 ausführen: vom Nutzer verworfen. In W-009 mischen:
verwischt die eigene neue Umsetzung. Gewählt ist der gesonderte aktivierte
Folgeplan mit verbindlicher Rückkehr zur offenen Suite-Abnahme.

## Consequences

Nur ein Plan ist aktiv. PLAN-0035 wird als draft mit pausiertem W-009 erhalten,
seine beobachteten Steps und historische Nachweise bleiben. PLAN-0036 erhält
W-001 als current_item. Keine Freigabe für Source-Push, Veröffentlichung,
Installation oder lokales Rust. Notwendige private Runtime-CI-Nachläufe bleiben
an die vorhandene konkrete Freigabe nach ADR-0184 gebunden.

## Confirmation

Die Umsetzung folgt der vorhandenen Astra/high-Prüfung in
development/plan-evidence/0035-w009-external-followup-astra-high-review.json:
vollständig lesen und wesentliche Fakten behalten vor HANDOFF_ACCEPTED,
danach authentifiziertes TAKEOVER_COMPLETE vor Projektarbeit. Kanonische
Helper, betroffene native Consumer, negative Aufrufe und Korrekturen gezielt
prüfen. Sol6.1/high reviewt Testblöcke und den abgeschlossenen Arbeitspunkt.

## Revisit when

Ein neues fehlendes Recht, ein größerer Scope oder ein Budgetbedarf über 300
die Umsetzung oder die verbindliche Rückkehr verhindert.
