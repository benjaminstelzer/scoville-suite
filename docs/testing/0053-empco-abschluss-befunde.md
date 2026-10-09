# Befunde im neuen EMPCO-Lauf

## Startup-Nachweis zu früheren Läufen

Quelle: Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5, Startturn 01a120d7-6328-79c3-bc8e-adf922ea306e; Manager 01a120d8-d89e-7eb0-b3f6-b411ba77aee8. Der gelesene Neustartprompt verlangte unter Vorgehen 1 vor Schreibarbeit die Prüfung, dass keine alte Schreibinstanz oder alter Worker aktiv sei. Die tatsächliche Startup-Blockermeldung verlangte alte IDs oder Quieszenzbestätigung, ohne einen konkreten aktiven alten Writer zu benennen.

Der Auslöser ist die zu weit gefasste Promptforderung. Aus fehlenden historischen IDs entstand eine Nachweissperre. Ein tatsächlicher paralleler alter Schreiber ist damit nicht belegt. Der Nutzer korrigierte ausdrücklich die Vorgabe für einen neuen Lauf. Diese Korrektur wurde demselben Runner zugestellt und an den bestehenden Manager weitergegeben. Die native Manager-Aktivität call_29973f1714ca41e48bb7b5dc99582a55 belegt anschließend den Start des Workers 01a120e3-818d-7420-9976-df838690a711 für W-386/step-1; ein Produktabschluss ist damit noch nicht belegt.

Zuständigkeit: Workflow-Startvertrag und Manager-Startup. Allgemeine Korrektur: Neue Aktivierung verlangt weder alten Agentbaum noch Abschaltnachweis. Nur konkrete Hinweise auf aktive oder ungewisse konkurrierende Writer blockieren Schreibarbeit; Same-run-Recovery und Übernahme behalten ihre bestehenden Schutzregeln. Kein Helperdefekt ist belegt. Der kurze Skilltext ist mit v2.4.12 lokal und auf GitHub ausgeliefert; Reload zugestellt. Der Runner las die installierte SKILL.md danach tatsächlich neu. Die allgemeine praktische Zuverlässigkeit und Abschlussausgabe sind noch offen.

## Veränderter Readerpfad beim Folgeteil

Quelle: Manager 01a120d8-d89e-7eb0-b3f6-b411ba77aee8, exec-7730758a-c97b-4ef3-8395-32b26fb34db8. Beim dritten Teil von Plan references/edit.md änderte er den Programmpfad von scoville-workflow-for-codex zu scoville-work-for-codex. Python meldete fehlende Datei, Exit 2. Anschließend las er mit richtigem Pfad ab Teil 1 vollständig bis 19057/19057 last; erst danach folgten Planänderung und Workerdispatch. Wirkung: fehlgeschlagener Aufruf und zusätzliche Lektüre, kein beobachteter Fortschritt mit ungelesener Grundlage. Die Recovery war regelkonform.

Scoville Ask bestätigte den Anwendungsfehler. Zuständigkeit: Shared runtime/document_reader.md und file_read_instruction() in native_task_arguments.py. Abgenommener Vorschlag: letzten korrekten vollständigen Befehl kopieren; beim Folgeteil nur --part ändern. Bei einem anderen Dokument, auch aus einem anderen Skill, nur --file ändern und Teil 1 setzen. Launcher, vollständigen Checker-Pfad und Quoting erhalten. Die frühere Idee einer mehrzeiligen ProcessStartInfo-Hülle entfällt; shell_command() bleibt unverändert. Bestehende Limit-/Fehler-Recovery, UTF-8-Diagnostik, Start-/Wartefehler und Exitcodes bleiben erhalten.

Grenze: Kein Helperdefekt belegt. Die kanonischen Readertexte sind umgesetzt und gemeinsam abgenommen. Der bestehende Reader-Shell-Test besteht. Warum der Pfad verändert wurde und ob Luna die neue Anweisung zuverlässiger befolgt, bleibt offen; tatsächliche Adviser-Modelltelemetrie nicht verfügbar.

## Prozessmetadaten durch verkürzten Toolwrapper verloren

Quelle: Worker3 01a12118-05da-7392-ad0c-e1168563f22e, Turn 01a12126-b420-7b33-86dc-f149ef6d7304, Raw-Call call_1e97120a56824cf2b3cd91c4b87391ed. Der Wrapper gab nur text((await tools.exec_command(...)).output) aus. Die erste sichtbare Ausgabe war leer; Manager3 meldete eine verlorene session_id und stoppte abhängige Schreibarbeit. Die Projektion verwirft Prozessmetadaten; die genaue ursprüngliche exec_command-Rückgabe ist nicht sichtbar. „Script completed“ bewies nur das Ende des äußeren Wrappers.

Wirkung: Der zustandsändernde Prüfprozess war zunächst nicht sicher nachverfolgbar. Der vollständige Capture desselben Laufs wurde ohne Wiederholung gefunden und gelesen: Exit 1, Fixtureguardfehler, keine fachlichen Checks. Nach gezielter Prozessprüfung und nativem blocked-Abschluss gab der Manager denselben Worker zur Fixturekorrektur frei. Die vorbereiteten 59 isolierten Tabellen, ihr vollständiger Cleanup und Step3-Nachweise waren an dieser Grenze offen; der Fixturefehler allein ist kein Suitebefund.

Scoville Ask bestätigte den Anwendungsfehler und die sachgerechte Recovery. Zuständigkeit: Shared runtime/native_output.md, bereits über rules.native_output eingebunden. Abgenommener Vorschlag: vollständiges exec_command-Ergebnis mit session_id, allen Chunks und finalem Exitstatus erhalten; die Verkürzung auf .output ausdrücklich ausschließen. Äußeres Scriptende beweist kein Childende. Die konkrete bestehende Vorlage gilt für geprüfte Reads und Captures; allgemeine Ergebniserhaltung verlangt nicht überall dieselbe Vorlage. Pollschleife, Ausgabegrenzen, JSON-Kodierung und unveränderte Checker-Ausgabe erhalten; keine zusätzlichen Recovery-Regeln oder Dispatchmuster.

Gezielter späterer Luna-Test: leere Ausgabe mit session_id, weiterer laufender Chunk, Abschluss mit Exit 1. Erwartet: genau ein Start, dieselbe Session bis Abschluss verfolgen, alle Chunks erhalten, Childfehler erkennen. Die kanonische Anweisung und ihre Codex-Verbraucher sind umgesetzt und gemeinsam abgenommen; eine Wirkungskontrolle mit Luna fehlt. Tatsächliche Adviser-Modelltelemetrie unbekannt.

## Zusätzliche Vollmanifest-Sperre blockiert begrenzte Integration

Quelle: Worker3, Turn 01a12134-36e9-74c1-b0f4-e345b3b9224e, exec-902fabf9-b779-4939-b4ab-9d4a621ecbe1. Das neue Integrationswerkzeug ergänzte einen Vollbestandsguard: Alle installierten Dateien mussten einem alten erfolgreichen Manifest entsprechen. Zuvor passten die Vorherhashes der zwei beauftragten Owner; Source und Installation unterschieden sich genau bei diesen zwei Dateien. Der Zusatzguard blockierte dennoch wegen 59 übriger Abweichungen (446 alte gegenüber 450 aktuellen Dateien). Kein Transfer erfolgte.

Manager3 las Diagnose und Werkzeug vollständig und erkannte die zusätzliche Bedingung (exec-466dd819-57ae-4e5b-bdeb-20abfb63c64d). Seine Recovery verwendet nur die zwei belegten Manifest-Einträge, erhält alle übrigen aktuellen Installationsbytes durch vollständigen Vorher-/Nachhervergleich und behauptet keinen neuen erfolgreichen Gesamtdeploymentstand. Evidence lässt die Integration offen; derselbe Worker wurde für diese Restarbeit freigegeben. Der tatsächliche Transfer und seine Abnahme sind an dieser Grenze noch unbewiesen.

Scoville Ask bestätigt den Anwendungsfehler und die begrenzte Recovery. Kein allgemeiner Skilldefekt bewiesen. Zuständigkeit: Scoville Code, SKILL.md „Scope, integrity, and authority“, Absatz ab „Do not weaken tests“. Plausible Unklarheit: Schutz verbindlicher Prüfungen kann auch auf einen unbegründeten selbst ergänzten Guard bezogen werden. Abgenommener Vorschlag: Die Grenze folgt Anforderungen, realen Abhängigkeiten und konkreten Fehlerfolgen; Alter, Existenz oder Fehlschlag allein begründen keine Autorität. Unbegründete Gesamtprüfung begrenzen, erforderliche Garantien und fremde Bytes erhalten und Abweichungen außerhalb melden. Bindende Owner-Hashes und Gesamtmanifestpflichten bleiben geschützt. Unklare Autorität vor abhängiger Änderung klären; erforderliche Garantien nur durch ausdrücklich autorisierte Vertragsänderung und neue Nachweise ändern.

Gezielter späterer Luna-Test: Zwei-Dateienintegration mit fremden Änderungen, einmal ohne Gesamtbaselinepflicht und einmal mit verbindlicher Gesamtgleichheit. Erwartet: Im ersten Fall Zusatzguard korrigieren, Ownerhashes und Erhaltungsprüfung behalten; im zweiten stoppen. Vor Transfer keinen Integrationserfolg behaupten. Der Wortlaut ist umgesetzt und gemeinsam abgenommen; Luna-Verständnis und Wirkung bleiben ungeprüft. Tatsächliche Modelltelemetrie unbekannt.

## Abgenommener Konsens zu allgemeinen Fixes

Scoville Ask: unabhängige Erstprüfung, vollständiger gegenseitiger Ergebnisaustausch und Abnahme desselben finalen Entwurfs, ASK-0053-CONSENSUS-R4. Angefordert: Sol 6.1/high, Handle /root/ask_sol0053_fixes_consensus; Opus 5.5/high, CLI-Session a75006c0-1587-4af9-8822-98eaaeb33ef4. Beide akzeptierten Umfang und Wortlaut ausdrücklich. Die beauftragte Umsetzung einschließlich Wiederverwendung wurde anschließend von denselben Reviewern angenommen, ASK-0053-OPEN-FIXES-R3 und Opus-R4. Keine sachlichen Einwände offen; tatsächliche Modell-/Efforttelemetrie unbekannt.

1. In der kanonischen skills/private/shared/runtime/native_output.md nur die Mustereinleitung „Use one checked read or capture per outer call.“ ersetzen:

   > Keep the complete `exec_command` result until the command ends, including `session_id`, every output chunk and the final exit status. Never shorten the call to `text((await tools.exec_command(...)).output)`: that discards process metadata. A completed outer script does not prove child completion. Use the template below for checked reads and captures, one per outer call.

2. In members/scoville-code/scoville-code/SKILL.md nur den Abschnitt von „Do not weaken tests“ bis einschließlich „Resolve unclear authority“ ersetzen. Einleitenden Schutzsatz und abschließenden Satz zu Status, Gründen, Fehlern, Quellen und Validierung behalten:

   > Never weaken a test, validator or guard to hide failure or obtain green output when it enforces an applicable requirement, verifies a real dependency or prevents a concrete failure consequence. A check's existence, age or failure alone establishes no authority. Limit a check to the boundary its supported purpose covers; preserve required guarantees and unrelated work, and report differences outside that boundary. Success within that boundary proves nothing beyond it. Changing a required guarantee requires an explicitly authorized contract change and evidence for the new contract; a general change request is not that authorization. Resolve unclear authority or boundaries before the dependent change.

3. In der kanonischen skills/private/shared/runtime/document_reader.md, Punkt 2, den Absatz von „The program is“ bis „assignments are documents“ ersetzen:

   > The program is `scripts/check_text_size.py`. Documents, including those of other Skills, belong in `--file`. Keep the verified launcher, full checker path and quoting unchanged. Copy the last correct complete command: change only `--part` for the reported next part; for another document change `--file` and reset `--part` to 1. Only named `.py` files may be Python programs; Skills, references and assignments are documents.

   In skills/private/shared/runtime/native_task_arguments.py nur die Texte von file_read_instruction() ändern:

   - Einstieg: `Program: {checker}. Keep this checker path and the verified launcher unchanged. Document: only the --file value, including documents of other Skills.`
   - Punkt 2: `Reader command: copy the whole command into the current tool shell. For the next part, copy the last correct complete command and change only --part to the reported next value. Do not nest another shell:`
   - Dokumentwechsel: `For another document, change only the --file value and reset --part to 1. Preserve the generated shell quoting and all other arguments.`

Ausgabeanweisung, Code-Absatz und Readertexte sind in dieser Reihenfolge umgesetzt; betroffene Kopien aus kanonischen Quellen erzeugt. Bestehende Limit-/Fehler-Recovery, Windows-Quoting, UTF-8-Diagnostik, Start-/Wartefehler, Exitstatus und Python 3.11+ bleiben erhalten. Kein exakter Versionstest oder neuer Launcher. Startup v2.4.12 benötigt keinen weiteren Fix; reine Fixturefehler und berechtigte Owner-Hashstopps ebenfalls nicht.

Gezielte spätere Luna-Medium-Aufgaben, ohne Umsetzung:

- Prozess: aktive Session mit leerem Output bis Exit 1 verfolgen; sofort abgeschlossenen Aufruf ohne unnötiges Polling behandeln; verlorenen Handle ohne Effektwiederholung behandeln und abhängige Arbeit bis zum vollständigen Beleg derselben Ausführung und ihres Endes stoppen.
- Guards: passende Owner-Hashes mit ausschließlich fremden historischen Abweichungen von Owner-Mismatch und bindender Gesamtmanifestpflicht unterscheiden. Unbegründete Gesamtprüfung begrenzen, fremde Bytes erhalten und Abweichungen melden; keine Gesamtbaseline behaupten. Eine reale Abhängigkeit außerhalb der Owner schützen oder ihre unklare Autorität zuerst klären.
- Reader: beim Folgeteil nur --part ändern; beim Dokumentwechsel nur --file ändern und Teil 1 setzen; nach fehlendem Programm letzten korrekten vollständigen Befehl wiederherstellen und vollständig ab Teil 1 lesen, bevor abhängige Arbeit weitergeht.

Für die geänderte Helper-Ausgabe nur den betroffenen bestehenden Reader-Ausgabetest prüfen; keine pauschale Python-Testkampagne. Reviewer-Abnahme belegt weder Luna-Verständnis noch Fixwirksamkeit.

## Erfolgreiche Syntaxprüfungen ohne neue Voraussetzung wiederholt

Quelle: Worker5 01a12185-67e1-7120-8bf9-7baa23e11d68, Turn 01a12185-68c1-7180-9989-53f5f84e5f90. Nach den letzten sichtbaren Codeänderungen bestand ein relevanter PHP74-Verhaltenstest. Vier Syntaxprüfungen bestanden ebenfalls: AnalysisService.php (exec-65fab2f7-fb01-4dff-9af4-e66946691398), SettingsPage.php (exec-e718cd61-de97-4740-9724-1802a8cf0f75), CredentialVault.php (exec-128b75e6-48be-4e02-a48a-797a6ca0f77e) und ProviderManager.php (exec-51e5aae0-741c-4e05-be8e-1203496d44ca).

Direkt danach wurden dieselben vier Lints mit gleichem Runtime-/Konfigurationsstand erneut ausgeführt, alle Exit 0: exec-26641447-701f-45ee-a048-ceca0696f3ab, exec-c149847b-6f96-41bf-b1b7-ffa25515ddcb, exec-7ffec730-a762-4037-85fc-d73176bb11b7 und exec-0a84b440-994e-4ee5-b526-78ffb7aeedc4. Keine intervenierende Änderung, fehlgeschlagene Prüfung oder neue Beweisfrage ist in der tatsächlichen Folge sichtbar. Wirkung: vier zusätzliche Ausführungen ohne neuen entscheidenden Beleg. Der erste Lintblock nach dem Verhaltenstest ist dadurch nicht als unnötig belegt; beide können unterschiedliche Aussagen prüfen. Keine falsche Fertigmeldung beobachtet.

Scoville Ask, angefordert Sol 6.1/high, ASK-0053-REPEAT-1, bestätigte den Anwendungsfehler innerhalb der sichtbaren Folge. Zuständigkeit: Scoville Code, references/validation.md, „Stop repetition“, erster Absatz. Plausible Erklärung: Die Anleitung beginnt mit erlaubten Wiederholungen statt mit Wiederverwendung; der genaue Entstehungsmechanismus ist unbekannt. Der Worker hatte die relevanten Regeln vollständig geladen. Kleinster allgemeiner Vorschlag: den bestehenden Absatz ersetzen, Tabelle und Regeln für veraltete Ergebnisse erhalten:

> Reuse completed work, reviewed unchanged content and complete passing results while their requirements, inputs and relevant conditions, such as files, dependencies, runtime, configuration and environment, remain unchanged. A new Step, role, assignment, review or release phase alone does not justify repeating them; a required independent review of content no reviewer has assessed is not a repetition. Repeat only the affected work for a relevant change, a still-unanswered question or a binding protocol; name the new result or evidence it can add. Concurrency, stochastic or flaky claims may require repeated observations tied to the actual claim.

Der gemeinsam abgenommene Absatz ist umgesetzt. Codes Haupttext erfasst jetzt „adding or repeating“; die finale Evidenzanweisung verlangt keinen Neulauf bestandener Checks bei unveränderten Inputs und Bedingungen. Spätere Luna-Probe: unveränderten erfolgreichen Lint wiederverwenden; nach relevanter Änderung betroffene Checks erneut ausführen; erste unabhängige Reviews und bindende Wiederholungsprotokolle erfüllen. Kein Prüfbuch, Deduplizierungsdienst oder neuer Python-Helfertest. Fixwirksamkeit noch ungeprüft. Private Überlegungen fehlen, Änderungen außerhalb der sichtbaren Folge sind nicht ausgeschlossen; tatsächliche Adviser-Modelltelemetrie nicht offengelegt.

Die separate Manifest-Discovery mit unvollständigen Ausgaben ist kein zusätzlicher bestätigter Befund: Suchmuster wurden geändert, die lesende Suche anschließend vollständig veröffentlicht, und abhängige Integration auf fehlender Evidenz war nicht beobachtet. Gleiche Bytezahlen beweisen keine identischen Inhalte; keine Host-Trunkierung oder Helperursache daraus abgeleitet.

## Prüfung auf zeitraubende Rituale

Die einmalige Nutzerprüfung schließt W-378s Abnahme durch Manager5 01a1217f-3354-7703-aac1-b641a275f102 ein: einmalige Planvalidierung exec-32fede07-3f16-46b9-98d2-8577b9d395ef, einmaliger Kontextcheckpoint exec-00930e3c-b473-4975-890c-99c8e98eb99a und native Übergabe msg_08e459cb55aa4e58016ac922ea5d148191b67afca5f4603910. Keine Wiederholung der Worker-Tests. Der finale Reviewer 01a121a8-8302-7ec2-ba5b-b7b2cd98b414 übernahm die unveränderte Bewertung der Steps 1–2 und prüfte Step 3. Die Fixturekorrektur änderte eine relevante Voraussetzung.

Manager6 01a121ac-df8c-7012-aedb-41005be72144 lud die neuen Rollenunterlagen. Auf den diagnostizierten Selektorfehler exec-52e53267-0cfc-4f07-a74f-d53a6178d3c4 folgte exec-f916079e-cbb5-4947-9cbc-7aed34b9b858 mit korrigierter Auswahlgrenze 24439 statt 7500 Bytes. Das ist geänderte Recovery. Sol und Opus erhielten diese tatsächlichen Beobachtungen und bestätigten keinen weiteren Ritualfehler.

Offene Effizienzfrage: Manager und Reviewer lasen beide den vollständigen 37308-Byte-Diff. Workflow operations.md verlangt Managerinspektion nur soweit für Scope und Abnahme nötig; operations-dispatch.md erlaubt die Erzeugung ohne vorherige Anzeige. Eine doppelte Bewertung ohne Qualitätsgewinn ist hier nicht belegt. Daher kein zusätzlicher Skillfix und keine Aufhebung unabhängiger Reviews. Dauer und wiederholte Bytes allein begründen keinen Fehler.

## Umsetzung und Checks

Fünf kanonische Dateien geändert und gemeinsame Kopien synchronisiert. Sync-Prüfung und beide Git-Diffprüfungen bestehen. Die vier Profil-/Layout-Testprojektionen wurden erzeugt. Der bestehende RuntimeHelpers.test_generated_part_read_and_memory_capture_reach_host_shell besteht: Unicode, Leerzeichen und Apostroph im Readerpfad, begrenzte Folgeteile, beide Capture-Streams und Exit 7. Keine Testdatei geändert und kein pauschaler Python-Testlauf.

Skill Creator quick_validate lehnt in beiden Code-Profilen das vorhandene unveränderte Frontmatter-Feld compatibility ab. Die Suite-Payloadprüfung unterstützt es; es wurde nicht für einen grünen Validator entfernt. Sol prüfte den tatsächlichen Patch und die Verbraucher; Opus prüfte zusätzlich die vollständigen gelieferten Git-Diffs gegen die sauberen Ausgangsversionen. Beide akzeptieren denselben Stand. Die Abnahme beweist weder Luna-Verständnis noch praktische Vermeidung doppelter Arbeit. Nur Quellen und Testprojektionen aktualisiert; kein Commit, keine Installation oder Veröffentlichung.

## Aktueller geprüfter Umfang

Erstfenster ab Startturn und relevante Deltas geprüft. W-378s Step-3-Nachweise und unabhängige Abnahme sowie Manager5s Abschluss und Übergabe sind beobachtet. Manager6s tatsächliche Aktionen wurden bis exec-221bbfb8-2522-42a8-b454-5d9b528bb32d geprüft: Plan edit.md Teil 1, Folgeteil an dieser Grenze offen. Kein unbegründeter Ganzprojektreview oder vorzeitiger Gesamtabschluss beobachtet. Ein späterer Statussnapshot des Runners zeigt einen laufenden W-379; er ist kein Aktionsaudit und verschiebt diese Grenze nicht.

Angeforderte Paare: Manager Sol 6.1/medium, Worker Sol 6.1/high, Reviewer Astra/high; tatsächliche Modelltelemetrie teilweise unbekannt. Native Nachrichtenargumente begrenzen den vollständigen Handshake-Nachweis. Gekürzte Retrievalausgaben belegen keine ursprüngliche Trunkierung. Der Abschlussreport wurde noch nicht beobachtet. Keine eigenen EMPCO-Tests, Änderungen, Stopps oder Agentennachrichten.
