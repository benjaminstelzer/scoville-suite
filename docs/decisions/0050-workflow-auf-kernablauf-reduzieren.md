---
format_version: 1
id: ADR-0050
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: workflow/orchestration
superseded_by: ADR-0063
transition_batch: f4ac9627ee1ebc83f5a18c0e13e4603d1b8485d4b1e82bf5fda3951a69d634b4
transition_batch_members: [ADR-0047, ADR-0048, ADR-0049, ADR-0050, ADR-0051]
---

# Workflow auf eine klare Ausführungsschleife reduzieren

## Decision

Empfohlen: der aufrufende Task koordiniert eine Einheit nach der anderen. Er startet direkt einen Worker, prüft dessen Ergebnis und den tatsächlichen Diff, startet bei relevanten Änderungen einen Reviewer und höchstens drei Reparaturen. Eigene Prozent-Rolloverketten, Park-/Aktivierungszeremonien, Modell-Transportbelege und Standard-Bundling entfallen.

## Problem

Der derzeitige Workflow enthält viele Übergabezustände und umfangreiche Pflichtlektüre für denselben Kernablauf.

## Drivers

- ADR-0045 verlangt echten Komplexitätsabbau.
- Keine neue Absicherung bloß theoretischer Fälle.
- Der Plan bleibt Fortschrittsbesitzer; Schreibaufträge und Nutzerstopps müssen klar bleiben.

## Considered alternatives

- Bestehenden Workflow nur sprachlich kürzen: wenig Verhaltensrisiko, Zustandsaufwand bleibt.
- Reviewentwurf vollständig übernehmen: kurzer Vertrag, aber zugleich unnötige Format-/Routingmigrationen.
- Kernablauf vereinfachen und bestehende Schnittstellen zunächst erhalten: empfohlener kleinerer Neuschnitt.

## Consequences

- Nur Run-ID, Coordinator, aktive Einheit und Ergebnis bleiben als nachvollziehbarer Arbeitsstand. Gemäß ADR-0052 entsteht daraus keine Sperr- oder Konfliktmaschine für parallele Bearbeitung.
- Fünf Routewerte und Rollenresultatformat vorerst erhalten. Drei Modellpaare können mehrere Routen bedienen.
- AGENTS-Vertrag und Archivierung vereinfachen, ohne fremde Aufgaben zu autorisieren. Archivierungsfehler werden gemeldet und blockieren nicht die fachliche Abnahme.
- Konfiguration während eines Auftrags unverändert lassen. Kein eingefrorener Reparaturfahrplan.
- Bestehende aktive Runs nicht automatisch migrieren; betroffene akzeptierte Decisions vor Einführung gezielt ablösen.

### Umfang des Neuschnitts

Diese Tabelle ist die Abnahmecheckliste für PLAN-0011/W-010, keine neue Laufzeitregel. „Entfällt“ entfernt den Sondermechanismus, nicht die zugrunde liegende Aufgabe.

| Bereich aus F-18 | Zielzustand |
| --- | --- |
| Launcher/Coordinator-Handshake | Entfällt: aufrufender Task koordiniert direkt, kein separater Park-/Claim-Start. |
| Coordinator-Rollover | Eigene Prozent-/Nachfolgerkette entfällt; normaler gespeicherter Arbeitsstand ermöglicht Fortsetzung. |
| Worker-Übergaben | Eigene Prozent-/Generations-/Progress-Gate-Kette entfällt; bei unvollständiger Einheit klaren Rest melden und neu beauftragen. |
| Pending-Writer-Aktivierung | Parken, vorhergesagte Revision und Announcement entfallen; direkter Auftrag mit gespeichertem Taskhandle. |
| Guard-Revisionen/Generationen/Capabilities | Konfliktmaschine und Signatur entfallen; aktuelle Einheit, Task und Ergebnis bleiben Arbeitsstand für Einzelbetrieb. |
| Step-Bundling | Entfällt: eine geplante Einheit pro Worker. Größere Einheiten im Plan formulieren. |
| Archivierung | Ein Archivierungsversuch und Prüfung der Antwort; Fehler berichten, keine mehrstufige Abnahmesperre. |
| Hash-/Transportbelege | Modellseitige Hash-, Byte- und Empfangsbelege entfallen; Helper-Ergebnis direkt übergeben. |
| Persistente Goals | Eigene Übernahme-/Pausierungs-/Recovery-Sonderlogik entfällt; Workflow erzeugt kein zusätzliches Goal. Ein vorhandenes Goal sichtbar melden, nicht eigenmächtig verändern. |
| AGENTS.md-Block | Als zusätzliche Einrichtung optional; keine Pflichtprüfung vor jedem Start. Rollenauftrag enthält die nötigen Schreibgrenzen. |
| Fünf Routeklassen | Werte bleiben für bestehende Planannotationen kompatibel; Kriterien kurz erklären, keine neue Klassenskala. Reduktion auf drei ist bewusst kein Teil dieses Umbaus. |
| Review-Einstufung | Tatsächlichen Diff verwenden; doppelte Einstufungs-/Kontextprotokolle vereinfachen. Bestehendes Rollenresultatformat zunächst kompatibel lesen. |

## Confirmation

1. Gleiche jede Tabellenzeile am Endstand ab. Prüfe Normalablauf, Review mit Reparatur, drei erfolglose Reparaturen, Nutzerentscheidung, Stopp und Wiederaufnahme.
2. Vergleiche mit belegten bisherigen Fehlerfällen; streiche nicht allein für kleinere Zahlen.
3. Belege einen begrenzten realen Mehr-Einheiten-Lauf und tatsächlichen Aufwand vor Freigabe.

## Revisit when

Ein realer Lauf zeigt, dass die verbleibende Schleife einen erforderlichen Zustand nicht eindeutig behandeln kann.
