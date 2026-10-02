---
format_version: 1
id: ADR-0139
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: workflow/runner-feedback
---

# Fragen und Stillstand im sichtbaren Runner melden

## Decision

Auf Nutzerwunsch vor dem UI-Nachtest die Weiterleitung Kind → Manager → Runner
prüfen und korrigieren. Der Runner nennt die genaue Frage, ihren Grund, die
betroffene Arbeit und ob sie auf Antwort oder eine externe Lösung wartet.
Neue Rückfragen und Blocker werden unabhängig von Fortschrittsmeldungen weitergegeben.

## Problem

Im DIVI-5-Verlauf wurden zwei Fragen tatsächlich weitergeleitet. Ein genereller
Nachrichtenverlust ist nicht belegt. Die Regeln beschreiben Weiterleitung vor allem
nach einem Kind-Ergebnis; eigene Managerprobleme und Rückfragen während eines
laufenden Auftrags brauchen denselben eindeutigen Vertrag.

## Drivers

- Nutzer sieht notwendige Frage und tatsächlichen Blocker im Hauptchat.
- Alle Ursachen nutzen dieselbe Weiterleitung, ohne Fortschritt zu erfinden.

## Considered alternatives

- Nur Ergebnisfälle ergänzen: lässt eigene Managerprobleme offen.
- Kinder direkt fragen lassen: verlagert die Frage aus dem sichtbaren Runner.

## Consequences

Kinder fragen ihren tatsächlichen Manager; nur der sichtbare Runner fragt den
Nutzer. Bericht und Plan bleiben erhalten, Fehler beim Speichern dürfen die
Warnung nicht verstecken. Abhängige Arbeit wartet auf die tatsächliche Antwort.
Bestehende Nachrichtenautorisierung und Senderprüfung gelten weiter. Keine
zusätzlichen Agenten, automatische Wiederholungen oder Threads zur Fehlerbehebung.

## Confirmation

Gebauten Skill seriell mit Luna Medium gegen offene Rückfrage, Manager-Blocker,
Berichtsfehler und unveränderten Fortschritt prüfen. Nur tatsächliche native
Nachrichten belegen Weiterleitung; reine Quellprüfungen sind Strukturbelege.
Nutzer verlangt gpt-6-luna Medium für Verhaltenstests, danach Astra Medium für
den gesamten Workflow-Skill sowie lokales Update und einen Codex-Suite-Release.
Astra liest ausschließlich das tatsächliche gebaute Skill-Paket ohne Plan,
Entwicklungsdokumentation, bisherigen Kontext oder Testberichte. Schwerpunkt:
schlanke, eindeutige Sprache, Dopplungen, unnötige Abschnitte und korrekte Regeln.
Außerdem anhand des Skills prüfen, ob der Runner den aktuellen Planpunkt und
den tatsächlich begonnenen Step zuverlässig erhält und sichtbar ausgibt.

## Revisit when

Native Nachrichten trotz korrekter Weiterleitung nicht sichtbar werden.
