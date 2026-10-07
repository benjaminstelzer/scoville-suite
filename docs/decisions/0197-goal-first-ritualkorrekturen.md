---
format_version: 1
id: ADR-0197
status: accepted
created: 2026-10-06
accepted: 2026-10-06
scope: suite/goal-first-skill-fixes
---

# Ritualkorrekturen in PLAN-0036 aufnehmen

## Decision

Der Nutzer verlangt ausdrücklich, das Goodhart-Problem in den Skills zu
beheben: Goal und Entwicklung bleiben das Ziel, Tests und Buchführung dienen
diesem Ergebnis. Seine Anweisung „ziehe das mit in PLAN 0036 als fixes“
autorisiert den zusätzlichen eigenständigen Fixpunkt W-002.

## Problem

Vorhandene Regeln begrenzen Wiederholungen bereits. Im laufenden Auftrag
haben dennoch Nachweisverwaltung, erneute Bestätigungen und viele kleine
Profiländerungen den Entwicklungsfortschritt verdrängt. Neue Zählziele oder
weitere Prüfphasen lösen diesen Fehler nicht.

## Drivers

Konkrete Skill-Anleitung für Entwicklung zuerst, gebündelte Nachweise und
Wiederverwendung gültiger Ergebnisse. Die externe Statistik bleibt eine
externe Beobachtung, keine hier verifizierte Messung.

## Considered alternatives

Nur das Verhalten dieses Agents ändern: erfüllt die geforderte dauerhafte
Skill-Korrektur nicht. Alle Tests abschaffen oder ein Zeitverhältnis vorgeben:
verletzt notwendige Nachweise oder schafft eine neue Ersatzmetrik.

## Consequences

W-002 hat wegen der ausdrücklich betonten Priorität Vorrang vor weiteren
Recovery-Tests. W-001 pausiert mit erhaltenem Stand und wird danach fortgesetzt.
Astra/high prüft die konkreten Vorschläge vor Source-Änderungen. Sol6.1/high
prüft den abgeschlossenen Fixblock. Notwendige Nachtests korrigierter Fehler,
300 gemeinsame Luna/high-Reservierungen und Freigabegrenzen bleiben verbindlich.
Kein Source-Push, keine Veröffentlichung, Installation oder lokale Rust-Builds.

## Confirmation

An kanonischen Skill-Ownern kleine konkrete Regeln ändern. Gültige Nachweise
wiederverwenden und nur betroffene Anforderungen prüfen. Ein aktueller Bericht
je Work Item, vollständige Rohdaten bei Bedarf separat. Keine neue Zählstudie,
keine Review-Kette allein zum Bestätigen eines bereits bestandenen Reviews.

## Revisit when

Ein konkreter unverifizierter Vertragsbruch oder eine neue Nutzeranforderung
einen weiteren Test oder eine geänderte Freigabe erfordert.
