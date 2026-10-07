---
format_version: 1
id: ADR-0166
status: superseded
created: 2026-10-04
accepted: 2026-10-04
scope: suite/evaluation
supersedes: ADR-0161
superseded_by: ADR-0167
---

# Gezielte Abnahme mit höchstens 300 Testläufen

## Decision

Höchstens 300 Testläufe insgesamt, einschließlich Kontrollen, Wiederholungen,
Transportfehlern und invalidierten Versuchen. Eine vorab begründete gezielte
Auswahl genügt für W-014; ausgelassene Fälle werden ausdrücklich ausgewiesen.
Luna bleibt gpt-6-luna/high. Sol 6.1/high bewertet vollständige Gruppen nach
Sammlung, nicht abwechselnd nach jedem Einzelversuch. Bewertungen zählen separat.

## Problem

Die vollständige Matrix benötigt 2.571 erste Luna-Läufe. Der Nutzer lehnt eine
Erhöhung auf 4.500 ab und bestätigt ausdrücklich 300 Läufe samt gezielter Auswahl.

## Drivers

Ausdrückliche Antwort: „300 Läufe insgesamt; gezielte Auswahl genügt“.

## Considered alternatives

Die vollständige Matrix überschreitet den gewählten Umfang. Die bisherigen
150 Läufe werden durch 300 ersetzt, nicht um 300 zusätzliche Läufe ergänzt.

## Consequences

Der vorhandene gemeinsame Zähler wird unter Erhalt aller bisherigen Versuche
auf 300 erweitert. Die Auswahl nutzt qualifizierte Verständniswege über alle
acht Skills und relevante Profil-/Layoutunterschiede. Nicht qualifizierte
Trigger-, Befolgungs-, Wirkungs-, Claude- und native Wege bleiben ausgewiesene
Lücken, keine bestandenen Tests. W-001 qualifiziert die für diese Auswahl
benötigten Runner; die übrigen vorbereiteten Wege bleiben unverifiziert.

Die ursprüngliche Vollmatrix-Abnahme von W-014 ist entsprechend begrenzt.
Ausgewählte Fälle behalten ihre eingefrorenen Erwartungen, drei bewertbaren
Läufe und fünf bei gemischtem Urteil. Das Limit erlaubt weder zusätzliche
Claude-Tests noch native Proben, CI-Push, Installation oder Veröffentlichung.
Lokale technische Prüfungen und der gesondert freizugebende Runtime-CI-Nachweis
bleiben für ihre bestehenden Ansprüche erforderlich.

## Confirmation

Auswahl, Auslassungen, sämtliche Versuche und Gruppenurteile sind dokumentiert.
Der Zähler bleibt einschließlich der drei bisherigen Hostversuche höchstens 300.
Der Bericht beansprucht nur die tatsächlich geprüfte Auswahl und vorhandene
technische Nachweise, keine vollständige Aktivierungs- oder Wirkungsabnahme.

## Revisit when

Andere Testarten, mehr Versuche oder eine vollständige Matrix verlangt werden.
