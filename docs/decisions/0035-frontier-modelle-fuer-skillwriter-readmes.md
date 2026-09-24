---
format_version: 1
id: ADR-0035
status: accepted
created: 2026-09-24
accepted: 2026-09-24
scope: suite/skillwriter-release-requirements
---

# Frontier-Modell als Mindestvoraussetzung überarbeiteter Skills

## Decision

Auf Nutzerauftrag müssen alle READMEs von mit Skillwriter überarbeiteten Skills ein Frontier-LLM aus den Familien Fable, Astra, SOL oder Opus ab Version 5.0 voraussetzen.

## Problem

Die vereinfachten Anweisungen setzen leistungsfähige Modelle voraus; diese Voraussetzung muss vor Veröffentlichung sichtbar sein.

## Drivers

- Einheitliche Mindestanforderung für künftige Skillwriter-Überarbeitungen.
- Modellvoraussetzung und tatsächliche Prüfnachweise bleiben getrennt.

## Considered alternatives

- Nur getestete Modelle nennen: dokumentiert Evidenz, ersetzt aber nicht die gewünschte Mindestvoraussetzung.
- Mindestvoraussetzung und separate Testangaben: entspricht dem Nutzerauftrag ohne pauschale Kompatibilitätsbehauptung.

## Consequences

- Kanonische README-Quellen und alle zugehörigen Releaseprojektionen müssen die Voraussetzung enthalten.
- Aktuell betroffen sind Scribe und der eigenständige Skillwriter. Weitere Überarbeitungen erweitern den Umfang.
- Die Anforderung ist kein Nachweis erfolgreicher Läufe auf sämtlichen Modellfamilien und hebt bestehende Releasegates nicht auf.

## Confirmation

1. Scribes Compatibility-Fragment und Skillwriters README ergänzen; Folgepflicht im Skillwriter festhalten.
2. Vor W-010 und W-011 die seit dieser Entscheidung mit Skillwriter überarbeiteten Skills erfassen und sämtliche zugehörigen README-Projektionen prüfen.
3. Releaseevidence nennt die geprüften Dateien und trennt Mindestvoraussetzungen von tatsächlich getesteten Modellen.

## Revisit when

Der Nutzer die Modelluntergrenze ändert oder neue Prüfergebnisse eine andere Voraussetzung begründen.
