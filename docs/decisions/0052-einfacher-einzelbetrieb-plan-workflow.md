---
format_version: 1
id: ADR-0052
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/operating-model
---

# Plan und Workflow auf einfachen Einzelbetrieb ausrichten

## Decision

Der Nutzer priorisiert für Plan und Workflow weniger Komplexität und Tokenverbrauch sowie höhere Ausführungsgeschwindigkeit. Dafür akzeptiert er geringfügig weniger Schutz gegen Fehlbedienung. Der normale Betrieb ist ein gestarteter Auftrag, der bis zum Abschluss läuft. Währenddessen werden betroffene Projektdateien nicht parallel bearbeitet und Modelleinstellungen nicht geändert. Diese Bedienregel gehört verständlich in die READMEs.

## Problem

Vorsorgliche Absicherung paralleler Schreiber, laufender Konfigurationswechsel und komplizierter Übergaben belastet den üblichen einzelnen Durchlauf.

## Drivers

- Der Nutzer bestätigt dieses Ziel ausdrücklich für Workflow und Plan.
- Die Bedienregel ersetzt zusätzliche technische Absicherung theoretischer Paralleländerungen.
- Klare Fehler und ein nachvollziehbarer Arbeitsstand bleiben erforderlich.

## Considered alternatives

- Gleichzeitige fremde Änderungen technisch absichern: mehr Zustände und Prüfungen für einen nicht gewünschten Betriebsfall.
- Einzelbetrieb dokumentieren und darauf vereinfachen: gewählte geringere Komplexität bei bewusst engerem Betriebsvertrag.

## Consequences

- Keine neue Hash-, Snapshot-, Versionsbindungs- oder Konfliktmaschine für Änderungen während eines laufenden Auftrags. Bestehende Mechanismen mit ausschließlich diesem Zweck sollen entfallen.
- Ein kleiner Datensatz für aktuelle Einheit, Task und Ergebnis dient der Fortsetzung, nicht einer behaupteten Sperre gegen parallele Änderungen.
- Kontextgebundene Änderungen und vorhandene einfache Fehlerdiagnosen bleiben nutzbar. Keine Erfolgsmeldung ohne tatsächlich abgeschlossenes Ergebnis.
- Bei unbeabsichtigter Paralleländerung besteht keine Zusage konfliktfreier Fortsetzung oder automatischer Wiederherstellung. Sichtbare Widersprüche werden gemeldet.
- Eingabegültigkeit, Schutz vor falschen Löschzielen, Geheimnisbehandlung und ausdrückliche Autorisierungsgrenzen werden dadurch nicht aufgehoben.
- Vergleiche messen typische vollständige Planhandlungen und Workfloweinheiten: tatsächlichen Tokenverbrauch, Tool-Aufrufe und Dauer bei gleichem Ergebnis. Keine willkürlichen Prozentziele und kein zusätzlicher Großtest für bloß theoretische Fehlbedienung.
- ADR-0045 und ADR-0046 werden durch diesen konkreten Betriebsvertrag ergänzt. Die genaue Umsetzung wird im Fixplan ausgearbeitet; dieser Auftrag führt noch keine Skilländerungen aus.

## Confirmation

1. Prüfe, dass READMEs den Einzelbetrieb, den sicheren Zeitpunkt für Einstellungsänderungen und die Folgen paralleler Bearbeitung einfach erklären.
2. Prüfe normalen Durchlauf, klares Anhalten bei echtem Fehler und Fortsetzung anhand des gespeicherten Arbeitsstands.
3. Vergleiche Ergebnis, Tokens, Tool-Aufrufe und Dauer mit dem bisherigen Ablauf und benenne den bewusst entfallenen Fehlbedienungsschutz.

## Revisit when

Der Nutzer tatsächlich parallele Schreiber oder Einstellungswechsel während eines laufenden Auftrags unterstützen möchte.
