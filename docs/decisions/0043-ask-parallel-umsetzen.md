---
format_version: 1
id: ADR-0043
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: ask/implementation-order
---

# ASK unabhängig vom UI-Update umsetzen

## Decision

Der Nutzer beauftragt die ASK-Zusammenführung und ihre Tests jetzt parallel zum UI-Update. Für PLAN-0002/W-001 und W-002 ersetzt dies den Wartepunkt aus ADR-0016 und die Release-Voraussetzung aus ADR-0013. Die bestehende UI-Planroute bleibt unverändert.

Die Quelle liegt unter `members/scoville-ask-for-codex/`. Tests führt ein Subagent mit angefordertem `gpt-6-sol` und `medium` aus. README, Requirements und Installation verwenden die bestehenden Shared-Blöcke und kanonischen Fragmente. Nach vollständiger Übernahme und bestandenen Prüfungen darf der alte Ordner `../ask-suite-for-codex` entfernt werden; Git-Historie und lokale Änderungen werden zuvor gesichert.

## Problem

Die bisherige Reihenfolge verhindert die nun ausdrücklich gewünschte unabhängige ASK-Arbeit.

## Drivers

- Das UI-Update läuft parallel und behält seine Änderungen sowie seinen Planstatus.
- Der Nutzer bestätigt Zielpfad, Testmodell, Shared-Dokumentation und anschließende Entfernung der alten Quelle.

## Considered alternatives

- Auf den UI-Release warten: entspricht der bisherigen Reihenfolge, widerspricht dem aktuellen Auftrag.
- ASK unabhängig bearbeiten und gemeinsame Dateien vor jeder Änderung abgleichen: ermöglicht parallele Arbeit bei expliziter Integrationsprüfung.

## Consequences

- Die ASK-Punkte bleiben im bestehenden Plan; keine zweite aktive Root-Planroute wird angelegt.
- Tests berichten Simulationen, tatsächliche Provideraufrufe und verbleibende Lücken getrennt.
- Der Auftrag umfasst lokale Umsetzung und Tests, keine neue Veröffentlichung oder Installation.

## Confirmation

1. Prüfe ASK-Verhalten durch den beauftragten SOL-6-Medium-Subagenten und dokumentiere konkrete Nachweise.
2. Prüfe die Integration ohne Überschreiben fremder Änderungen und vor Entfernung des alten Ordners dessen Sicherung und verbleibende Verbraucher.

## Revisit when

Parallele Änderungen dieselben Verträge betreffen oder der Nutzer den Umsetzungsumfang ändert.
