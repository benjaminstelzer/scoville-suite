---
format_version: 1
id: ADR-0167
status: superseded
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
supersedes: ADR-0166
superseded_by: ADR-0168
---

# Vollständige Workflow-Funktionstests mit niedrigen Kontextschwellen

## Decision

Der Nutzer verlangt vollständige Scoville-Workflow-Tests einschließlich nativer
Ausführung und gezielter Kontextschwellen von 15/15 Prozent. Er erlaubt dafür
eine Erhöhung der bisherigen Gesamtgrenze. Die bestehende Suite-Auswahl behält
höchstens 300 Versuche. Zusätzlich sind höchstens 100 Workflow-Versuche geplant,
insgesamt höchstens 400. Kontrollen, Fehler und Wiederholungen zählen mit.

Die gezielte Suite-Auswahl, eingefrorene Erwartungen und gruppierte Bewertung
aus ADR-0166 bleiben bestehen. Für Workflow entfällt dessen Ausschluss nativer
Funktionsprüfungen. Andere zusätzliche native Skill-Proben sind nicht freigegeben.

## Problem

Ein einzelner hypothetischer Schreibfall belegt die Workflow-Funktion nicht.
Nach 243 gezählten Suite-/Hostversuchen bleiben im bisherigen Budget 57 Plätze
für notwendige Wiederholungen. Die zusätzliche vollständige Workflow-Prüfung
benötigt einen eigenen begrenzten Anteil.

## Drivers

Nutzer: „Also vollständige scoville Workflow Tests“, „context threshold von
15/15%“ und „Die Grenze von 300 kann dafür erhöht werden“.

## Considered alternatives

Nur der vorhandene Schreibfall oder ein einzelner erfolgreicher Durchlauf
widerspricht der erweiterten Anforderung. Unbegrenzte zusätzliche Läufe sind
nicht nötig: Der vorhandene Workflow-Katalog hat 16 eigene Fälle; zwei gezielte
Kontextgrenzen-Fälle ergeben 18, jeweils drei und bei gemischtem Urteil fünf
Läufe. 100 zusätzliche Versuche enthalten Kontrollen und begrenzte Ersatzläufe.

## Consequences

Tests und Konfiguration bleiben im Projekt test unter Desktop/test/plan0034.
Manager- und Worker-Schwellen werden dort auf 15 gesetzt, nicht in Live-Projekten.
Managerwechsel gelten ab 15 Prozent, Child-Schwellen strikt oberhalb 15 Prozent.
Gemessene Überschreitung plant den Wechsel erst nach vollständiger Zuweisung,
Prüfungen und erforderlichen Reviews bei bestätigter Writer-Ruhe. Fehlende
Telemetrie darf nicht als gemessener Wechsel gelten. Worker geben nach ihrer
letzten Prüfung regulär zurück; eine Schwelle erzeugt keinen künstlichen
Handoff unfertiger Arbeit.

Luna/high bleibt Testmodell, Sol 6.1/high bewertet gesammelte Fallgruppen.
Die internen Workflow-Reviews bleiben Bestandteil echter Funktionsdurchläufe.
Native Handles, Steuerung, Stop/Resume, Übergaben, Berichte und tatsächliche
Dateiergebnisse müssen beobachtet werden. Modellfreie Fehlerprüfungen bleiben
von nativen Wirkungsnachweisen getrennt. Das Zählen bleibt in einem Ledger;
neue Modell-/Hostverträge vermischen keine alten Abnahmeergebnisse.

## Confirmation

Eine vollständige Abdeckungsmatrix verbindet Workflow-Verträge mit Prüfungen,
nativen Spuren und Ergebnissen. Kein erforderlicher ungeprüfter Weg wird als
bestanden gemeldet. Suite-Anteil höchstens 300, zusätzlicher Workflow-Anteil
höchstens 100, Gesamtverbrauch höchstens 400. Keine Installation oder
Veröffentlichung; ADR-0151 bleibt die begrenzte CI-Push-Freigabe.

## Revisit when

Der vollständige Testumfang, ein erforderlicher Host oder die verbleibenden
Versuche eine erfüllte Abnahme verhindern.
