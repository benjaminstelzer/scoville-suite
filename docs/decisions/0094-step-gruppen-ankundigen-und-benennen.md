---
format_version: 1
id: ADR-0094
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: workflow/dispatch
---

# Step-Gruppen kurz ankündigen und vollständig benennen

## Decision

Planer und ausführender Coordinator nennen Plan, ausgewählte Step-Gruppen und
den Grund der Zusammenfassung in ein bis zwei Sätzen. Im Workflow ersetzt dies
die erste Dispatch-Meldung. Kein zusätzlicher Bericht.

Worker-, Reviewer- und Repair-Titel enthalten den gesamten zugewiesenen
Step-Bereich, etwa S-WORK-#1-W-001/STEPS-1-3. Das gilt auch für alle Steps eines
Planpunkts. Der Titel zeigt nicht nur den gerade bearbeiteten Step.

## Problem

Der Nutzer muss Gruppierung und deren Nutzen erkennen können; ein einzelner
Step im Titel verdeckt den tatsächlichen Auftrag.

## Drivers

- Explizite Nutzerpräzisierung und Nachtestauftrag.
- Kurze verständliche Rückmeldung ohne zusätzliche Ablaufschicht.

## Considered alternatives

- Nur den aktuellen Step benennen: zeigt den Auftragsumfang nicht.

## Consequences

Logische Einheiten und Reihenfolge bleiben erhalten. Rollover behält den
zugewiesenen Bereich; ein Punkt ohne Steps hat keinen Step-Zusatz.

## Confirmation

SOL 6 Medium prüft die Formulierung; der native Kandidatenlauf belegt die
tatsächliche Meldung und die erzeugten Chat-Titel.

## Revisit when

Eine konkrete Meldung oder Benennung den Umfang falsch wiedergibt.
