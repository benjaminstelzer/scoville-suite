---
format_version: 1
id: ADR-0121
status: accepted
created: 2026-09-30
accepted: 2026-09-30
scope: workflow/model-defaults
supersedes: ADR-0082
---

# Bestätigte Workflow-Modellpaare verwenden

## Decision

Die aktuelle Zuordnung gilt als Workflow-Default. Der Nutzer hat medium und
ultra_high ausdrücklich korrigiert:

| Risiko | Ausführung | Effort | Review | Effort |
| --- | --- | --- | --- | --- |
| ultra_low | gpt-6-luna | medium | gpt-6.1-sol | low |
| low | gpt-6-luna | high | gpt-6.1-sol | medium |
| medium | gpt-6.1-sol | medium | gpt-6-astra | medium |
| high | gpt-6.1-sol | high | gpt-6-astra | high |
| ultra_high | gpt-6.1-sol | xhigh | gpt-6-astra | xhigh |

Projektüberschreibungen bleiben erhalten. Ask-SOL bleibt gpt-5.6-sol/high.
Manager nutzen das geerbte oder ausdrücklich gewählte Paar. Die zurückgezogene
Anweisung zur restlosen Entfernung von Workflow-Pinning wird nicht umgesetzt.
Legacy-Werte bleiben lesbar und haben auf native Agenten keine Wirkung.

## Problem

ADR-0082 dokumentiert frühere Paare und würde die neue Konfiguration falsch
erklären.

## Drivers

- Ausdrückliche Korrektur der beiden Risikorouten durch den Nutzer.
- Defaults, Konfiguration und Paketprojektionen müssen übereinstimmen.

## Considered alternatives

- Frühere Paare beibehalten: widerspricht der aktuellen Zuordnung.

## Consequences

Neue Dispatches verwenden die aufgelösten Paare. Host-Ablehnung wird gemeldet,
ohne stilles Ersatzmodell. Diese Änderung beweist keine reale Abnahme jedes
Modellpaars.

## Confirmation

Aufgelöste Defaults, Overrides und Build-Ausgaben vergleichen und die
Workflow- sowie Setup-Tests ausführen.

## Revisit when

Der Nutzer neue Paare festlegt oder der Host eine Route ablehnt.
