---
format_version: 1
id: ADR-0142
status: accepted
created: 2026-10-02
accepted: 2026-10-02
scope: suite/project-context
---

# Schutzregeln und Formatabnahme von Context Cleanup

## Decision

Der Nutzer genehmigte Variante (b): Bestehende Freigabepflichten und Verbote für
externe Handlungen bleiben mit Bedingungen und Ausnahmen in der Regeldatei,
auch wenn das Verfahren vollständig referenziert oder beauftragt ausgelagert wird.

Das spezifizierte Feld `compatibility` bleibt erhalten. Für die aktuelle und
künftige Formatabnahme dieses Skills gelten `skills-ref validate <skill-folder>`
am unveränderten gebauten Paket und die Suite-Paketprüfung. Skill Creators
`quick_validate.py` wird weiterhin ausgeführt und wahrheitsgemäß berichtet.
Seine isolierte Ablehnung von `compatibility` ist eine dokumentierte Ausnahme,
kein bestandener Check. Andere Fehler sind davon nicht gedeckt.

## Problem

„Directly accessible“ ließ den Speicherort von Schutzregeln offen. Der lokale
Skill-Creator-Validator schließt zudem ein gültiges optionales Formatfeld aus.

## Drivers

- Schutzregeln sollen auch ohne Erkennen des Verfahrensauslösers sichtbar sein.
- Die [Agent-Skills-Spezifikation](https://agentskills.io/specification) erlaubt
  `compatibility` mit 1 bis 500 Zeichen und empfiehlt `skills-ref` zur Validierung.

## Considered alternatives

- Schutzregeln nur hinter einem Verweis: weniger Wiederholung, aber zusätzliche
  Abhängigkeit vom Erkennen und Lesen des Verfahrensauslösers.
- Metadaten entfernen oder den fremden Validator patchen: vermeidbare Änderung
  am gültigen Paket beziehungsweise am nicht hier gepflegten Prüfwerkzeug.

## Consequences

Die notwendige Schutzzeile bleibt bewusst doppelt. Prüfberichte unterscheiden
Referenzvalidierung, Suite-Paketprüfung und beobachtetes Modellverhalten.
`skills-ref` dient nur der Entwicklungsprüfung und wird nicht mit dem Skill
ausgeliefert. Der Hersteller bezeichnet die Bibliothek als Referenzdemonstration.
PLAN-0024 und sein damaliger Skill-Creator-Nachweis bleiben historische Records;
die neue Abnahme ersetzt sie nicht rückwirkend.

## Confirmation

Vollständige Referenz und beauftragte Auslagerung erhalten die Schutzregeln in
AGENTS.md und das vollständige Verfahren in der Referenz. Unvollständige
Referenzen bleiben bei bloßer Bereinigung unverändert. Geprüfte Werkzeugrevision,
Befehle, Resultate und Grenzen stehen im
[Nachweis](../../members/scoville-project-context-cleanup/development/test-results/2026-10-02-safeguards.md).

## Revisit when

Skill Creator `compatibility` unterstützt, die Formatspezifikation sich ändert
oder ein realer Host das unveränderte Feld zurückweist.
