# PLAN-0021 Nachweise

## Claude und Staging

ask.py prepare/claude benötigt keine creation_authorized/authorized-Felder mehr.
Aufrufvertrag und Tests sind angepasst; 34 Ask-Regressionstests bestanden.

Realer Test am 29.09.2026 mit gepacktem Helper, Claude Code 2.1.283,
angefordertem claude-opus-5-5/high, Budgetgrenze 1 USD je Aufruf:
prepare erzeugte direkt verwendbaren Auftrag ohne Genehmigungsfeld. Claude
fragte nach fehlender PHP-Mindestversion. Die Antwort PHP 7.4 wurde mit der
bestätigten Session-ID 563e180b-e608-48dc-b14d-829813dfe79c übergeben.
Ergebnis: context_mode continued, unveränderte Session-ID, ursprünglicher
Referenzmarker Cedar-472 und korrekter Befund samt strpos-Alternative.
Keine Permission-Denials. Transport meldet tatsächliches Modell/Effort nicht;
die Selbstauskunft im Antworttext ist kein Telemetrienachweis.
Rohdaten: Desktop/test/plan0021/claude-*-request.json und *-result.json.
Die Testberatung ist abgeschlossen; Session-Historie bleibt erhalten.

Isolierter Ask-Fall mit Luna High:
Desktop/test/plan0020/runs/ask-luna-high-v5-ask,
Chat 01a0ec34-25aa-7061-a1d3-fa9b0c806ae3. Zehn Fälle inhaltlich bestanden:
kurzer Titel, Helper-Argumente, Pinning, eigene Beraterantwort, Rückfrage,
Nichtaktivierung, Nutzerstopp, Timeout und kein redundanter Ergebnisabruf.
UI-default_prompt nicht als auszuführenden Testauftrag eingebettet;
Konfigurationsreferenz vollständig mitgeliefert. Frühere kontaminierte bzw.
unvollständige Harness-Läufe bleiben als ausgeschlossene Versuche erhalten.

General und Codex in skills/temp/release aktualisiert. Inventaränderungen nach
Sicherung durch Dateikopien und Verschieben veralteter Dateien abgeglichen.
Beide check-packages und Codex check-helpers: valid:true. Ältere Exporte und
Vergleichsbuilds nach Desktop/test/plan0021/retired-staging verschoben; dort
gesichert. Zwei verbleibende gesperrte Verzeichnisgerüste enthalten null Dateien.
Kein Commit oder Export aus ungeprüften uncommitteten Quellen behauptet.

## Luna-High-Gesamtprüfung

Separater Luna-High-Prüfer: 15 direkte Plan-/Setup-/Ask-Helperfälle bestanden,
einschließlich falscher und korrigierter Aufrufe. General-Standalone und -Suite
enthalten genau zwei Plan-Fallbacks; Codex enthält keine. Modellkatalog benutzt
einen lokalen Protokoll-Mock. Evidence: Desktop/test/plan0021/luna-helper-audit.
Zusätzlich 12 direkte Workflow-Helperfälle, 16 simulierte manuelle
Fallback-Vergleiche und negative Profilprüfungen bestanden. Das ist kein Test
auf einem Rechner ohne Python. Der native Gesamtplan läuft noch.

Nativer Manager: 01a0ec31-de2e-76d0-8c40-81331cffa100, Luna High, Projekt test.
Testkonfiguration mit Setup-Helper geschrieben: Manager/Worker 15/15, alle
Execute-/Review-Routen gpt-6-luna/high. Testplan PLAN-0001 implementiert einen
kleinen CSV-Parser mit CLI und Integration in drei echten Arbeitspunkten.
Produktdateien ausschließlich Desktop/test/plan0021/workflow-app.

## Befunde im nativen Workflow

W-001 und W-002 mit unabhängigen Reviews bestanden. Reale Manager-Rollover
bei 55.559 und 60.748 Input-Tokens sowie ein Worker-Rollover fanden statt.
Nachfolger sendeten die Übernahme vor gewöhnlichem Lesen an ihren Vorgänger.
Helper-Ausgaben entsprachen den tatsächlich verwendeten Erstellungsargumenten.

Manager 3 und 4 prüften eine bereits vom Vorgänger verbrauchte Grenze erneut.
Bei 15% überschritt schon der Startkontext die Schwelle. Der Test stoppte nach
zwei Übergaben ohne Fortschritt korrekt. Reparatur: Jede Grenze wird einmal
verbraucht; erst neue geprüfte Arbeit/ein neuer Worker-Handoff löst die nächste
Prüfung aus. Regel steht in operations.md und im generierten Managerprompt.
Ein verkürzter Aufrufer-UUID verursachte zusätzlich Invalid conversation.
Der Managerhelper nimmt die Rückmeldeadresse jetzt als validierten Parameter
--report-to-thread-id entgegen. Fehlerfall und korrigierter Aufruf sind geprüft.
Der Parameter schützt vor Syntaxfehlern, nicht vor einer gültigen falschen ID.

Weitere gezielte Reparaturen: Manager verwenden exakten Planpfad/Selector statt
geratener Dateinamen und breiter Suche. Ein erfolgreicher Kind-Callback enthält
den vollständigen Bericht; die sichtbare Abschlussantwort bestätigt nur kurz die
Zustellung. Bei Versandfehler bleibt der vollständige Bericht in der Antwort.
Acceptance wird nicht zusätzlich im Supplemental-Kontext wiederholt.

Manager 4 setzt W-003 nach expliziter Korrektur mit unveränderten 15/15 fort.
Die neuen Pakete liegen getrennt unter Desktop/test/plan0021/skills-repaired.
Dieser Wiederanlauf ist ein kontrollierter Reparaturtest, kein unbeeinflusster
Gesamtdurchlauf. Alte Pakete/Logs bleiben erhalten.

## Setup und Pinning

Ask und Workflow besitzen unabhängige pin_threads-Booleanwerte, Default true.
Setup-Skill, Helper, Consumer und kanonische README-Fragmente sind erweitert.
False unterbindet neue Pin-Aufrufe; vorhandene Pins bleiben unverändert.
Claude besitzt keine Sidebar-Zeile. Technisch geprüft: Defaults, unabhängiges
Speichern, String/Integer-Ablehnung ohne Dateiveränderung und echte Consumer.
Aktuell erneut bestanden: Setup 2, Ask 34, Workflow 26, Build 37 Tests.
Beide Staging-Paketprüfungen und Codex-Helperprüfung bestehen. Unabhängige
Luna-High-Gegenprüfung umfasst 14 bestandene Pin-Fälle: Default, unabhängige
Booleanwerte, Consumer und das Auslassen neuer Pin-Aufrufe ohne Entpinnen.

## Abschluss und gezielte Nachprüfung

Der reale Testplan PLAN-0001 ist completed, der Index idle. Manager 5
01a0ec4f-88af-7912-ab20-56b4c7a01722 erhielt den neuen Helperprompt inklusive
validierter Rückmeldeadresse und lieferte das Ergebnis erfolgreich hierher.
W-003-Review ohne Befunde; Worker führte alle 13 Tests und echtes CLI-Beispiel
erfolgreich aus. Reviewer prüfte Dateien/Vertrag, wiederholte die Tests nicht.
Testcommit 9eb1a01. Der zunächst verkürzte Evidence-Pfad wurde mit 5f8fbbd
korrigiert und das Profil erneut validiert, ohne den Workflow wieder zu starten.

Im kontrollierten Wiederanlauf führte Manager 4 nochmals den alten Checkpoint
aus, ignorierte ihn aber und dispatchte W-003. Deshalb keine Behauptung eines
fehlerfreien Wiederanlaufs. Ein gezielter Luna-High-Prompttest mit bereits
verbrauchter Grenze setzte W-003 dagegen ohne erneuten Checkpoint fort.
Worker 4 checkpointete außerdem trotz abgeschlossener eigener Arbeit und meldete
context_handoff. Die Regel stand bereits im Prompt; die terminale Ausnahme wurde
nun unmittelbar an die Batch-Regel gezogen: nur bei noch offener eigener Arbeit
prüfen, sonst normales Ergebnis. Der Koordinator behandelte den Bericht inhaltlich
korrekt und ließ die fertige Arbeit reviewen, statt sie erneut umzusetzen.
Beide gezielten Luna-High-Proben bestanden: fertige eigene Arbeit meldet completed
ohne Checkpoint trotz 15%-Überschreitung; noch fehlgeschlagene Prüfung ergibt
context_handoff mit offenem Fehler und nächster Aktion. Es sind kontrollierte
Promptproben, kein weiterer vollständiger nativer Workflow. Inputs und Antworten
unter Desktop/test/plan0021/luna-helper-audit/terminal-checkpoint-probes.

Plan 80, Setup 2, Ask 34, Workflow 26 und Suite-Build 37 Tests bestanden.
Alle 62 kanonischen Shared-Tests bestanden nach Korrektur zweier veralteter
Testannahmen und Synchronisierung der Shared-Snapshots. Die Test-Fixture trägt
jetzt den vorgeschriebenen Helpervertrag; der Beschreibungstest trennt historische
README-Beispiele vom gemeinsamen Beschreibungstext. Keine Validierung gelockert.

Workflow-/Plan-Einstiege erklären auf Nutzerauftrag sorgfältige Planung,
Ask-Reviews, frühe Fehlererkennung, kontrollierte Übergabe und Plan als Backbone.
Kosten/Cache-Erklärung steht im Kostenabschnitt. Wortlaut mit geladenem
benjaminstelzer-imitate-me überarbeitet. Generierte Member-READMEs und beide
Stagingprofile nachgeführt; 16 gezielte README-Tests und Paketprüfungen bestanden.
