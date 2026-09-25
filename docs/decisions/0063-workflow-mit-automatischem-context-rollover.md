---
format_version: 1
id: ADR-0063
status: superseded
created: 2026-09-25
accepted: 2026-09-25
scope: workflow/orchestration
supersedes: ADR-0050
superseded_by: ADR-0064
---

# Workflow vereinfachen und automatischen Context-Rollover erhalten

## Decision

Der aufrufende Task koordiniert eine Einheit nach der anderen. Er startet direkt einen Worker, prüft dessen Ergebnis und den tatsächlichen Diff, startet bei relevanten Änderungen einen Reviewer und höchstens drei Reparaturen. Automatischer Context-Rollover bleibt für Koordinator und Worker ein zentrales Pflichtfeature. Vereinfacht werden Park-/Aktivierungszeremonien, unnötige Generationen und Modell-Transportbelege; Standard-Bundling entfällt.

## Problem

Der derzeitige Workflow enthält viele Übergabezustände und umfangreiche Pflichtlektüre für denselben Kernablauf.

## Drivers

- Der Nutzer stellt klar: Context-Rollover ist das wichtigste Feature und muss für Koordinator und Worker erhalten bleiben.
- ADR-0045 verlangt echten Komplexitätsabbau ohne Verlust dieses Features.
- Keine neue Absicherung bloß theoretischer Fälle.
- Der Plan bleibt Fortschrittsbesitzer; Schreibaufträge und Nutzerstopps müssen klar bleiben.

## Considered alternatives

- Bestehenden Workflow nur sprachlich kürzen: wenig Verhaltensrisiko, Zustandsaufwand bleibt.
- Reviewentwurf vollständig übernehmen: kurzer Vertrag, aber zugleich unnötige Format-/Routingmigrationen.
- Kernablauf vereinfachen und bestehende Schnittstellen zunächst erhalten: empfohlener kleinerer Neuschnitt.

## Consequences

- Run-ID, Koordinator, aktive Einheit, Ergebnis und bei Übergabe der konkrete Nachfolgetask bleiben als nachvollziehbarer Arbeitsstand. Gemäß ADR-0052 entsteht daraus keine Sperr- oder Konfliktmaschine für parallele Bearbeitung.
- Fünf Routewerte und Rollenresultatformat vorerst erhalten. Drei Modellpaare können mehrere Routen bedienen.
- AGENTS-Vertrag und Archivierung vereinfachen, ohne fremde Aufgaben zu autorisieren. Archivierungsfehler werden gemeldet und blockieren nicht die fachliche Abnahme.
- Bestehende Kontextschwellen bleiben zunächst Defaults: Koordinator ab 33 Prozent, Worker über 66 Prozent; die Workergrenze gilt auch für Reviewer und Reparaturworker. Setup bearbeitet die Overrides in .scoville/config.json gemäß ADR-0061.
- Native Kompaktierung und ein gespeicherter Stand ersetzen keinen automatischen Taskwechsel. Kontextsignal und Auslöser müssen tatsächlich geprüft werden; fehlende Telemetrie darf keinen erfolgreichen Rollover vortäuschen.
- Konfiguration während eines Auftrags unverändert lassen. Kein eingefrorener Reparaturfahrplan.
- Bestehende aktive Runs nicht automatisch migrieren; betroffene akzeptierte Decisions vor Einführung gezielt ablösen.

### Umfang des Neuschnitts

Diese Tabelle ist die Abnahmecheckliste für PLAN-0011/W-010, keine neue Laufzeitregel. „Entfällt“ entfernt den Sondermechanismus, nicht die zugrunde liegende Aufgabe.

| Bereich aus F-18 | Zielzustand |
| --- | --- |
| Launcher/Coordinator-Handshake | Entfällt: aufrufender Task koordiniert direkt, kein separater Park-/Claim-Start. |
| Coordinator-Rollover | Bleibt automatisch: am Kontextschwellwert Gesamtstand speichern und einen Nachfolgetask zur Fortsetzung desselben Laufs starten. Keine neue Einheit im alten Koordinator starten. Taskhandle und Übernahme müssen eindeutig sein. |
| Worker-Übergaben | Bleiben automatisch: am Kontextschwellwert Zwischenstand und konkreten Restauftrag übergeben; Koordinator startet den Nachfolgeworker für dieselbe unvollständige Einheit. Kein falscher Abschluss und keine gleichzeitige Weiterarbeit des Vorgängers. |
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

1. Gleiche jede Tabellenzeile am Endstand ab. Prüfe Normalablauf, Review mit Reparatur, drei erfolglose Reparaturen, Nutzerentscheidung, Stopp und Wiederaufnahme sowie tatsächlichen automatischen Koordinator- und Worker-Rollover. Grenzwerte, fehlende/veraltete Telemetrie, eindeutiger Nachfolger und erhaltene unvollständige Arbeit gehören zur Abnahme.
2. Vergleiche mit belegten bisherigen Fehlerfällen; streiche nicht allein für kleinere Zahlen.
3. Belege einen begrenzten realen Mehr-Einheiten-Lauf und tatsächlichen Aufwand vor Freigabe.

## Revisit when

Ein realer Lauf zeigt, dass die verbleibende Schleife einen erforderlichen Zustand nicht eindeutig behandeln kann.
