---
format_version: 1
id: ADR-0151
status: superseded
created: 2026-10-04
accepted: 2026-10-04
scope: suite/runtime-ci
superseded_by: ADR-0170
---

# Privater Runtime-CI-Push und geschütztes Release-Staging

## Decision

Der Nutzer genehmigt Commit und Push des vorbereiteten Snapshots
`runtime-ci-candidate` im privaten Testprojekt nach
`benjaminstelzer/scoville-runtime-ci`. Input-SHA256:
`bd26c0b4038fc62fbb9fb4640bb9bbb4949e8354d4f2f0ccf59db0c78d81a810`.
Die sechs Runtime-CI-Jobs dürfen laufen. Die Freigabe gilt nur für diesen
Testsnapshot, nicht für Veröffentlichung, Installation oder andere Kandidaten.
Das Testprojekt unter Desktop/test ersetzt für diese Vorbereitung das geschützte
Release-Staging entsprechend der ausdrücklich vorgegebenen Testablage.

## Problem

Der Prompt schützt das Release-Staging, während fragments.md Runtime-Snapshots dort vorsieht. Ein verifizierter Build braucht zudem den privaten Push.

## Drivers

Kein echter Commit/Push ohne Freigabe; private Quellen bleiben privat; bestehender Release-Baum unverändert.

## Considered alternatives

Verifizierten Build offen lassen: Kandidaten- und lokale Tests möglich, kein vollständiger CI-Nachweis. Staging-Ausnahme freigeben: verändert ausdrücklich den bisherigen Schutzumfang.

## Consequences

W-014 benötigt weiterhin einen erfolgreichen, exakt passenden CI-Nachweis. Lokale Prüfungen allein ersetzen ihn nicht. Quellrepositories werden nicht committet oder gepusht; Release-Staging bleibt unverändert.

## Confirmation

Nutzerantwort: „Diesen privaten CI-Push freigeben“. Der Builder-Snapshot und neun bestandene lokale Tests lagen vor der Entscheidung vor. Nach Push den passenden Run mit exakten Paket-/Test-Hashes nachweisen.

## Revisit when

Der CI-Vertrag oder die Staging-Vorgabe geändert wird.

