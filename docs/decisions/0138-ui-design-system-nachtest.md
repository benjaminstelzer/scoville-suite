---
format_version: 1
id: ADR-0138
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: ui/design-system-tests
---

# Vorgegebenes Design-System unabhängig prüfen

## Decision

Nach dem abgeschlossenen Release folgen serielle UI-Audits im gespeicherten
Projekt test. Luna Medium erhält das beschriebene oder anhand seiner Quellen
erkennbare Design-System und die Vorlage, jedoch keine Fehlerliste. Astra
Medium analysiert anschließend tatsächliche Fehlbefunde und Skill-Regeln.
Belegte Skill-Lücken werden gezielt korrigiert und unabhängig nachgetestet.

## Problem

Eine plausibel aussehende Vorlage oder ein bestandenes Overflow-Prüfen belegt
keine Einhaltung vorgegebener Abstände, semantischer Schrift- und Farbrollen.

## Drivers

- Nutzer-Vorgabe: 4px-Raster, Boxabstand 8px, Innenabstand 4px.
- Definierte Schriftrollen und Palette, einschließlich kleiner Farbabweichungen.
- WordPress-Backend prüft den zuständigen nativen WordPress-Owner.
- Design-System liegt offen; nur gezielte Fehler und Auswertung bleiben verborgen.
- Lokale Skill-Updates den bestehenden Fluid-Base- und EMPCO-Workflows mitteilen.

## Considered alternatives

- Nur optische Stimmigkeit bewerten: prüft die vorgegebenen Rollen nicht.
- Eine allgemeine 4px-Regel im Skill: überschreibt andere Design-Systeme.

## Consequences

Fixture und Sollwerte entstehen vor dem Audit. Korrekte Rollen, Varianten und
Ausnahmen dienen als Gegenprobe. Audits bleiben read-only. Keine Reparatur des
Testprodukts, keine neue GitHub-Veröffentlichung durch diesen Nachtest allein.
Tests und Analyse erfolgen seriell mit wenigen notwendigen Agenten. Astra
Medium ist die ausdrücklich gewählte Analyse, nicht ein Luna-Testexecutor.

## Confirmation

Tatsächliche Referenzlektüre, Quellzuordnung, Computed Styles, gemessene
Beziehungen und betrachtete Renders mit unabhängiger Fehlerliste vergleichen.
Übersehene Fehler, falsche Befunde und offene Messgrenzen getrennt erhalten.
Nach einer Korrektur frischer Lauf und andere Verletzungsstellen.

## Revisit when

Der Test keine eindeutigen Owner oder reproduzierbaren Sollwerte bereitstellt.
