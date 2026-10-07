---
format_version: 1
id: ADR-0155
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
---

# Modellgestützte Verbraucher und vollständige Schlussabnahme

## Decision

Der Nutzer hat die beiden Korrekturen aus dem erneuten Plan-Review beauftragt.
W-007 und W-013 prüfen Helper lokal ohne Modellaufrufe. W-014 prüft nach allen
Skill-Änderungen deren tatsächliche modellgestützte Verbraucher. Nachgebildete
Aufrufsignaturen ersetzen keine native Verbraucherprüfung.

W-014 wird nur mit bestandenen Pflichtprüfungen abgeschlossen, einschließlich
Helper-, Build-, Portabilitäts-, Modell- und erforderlicher Live-Prüfungen sowie
des verifizierten Runtime-CI-Builds. Fehlende Freigaben oder unverifizierte
Pflichtprüfungen erlauben einen Zwischenbericht, keine vollständige Abnahme
oder Veröffentlichung. Die Freigaben selbst sind damit nicht erteilt.

## Problem

Die bisherige Helper-Abnahme konnte Modellläufe vor deren erlaubtem Zeitpunkt
verlangen. Die Schlussabnahme verlangte bei technischen Prüfungen nur Belege,
ohne bestandene Ergebnisse ausdrücklich zur Abschlussbedingung zu machen.

## Drivers

Keine Baseline-Modellläufe; vollständige Tests vor Veröffentlichung nach ADR-0154.

## Considered alternatives

Native Verbraucher vorab prüfen widerspricht dem Testzeitpunkt. Nur lokale
Aufrufsignaturen prüfen lässt den tatsächlichen Verbraucher unbestätigt.

## Consequences

Die Änderungen können vor der Modelltestphase abgeschlossen werden. Fehlende
Pflichtnachweise halten die Schlussabnahme offen. ADR-0154 gilt unverändert.

## Confirmation

PLAN-0034 ordnet die Prüfungen W-007/W-013 und W-014 eindeutig zu und erhält
Budget-, Push- und Live-Freigaben. Die Strukturprüfung muss bestehen.

## Revisit when

Der Nutzer Testumfang, Testzeitpunkt oder Freigabegrenzen ändert.
