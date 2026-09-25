---
format_version: 1
id: ADR-0058
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: ask/naming-and-distribution
supersedes: ADR-0057
superseded_by: ADR-0059
---

# Ask-Aufgabentitel mit sichtbarem Trennzeichen

## Decision

Der Anzeigename lautet Ask. Technische IDs und Dateinamen bleiben unverändert.

Neue native Ask-Aufgaben heißen exakt `Ask | <Titel der aufrufenden Aufgabe>`, ohne Ask-TAsk-Suffix, Nummerierung, Modellnamen oder Adviser-ID. Der Nutzer streicht die automatische Sidebar-Platzierung vollständig, um Komplexität zu reduzieren. Es gibt dafür weder eine Einstellung noch einen optionalen Zusatzablauf.

Die unveränderte Distribution bleibt: scoville-ask-for-codex gehört zur Codex-Suite und wird zusätzlich im allgemeinen Suite-README einzeln installierbar als „Codex online“ angeboten. General führt nur den Katalogeintrag, kein Ask-Laufzeitmitglied. Workflow-Distribution, Veröffentlichungs- und Installationsgrenzen bleiben unverändert.

## Problem

Eine automatische Anordnung verursacht zusätzliche Host-Aufrufe und Pflege, während das vorangestellte Ask bereits die gewünschte Kennzeichnung liefert.

## Drivers

- Der Nutzer verlangt Ask am Anfang für Lesbarkeit langer Titel.
- Der Nutzer verlangt den Wegfall der Sidebar-Platzierung zur Vereinfachung.

## Considered alternatives

- Automatische Platzierung behalten: zusätzliche Mechanik ohne weiterhin gewünschten Nutzen.
- Platzierung optional machen: Konfiguration und Testfläche bleiben bestehen.
- Platzierung entfernen: gewählte vollständige Vereinfachung.

## Consequences

- Entferne die Ask-Platzierungsoperation, ihre Aufrufer, Einstellungen soweit vorhanden und zugehörige Anweisungen; keine Ersatzsortierung.
- Die normale Hostsortierung bestimmt die Position. Kein list_threads/reorder_section-Aufruf allein für Ask-Platzierung. Für tatsächlich benötigte Taskidentifikation bleiben vorhandene Hostmittel erlaubt.
- Task-IDs und Handles bleiben Identität. Bestehende Aufgaben werden weder umbenannt noch umsortiert.
- Diese Entscheidung plant die Änderung; keine Laufzeitimplementierung oder Veröffentlichung erfolgt hier.

## Confirmation

1. Prüfe neue kurze, lange und Unicode-Titel auf das genaue Präfix und unveränderten Aufrufertitel.
2. Prüfe im simulierten Ask-Ablauf, dass keine Platzierungsoperation ausgelöst wird und ID-Zuordnung/Fortsetzung funktionieren.
3. Prüfe Helper, Aufrufer und erzeugte Dokumentation auf entfernte Platzierungsregeln.

## Revisit when

Der Nutzer erneut eine automatische Taskanordnung ausdrücklich verlangt.
