---
format_version: 1
id: ADR-0015
status: accepted
created: 2026-09-24
accepted: 2026-09-24
scope: suite/ui-foundation
---

# Gemeinsame UI-Regeln mit allgemeinem und WordPress-Adapter

## Decision

Festgelegt ist, Qualitäts- und Validierungsregeln für beide UI-Skills einmal unter `../shared/ui/` zu pflegen und über die vorhandenen `shared:`-Dateizuordnungen in beide Pakete zu kopieren. Die allgemeine Variante ermittelt das Framework; die WordPress-Variante bindet denselben Vertrag an ihre unterstützten wp-admin-Oberflächen. Die Quellen sind `quality.md` und `validation.md`.

## Problem

Getrennte Regeltexte haben trotz großer Übereinstimmung unterschiedliche Prüfauslöser und keine einheitliche Grundlage für Informationsaufbau und Nutzerfreundlichkeit.

## Drivers

- Der Nutzer wünscht denselben Unterbau für beide Skills und eine zentrale Pflege ohne massives Aufblähen.
- Bestehende native WordPress-Konventionen, Versionsgrenzen und Übersetzbarkeit bleiben erhalten.
- Das Repository unterstützt gemeinsame Dateiquellen mit lokalen, vollständigen Paketkopien.
- Der Auftrag umfasst Audit und Fixplan-Entwurf, keine Umsetzung oder Veröffentlichung.

## Considered alternatives

- Gemeinsame Buildquellen mit zwei Adaptern: eine Pflegequelle, selbständige Pakete; Änderungen müssen beide Verbraucher prüfen.
- WordPress lädt Scoville UI zur Laufzeit: weniger Paketkopien, aber Installationsabhängigkeit und Gefahr zweier Abnahmeprozesse.
- Getrennte Quellen mit Paritätstests: kleinerer Umbau, aber weiterhin doppelte inhaltliche Pflege.
- Ein einziger großer Skill: ein Einstieg, aber allgemeinere Aktivierung und zusätzlicher WordPress-Kontext bei fremden Frameworks.

## Consequences

- Allgemeine Informationsstruktur, Interaktion und Evidenzgrenzen werden nur einmal geändert.
- WordPress bleibt alleiniger Implementierungs- und Abnahmebesitzer seiner Oberflächen; Frameworkwahl und Plattformausnahmen liegen im Adapter.
- Neue gemeinsame Regeln ersetzen Doppeltext. Quellenpflege und Spezialfälle werden nur bei Bedarf geladen.
- Gewöhnliche Nutzerführung gehört zur UI-Aufgabe. Gesonderte Art Direction braucht einen eigenen Auftrag; bestehende Produktentscheidungen werden bei Konflikten zurückgemeldet statt überschrieben.
- Es entstehen zwei generierte Paketkopien, aber keine zwei Autoritätsquellen und kein Zugriff auf installierte Geschwister.

## Confirmation

1. Binde dieselben Quellen über `suite.json` in beide Pakete ein und prüfe gleiche Bytes je Profil/Layout sowie den isolierten Export ohne Workspace-Shared-Verzeichnis.
2. Prüfe gemeinsame Qualitätsfälle mit beiden Adaptern; erhalte WordPress-Negativkontrollen für Classic, Tokenladen und ausgeschlossene Oberflächen.
3. Vergleiche reale Ergebnisse und geladenen Kontext gegen den bisherigen Paketstand. Struktur- und Verständnistests ersetzen keine Laufzeitnachweise.

## Revisit when

- Ein gemeinsamer Satz braucht widersprüchliche plattformspezifische Ausnahmen; verschiebe nur diese Abbildung in den Adapter.
- Die gemeinsame Quelle verursacht nachgewiesene unnötige Referenzladung oder kann im isolierten Paket nicht vollständig ausgeliefert werden.
