---
format_version: 1
id: PLAN-0013
status: completed
created: 2026-09-25
updated: 2026-09-25
---

# Scoville Plan auf Vorlage und Validator verschlanken

## Goal

Scoville Plan lädt für gewöhnliche Planpflege deutlich weniger Anleitung bei gleicher Funktion für bestehende Pläne. Der Validator prüft Formatregeln; die Anleitung enthält eine Vorlage und nur Regeln, die keine Maschine prüfen kann: Autorität, Nachweise, Schreibqualität und Zuschnitt. Orientierungswert für Einfügen, Fortschreiben, Abschluss und Wiederaufnahme sind höchstens rund 12 KB geladene Anleitung statt heute rund 33 KB. Format version 1, Viewer, Selector und alle bestehenden Records bleiben unverändert gültig.

## Non-goals

- Keine Formatänderung und keine Migration bestehender Plan- oder Decision-Records.
- Keine Änderung an Viewer-Leselogik oder Selector-Ausgabevertrag für Workflow.
- Keine Übernahme von Route-Klassen-Definitionen in Plan; Workflow bleibt deren Besitzer.
- Keine unbelegten Behauptungen zu Token-, Kosten- oder Laufzeitersparnis.
- Keine Veröffentlichung oder Installation durch diesen Plan.
- Keine Aufhebung des General-Fallbacks ohne Python; Codex behält die Python- und Validatorpflicht.

## Work items

### W-001 Ausgangsstand ist gemessen und Streichungen sind entschieden

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0074, ADR-0075, ADR-0076, ADR-0077]
Outcome: Vergleichbare Messwerte für vier Standardwege liegen vor und jede geplante Streichung ist als Decision festgehalten.
Acceptance: Für Einfügen, Fortschreiben, Abschluss und Wiederaufnahme sind geladene Dateien, Bytes, Tool-Aufrufe und Ergebnis am aktuellen Stand dokumentiert. Vier Decisions dokumentieren die bereits beauftragte Richtung; nur zusätzliche offene materielle Entscheidungen benötigen eine Nutzerwahl: Vorlage plus Validator als Grundprinzip, kein Schreiben neuer Decision-Batches, keine neuen Deferred/Prioritized-Titelpräfixe, keine Route-Klassen-Kriterien in Plan.
Steps:
1. Miss die vier Standardwege mit development/luna-tests/run_codex_cli_case.py und dem in development/luna-tests/suite-simplification-comparison.md dokumentierten Verfahren am aktuellen Stand von members/scoville-plan/scoville-plan/ und halte Dateien, geladene UTF-8-Bytes einschließlich wiederholter Reads, Read-Anfragen, tatsächlich beobachtbare Tool-Aufrufe und Ergebnis dort getrennt fest. Sichere Fälle, Quellenstand, Modell, Effort, Host und Laufgrenzen vor dem Umbau unter workspace temp/; kennzeichne den Runner als hypothetischen Verständnis- und Lesevergleich ohne Projektaktionen.
2. Prüfe bestehende Decisions unter docs/decisions/ und dokumentiere die vier bereits beauftragten Richtungen ohne erneute Freigabefrage in passenden bestehenden oder neuen akzeptierten Decisions. Verknüpfe die betroffenen todo-Items; zusätzliche offene materielle Entscheidungen bleiben proposed und blockieren nur abhängige Arbeit.
Evidence: [Planwechsel am 2026-09-25 ausdrücklich bestätigt; PLAN-0012 unverändert zurückgestellt, Aktuelle CLI lokal qualifiziert; Rohdaten in workspace temp/2026-09-25-plan-0013/preflight, Vier Ausgangsläufe und Grenzen in development/luna-tests/suite-simplification-comparison.md; 2 Protokoll-PASS und 2 READ-Fehler, ADR-0074 bis ADR-0077 halten die beauftragten Richtungen akzeptiert fest]

### W-002 Häufige Planpflege läuft über einen kompakten Kern

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0074]
Outcome: Bei verfügbarem Validator genügen SKILL.md und eine neue Referenz references/edit.md für Einfügen, Verfeinern, Fortschreiben, Blockieren und Abschließen von Work Items.
Acceptance: SKILL.md enthält Einsatzgrenzen, Vorlage eines Work Items, höchstens rund zehn Autoritäts- und Nachweisregeln, Einzelbetrieb und die profilabhängige Strukturprüfung nach jeder abgeschlossenen Schreiboperation: Codex mit Python 3.11+ und Validator; General mit verfügbarem Python per Validator, sonst über die manuelle Fallback-Referenz. edit.md enthält eine Tabelle der pro Status änderbaren Felder sowie die Regeln für Next action, Evidence, Einfügen, Abschluss und Auswahl des nächsten Items. Die Routingtabelle in SKILL.md lädt für diese Wege bei verfügbarem Validator nur SKILL.md und edit.md; die Aufruf- und Diagnosebehandlung ist damit erreichbar. Der General-Fallback wird nur ohne Python zusätzlich geladen. Jede semantische Kernregel hat einen eindeutigen Besitzer. Wiederholungen wie „never invent evidence“ sind entfernt.
Steps:
1. Verdichte members/scoville-plan/scoville-plan/SKILL.md auf Einsatzgrenzen, Work-Item-Vorlage, Autoritäts- und Nachweisregeln, Einzelbetrieb und profilabhängige Strukturprüfung. Entferne Formatdetails aus dem häufigen Leseweg nur soweit validate_profile.py sie prüft und der General-Fallback sie weiterhin vollständig beschreibt.
2. Erstelle members/scoville-plan/scoville-plan/references/edit.md aus den häufigen Teilen von references/native-plan-format.md, references/native-work-items.md und references/native-editing.md mit Status-Feld-Tabelle, Next-action- und Evidence-Regeln sowie Abschluss und Auswahl, und trage die Datei in suite.json ein.
3. Passe die Routingtabelle in SKILL.md für den häufigen Validatorweg auf SKILL.md und edit.md an. Erhalte den bedingten General-Fallback ohne Python und prüfe mit rg sowie semantischer Durchsicht die eindeutigen Besitzer der Kernregeln.
Evidence: [SKILL.md routet gewöhnliche Edits nur zu edit.md; Vorlage und acht Autoritätsregeln vorhanden, build_suite.py --size-report rendert General erfolgreich; Runtime- und Diagnoseverträge geprüft]

### W-003 Seltene Wege liegen in eigenen kurzen Referenzen

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0074, ADR-0075, ADR-0076]
Outcome: Plan-Lebenszyklus, Decisions und Sonderfälle werden nur bei Bedarf geladen und enthalten keine gestrichenen Schreibmechanismen mehr.
Acceptance: Aktivieren, Abschließen, Abbrechen und Löschen von Plänen, die Ausnahme für ungestartete Pläne, Decision-Übergänge und Supersession sind in kurzen Referenzen beschrieben, die die Routingtabelle nur für diese Operationen lädt. Neue Decision-Batches, Deferred/Prioritized-Präfixe und benannte Operationen wie complete_and_advance werden nicht mehr erzeugt; bestehende Batch-Felder und Präfixe bleiben lesbar und unverändert. Neue Aufgaben werden standardmäßig in Ankunftsreihenfolge angehängt. Nur eine ausdrücklich gewünschte Priorität bestimmt eine andere zulässige Position; Abhängigkeiten bleiben gültig. Bestehende Prioritäten aus historischen Präfixen und Rückkehranweisungen bleiben auch nach Wiederaufnahme verbindlich. Die Umleitung laufender Arbeit steht in der Next action. General behält in references/profile-without-python.md alle für die manuelle Prüfung nötigen Formatregeln; Codex erhält diesen Fallback nicht. native-plan-format.md, native-work-items.md und native-editing.md sind entfernt oder auf nicht doppelte Restinhalte reduziert.
Steps:
1. Überführe die seltenen Teile aus references/native-project-lifecycle.md, references/native-work-items.md und references/native-decision-format.md in kurze Referenzen für Plan-Lebenszyklus, Sonderfälle und Decisions und aktualisiere Routingtabelle und suite.json.
2. Ersetze Decision-Batches durch einzelne validierte Übergänge und complete_and_advance durch Abschluss, Auswahl und profilabhängige Strukturprüfung. Ersetze die Präfix-Warteschlange durch Anhängen in Ankunftsreihenfolge mit abweichender Position nur bei ausdrücklich gewünschter Priorität. Erhalte historische Prioritäten und Rückkehranweisungen bei Wiederaufnahme und lösche references/native-decision-batches.md erst nach Übernahme ihrer weiterhin nötigen Leseregeln.
3. Entferne oder kürze references/native-plan-format.md, references/native-work-items.md und references/native-editing.md auf Inhalte, die weder in edit.md noch in den neuen Referenzen stehen, und korrigiere alle Verweise in SKILL.md und den Referenzen. Überführe die sonst entfallenden manuellen Format- und historischen Batch-Prüfregeln nach references/profile-without-python.md und erhalte die General/Codex-Projektion in suite.json.
Evidence: [Lebenszyklus und Decisions verdichtet; historische Präfixe und Batch-Leseregeln erhalten, General-Fallback enthält konsolidierte Formatregeln; Codex-Manifest schließt ihn aus, rg findet keine entfernten Referenznamen oder complete_and_advance in Paket-Markdown]

### W-004 Zuschnitt von Work Items und Steps ist eine kurze Checkliste

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0077]
Outcome: references/planning-granularity.md erklärt Zuschnitt ohne Route-Klassen-Kriterien.
Acceptance: Die Referenz enthält eine kurze Checkliste für eigene Work Items gegenüber Steps, konkrete Steps mit Pfaden und die Trennung von Steps mit deutlich unterschiedlichem Risiko. Die Kriterien ultra_low bis ultra_high stehen nur noch in members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations-dispatch.md. Annotationen [route: …] und [execute: …] werden weiterhin unverändert erhalten.
Steps:
1. Kürze members/scoville-plan/scoville-plan/references/planning-granularity.md auf Zuschnitt-Checkliste, Step-Regeln und einen Satz zu Risikotrennung und Annotationserhalt und entferne die Route-Klassen-Definitionen.
2. Prüfe, dass members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations-dispatch.md die entfernten Kriterien vollständig enthält und kein Plan-Text mehr darauf verweist.
Evidence: [Zuschnitt auf Checkliste und Annotationserhalt reduziert, operations-dispatch.md enthält alle fünf Klassen samt Unknown-Grenze und Dateimengen-Ausnahme; Workflow unverändert]

### W-005 Validator und Selector passen zu den gestrichenen Schreibwegen

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0075, ADR-0076]
Outcome: Validator und Selector lesen alle bestehenden Records unverändert und verlangen keine gestrichenen Mechanismen mehr.
Acceptance: Bestehende Batch-Felder und Titelpräfixe bleiben gültig und werden nicht als Fehler gemeldet. Neue Records ohne diese Mechanismen sind gültig. Historische Batch-Integritätsprüfungen bleiben erhalten. Nur nachweislich ausschließlich entfallene Erzeugungspflichten dürfen entfernt werden; existieren solche Prüfungen nicht, bleibt der Validator unverändert und der Befund wird dokumentiert. Diagnosen nennen Datei, Feld und eine direkt umsetzbare Korrektur. Der Selector-Ausgabevertrag für Workflow ist unverändert.
Steps:
1. Prüfe in members/scoville-plan/scoville-plan/scripts/validate_profile.py, ob überhaupt ausschließlich entfallene Erzeugungspflichten existieren. Entferne nur solche belegten Prüfungen; erhalte Batch-Integrität und historische Lesbarkeit. Fehlt ein Änderungsbedarf, dokumentiere den Befund und lasse die Quelle unverändert.
2. Prüfe members/scoville-plan/scoville-plan/scripts/select_context.py gegen members/scoville-plan/development/tests/selector-contract.json und stelle sicher, dass Ausgabeform und source_text unverändert bleiben.
Evidence: [Validator prüft Batch-Felder nur bei Vorhandensein; keine Präfix- oder Batch-Erzeugungspflicht vorhanden, Validator und Selector bytegleich zum gesicherten Ausgang; source_text und selector-contract.json unverändert, Diagnosen enthalten Dateikontext und gezielte Hinweise; historische Integritätsprüfungen bleiben erhalten]

### W-006 Regressionen belegen gleiche Funktion

Status: done
Depends on: [W-003, W-004, W-005]
Blocked by: []
Decisions: [ADR-0074, ADR-0075, ADR-0076, ADR-0077]
Outcome: Evaluationsfälle und Fixtures belegen, dass bestehende Pläne und die vereinfachten Schreibwege korrekt funktionieren.
Acceptance: Alle Tests unter members/scoville-plan/development/tests bestehen grün unter Python 3.11 und einer aktuellen 3.x-Version, mit Angabe von Plattform und Version je Lauf. Fälle zu gestrichenen Mechanismen prüfen „wird gelesen, nicht neu erzeugt“; das Nicht-Erzeugen wird an tatsächlichen Modell-Dateiedits beobachtet. Routingtests und Feature-/Invariantenverträge bilden die neuen Besitzer ab, ohne historische Integrität oder aussagekräftige Verhaltensprüfungen zu schwächen. General ohne Python und Codex mit verpflichtendem Validator werden getrennt geprüft. Zwei nacheinander angehängte Aufgaben, explizite Priorität, historische Priorität und Rückkehr nach Wiederaufnahme behalten ihre Reihenfolge. Die Fixtures valid-profile und record-writing bleiben gültig. Der Viewer-Reader liest ein Profil mit neu geschriebenen Records.
Steps:
1. Passe unter members/scoville-plan/development/tests/ evaluation-cases.json, test_routing_contract.py, native-feature-contract.json und profile-invariants.json an neue Referenzbesitzer und erlaubtes Schreibverhalten an. Ersetze entfallene Route-Textmarker durch aussagekräftige Zuschnitt- und Annotationserhalt-Prüfungen; ergänze Fälle für Statusfelder, beide Python-Verträge, Warteschlangenreihenfolge und historische Prioritäten. Erhalte negative Batch-Integritätsfälle in test_validate_profile.py.
2. Führe die angepassten Modellfälle mit beobachtbaren Dateiedits an isolierten Profilen aus und trenne deren Ergebnis von bloßen Fallbeschreibungen und Unit-Tests. Führe members/scoville-plan/development/tests und die Rust-Tests von members/scoville-plan/development/viewer/src-tauri/src/reader.rs mit einem neu geschriebenen Beispielprofil aus.
Evidence: [ADR-0078: Nutzer nimmt Viewer-Test ausdrücklich aus; gestartete Acceptance bleibt historische Ausgangsanforderung, 73 Tests grün unter Windows Python 3.11.15 und 3.14.3; drei Bestandsfixtures valid:true, Fünf tatsächliche Luna-Modellfälle samt beobachtetem korrigierten Zwischenfehler im Vergleichsdokument; Endzustände unabhängig geprüft]

### W-007 Nachmessung, Pakete und Workflow-Lauf belegen den Effekt

Status: cancelled
Depends on: [W-006]
Blocked by: []
Decisions: [ADR-0074, ADR-0075, ADR-0076, ADR-0077, ADR-0078]
Outcome: Die Vereinfachung ist gemessen, gebaut und in einem echten Workflow-Lauf erprobt.
Acceptance: Vor der Nachmessung liegt ein unabhängiger Astra-Medium-Review gegen PLAN-0013 vor; relevante Befunde sind behoben. Dieselben vier Standardwege aus W-001 sind mit identischen Fällen, Modell, Effort, Host und Laufgrenzen erneut gemessen und im Vergleichsdokument gegenübergestellt. Geladene UTF-8-Bytes samt wiederholten Lesevorgängen, Read-Anfragen und tatsächlichen Tool-Aufrufen sind getrennt ausgewiesen; fehlende Werte bleiben als nicht verfügbar markiert. Hypothetische Runnerantworten gelten nur als Verständnis- und Lesemessung. Einfügen, Fortschreiben, Abschluss und Wiederaufnahme sind zusätzlich jeweils als tatsächliche Dateiedits an isolierten Profilen ausgeführt; Validator und Selector prüfen jeden relevanten Endzustand. Historie, Decisions und offene Arbeit bleiben erhalten; eine Abweichung vom Orientierungswert ist begründet. Beide Distributionsprofile sind gebaut und die Paketkopien entsprechen den Quellen mit LF. Ein Workflow-Lauf über mindestens drei Einheiten eines echten Plans erzeugt valide Records, und Worker führen die schlankeren Plan-Punkte ohne Rückfragen zu fehlendem Kontext aus. Aussagen zu Kosten und Laufzeit gelten nur so weit, wie sie gemessen sind.
Steps:
1. [execute: model=gpt-6-astra; reasoning=medium] Prüfe die Umsetzung unabhängig gegen docs/plans/0013-plan-verschlanken.md einschließlich ADR-0078; halte Befunde und Grenzen fest und behebe relevante Abweichungen vor der Nachmessung.
2. Wiederhole die Lesemessung aus W-001 unter gleichen Bedingungen und ergänze development/luna-tests/suite-simplification-comparison.md um Dateien, Bytes, Read-Anfragen, tatsächliche Tool-Aufrufe und Ergebnis. Führe dieselben vier Standardwege zusätzlich auf isolierten Profilen tatsächlich aus und prüfe die entstandenen Zustände mit members/scoville-plan/scoville-plan/scripts/validate_profile.py und members/scoville-plan/scoville-plan/scripts/select_context.py. Halte Rohdaten nur unter workspace temp/ und die knappe Auswertung im Vergleichsdokument fest.
3. Baue beide Profile mit development/build_suite.py, gleiche packages/scoville-plan mit den Quellen ab und führe einen begrenzten Workflow-Lauf über einen echten Plan durch, dessen Records danach der Validator prüft.
Evidence: [Nutzer bricht W-007 ausdrücklich ab; keine Nachmessung und kein Workflow-Lauf gestartet, Astra 01a0da62-677e-74b0-9641-f493f836d259 lieferte Befunde unmittelbar vor bestätigtem Stop, Review nennt fehlende draft-Aktivierungsgrenze sowie noch unbelegte entscheidungswirksame historische Priorität]

### W-008 Plantexte werden ausdrücklich als UTF-8 gelesen und geschrieben

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Plan erklärt eine plattformunabhängige UTF-8-Schreibweise; die durch diese Umsetzung beschädigten Zeichen sind wiederhergestellt.
Acceptance: edit.md verlangt explizites UTF-8 beim Lesen und Schreiben sowie korrekte PowerShell-Übergabe. Der unveränderte Goal und die gestarteten W-001 bis W-006 stimmen in ihren ursprünglichen authored Feldern mit der Sicherung überein. Eine Umlautprobe besteht unter Windows; Strukturprüfung und gezielte Routingtests bestehen.
Steps:
1. Stelle ausschließlich beschädigte Zeichen in docs/plans/0013-plan-verschlanken.md und members/scoville-plan/scoville-plan/references/edit.md aus der Sicherung beziehungsweise durch belegte Encoding-Rückführung wieder her.
2. Ergänze die konkrete UTF-8-Regel in members/scoville-plan/scoville-plan/references/edit.md und prüfe einen tatsächlichen Umlaut-Roundtrip sowie die gültigen Planrecords.
Evidence: [Viewer liest mit fs::read_to_string; fehlerhafte Unicode-Zeichen standen bereits in der Plandatei, Python 3.14 lief mit cp1252 als Plattformstandard; explizite UTF-8-Dekodierung belegt den Schreibfehler, Goal und Non-goals sowie ursprüngliche authored Felder W-001 bis W-006 stimmen mit Sicherung überein, Windows UTF-8-Umlaut-Roundtrip besteht ohne BOM mit LF; vier Routingtests grün]

### W-009 Astra-Befunde zu Aktivierung und historischer Priorität sind behoben

Status: done
Depends on: [W-008]
Blocked by: []
Decisions: [ADR-0074, ADR-0076]
Outcome: Die ursprüngliche Aktivierungsgrenze bleibt erhalten und historische Priorität ist nach Wiederaufnahme entscheidungswirksam belegt.
Acceptance: native-project-lifecycle.md erlaubt Aktivierung nur aus draft und erhält terminale Planhistorie samt ungestarteter Ausnahme. Ein frischer Modelllauf wählt bei abweichender Dokumentreihenfolge den historischen priorisierten Nachfolger; Validator und Selector bestätigen den Endzustand und fremde Blöcke bleiben unverändert. Ein Konflikt zwischen Rückkehr und historischer Priorität wird mit erhaltener Historie zur Klärung vorgelegt. Die ursprüngliche W-006-Nachweislücke und ihre Schließung bleiben nachvollziehbar.
Steps:
1. Stelle die draft-Beschränkung und die terminale Behandlung in members/scoville-plan/scoville-plan/references/native-project-lifecycle.md wieder her und ergänze einen gezielten Vertragsfall.
2. Prüfe historische Priorität und Rückkehrkonflikt mit tatsächlichen Modellaktionen an isolierten Profilen und halte Ergebnisse in development/luna-tests/suite-simplification-comparison.md fest.
Evidence: [Aktivierung wieder nur aus draft; terminale Historie und ungestartete Ausnahme erhalten, Historische Priorität wählt W-003 vor W-002; Validator und Selector bestehen; fremder Block unverändert, Erster Konfliktfall scheiterte; nach Regelkorrektur fragt frischer Nachtest bei erhaltenem current_item und unveränderten Zielblöcken, Konflikt-Nachtest sowie Validator und Selector und unabhängiger Vergleich bestanden; fünf Routingtests unter Python 3.11.15 und 3.14.3 grün, Vollständige Befunde und Grenzen in development/luna-tests/suite-simplification-comparison.md]
