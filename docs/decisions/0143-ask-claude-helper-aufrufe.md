---
format_version: 1
id: ADR-0143
status: accepted
created: 2026-10-02
accepted: 2026-10-02
scope: ask/claude-preparation
---

# Claude-Anfragen im Ask-Helper vorbereiten

## Decision

Der Nutzer beauftragt direkte Helper-Aufrufe für Claude-Erstfragen und Follow-ups sowie die Entfernung von list_models.py. ask.py erzeugt ausführbare Request-Dateien aus UTF-8-Fragedateien. Fortsetzungen übernehmen Adviser, Arbeitsverzeichnis und Einstellungen aus dem gespeicherten Request und verlangen die exakte Session-ID. Explizite Modell-, Effort-, Web-, Timeout- und Budget-Overrides bleiben möglich. Die JSON-Schnittstelle bleibt erhalten. Ask bleibt Codex-only mit Python-Pflicht ohne manuellen Fallback.

## Problem

Das eingebettete Python-Beispiel verlangt wiederholten mechanischen Zusammenbau durch den Agenten. Der ausgelieferte Modellkatalog hat keinen aktiven Aufrufer.

## Drivers

- Ausdrücklicher Umsetzungsauftrag vom 2026-10-02.
- Kopierbare Aufrufe und erhaltene Follow-up-Einstellungen.

## Considered alternatives

- Serializer-Beispiel behalten: zusätzliche Codebearbeitung für jede Beratung.
- Eigenen Helper hinzufügen: unnötiger zweiter Einstieg neben ask.py.

## Consequences

Die Vorbereitung startet keinen Adviser. Die erzeugte Datei geht unverändert an ask.py --input-file. Native Modellverfügbarkeit bleibt beim Host. Build und Veröffentlichung behalten ihre bestehenden Gates.

## Confirmation

Erstaufruf, Follow-up, explizite Overrides, geänderte Projekt-Defaults und korrigierte Fehlerfälle mit gebauten Paketen und tatsächlichem CLI-Prozess prüfen. Testdoubles belegen keinen echten Claude- oder Luna-Lauf.

## Revisit when

Der Claude-Sessionvertrag oder die benötigten Eingaben ändern sich.
