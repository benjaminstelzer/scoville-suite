---
format_version: 1
id: ADR-0055
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: ask/naming-and-distribution
supersedes: ADR-0054
superseded_by: ADR-0057
---

# ASK-Präfix ohne automatische Sidebar-Platzierung

## Decision

Neue native ASK-Aufgaben heißen exakt `ASK <Titel der aufrufenden Aufgabe>`, ohne ASK-TASK-Suffix, Nummerierung, Modellnamen oder Adviser-ID. Der Nutzer streicht die automatische Sidebar-Platzierung vollständig, um Komplexität zu reduzieren. Es gibt dafür weder eine Einstellung noch einen optionalen Zusatzablauf.

Die unveränderte Distribution bleibt: scoville-ask-for-codex gehört zur Codex-Suite und wird zusätzlich im allgemeinen Suite-README einzeln installierbar als „Codex online“ angeboten. General führt nur den Katalogeintrag, kein ASK-Laufzeitmitglied. Workflow-Distribution, Veröffentlichungs- und Installationsgrenzen bleiben unverändert.

## Problem

Eine automatische Anordnung verursacht zusätzliche Host-Aufrufe und Pflege, während das vorangestellte ASK bereits die gewünschte Kennzeichnung liefert.

## Drivers

- Der Nutzer verlangt ASK am Anfang für Lesbarkeit langer Titel.
- Der Nutzer verlangt den Wegfall der Sidebar-Platzierung zur Vereinfachung.

## Considered alternatives

- Automatische Platzierung behalten: zusätzliche Mechanik ohne weiterhin gewünschten Nutzen.
- Platzierung optional machen: Konfiguration und Testfläche bleiben bestehen.
- Platzierung entfernen: gewählte vollständige Vereinfachung.

## Consequences

- Entferne die ASK-Platzierungsoperation, ihre Aufrufer, Einstellungen soweit vorhanden und zugehörige Anweisungen; keine Ersatzsortierung.
- Die normale Hostsortierung bestimmt die Position. Kein list_threads/reorder_section-Aufruf allein für ASK-Platzierung. Für tatsächlich benötigte Taskidentifikation bleiben vorhandene Hostmittel erlaubt.
- Task-IDs und Handles bleiben Identität. Bestehende Aufgaben werden weder umbenannt noch umsortiert.
- Diese Entscheidung plant die Änderung; keine Laufzeitimplementierung oder Veröffentlichung erfolgt hier.

## Confirmation

1. Prüfe neue kurze, lange und Unicode-Titel auf das genaue Präfix und unveränderten Aufrufertitel.
2. Prüfe im simulierten ASK-Ablauf, dass keine Platzierungsoperation ausgelöst wird und ID-Zuordnung/Fortsetzung funktionieren.
3. Prüfe Helper, Aufrufer und erzeugte Dokumentation auf entfernte Platzierungsregeln.

## Revisit when

Der Nutzer erneut eine automatische Taskanordnung ausdrücklich verlangt.
