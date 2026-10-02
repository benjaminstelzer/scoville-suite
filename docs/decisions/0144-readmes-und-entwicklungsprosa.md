---
format_version: 1
id: ADR-0144
status: accepted
created: 2026-10-02
accepted: 2026-10-02
scope: suite/public-copy
---

# Leserorientierte READMEs und Entwicklungsprosa

## Decision

Der Nutzer verlangt kurze, vollständige READMEs in seiner Stimme mit dezentem,
leicht sarkastischem Humor. Nutzen steht im Mittelpunkt, relevante Grenzen
werden dazu eingeordnet. Jede Suite und jeder Skill erklärt den Namen Scoville
kurz. Flowcharts bleiben erhalten. Die Gesamttexte werden auf Lesefluss,
gedankliche Anschlüsse und Wiederholungen geprüft, nicht nur ihre Fragmente.

Entwicklungstexte erklären als knappe Prosa Rückschläge, hilfreiche Änderungen
und übertragbare Erkenntnisse. Interne Zeitstempel, Laufzahlen und Testtagebücher
gehören nicht in diese Erzählung. Changelogs behalten relevante Nutzeränderungen.

## Problem

Interne Verfahren und wiederholte Details verdecken den Nutzen für GitHub-Leser.

## Drivers

- Expliziter Nutzerauftrag einschließlich dauerhafter Regeln im GitHub-Skill.
- Erhaltene Fakten, Flowcharts, Installationsanforderungen und relevante Grenzen.

## Considered alternatives

- Nur Fragmente kürzen: erkennt Brüche und Wiederholungen im Gesamttext nicht.
- TL;DR voranstellen: lässt den ausschweifenden Haupttext unverändert.

## Consequences

Kanonische Fragmente und Vorlagen bleiben die einzige Textquelle. Erforderliche
historische Nachweise bleiben bei ihren Besitzern und werden nicht als
Entwicklungserzählung wiederholt. Die persönlichen Skills erhalten die
Schreibpräferenz und die genehmigte Bereinigung veralteter Suite-Regeln.

## Confirmation

Generierte READMEs vollständig lesen, Flowcharts mit dem Ausgangstext vergleichen
und beide Profile bauen. Paket- und Releaseprüfungen bleiben erforderlich.

## Revisit when

Zielgruppe, Produktumfang oder ausdrücklich gewünschter Ton ändern sich.
