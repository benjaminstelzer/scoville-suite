---
format_version: 1
id: ADR-0193
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/code-evaluation
---

# Mindestens zehn unterschiedliche Code-Fälle mit Kreuzreview

## Decision

Nutzerauftrag: „Wir brauchen mindestens 10 unterschiedliche Code Fälle. Passt
Astra Medium noch 7 weitere Schreiben und die von Opus 5.5 prüfen lassen“.
Zusätzlich zu Opus' drei Fällen erstellt Astra/medium sieben weitere.
Opus5.5/high prüft Astras sieben; Astra/medium prüft Opus' drei nach ADR-0192.

## Problem

Drei Fälle decken die zentralen Code-Verhaltensgrenzen nicht ausreichend breit
ab. Zehn Fälle müssen unterschiedliche tatsächliche Aufgaben prüfen.

## Drivers

Unabhängige Autoren, Kreuzreview vor Ausführung und nachvollziehbare Erwartungen.
Keine Verfahrensrezitation oder zehn künstliche Varianten derselben Aufgabe.

## Considered alternatives

Drei Fälle behalten widerspricht der Erweiterung. Sieben ergänzende Fälle
erlauben breitere Verhaltensnachweise, kosten aber zusätzliche Luna-Versuche.

## Consequences

Zehn eigenständige Fixtures und Aufgaben auf Überschneidungen prüfen. Baseline
und getrennte Referenzlösungen ausführen; Testaufbaufehler vor Luna-Starts
korrigieren und im Kreuzreview nachprüfen. Zunächst drei Läufe je Fall,
fünf bei gemischtem Urteil nach bestehendem Vertrag. Sol6.1/high bewertet pro
Block. Alle Rollen und Korrekturläufe zählen im 300er-Gesamtbudget aus ADR-0192.
Historische FAILs, ADR-0190 und übrige Freigabegrenzen bleiben erhalten.

## Confirmation

Beide vollständigen Autorenantworten, zehn unterschiedliche Aufgaben,
Kreuzreviews, eingefrorene Prüfkriterien und tatsächliche native Ergebnisse
in W-009 sichern. Mehr Fälle sind kein Ersatz für korrekte oder bestandene Fälle.

## Revisit when

Überschneidungen, unerreichbare Erwartungen oder ein bestätigter Fehler die
Auswahl verändern. Vor Ausführung den konkreten korrigierten Vertrag prüfen.
