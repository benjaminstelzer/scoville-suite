---
format_version: 1
id: ADR-0131
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: plan/continuation-instructions
---

# Zusätzliche Anweisungen getrennt vom Fortschritt halten

## Decision

Nutzerpräferenz und Astra-Medium-Prüfung: Ein optionales Feld Instructions statt
separater Felder für Rückkehr und offene Abnahme. Einzeiliger Freitext trägt
zusätzliche bindende Bedingungen. Exakt [] heißt ausdrücklich keine;
fehlend heißt nicht erfasst. Neue Work Items schreiben das Feld, alte dürfen
es auslassen. Schrittfortschritt gehört ausschließlich in Stepstatus.

Instructions trägt beispielsweise ausdrücklich verlangte Rückkehr oder noch
fälliges Gesamt-Review. Acceptance definiert Anforderungen, Evidence belegt
Resultate. Erfüllte Anweisungen werden aktualisiert/entfernt und ihr Vollzug
belegt. Vor neuem terminalem Abschluss bleiben keine unerfüllten bindenden
Bedingungen. Alte terminale Angaben werden als Historie gelesen.

## Problem

Zusätzliche Vorgaben sind bisher zwischen Next action und Evidence verteilt.
Mehrere neue strukturierte Felder würden Typen, Verknüpfungsregeln und
Listenpflege benötigen. Gewünscht ist eine einfache, flexible Agentenregel.

## Drivers

- Fortschritt ohne doppelte Quelle pflegen.
- Bindende Informationen beim Wiedereinstieg gezielt bereitstellen.
- Bestandskompatibilität und belegbare Migration.

## Considered alternatives

- Pending acceptance und Resume after: stärker automatisierbar, mehr Regeln.
- Nur Evidence: Nachweise und operative Anweisungen bleiben vermischt.

## Consequences

Diese Entscheidung präzisiert ADR-0130: Dessen frühere Ablage operativer
Zusatzbedingungen in Evidence wird durch Instructions ersetzt. Offene
Entscheidungen werden aus Decisions/ADRs gelesen. Die Step-Pflicht und Abschaffung
neuer Next-action-Felder bleiben bestehen; damit ist auch die ursprüngliche
Next-action-Regel aus ADR-0129 für neue Arbeit abgelöst. Alte Anweisungen bleiben
bis zu ihrer belegten Migration verbindlich.

Der Positionshelper liefert Instructions des aktuellen Items und paused_context
aller pausierten Items desselben Plans mit IDs, Status, Dependencies, Blockern
und Anweisungen. Historische Prioritätstitel werden mitgeliefert. Bei fehlenden
Instructions bleibt Legacy-Next-action/Evidence zugänglich. Der Agent beurteilt
Bedeutung und Konflikte; der Helper errechnet daraus keinen Nachfolger oder Abschluss.

Decisions bleibt Beziehungsbesitzer, ADR-Status alleinige Entscheidungsquelle.
Relevante vorgeschlagene ADRs dürfen gestarteten Items hinzugefügt werden.
Helper und Viewer zeigen daraus offene Vorschläge. Vorschläge blockieren nur
betroffene Arbeit; Ablehnung allein beseitigt keinen bestehenden Blocker.

## Confirmation

Astra Medium bestätigte diese einfachste Variante mit klarer Auswertungsgrenze.
Luna Medium prüft Wiederaufnahme, konkrete Helper-Ausgaben, Rückkehrkontext und
Migration. Validator/Reader erhalten fehlend gegenüber ausdrücklich leer.

## Revisit when

Automatische Rückkehr- oder Abnahmeentscheidung wird ausdrücklich benötigt.
