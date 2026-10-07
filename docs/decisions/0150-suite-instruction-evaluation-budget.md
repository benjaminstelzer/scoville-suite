---
format_version: 1
id: ADR-0150
status: proposed
created: 2026-10-04
scope: suite/evaluation
---

# Modelle, Laufbudget und native Live-Proben

## Decision

Offen bleiben Claude-Testbudget, die vollständige Matrix und native Workflow-/Ask-Proben. Empfehlung für Claude: claude-opus-5-5 mit high für die fünf General-Skills und vorab begrenzte Versuche/Kosten. ADR-0161 genehmigt bereits insgesamt 150 Luna-high-Testversuche mit gebündelter Sol-6.1-high-Bewertung. Keine volle Matrix und keine nativen Proben ohne zusätzliche Freigabe.

## Problem

Die verpflichtenden Wiederholungen und Varianten des Datensatzes PLAN-0034-cases-v5 erzeugen 4.278 initiale bis 7.130 Case-Ausführungen bei überall gemischter Bewertung, zuzüglich ebenso vieler Einzelbewertungen und gesonderter Zusatzversuche. Laufkosten und verfügbare native Testumgebungen sind noch nicht gemessen. Die aktuelle Matrix steht im Laufbudgetbericht; frühere Schätzungen sind überholt.

## Drivers

Frischer Kontext; gleiche Cases und Laufzahlen; feste Modelle/Efforts; kein Kostenauftrag durch bloße Planerstellung.

## Considered alternatives

Gesamte Matrix sofort freigeben: weniger Stopps, aber unbekannte Kosten. Kleinere Stichprobe als endgültige Abnahme: wäre eine gesondert genehmigungspflichtige Abschwächung des ursprünglichen Umfangs.

## Consequences

Die Schätzung steht im Plan-Review-Bericht. Pilotkosten zählen zum späteren Gesamtbudget; gültige Pilotläufe am unveränderten Endstand dürfen in die Gesamtauswertung eingehen. Transportversuche erhalten zusätzlich ein vorab vereinbartes Kosten-/Versuchslimit. Ohne native Freigabe bleiben Workflow-/Ask-Wirkung und vollständige Abnahme offen.

## Confirmation

Modell/Effort tatsächlich beobachtet, Pilotverbrauch und extrapolierte Matrix vor voller Ausführung vorlegen. Jede Budgeterhöhung ausdrücklich bestätigen lassen.

## Revisit when

Verfügbarkeit, Preise, Hostfähigkeit, Testmatrix oder Umfang sich ändern.

