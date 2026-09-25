---
format_version: 1
id: PLAN-0006
status: draft
created: 2026-09-24
updated: 2026-09-25
---

# Gemeinsamer UI-Unterbau mit WordPress-Spezialisierung (zur Umsetzung freigegeben)

## Goal

Scoville UI und Scoville WordPress UI verwenden dieselbe gepflegte Grundlage für Informationsaufbau, Nutzerführung, Interaktion und überprüfbare Qualität. Der allgemeine Skill ermittelt das Framework; WordPress konkretisiert dieselben Anforderungen für seine unterstützten wp-admin-Oberflächen. Grundlage ist der [Audit vom 2026-09-24](../ui-skills-audit-2026-09-24.md).

## Non-goals

- Keine Installation, Veröffentlichung oder Wiederaufnahme früher verschobener Tests außerhalb des beauftragten Prüfumfangs.
- Kein neuer Laufzeit-Skill, Remote-Regeldownload, Stil-/Palettenkatalog oder Import aus einem installierten Geschwister.
- Keine Erweiterung des WordPress-Surface-Supports, erzwungene React-/Tokenmigration oder automatische Übersetzungsproduktion.
- Keine pauschale Accessibility-, Performance- oder Usability-Freigabe aus Quellprüfung, Screenshots oder Regelverständnis.

## Work items

### W-001 Vergleichsgrundlage trennt Regelverständnis und tatsächliche UI-Qualität

Status: paused
Depends on: []
Blocked by: []
Decisions: [ADR-0015, ADR-0016]
Outcome: Ein vor Änderungen festgelegtes Protokoll kann gemeinsame Qualitätsziele und beide Framework-Adapter an realen Aufgaben prüfen.
Acceptance: Das Protokoll enthält die sechs Fallgruppen des Audits, identische Ausgangsbedingungen je Vergleich, getrennte Entwicklungs- und Schlussprüfungsfälle mit verdeckten Fehler-/Bewertungsschlüsseln, Negativkontrollen, Modell-/Paketidentität und Aufwandsmessung. Hypothetische Antworten, Runtime-Prüfung und Nutzertest bleiben getrennt. Historisch verschobene Tests werden weder gestartet noch als erledigt behandelt, solange der Ausführungsauftrag das nicht abdeckt.
Steps:
1. Lies docs/decisions/0015-shared-ui-foundation.md und docs/ui-skills-audit-2026-09-24.md; prüfe den aktuellen Status von ADR-0015. Die technische Entscheidung ist angenommen; ADR-0016 hält den Umsetzungsauftrag fest. Gleiche W-002 in members/scoville-ui-anti-ai-slop/development/docs/plans/0001-source-first-ui-validation.md und members/scoville-wordpress-ui-backend-anti-ai-slop/development/docs/plans/0001-source-first-ui-validation.md mit development/luna-tests/ui-cases.md und development/luna-tests/wordpress-cases.md ab; bewahre die Member-Pläne als Historie und benenne den tatsächlich neu beauftragten Testumfang.
2. Lies den aktuellen Stopp in PLAN-0002/W-009; die Protokollvorbereitung nimmt dessen Prüfungen nicht wieder auf. Lege das gemeinsame Protokoll unter development/ui-evaluation.md an. Verwende bestehende Projekt-Testnähte für die Runtime-Fixtures; kläre zuerst Browsersteuerung sowie lokale Classic-/React-WordPress-Laufzeit und die Testgrenze von development/luna-tests/prepare_wordpress.py. Plane die tatsächlichen UI-Läufe gesondert vom toolbeschränkten Verständnis-Runner; dessen simulierte Aktionen sind kein Runtime-Nachweis. Erfinde keine bereits vorhandene Runtime-Harness.
3. Lies AGENTS.md und development/release-preflight.md für das einzige Build-Staging E:/Dropbox/AI Projects/skills/temp/release/ und den Schutz bestehender Leser. Friere im Rahmen des späteren Ausführungsauftrags gebaute Ausgangspakete und vergleichbare Aufgaben ohne Skill und mit bisherigem Skill ein. Lege Runtime-Fixtures, Ausgangsläufe und verdeckte Bewertungsschlüssel im Workspace-temp ab; erhalte sie bis W-005. Halte Schlüssel und Schlussprüfungsfälle von der Regelentwicklung fern; W-003/W-004 verwenden Entwicklungsfälle. Modell, Tools, Budgets und zusätzliche Skills bleiben zwischen den Armen kontrolliert.
Evidence: []
Next action: Nutzer hat 36 SOL-6-Medium-Läufe bestätigt; Budget in development/ui-evaluation.md festhalten und Classic-/React-Runtime prüfen. Baseline gesichert; keine UI-Quellen geändert.

### W-002 Gemeinsame Regeln werden einmal gepflegt und vollständig in beide Pakete gebaut

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0015, ADR-0016]
Outcome: Beide UI-Pakete verwenden dieselben Qualitäts- und Validierungsquellen mit getrennten Framework-Adaptern und ohne Laufzeitabhängigkeit.
Acceptance: ADR-0015 ist vor der Umsetzung ausdrücklich angenommen; bei Ablehnung oder Änderung bleibt die davon abhängige Umsetzung bis zur Plananpassung offen. Allgemeine bisherige Guards bleiben vollständig erhalten; WordPress gewinnt die fehlenden relevanten Prüfauslöser. Paketkopien sind je Profil/Layout bytegleich, Links vollständig lokal auflösbar und der isolierte Export baut ohne Workspace-Shared-Verzeichnis. Kein doppelter UI-Abnahmeprozess entsteht.
Steps:
1. Lies docs/decisions/0015-shared-ui-foundation.md und prüfe die ausdrückliche Annahme vor Änderungen. Ordne die bestehenden Absätze aus beiden references/validation.md sowie UI references/ui-quality.md und WordPress references/ui-guidance.md den gemeinsamen Anforderungen oder Plattformabbildungen zu. Nutze die erhaltenen Negativkontrollen aus W-001; behalte Source-vor-Messung-vor-Sicht, Nachweisgrenzen und Audit-Autorität.
2. Lege gemäß ADR-0015 ../shared/ui/quality.md und ../shared/ui/validation.md als Quellen an. Ersetze in suite.json den bisherigen UI-Qualitätseintrag und ergänze für beide Member files[].source mit shared:ui/quality.md beziehungsweise shared:ui/validation.md. Verwende die vollständigen memberbezogenen Zielpfade <skill-name>/references/ui-quality.md und <skill-name>/references/validation-common.md; erzeuge keine doppelten Ziele. Entferne abgelöste lokale Autoritätsquellen; reduziere lokale validation.md auf Adapterregeln und passe beide SKILL.md-Router auf gezieltes einmaliges Laden an.
3. Ergänze die kleinste passende Regression in development/tests/test_build_suite.py oder im zuständigen kanonischen Test unter ../shared/tests/. Synchronisiere danach Quellen und Tests mit python -B ../shared/build/sync_suite_sources.py --root . in den generierten Shared-Snapshot. Prüfe Manifest, gleiche Shared-Payloads, vollständige Links und isolierten Build über die vorhandenen Build-/Exportprüfungen.
Evidence: []
Next action: Nach W-001 den angenommenen Shared-Dateivertrag aus ADR-0015 und seine Verbraucher gegen den aktuellen Builder prüfen und umsetzen.

### W-003 Informationsaufbau und Nutzerführung haben einen kompakten gemeinsamen Maßstab

Status: todo
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0015, ADR-0016]
Outcome: Beide UI-Varianten prüfen Informationsstruktur und Bedienbarkeit anhand derselben aufgabenbezogenen Regeln.
Acceptance: Die zehn Regelideen des Audits sind ohne Doppeltext auf die gemeinsame Quelle verdichtet und mit konkreten Fehlersignalen prüfbar. WCAG-Pflichten, Usability-Heuristiken und Plattformkonventionen sind unterschieden. Bestehende Inhalte und Designentscheidungen bleiben geschützt; normale Nutzerführung verlangt keinen zusätzlichen Designauftrag. Lokale Aufgaben laden keine irrelevanten Kapitel.
Steps:
1. Lies den Regelentwurf und seine Quellenabgrenzung in docs/ui-skills-audit-2026-09-24.md. Überarbeite ../shared/ui/quality.md anhand des Regelentwurfs im Audit: Aufgabe und Ort, Entscheidungsreihenfolge, Gruppierung, Aktionsbereich, Offenlegung, Wiedererkennen, Zustände, Erholung, Sprache/Hilfe und vollständige Zugänglichkeit. Ersetze entsprechende bestehende Absätze statt einen weiteren Katalog anzuhängen.
2. Präzisiere die Grenzen in members/scoville-ui-anti-ai-slop/scoville-ui-anti-ai-slop/SKILL.md, members/scoville-wordpress-ui-backend-anti-ai-slop/scoville-wordpress-ui-backend-anti-ai-slop/SKILL.md an: UI besitzt die allgemeine Nutzbarkeit und berücksichtigt angeforderte Formulierungen ohne einen zusätzlichen Skill. Bewahre aktive Entscheidungs- und Opt-out-Verträge sowie Suite-/Standalone-Unterschiede.
3. Prüfe die neuen Regeln an den Informations- und Formfällen aus W-001 sowie an Negativkontrollen für legitime Dichte, mehrere Entscheidungsbereiche und geschützte Texte. Gleiche WordPress references/ui-guidance.md auf reine Plattformergänzungen ab.
Evidence: []
Next action: Nach W-002 die vorhandenen Qualitätsabsätze mit den zehn Regelideen abgleichen und nur echte Lücken ergänzen.

### W-004 Interaktions- und Laufzeitprüfungen erfassen die risikorelevanten Übergänge

Status: todo
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0015, ADR-0016]
Outcome: Gemeinsame Prüfregeln erfassen relevante Fokus-, Eingabe-, Lade- und Fehlerübergänge; die WordPress-Abbildung bewahrt native Verträge.
Acceptance: Betroffene Dialog-, Drag-, Formular- und dynamische Datenfälle prüfen tatsächliche Bedienung statt nur Endbilder. Themes/Kontrastmodi, reduzierte Bewegung und Eingabewechsel werden für beide Adapter bei Relevanz ausgewählt. WCAG-Ausnahmen bleiben erhalten. Lokale Performance-Beobachtung wird nicht als Felddatenbeleg bezeichnet. WordPress-Version, Tokenladeort, native Abstände und i18n bleiben nachweisbar korrekt.
Steps:
1. Lies F4/F5 und die referenzierten WCAG-/APG-Grenzen in docs/ui-skills-audit-2026-09-24.md. Ergänze ../shared/ui/quality.md und ../shared/ui/validation.md um knappe bedingte Auslöser für Dialogfokus, Drag-Alternative/Abbruch, Paste/Autofill bei betroffenen Formularen, Werterhalt, Doppelaktionen und veraltete Ergebnisse. Erhalte bestehende Quellen-/Mess-/Sichtreihenfolge und prüfe Übergänge nur im betroffenen Ablauf.
2. Ergänze die gemeinsame Validierung um Layout-Stabilität während des Ladens und stockende Eingaben bei konkretem Risiko. Halte Backend-Optimierungen außerhalb dieses Vertrags und unterscheide Labor, Feld, Emulation und tatsächlich getestete Eingabe-/Gerätebedingungen.
3. Prüfe die Adapterabbildung in beiden lokalen validation.md sowie WordPress responsive.md, version-compatibility.md und internationalization.md. Übe in den autorisierten Fixtures die relevanten Core-7.0/7.1-, Portal-, Notice-, Sprach- und Fokusfälle aus W-001; ändere keine funktionierenden Classic-Konventionen zum Zweck numerischer Gleichheit.
Evidence: []
Next action: Nach W-003 die gemeinsamen Trigger zuerst den betroffenen Fixture-Abläufen zuordnen.

### W-005 Gebaute Pakete zeigen Nutzen und Aufwand des gemeinsamen Unterbaus

Status: todo
Depends on: [W-004]
Blocked by: []
Decisions: [ADR-0011, ADR-0013, ADR-0015, ADR-0016]
Outcome: Ein dokumentierter Ergebnisvergleich entscheidet über Übernahme oder Nachbesserung; Paketvarianten und Adapter sind anhand aktueller Bytes geprüft.
Acceptance: Die zurückgehaltenen Schlussprüfungsfälle aus W-001 werden mit Kandidat und vergleichbaren Ausgangsbedingungen bewertet. Bericht nennt Defekte, Fehlalarme, Aufgabenabschluss, Owner-Verstöße, falsche Claims und Aufwand je Fall. Gemeinsame Fälle gelten für beide Adapter; Verständnisproben ersetzen keine Runtime-Prüfung. Erforderliche Varianten, Buildchecks und projektseitige Modellprüfungen sind belegt; offene Pflichtprüfungen verhindern den Abschluss. Ein belegtes Null- oder Negativergebnis erfüllt den Vergleich ohne Überlegenheitsbehauptung. Bei nachträglichen Kandidatenänderungen sind Neubau und betroffene Prüfungen auf den finalen Bytes nötig; offengelegte Fälle sind dann keine unbekannte Schlussprüfung. Keine Veröffentlichung ist Teil dieses Items.
Steps:
1. Aktualisiere development/luna-tests/ui-cases.md, ui-expected.md, wordpress-cases.md und wordpress-expected.md sowie members/scoville-ui-anti-ai-slop/development/tests/evaluation-cases.json für Shared-Unterbau, Adapter und Paketlayout. Bewahre bisherige Grenzfälle; halte den Antwortschlüssel vom ausführenden Modell fern.
2. Lies AGENTS.md, development/release-preflight.md und development/shared/luna-release-gate.md. Baue Standalone/general sowie die vollständigen Suite/general und Suite/codex mit development/build_suite.py unter E:/Dropbox/AI Projects/skills/temp/release/ nach Ende bestehender Leser; Task-temp hält Baseline-Kopien und Laufdaten. Prüfe aktuelle Pakete, Shared-Snapshot und isolierten Export. Pflege README-Änderungen in development/readme/scoville-ui-anti-ai-slop und development/readme/scoville-wordpress-ui-backend-anti-ai-slop. Führe betroffene Build-/Pakettests und die beauftragten Verständnisfälle gemäß ADR-0011 aus; der gestoppte PLAN-0002-Testlauf bleibt davon getrennt.
3. Lies das eingefrorene Protokoll in development/ui-evaluation.md. Führe den autorisierten praktischen Vergleich mit finalen Paketen aus und bewerte nach W-001. Dokumentiere Nutzen, Regressionen, geladene Bytes/Tokens, Toolaufwand und Grenzen kompakt beim zuständigen Entwicklungsbesitzer. Bewahre Rohdaten nur gemäß Retentionsvertrag; beanspruche keine allgemeine Modellüberlegenheit aus dem Pilot.
Evidence: []
Next action: Nach W-004 Kandidatenbytes einfrieren und die noch unbeobachteten Paket- und Ergebnisprüfungen durchführen.
