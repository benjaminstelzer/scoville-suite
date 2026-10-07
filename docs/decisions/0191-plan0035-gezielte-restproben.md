---
format_version: 1
id: ADR-0191
status: proposed
created: 2026-10-06
scope: suite/evaluation
---

# Gezielte Restproben innerhalb von 130 Reservierungen

## Decision

Vorgeschlagen: Das bestehende Register bis höchstens 130 Luna/high-Versuche
fortführen, ohne alte Zeilen zu entfernen oder umzubinden. Nutzerentscheidung
ausstehend; bis dahin gilt unverändert die 120er-Grenze aus ADR-0187.

## Problem

117 Zeilen sind reserviert, 114 tatsächlich gestartet. Workflow-v2 zeigt echte
Korrektur und Fortsetzung, aber fehlenden Manager-Checkpoint, widersprüchliche
Step-Closure, umformulierte Runner-Meldungen und verbotene Executor-Löschungen.
Drei freie neue Reservierungen reichen nicht für den gezielten vollständigen
Nachtest der unterstützten Sequenzkorrektur und die übrigen Pflichtproben.

## Drivers

Skill-Verhalten nach bestätigten Problemen prüfen. Keine identischen Ask-Läufe
für eine reine verschlüsselte Beobachtungsgrenze, keine künstliche Kontextfüllung,
keine umbewerteten FAILs oder abgeschwächten fachlichen Kriterien.

## Considered alternatives

120 behalten: Source-Korrektur und übrige modellfreie Arbeit weiterführen;
fehlende native Pflichtnachweise und Planabschluss offen halten.

130 erlauben: Zwölf konkrete neue Rollen und eine Reserve ermöglichen.
Die aktuelle Abnahme wird damit nicht zugesichert.

## Consequences

Geplanter Höchstbedarf: fünf frische Luna-Rollen für den vollständigen
Workflow-Nachtest (Runner, Manager, Regression, Korrektur, Nachfolgermanager),
vier für eine gesondert ausdrücklich autorisierte echte Recovery-Probe
(Runner, Manager, unterbrochener Worker, Recovery-Worker), drei für die noch
fehlende ausgewählte Workflow-Scope-Beobachtung. 117 + 12 = 129; eine Reserve.
Unbenutzte alte Reservierungen bleiben sichtbar. Rollen nur starten, wenn ihre
konkrete Probe qualifiziert ist; tatsächlich unnötige Rollen nicht verbrauchen.
Sol6.1/high prüft pro Block. Keine Installation, Veröffentlichung oder neue
Freigabe für Source-Pushes oder lokale Viewer-Kompilierung.

## Confirmation

Nach Nutzerentscheidung Wortlaut und Grenze festhalten. Bestehende Register-
Historie, vorab reservierte reale Starts, tatsächliche Profile, vollständige
native Ergebnisse und unveränderte Abnahme prüfen. Recovery braucht einen
qualifizierten konkreten erlaubten Transfer; ein Schwellenübertritt allein
ersetzt ihn nicht. Verschlüsselte Kontrollbindung und ADR-0190 bleiben offene
Nachweis-/Maßstabfragen, keine durch Budget gelösten Kriterien.

## Revisit when

Zusätzliche Korrektur oder eine qualifizierte Probe den Restbedarf verändert.
Vor absehbarem Mehrbedarf erneut entscheiden, nie nachträglich genehmigen.
