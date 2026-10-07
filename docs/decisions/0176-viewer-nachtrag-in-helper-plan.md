---
format_version: 1
id: ADR-0176
status: accepted
created: 2026-10-05
accepted: 2026-10-05
scope: suite/viewer-sequencing
---

# Viewer-Nachtrag als letzter Punkt von PLAN-0035

## Decision

Auf Nutzerauftrag vom 05.10.2026 wird der noch unbegonnene W-015 aus PLAN-0034
mit gleicher ID als letzter Punkt nach PLAN-0035 übertragen. Ergebnis und
Bedienprüfungen bleiben erhalten. Seine neue Umsetzung und Nachweise gehören
in PLAN-0035. Sonst bleiben PLAN-0034 und dessen aktiver Index unverändert.
Die neue Reihenfolge ersetzt ausschließlich die bisherige Zuordnung von W-015
aus ADR-0165. PLAN-0035 bleibt draft bis PLAN-0034 abgeschlossen und der Nutzer
den neuen Plan ausdrücklich aktiviert hat.

## Problem

Der Viewer-Nachtrag soll nicht mehr den laufenden Skill-Umbau abschließen,
sondern nach den neuen Helper-Erweiterungen folgen.

## Drivers

- Ausdrücklicher Nutzerauftrag: W-015 ans Ende des neuen Plans.
- Derselbe noch nicht gestartete Umfang, keine verlorene Abnahme oder Historie.

## Considered alternatives

- W-015 in beiden Plans halten: erzeugt widersprüchliche Zuständigkeit.

## Consequences

Historische Symptombelege bleiben unter PLAN-0034 lesbar. Neue Nachweise gehören
dem neuen Plan. Native Builds benötigen weiterhin eine gesonderte Freigabe;
kein lokales Rust, keine automatische Installation oder Veröffentlichung.
Etwaige Luna-Modelltests zählen in die achtzig Versuche von ADR-0175.

## Confirmation

Unbegonnenen Status, fehlende eingehende Abhängigkeiten, erhaltenen Umfang,
letzte Position und Profilvalidierung nach der Übertragung prüfen.

## Revisit when

Der Nutzer Reihenfolge, Abnahme oder Aktivierungsgrenze ändert.
