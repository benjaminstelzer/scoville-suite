---
format_version: 1
id: ADR-0013
status: accepted
created: 2026-09-24
accepted: 2026-09-24
scope: suite/build-profiles
---

# Allgemeine Suite und Codex-Suite aus gemeinsamen Quellen

## Decision

Eine gemeinsame Entwicklungsgrundlage erzeugt die allgemeine Scoville Suite mit Buildprofil `general` und Scoville Suite for Codex mit Buildprofil `codex`. Nur die Codex-Suite enthält Workflow und später den zusammengeführten Scoville Ask. Beide werden ausschließlich als Suite-Bestandteile angeboten.

## Problem

Die portable Ausgabe benötigt Ersatzwege ohne Python, während Codex-Aufträge mit verpflichtenden Helpern ohne diese zusätzlichen Anweisungen auskommen sollen.

## Drivers

- Gemeinsame Fachregeln werden einmal gepflegt.
- Die allgemeine Ausgabe enthält bedingt geladene Python-Fallbacks.
- Die Codex-Ausgabe enthält keine Python-Fallback-Anweisungen oder entsprechenden Laufzeitdateien.
- Fehlerdiagnosen, Autorisierungsgrenzen und fachliche Prüfungen bleiben erhalten.

## Considered alternatives

- Zwei unabhängig gepflegte Kopien: einfache Trennung, aber doppelte Pflege und mögliche Abweichungen gemeinsamer Regeln.
- Gemeinsame Quellen mit expliziten Buildprofilen: Änderungen bleiben zentral, der Builder muss Text, Mitgliedschaft, Dateien und Export zusammenhängend auswählen.

## Consequences

- `../shared/build/build_suite.py` und `export_suite.py` erhalten dieselbe Profilauswahl. Die bestehenden Sichtbarkeits- und Veröffentlichungsgates gelten zusätzlich.
- Bedingte Includes erzeugen vollständige Anweisungen. Reine Fallback-Blöcke können in `codex` leer entfallen. Abweichende Voraussetzungen benötigen passende Ersatztexte.
- Manifest und Buildnachweis bestimmen pro Profil Mitglieder, Dateien, README-Bausteine, Familienlisten und Quellen. Der Export darf nicht ungefiltert alle versionierten Quellen übernehmen.
- Gemeinsame Helper und Regeln werden beim Build in die benötigten Pakete kopiert. Installierte Skills importieren keine Geschwister oder Entwicklungsverzeichnisse.
- Zuerst werden Plan und Workflow korrigiert. Danach werden beide Suite-Ausgaben und ihre Dokumentation fertiggestellt und geprüft. Erst wenn alle Nicht-Ask-Implementierungs- und Prüfpunkte abgeschlossen sind, werden die Korrekturen und die reine Codex-Suite zunächst ohne den neuen Ask veröffentlicht. Erst nach beiden belegten Veröffentlichungen beginnt der Ask-Umbau gemäß ADR-0012. Die allgemeine Ausgabe bleibt Bestandteil der gemeinsamen Buildprüfung.
- Vorhandene Repositories, Releases, Installationen und andere Einzel-Distributionen werden nicht durch diese Entscheidung gelöscht oder umgestellt.

## Confirmation

1. Baue beide Profile aus demselben Quellenstand und prüfe reproduzierbare Dateibestände und Hashes.
2. Prüfe, dass Workflow und nach seiner späteren Integration Ask ausschließlich in `codex` enthalten sind, dort keine Python-Ersatzrouten bestehen und `general` nur bei fehlendem Python auf die vorgesehenen Referenzen verweist.
3. Prüfe erzeugte Dokumentation, lokale Links, isolierte Paketnutzung und profilgerechten Suite-Export.

## Revisit when

Ein weiterer Host eine eigene technische Ausführung benötigt oder die gemeinsame Quelle echte fachliche Unterschiede zwischen den Ausgaben nicht mehr abbildet.
