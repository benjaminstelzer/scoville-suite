---
format_version: 1
id: ADR-0187
status: superseded
created: 2026-10-05
accepted: 2026-10-05
scope: suite/helper-evaluation
supersedes: ADR-0185
superseded_by: ADR-0192
---

# Restnachweise innerhalb einer neuen Gesamtgrenze

## Decision

Der Nutzer bestaetigt mit "Ja" auf die konkrete Budgetfrage die Gesamtobergrenze von 120 gpt-6-luna/high-Versuchen fuer PLAN-0035. Dasselbe Register und alle 81 bisherigen Versuche erhalten. Die Budgetaufteilung ist Kapazitaet, kein Verbrauchsziel oder Wirksamkeitsnachweis.

## Problem

19 Versuche sind frei. Die noch ausgewaehlten UI- und Ask-Funktionsgruppen brauchen je drei Aufrufer, die drei Workflow-Scope-Proben neun Luna-Rollen und der korrigierte Code-Standalone-Kandidat drei Laeufe: zusammen 18, ohne gemischte Urteile oder weitere Skill-Korrektur. Fuer die zusaetzlichen vollstaendigen 15/15-, Recovery-, Blocker- und Warteproben bliebe ein Versuch. Ein vollstaendiger Ablauf braucht mehrere reale Rollen; seine konkrete Host- und Rollenqualifikation ist noch offen. Das bisherige 12-Rollen-Kontingent war Kapazitaet, kein bereits ausfuehrbarer Nachweisplan.

## Drivers

Der Nutzer verlangt vollstaendige Skill-Nachweise, gezielte Nachtests jedes Fixes, gebuendelte Sol-Reviews und ein verbindliches Gesamtlimit. Wiederholungen dienen dem erhaltenen Testvertrag, nicht einem Verbrauchsziel.

## Considered alternatives

100 erhalten: die verbleibenden Versuche priorisieren, erforderliche fehlende Abnahmen offen halten und PLAN-0035 nicht als abgeschlossen melden.

120 erlauben: geplante Restgruppen und notwendige Korrekturreserve abdecken. Eine bestandene Abnahme wird dadurch nicht zugesichert.

## Consequences

Budgetentwurf: 81 verbraucht, Code-Standalone 3, UI 3, Ask 3, Workflow-Scope 9, vollstaendiger Workflow hoechstens 12 Rollen Kapazitaet, Restreserve 9. Konkrete Rollen und echte Isolation vor nativen Starts qualifizieren. Frische Luna-Kinder vorab zaehlen. Keine Erwartungen, Wiederholungsregeln, Rollen oder Freigabegrenzen abschwaechen. Sol-Reviews sind keine Luna-Versuche. Keine Installation oder Veroeffentlichung.

## Confirmation

Nach ausdruecklicher Annahme dieselbe Budgetdatei und ihre zulassende Validierung gezielt aktualisieren und den harten Stopp nachtesten. Alle bisherigen Eintraege erhalten. Pflichtnachweise und offene Grenzen weiterhin getrennt belegen.

## Revisit when

Neue gemischte Urteile, Skill-Korrekturen oder die konkrete native Qualifikation den genehmigten Bedarf erneut ueberschreiten.
