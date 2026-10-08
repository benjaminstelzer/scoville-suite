---
format_version: 1
id: PLAN-0039
status: completed
created: 2026-10-08
updated: 2026-10-08
---

# Skilltexte und beobachtete Ablaufprobleme klären

## Goal

Alle Skilltexte der Suite prägnanter und eindeutiger machen. Beobachtete Fehlinterpretationen durch kleine allgemeine Korrekturen beheben; Intent, Freigaben, Rollen, vollständige Übertragung und Betriebssystemgrenzen erhalten. Ausgangsbefunde: PLAN-0038 / W-001, Steps 3–6.

## Non-goals

Keine Eingriffe in den laufenden EMPCO-Workflow. Keine Reviewarchive, Laufhistorie oder zusätzlichen Pflichtprüfungen ohne konkreten Nutzen.

## Work items

### W-001 Dokumente sicher lesen und vollständig übertragen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0203, ADR-0204]
Outcome: Reader- und Ausgabeanweisungen führen eindeutig zum vollständigen Lesen statt zur Ausführung eines Dokuments oder zum Abschneiden.
Acceptance: Dokument- und Programmpfad sind unterscheidbar. Die kleinste geltende Ausgabegrenze umfasst die gesamte Ausgabe. Teilfolgen bleiben vollständig; große erforderliche Inhalte erreichen den Empfänger unverändert.
Instructions: []
Steps:
1. [status: done] Behebe F-001 und F-002 in ../shared/prompting/common.md, ../shared/runtime/native_task_arguments.py::file_read_instruction und helper.policy in ../shared/build/build_suite.py: festes check_text_size.py als Programm, Dokument nur hinter --file, .py-Regel gemäß ADR-0203. Den sicheren argv-Launcher erhalten. Teilbudget unverändert lassen; Wechsel beginnt bei Teil 1. Keine pauschale JSON-Sperre. Gemeinsame Fragmente ohne positionsabhängige Links oder unaufgelöste Profilblöcke verwenden; Fallbacks bleiben beim passenden Verbraucher.
2. [status: done] Ergänze ausschließlich native Quellen um eine ausführbare functions.exec-Vorlage mit echter Host-API: gleiche äußere, innere und Checker-Grenze, vollständiges gerendertes output unverändert weitergeben. Vollständigkeit und Befehlsstatus getrennt beurteilen: --run kann einen fehlgeschlagenen Kindbefehl vollständig erfassen; dessen Erfolg darf daraus nicht abgeleitet werden. Laufende Prozesse, Reader-/Capturefehler oder unvollständiger Pflichtinput sperren abhängige Arbeit. Erwartete Fehlernachweise bleiben auswertbar. Keine Fehlerausgabe verwerfen oder ungemessene Statuszeile ergänzen; vollständigen Dateifallback erhalten. Selector-Budgetdiagnose erklärt Auswahlgrenze getrennt von Anzeigegrenze.
3. [status: done] Platziere den Reader in members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_manager_handoff.py vor dem Leseauftrag; Reihenfolge Protokoll → READY → START → bei Nachfolge HANDOFF_REQUEST → Assignment erhalten. Übernahmegates im Assignment und Protokoll beibehalten, nicht im Spawntext verdoppeln. Native Dispatch- und Ask-Prompts binden die benannten Python-/Checkerpfade eindeutig; check_text_size --file-Hilfe unterscheidet Dokumentlesen und Größenprüfung. Entferne danach lokale Markdown-Sonderhinweise.
4. [status: done] Vereinheitliche Python 3.11+ gemäß ADR-0204 in ../shared/runtime/python_discovery.md, Skill-Verbrauchern und Kompatibilitätsangaben einschließlich Paket-/README-Metadaten; entferne die Plan-General-3.10-Zusage. Prüfe vor dem ersten Helper die dokumentierte Runtime und nutze den verifizierten Interpreter für python, <verified-python> und Python-Aufrufe hinter --run --. Bestehende Profil- und Fallbackgrenzen erhalten.
5. [status: done] Teste Reader-Aufrufe mit Leerzeichen, Unicode und Apostrophen, Verzeichnisfehler, vollständige Teilfolgen sowie erfolgreiche und fehlgeschlagene Dateilieferung auf Windows und Linux. Prüfe tatsächlich gelesene Inhalte, vollständige Diagnosen und Nachfolge-Reihenfolge.
Evidence: Reader und vollständiger Transfer bestehen auf Windows/Linux; gebaute Manager-/Dispatch-Consumer bestehen. Python 3.11+ freigegeben; Textwirkung bleibt ohne Modellnachweis.

### W-002 Zugewiesene Reviewquellen eindeutig erlauben

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der Reviewer kann die ausdrücklich beauftragten Quellen prüfen, ohne seine Rolle oder Autorität auszuweiten.
Acceptance: Benannte Planpunkte und Decisions sind als begrenzte Review-Evidenz lesbar. Pflege, Tests und zusätzliche Kontextsuche bleiben ausgeschlossen.
Instructions: []
Steps:
1. [status: done] Behebe F-003 in members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py und im selben Skill in references/operations-dispatch.md: exakt benannte Plan-/Decisionquellen sowie zuständige Plan-Feldregeln für einen beauftragten Feldreview sind lesbar; keine zusätzliche Ausführungsbefugnis. Supplemental context nennt genaue Pfade und Abschnitte.
2. [status: done] Prüfe auf Windows und Linux einen Reviewauftrag mit benannter Plan-/Decisionquelle sowie die erhaltenen Verbote von Pflege, Tests und freier Kontextsuche. Keine zusätzliche Reviewrunde im regulären Workflow.
Evidence: Benannte Reviewquellen sind eng erlaubt; Pflege und Tests bleiben verboten. Gebaute frische und fortgesetzte Reviewaufträge bestehen auf Windows/Linux; Modellwirkung noch offen.

### W-003 Acceptance beim Ownerwechsel und Feldreview schlank halten

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Ownerwechsel erhalten notwendige Abnahmebedingungen; beauftragte Reviews nativer Planfelder verwenden die zuständigen Feldregeln.
Acceptance: Jede weiterhin bindende Bedingung steht einmal oder als genauer Originalverweis in Acceptance; schon erfüllte Garantien bleiben erhalten. Aktionen und Ergebnisse stehen in ihren zuständigen Feldern. Der Code-Reviewpfad lädt die einschlägigen Planregeln.
Instructions: []
Steps:
1. [status: done] Behebe F-004 beim Feld-Owner members/scoville-plan/scoville-plan/references/edit.md; members/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md verweist darauf: autorisiert verschobene Restarbeit erhält alle weiter bindenden Bedingungen einschließlich schon erfüllter Garantien einmal oder als exakten Pfad-/Abschnittsverweis. Zuordnung in Steps, angenommene Beiträge und Grenzen in Evidence; keine erledigten Aktionen oder Ergebnisse in Acceptance. Ein bloßer Manager-/Worker-Handoff desselben Items ändert dessen Felder und Kriterien nicht.
2. [status: done] Ergänze members/scoville-code/scoville-code/references/planning-and-decisions.md und die Einstiegsrouten von Code und Plan für beauftragte Reviews nativer Felder um Plan/read-only und die einschlägigen Feldregeln. Standalone nutzt Plan nur, wenn bereits verfügbar und anwendbar. Regeln bleiben bei Plan; keine zusätzliche Reviewrunde.
3. [status: done] Teste auf Windows und Linux einen Ownerwechsel und einen beauftragten Feldreview: Restbedingungen bleiben erhalten, Aktionen und Ergebnisse landen in den richtigen Feldern, der Review verwendet Planregeln.
Evidence: Gebauter Feldtest bewahrt Acceptance bei Ownerwechsel; Reviewer liest zuständige Regeln ohne Tests oder Pflege. Planhelper auf Windows/Linux bestehen; kein nativer Linux-Agentenbeleg.

### W-004 Skilltexte der gesamten Suite prägnanter und klarer formulieren

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Einstieg, Referenzen und erzeugte Anweisungen geben Intent, nächste Handlung und wichtige Verzweigungen verständlich und ohne unnötige Wiederholung weiter.
Acceptance: Konkrete Missverständnisse werden an ihrer zuständigen Quelle behoben. Notwendige Bedingungen, Ausnahmen und Freigaben bleiben erhalten; Kürze allein gilt nicht als Qualitätsnachweis. Jeder unterschiedliche manuelle Python-Helper-Fallback wird mit Luna auf Windows und Linux praktisch geprüft; bestätigte Fehler werden korrigiert und nachgetestet.
Instructions: []
Steps:
1. [status: done] Straffe ../shared/prompting/common.md ohne Informationsverlust und wiederholte Budgeterklärungen. Ohne Befehlsrecht nur erlaubte UTF-8-Reader mit geordneten Bereichen nutzen; ungelesene erforderliche Inhalte sperren abhängige Arbeit. Dies ersetzt keine verpflichtende Helperoperation. Im Plan-Skill verweisen references/edit.md und references/read-only.md für Capture auf den Einstieg, erhalten aber Diagnose-Stopp, vollständige Kontextpflicht und Reviewer-Schreibverbot für Quellcaptures. Ask-Claude erhält keine native Dateitransferlogik oder zusätzlichen Befehlsrechte.
2. [status: done] Kläre Workflow-Einstieg und operations.md: Collaboration-Tools direkt statt in functions.exec; Reviewtaktung als klare Verzweigung. Begrenzte Diff-/Evidenzprüfung, Verbot doppelter Workerdiagnose/-tests und materieller Reviewgrund bleiben erhalten. Lange Handoff-/Verification-Tabellenzellen im manager-protocol.md nur verlagern; Empfänger, Reihenfolge, Quieszenz und Übernahmegates erhalten.
3. [status: done] Kläre im Workflow-Skill references/run-feedback.md mit expliziten Rollen Manager, Kind und Runner samt bestehender Startup-Ausnahme. Abschluss nur durch complete; status --kind completed ist Altkompatibilität ohne Reportabschluss, ebenso in scripts/run_feedback.py-Hilfe kennzeichnen. assets/workflow.toml kommentiert Projekt-Overrides, wirkungsloses Pinning und Schwellen für alle Kinder; Werte unverändert.
4. [status: done] Straffe im Code-Skill SKILL.md-Safeguards und references/validation.md: Risiko bestimmt Untersuchungsbedarf, keine pauschale Maschinerie. Bei Zusammenlegung Rerun-Gründe, Ursachen-Checkpoint nach zwei gescheiterten Korrekturen, Host-Versuchslimits, veraltete Aggregatnachweise und begrenzte Aufbewahrung erhalten. Keine neue Pflichtprüfung nach Erfolg.
5. [status: done] Straffe im UI-Skill SKILL.md und WordPress-Referenzen: Admin-Routing vor Einordnung; unbekannte oder ausgeschlossene Ownership nicht in die General-Route verschieben. Runtime, Versionen und Qualitätsroute erhalten. Flex-Details nach references/wordpress/spacing.md verlagern, Default für allow/deny/unknown und funktionierenden Margin-Flow erhalten; Adapter behält Owner-Leiter und Verweis. Überschrift Headings bereinigen.
6. [status: done] Kläre im Ask-Skill references/native.md mit gültigem task_name-Beispiel aus Kleinbuchstaben, Ziffern und Unterstrichen. Setup entfernt chat pinning aus Beschreibung und irreführender Hilfe, behält aber konkrete Obsolete-Diagnose. Im Plan-Skill nennt scripts/select_context.py gültige Unit-Beispiele und aktiven oder benannten Plan; zugehörigen Fallbacksatz korrigieren. Handoff bündelt Snapshot-Verantwortung; Cleanup verwendet einheitlich shared writing rules.
7. [status: done] Prüfe betroffene Verweise und Verbraucher. Optionale Leerzeilen-/Einrückungskorrekturen nur bei ohnehin bearbeiteten Texten; keine eigenen Prüfpflichten. family-Wording in suite.json kann bei der Quellenpflege geklärt werden; daraus keinen ungeprüften README-/Renderingeffekt behaupten. README-Fragmente und fertige Renderings gehörten nicht zum Textreview.
8. [status: done] Teste zusätzliche bestätigte und korrigierte Fehler gezielt auf Windows und Linux. Reine redaktionelle Änderungen begründen keine neue pauschale Testkampagne. Die sprachlichen Missverständnisszenarien sind Hypothesen, keine nachgewiesene Luna-Wirkung.
9. [status: done] Ermittle unterschiedliche Python-Fallbacks aus den Helperverträgen. Teste nur deren manuelle Routen mit Luna auf Windows und Linux, einschließlich relevanter Erfolgs- und Stoppfälle; keine Wiederholung der gesamten Skills. Bewerte tatsächliche Ergebnisse, korrigiere bestätigte Fehler und lege Umsetzungen sowie Nachtests beiden Reviewern vor.
Evidence: Opus 5.5/high und GPT 6.1/xhigh: PASS für Korrekturen und gebaute Consumer. Drei Python-Fallbackrouten mit Luna/medium auf Windows und WSL-Linux geprüft; gezielte Nachtests bestehen.

### W-005 Konsistente Suitepakete aus den korrigierten Quellen erzeugen

Status: done
Depends on: [W-001, W-002, W-003, W-004]
Blocked by: []
Decisions: []
Outcome: Die erzeugten Pakete geben die korrigierten Anweisungen mit ihren benötigten Ressourcen und Profilgrenzen konsistent weiter.
Acceptance: Erzeugte Pakete enthalten ihre benötigten Dateien und funktionsfähigen Aufrufe. General- und Codex-Profilgrenzen sowie offene Plattformnachweise bleiben korrekt ausgewiesen.
Instructions: []
Steps:
1. [status: done] Erzeuge Pakete aus den kanonischen Quellen. Prüfe Struktur, Verweise, benötigte Dateien und relevante gebaute Aufrufe auf Windows und Linux. Kein Test auf wechselnde Formulierungen im Source-Material.
2. [status: done] Schließe mit den gezielten Nachweisen der zuständigen Fehlerpunkte und konkret verbleibenden Grenzen ab; keine erneuten unveränderten Prüffälle oder Reviewarchive.
Evidence: Vier Profile erzeugt; Inventar, Ressourcen und betroffene Aufrufe auf Windows/WSL-Linux geprüft. Runtime-CI und Release-Abnahme stehen aus.

