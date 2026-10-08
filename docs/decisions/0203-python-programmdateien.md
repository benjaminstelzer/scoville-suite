---
format_version: 1
id: ADR-0203
status: accepted
created: 2026-10-08
accepted: 2026-10-08
scope: suite/document-reading
---

# Nur .py-Dateien als Python-Programmdateien starten

## Decision

Als Python-Programmdatei darf nur eine Datei mit Endung .py gestartet werden. Dokumentpfade werden dem Reader als Eingabe übergeben, beispielsweise hinter --file. Diese Regel betrifft Dateiargumente, nicht andere Python-Aufrufarten wie -c oder -m.

## Problem

Agenten starteten wiederholt Markdown-Anleitungen direkt als Python und erhielten SyntaxError.

## Drivers

- Die Unterscheidung zwischen Reader und Dokument muss im Aufruf unmittelbar erkennbar sein.

## Considered alternatives

- Nur Markdown ausschließen: andere Dokumenttypen bleiben verwechselbar.
- .py als Programmdatei verlangen: benennt die zulässige Rolle positiv.

## Consequences

Gemeinsame Anweisungen und Vorlagen unterscheiden festen Helperpfad und austauschbaren Dokumentpfad. Diese Klarstellung verlangt keinen allgemeinen Befehlsparser.

## Confirmation

Reader-Aufrufe mit Dokumentpfaden, Leerzeichen und Unicode unter Windows und Linux prüfen.

## Revisit when

Ein benötigter dateibasierter Python-Aufruf kann diese Endungsregel nachweislich nicht erfüllen.

