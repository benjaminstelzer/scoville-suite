---
format_version: 1
id: ADR-0073
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: suite/public-export
supersedes: ADR-0072
---

# Öffentliche Pfade neutral halten

## Decision

Öffentliche Suite-Exporte dürfen `docs/`, `development/` und `PROJECT_INDEX.md` enthalten. Veröffentlichte Texte verwenden für lokale Pfade neutrale repository- oder workspace-relative Angaben und enthalten keine persönlichen Laufwerke Benutzerverzeichnisse oder Sessionpfade.

## Problem

Entwicklungs- und Planunterlagen sind für das öffentliche Repository nützlich enthalten aber teilweise maschinenspezifische Pfade.

## Drivers

- Der Nutzer will `docs/` und `development/` im öffentlichen Repository behalten.
- Ein Kollege kann denselben Checkout auf einem anderen Laufwerk und in einem anderen Verzeichnis verwenden.
- Öffentliche Inhalte dürfen keine privaten Informationen über den Entwicklungsrechner offenlegen.

## Considered alternatives

- Ganze Verzeichnisse ausschließen: Verhindert Lecks entfernt aber nützliche Entwicklungs- und Planunterlagen.
- Maschinenspezifische Pfade unverändert veröffentlichen: Bewahrt historische Genauigkeit ist aber nicht portabel und gibt private Rechnerdetails preis.
- Pfade neutralisieren: Behält die Inhalte und macht lokale Verweise portabel.

## Consequences

- Der Export bleibt eine vollständige Projektion einschließlich Entwicklungs- und Planunterlagen.
- Lokale Pfade werden als repository-relative Ziele oder neutrale Platzhalter wie `<workspace-root>` und `<user-home>` geschrieben.
- Releaseprüfungen suchen im finalen Export nach persönlichen Laufwerken Benutzerverzeichnissen und Sessionpfaden.

## Confirmation

1. Baue General- und Codex-Export aus dem finalen Quellenstand.
2. Prüfe beide Dateibäume einschließlich `docs/` und `development/` auf maschinenspezifische Pfade.
3. Öffne README- und Entwicklungslinks aus einem verschobenen Checkout oder löse sie repository-relativ auf.

## Revisit when

Ein öffentlicher Inhalt benötigt ausnahmsweise einen absichtlich plattformspezifischen absoluten Beispielpfad.
