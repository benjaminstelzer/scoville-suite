---
format_version: 1
id: ADR-0125
status: accepted
created: 2026-09-30
accepted: 2026-09-30
scope: workflow/runner-skills
---

# Zusätzliche Skill-Nutzung im Runner begrenzen

## Decision

Der Nutzer verlangt eine Schutzregel in der Runner-Rolle von Scoville Code.
Während eines aktiven Workflows nutzt der Runner nur den Scoville-Kern und
Planer. Die vorläufig konkretisierte Liste ist Code, Workflow und Plan.
Zusätzliche Skills und Code-Implementierungs-, Review- oder Prüfrouten bleiben
dem Runner gesperrt. Die vorhandene Planarbeit bleibt beim Manager.
Eine Rückfrage zur genauen Liste ist gestellt. Die übrige Schutzregel ist
ausdrücklich beauftragt und braucht keine erneute Freigabe.

## Problem

Eine Zwischenfrage kann den Runner zu einer zusätzlichen Skill-Aktivierung und
fachlicher Arbeit außerhalb seiner Koordinationsrolle verleiten.

## Drivers

- Explizite Ergänzung während der laufenden Luna-Abnahme.
- Rollenbegrenzung ohne Einschränkung der Implementierungsrollen.

## Considered alternatives

- Alle Rollen begrenzen: würde erforderliche Worker- und Reviewer-Skills sperren.

## Consequences

Die Regel steht im Codex-Profil von Code und gilt auch über Pause, Wiederaufnahme
und Managerwechsel. Erlaubnis für Plan erweitert keine Runner-Befugnis auf
Planinhalte oder Managerarbeit. Der laufende Test erhält die neue Vorgabe als
Steuerung. Seine bereits kopierten Pakete bleiben unverändert. Eine neue
Abnahme muss die aktualisierte gebaute Code-Regel direkt verwenden.

## Confirmation

Code-Projektionen und tatsächlichen Runner-Verbrauch prüfen. Statusfragen
dürfen keinen weiteren Skill aktivieren. Den ersten Lauf mit älterem Paket
und die spätere aktualisierte Abnahme getrennt ausweisen.

## Revisit when

Der Nutzer die erlaubte Liste präzisiert oder eine andere Runner-Rolle verlangt.
