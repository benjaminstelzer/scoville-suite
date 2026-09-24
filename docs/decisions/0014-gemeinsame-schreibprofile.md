---
format_version: 1
id: ADR-0014
status: accepted
created: 2026-09-24
accepted: 2026-09-24
scope: prompting/worker-profiles
---

# Gemeinsame Schreibregeln mit getrennter Konfiguration

## Decision

Plan und Workflow verwenden dieselben zentral gepflegten Schreibregeln und denselben Helper für `low`, `medium` und `high`. Ihre Einstellungen bleiben getrennt. Ohne bekannte Zuordnung gilt `medium`. Explizite Nutzerangaben haben Vorrang.

Plan wählt die Anleitungstiefe pro Arbeitspunkt anhand des vorgesehenen Empfängers oder der vorhandenen Aufgabenbewertung. Workflow übernimmt den kanonischen Planpunkt vollständig und unverändert. Nur seine zusätzlichen Anweisungen folgen dem Profil des tatsächlichen Empfängermodells.

## Problem

Ein einheitlicher Detailgrad passt nicht zu allen vorgesehenen Workern. Eine nachträgliche Umformulierung durch den Dispatcher könnte Anforderungen verändern.

## Drivers

- Kein Worker und kein Koordinator darf Gesprächshistorie voraussetzen.
- Die Auswahl soll ohne zusätzliche Bewertungsskala oder Modellabfrage auskommen.
- Mehr Anleitung senkt weder Risiko noch benötigte Modellfähigkeit.
- Plan und Workflow müssen unabhängig konfigurierbar sein.

## Considered alternatives

- Ein globales Profil und eine gemeinsam wirksame Konfiguration: einfach, aber ungeeignet für unterschiedliche Planpunkte und getrennte Einstellungen.
- Einfache Profilauswahl je Auftrag mit gemeinsamen Regeln: bewahrt die Unterschiede ohne doppelte Pflege der Mechanik.
- Umschreiben des Planpunkts beim Dispatch: kann verlorene oder veränderte Anforderungen verursachen und ist ausgeschlossen.

## Consequences

- Gemeinsame Quellen liegen unter `../shared/`. Der Build erzeugt eigenständige Pakete mit identischen Helpern und Regeln, aber getrennten Konfigurationsdateien.
- Die kompakte Standardzuordnung speichert nur `low` und `high`. Luna und Gemini 3.8 Flash sind zunächst `low`, Astra, Fable 5.1 und Opus 5.5 `high`. Alle übrigen IDs erhalten `medium`. Dies ist eine konfigurierbare Arbeitseinteilung, kein belegtes Leistungsranking.
- `low` beschreibt Voraussetzungen und Schritte ausdrücklich. `medium` verwendet zusammenhängende Anweisungen. `high` legt Ergebnis, notwendige Grenzen und Abschluss fest und lässt geeignete Umsetzungsschritte offen. Alle Profile erhalten dieselben erforderlichen Fakten.
- Planpunkte und Übergaben enthalten benötigten Kontext direkt oder eindeutige Referenzen mit ausdrücklichem Leseauftrag. Ein Vorkommen irgendwo im Gesamtplan genügt nicht.
- Zusätzliche Erläuterungen erzeugen keine weiteren Dispatch-Einheiten. Aufgabenroute und Reasoning bleiben von der Anleitungstiefe getrennt.
- Die allgemeinen Projekt-Schreibregeln müssen die verbindliche Kontextvollständigkeit erhalten und zugleich die bisher pauschale Ausrichtung aller Planpunkte auf Luna mit der bewussten Profilwahl vereinbaren.

Die High-Regeln werden aus den am 2026-09-24 gelesenen Herstelleranleitungen abgeleitet: [OpenAI](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) und [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1). Gemeinsame Regeln sind vollständiges Ergebnis, eindeutiger Abschluss, notwendige statt pauschale Schrittvorgaben, konkrete Entscheidungsgrenzen, selbstständige Erledigung autorisierter Arbeit, begrenzter Umfang, gezielter Kontext und angemessene Prüfung. Ergänzend berücksichtigt das Profil verständliche Fortschrittsmeldungen, eigenständig verständliche Abschlussberichte und konkrete Blocker. API-, Effort- und Tokenlimit-Einstellungen werden nicht verallgemeinert. Die Übertragung auf drei Schreibprofile ist ein Entwurf und muss an Beispielaufträgen geprüft werden.

**Gemeinsame Schreibregeln**

W-005 setzt diese gemeinsame Grundlage für Planschreiber und zusätzliche Empfängeranweisungen um. Sie verändern keine Rollen, Berechtigungen, Aufgabenrouten oder festen Ergebnisformate.

**common.md:** Bewahre Ergebnis, Umfang, notwendige Voraussetzungen, Entscheidungen, Berechtigungen, Grenzen und Abnahmekriterien. Gib jedem Empfänger den erforderlichen Kontext direkt oder durch eindeutig bezeichnete, für ihn zugängliche Quellen mit ausdrücklichem Leseauftrag. Setze keine Gesprächshistorie voraus.

Benenne den vollständigen Abschluss, die erforderliche Prüfung und konkrete fehlende Informationen oder Entscheidungen. Fordere die Fortsetzung bereits autorisierter Arbeit. Ein reiner Frage- oder Bewertungsauftrag autorisiert keine Änderungen. Ein Schreibprofil ändert weder Risiko noch erforderliches Modell, Rolle oder Befugnisse.

Schreibe direkt, konkret und knapp. Führe jeden Sachverhalt an seinem zuständigen Ort. Nutze Absätze und Listen, wenn sie das Verständnis verbessern. Bei längerer Arbeit erklären kurze Fortschrittsmeldungen relevante Erkenntnisse und nächste Schritte. Der Abschluss nennt Ergebnis, tatsächliche Prüfungen und offene Grenzen eigenständig verständlich; feste Ergebnis- und Zustellformate gelten weiter.

**low.md:** Formuliere notwendige Voraussetzungen, Eingaben, geordnete Schritte und erwartete Prüfergebnisse ausdrücklich. Zusätzliche Erklärung erzeugt keine neuen Aufgaben oder Dispatch-Einheiten.

**medium.md:** Verbinde Ziel, nötige Schritte und Prüfung in kurzen zusammenhängenden Anweisungen. Erläutere nicht offensichtliche Übergänge.

**high.md:** Führe mit dem Ergebnis und dem Maßstab für einen vollständigen Abschluss. Gib nur Umsetzungsschritte vor, deren Reihenfolge oder Ausführung für Ergebnis, Schnittstelle oder Berechtigungsgrenze erforderlich ist. Überlasse die übrige Methode dem Empfänger. Füge keine vorsorglichen Teilaufgaben, Pflichtlektüren, Freigaberunden oder zusätzlichen Testserien hinzu.

Grundlage: [OpenAI Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) zu gezielter Skill-Lektüre, Entscheidungsgrenzen und vollständiger Erledigung; [Anthropic Fable](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) zu autorisierter Fortsetzung, begrenztem Umfang, angemessenen Tests, Schreibdichte, Fortschrittsmeldungen und Übergabekontext. Die gemeinsame Regelbildung und die drei Profile sind eine Projektableitung. Modellzuordnungen sind keine belegte Leistungsrangliste; API-, History-, Effort- und Tokenlimit-Regeln werden nicht verallgemeinert.

Review vom 2026-09-24: `scoville-plan-0002-astra-20260924-02` bestätigt die Regeln und die Phasenfolge. Übernommen sind gezielter Kontext, bestehende Step-Syntax, getrennte Phasen und ein Kompatibilitätsnachweis für das veröffentlichte Plan-/Workflow-Paar. Invariante Regeln gehören ausschließlich nach `common.md`; Profile ergänzen die Anleitungstiefe.

## Confirmation

1. Prüfe explizite Profile, eigene Skill-Einstellungen, bekannte und unbekannte Modelle und fehlende Auswahlgrundlagen gegen feste erwartete Ergebnisse.
2. Prüfe denselben Auftrag in drei Profilen auf vollständige Fakten, Berechtigungen und Abnahmekriterien ohne Gesprächshistorie.
3. Vergleiche den aus dem Übergabeprompt zurückgewonnenen Planpunkt mit seinem kanonischen Text. Nur Zusatzanweisungen dürfen zwischen Empfängerprofilen variieren.

## Revisit when

Reale Aufgaben die Zuordnung widerlegen oder ein weiterer Auswahlmechanismus nachweislich nötig wird.
