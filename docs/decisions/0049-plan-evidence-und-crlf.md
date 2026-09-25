---
format_version: 1
id: ADR-0049
status: accepted
created: 2026-09-25
accepted: 2026-09-25
scope: plan/serialization
transition_batch: f4ac9627ee1ebc83f5a18c0e13e4603d1b8485d4b1e82bf5fda3951a69d634b4
transition_batch_members: [ADR-0047, ADR-0048, ADR-0049, ADR-0050, ADR-0051]
---

# Plan-Evidence und Zeilenenden alltagstauglich lesen

## Decision

Empfohlen: neue Leser akzeptieren zusätzlich gequotete und escapte Evidence-Einträge sowie konsistentes CRLF. Neue Dateien bleiben LF. Alte gültige Records bleiben lesbar. Der Rollout benennt ausdrücklich, dass alte Leser die erweiterte Evidence-Syntax möglicherweise ablehnen.

## Problem

Natürliche Evidence mit Komma und Windows-Checkouts scheitern am aktuellen engen Formatvertrag.

## Drivers

- Kein stiller Verlust von source_text, Zeichen oder Evidenz.
- Native Records, Selector und Viewer müssen dieselbe Interpretation verwenden.

## Considered alternatives

- Bestehendes Format unverändert und LF erzwingen: wenig Implementierung, dauernde Formulierungs- und Checkoutanforderungen.
- Leser erweitern: bessere Bedienbarkeit, koordinierter Reader-Rollout nötig.

## Consequences

- Vor Umsetzung alle tatsächlichen Parser/Verbraucher identifizieren.
- Ob eine Formatversion nötig ist, anhand veröffentlichter Readerkompatibilität entscheiden; keine beidseitige Kompatibilität versprechen.
- Alte Records werden nicht allein für das Upgrade normalisiert oder migriert.

## Confirmation

1. Prüfe alte Fixtures und Evidence mit Komma, Klammern, Anführungszeichen und Backslash.
2. Prüfe LF und CRLF einschließlich unverändertem source_text und betroffenen Batch-/Viewer-Verbrauchern.
3. Belege Upgradeverhalten mit einem bisherigen Leser; dokumentiere die tatsächliche Grenze.

## Revisit when

Ein veröffentlichter Verbraucher keine koordinierte kompatible Erweiterung zulässt.
