---
format_version: 1
id: ADR-0200
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/path-audit
---

# Verwendete Pfade der ausgelieferten Skills prüfen

## Decision

Der Nutzer begrenzt W-017 auf die öffentlich ausgelieferten Skill-Dateien und
die darin verwendeten Pfade. Dazu gehören Anleitungen, Referenzen, Assets,
Runtime-Helper und deren Imports. Interne Build-, Test- und Nachweisdateien
gehören nicht zur Prüfung. Die Fehlerdiagnose-Prüfung betrifft ausgelieferte
Helper. Vorhandene technische Build-Nachweise werden weiterverwendet.

## Problem

Die erste Erfassung schloss ganze Suite-, Shared- und Paketbäume ein und war
damit breiter als der beauftragte abschließende Skill-Pfadcheck.

## Drivers

- Direkte Nutzerpräzisierung: nur später öffentliche, von Skills verwendete Pfade.
- Maschinelle Fundliste vor Agentenprüfung beibehalten, unnötige Arbeit entfernen.

## Considered alternatives

- Gesamte Repository-Bäume prüfen: umfasst interne Artefakte außerhalb des Auftrags.
- Ausgelieferte Skill-Bäume prüfen: erfasst die tatsächlich benötigten Pfade.

## Consequences

Die vorhandene Erfassung wird anhand der vier Paketvarianten und ihrer
Manifest-Besitzer gefiltert. Identische Dateiinhalte dürfen gemeinsam geprüft
werden; ihre Paketpositionen bleiben erhalten. Abweichende Inhalte und
General-/Codex-Profilgrenzen bleiben getrennt. Die frühere breite W-017-Fassung
bleibt in dessen Nachweis als überholter Umfang festgehalten.

## Confirmation

Die Prüfliste enthält nur ausgelieferte Skill-Dateien mit kanonischem Besitzer.
Agenten verfolgen ihre Pfade, Imports und Fehlerbehandlung zum Verbraucher.
Bestätigte Fehler werden korrigiert und gezielt unter den betroffenen OS-Wegen
nachgetestet. Eine Fundstelle allein ist kein Fehler- oder Erfolgsnachweis.

## Revisit when

Der Nutzer beauftragt eine zusätzliche Prüfung interner Build- oder Testpfade.
