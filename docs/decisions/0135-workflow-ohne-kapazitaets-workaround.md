---
format_version: 1
id: ADR-0135
status: accepted
created: 2026-10-01
accepted: 2026-10-01
scope: workflow/agent-capacity
supersedes: ADR-0126
---

# Automatische Kapazitätsbereinigung entfernen

## Decision

Der Nutzer beauftragt im Chat „Prüfe den followup_task Trick“ die vollständige
Entfernung des automatischen Drain-/Recovery-/Retry-Wegs. Die weitergegebene
Anweisung wurde am tatsächlichen Nutzerauftrag dieses Chats geprüft.
Workflow entfernt seine Recovery-Protokollzustände, Rollenadapter und nur
dafür benötigten Regeln. Kapazitätsfehler bleiben mit Diagnose, tatsächlichem
Blocker und gesichertem Fortsetzungsstand sichtbar. Keine automatischen
Ersatzchats oder versuchsweise geweckten abgeschlossenen Agenten.

Die verifizierte Übergabe mit Empfang vor Vorgängerabschluss bleibt erhalten.
Notwendige Rückfragen und Fortsetzung desselben unerledigten Auftrags verwenden
weiterhin den exakten Handle. Keine Routinequittung nach nativem Abschluss.
Bei unklarem Zustand vor notwendigem send_message einmal prüfen; die Race
zwischen Prüfung und Zustellung bleibt möglich, ohne neue Pollingmechanik.

Der Nutzer verlangt außerdem den README-Hinweis und das lokale Codex-Limit 256.
Das betrifft agents.max_concurrent_threads_per_session, dessen alter Alias
max_threads ist. Modelle, Efforts und serielle Testausführung bleiben erhalten.

## Problem

Eine generische Kapazitätsablehnung identifiziert keine wartende Mailbox.
Ein erneuter Final beweist keine Kapazitätsfreigabe. Die recherchierten
Fehlerberichte zeigen erfolgreiche Spezialfälle und erfolglose Bereinigungen.

## Drivers

- Ausdrückliche Entfernung statt weiteren Reparaturversuchen.
- Ergebnisse, notwendige Folgefragen und echte Übergaben bewahren.
- Keine zusätzliche Turn-/Protokollkomplexität ohne belegte Wiederherstellung.

## Considered alternatives

- Bisheriger begrenzter Retry: unbekannte Fehlerursache und unzuverlässiger Nutzen.

## Consequences

W-002/W-003 und frühere Recovery-Tests bleiben historische Umsetzungsevidenz.
W-014 entfernt das Verhalten. W-006 bewertet danach den neuen Fehlervertrag,
ohne die übrige Akzeptanz zu reduzieren. Ask erhält seine eigene Ersatzentscheidung.
Der bestehende Releaseauftrag dieses Chats bleibt bestehen; die Weitergabe
selbst erteilt keinen zusätzlichen Veröffentlichungsauftrag.

## Confirmation

Keine Recovery-Zustände oder Bereinigungsturns in aktiven Quellen, generierten
Managerprompts oder Paketen. Technische Gates und echte Luna-Medium-Verbraucher
prüfen Diagnose/Blocker, erhaltene Ergebnisse und notwendige Fortsetzung.
Native Hostfehler nur als ausgeführt bezeichnen, wenn tatsächlich beobachtet.

## Revisit when

Der Host bietet einen belegten, vom Nutzer beauftragten Kapazitätsvertrag.

### Sources

- https://github.com/openai/codex/issues/32353
- https://github.com/openai/codex/issues/39694
- https://github.com/openai/codex/issues/44351
