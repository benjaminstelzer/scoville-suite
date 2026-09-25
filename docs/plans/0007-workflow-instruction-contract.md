---
format_version: 1
id: PLAN-0007
status: completed
created: 2026-09-25
updated: 2026-09-25
---

# Workflow-Verträge für moderne Modelle vereinfachen

## Goal

Scoville Workflow lädt für Launcher, Coordinator und Kinder die kleinste aus autoritativen Zustandsbelegen eindeutig ableitbare vollständige Regelmenge. Wo sich eine aktuelle Phase nicht eindeutig belegen lässt, bleibt der vollständige Vertrag erhalten und wird nur ohne Bedeutungsverlust konsolidiert. Exakte Protokoll-, Identitäts-, Zustands-, Autorisierungs-, Ergebnis- und Wiederanlaufgrenzen bleiben vollständig erhalten und werden weiterhin durch ihre kanonischen Helper und Verhaltenstests abgesichert.

## Non-goals

- Keine Änderung der expliziten Aktivierung, Rollen, Planhoheit, Guard-Autorität, Modellrouten, Reparaturgrenze, Git-Grenzen oder Berechtigungen.
- Kein zweiter dauerhafter Zustandsbesitzer neben Plan und Guard und kein manueller Ersatz für Helperausgaben.
- Keine Veröffentlichung, Installation oder Änderung laufender Workflow-Aufgaben.
- Keine Kürzung allein nach Wortzahl und keine Wirksamkeitsbehauptung aus Strukturtests oder Quellreview.

## Work items

### W-001 Unverzichtbare Verträge und vereinfachbare Modellprosa sind getrennt belegt

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Eine prüfbare Ausgangsbasis ordnet jede Workflow-Regel ihrem kanonischen Besitzer und entweder einer exakten Protokollgrenze oder vereinfachbarer Modellprosa zu.
Acceptance: `development/workflow-instruction-refactor.md` nennt je Regelgruppe Besitzer, Verbraucher, beobachtetes Fehlerrisiko und vorhandenen Verhaltenstest. Der Bericht misst `SKILL.md`, den gebauten Coordinator-Vertrag und repräsentative Executor-, Reviewer- und Repair-Prompts, bindet die Baseline an Quellrevision und Paketbytes und trennt strukturelle Prüfungen von Modell- und Laufzeitnachweisen. Role Marker, Aktivierung, Workspace- und Taskidentität, Guard-Revision und -Generation, Helperpflicht, Unit-Projektion, unverändertes `source_text`, Ergebnis-JSON, Wait- und Archivierungsnachweis, Compaction, Rollover, Reparaturgrenze, Modellverfügbarkeit, Git und externe Autorisierung sind ausdrücklich als präzise zu erhaltende Verträge klassifiziert.
Steps:
1. Inventarisiere `members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md`, `references/operations*.md`, `scripts/coordinator_contract.py`, `scripts/build_dispatch_prompt.py`, `scripts/manage_workflow_guard.py`, die Shared-Helper aus `../shared/runtime/` und die Promptprofile aus `../shared/prompting/`; ordne jede Regel genau einem Besitzer zu.
2. Erzeuge aus dem aktuellen gebauten Paket reproduzierbare Größen-, Hash- und Verhaltenstest-Baselines und dokumentiere nur die knappe dauerhafte Zuordnung in `development/workflow-instruction-refactor.md`; Rohprompts und vollständige Ausgaben bleiben im Workspace-temp.
Evidence: [Baseline report binds source revision b0be796 package receipt ad996979 and prompt hashes, Existing Workflow contract suite passed 80 tests before instruction changes, development/workflow-instruction-refactor.md maps every required contract to owner consumer risk and behavior proof]

### W-002 Entry Point und statische Regelbesitzer enthalten jede Regel genau einmal

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Die Skillbeschreibung und `SKILL.md` führen knapp zu Aktivierung, Role Gate und zuständigem Ablauf, während jede weitere statische Regel nur in ihrer kanonischen Referenz oder ihrem Helpervertrag steht.
Acceptance: Die Description benennt Fähigkeit, ausschließlich explizite Trigger und Abgrenzung ohne Startup-Ablauf. `SKILL.md` behält Voraussetzungen, installed-contract check, Role Gate, Launcher-/Coordinator-Auswahl, Helperpflicht und Autoritätsgrenzen. Native Argumentformen, Parking- und Aktivierungsdetails sowie Phasenregeln haben jeweils einen verlinkten Besitzer. Kein erlaubter oder verbotener Übergang geht verloren. Launcher, Coordinator und Kind wählen nach unveränderten Triggern denselben Pfad wie in der Baseline; Paket- und Routentests prüfen die tatsächliche Projektion statt bloß neue Formulierungen.
Steps:
1. Überarbeite `members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md` und seine Description nach Skillwriter und Skill Creator; verschiebe nur bereits zugeordnete Detailregeln zu ihren kanonischen Besitzern und bewahre die vor Projektzugriff nötigen Regeln im Entry Point.
2. Konsolidiere doppelte Workspace-, Task-Creation-, Writing-Profile-, Ergebnis- und Archivierungsregeln in den zuständigen `references/operations*.md` und Helperverträgen; ersetze Wiederholungen durch eindeutige Verweise oder Helperaufrufe.
3. Passe nur solche Tests unter `members/scoville-workflow-for-codex/development/tests/` an, die den unveränderten Vertrag über veraltete Wortlaute statt beobachtbares Verhalten prüfen.
Evidence: [SKILL.md routes conditional launcher detail to references/launcher.md and the suite manifest packages that owner, Entry tests verify explicit triggers ordered parking and activation fields and helper-owned task creation, Workflow contract tests verify helper results schemas bindings state transitions and required protocol literals]

### W-003 Der Coordinator lädt nur eindeutig ableitbare Regelpakete

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Der Coordinator erhält jederzeit alle für den sicheren nächsten Übergang nötigen Regeln; eine kleinere Regelmenge wird nur verwendet, wenn vorhandene autoritative Belege sie eindeutig bestimmen.
Acceptance: Vor einer Vertragsaufteilung ordnet `development/workflow-instruction-refactor.md` für Startup, Auswahl, Dispatch, Writer-Aktivierung, Reviewer, Wait, Resultatverarbeitung, Review, Acceptance, Stop, Compaction, Rollover sowie unbekannte Toolausgänge die vorhandenen Plan-, Guard- und nativen Lifecycle-Belege der vollständig benötigten Regelmenge zu. Mindestens zwei Reviewer- oder Wiederaufnahmeverläufe mit gleichem Guardzustand belegen, ob weitere autoritative Unterscheidungsmerkmale existieren. Nur eine eindeutige Zuordnung darf `scripts/coordinator_contract.py` in einen vollständigen Kern und deterministisch geladene Regelpakete teilen. Eine fehlende, falsche, veraltete, gekürzte, fremde oder aus mehreren möglichen Phasen frei gewählte Regelmenge blockiert vor Projekt- oder Planmutation. Mehrdeutige Zustände laden deterministisch die vollständige notwendige Regelmenge; fehlt ein belegbarer sicherer Auswahlweg, bleibt der vollständige Runtime-Vertrag erhalten und nur seine Prosa wird konsolidiert. Nach Compaction wird dieselbe vollständige Regelmenge aus Toolausgabe geladen. Plan und Guard bleiben die einzigen dauerhaften Zustandsbesitzer; ein neuer Phasenzähler oder eine neue Zustandsdatei allein für die Kürzung ist unzulässig. Die bestehenden Startup-, Dispatch-, Wait-, Result-, Review-, Accepted-, Stop-, Compaction- und Rolloverfehlerfälle bestehen mit unveränderter beobachtbarer Reaktion.
Steps:
1. Erstelle in `development/workflow-instruction-refactor.md` eine Zustand-zu-Regelpaket-Tabelle aus vorhandenen Plan-, Guard- und nativen Lifecycle-Belegen einschließlich Reviewer, Wait, Unterbrechung, Compaction und unbekannter Toolausgänge; prüfe ausdrücklich mehrere Abläufe mit demselben Guardzustand.
2. Entscheide anhand der Tabelle vor der Runtime-Änderung zwischen sicher gebundenen Regelpaketen und einem vollständig erhaltenen konsolidierten Vertrag; führe keinen neuen dauerhaften Phasenzähler oder frei gewählten Phasenparameter ein.
3. Implementiere die belegte Variante in `scripts/coordinator_contract.py` und `references/operations*.md`; erhalte exakte Helperpfade, Digests, vollständige Wiederherstellung und fail-closed Verhalten.
4. Ergänze fokussierte Regressionen für jede belegte Regelmengenauswahl sowie mehrdeutigen Zustand, alte Revision oder Generation, gekürzte Ausgabe, fremde Identität, Compaction und vollständigen nativen Creation-Ursprung.
Evidence: [State table proves selection review acceptance Stop and recovery can share the same authoritative guard state, coordinator_contract.py keeps every normal phase and accepts no model-selected phase argument, New ambiguous-state regression passes and no phase counter or persistent state file was added]

### W-004 Kind-Prompts und Tests sichern Verhalten statt wiederholten Wortlaut

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Executor, Reviewer und Repair erhalten kurze rollenbezogene Prompts mit unveränderten Autoritäts-, Kontext-, Ergebnis- und Delivery-Verträgen; Tests schützen das Verhalten und nur echte Protokollliterale bytegenau.
Acceptance: `scripts/build_dispatch_prompt.py` erzeugt weiterhin den exakten Role Marker, Dispatchvertrag, Guardbindung, Workspace, unveränderten Plan-Kontext, erlaubte Rolle, Git- und Publikationsgrenzen, Resultatschema, Compaction-Gate und Delivery-Bindung. Allgemeine Schreibregeln werden nur über die gebundenen Promptprofile geliefert. Wiederholte Begründungen und Alternativverbote ohne eigenen Fehlerfall sind entfernt. Tests prüfen Role Marker, Feldnamen und -reihenfolge, JSON-Schema, Digests, unveränderte Übertragung und Bindungen exakt; übrige Fälle prüfen beobachtete Zustandsübergänge und Fehlerreaktionen. Der erste Ausführer plus höchstens drei Repairs, Reviewer-Schwellen und Modellauflösung bleiben unverändert.
Steps:
1. Ordne in `scripts/build_dispatch_prompt.py` jede Promptzeile einem präzisen Vertrag aus W-001 zu und entferne oder vereinige nur unbelegte Wiederholungen; bewahre die klaren Abschnitte für Gate, Autorität, Arbeit, Ergebnis, Delivery und Eingaben.
2. Ersetze in `development/tests/test_contract.py` und den fokussierten Testdateien reine Prosa-Assertions durch Helper-, Schema- und Zustandsprüfungen, außer der konkrete Wortlaut oder die Bytefolge ist selbst Teil des Protokolls.
3. Vergleiche gebaute Executor-, Reviewer- und Repair-Prompts gegen die Baseline auf erhaltene Inputs, Autorisierung, Ergebnisse und Blockaden; dokumentiere Größenänderung getrennt von Wirksamkeit.
Evidence: [Candidate 2 preserves exact role unit guard workspace source_text result and delivery bindings across 82 passing contract tests, Representative executor reviewer and repair prompts are 17.5 17.0 and 17.0 percent smaller than baseline, Coordinator section extraction is heading-bound and regression-tested after the refactor exposed the prior order dependency]

### W-005 Der vereinfachte Workflow besteht Vertrags- und Laufzeitnachweise

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: []
Outcome: Der finale Workflow ist strukturell, verhaltensbezogen und in nativen Codex-Aufgaben gegen den bisherigen Vertrag geprüft, ohne aus kürzeren Prompts allein einen Nutzen abzuleiten.
Acceptance: Skill-Creator-Validierung, fokussierte Helpertests, vollständige Workflow-Tests, Suite-Buildtests, Paketprüfung, isolierter Export und Planprofilvalidierung bestehen auf dem finalen Baum. Eine Entwicklungsfallgruppe und getrennte verdeckte Schlussfälle prüfen mindestens explizite Aktivierung, falsche Rolle, unbekannte Creation, Writer-Aktivierung, Ergebniswiederherstellung, Archivierung, Compaction, Rollover, Reparaturgrenze und Stop in nativen Codex-Aufgaben. Alle obligatorischen nativen Erhaltungsfälle bestehen nach dem vor den Läufen festgelegten Bewertungsschlüssel; keine offene Kandidatenregression bleibt. Ein nicht ausführbarer erforderlicher Hostfall bleibt unverifizierte offene Acceptance und wird nicht durch Fixture, Strukturprüfung oder Quellreview ersetzt. Modell, Effort, Paketbytes, Prompts, Tools, Laufbudget und Ergebnisse sind dokumentiert. Ein Nutzen für Modellleistung oder Effizienz wird nur aus vorher benannten Ergebnis- und Kostenmaßen unter vergleichbaren Bedingungen abgeleitet; andernfalls berichtet der Nachweis ausschließlich Vertragserhaltung und gemessene Größenänderung. Ein abschließendes Astra-High-Review prüft Skill und Referenzen gegen Skillwriter, ursprüngliche Workflowintention und die als präzise klassifizierten Verträge ohne handlungsrelevanten Restbefund. Veröffentlichung und Installation bleiben offen.
Steps:
1. Führe die final betroffenen Struktur-, Helper-, Workflow-, Build-, Paket-, Export- und Planprüfungen aus und behebe nur ursächlich durch diese Überarbeitung entstandene Fehler.
2. Lege vor den Modellläufen Entwicklungs- und verdeckte Schlussfälle samt Bewertungsschlüssel fest; kläre notwendiges Modell, Effort und Laufbudget ausdrücklich und führe die autorisierten nativen Vergleiche gegen gebundene Baseline- und Kandidatenpakete aus.
3. Lasse den finalen Skill und alle geladenen Referenzen durch Astra High gegen Skillwriter, Zieltreue und die W-001-Vertragskarte prüfen; korrigiere bestätigte Befunde und wiederhole nur betroffene Nachweise.
Evidence: [Final Workflow contract suite passed 88 tests including six deterministic host-simulation scenarios and ordered Rollover instruction coverage, Skill Creator validation passed after removal of the obsolete compatibility frontmatter field, Suite development tests passed 23 and shared build export tests passed 46, Current Codex suite build receipt e3bac76d passed package freshness, Native Plan profile validation passed with 18 files and no diagnostics, Continued Astra Medium reviews workflow-refactor-astra-medium-20260925-06 and -08 returned FREIGABE for the final source iterations, First 24-run SOL Medium policy pilot remained diagnostic because both packages produced valid evaluator JSON in 2 of 12 runs, Second 24-run SOL Medium policy pilot produced readable actions and exposed a candidate Rollover ordering error that was corrected in the current source, Finale SOL-6-Medium-Qualifikation führte zwölf Aufgaben aus und bestätigte alle elf gültigen Fälle, Exakte Archivierungsaufrufe bestätigten archived:true für alle zwölf Testaufgaben, D02 war ungültig weil die Fixture den verpflichtenden Installed-Contract-Zustand ausließ und Wrong-Role nicht erreichte, H02 belegte einen Oraclefehler weil der Vertrag offene Befunde vor der Nutzerentscheidung erfasst, r3 bestand 90 Workflow-Tests 23 Suite-Tests und 46 gemeinsame Build- und Exporttests, r3-Paketprüfung bestätigte sechs Pakete und 115 Dateien und Skill Creator validierte den Workflow, r3-Buildreceipt 0fba8ea323665f68eee34ed95c6b882b09d1286fd3022e787eb316031f966e21 und Workflow-Dateikarte 345c3f27 binden 42 Dateien, Astra High workflow-final-astra-high-20260925-03 gab FREIGABE für Reviewer-Fortsetzung und Transport, D02R1 mit gpt-6-sol medium blockierte die fremde Taskidentität exakt nach dem r3-Vertrag und bestand den eingefrorenen Oracle, D02R1-Task 01a0d7cc-8244-72b3-bc0b-cce1a0e7a7e9 wurde nach Sicherung von ID und Ergebnis archiviert, D02R1-Manifest b80fe75a und Ergebnis 4b0879bf binden den bestandenen Wrong-Role-Nachweis, Abschließende Planprofilvalidierung prüfte 25 Dateien mit null Fehlern und null Warnungen]

### W-006 Rollenresultate verwenden ein geprüftes Zeilenprotokoll

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: [ADR-0036]
Outcome: Executor, Reviewer und Repair liefern ein festes einzeiliges Ergebnisprotokoll, das ein kanonischer Helper fail-closed validiert und intern ohne Semantikverlust strukturiert bereitstellt.
Acceptance: Der Helper akzeptiert nur `SCOVILLE_RESULT_V1` mit rollenabhängigen Pflichtfeldern, fester Reihenfolge, höchstens acht Findings und den festgelegten Zeichenlimits. Er lehnt unbekannte, doppelte, fehlende, mehrzeilige, falsch geordnete oder rollenwidrige Felder ab. Prompts, Ergebnisverarbeitung, Delivery-Bytevergleich, Compaction-Recovery und Reviewer- oder Repair-Weitergabe verwenden das Protokoll ohne manuell erzeugtes Ergebnis-JSON. Fokussierte Helper- und Recoverytests, vollständige Workflowtests, Suite-Buildtests, Paketprüfung, isolierter Export, Skill-Creator-Validierung und Planprofilvalidierung bestehen auf dem finalen Baum. Ein frischer Build wird in derselben Astra-Medium-Session gegen Skillwriter, Workflowintention und erhaltene Protokollgrenzen ohne handlungsrelevanten Restbefund geprüft.
Steps:
1. Sichere die aktuellen Ergebnisprotokollquellen, Tests und Paketbytes als Baseline und implementiere den kanonischen Parser in `members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/parse_role_result.py`.
2. Stelle `members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py`, `members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/inspect_native_context.py` und die betroffenen `references/operations*.md` auf das Zeilenprotokoll um, ohne Identitäts-, Delivery-, Recovery- oder Archivierungsgrenzen zu ändern.
3. Ergänze Verhaltenstests unter `members/scoville-workflow-for-codex/development/tests/` und paketiert den Helper über `suite.json`; führe die betroffenen und vollständigen Prüfungen sowie einen frischen isolierten Build aus.
4. Lasse den gebauten Kandidaten in der bestehenden Astra-Medium-Session prüfen, behebe bestätigte Befunde und wiederhole nur betroffene Nachweise.
Evidence: [Workflow contract suite passed 88 tests including dispatch identifier rejection and SCOVILLE_RESULT_V1 parser cases, Suite tests passed 23 and shared build and export tests passed 46, Codex build receipt 8f363ff7 passed freshness and package verification for 6 packages and 115 files, Final isolated export receipt 02ff5e79 contains 637 files and all 6 isolated payloads matched canonical package bytes, Skill Creator validation passed for the built Workflow package, Astra Medium review workflow-protocol-names-astra-medium-20260925-03 returned FREIGABE after result-protocol reviews -01 and -02]
