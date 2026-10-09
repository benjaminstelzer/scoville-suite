# Scoville-Befunde aus dem EMPCO-Lauf

Beobachtung durch Nutzerstopp am 2026-10-09 beendet; Automation gelöscht. Geprüft sind die festgehaltenen Befunde und spätere Änderungen bis 06:43 UTC. Die vollständige historische Abdeckung ab Ausgangsgrenze blieb offen. Kein Abschluss des EMPCO-Workflows behauptet. Umsetzung des Konsenses: PLAN-0048.

Stand: 2026-10-09. Scoville Ask mit angefordertem Opus 5.5/high und GPT 6.1/xhigh: Beide haben ihre Bewertungen gegenseitig vollständig gelesen und die folgenden Lösungen ausdrücklich abgestimmt. Tatsächliche Modell-/Effort-Telemetrie ist nicht offengelegt. Umsetzung und Tests stehen aus. EMPCO ist nur das Praxisbeispiel.

## Instructions enthält Ergebnisgeschichte und doppelte Stepaktion

- Quellen: Manager 01a11cec-4b70-78d3-8144-5fa27ad35867, W370 Instructions/Step4; Astra/high Reviewer9 01a11d5a-e03f-7fe3-a29c-1314f55deb05, finale msg_003c435cafd4d812016ac807eec0508191841297f60955a862; Korrektur exec-e818f3ae-b3c3-4e75-b20b-a44a9359b638.
- Wirkung: Instructions enthielt erfüllte GitHubsicherung samt Commitnachweis und wiederholte den vollständigen Reviewauftrag aus Step4. Ergebnisgeschichte und doppelte Auftragspflege vergrößern Kontext und schaffen mögliche Drift.
- Recovery: Reviewer verlangte Korrektur; Manager entfernte Ergebnisgeschichte und Doppelung, erhielt aktuelle Commitsperre/Schutzgrenzen und übernahm fehlende Reviewbedingungen in Step4. Step3 bleibt offen. Die Profilprüfung bestand, ist aber kein semantischer Abnahmenachweis.
- Vereinbarter Fix, zuständig Plan references/edit.md, bestehender Abnahmeschritt: Geänderte Sätze zuordnen: Aktionen in Steps, beobachtete Ergebnisse in Evidence, zusätzliche aktuelle Bedingungen in Instructions. Erledigte Aktionen und Ergebnisgeschichte entfernen; bindende Schutzgrenzen und fällige Reviews bewahren. Keine zusätzliche Workflow-Feldregel, Prüfung oder Reviewrunde.
- Grenze: Ungetestet und nicht umgesetzt. Falsche Feldwahl ist beobachtet; ihre kognitive Ursache bleibt unbekannt. Der unabhängige Reviewer erkannte sie. Die Beratung ersetzt keine Änderungsrechte-Abnahme des gestarteten Items.

## Windows-Shellwahl und wörtlicher Dateiglob

- Quellen: Worker 9, 01a11d4d-a965-75b0-80db-b6be1cec0190. exec-e276a6d8-3bf4-4fa7-a2ae-87c65ecb9c54 verwendete powershell für Kopieren und Get-FileHash; der Hashbefehl war dort unbekannt. exec-773e5f6c-bb47-432e-930a-26be464698c4 übergab rg einen Dateipfad mit Stern; rg wies ihn mit os error 123 zurück.
- Wiederholung bei Worker 10, 01a11d66-f799-7a90-81d0-b4662a6152b2: exec-b329abf5-5c75-49a6-b20a-15908baf544d nutzte erneut powershell/Get-FileHash. Der gelesene Vollnachweis zeigte Cmdletfehler trotz Exit 0 und Erfolgstext; anschließend bestätigte exec-e0869e3c-8422-4c43-b93c-43d4d2fb0fbe die Bytegleichheit und Cleanup ohne das Cmdlet. Die bestehenden Vorschläge zu Launcherwahl und Fehlerstatus gelten auch hier.
- Wirkung: Zwei fehlgeschlagene Aufrufe. Hash-Recovery mit explizitem PowerShell-7-Pfad bestätigte die vorhandenen Kopien ohne erneutes Kopieren; rg-Recovery mit Verzeichnis und -g lieferte die benötigte Suche. Keine daraus entstandene unvollständige Fachaktion beobachtet.
- Vereinbarter Fix, zuständig shared/prompting/common.md mit Code als Verbraucher: Aktuelle Toolshell verwenden; erzeugte Befehle nicht verschachteln. Bei nötigem Shellwechsel den bekannten passenden absoluten Launcher übergeben; powershell übernimmt nicht automatisch den Launcher einer pwsh-Sitzung. Bei --run expandiert keine Shell Dateiglobs: rg erhält ein vorhandenes Verzeichnis und das genaue Muster mit -g. Keine zusätzliche Versionsabfrage, Cmdlet-Inventur oder Dateiliste.
- Grenze: Vorschläge ungetestet, noch nicht umgesetzt. Der tatsächliche powershell-Pfad, dessen Version und der Grund des fehlenden Cmdlets sind unbekannt. Kein Generatordefekt belegt. Tabellenellipsis betrifft nur Pfaddarstellung, keine belegte Checkertrunkierung. Normale CSS-Regressionen bleiben Produktbefunde.

## Windows-Aufrufstruktur fehlerhaft rekonstruiert

- Quelle: Worker 9, 01a11d4d-a965-75b0-80db-b6be1cec0190, exec-15055e8a-1070-4555-9ed7-2bb07f93bd06. Im vorbereiteten Reader-Aufruf fehlte die Zuweisung durch Process.Start vor WaitForExit.
- Derselbe Verbesserungsbereich ist auch bei Worker 10, 01a11d66-f799-7a90-81d0-b4662a6152b2, exec-9e308e14-c228-4f4a-83de-09096568354f belegt: Die rekonstruierte Start-/Exitstruktur für Part8 war syntaktisch beschädigt, ParserError/Exit1. Derselbe Part wurde korrekt wiederholt und die Folge vor Projektarbeit bis last gelesen. Der vorhandene Vorlagenvorschlag deckt diese Wiederholung ab; keine erneute Konsultation nötig.
- Wirkung: Nullwertfehler statt Dokumentlesung, trotzdem Tool-Exit 0. Der korrigierte Folgeaufruf startete den Prozess; die Teilfolge wurde vor Codearbeit gelesen. Kein Projektwrite aus dem Fehlaufruf beobachtet.
- Zuständig: Workflow, gemeinsame Windows-Aufrufvorlage. Die installierte native_task_arguments.py:143–149 enthält den Prozessstart; eine fehlerhafte Ausführung ist belegt, ein Generatorfehler nicht.
- Vereinbarter Fix, zuständig shared/runtime/native_task_arguments.py, shell_command: Windows-Prozessstart und Warten mit lokalem Stop, try/catch und Nullprüfung absichern. Volle Diagnose und Nichtnullstatus bei Fehler; echten Nichtnull-Kindstatus weitergeben. Bei Kindexit0 normal zurückkehren. ProcessStartInfo, UseShellExecute=false und vollständige list2cmdline-Quotierung erhalten; POSIX unverändert. Keine zusätzliche Vorabprüfung oder Kontrolllesung.
- Grenze: Ungetestet und nicht umgesetzt. Der beobachtete fehlende Start war ein Nachbaufehler. Dass die heutige korrekt erzeugte Vorlage bei einer Startausnahme ebenfalls Exit0 liefern könnte, ist nur gefolgert. Herkunft der ausgelassenen Zeile und genaue Ursache des beobachteten Exit0 bleiben unbekannt. Exit125 unterscheidet einen Helperfehler nicht von einem Kind mit eigenem Exit125; beide stoppen abhängige Arbeit.

## Dokument als Python-Programm gestartet

- Quelle: Manager 01a11cec-4b70-78d3-8144-5fa27ad35867, exec-268400d4-5ecb-401d-9c91-0e63098111c7, W-370 nach Schritt 2. Python startete references/operations-rollover.md statt scripts/check_text_size.py mit --file.
- Wirkung: SyntaxError, Exit 1, unnötiger Fehlaufruf. Der nächste Aufruf las dieselbe Datei korrekt bis last; kein Projektwrite aus dem Fehlaufruf beobachtet.
- Zuständig: Workflow und gemeinsame Aufrufanleitung. Die vorhandene Regel „nur .py als Programme“ verhinderte diese neue Wiederholung nicht.
- Vereinbarter Fix, zuständig native_task_arguments.py, file_read_instruction, und Workflow scripts/build_manager_handoff.py: Für alle bereits genannten Managerdokumente vollständige statisch gequotete Readerbefehle erzeugen: Protokoll vor READY, Assignment nach START, übrige Referenzen an bestehenden Lesestufen. Erklärung einmal nennen; vollständigen Befehl direkt übernehmen. Für andere Dokumente die positive Kopierregel in shared/runtime/document_reader.md erhalten. Den &-Hinweis in python_discovery.md auf direkte Interpreteraufrufe begrenzen; erzeugte Readerbefehle nicht ersetzen. Keine zusätzlichen Leseaufträge oder Prüfschritte.
- Grenze: Ungetestet und nicht umgesetzt. Die kognitive Ursache bleibt unbekannt. Fertige Befehle verringern Rekonstruktion, garantieren aber keine Befolgung; der Checker kann Aufrufe nicht abfangen, die ihn gar nicht starten.

## Evidence überschreitet das Zeichenbudget

- Quelle: Manager 01a11cec-4b70-78d3-8144-5fa27ad35867, W370; exec-8c7814f9-2375-45fd-b234-c416a57383e8 meldete WORK_EVIDENCE_INVALID: 213 statt maximal 200 Zeichen. exec-b7e7d4fd-59d3-4035-ab87-bbae9da79f0c kürzte auf 170; exec-68d5bc4a-6679-4cef-a64f-319ec22a8e50 bestätigte valid=true vor Dispatch.
- Wirkung: Vermeidbarer Fehler-/Korrekturzyklus; kein falscher Abschluss oder Informationsverlust belegt. Der Validator arbeitete korrekt.
- Vereinbart: Kein zusätzlicher Skilltext, Zählcheck oder Validatorfix. Die vorhandene Grenze griff korrekt; die frühere zusätzliche Formulierungshilfe entfällt.
- Grenze: Vorhandene geladene Feldregel wurde nicht angewandt; Ursache durch Kontextkompaktion nicht belegt.

## Ergänzung für die ohnehin erforderliche Hashprüfung

- Zuständig: Kanonische shared/runtime/check_text_size.py, document_reader.md und check_text_size-fallback.md; Suitekopien daraus erzeugen.
- Vereinbarter Fix: Enger --sha256-Modus, nur für übergebene erwartete Hashwerte. Originalbytes strikt als UTF-8 prüfen und ausschließlich eine JSON-Zeile mit utf8_bytes und sha256 ausgeben. Kein Größenstatus, Inhalt oder Bearbeitungsauftrag. JSON inklusive Zeilenende und Diagnosen im unveränderten kleinsten Budget halten; part_budget auch für diesen Modus setzen. Bei zu großem JSON kein JSON und Nichtnullstatus; passende Diagnose vollständig auf stderr, niemals kürzen. Kombinationen mit part, publish-full, project-root oder run ablehnen; andere Modi unverändert.
- Leseregel: Erwarteten Hash vergleichen; bei Abweichung oder Fehler abhängige Arbeit stoppen. Danach dieselbe unveränderte Datei mit demselben Limit vollständig von Part1 bis last lesen. Hashprüfung ersetzt Lesen nicht. Der Fallback nutzt ein vorhandenes Hostwerkzeug über Originalbytes. Keine neue Hashprüfung gewöhnlicher Quellen.
- Grund und Grenze: Der normale Größenstatus compact_required fordert zugleich zum Kürzen oder Publizieren auf. Dies passt nicht zum unveränderten Lesen eines empfangenen Artefakts; ein zusätzlicher Hash in derselben Ausgabe würde den Widerspruch erhalten. Neuer Modus ungetestet und nicht umgesetzt.

## Verworfen und gezielte spätere Abnahme

Rohe variable Windowsargumente an einen gequoteten Befehl anhängen wurde wegen möglichem Verlust der Argumentgarantie verworfen. Hash in der normalen Größenprüfung entfällt wegen des widersprüchlichen Bearbeitungsauftrags. Unbedingtes exit0 entfällt, weil es die aufrufende PowerShell beenden kann. Zusätzliche Evidence- und doppelte Instructions-Regeln entfallen zugunsten bestehender Besitzer und Abnahme.

Nach autorisierter Umsetzung auf Windows und Linux nur geänderte Verträge prüfen: Argumente einschließlich Leerwert, Leerzeichen, Apostroph, Quote und abschließendem Backslash; Startfehler mit voller Diagnose und Nichtnullstatus, Kindexit3 und Stderr bei Kindexit0; bestehende Readerfolgen und Lesestufen; Hash großer Artefakte, veränderte Bytes, zu kleine Budgets, ungültiges UTF-8 und verbotene Optionen samt anschließendem vollständigem Lesen; Planmischfall ohne Doppelung bei erhaltenen Schutzgrenzen. Windows umfasst die unterstützten PowerShellpfade. Unveränderte Helper brauchen keine pauschale Testwiederholung. Wirkung auf Luna bleibt offen.

Für Routingtimeout, pending_init und reine EMPCO-Produkt-/Fixturefehler ist keine Suiteursache belegt. Dafür ist kein Suitefix vereinbart.
