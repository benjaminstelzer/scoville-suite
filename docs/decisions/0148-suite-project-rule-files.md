---
format_version: 1
id: ADR-0148
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/project-rules
---

# Lesen, Bearbeiten und Neuanlage von Projektregeldateien

## Decision

General berücksichtigt vorhandene anwendbare AGENTS.md und CLAUDE.md. Lesen beider Dateien erlaubt keine automatische doppelte Bearbeitung. Cleanup ändert den bestehenden zuständigen Regelort; bei widersprüchlichen gleichrangigen Regeln entscheidet der Nutzer. Fehlen beide, legt General beim Claude-Host CLAUDE.md an, bei anderen Hosts AGENTS.md. Codex nennt weiter nur AGENTS.md. Ein künftiges claude-Profil erhält seine Dateisemantik erst in PLAN-0019.

## Problem

„AGENTS.md schließt CLAUDE.md ein“ entscheidet weder Schreibziel noch Konflikte oder Neuanlage.

## Drivers

Bestehende Zuständigkeiten erhalten; keine parallelen Regeldateien für denselben Geltungsbereich erzeugen; Host-Autorität respektieren.

## Considered alternatives

Beide Dateien synchron bearbeiten: zusätzliche Wartung und Gefahr überschreibender Regeln. General legt CLAUDE.md an: priorisiert einen Host ohne entsprechende bisherige Entscheidung.

## Consequences

W-006 und die Erwartungen in W-002 übernehmen diese am 04.10.2026 ausdrücklich gewählte Host-Unterscheidung. Die Sprachregel ändert keine Nutzerdaten oder Projektregel-Sprache.

## Confirmation

Fixtures nur mit AGENTS.md, nur CLAUDE.md, beiden konsistent/inkonsistent sowie ohne lokale Datei in beiden Profilen prüfen. General prüft die Neuanlage auf Claude und auf einem anderen Host.

## Revisit when

Das claude-Profil eingeführt wird oder ein Host eine abweichende verbindliche Priorität vorgibt.

