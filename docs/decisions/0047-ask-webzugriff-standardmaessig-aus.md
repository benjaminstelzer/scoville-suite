---
format_version: 1
id: ADR-0047
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: ask/web-tools
transition_batch: f4ac9627ee1ebc83f5a18c0e13e4603d1b8485d4b1e82bf5fda3951a69d634b4
transition_batch_members: [ADR-0047, ADR-0048, ADR-0049, ADR-0050, ADR-0051]
---

# ASK-Webwerkzeuge nur bei ausdrücklichem Bedarf

## Decision

Empfohlen: claude.web_tools ist standardmäßig false. WebSearch und WebFetch werden nur durch explizite Konfiguration oder Anfrage erlaubt. Read/Grep/Glob bleiben verfügbar.

## Problem

Der aktuelle Reviewkanal erlaubt Lesen lokaler Inhalte und zusätzliche Netzabfragen ohne aufgabenspezifischen Bedarf.

## Drivers

- Zusatzfähigkeiten sollen dem angefragten Review dienen.
- Kein hier nachgewiesener Exploit und keine falsche Offline-Zusage.

## Considered alternatives

- Webwerkzeuge immer erlauben: bequem für Recherche, unnötige Fähigkeit bei lokalen Reviews.
- Expliziter Opt-in: geringerer Standardumfang, Recherche braucht eine bewusste Auswahl.

## Consequences

- README und CLI-Anleitung erklären die Änderung knapp.
- Native Adviser bleiben vertraglich read-only; keine neue Hash-Sandboxsimulation.
- Claude-Modellkommunikation bleibt online. Bash-Git wird nicht zusätzlich freigegeben.

## Confirmation

1. Prüfe Standardbefehl ohne Webwerkzeuge und ausdrücklich aktivierten Befehl mit ihnen.
2. Prüfe Konfigurationsrangfolge und Ablehnung ungültiger Werte.
3. Benenne im Ergebnis fehlende Recherchefähigkeit, falls sie zur Aufgabe nötig ist.

## Revisit when

Regelmäßige reale Reviews ohne Webzugriff ihre beauftragte Aufgabe nicht erfüllen.
