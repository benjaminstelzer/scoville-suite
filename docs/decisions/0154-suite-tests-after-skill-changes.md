---
format_version: 1
id: ADR-0154
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/instruction-quality
supersedes: ADR-0146
---

# Modelltests erst nach den Skill-Änderungen, nur mit Luna high

## Decision

Der Nutzer beauftragt PLAN-0034 auf Grundlage des geprüften Änderungsprompts.
Beauftragt sind Planerstellung und unabhängiger Review, nicht die Umsetzung.

- Keine Baseline: Modelltests laufen erst nach allen Skill-Änderungen und vor
  jeder Veröffentlichung. Builds, Paketvergleiche, Unit- und
  Helper-Consumer-Tests bleiben bei den Änderungen.
- Cases und erwartete Ergebnisse werden vor der ersten Skill-Änderung ohne
  Läufe festgelegt und eingefroren.
- Jeder anwendbare Case muss bestehen: drei Läufe, bei uneinheitlicher
  Bewertung fünf, die Mehrheit entscheidet. Kosten werden statisch gegen den
  Ausgangsstand verglichen.
- Alle Luna-Läufe nutzen gpt-6-luna mit high. W-014 setzt den Satz zur
  niedrigsten getesteten Basis in den README-Compatibility-Fragmenten auf
  Luna High. Das betrifft nur Tests, nicht Laufzeit-Defaults wie Workflows
  execute.ultra_low.
- Aus ADR-0146 gilt weiter: Laufbudget vor Ausführung schätzen; zulässige
  gemeinsame Aktivierung ist keine Verwechslung; Zusammenführung erhält
  Semantik; General umfasst fünf Skills; der Sprachtest braucht eine
  ergänzende Sichtprüfung; nach Korrekturen invalidierte Nachweise erneuern.

## Problem

ADR-0146 setzte Baseline-Läufe vor den Änderungen und Luna medium für Cleanup
und Ask voraus. Der Nutzer will nur den geänderten Stand vor der
Veröffentlichung vollständig testen.

## Drivers

- Ausdrückliche Nutzerentscheidung vom 04.10.2026.
- Weniger Läufe ohne schwächere Abnahme des geänderten Stands.
- Vorab festgelegte Erwartungen verhindern, dass Schlüssel an neue Texte angepasst werden.

## Considered alternatives

- Baseline wie in ADR-0146: zeigt Regressionen gegenüber dem Ausgangsstand, kostet aber deutlich mehr Läufe.
- Luna medium zusätzlich: stützt die bisherige README-Angabe, vergrößert aber die Matrix.

## Consequences

Ein Fehlschlag lässt sich nicht als Regression oder vorbestehender Fehler
einordnen; der Case muss trotzdem bestehen. Die README-Angabe Luna 6 Medium
weicht Luna High. Workflow-Defaults bleiben unverändert.

## Confirmation

W-002 friert den Katalog ohne Läufe ein. W-014 belegt Luna high in jeder
Laufidentität und ändert die README-Angabe erst nach bestandenen
Luna-high-Tests des jeweiligen Skills.

## Revisit when

Der Nutzer einen Vorher-Nachher-Vergleich oder weitere Luna-Efforts verlangt.
