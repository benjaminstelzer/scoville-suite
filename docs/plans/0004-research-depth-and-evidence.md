---
format_version: 1
id: PLAN-0004
status: draft
created: 2026-09-24
updated: 2026-09-24
---

# Scoville Research: tiefere Recherche mit überprüfbarem Mehrwert (zur Umsetzung freigegeben)

## Goal

Scoville Research soll entscheidende Evidenz zuverlässiger entdecken, ihre Aussagekraft prüfen und daraus nachvollziehbare Schlussfolgerungen gewinnen. Ein kontrollierter Ergebnisvergleich soll den Zusatznutzen gegenüber demselben Auftrag ohne Research-Skill und gegenüber dem bisherigen Skill zeigen. Grundlage ist das [Audit vom 2026-09-24](../../members/scoville-research/development/research-depth-audit-2026-09-24.md).

## Non-goals

- Keine Unterbrechung noch laufender Arbeit in PLAN-0002/W-009. Die Ausführungsreihenfolge ist in ADR-0016 festgelegt.
- Keine Veröffentlichung, Installation, neue Plattform, verpflichtende Agentenrunde oder automatische Änderung des Deep-Datenformats.
- Keine Qualitätsbehauptung allein aus Quellenzahlen, Berichtslänge, Strukturtests oder Regelverständnis.

## Work items

### W-001 Vergleichsgrundlage misst Research-Ergebnisse statt Regelwiedergabe

Status: todo
Depends on: []
Blocked by: []
Decisions: [ADR-0016]
Outcome: Ein vor der Überarbeitung festgelegter Vergleich kann Ergebnisnutzen und Aufwand ohne Skill sowie mit aktuellem und überarbeitetem Skill unterscheiden.
Acceptance: Das Protokoll enthält identische Aufgaben und Budgets je Bedingung, Quellenzugang, Modellkonfiguration, verdeckte Bewertung, zurückgehaltene Fälle, Fehlerkriterien und Aufwandsmessung. Es trennt Live-Entdeckung von Interpretation im eingefrorenen Bestand und dokumentiert jeden nicht ausgeführten Vergleich. Der bereits korrigierte Authority-Fall bleibt mit dem Core konsistent.
Steps:
1. Lies F1/F8 und den Vergleichsentwurf in members/scoville-research/development/research-depth-audit-2026-09-24.md. Prüfe den aktuellen Stand von members/scoville-research/development/tests/authority-cases.json gegen members/scoville-research/scoville-research/SKILL.md und development/luna-tests/research-cases.md; übernimm den bereits korrigierten Fall durable-default-path in die Vergleichsgrundlage.
2. Lege das kompakte Vergleichsprotokoll in members/scoville-research/development/README.md an; konkretisiere die sechs Falltypen, Wiederholungszahl und Bewertungsregeln des Audits vor der Kandidatenänderung. Trenne Entwicklungsfälle von zurückgehaltenen Schlussprüfungsfällen; weder deren Aufgaben noch Baseline-Ausgaben oder Bewertungsschlüssel dürfen in die Regelentwicklung gelangen. Andere Skills dürfen der Kontrollbedingung nicht die Research-Methode zuführen. Halte Korpora, Antwortschlüssel und Rohdaten unter dem Workspace-temp-Verzeichnis.
3. Lies AGENTS.md und development/release-preflight.md. Erzeuge die benötigte Baseline mit development/build_suite.py unter E:/Dropbox/AI Projects/skills/temp/release/ erst nach Ende bestehender Leser; sichere eine unveränderte Kopie samt Receipt im Workspace-temp bis W-005. Erfasse Paket-Hashes, Profil/Layout, Modell, Reasoning und Werkzeuge. Führe Ausgangsbedingungen in frischen Kontexten nur im Rahmen des Ausführungsauftrags aus; halte verdeckte Schlussprüfungen auch bei Baseline-Läufen von der Regelentwicklung getrennt.
Evidence: []
Next action: Bei Aktivierung den aktuellen Authority-Fall und den vorgesehenen Vergleichsumfang prüfen.

### W-002 Suchstrategie entdeckt entscheidende Gegenbelege und übersehene Alternativen

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0016]
Outcome: Die bestehende Recherche-Schleife verfolgt überprüfbare Teilfragen und wechselt bei fehlendem Erkenntnisgewinn begründet die Suchrichtung.
Acceptance: Die Fälle zu falscher Erstannahme und anders benannter Alternative werden mit konkreter Gegenprobe beziehungsweise passender Sucherweiterung bearbeitet. Sättigung wird von Budgetende und Zugriffsgrenzen unterschieden. Kleine Fragen brauchen weder feste Quellenquoten noch gespeicherte Pakete.
Steps:
1. Lies F2/F3 in members/scoville-research/development/research-depth-audit-2026-09-24.md. Ergänze members/scoville-research/scoville-research/SKILL.md an der bestehenden Vertrags- und Evidenzschleife um entscheidende Beobachtungen und begründete Auswahl der nächsten Suche; bewahre Scope und Autorisierungsgrenzen.
2. Konkretisiere in members/scoville-research/scoville-research/references/deep-research.md die adaptive Teilfragenabdeckung, Gegenprobe und Stoppbegründung. Präzisiere in references/development-research.md desselben Skill-Ordners die Auswahl und begründete Verwerfung ernsthafter Kandidaten.
3. Prüfe den gebauten Kandidaten an den vorbereiteten Entwicklungsfällen aus W-001 auf Suchentscheidungen und tatsächliche Evidenzfunde; bewahre zurückgehaltene Fälle für W-005.
Evidence: []
Next action: Nach W-001 die Ausgangsläufe auf die in F2/F3 benannten Fehlmechanismen prüfen.

### W-003 Evidenzbewertung und Synthese tragen die Schlussfolgerung

Status: todo
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0016]
Outcome: Tragende Schlussfolgerungen unterscheiden Quellenbericht, methodische Aussagekraft, gemeinsame Herkunft und Übertragbarkeit auf die Nutzerfrage.
Acceptance: Die vorbereiteten Fälle zu schwacher Methodik, gemeinsamer Herkunft und unzulässiger Gesamtfolgerung führen zu begründeter Gewichtung oder Begrenzung. Eine einzelne Spezifikation bleibt für ihren eigenen Vertrag ausreichend. Gelesene Testdefinitionen werden nicht als erfolgreiche Ausführung ausgegeben.
Steps:
1. Lies F4–F7 in members/scoville-research/development/research-depth-audit-2026-09-24.md. Ergänze members/scoville-research/scoville-research/references/academic-research.md um eine claimbezogene Prüfung der entscheidenden methodischen Schwächen; präzisiere die Beobachtungsarten in references/development-research.md desselben Ordners.
2. Konkretisiere im Core und in references/deep-research.md desselben Ordners die semantische Schlussprüfung über Prämissen, Inferenz und Gültigkeitsgrenzen. Kläre supported gegenüber single-source sowie die Erläuterung gemeinsamer Herkunft in vorhandenen Notizen, ohne Schemaänderung oder neuen Wahrheitsanspruch des Validators.
3. Prüfe die neuen Regeln an den entsprechenden Entwicklungsfällen aus W-001 und an einfachen Vertragsfragen; entferne Regeln ohne erkennbaren Zusatznutzen oder mit unverhältnismäßigem Pflichtaufwand.
Evidence: []
Next action: Nach W-002 die Ausgangsbefunde zu F4–F7 in konkrete minimale Regeländerungen übersetzen.

### W-004 Gebaute Varianten bewahren die Research-Verträge

Status: todo
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0011, ADR-0013, ADR-0016]
Outcome: Die geänderte Methode ist in den vorgesehenen Paketvarianten konsistent verfügbar und bewahrt Chat-only-, Speicher- und Beweisgrenzen.
Acceptance: Member-Strukturtests und betroffene Buildprüfungen bestehen auf dem aktuellen Stand. Die Research-Verständnisfälle einschließlich einfacher Fragen, Chat-only Deep und Autorisierung bleiben erfüllt; ausgeführte Modellprüfungen sind von statischer Inspektion getrennt belegt. README-Aussagen versprechen nur nachgewiesene Fähigkeiten.
Steps:
1. Gleiche development/luna-tests/research-cases.md und research-expected.md sowie members/scoville-research/development/tests/authority-cases.json mit den neuen Regeln ab; erhalte bestehende Grenzfälle und ergänze nur neue entscheidende Verhaltensfälle.
2. Aktualisiere erforderliche Nutzerhinweise ausschließlich in den zuständigen Fragmenten unter development/readme/scoville-research; erzeuge Mitglieds-READMEs und Pakete über development/build_suite.py gemäß AGENTS.md und development/release-preflight.md im einzigen Release-Staging nach Ende seiner Leser. Prüfe die zum Ausführungszeitpunkt geltenden general/codex- und Standalone/Suite-Projektionen.
3. Führe aus members/scoville-research den dokumentierten unittest-Aufruf und die betroffenen vorhandenen Buildprüfungen aus. Lies ADR-0011 und development/shared/luna-release-gate.md für die betroffenen Verständnisfälle; führe sie mit bestätigtem gpt-6-luna/medium nur im beauftragten Umfang aus, ohne gestoppte PLAN-0002-Prüfungen wiederaufzunehmen; vermerke fehlende Ausführung ausdrücklich.
Evidence: []
Next action: Nach W-003 den aktuellen Buildvertrag und die betroffenen Testbesitzer vor der Paketprüfung erneut lesen.

### W-005 Ergebnisvergleich entscheidet über die Übernahme

Status: todo
Depends on: [W-004]
Blocked by: []
Decisions: [ADR-0016]
Outcome: Ein fallbezogener Vergleich zeigt belegten Mehrwert, fehlenden Nutzen oder Regressionen des Kandidaten einschließlich zusätzlichem Aufwand.
Acceptance: Die drei Bedingungen aus W-001 werden mit unveränderten Bewertungsregeln verglichen; zurückgehaltene Testfälle bleiben der Regelentwicklung bis zur Schlussprüfung unbekannt. Kritische Claims werden anhand der Quellen geprüft. Der Bericht nennt Unterschiede je Fall, Wiederholungen, Kosten und Grenzen; keine allgemeine Überlegenheit aus bloßem Pilotmittelwert. Ein belegtes Null- oder Negativergebnis erfüllt den Vergleich, rechtfertigt aber keine Verbesserungsaussage. Fehlende Pflichtvergleiche lassen das Item offen.
Steps:
1. Lies das eingefrorene Protokoll in members/scoville-research/development/README.md. Führe die Kandidatenbedingung aus W-001 einschließlich zurückgehaltener Fälle in frischen Kontexten aus; prüfe die Vergleichbarkeit der Ausgangsbedingungen und wiederhole sie nur bei einer konkret benannten Veränderung. Führe bislang zurückgehaltene Baseline- und Kontrollfälle erst jetzt aus, falls sie in W-001 noch nicht in getrennten Kontexten erhoben wurden.
2. Bewerte anonymisierte Ergebnisse anhand des eingefrorenen Protokolls und prüfe entscheidende Claims direkt. Unterscheide Fehler der Suche, Quelleninterpretation und Schlussfolgerung; untersuche bei Bedarf gezielt den Beitrag einer neuen Regelgruppe.
3. Formuliere aus den beobachteten Ergebnissen eine begründete Übernahme-, Kürzungs- oder Nachbesserungsempfehlung. Ändert eine Nachbesserung den Kandidaten, baue ihn neu und prüfe betroffene Verträge und Ergebnisse erneut; bereits offengelegte Fälle sind dann keine unbekannte Schlussprüfung mehr. Bewahre nur die vom Retentionsvertrag erlaubte knappe Zusammenfassung beim Mitglied; Rohdaten bleiben temporär und werden nach abgeschlossener Auswertung gemäß Workspace-Regeln entfernt.
Evidence: []
Next action: Nach W-004 den finalen Kandidaten einfrieren und den vereinbarten Vergleich ausführen.
