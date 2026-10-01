---
format_version: 1
id: ADR-0129
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: plan/step-progress
---

# Stepstatus optional und direkt im Plan speichern

## Decision

Nutzerauftrag: kompatiblen Stepstatus planen, durch Astra Medium prüfen und
umsetzen. Erste optionale Annotation: `1. [status: done] Aktion.` Unterstützt
werden todo, in_progress, done und cancelled. Ohne Annotation bleibt der Status
unbekannt; alte und gemischte Listen bleiben gültig. Neue Steps erhalten Status.
Bestehende Steps werden nur bei belegtem Fortschritt ergänzt.

## Problem

Stepfortschritt muss bisher aus Evidence, Next action und Übergaben erschlossen
werden. Das erschwert den Wiedereinstieg nach einer Kompaktierung.

## Drivers

- Bestehende format_version-1-Pläne erhalten.
- Geschriebenen Fortschritt unmittelbar für Agenten und Viewer nutzbar machen.

## Considered alternatives

- Nur erledigt/offen: zeigt begonnenen Step oder aktive Gruppe nicht eindeutig.
- Vollständiger Step-Lebenszyklus: zusätzliche Pflege ohne benötigte unabhängige Abnahme.

## Consequences

Plan bleibt die einzige Fortschrittsquelle. Next action benennt konkrete
Restarbeit; Evidence hält Beobachtungen. Pause und Blocker gehören zum Work Item.
Steps haben keine eigenen Dependencies oder Acceptance. Done erfordert erledigte
Stepaufgaben und zugehörige Prüfungen; fällige Reviews bleiben erhalten.
Cancelled benötigt ausdrückliche Richtung und ist keine erledigte Arbeit.
Korrekturen bleiben möglich, ohne bereits erledigte Effekte zu wiederholen.
Nummern und route/execute bleiben erhalten. Neue Leser erhalten optionale
Strukturdaten; historische Dateien werden nicht automatisch umgestellt.

## Confirmation

Alte, neue und gemischte Listen mit Validator, Selector, tatsächlichem Dispatch-
Builder und Viewer prüfen; ungültige Annotationen diagnostizieren und korrigieren.
Aktive Stepgruppe, unbekannte Zustände und Work-Item-Abnahme getrennt prüfen.

## Revisit when

Ein konkreter Bedarf unabhängige Pause, Blocker oder Abnahme einzelner Steps verlangt.
