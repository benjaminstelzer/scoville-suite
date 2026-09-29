---
format_version: 1
id: ADR-0117
status: accepted
created: 2026-09-29
accepted: 2026-09-29
scope: ask/delivery
---

# Ask-Ergebnisse nativ im aufrufenden Chat abholen

## Decision

Auf Nutzerwunsch wird Ask auf den normalen Chat-Ablauf vereinfacht. Der Berater gibt Ergebnis oder notwendige Rückfrage als normale
Antwort in seinem Chat zurück. Der aufrufende Ask-Chat übernimmt sie über
native Task-Werkzeuge und sendet nötige Antworten an denselben Berater.
Keine zusätzliche Genehmigungslogik und kein manueller Prompt-Fallback.

## Problem

Gleich konfigurierte Astra-Berater und Workflow-Reviewer legen weitergegebene
Rücksendeaufträge unterschiedlich aus. Beide erhalten Delegationen. Die
erfolgreichen Workflow-Sendungen belegen keine Sonderberechtigung für diese
Rolle. Pflicht-Callbacks sind für das Zurückgeben einer Beratung unnötig.

## Drivers

- Nutzer verlangt den einfachsten vollständigen Beratungsablauf.
- Skilltext kann höherrangige Host-Vorgaben nicht aufheben.

## Considered alternatives

- Aktive Rücknachricht behalten: bewahrt den bisherigen Weckmechanismus,
  bleibt aber von der tatsächlich vom Host anerkannten Autorisierung abhängig.

## Consequences

Der Caller besitzt die Ergebnisabholung. Native Ereignis-Waits ersetzen keine
erfundene Callback-Garantie; Timeout, Unterbrechung und Wiederaufnahme müssen
ohne doppelte Beratung behandelt werden. Vor Änderung den vollständigen
Rückfrage-/Ergebnisweg mit Astra prüfen. Keine zusätzliche Freigabeprüfung.

## Confirmation

Direkter Helper-Output startet einen Berater; dessen Rückfrage und vollständiges
Ergebnis werden am Caller ohne zusätzliche Genehmigungsfrage übernommen.

## Revisit when

Der Host aktive Beraternachrichten zuverlässig für den Ask-Aufruf autorisiert.
