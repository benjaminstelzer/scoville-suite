---
format_version: 1
id: ADR-0009
status: accepted
created: 2026-09-22
accepted: 2026-09-22
scope: suite/publication
---

# Vollständiger Release mit Workflow als Beta

## Decision

Der Nutzer autorisiert die Veröffentlichung beider Suites und ihrer Einzelpakete. Workflow bleibt ausschließlich in Scoville Suite und wird als Beta gekennzeichnet. Die Kennzeichnung ist zentral entfernbar, ohne Skill-Namen oder Installationspfad zu ändern.

## Problem

Die bisherigen Quellen sperren den privaten Workflow für öffentliche Builds.

## Drivers

- Vollständiger GitHub Release einschließlich des Workflows.
- Beta bleibt sichtbar, bis die Version getestet und die Kennzeichnung zur Entfernung freigegeben ist.

## Considered alternatives

- Zentraler README-Baustein: entfernt die Kennzeichnung bei Neubuilds ohne Identitätswechsel.
- Beta im Skill-Namen: würde spätere Umbenennung und geänderte Installationspfade verlangen.

## Consequences

- Öffentliche Freigabe ersetzt die bisherige Sichtbarkeitssperre, nicht die Test- und Asset-Gates.
- Das bestehende private Alt-Repository wird nicht als Workflow-Releaseziel verwendet.
- Historische Git-Tags werden nicht zur Entfernung des Beta-Hinweises umgeschrieben.

## Confirmation

1. Suite und Workflow-README zeigen denselben zentral gepflegten Beta-Hinweis.
2. Ein Neubuild mit leerem Hinweis entfernt ihn ohne Laufzeitänderung.
3. Remote-Pakete, Versionen und Plan-Viewer-Assets sind vor Releaseabschluss verifiziert.

## Revisit when

Der Nutzer gibt nach den Tests die stabile Kennzeichnung frei.
