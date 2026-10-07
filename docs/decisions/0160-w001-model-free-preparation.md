---
format_version: 1
id: ADR-0160
status: accepted
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
---

# W-001 zunächst modellfrei vorbereiten

## Decision

W-001 darf jetzt modellfrei umgesetzt und lokal geprüft werden. Danach prüft
Astra High die Änderungen über Ask. Die Freigabe ersetzt den bisherigen Stopp
vor W-001 nur für diese Vorbereitung.

## Problem

Die Skill-Änderungen sind abgeschlossen. Runner und Testumgebungen müssen vor
der Entscheidung über kostenpflichtige Testläufe vorbereitet werden.

## Drivers

Der Nutzer bestätigt die vorgeschlagene modellfreie Vorbereitung mit
„Ja mach erst mal w001“. Testmaterial bleibt im Projekt Desktop/test.

## Considered alternatives

Sofortige Modelltests würden die noch offene Budgetentscheidung vorwegnehmen.

## Consequences

Lokale Kontrollen dürfen Doubles verwenden, gelten aber nicht als Modell- oder
Hostnachweis. W-001 bleibt offen, soweit seine Acceptance echte Kontrollläufe
benötigt. ADR-0150 begrenzt weiterhin Modellbudget und native Live-Proben,
ADR-0151 den privaten CI-Push. W-014 wird nicht gestartet.

## Confirmation

Vorbereitung, lokale Kontrollen und unabhängiges Review werden dokumentiert.
Nicht beobachtete Hostfähigkeiten bleiben unverifiziert.

## Revisit when

Der Nutzer Pilotbudget, native Proben oder einen größeren Umfang freigibt.
