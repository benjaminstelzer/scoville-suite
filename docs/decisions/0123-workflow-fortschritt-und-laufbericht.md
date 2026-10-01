---
format_version: 1
id: ADR-0123
status: accepted
created: 2026-09-30
accepted: 2026-09-30
scope: workflow/run-feedback
---

# Auftragsfortschritt und gezielte Laufhinweise ausgeben

## Decision

Der Nutzer beauftragt die bisher geplante Anzeige und Laufdatei sowie volle
Workflow-Tests. Die Anzeige lautet `Working on: <Project> → <Plan> → <Planstep>`
und `Scope: <tatsächlich beauftragter Gesamtumfang als Freitext>`. Sie erscheint
beim ersten Punkt und danach nur bei einem Wechsel von Projekt, Plan oder Punkt.
Der Runner unterdrückt Wiederholungen auch über Managerwechsel und Wiederaufnahme.

Jeder Lauf erhält eine eigene Markdown-Datei direkt unter `.scoville/`.
Der Runner zeigt ihren vollständigen Pfad vor dem ersten Managerstart. Manager
schreiben nur Nutzerfragen, deswegen angehaltene Punkte und Probleme hinein,
die Nutzerprüfung benötigen. Sie ergänzen Klärungen und bewahren dieselbe Datei
über Übergaben. Normale Statusmeldungen und Testergebnisse gehören nicht hinein.
Nur ein vollständig abgeschlossener problemloser Lauf erhält den Satz
`No issues occurred during this run.`. Der Runner meldet den Auftragsabschluss
und gibt den Bericht aus. Stopp und Blockierung gelten nicht als Abschluss.

## Problem

Der bisherige Runner zeigt den aktuellen Planpunkt nicht. Nutzerfragen und
prüfbedürftige Probleme können beim autonomen Ablauf und Kontextwechsel verloren
gehen. Die leere Datei eines erfolgreich abgeschlossenen Laufs wirkt fehlerhaft.

## Drivers

- Ausdrücklicher Umsetzungs- und Testauftrag nach der Build-Integration.
- Native Test-Subagenten und ein realer Lauf im Testprojekt sind genehmigt.
- Keine neuen Chats und keine Anwendung des Workflow-Skills durch diesen Chat.

## Considered alternatives

- Jede Aktivität protokollieren: widerspricht dem gezielten Laufbericht.

## Consequences

Der Runner erhält zusätzlich kurze Anzeigedaten und liest beim Abschluss die
beauftragte Laufdatei. Der Dateipfad ist Kontrollmetadatum für jeden Managerstart,
kein fachlicher Übergabetext. Die direkte Vorgängerübergabe bleibt erhalten.
Schreibfehler und unbekannte Dateizustände dürfen keinen Abschluss erzeugen.

## Confirmation

Gebauten Helper-Output in seine echten Verbraucher übernehmen. Vollständige
technische Workflow-, Suite- und Shared-Tests sowie reale native Fälle für
Punktwechsel, Frage/Klärung, Stopp/Wiederaufnahme, sichere Übergabe und Abschluss
prüfen. Nicht erzeugbare Host-Transportfehler bleiben ausdrücklich unbewiesen.

## Revisit when

Der Nutzer weitere Anzeigen oder Protokollinhalte verlangt oder die Hostzustellung
die notwendigen Kontrollnachrichten nicht zuverlässig liefert.
