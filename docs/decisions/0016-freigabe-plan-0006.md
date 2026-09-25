---
format_version: 1
id: ADR-0016
status: accepted
created: 2026-09-24
accepted: 2026-09-24
scope: suite/implementation-order
---

# PLAN-0006 ist abgenommen und zur Umsetzung beauftragt

## Decision

Der Nutzer hat PLAN-0006 inhaltlich abgenommen und seine Umsetzung einschließlich der vorgesehenen Prüfungen beauftragt. Eine erneute grundsätzliche Freigabe ist nicht erforderlich.

Die Reihenfolge ist verbindlich: nach PLAN-0002/W-009 zunächst PLAN-0006 vollständig ausführen, anschließend PLAN-0002/W-010 und W-011. Vor PLAN-0002/W-001 stoppen. Ask-Entwicklung und -Integration in W-001/W-002 benötigen einen späteren ausdrücklichen Auftrag.

## Problem

Das native Planformat unterscheidet keinen freigegebenen wartenden Plan von einem noch nicht abgenommenen Entwurf.

## Drivers

- PLAN-0006 ist ein verbindlicher Umsetzungsauftrag und kein offener Vorschlag.
- Laufende Arbeit wird durch die Dokumentation der Freigabe nicht unterbrochen.
- Die Ask Suite wird erst später entwickelt.

## Considered alternatives

- PLAN-0002 und PLAN-0006 gleichzeitig active setzen: widerspricht dem einzelnen aktiven Plan im bestehenden Format.
- Freigabe durch eine angenommene Entscheidung dokumentieren: bewahrt das Format und macht die Autorisierung für jeden betroffenen Arbeitspunkt erreichbar.

## Consequences

- Der technische Status draft bedeutete bei PLAN-0006 bis zur Aktivierung nur wartend. Die Freigabe ist durch diese Entscheidung erteilt.
- PLAN-0002 bleibt vorübergehend draft mit W-010 als Rückkehrpunkt. Nach PLAN-0006 wird er bei W-010 reaktiviert. Es bleibt jeweils genau ein Plan active.
- Acceptance, Ressourcen- und Evidenzanforderungen von PLAN-0006 bleiben verbindlich. Fehlende notwendige Ressourcen oder menschliche Bewertungen werden konkret gemeldet und nicht durch erfundene Nachweise ersetzt.
- W-010 beginnt erst nach Abschluss von PLAN-0006. Die geltenden Releasegates müssen die endgültigen betroffenen Paketbytes abdecken. Diese Entscheidung ordnet kein zusätzliches Astra-Review gegen einen bestehenden Nutzerstopp an.
- Nach W-011 bleiben die Ask-Punkte todo. PLAN-0002 wird wegen der verbleibenden Arbeit nicht als completed markiert. Veröffentlichung und Installation erhalten keine über die bestehenden Aufträge hinausgehende Freigabe.

## Confirmation

1. Prüfe die Verknüpfung dieser Entscheidung mit allen Arbeitspunkten von PLAN-0006 sowie den betroffenen Release- und Ask-Punkten in PLAN-0002.
2. Prüfe vor W-010 die vollständigen Abschlussnachweise von PLAN-0006 und die Gültigkeit der betroffenen Releaseprüfungen.
3. Dokumentiere nach W-011 den Stopp vor W-001 und validiere den nativen Planstatus ohne erfundene Fertigstellung.

## Revisit when

Der Nutzer ändert Umfang, Reihenfolge oder den Stopp vor der Ask-Entwicklung.
