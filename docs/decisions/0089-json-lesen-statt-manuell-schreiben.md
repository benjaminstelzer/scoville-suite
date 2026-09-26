---
format_version: 1
id: ADR-0089
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/uebergabeformat
supersedes: ADR-0088
---

# JSON darf gelesen und automatisch erzeugt werden

## Decision

Agenten dürfen JSON aus Helpern lesen und Konfiguration als JSON verwenden. Sie dürfen nicht gezwungen werden, korrektes JSON als Freitext für Übergaben oder Helper-Anfragen zu schreiben. Klartext, Helper-Erzeugung, native strukturierte Argumente und automatische Serialisierung sind zulässig. Technische Parameter und die JSON-Schnittstelle von Ask Claude bleiben erhalten.

## Problem

Die bisherige Regel beschränkte das Ausgabeformat stärker als vom Nutzer beabsichtigt. Fehler entstanden beim manuellen Schreiben von JSON, nicht beim Lesen.

## Drivers

- Explizite Nutzerpräzisierung am 2026-09-26.

## Considered alternatives

- JSON-Rückgaben allgemein verbieten: unnötige Schnittstellenänderungen.

## Consequences

Der bereits korrigierte Klartext-Dispatch bleibt zulässig. Helper- und Konfigurationsdaten benötigen keine Formatumstellung. Beispiele müssen JSON-Anfragen automatisch erzeugen oder einen vollständigen Helper-Aufruf anbieten.

## Confirmation

Geänderte Aufrufbeispiele und Modelltests verlangen keine manuell geschriebenen JSON-Übergaben; Rückgaben werden ohne Reparatur verwendet.

## Revisit when

Eine dokumentierte Anfrage nur durch manuelles JSON-Schreiben ausführbar ist.
