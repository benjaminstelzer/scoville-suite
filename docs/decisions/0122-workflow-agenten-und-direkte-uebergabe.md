---
format_version: 1
id: ADR-0122
status: accepted
created: 2026-09-30
accepted: 2026-09-30
scope: workflow/native-lifecycle
supersedes: ADR-0092
---

# Workflow-Agenten mit direkter Managerübergabe ausliefern

## Decision

Die beauftragte neue Workflow-Version ersetzt native Codex-Rollen-Chats durch
Agenten. Der sichtbare Runner startet einen Manager und prüft dessen exakte
Identität mit READY/START. Der Manager besitzt Planpflege, autorisierte Commits,
Worker und lesende Reviewer. Höchstens ein Worker schreibt im gemeinsamen
Checkout. Der Runner erhält kurze Steuerzustände und notwendige Nutzerfragen.

Die Standardschwellen bleiben Manager ab 40 Prozent und Kinder strikt über
60 Prozent. Der vollständige laufende Auftrag einschließlich fälliger Reviews,
Korrekturen, Checks und Planpflege endet zuerst. Der Manager fordert seinen
Nachfolger bei ruhenden Kindern und Schreibzugriffen an. Dieser erhält vom
Runner nur die Vorgänger-ID als Arbeitskontext und fordert die fachliche
Übergabe direkt an. Er prüft Plan, Dateien und Kinder vor Schreibbeginn.
Kinder geben ihr normales Ergebnis zurück; spätere Aufträge nutzen neue Agenten.

Separate Rollen-Chats und deren Selbstarchivierung entfallen. Vorgänger bleiben
schreibinaktiv und für Rückfragen erreichbar. Review-Grenzen aus ADR-0102
bleiben erhalten, dessen frühere Chat-/Worker-Handoff-Regeln werden für Codex
durch diesen vollständigen Auftragsabschluss ersetzt. Unklare Starts und
Übergaben halten an. Claude-Regeln werden damit nicht geändert.

## Problem

Die früheren Chat- und Archivierungsregeln erklären die integrierte
Runner-Manager-Architektur nicht.

## Drivers

- Ausdrücklicher Auftrag zur Integration der überarbeiteten Workflow-Version.
- Direkte Übergaben, geordnete Planarbeit und ein eindeutiger Schreiber.

## Considered alternatives

- Rollen-Chats weiter bauen: widerspricht der beauftragten Agentenversion.

## Consequences

Die Integration übernimmt geprüfte Quellen, ist aber keine vollständige
Live-Abnahme. Nachprüfungen korrigierter Dispatch-/Statuswege und negativer
Start-/Übernahmefälle bleiben offen. Die geplante Fortschrittsanzeige und
Laufdatei stehen weiterhin in W-005 des isolierten Agenten-Plans und sind
nicht durch diese Integration implementiert.

## Confirmation

Workflow-, Suite- und Shared-Tests, alle Paketvarianten und vorhandene
Live-Nachweise prüfen. Offene Live-Fälle bleiben als solche dokumentiert.

## Revisit when

Der Host kann Identität, sichere Übergabe oder verfügbaren Agentenstart nicht
bestätigen, oder der Nutzer ändert die Architektur.
