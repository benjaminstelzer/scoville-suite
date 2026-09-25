---
format_version: 1
id: ADR-0067
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/reasoning
---

# Reguläre Reasoning-Auswahl und manuelle Zusatzwerte

## Decision

Die regulären Reasoning-Stufen sind low/medium/high/xhigh. Setup setzt nur diese vier. Manuelle Konfiguration und ausdrücklich gewünschte Plan-Annotationen dürfen zusätzlich none/minimal/max/ultra verwenden sofern das Modell sie unterstützt. Setup erhält manuelle Zusatzwerte bei anderen Änderungen.

## Problem

Plan und Ausführung hatten unterschiedliche Wertelisten; alle syntaktisch gültigen Stufen sollen lesbar bleiben ohne seltene Stufen in Setup anzubieten.

## Drivers

- Der Nutzer erlaubt low für minimale Änderungen.
- Zusätzliche Stufen erfordern eine bewusste manuelle Vorgabe.
- Plan wählt selbst keine Modelle oder Reasoning-Stufen.

## Considered alternatives

- Alle Stufen in Setup anbieten: vom Nutzer verworfen.
- Zusätzliche Stufen vollständig ablehnen: verhindert gewünschte manuelle Konfiguration.

## Consequences

Die Leser behalten alle acht Syntaxwerte. Workflow verwendet konfigurierte Paare und prüft die Modellunterstützung. Setup begrenzt nur seine angeforderten Änderungen statt vorhandene manuelle Werte zu überschreiben. Keine zusätzliche Konfigurationsebene. Das Plan-README erklärt explizite Step-Annotationen und reguläre Stufen.

## Confirmation

Prüfe alle acht Werte durch Selector und Resolver sowie die Modellprüfung. Prüfe Setup-Schreibgrenze und Erhalt manueller Werte. Plan-README zeigt reasoning allein und zusammen mit model.

## Revisit when

Der Nutzer die reguläre Auswahl ändert.
