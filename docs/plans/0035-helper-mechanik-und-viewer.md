---
format_version: 1
id: PLAN-0035
status: completed
created: 2026-10-05
updated: 2026-10-07
---

# Mechanische Helper-Prüfungen und bedienbare Viewer-Menüs

## Goal

Vorhandene Plan- und Workflow-Helper übernehmen eindeutige Mechanik und liefern
direkt verwendbare Ergebnisse. Inhalt, Auswahl, Ermessen, Autorisierung und
Acceptance bleiben beim Agenten. Fehler liefern eine klare Diagnose mit
korrigiertem Aufruf und keine Teilausgabe. Plan-Dateien werden direkt bearbeitet:
„No planning CLI is a write path“ bleibt gültig. Automatisch mitgegeben werden
nur Einschränkungen. Die maschinelle Pfad- und Fehlerausgabenprüfung
erfolgt vor den abschließenden Gesamtläufen. Lange Viewer-Menüs bleiben
der letzte Umsetzungspunkt.

W-009 übernimmt gemäß ADR-0177 die finale Restabnahme aus PLAN-0034.
Sol 6.1/high prüft über Ask je Arbeitspunkt und verblindet je gesammelter
Testgruppe; für W-007 entfällt das zusätzliche Abschlussreview (ADR-0186).
Bestätigte Fehler werden korrigiert und betroffene Nachweise erneuert.

Kanonische Quellen liegen in skills/private/scoville-suite und
skills/private/shared. Paketvarianten entstehen nur als temporäre Testprodukte
im vorhandenen Desktop-Testprojekt unter test/plan0035, keine Änderungen an
bestehenden packages/, Exporten, skills/public/, skills/temp/release/ oder
scoville-agent-dev. Ausgelieferte Inhalte bleiben Englisch. Jedes ausgelieferte
Runtime-Skript besitzt einen exakten helper_contracts-Eintrag in suite.json als
aufrufbarer Helper oder interne Bibliothek. Aufrufbare Helper erhalten nur bei
General-Auslieferung ihren Fallback unter references/fallbacks/. Codex-Pakete
enthalten weder Fallbacks noch Verweise darauf.
Jeder geänderte Helper wird mit seinem tatsächlichen nächsten Verbraucher sowie
einem ungültigen und dem korrigierten Aufruf geprüft. Erweitert wird die
bestehende Mechanik. Semantische Entscheidungen werden nicht automatisiert. Alle ausgelieferten
Helper, Pfade und Aufrufe müssen unter Windows, macOS und Linux funktionieren
(ADR-0183); Python-Plattformprüfungen über GitHub Actions ausführen und je OS
ausweisen. Native lokale Consumer-Proben getrennt belegen; WSL ergänzend nutzen.

## Non-goals

- Keine automatische Übernahme von Goal oder Decisions in Dispatch-Aufträge.
- Keine schreibenden Plan-Helper oder Zustandsautomaten für den Runner.
- Kein automatisches Anheben von Ausgabebudgets.
- Keine Nachfolgerwahl durch Returns oder Prioritäten als Helper-Logik.
- Keine neuen Helper für Code, UI, Handoff oder Cleanup.
- Kein Commit, Push, CI-Lauf, native Viewer-Kompilierung, Installation oder
  Veröffentlichung ohne die konkrete Nutzerfreigabe. Kein lokales Rust.

## Work items

### W-001 Workflow-Abschluss in einem Helper-Aufruf

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0175, ADR-0179]
Outcome: run_feedback.py complete schließt den Laufreport und liefert anschließend die Completed-Nachricht in einem Aufruf.
Acceptance: complete übernimmt sämtliche Prüfungen von finish --completed. Ein Fehlschlag erzeugt weder Completed-Nachricht noch partiellen Abschluss. Saubere, dokumentierte Problemfälle und bereits abgeschlossene Reports sind geprüft; wiederholter Abschluss verändert keinen fertigen Report und erhält dieselbe Abschlusssemantik. Bestehende Unterbefehle bleiben kompatibel. Der Manager verwendet die erfolgreiche Ausgabe unmittelbar und der Runner zeigt sie unverändert an. Ungültiger und korrigierter Aufruf sowie Sol 6.1/high-Review sind belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/run_feedback.py den Abschlussvertrag einschließlich wiederholtem Aufruf bestimmen, complete implementieren und Fehler-/Erfolgsfälle in members/scoville-workflow-for-codex/development/tests/test_run_feedback.py prüfen.
2. [status: done] In derselben Skill-Quelle references/operations.md bei Complete and exit und references/run-feedback.md bei Completion nur den Ein-Aufruf-Weg beschreiben. Den tatsächlichen Manager-/Runner-Verbrauch einschließlich Fehlermeldung prüfen und den vollständigen Punkt durch Ask mit Sol 6.1/high reviewen.
Evidence: Abschluss-Helper und Windows-Consumer geprüft; Sol-Review und Korrekturen abgeschlossen, finale Wiederholung bei W-007.

### W-002 Auftragsdateien ohne manuelle Pfadkonstruktion

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0181, ADR-0175, ADR-0178, ADR-0179, ADR-0182, ADR-0183]
Outcome: Frische Create-Dispatches und Manager-Starts erzeugen ihre eindeutige Auftragsdatei selbst und liefern sofort verwendbare native Aufrufe.
Acceptance: Beide Builder veröffentlichen vollständige UTF-8-Dateien atomar ohne Überschreiben; Fehler liefern kein Erfolgs-JSON und hinterlassen keine unvollständige Auftragsdatei. Automatische und explizite --assignment-file-Pfade funktionieren. Der absolute Pfad steht im JSON-message des unverändert nutzbaren nativen Fünf-Felder-Aufrufs, ohne zusätzlichen spawn_agent-Parameter. Native Children lesen die Datei im tatsächlich verwendeten Codex-Sandbox-Modus vor Projektarbeit; Manager beachten READY/START. Automatische und explizite Pfade funktionieren auf Windows, Linux und macOS mit den jeweiligen temporären Verzeichnissen, absoluten Pfadformaten, Trennzeichen und Shell-Quoting, auch bei Leerzeichen und Unicode. Es gibt keine Windows-Annahme oder hartcodierten Hostpfade. Der Standardort liegt auf jedem unterstützten Betriebssystem außerhalb des Projektbaums; erfolgreiche Python-Lektüre ist über Actions je OS und native Codex-Lektüre im verwendeten lokalen Sandbox-Modus belegt (ADR-0183). Recovery bleibt direkt und dateilos. Kollision, nicht lesbarer Ort, ungültiger und korrigierter Aufruf sowie Sol 6.1/high-Review sind belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py und build_manager_handoff.py plattformgerechte automatische Pfadwahl und atomare Veröffentlichung für Windows, Linux und macOS ergänzen; gemeinsame Mechanik bei Bedarf in ../shared/runtime/native_task_arguments.py pflegen. Frische Executor-, Reviewer-, Manager-Start-/Nachfolger-Aufträge sowie dateiloses Recovery prüfen.
2. [status: done] In derselben Skill-Quelle SKILL.md und references/operations-dispatch.md manuelle Pfadregeln durch Helper-Aufrufe ersetzen; helper_contracts und erforderliche Profilregeln abgleichen und Ask-Sol 6.1/high-Review abschließen.
3. [status: done] Lokale native Verbraucher auf lesbare vollständige Dateien und unveränderte Kontrollreihenfolge prüfen. Python-Temp-/Pfad-/Unicode-/Quoting-Verhalten über Actions auf Windows, Linux und macOS nachweisen (ADR-0183); WSL ergänzend vorbereiten.
Evidence: Auftragsdateien mit nativen Windows-/WSL-Consumern und Drei-OS-Actions geprüft; Sol-Review nach Testkorrekturen bestanden.

### W-003 Budgetfehler liefern den ausführbaren Korrekturaufruf

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0181, ADR-0175, ADR-0179, ADR-0183, ADR-0184, ADR-0185]
Outcome: Dispatch und Fortschrittsmeldung nennen bei OUTPUT_BUDGET_EXCEEDED den vollständigen, plattformgerecht gequoteten Korrekturaufruf.
Acceptance: build_dispatch_prompt.py und run_feedback.py progress liefern Diagnose und vollständigen Aufruf mit --max-output-bytes <required_bytes>, erhalten übrige Argumente und geben keinen partiellen Erfolg aus. Der Korrekturaufruf funktioniert unverändert mit Leerzeichen und relevanten Sonderzeichen auf unterstützten Shells wie checkpoint_command(). Budgets steigen nie automatisch. Übersteigt required_bytes eine gesetzte Obergrenze, bleibt der Vorgang offen; der Manager holt die nötige Entscheidung ein. Tatsächlicher Consumer, ungültiger und korrigierter Aufruf sowie Sol 6.1/high-Review sind belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py und run_feedback.py vorhandene Budgetdiagnosen und checkpoint_command()-Quoting erweitern. Originalargumente, Shell-Quoting, zu kleine und ausreichende Budgets einschließlich Caller-Obergrenze prüfen.
2. [status: done] In derselben Skill-Quelle references/operations-dispatch.md die Pre-dispatch-Korrektur auf den vollständigen Helper-Vorschlag verweisen lassen; direkte Ausführung des korrigierten Aufrufs prüfen und Ask-Sol 6.1/high-Review abschließen.
3. [status: done] Consumer-Verhalten am finalen Stand prüfen; offene native Empfänger- und Plattformnachweise vollständig abnehmen.
Evidence: Korrekturaufruf im nativen Consumer geprüft; Actions und Paketbindungen bestanden. Sol-Review durchgeführt.

### W-004 Plan-Non-goals erreichen jeden Dispatch unverändert

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0181, ADR-0174, ADR-0175, ADR-0179, ADR-0183]
Outcome: Jeder Executor-, Reviewer-, Korrektur- und Recovery-Auftrag erhält die wörtlichen Plan-Non-goals aus der Selector-Ausgabe.
Acceptance: Der Non-goals-Inhalt bleibt verlustlos unter Plan-wide exclusions (Non-goals) erhalten, auch bei Recovery ohne erneute vollständige erledigte Arbeit. Goal und Decision-Abschnitte werden nicht automatisch eingesetzt. Eine begründete UTF-8-Größenobergrenze ist dokumentiert und an der Grenze sowie darüber geprüft; Überschreitung erzeugt eine konkrete Diagnose ohne Teilausgabe. Automatische Einschränkungen ändern keine Rollenbefugnis. Tatsächliche Empfänger befolgen die Ausschlüsse; ungültiger und korrigierter Aufruf sowie Sol 6.1/high-Review sind belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py plan.non_goals übernehmen, eine angemessene begründete Größenobergrenze bestimmen und alle Dispatch-Routen einschließlich Korrektur und Recovery mit Grenz-/Fehlerfällen prüfen.
2. [status: done] In derselben Skill-Quelle references/operations-dispatch.md Non-goals aus der supplemental-context-Auswahl entfernen. Der Manager wählt weiterhin relevante Goal-Teile, geltende ADR-Vorgaben, Berechtigungen und Abhängigkeitsergebnisse. Ask-Sol 6.1/high-Review abschließen.
3. [status: done] Tatsächliche Verbraucher am finalen Stand prüfen und die offenen Empfänger-Nachweise vollständig abnehmen.
Evidence: Non-goals-Übertragung und gezielte Nachtests bestanden; Sol-Review durchgeführt. Plattform-/Consumer-Nachweise bleiben auf geprüfte Wege begrenzt.

### W-005 Nächste IDs nur lesend ermitteln

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0181, ADR-0175, ADR-0179, ADR-0183, ADR-0184, ADR-0185]
Outcome: Der Selector liefert kollisionsfreie nächste Work-Item-, Plan- und Decision-IDs sowie die erforderlichen Dateinamensmuster ohne Schreibwirkung.
Acceptance: --next-id work-item|plan|decision liefert höchste Nummer plus eins ohne Lückenreuse oder Kollision mit IDs/Dateinamen; work-item verlangt --plan, Plan/Decision nennen das Dateinamensmuster. Lückenhafte Belegung, Konflikte zwischen Dateinamen und Metadaten und Grenzen gültiger ID-Formate sind geprüft; keine IDs werden reserviert und keine Dateien geschrieben. Der tatsächliche Plan-Agent kann die Ausgabe direkt für die nachfolgende manuelle Anlage verwenden. Ungültiger und korrigierter Aufruf, General-Fallback, Codex-Ausschluss und Sol 6.1/high-Review sind belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-plan/scoville-plan/scripts/select_context.py den next-id-Modus mit eindeutigen Argumenten ergänzen. Alle drei ID-Arten, höchste Nummer aus ID und Dateiname, Lücken, Kollisionen, Formatgrenzen und unveränderte Projektdateien prüfen.
2. [status: done] In derselben Skill-Quelle references/fallbacks/select_context-fallback.md für General und die ID-Regeln in references/edit.md, native-project-lifecycle.md und native-decision-format.md aktualisieren. Lokale manuelle Anlage mit unveränderter Ausgabe sowie Fehler-/Korrekturaufrufe prüfen; Ask-Sol 6.1/high-Review abschließen.
3. [status: done] Manuelle Anlage durch den tatsächlichen Plan-Agenten am finalen Stand mit der unveränderten Ausgabe prüfen; offene native Consumer-Abnahme vollständig belegen.
Evidence: Nächste IDs durch tatsächliche native Anlage verwendet; Actions und Paketbindungen geprüft. Sol-Review durchgeführt.

### W-008 Strukturelle Startvoraussetzungen nur lesend prüfen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0181, ADR-0175, ADR-0179, ADR-0183]
Outcome: Der Selector liefert Status und verletzte strukturelle Startbedingungen eines benannten Items, ohne es auszuwählen, zu autorisieren oder zu starten.
Acceptance: --check-start W-NNN liefert Itemstatus, Abhängigkeitsstatus, Blocker, andere in_progress-Items, current_item-Abgleich, verlinkte offene Proposals und verletzte strukturelle Startbedingungen. Draft-/inaktive Plans sowie terminale, todo, paused und bereits gestartete Items werden eindeutig unterschieden. Erfolg ist kein Autorisierungs- oder Acceptance-Nachweis. Alle Aufrufe bleiben read-only. Der tatsächliche Plan-Agent verwendet die Fakten unverändert für seine Startentscheidung, ohne Berechtigungen aus ihnen abzuleiten. Ungültiger und korrigierter Aufruf, General-Fallback, Codex-Ausschluss und Sol 6.1/high-Review sind belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-plan/scoville-plan/scripts/select_context.py den check-start-Modus mit eindeutigen Modus-/Plan-Argumenten ergänzen. Strukturbedingungen, fehlende oder unklare Auswahl, offene Proposals, paused-Resume und bereits gestartete Items sowie unveränderte Projektdateien prüfen.
2. [status: done] In derselben Skill-Quelle references/fallbacks/select_context-fallback.md und references/edit.md auf die Faktenprüfung verweisen. Workflow references/operations.md unter Plan progress before execution abgleichen. Menschliche Auswahl und Autorisierung erhalten, aktuellen Plan-Agent-Verbrauch prüfen und Ask-Sol 6.1/high-Review abschließen.
3. [status: done] Tatsächlichen nativen Plan-Consumer am finalen Stand prüfen und die offene finale Abnahme vollständig belegen.
Evidence: Strukturelle Startprüfung im nativen Consumer und Nachtests bestanden; Sol-Review durchgeführt. Kein Autorisierungsnachweis aus Strukturprüfung.

### W-006 Kodierungswarnungen und ausreichende Format-Anleitung

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0181, ADR-0175, ADR-0179, ADR-0183]
Outcome: Der Validator warnt bei typischem Zeichensalat in gültigem UTF-8; Format-Anleitungen verweisen kurz und vollständig auf Vorlage und Diagnose.
Acceptance: Typische Mojibake-Fälle wie Ã¤ und â€ werden als Warnung mit genauer Fundstelle gemeldet, ohne allein valid/Exitstatus auf Fehler zu setzen. Ein vorab bestimmter Korpus aus korrekt gespeicherten mehrsprachigen Texten, wörtlichen Encoding-Beispielen und Code belegt die Fehlalarme quantitativ; die niedrige Fehlalarmrate wird vor Abnahme begründet. Echte Syntax-/Kodierungsfehler bleiben Fehler. edit.md erhält Mindestsyntax, Vorlage und Validator-Aufruf für Stepstatus, Annotationen, Blocker, Evidence-Länge, BOM und Zeilenenden. Die manuelle Umlautprüfung bleibt für nicht sicher erkannte Fälle. Tatsächlicher Plan-Agent, ungültiger und korrigierter Aufruf, General-Fallback und Codex-Ausschluss sowie Sol 6.1/high-Review sind belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-plan/scoville-plan/scripts/validate_profile.py Warnungen ergänzen und in members/scoville-plan/development/tests Warn- und Nichtwarnfälle mit festgelegten Erwartungen prüfen. Warnungen müssen für den tatsächlichen Plan-Consumer sichtbar und eindeutig von Fehlern getrennt sein.
2. [status: done] In derselben Skill-Quelle references/edit.md die bereits mechanisch geprüften Formatregeln kürzen und references/fallbacks/validate_profile-fallback.md abgleichen. Mindestwissen und manuelle Prüfung erhalten, Diagnose-/Korrekturaufrufe prüfen und Ask-Sol 6.1/high-Review abschließen.
3. [status: done] Tatsächlichen nativen Plan-Consumer und finale General-/Codex-Paketprojektion nach den Maskierungskorrekturen prüfen; offene Schlussabnahme vollständig belegen.
Evidence: Kodierungswarnungen, Maskierungskorrekturen und native Consumer geprüft; Sol-Review durchgeführt. Heuristik ersetzt keine vollständige Unicode-Prüfung.

### W-016 Workflow-Aktivierung explizit halten

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0181, ADR-0179]
Outcome: Workflow-Metadaten und Aktivierungsregeln erlauben nur ausdrücklich beauftragte Workflow-Aktivierung. Plan-Ausführung und Arbeit an Workflow-Quellen starten keinen Workflow.
Acceptance: Die Codex-Metadaten entsprechen der expliziten Aktivierungsgrenze. Explizite Aktivierung bleibt möglich; generische Plan-Ausführung und Helper-Arbeit aktivieren den Workflow nicht. Ask mit Sol 6.1/high prüft die Änderung. Native Workflow-Tests bleiben gesonderte isolierte Testaufträge.
Instructions: []
Steps:
1. [status: done] agents/openai.yaml und die Aktivierungsregel in members/scoville-workflow-for-codex/scoville-workflow-for-codex prüfen und die widersprüchliche implizite Aktivierungsmetadaten korrigieren; Paketprojektion und explizite Aktivierungsgrenze prüfen.
2. [status: done] Ask-Sol-6.1/high-Review einholen und bestätigte Befunde beheben; Nachweise unter PLAN-0035 sichern.
Evidence: Implizite Workflow-Aktivierung deaktiviert, expliziter Aufruf erhalten; Paketprojektion und Sol-Review geprüft. Host-Trigger getrennt ausgewiesen.

### W-007 Helper- und Paketabnahme am finalen Stand

Status: done
Depends on: [W-001, W-002, W-003, W-004, W-005, W-008, W-006]
Blocked by: []
Decisions: [ADR-0185, ADR-0183, ADR-0179, ADR-0182, ADR-0184, ADR-0186]
Outcome: Die Helper-Erweiterungen sind lokal, durch tatsächliche Luna-Verbraucher und unabhängige Reviews am finalen Stand abgenommen.
Acceptance: General/Codex jeweils standalone/suite bauen und bestehen Source-, Sync-, README-, Sprach- und lokale Workflow-/Plan-/shared-Prüfungen. Je geändertem Helper ist seine Ausgabe ohne Agentenreparatur im tatsächlichen nächsten Schritt durch Luna gpt-6-luna/high verwendet; invalides Input und korrigierter Aufruf sind geprüft. Sol gpt-6.1-sol/high bewertet verblindet in Gruppen. Alle begonnenen Modelltests stehen vorab reserviert im eigenen Register und bleiben insgesamt bei höchstens 100. Semantik-Diff, Datei-/Routendeltas, Befunde, Korrekturen und Nachweisgrenzen sind in diesem Plan belegt. Pflichtreviews der Helper-Punkte liegen vor. Diese Abnahme erhält nach ADR-0186 kein zusätzliches W-007-Abschlussreview. GitHub-Actions-Runtime-Tests sind nach ADR-0183 im aktivierten Plan beauftragt; ein nötiger privater Snapshot-Push benötigt seine konkrete Freigabe. Ohne aktuellen erforderlichen CI-Nachweis bleibt die Abnahme offen. Alle ausgelieferten Helper, Pfade und Aufrufe bestehen den Abschlusscheck auf Windows, macOS und Linux, einschließlich Temp-/Absolutpfaden, Trennzeichen, Leerzeichen, Unicode, Shell-Quoting, Abhängigkeiten und direkt verwendbarer Consumer-Ausgabe. Erforderliche Plattformtests laufen nach Möglichkeit als GitHub-Actions-Matrix; Source-Stand, Joblinks und Resultate sind je Betriebssystem belegt. Python-OS-Nachweise erfolgen durch Actions, native Consumer-Proben lokal (ADR-0183). Separate macOS-/Linux-Codex-Hosts sind keine Abschlussvoraussetzung. Fehlende tatsächlich erforderliche Nachweise halten die Abnahme offen.
Instructions: []
Steps:
1. [status: done] Für den finalen Source-Stand Tests und temporäre vier Varianten im Desktop-Testprojekt aus kanonischen Quellen erstellen. Lokale Tests und Profil-/Paketprüfungen ausführen, Semantik-Diff sowie Datei-/Routendeltas nach development/plan-evidence/0035-*.md schreiben.
2. [status: done] Die gezielten tatsächlichen Consumer-Versuche mit Luna/high vor Start im eigenen Register reservieren, pro Gruppe ausführen und anschließend von Sol 6.1/high verblindet bewerten lassen. Korrekturen und notwendige Nachläufe im selben Budget sichern; kein zusätzliches W-007-Abschlussreview (ADR-0186). Windows-/macOS-/Linux-Runtime-Matrix möglichst über GitHub Actions nach ADR-0183, nötigen privaten Snapshot-Push erst nach konkreter Freigabe, fehlende Nachweise nicht als bestanden werten.
Evidence: Finale Helper-/Paket-/CI-Prüfungen bestanden, bestätigte Fixes nachgetestet; erforderliche Blockreviews durchgeführt. Kein zusätzliches Abschlussreview gemäß ADR-0186.

### W-017 Pfade und Helper-Fehlerausgaben abschließend maschinell erfassen und prüfen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0200]
Outcome: Die öffentlich ausgelieferten Skill-Dateien sind anhand eines reproduzierbaren maschinellen Fundstelleninventars auf Fehler ihrer verwendeten Pfade, Imports und Helper-Diagnosen geprüft und korrigiert.
Acceptance: Ein lesender Development-Helper erfasst die öffentlich ausgelieferten Skill-Dateien der vier finalen Paketvarianten in stabiler Reihenfolge und ordnet ihnen ihre kanonischen Suite- oder Shared-Besitzer zu. Interne Build-, Test- und Nachweisdateien sind nach ADR-0200 ausgeschlossen. Das Inventar bindet den geprüften Stand über Hashes und enthält je Fundstelle Datei, Zeile, Spalte, Textkontext und Art. Pfadliterale, Pfadkonstruktionen, Imports und Pfadreferenzen sowie Fehlerausgaben, Raises und weitergereichte Fehler der ausgelieferten Helper werden erfasst; Python-Code wird strukturell ausgewertet, nicht nur nach Stichworten durchsucht. Dynamische oder nicht sicher erkannte Konstruktionen, nicht auswertbare Dateien und ausgeschlossene Dateien oder Verzeichnisse stehen mit Grund im Inventar. Keine solche Lücke gilt automatisch als bestanden. Ein Agent arbeitet erst dieses Inventar entlang der tatsächlichen Aufrufer und Verbraucher ab. Erforderliche Pfade und Imports funktionieren unter Windows, macOS und Linux; Helper-Fehler benennen die betroffene Eingabe oder Bedingung, die Erwartung und den Korrekturweg, erhalten den Fehlerstatus und liefern keinen partiellen Erfolg. Bestätigte Fehler sind an ihrem kanonischen Besitzer behoben und mit ungültigem sowie korrigiertem Aufruf beim tatsächlichen Verbraucher nachgetestet. Die Schlussliste enthält keine ungeklärte erforderliche Fundstelle; historische Belege und beabsichtigte Platzhalter bleiben als solche ausgewiesen. Ask-Sol 6.1/high prüft den gesamten Punkt einmal nach den Korrekturen.
Instructions: []
Steps:
1. [status: done] Unter development/ einen kleinen deterministischen, lesenden Inventar-Helper für Pfade und Fehlerstellen erstellen. Die tatsächlichen öffentlichen Skill-Paketdateien über suite.json samt shared_helpers ihren kanonischen Besitzern zuordnen; nur deren Fundstellen abarbeiten. Vollständige Datei- und Fundstellenlisten samt Auswertungslücken ausgeben; die Erfassung mit gezielten positiven und negativen Fixtures über Actions prüfen.
2. [status: done] Die maschinelle Liste gezielt entlang von Aufruf, Pfadauflösung, Import, Paketposition, Fallback und Fehlerbehandlung abarbeiten. Bestätigte Befunde ausschließlich in den kanonischen Suite- oder Shared-Quellen korrigieren, betroffene Consumer und OS-Wege nachtesten und das Inventar für den geänderten Endstand erneuern. Unveränderte belegte Prüfungen weiterverwenden.
3. [status: done] In development/plan-evidence/0035-w017-result.md das vollständige Inventar, dessen Abdeckung, Entscheidungen zu Fundstellen und tatsächliche Korrektur-Nachweise verlinken. Ask-Sol 6.1/high über die abgeschlossene Prüfung einholen und bestätigte Befunde gezielt beheben; Abschluss nur ohne offene erforderliche Pfad- oder Fehlerdiagnose.
Evidence: Maschinelles öffentliches Pfad-/Fehlerinventar abgearbeitet; bestätigte Fehler behoben und nachgetestet. Actions bestanden, Sol-Review durchgeführt.

### W-009 Übertragene finale Skill-Abnahme vollständig belegen

Status: done
Depends on: [W-007]
Blocked by: []
Decisions: [ADR-0185, ADR-0177, ADR-0183, ADR-0179, ADR-0180, ADR-0182, ADR-0184, ADR-0187, ADR-0188, ADR-0189, ADR-0190, ADR-0191, ADR-0192, ADR-0193, ADR-0194, ADR-0195, ADR-0196, ADR-0198, ADR-0199]
Outcome: Die aus PLAN-0034/W-014 übertragenen offenen Nachweise nehmen den endgültigen Skill-Stand nach den neuen Helper-Änderungen ab.
Acceptance: Die nach ADR-0180 neu vorab ausgewählten ausstehenden oder durch Source-Änderungen invalidierten Skill-Cases bestehen am finalen Stand; die verbleibenden Prüfkriterien von PLAN-0034/W-014 bleiben erhalten. Bereits belegte unveränderte Prüfungen dürfen mit präzisem Stand-/Berichtsverweis weitergelten. Code, Plan, UI, Ask, Setup, Handoff, Cleanup und Workflow werden getrennt nach Testart ausgewiesen. Vollständige native Workflow-Proben mit 15/15-Prozent-Kontextschwellen belegen Ausführung, Pflichtreviews, Korrektur, Rollover/Recovery, blockierten Planpunkt, sichtbare Runner-Benachrichtigung und korrektes Warten/Fortsetzen. Geänderte Helper-Ausgaben funktionieren unmittelbar beim tatsächlichen Consumer. Erforderliche lokale Helper-, Sprach-, Build-, Portabilitäts- und Runtime-CI-Nachweise bestehen am finalen Stand. Nötige Trigger-Wiederholungen, README-Compatibility erst nach bestandenen Luna-high-Skill-Tests, Semantik-Diff, PLAN-0034/W-004-Paketvergleich und statischer Datei-/Routenkostenvergleich sind belegt. Ausgelassene Fälle und nicht qualifizierte Testarten bleiben ausdrücklich unverifiziert; keine vollständige Wirkungsabnahme aus einer Auswahl ableiten. Insgesamt höchstens 300 Luna-high-Versuche für ganz PLAN-0035; Sol 6.1/high bewertet verblindet in Gruppen. Abschlussbericht je Skill und Ask-Sol 6.1/high-Review liegen vor. Alle ausgelieferten Helper, Pfade und Aufrufe bestehen den Abschlusscheck auf Windows, macOS und Linux, einschließlich Temp-/Absolutpfaden, Trennzeichen, Leerzeichen, Unicode, Shell-Quoting, Abhängigkeiten und direkt verwendbarer Consumer-Ausgabe. Erforderliche Plattformtests laufen nach Möglichkeit als GitHub-Actions-Matrix; Source-Stand, Joblinks und Resultate sind je Betriebssystem belegt. Python-OS-Nachweise erfolgen durch Actions, native Consumer-Proben lokal (ADR-0183). Separate macOS-/Linux-Codex-Hosts sind keine Abschlussvoraussetzung. Fehlende tatsächlich erforderliche Nachweise halten die Abnahme offen.
Instructions: []
Steps:
1. [status: done] PLAN-0034/W-014, den Abschnitt Testvertrag und Abnahme aus seinem Goal sowie ADR-0166 und development/plan-evidence/0034-w014-test-corrections.md, 0034-opus-v5-corrections.md sowie die verlinkten Case-/Skill-Berichte gegen den finalen Source-Stand prüfen. Noch gültige Ergebnisse und jeden offenen oder invalidierten Nachweis unterscheiden, die neue gezielte Auswahl ausstehenden Skill-/Trigger-/Consumer-/Workflow-Fälle nach ADR-0180 samt unverifizierten Auslassungen im Desktop-Testprojekt vorab festlegen und den Gesamtbedarf einschließlich Korrekturen im eigenen 300er-Register planen.
2. [status: done] Die ausstehenden vorab gewählten Cases und tatsächlichen Consumer-Proben mit gpt-6-luna/high pro Gruppe nach Reservierung ausführen; anschließend verblindete Sol-gpt-6.1-sol/high-Bewertung. Vollständige native Workflow-Fälle mit 15/15-Schwellen einschließlich Runner-Blocker-Benachrichtigung und Warten/Fortsetzen prüfen. Ursachen in kanonischen Suite-/Shared-Quellen korrigieren und invalidierte Nachweise erneuern. Description-/Trigger-Änderungen nur bei belegtem Problem; bei geänderter Description die geforderten Trigger-Cases gemeinsam am endgültigen Stand wiederholen.
3. [status: done] Die drei unterschiedlichen praktischen Zusatzfälle für Ask, Setup, UI, Handoff und Cleanup mit Luna/medium auf Windows und Linux vorbereiten und ausführen. Identische Ausgangsdaten und tatsächliche Consumer verwenden, beide Plattformen getrennt belegen. Sol 6.1/high bewertet pro Skill den gesammelten Block; bestätigte Fehler korrigieren und relevant nachtesten.
4. [status: done] Vier temporäre Paketvarianten und erforderliche lokale Workflow-/Plan-/Ask-/Setup-/shared-, Source-/Sync-/Sprach-/Portabilitätsprüfungen am finalen Stand bestätigen oder nach Änderungen erneuern. Windows-/macOS-/Linux-Runtime- und Portabilitätsmatrix möglichst über GitHub Actions nach ADR-0183 ausführen; einen nötigen privaten Snapshot-Push erst nach konkreter Freigabe. In development/readme/-Fragmenten und ../shared/readme/suite-requirements.md Luna-High-Compatibility je Skill erst nach bestandenem Nachweis setzen und README-Vorschauen generieren; Semantik-Diff, unveränderte PLAN-0034/W-004-Pakete beziehungsweise erforderliche genehmigte Änderungen und statische Datei-/Routenkosten gegen den ursprünglichen Stand ausweisen.
5. [status: done] Abschlussbericht je Skill mit Testart, Sprache, Modell/Effort, Korrekturrunden, Deltas, tatsächlichem Ergebnis und unverifizierten Wegen nach development/plan-evidence/0035-*.md schreiben. Nicht angenommene Skills, externe Case-Hindernisse, getrennte Regeln, README-Beispiel/-Dateiregelstellen und offene Pflichtnachweise nennen. Ask-Sol 6.1/high prüft den vollständigen Punkt; dessen bestätigte Befunde beheben und den finalen Nachweis in diesem Plan behalten.
Evidence: Ausgewählter finaler Skill-Stand abgenommen; Sol-Review durchgeführt. Begrenzter Code-Nachweiswechsel gemäß ADR-0190; historische FAILs und unverifizierte Auslassungen bleiben ausgewiesen.

### W-015 Lange Viewer-Menüs bleiben vollständig bedienbar

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0176, ADR-0179, ADR-0187, ADR-0201]
Outcome: Alle langen Auswahlmenüs des Plan Viewers, ausdrücklich Plan history und Project, bleiben im verfügbaren Fenster scrollbar und ihre letzten Einträge auswählbar.
Acceptance: Mit mehr Einträgen als sichtbarem Platz sind erste und letzte Option bei kleiner und normaler Fensterhöhe per Maus/Trackpad und Tastatur erreichbar. Fokus und ausgewählter Eintrag bleiben sichtbar; Auswahl, Escape und Wiederöffnen funktionieren. Kurze Menüs und übrige gemeinsam betroffene Menüs regressieren nicht. Ask-Sol 6.1/high prüft den vollständigen Punkt. Die erforderliche native Desktop-Gegenprobe ist belegt.
Instructions: []
Steps:
1. [status: done] In members/scoville-plan/development/viewer die beiden Screenshots und Nutzerbeobachtung mit einer Fixture mit vielen Plänen und Projekten reproduzieren. App.svelte, gemeinsame src/lib/components/ui/select/-Komponenten und übrige Menü-Verbraucher prüfen.
2. [status: done] Ursache an der zuständigen gemeinsamen Komponente korrigieren, soweit Menüs denselben Mechanismus verwenden. Verfügbare Fensterhöhe, tatsächlichen Scrollbereich und Fokusführung über das bestehende UI-System berücksichtigen; keinen unbelegten pauschalen CSS-Fix verordnen.
3. [status: done] Interaktiv kleine/normale Fenster, Überlauf/kurze Listen und Auswahl letzter Einträge in Plan history, Project und weiteren betroffenen Menüs prüfen. Regression an der gemeinsamen Ursache gezielt absichern und tatsächlich betrachtete Renders plus Bediennachweise aufzeichnen.
4. [status: done] Vorhandene Frontend-Prüfungen ausführen. Native Desktop-Gegenprobe mit freigegebenem Actions-Build durchführen oder deren fehlenden Nachweis ausdrücklich offen lassen; keine automatische Installation oder Veröffentlichung. Ask-Sol 6.1/high-Review und alle Nachweise in PLAN-0035 sichern.
Evidence: Menüs korrigiert und nativ unter Windows geprüft; übrige Plattformbuilds und Hashes verifiziert. Sol- und Opus-Reviews samt gezielten Nachtests abgeschlossen.
