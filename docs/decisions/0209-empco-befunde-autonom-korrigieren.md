---
format_version: 1
id: ADR-0209
status: accepted
created: 2026-10-09
accepted: 2026-10-09
scope: suite/empco-observation
---

# Bestätigte EMPCO-Beobachtungsbefunde autonom korrigieren

## Decision

Der Nutzer beauftragt für den benannten EMPCO-Lauf jede bestätigte Scoville-Fehlanwendung oder Suiteursache bis zur geprüften Auslieferung: Sol 6.1/high und Opus 5.5/high beraten, ihre Ergebnisse zum Konsens austauschen, kleinsten allgemeinen Fix umsetzen, von beiden abnehmen lassen, gezielte Checks und Luna 6/medium-Verständnisproben, Build, lokale Updates, Reloadhinweis an den Runner sowie GitHub-Push und Releases. Während jeder Fixphase ist die Überwachung pausiert; danach läuft sie für denselben Thread weiter.

## Problem

Der nach Auslieferung erneut falsch zusammengesetzte Reader-Aufruf bleibt offen. Weitere bestätigte Befunde sollen ohne wiederholte Freigabe kleiner Korrekturen behoben werden.

## Drivers

- Bestehende Texte kürzer und verständlicher ersetzen, erforderliche Garantien erhalten.
- EMPCO bleibt ausschließlich lesend. Nur Reloadhinweise an Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5 sind erlaubt; keine Tests, Projektänderungen, Stopps, Kindernachrichten oder geschützten Remotezugriffe.

## Considered alternatives

- Nur melden: lässt bestätigte Fehler trotz vorhandener Umsetzungsvollmacht offen.

## Consequences

Kleine bestätigte Fixes benötigen keine erneute Zustimmung. Schwerwiegende Vertrags-, Sicherheits- oder Scopeänderungen und tatsächlich fehlende menschliche Entscheidungen bleiben rückfragepflichtig. Ungeklärte Beobachtungen werden zuerst bestätigt; reine Produkt- oder Fixturefehler begründen keinen Suitefix. Genau ein Editor bearbeitet die Quellen. Unveränderte erfolgreiche Nachweise werden wiederverwendet.

## Confirmation

Konsens und Patchabnahme beider Reviewer, gezielte Ergebnisse, vollständige Build- und lokale Paketgleichheit sowie Remote-Dateien, Releases, Tags und erforderliche Assets nachweisen. Keine allgemeine Livewirksamkeit aus Verständnistests ableiten.

## Revisit when

Der Nutzer ändert den Auftrag, der konkrete Lauf endet oder eine schwerwiegende Änderung benötigt seine Entscheidung. Kein anderer Lauf wird automatisch übernommen.
