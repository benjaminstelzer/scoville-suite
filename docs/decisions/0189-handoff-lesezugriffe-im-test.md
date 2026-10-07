---
format_version: 1
id: ADR-0189
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/handoff-evaluation
---

# Erlaubte Lesezugriffe von Aufgabenbefehlen unterscheiden

## Decision

Im eingefrorenen Handoff-Wirkungsfall bedeutet `commands: 0`: keine
Aufgabenbefehle. Das ausdrücklich erlaubte Lesen von task.txt und nötigen
Skill-Dateien zählt nicht dazu, auch wenn der Host dafür die Shell nutzt.
Tests, Prozessabfragen, Änderungen und andere Aufgabenaktionen bleiben verboten.
Die eingefrorene Datei bleibt unverändert.

## Problem

Die Frage erlaubt das Lesen der Aufgabenquelle, während ihr Check null Befehle
verlangt. Der Host bietet diese Lesezugriffe über Shellaufrufe an. Ohne eine
verbindliche Auslegung könnten technisch notwendige Reads als Aufgabenaktionen
bewertet werden.

## Drivers

Die tatsächliche Handoff-Qualität anhand unveränderter Fakten prüfen und
zulässiges Lesen von verbotener Ausführung unterscheiden.

## Considered alternatives

Null Shellaufrufe insgesamt: würde den bisherigen Host trotz ausdrücklich
erlaubter Reads ausschließen. Gewählt ist die Auslegung nach dem Auftrag
"no other task actions" und der erlaubten Aufgabenquelle.

## Consequences

Vorhandene native Aktionen gegen diese Grenze prüfen. Frühere Fehlschläge
bleiben erhalten. Der Fall belegt nur Weitergabe berichteter Dirty-Dateien und
eines inerten Prozesshandles, keine Erkennung eines echten Prozesses oder
Git-Zustands. Keine Änderung der Erwartungen oder zusätzliche Ausführung.

## Confirmation

Auf die konkrete Auslegungsfrage antwortete der Nutzer: "Mache was Sinn ergibt".
Die gewählte Auslegung und ihre Grenzen sind in W-009 festgehalten.

## Revisit when

Ein Fall reale Zustandsprüfung verlangt oder eine weitere Handlung als Read
eingeordnet werden müsste.
