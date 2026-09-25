---
format_version: 1
id: ADR-0045
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/simplification
---

# Unnötige Komplexität und Übergabebelege entfernen

## Decision

Der Nutzer beauftragt die Reduktion unnötiger Komplexität und SHA-256-Vorkehrungen bei Übergaben. Vom Modell berechnete, kopierte oder verglichene Hashes, Bytezählungen und doppelte Übergabebelege sollen entfallen. Auch Plan soll deutlich einfacher werden: geordnet schreiben, klare nächste Schritte und zuverlässige Fortschreibung. Jeder Reviewpunkt einschließlich missverständlicher Sprache wird einzeln geprüft. Vorschläge werden nicht blind übernommen.

## Problem

Historisch ergänzte Regeln und Belege erschweren einfache Aufgaben und können von Menschen und Modellen unterschiedlich verstanden werden.

## Drivers

- Einfachheit hat Vorrang vor zusätzlicher Absicherung theoretischer Fälle.
- Erforderliche Ergebnisse, Aufgabenbesitz und klare Fehler bleiben erhalten.

## Considered alternatives

- Bestehende Absicherungen unverändert lassen: widerspricht dem ausdrücklich gewünschten Abbau.
- Sämtliche Mechanismen pauschal entfernen: übersieht mögliche konkret belegte Fehler.
- Je Mechanismus vereinfachen: entfernt Aufwand und erhält nur nachweislich nötige Funktion.

## Consequences

- Direkte Helper-Übergabe ersetzt Modellbelege. Planänderungen verwenden aktuelles Lesen und kontextgebundene Patches ohne Modell-Hashpflicht.
- Eine notwendige Prüfung gehört möglichst in vorhandene Werkzeuge und bleibt aus dem Modellkontext.
- Build-/Release- und Backup-Identität werden nach eigenem Zweck beurteilt, nicht als Übergabezeremonie behandelt.
- Größere Änderungen am Workflow, Planformat oder ausdrücklich offenen Reviewvarianten sind durch diese Richtung nicht automatisch ausgewählt.

## Confirmation

1. Ordne jeden entfernten oder behaltenen Mechanismus einer konkreten Funktion zu.
2. Prüfe die betroffenen normalen Abläufe und belegten Fehlerfälle mit erhaltenem Ergebnis.
3. Prüfe Sprache auf eindeutige Handlung, Voraussetzung und Fehlerfolge; miss Verständlichkeit nicht allein an Textlänge.

## Revisit when

Ein realer Lauf einen verlorenen erforderlichen Schutz oder neue unnötige Komplexität zeigt.
