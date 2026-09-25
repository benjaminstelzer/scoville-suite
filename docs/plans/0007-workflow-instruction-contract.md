---
format_version: 1
id: PLAN-0007
status: draft
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

Status: todo
Depends on: []
Blocked by: []
Decisions: []
Outcome: Eine prüfbare Ausgangsbasis ordnet jede Workflow-Regel ihrem kanonischen Besitzer und entweder einer exakten Protokollgrenze oder vereinfachbarer Modellprosa zu.
Acceptance: `development/workflow-instruction-refactor.md` nennt je Regelgruppe Besitzer, Verbraucher, beobachtetes Fehlerrisiko und vorhandenen Verhaltenstest. Der Bericht misst `SKILL.md`, den gebauten Coordinator-Vertrag und repräsentative Executor-, Reviewer- und Repair-Prompts, bindet die Baseline an Quellrevision und Paketbytes und trennt strukturelle Prüfungen von Modell- und Laufzeitnachweisen. Role Marker, Aktivierung, Workspace- und Taskidentität, Guard-Revision und -Generation, Helperpflicht, Unit-Projektion, unverändertes `source_text`, Ergebnis-JSON, Wait- und Archivierungsnachweis, Compaction, Rollover, Reparaturgrenze, Modellverfügbarkeit, Git und externe Autorisierung sind ausdrücklich als präzise zu erhaltende Verträge klassifiziert.
Steps:
1. Inventarisiere `members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md`, `references/operations*.md`, `scripts/coordinator_contract.py`, `scripts/build_dispatch_prompt.py`, `scripts/manage_workflow_guard.py`, die Shared-Helper aus `../shared/runtime/` und die Promptprofile aus `../shared/prompting/`; ordne jede Regel genau einem Besitzer zu.
2. Erzeuge aus dem aktuellen gebauten Paket reproduzierbare Größen-, Hash- und Verhaltenstest-Baselines und dokumentiere nur die knappe dauerhafte Zuordnung in `development/workflow-instruction-refactor.md`; Rohprompts und vollständige Ausgaben bleiben im Workspace-temp.
Evidence: []
Next action: Aktuelle Quellen und gebaute Pakete an eine Quellrevision binden und die Regelbesitzer mit ihren vorhandenen Verhaltenstests inventarisieren.

### W-002 Entry Point und statische Regelbesitzer enthalten jede Regel genau einmal

Status: todo
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Die Skillbeschreibung und `SKILL.md` führen knapp zu Aktivierung, Role Gate und zuständigem Ablauf, während jede weitere statische Regel nur in ihrer kanonischen Referenz oder ihrem Helpervertrag steht.
Acceptance: Die Description benennt Fähigkeit, ausschließlich explizite Trigger und Abgrenzung ohne Startup-Ablauf. `SKILL.md` behält Voraussetzungen, installed-contract check, Role Gate, Launcher-/Coordinator-Auswahl, Helperpflicht und Autoritätsgrenzen. Native Argumentformen, Parking- und Aktivierungsdetails sowie Phasenregeln haben jeweils einen verlinkten Besitzer. Kein erlaubter oder verbotener Übergang geht verloren. Launcher, Coordinator und Kind wählen nach unveränderten Triggern denselben Pfad wie in der Baseline; Paket- und Routentests prüfen die tatsächliche Projektion statt bloß neue Formulierungen.
Steps:
1. Überarbeite `members/scoville-workflow-for-codex/scoville-workflow-for-codex/SKILL.md` und seine Description nach Skillwriter und Skill Creator; verschiebe nur bereits zugeordnete Detailregeln zu ihren kanonischen Besitzern und bewahre die vor Projektzugriff nötigen Regeln im Entry Point.
2. Konsolidiere doppelte Workspace-, Task-Creation-, Writing-Profile-, Ergebnis- und Archivierungsregeln in den zuständigen `references/operations*.md` und Helperverträgen; ersetze Wiederholungen durch eindeutige Verweise oder Helperaufrufe.
3. Passe nur solche Tests unter `members/scoville-workflow-for-codex/development/tests/` an, die den unveränderten Vertrag über veraltete Wortlaute statt beobachtbares Verhalten prüfen.
Evidence: []
Next action: Nach W-001 die Description und den Entry Point gegen die belegte Besitzerkarte kürzen.

### W-003 Der Coordinator lädt nur eindeutig ableitbare Regelpakete

Status: todo
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
Evidence: []
Next action: Nach W-002 die Zustand-zu-Regelpaket-Tabelle erstellen und vor jeder Runtime-Aufteilung die sichere Variante gegen mehrdeutige gleiche Guardzustände bestimmen.

### W-004 Kind-Prompts und Tests sichern Verhalten statt wiederholten Wortlaut

Status: todo
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Executor, Reviewer und Repair erhalten kurze rollenbezogene Prompts mit unveränderten Autoritäts-, Kontext-, Ergebnis- und Delivery-Verträgen; Tests schützen das Verhalten und nur echte Protokollliterale bytegenau.
Acceptance: `scripts/build_dispatch_prompt.py` erzeugt weiterhin den exakten Role Marker, Dispatchvertrag, Guardbindung, Workspace, unveränderten Plan-Kontext, erlaubte Rolle, Git- und Publikationsgrenzen, Resultatschema, Compaction-Gate und Delivery-Bindung. Allgemeine Schreibregeln werden nur über die gebundenen Promptprofile geliefert. Wiederholte Begründungen und Alternativverbote ohne eigenen Fehlerfall sind entfernt. Tests prüfen Role Marker, Feldnamen und -reihenfolge, JSON-Schema, Digests, unveränderte Übertragung und Bindungen exakt; übrige Fälle prüfen beobachtete Zustandsübergänge und Fehlerreaktionen. Der erste Ausführer plus höchstens drei Repairs, Reviewer-Schwellen und Modellauflösung bleiben unverändert.
Steps:
1. Ordne in `scripts/build_dispatch_prompt.py` jede Promptzeile einem präzisen Vertrag aus W-001 zu und entferne oder vereinige nur unbelegte Wiederholungen; bewahre die klaren Abschnitte für Gate, Autorität, Arbeit, Ergebnis, Delivery und Eingaben.
2. Ersetze in `development/tests/test_contract.py` und den fokussierten Testdateien reine Prosa-Assertions durch Helper-, Schema- und Zustandsprüfungen, außer der konkrete Wortlaut oder die Bytefolge ist selbst Teil des Protokolls.
3. Vergleiche gebaute Executor-, Reviewer- und Repair-Prompts gegen die Baseline auf erhaltene Inputs, Autorisierung, Ergebnisse und Blockaden; dokumentiere Größenänderung getrennt von Wirksamkeit.
Evidence: []
Next action: Nach W-003 die Kind-Promptzeilen gegen die Besitzerkarte klassifizieren und die Protokollliterale von erklärender Prosa trennen.

### W-005 Der vereinfachte Workflow besteht Vertrags- und Laufzeitnachweise

Status: todo
Depends on: [W-004]
Blocked by: []
Decisions: []
Outcome: Der finale Workflow ist strukturell, verhaltensbezogen und in nativen Codex-Aufgaben gegen den bisherigen Vertrag geprüft, ohne aus kürzeren Prompts allein einen Nutzen abzuleiten.
Acceptance: Skill-Creator-Validierung, fokussierte Helpertests, vollständige Workflow-Tests, Suite-Buildtests, Paketprüfung, isolierter Export und Planprofilvalidierung bestehen auf dem finalen Baum. Eine Entwicklungsfallgruppe und getrennte verdeckte Schlussfälle prüfen mindestens explizite Aktivierung, falsche Rolle, unbekannte Creation, Writer-Aktivierung, Ergebniswiederherstellung, Archivierung, Compaction, Rollover, Reparaturgrenze und Stop in nativen Codex-Aufgaben. Alle obligatorischen nativen Erhaltungsfälle bestehen nach dem vor den Läufen festgelegten Bewertungsschlüssel; keine offene Kandidatenregression bleibt. Ein nicht ausführbarer erforderlicher Hostfall bleibt unverifizierte offene Acceptance und wird nicht durch Fixture, Strukturprüfung oder Quellreview ersetzt. Modell, Effort, Paketbytes, Prompts, Tools, Laufbudget und Ergebnisse sind dokumentiert. Ein Nutzen für Modellleistung oder Effizienz wird nur aus vorher benannten Ergebnis- und Kostenmaßen unter vergleichbaren Bedingungen abgeleitet; andernfalls berichtet der Nachweis ausschließlich Vertragserhaltung und gemessene Größenänderung. Ein abschließendes Astra-Review prüft Skill und Referenzen gegen Skillwriter, ursprüngliche Workflowintention und die als präzise klassifizierten Verträge ohne handlungsrelevanten Restbefund. Veröffentlichung und Installation bleiben offen.
Steps:
1. Führe die final betroffenen Struktur-, Helper-, Workflow-, Build-, Paket-, Export- und Planprüfungen aus und behebe nur ursächlich durch diese Überarbeitung entstandene Fehler.
2. Lege vor den Modellläufen Entwicklungs- und verdeckte Schlussfälle samt Bewertungsschlüssel fest; kläre notwendiges Modell, Effort und Laufbudget ausdrücklich und führe die autorisierten nativen Vergleiche gegen gebundene Baseline- und Kandidatenpakete aus.
3. Lasse den finalen Skill und alle geladenen Referenzen durch Astra gegen Skillwriter, Zieltreue und die W-001-Vertragskarte prüfen; korrigiere bestätigte Befunde und wiederhole nur betroffene Nachweise.
Evidence: []
Next action: Nach W-004 den finalen Quellbaum einfrieren und zuerst die deterministischen Prüfungen ausführen; Modellläufe benötigen ein ausdrücklich festgelegtes Budget.
