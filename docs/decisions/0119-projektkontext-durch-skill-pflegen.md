---
format_version: 1
id: ADR-0119
status: accepted
created: 2026-09-30
accepted: 2026-09-30
scope: suite/project-context
---

# Projektkontext auf Nutzerauftrag durch einen Skill pflegen

## Decision

Der Nutzer hat den Namen `scoville-project-context-cleanup` gewählt. Der Skill
steuert Aufträge wie „Füge das den Projektregeln hinzu“, „Ergänze AGENTS.md“
oder „Aktualisiere PROJECT_INDEX.md“. Automatisch bedeutet Auswahl durch den
Agenten bei passenden Aufträgen, keine Überwachung sämtlicher Dateizugriffe.
Er prüft Informationsnutzen, kompakte Formulierung, Wiederholungen,
Widersprüche und die sinnvolle Gliederung und Reihenfolge der betroffenen Datei.
Notwendige Informationen, Bedeutung, Berechtigungen und Schutzregeln bleiben
erhalten. Scoville Plan besitzt weiterhin Indexformat und Planstatus.

## Problem

Neue Projektregeln können unnötigen Kontext und unübersichtliche Strukturen
erzeugen. Die Pflege soll als Mitglied in den bestehenden Suite-Build passen.

## Drivers

- Verständliche Anweisungen ohne versteckten Kontext, auch für Codex Luna.
- Kanonische Quellen, gezielte Aufrufe und unveränderte Zuständigkeiten.
- Beauftragt sind jetzt Planerstellung und GPT-6.1-Review, keine Umsetzung.

## Considered alternatives

- Dateizugriffe über Hooks überwachen: entspricht ausdrücklich nicht dem
  erläuterten Auftrag und fügt eine technische Anbindung hinzu.

## Consequences

Skill-Beschreibung und passende Suite-Verweise vermitteln die Aktivierung.
Der Skill führt keine pauschale Projektbereinigung aus und benötigt keinen
Watcher. Kürzere Dateien allein belegen weder bessere Ergebnisse noch
geringere Gesamtkosten. Verbindliche Regeln werden nicht als vermeintlich
überflüssig entfernt, nur weil das Modell ähnliche allgemeine Regeln kennt.

## Confirmation

Gezielte Aufträge ohne ausdrücklichen Skillnamen wählen den neuen Skill.
Ergänzungen erhalten Umfang und Regeln, passende vorhandene Texte bleiben
unverändert, Indexänderungen erfüllen weiterhin den Plan-Vertrag.

## Revisit when

Der Nutzer Dateizugriffsüberwachung, weitere Dokumentarten oder eine andere
Zuständigkeit ausdrücklich beauftragt.
