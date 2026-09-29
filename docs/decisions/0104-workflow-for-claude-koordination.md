---
format_version: 1
id: ADR-0104
status: accepted
created: 2026-09-28
accepted: 2026-09-28
scope: workflow/claude-coordination
---

# Workflow for Claude: Hauptsitzung koordiniert ohne Coordinator-Rollover

## Decision

Nutzerentscheid: Die Hauptsitzung ist der Coordinator. Sie startet Worker und Reviewer als Subagenten mit Modell pro Aufruf und wartet ohne Polling auf ihre Abschlussbenachrichtigung. Ihr Ergebnis ist ihre letzte Antwort. Die fachliche Logik von Workflow for Codex bleibt unverändert, einschließlich Review-Übergaben, Worker-Handoff über 60 Prozent an sicheren Punkten und Split beim dritten Handoff. Der Coordinator prüft Ergebnisse und Diffs wie bei Codex und nimmt Nutzeranweisungen direkt an.

Der Coordinator hat keinen Rollover und keine Schwelle. ADR-0063 und ADR-0098 gelten unter Claude nur für Worker, Reviewer und Reparaturworker, die Coordinator-Selbstprüfung aus ADR-0102 entfällt. Codex bleibt unverändert. Vor jedem Warten auf einen Subagenten steht der Laufstand in `.scoville/claude-workflow.md`: aktive Einheit, laufende agentId, fällige Reviews und offene Handoffs. Nach einer Auto-Compaction liest der Coordinator diese Datei neu, bevor er fortsetzt.

## Problem

Unter Claude Code kann sich eine interaktive Sitzung nicht selbst ersetzen, und das Modell kann `/compact` nicht auslösen. Ein Coordinator-Rollover bräuchte einen Coordinator-Subagenten unter einer Starter-Sitzung. Dessen `Agent`-Tool im Hintergrund widerspricht der Doku und ist für Plugin-Agents nicht belegt ([capabilities](../../development/claude-code/capabilities.md)).

## Drivers

- Der Coordinator hat sich bei schwierigen Problemen und manuellen Eingriffen bewährt und soll sich wie bei Codex verhalten.
- Autonomer Ablauf ist Pflicht, `/compact` durch den Nutzer scheidet aus.
- Nur dokumentierte Subagenten auf Tiefe 1, kein Polling, höchstens ein schreibender Subagent.
- Mehrkosten eines großen, gecachten Coordinator-Kontexts und seine Geschwindigkeit sind nachrangig.

## Considered alternatives

- Coordinator-Subagent unter schlanker Hauptsitzung mit Rollover: vollautomatisch, hängt aber an undokumentiertem Hintergrund-Nesting und braucht eine zusätzliche Ebene.
- Treiberskript steuert einen Headless-Coordinator per `claude -p --resume` und sendet `/compact`: belegt, braucht aber eigenen Treibercode, vorab erteilte Schreibrechte und läuft unsichtbar neben der Nutzersitzung.
- Dynamic Workflow als Treiber: keine Nutzereingabe während des Laufs, `agent()`-Optionen nicht verfügbar.

## Consequences

Der Coordinator-Kontext wächst über den ganzen Lauf. Lange Läufe erreichen die Auto-Compaction an einem nicht steuerbaren Punkt. Die Wiederherstellung hängt daher an `.scoville/claude-workflow.md`. Die Starter-Ebene, Coordinator-`context_handoff`, Zustellnachrichten, Archivierung und Empfangsbestätigungen entfallen.

## Confirmation

W-008 prüft interaktiv und headless: Worker-Handoff, Review mit Korrektur, Nutzereingriff und Stopp mit Wiederaufnahme. Nach einer Kompaktierung während eines laufenden Workers setzt der Coordinator aus `.scoville/claude-workflow.md` ohne doppelten Schreiber und ohne verlorenes Review fort. Das Kontextwachstum des Coordinators pro Einheit ist gemessen.

## Revisit when

Normale Pläne erreichen regelmäßig die Auto-Compaction, Wiederaufnahmen nach Kompaktierung scheitern, oder Claude Code erlaubt dem Modell eine gezielte Kompaktierung.
