---
format_version: 1
id: ADR-0130
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: plan/progress-source
---

# Neue Planpunkte nur über Steps fortsetzen

## Decision

Nutzerentscheidung: Next action als zusätzliche Fortschrittsquelle abschaffen.
Neue Work Items haben immer mindestens einen Step mit geschriebenem Status,
auch bei nur einer Aktion. Agenten pflegen den beobachteten Stepfortschritt.
Alte Steps ohne Status und alte Work Items ohne Steps bleiben gültig. Next action
wird als Legacy-Feld gelesen, für neue Arbeit aber nicht geschrieben oder verlangt.

Der Viewer ersetzt die grünen Next-action-Felder durch Next step. Die Auswahl
kommt ausschließlich aus geschriebenem Stepstatus, nicht aus dem Legacy-Feld.
Ohne Stepstatus bleibt das Feld verborgen. Der Positionshelper liefert bei
unbekanntem Fortschritt eine Evidence-/Resultatabgleich-Anweisung.

## Problem

Stepstatus und ein zusätzlich gepflegter Next-action-Text können widersprechen.
Die doppelte Pflege erhöht Aufwand und Verwechslungsgefahr beim Wiedereinstieg.

## Drivers

- Eine kanonische Fortschrittsquelle.
- Gleiches Verfahren für einen oder mehrere Steps.
- Bestandskompatibilität ohne automatische Migration.

## Considered alternatives

- Next action weiterhin zwingend synchronisieren: doppelte Pflege bleibt.
- Neue Steps optional lassen: für gleichartige neue Aufgaben entstehen zwei Verfahren.

## Consequences

Formatversion 1 bleibt erhalten. Nichtterminale Work Items haben entweder
eine gültige Legacy-Next-action-Zeile oder mindestens einen geschriebenen
Stepstatus. Parser erkennen Alter nicht aus Datum oder ID. Der Skill
erzwingt für neu angelegte Work Items mindestens einen markierten Step.
Alle neu geschriebenen Steps erhalten Status. Rückkehrbindungen, offene
Entscheidungen und konkret fehlende Abnahme stehen für neue Arbeit in Evidence.
Bestehende Legacy-Anweisungen bleiben lesbar und verbindlich.
Ein begonnenes Work Item darf mehrere tatsächlich gemeinsam begonnene Steps haben.
Unbekannte, pausierte, blockierte und vollständig erledigte Stepfolgen benötigen
eine eindeutige Auswahl oder einen ehrlichen Hinweis auf fehlende Position beziehungsweise
ausstehende Work-Item-Abnahme. Step-done ersetzt keine Acceptance oder fällige Reviews.

Auswahl: Alle geschriebenen in_progress-Steps anzeigen, nur angrenzende Nummern
gruppieren und jede unbekannte Lücke kennzeichnen. Ohne aktive Steps den ersten
geschriebenen todo nur wählen, wenn keine frühere unbekannte Lücke davor liegt.
Pause/Blocker zeigen die gespeicherte Position ohne Ausführungserlaubnis.
Nur terminale Steps ergeben keine nächste Aktion, sondern offene Work-Item-Abnahme
mit Acceptance/Evidence-Kontext. Helper aktivieren kein Reparatur-Routing.

## Confirmation

Astra Medium prüft die Logik vor Umsetzung. Validator, Selector, Workflow und
Viewer prüfen alte und neue Formen ohne Next action. Luna Medium erprobt Helper,
Step-Progression, Neuerstellung und Planreparatur im isolierten Testprojekt.

## Revisit when

Ein belegter Fortsetzungsfall benötigt Informationen, die Steps, Status, Blocker,
Acceptance und Evidence nicht ohne doppelte Fortschrittsquelle tragen können.
