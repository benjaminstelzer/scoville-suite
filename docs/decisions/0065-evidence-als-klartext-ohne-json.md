---
format_version: 1
id: ADR-0065
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: plan/evidence-syntax
---

# Evidence als Klartext ohne JSON

## Decision

Die Formaterweiterung aus ADR-0049 verwendet normalen einzeiligen Text hinter Evidence: statt einer neuen JSON- oder Escape-Syntax. Bestehende Listen bleiben unverändert lesbar. Ein mit [ beginnender Wert verwendet weiterhin die bisherige Listensyntax; alle anderen Werte sind ein wörtlicher Texteindruck ohne Decodierung. Die aktuelle Nutzerkorrektur ersetzt die in ADR-0049 erwogene Umsetzung mit gequoteten und escapten Einträgen.

## Problem

Die zunächst versuchte JSON-Erweiterung fügte vermeidbare Syntax hinzu, obwohl JSON nach Nutzererfahrung bereits mehrfach fehleranfällig war.

## Drivers

- Der Nutzer verlangt weniger Komplexität und lehnt JSON für Evidence ab.
- Alte gültige Einträge müssen ihre Bedeutung behalten.

## Considered alternatives

- JSON-Array: vom Nutzer wegen Komplexität und Fehleranfälligkeit verworfen.
- Gewöhnlicher Text neben bestehenden Listen: keine neue Escape-Sprache und keine Migration bestehender Pläne.

## Consequences

- Kommas und Klammern im Klartext bleiben unverändert. Anführungszeichen und Backslashes sind wörtlich.
- Leere Evidence bleibt []. Die bestehende Grenze von 200 Zeichen gilt je Eintrag; ausführliche Ergebnisse gehören in ihre Quelle.
- Neue Leser lesen alte Pläne. Alte Leser können Klartext-Evidence und CRLF ablehnen. Für diese Erweiterungen müssen die Leser aktualisiert sein.
- PLAN-0011/W-009 war bereits gestartet. Sein ursprünglicher Decision-Verweis bleibt als Verlauf erhalten; diese Nutzerkorrektur und ihr Nachweis stehen in seinen veränderlichen Evidence- und Next-action-Feldern.

## Confirmation

Prüfe Klartext mit Sonderzeichen, alte Listen, wörtliche Anführungszeichen, LF und CRLF mit Validator, Selector und Viewer. Prüfe die erwartete Ablehnung neuer Formen mit dem bisherigen Leser.

## Revisit when

Ein realer Plan benötigt Evidence, die mit diesen beiden eindeutig unterschiedenen Formen nicht verlustfrei dargestellt werden kann.
