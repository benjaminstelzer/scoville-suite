---
format_version: 1
id: ADR-0100
status: accepted
created: 2026-09-27
accepted: 2026-09-27
scope: workflow/release
---

# Geprüfte Skills unabhängig vom D5-Produktnachweis veröffentlichen

## Decision

Der Nutzer hat ausdrücklich bestätigt: Die geprüften Skills werden jetzt lokal und auf GitHub mit neuen Releases veröffentlicht. W-004 bleibt wegen des fehlenden D5-Wirkungsnachweises offen. Der DIVI-Manager erhält die neuen Regeln und führt nur zulässige offene Arbeit fort.

## Problem

PLAN-0018 band den Skill-Release an W-004. D4/D5-Bereinigung und D4-Wirkung sind belegt, der D5-Presetimport scheitert jedoch im Produkt. Der eigene Testzustand wurde erfolgreich wiederhergestellt. SOL, sechs Luna-6-High-Fälle und Astra Medium haben die Skilländerungen geprüft.

## Drivers

- Ausdrückliche Nutzerfreigabe zur getrennten Veröffentlichung.
- Geprüfte Ablaufverbesserungen verfügbar machen, ohne eine offene Produktabnahme als bestanden darzustellen.

## Considered alternatives

- Veröffentlichung bis D5-Abnahme zurückstellen: vom Nutzer verworfen.

## Consequences

W-004 pausiert während der Veröffentlichung. W-005 schließt die Skillprüfung und den überprüften Regelabgleich ab, ohne den D5-Effekt zu behaupten. W-006 übernimmt lokale Installation, Manager-Neuladen, zulässige Wiederaufnahme und Veröffentlichung. Ungeklärte Produktentscheidungen bleiben beim DIVI-Manager und Nutzer.

## Confirmation

Saubere Builds entsprechen den Luna-geprüften Paketbytes. W-006 prüft lokale Dateien, Manager-Reaktion, Remote-Bäume, Releases, Tags und Downloads. W-004 bleibt nach Veröffentlichung offen.

## Revisit when

Der DIVI-Manager liefert den fehlenden D5-Nachweis oder findet eine Regression im geänderten Vertrag.
