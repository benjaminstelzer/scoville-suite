---
format_version: 1
id: ADR-0223
status: accepted
created: 2026-10-13
accepted: 2026-10-13
scope: workflow/coordination
---

# Manager entlasten und Wiederverwendung früher begrenzen

## Decision

Der gemeinsame Default für Subagenten ist 30%. Die Messung erfolgt einmal vor
dem konkreten nächsten Auftrag; laufende Schreiber werden nicht unterbrochen.
Eine Zuwachsprognose oder neue Verwaltungsdateien werden nicht eingeführt.

Der Manager beurteilt vollständige Rückgabe, Probleme, erforderliche Checks,
gemeldete Pfade und Git-Status/Statistik. Technische Diffs prüft der Reviewer.
Geänderte Steps behalten ihr Review; Risiko bestimmt Tiefe und nötigen Kontext,
nicht zusätzliche Aufgaben oder das Überspringen der Prüfung. Jeder Auftrag
enthält weiterhin genau einen Originalstep. Kein Managerwechsel oder Runner.

Gelieferte Decision-Identitäten dienen der Änderungserkennung; Agenten berechnen
keine eigenen Decision-Digests. Frühere Ergebnisse sind Belege, keine neuen
Arbeitsanweisungen. Gewöhnliche erzeugte oder kopierte Ausgaben brauchen keinen
vollständigen Inhalts-/Hashvergleich ohne eigene Anforderung oder konkreten
Fehler. Unabhängig verbindliche Integritätsverträge bleiben erhalten.

Die Begrenzung auf einen effektfreien Korrekturaufruf entfällt. Korrigierbare
Eingaben können vor Veröffentlichung und Dispatch berichtigt werden; verbindliche
Limits und unklare bereits erfolgte Wirkungen dürfen nicht umgangen werden.

## Problem

Die Neustarts zeigen doppelte Koordination und Hashprüfungen ohne eigenen
Prüfzweck. Wiederverwendete Kinder können innerhalb eines großen Steps compaktieren.

## Drivers

Explizite Nutzerentscheidungen vom 13.10.2026 nach dem Neustart-Audit für
EMPCO und Fluid Base. Belege und Grenzen:
temp/2026-10-13-workflow-restart-audit/findings.md.

## Considered alternatives

Stepgruppen und Managerwechsel sind abgelehnt. Eine Zuwachsprognose würde neue
Messwerte benötigen; die feste niedrigere Schwelle erhält das einfache Modell.

## Consequences

Frühere Ersetzung kostet zusätzliche Fresh-Starts, reduziert aber das Risiko
eines überfüllten wiederverwendeten Kindes. Sie garantiert keine compactionfreie
Ausführung eines großen Einzelsteps. Gespeicherte Projektüberschreibungen bleiben
separat; eine Defaultlieferung ändert sie nicht automatisch.

## Confirmation

Defaultgrenzen und Projektüberschreibungen technisch prüfen. Betroffene
öffentliche Texte gezielt auf Rollen, Reviewscope, Messung und Hashverzicht
prüfen. Neue Defaultlieferung beweist keine Befolgung im laufenden Agenten.

## Revisit when

Tatsächliche Folgeläufe zeigen Scopeverlust oder weiterhin Koordination ohne
eigenen Zweck. Keine neue Verwaltung allein wegen eines Einzelfalls ergänzen.
