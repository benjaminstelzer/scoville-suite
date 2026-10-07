---
format_version: 1
id: ADR-0198
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/evaluation
supersedes: ADR-0192
---

# Luna-Grenze aufheben und dieselbe Aufgabe direkt in Codex prüfen

## Decision

Der Nutzer verlangt dieselbe Haushaltsbuch-Aufgabe parallel direkt in dieser
Codex-Sitzung und erklärt: „Es gibt kein Luna Limit mehr.“ Luna/medium,
Sol 6.1/high für unabhängige Pflichtreviews und 15/15 bleiben gesetzt.
Der zweite Lauf verwendet die bytegleiche ursprüngliche Aufgabe in einer
eigenen Desktop-Testkopie. So bleiben beide Läufe unabhängige Einzelwriter.

## Problem

Die bisherige 300er-Grenze und Vorabreservierungen begrenzen neue notwendige
Ausführung, obwohl der Nutzer funktionierende Skills und Skripte priorisiert.

## Drivers

Bestätigte Fehler korrigieren und relevant nachtesten. Entwicklung und
beobachtbares Verhalten gehen vor Test- und Buchführungsritualen. Auch die
beibehaltene Opus-5.5/high-Session prüft die tatsächliche Ablauflogik gründlich.

## Considered alternatives

Ein gemeinsames schreibendes Testverzeichnis würde die beiden Ergebnisse
vermischen. Getrennte identische Ausgangskopien erhalten die Vergleichbarkeit.

## Consequences

Die Budgetgrenze aus ADR-0192 entfällt einschließlich ihrer Planverweise.
Historische Reservierungen und Ergebnisse bleiben vollständig erhalten.
Die übrigen Entscheidungen aus ADR-0192 bleiben gültig: unabhängige Code-Fälle,
Prüfung ihres Aufbaus, Sol-Blockreviews und gezielte Korrektur-Nachtests.
Weitere Läufe brauchen keine Budgetfreigabe. Mehr Läufe sind kein Selbstzweck.
Eingefrorene Prüfkriterien und historische FAILs bleiben. W-015 bleibt zuletzt.
Keine neue Freigabe für Installation, Veröffentlichung, Source-Push oder Rust.

## Confirmation

Direkte native Agentenidentitäten und tatsächlich berichtete Modellpaare,
Produktverhalten, Planfortschritte und Übergaben getrennt von der Linux-Probe
ausweisen. Jede bestätigte Korrektur relevant nachtesten. Bestehende private
Actions-Freigaben und Opus-Nachprüfung im selben Gespräch weiterverwenden.

## Revisit when

Der Nutzer eine neue Grenze setzt oder die gemeinsame Aufgabe geändert wird.
