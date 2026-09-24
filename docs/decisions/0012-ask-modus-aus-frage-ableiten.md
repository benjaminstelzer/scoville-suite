---
format_version: 1
id: ADR-0012
status: accepted
created: 2026-09-24
accepted: 2026-09-24
scope: ask/consultation-mode
---

# Ask-Modus aus der Frage ableiten

## Decision

Ein Ask-Skill leitet Review oder Expertenrunde aus dem tatsächlichen Auftrag ab; der Zusatz „for Review“ ist nicht erforderlich. Eine ausdrückliche Modusvorgabe des Nutzers hat Vorrang.

## Problem

Getrennte Skill-Namen für Review und allgemeine Beratung würden die beabsichtigte Zusammenführung wieder aufbrechen oder eine Review-Absicht bei anders formulierten Fragen übersehen.

## Drivers

- Der Nutzer möchte einen konfigurierbaren Skill statt fünf Varianten.
- Ein Review kann als Frage formuliert sein.
- Eine allgemeine Frage an mehrere Berater soll eine Expertenrunde auslösen.
- Bestehende Review-Aufträge sollen pro Berater unabhängig bleiben.

## Considered alternatives

- Modus nur über „for Review“ wählen: eindeutig, aber sprachlich starr und bei gleichwertigen Prüfaufträgen unzuverlässig.
- Modus aus Ziel und Gegenstand der Frage ableiten: natürliche Aufrufe, braucht überprüfbare Regeln für Grenzfälle.

## Consequences

- „Prüfe diesen Patch auf Fehler“ führt auch ohne Namenszusatz zu getrennten Review-Aufträgen; „Wie würdet ihr das lösen?“ führt zur Expertenrunde.
- Bei mehrdeutiger Absicht muss der Skill die benötigte Präzisierung einholen, bevor er unterschiedliche Aufträge versendet.
- Die Expertenrunde besteht aus unabhängigen Antworten und einer Synthese im Ursprungstask. Eine zweite Austausch- oder Moderatorrunde ist nicht verpflichtend. Ask bleibt read-only.
- Der Umbau beginnt erst nach veröffentlichter Plan-/Workflow-Korrektur und veröffentlichter Codex-Suite; die Entscheidung allein zieht keine Implementierung vor.

## Confirmation

1. Prüfe allgemeine Fragen, explizite Reviews und als Frage formulierte Prüfaufträge gegen feste erwartete Modi.
2. Prüfe, dass ausdrückliche Nutzerüberschreibungen Vorrang haben und alle ausgewählten Berater im Review unabhängig beauftragt werden, auch bei mehr als zwei Beratern.
3. Prüfe, dass mehrdeutige Fälle keinen stillschweigend gewählten Modus auslösen.

## Revisit when

Der Nutzer einen festen Modus-Schalter verlangt oder reale Anfragen durch die Ableitung wiederholt falsch geroutet werden.
