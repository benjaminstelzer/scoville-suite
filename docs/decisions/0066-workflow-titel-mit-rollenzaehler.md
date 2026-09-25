---
format_version: 1
id: ADR-0066
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: workflow/task-titles
---

# Kurze Workflowtitel mit getrennten Rollenzählern

## Decision

Der Nutzer bestätigt diese Schreibweise in Großbuchstaben, mit Bindestrichen und ohne Leerzeichen:

- S-MNGR-#2-PLAN-0011
- S-WORK-#3-W-010/STEP-2
- S-REVW-#2-W-010/STEP-2
- S-FIXR-#1-W-010/STEP-2

Die Nummer zählt Aufgaben je Rolle innerhalb desselben Workflowlaufs. Jede Rolle beginnt bei 1. Ein neuer Nachfolger erhöht ihren Zähler, eine Fortsetzung derselben Aufgabe nicht. Manager zeigen die bearbeitete Plan-ID. Die anderen Rollen zeigen ihre konkrete Einheit ohne Planpunkttitel. Bei einer Einheit ohne Steps entfällt der STEP-Suffix.

## Problem

Die gemeinsame Laufnummer zeigte bei allen Managern RUN 1; lange Aufrufer- und Planpunkttitel verdeckten den relevanten Kontext.

## Drivers

- Manager-Nachfolger sollen anhand ihrer laufenden Nummer erkennbar sein.
- Alle vier Rollen erhalten dasselbe kurze Anzeigeschema.
- Der Nutzer streicht RUN, Mittelpunkt, Leerzeichen und ausgeschriebene Titel.

## Considered alternatives

- Gemeinsame Workflownummer anzeigen: unterscheidet Nachfolger nicht.
- Aufrufertitel oder Planpunkttitel anhängen: länger als die gewünschte Anzeige.
- Getrennte Rollenzähler und Plan-/Einheiten-ID: gewählte Darstellung.

## Consequences

Die neue Anzeige ersetzt die frühere Titelvorgabe in PLAN-0011/W-010. Dessen gestartete Acceptance bleibt als historische Vorgabe erhalten; diese ausdrückliche Nutzerkorrektur gilt für die Umsetzung. Logischer Workflowlauf, Reparaturversuch und Rollenzähler bleiben unterschiedliche Fakten. Der vorhandene Markdown-Laufstand hält die vier Zähler fest; keine neue Konfigurationsdatei oder Zustandsmaschine. Technische IDs bleiben unverändert, Großschreibung betrifft nur die Anzeige. Task-IDs bleiben Identität. Ask-Titel und Sidebar-Platzierung ändern sich nicht.

## Confirmation

Prüfe alle vier Rollen, aufeinanderfolgende Nummern, Plan-/Step-Anzeige, Same-Task-Fortsetzung und erhaltene IDs. Gleiche Helper, Anweisungen und erzeugte Pakete ab.

## Revisit when

Der Nutzer ein anderes Titelschema vorgibt.
