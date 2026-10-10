---
format_version: 1
id: ADR-0214
status: accepted
created: 2026-10-10
accepted: 2026-10-10
scope: suite/internal-communication
---

# Interne Agentenkommunikation auf notwendige Fakten kürzen

## Decision

Der Nutzer verlangt extrem knappe interne Ausgaben und Nachrichten für Manager,
Executor, Reviewer und Berater. Eindeutige beschriftete Felder genügen; nötig
sind nur Fakten für die nächste korrekte Entscheidung oder Aktion. Erzählungen,
Recaps und unveränderte Einstellungen entfallen, soweit kein Vertrag sie verlangt.

Pflichtpayloads, Statussemantik, exakte Kontrollmeldungen und Nutzerrelays,
Identitäten, Autorität, Stops, Belege und frischer Empfängerkontext bleiben
erhalten. Ein Review-pass benötigt nur seinen Status und gegebenenfalls den
erforderlichen Rollover-Messwert. Dauerhafte Anweisungen, Pläne, Decisions und
Nutzertexte behalten klare Luna-verständliche Sätze; komponierte interne Felder
brauchen keine vollständigen Sätze. Keine neue feste Feldsyntax einführen.

## Problem

Menschenorientierte Statusprosa und wiederholte bekannte Fakten vergrößern
interne Kommunikation ohne Nutzen für den Ablauf.

## Drivers

Pflichtkontext und Kontrollverträge bleiben auch bei gekürzten Ausgaben erhalten.

## Considered alternatives

[]

## Consequences

Interne Felder können satzfrei sein. Dauerhafte Quelltexte behalten die
konkreten Luna-Schreibkriterien; eine feste Feldsyntax ist nicht nötig.

## Confirmation

Gemeinsame Schreibquelle und betroffene Rollen- und Deliveryverträge gezielt
abnehmen. Öffentliche Anweisungen auf Verständlichkeit prüfen. Bestehenden
Paketbuild, technische Checks, lokale Updates und verifizierte Distributionen
verwenden; keine neuen Releases.

## Revisit when

Der Nutzer ändert die Kommunikations- oder Deliveryanforderungen.
