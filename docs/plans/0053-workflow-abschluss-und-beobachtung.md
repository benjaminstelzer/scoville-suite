---
format_version: 1
id: PLAN-0053
status: active
created: 2026-10-09
updated: 2026-10-10
current_item: W-015
---

# Kurzen Workflow-Abschluss ausliefern und neuen EMPCO-Lauf beobachten

## Goal

Die beauftragten Scoville-Korrekturen ausliefern und die Veröffentlichung vereinfachen. Die EMPCO-Beobachtung ist beendet. Den Plan Viewer als unabhängige Anwendung lokal und auf GitHub pflegen.

## Non-goals

Keine EMPCO-Projektänderungen, Tests, Stopps oder Nachrichten an dessen Kinder. Nur die beauftragten Runner-Nachrichten zur Änderung und Neuladung. Keine Zugriffe auf XMAPI, XMTEST, Holzbau oder Zugangsdaten. Keine allgemeinen Fortschrittsmeldungen aus der Beobachtung. Keine Fixes aus ungeklärten Beobachtungen oder reinen Produkt-/Fixturefehlern.

## Work items

### W-001 Abschlussvorgabe ausliefern

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Der geprüfte Build enthält die kurze Abschlussvorgabe, ist lokal installiert und auf geänderten GitHub-Zielen veröffentlicht; der neue EMPCO-Runner kennt die Änderung.
Acceptance: Abschluss nennt knapp den tatsächlich erledigten Umfang und wichtige offene Grenzen mit klickbarem Reportlink; vollständiger Reportread, Quieszenz und unmittelbare Problemweitergabe bleiben erhalten; alle Manifestziele verglichen, nur geänderte veröffentlicht; lokale Pakete und Remote-Dateien entsprechen dem Build; neue Releases, Tags und notwendige Assets verifiziert.
Instructions: []
Steps:
1. [status: done] Abschlussregeln in Workflow-SKILL.md und references/run-feedback.md prüfen, passende Changelogversion eintragen und Quellen committen. Bestehende Abschlusseinträge von PLAN-0052 erhalten.
2. [status: done] Einzigen Build unter skills/temp/release aktualisieren, betroffene Paketprojektionen und Metadaten prüfen, unveränderte Laufzeit- und Viewer-Nachweise wiederverwenden und lokale Installationen aktualisieren.
3. [status: done] Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5 auf Host local zur Neuladung informieren, geänderte Distributionen pushen und Releases veröffentlichen. Remote-Bytes und Assets vor Ersatzrelease-Bereinigung prüfen.
Evidence: 13 Skills bytegleich; Runner informiert. v2.4.11 / 112f698 mit Dateien und 14 Assets verifiziert; ein Release/Tag. Details: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-003 Neuen Lauf von alter Übernahme unterscheiden

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Der neue EMPCO-Lauf setzt nach geklärter Startup-Sperre fort; die ausgelieferte Skillvorgabe verhindert pauschale rückwirkende Agentnachweise.
Acceptance: Neue Aktivierung verlangt keine alten Agent-IDs oder Abschaltnachweise; konkrete konkurrierende Writer und Same-run-Recovery bleiben abgesichert; Runner erhält Nutzerkorrektur und lokalen Reloadstand; neuer Build, lokale Pakete, Push und Release verifiziert.
Instructions: []
Steps:
1. [status: done] Tatsächlichen Runnerstart und eingefügten Auftrag prüfen, Ursache belegen und Nutzerkorrektur an denselben Runner zur Fortsetzung übermitteln.
2. [status: done] Neue Aktivierung und Same-run-Recovery in Workflow-SKILL.md und references/operations.md knapp unterscheiden, Folgen prüfen und Quellen committen.
3. [status: done] Neuen Build unter skills/temp/release verifizieren, lokal aktualisieren und Reloadnachricht zustellen; geänderte GitHub-Ziele pushen und passendes neues Release samt Assets prüfen.
Evidence: Workerstart belegt; 13 lokale Skills aktualisiert, Reload zugestellt. v2.4.12 / 9162fda samt 14 Assets verifiziert: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-002 Anwendung im neuen Lauf beobachten

Status: cancelled
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0209]
Outcome: Neue bestätigte Scoville-Defekte und wiederholte Anwendungsfehler sind mit Ursache, kleinstem Fixvorschlag und Sichtbarkeitsgrenze dokumentiert.
Acceptance: Tatsächliche Aktionen des benannten neuen Laufs einschließlich Rollen, geladener Regeln, Übergaben, Reviews, zielgerechter Checks und Planfortschritt geprüft; neue relevante Befunde durch Ask mit Sol 6.1/high bewertet; Nutzer nur bei neuen bestätigten Ablauffehlern, notwendiger Entscheidung, Beobachtungsfehler oder Abschluss informiert; bei Laufende oder Nutzerstopp Schlussbewertung und Automation gelöscht.
Instructions: Nutzerstopp am 2026-10-10. Keine weitere EMPCO-Beobachtung oder Agentennachricht.
Steps:
1. [status: done] Automation alle fünf Minuten für Thread 01a120d7-5fcf-7122-b741-76eb3a203fc5 einrichten. Erstes Fenster ab Startturn 01a120d7-6328-79c3-bc8e-adf922ea306e tatsächlich prüfen; danach nur neue relevante Ereignisse. Aktuellen Stand unter temp/2026-10-09-empco-abschluss-beobachtung/state.json überschreiben.
2. [status: cancelled] Neue relevante Befunde gebündelt über Scoville Ask beurteilen und knapp in docs/testing/0053-empco-abschluss-befunde.md erfassen. Ohne neue Befunde keine Konsultation oder Planänderung.
3. [status: done] Nur diesen Lauf bis Ende oder Nutzerstopp beobachten, tatsächlich geprüften Umfang abschließend bewerten und Automation löschen.
Evidence: Nutzerstopp; Automation gelöscht. Audit bis 01:09 UTC, spätere Aktionen ungeprüft. Nötige Fixes ausgeliefert: [Befunde](../testing/0053-empco-abschluss-befunde.md).

### W-004 Offene Skillfixes und Wiederverwendung umsetzen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die offenen Klarstellungen verlangen Wiederverwendung unveränderter Ergebnisse und erhalten vollständige Prozessinformationen, Reader-Aufrufe und begründete Prüfgrenzen; ihre praktische Wirkung bleibt ungeprüft.
Acceptance: Sol 6.1/high und Opus 5.5/high haben den gemeinsamen Entwurf und die Änderungen geprüft; erfolgreiche unveränderte Checks und Reviews werden wiederverwendet, notwendige neue Nachweise bleiben erhalten; kanonische Quellen und generierte Kopien stimmen überein; relevante Checks bestehen, ungeprüfte Wirkung ist benannt.
Instructions: Kein neuer Releaseauftrag.
Steps:
1. [status: done] Bestehende Reviewer zu Wiederverwendung und den drei offenen Konsensfixes konsultieren und ihre Ergebnisse austauschen.
2. [status: done] Code validation.md und SKILL.md sowie shared/runtime/native_output.md, document_reader.md und native_task_arguments.py gezielt ändern; betroffene Kopien aus kanonischen Quellen erzeugen.
3. [status: done] Betroffene Struktur und Reader-Ausgabe prüfen; Änderungen von denselben Reviewern gegenprüfen und offene Grenzen knapp im Befundbericht aktualisieren.
Evidence: Sol/Opus nehmen Patch an; Sync und Reader-Test bestehen. Validatorgrenze, Luna-Wirkung und Auslieferung: [Befunde](../testing/0053-empco-abschluss-befunde.md).

### W-005 Abgenommene Skillfixes ausliefern

Status: done
Depends on: [W-004]
Blocked by: []
Decisions: []
Outcome: Die abgenommenen Fixes sind gebaut, lokal installiert und auf den geänderten GitHub-Zielen veröffentlicht.
Acceptance: Quellen und Paketprojektionen stimmen überein; lokale Skills entsprechen dem Build bei erhaltenen Einstellungen; alle manifestierten Ziele verglichen, geänderte mit passender Version veröffentlicht; Remote-Bäume, Tags und erforderliche Assets verifiziert. Keine ungetestete Luna- oder Live-Wirkung behauptet.
Instructions: []
Steps:
1. [status: done] Quellen und Versionsnotizen committen, einzigen Releasebuild aktualisieren und betroffene Paket-/Kompatibilitätsgrenzen prüfen; unveränderte Runtime- und Viewer-Nachweise wiederverwenden.
2. [status: done] Lokale Codex-/Claude-Skills aus geprüften Paketen aktualisieren und bytegleich prüfen, persönliche Einstellungen erhalten.
3. [status: done] Geänderte manifestierte GitHub-Ziele pushen und Releases mit passenden Assets veröffentlichen; Remote-Bytes und Ersatzreleases vor Bereinigung prüfen.
Evidence: 13 lokale Pakete bytegleich, sieben Releases mit Remote-Bäumen und Assets verifiziert; je ein Release/Tag. Luna-Wirkung offen: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-006 Reload mitteilen und Luna-Verständnis prüfen

Status: done
Depends on: [W-005]
Blocked by: []
Decisions: []
Outcome: Der Runner kennt den neuen Reloadstand; gezielte Luna-Medium-Fälle zeigen Verständnis und verbleibende Grenzen der vier Korrekturen.
Acceptance: Reloadnachricht an den benannten Runner zugestellt; frische Luna 6/Medium-Kontexte beantworten konkrete Fälle am installierten Text ohne Umsetzung oder sichtbare Musterantworten; Ergebnisse gegen vorher festgelegte Erwartungen bewertet, Testprobleme von Skillproblemen unterschieden; keine allgemeine Wirksamkeit behauptet.
Instructions: []
Steps:
1. [status: done] Runner 01a120d7-5fcf-7122-b741-76eb3a203fc5 über v2.4.13 und Reload am sicheren Übergabepunkt informieren.
2. [status: done] Durch Scoville Ask frische Luna-Medium-Verständnisblöcke zu Wiederverwendung, Prozessende, Reader-Aufrufen und Guardgrenzen prüfen; positive und begründete Stop-/Wiederholungsfälle trennen.
3. [status: done] Vollständige native Ergebnisse auswerten und knappe Befunde mit verbleibenden Grenzen im bestehenden Befundbericht festhalten; danach Beobachtung fortsetzen.
Evidence: Runner informiert, writing.md neu gelesen. 21 klare Luna-Erstentscheidungen korrekt; Test- und Antwortgrenzen getrennt: [Befunde](../testing/0053-empco-abschluss-befunde.md).

### W-007 Reader-Folgefehler korrigieren und ausliefern

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0209]
Outcome: Der Readertext trennt Pythonprogramm und Dokument an ihren Argumentpositionen verständlich; geprüfte Pakete sind lokal und auf geänderten GitHub-Zielen ausgeliefert und der Runner kennt den Reloadstand.
Acceptance: Sol 6.1/high und Opus 5.5/high erreichen nach gegenseitigem Ergebnisaustausch Konsens und nehmen den tatsächlichen Patch ab; erforderliche Reader-, Limit-, UTF-8-, Recovery- und Quotinggarantien bleiben erhalten; gezielte technische und Luna-Medium-Proben bestehen mit ehrlich benannten Grenzen; lokale Pakete und Remote-Dateien entsprechen dem verifizierten Build, Releases und notwendige Assets sind geprüft, Runner informiert und Beobachtung wieder aktiv.
Instructions: Überwachung bleibt während der Fixphase pausiert. Keine EMPCO-Projektänderungen oder Tests.
Steps:
1. [status: done] Beide bestehenden Reviewer zum Reader-Folgefehler und kürzesten allgemeinen Ersatz in shared/runtime/document_reader.md und native_task_arguments.py beraten lassen und vollständige Ergebnisse bis zum Konsens austauschen.
2. [status: done] Kanonische Texte gezielt ersetzen, betroffene Kopien erzeugen, erforderliche technische und Luna-Medium-Verständnisproben prüfen und den tatsächlichen Patch von beiden Reviewern abnehmen lassen.
3. [status: done] Quellen committen, einzigen Releasebuild aktualisieren und lokal installieren; Runner zum sicheren Reload informieren, geänderte Manifestziele pushen und Releases samt Remote-Bytes und Assets verifizieren; Überwachung für denselben Lauf fortsetzen.
Evidence: Sol/Opus-Abnahme, Consumer-Test und neun Luna-Fälle bestehen; 13 Pakete und sieben Releases geprüft, Runner informiert: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-008 Python-Helferaufruf klären und nötigen Fix ausliefern

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0209]
Outcome: Der beobachtete direkte Start einer Pythondatei nach --run wird unabhängig bewertet und ein begründeter allgemeiner Fix geprüft ausgeliefert.
Acceptance: Sol und Opus tauschen vollständige Ergebnisse bis zum Konsens aus; nur bestätigte Ursachen führen zu einem kurzen Ersatztext; nötige Garantien bleiben erhalten; tatsächlicher Patch, gezielte Checks, Luna-Verständnis und gegebenenfalls Build, lokale Installation, Runnerhinweis und GitHub-Releases sind geprüft.
Instructions: Überwachung während dieser Fixphase pausiert. Keine EMPCO-Projektänderungen oder Tests; keine erneute Beratung unveränderter bekannter Befunde.
Steps:
1. [status: done] Den tatsächlichen WinError-193-Aufruf und erfolgreiche Korrektur von beiden bestehenden Reviewern unabhängig beurteilen lassen und vollständige Ergebnisse austauschen.
2. [status: done] Begründeten minimalen Fix umsetzen, gezielt technisch und mit Luna Medium prüfen und von beiden Reviewern abnehmen lassen.
3. [status: done] Nötigen Build lokal und auf GitHub ausliefern, Runner zum sicheren Reload informieren und Beobachtung desselben Laufs fortsetzen.
Evidence: Sol/Opus-Abnahme, fünf klare Luna-Entscheidungen, 13 lokale Pakete und sieben Releases geprüft; Runner informiert: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-009 Wiederholte Suchpfadfehler gezielt korrigieren

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0209]
Outcome: Die zwei neuen rg-Aufrufe mit Wildcards im Pfad sind unabhängig bewertet und ein begründeter allgemeiner Fix ist geprüft ausgeliefert.
Acceptance: Sol und Opus erreichen nach vollständigem Ergebnisaustausch Konsens; ein nötiger kurzer Ersatztext bewahrt gültige Suchen und Capture-Garantien; tatsächlicher Patch, gezielte Checks und Luna-Verständnis sind geprüft; nötiger Build, lokale Installation, Runnerhinweis und GitHub-Releases verifiziert.
Instructions: Überwachung während der Fixphase pausiert. Keine EMPCO-Änderungen oder Tests; normale Pfadexploration und reine Fixturefehler getrennt halten.
Steps:
1. [status: done] Beide bestehenden Reviewer zu tatsächlichen Aufrufen, geladenem rg-Text und kleinstem begründetem Ersatz beraten lassen; vollständige Ergebnisse zum Konsens austauschen.
2. [status: done] Nötigen kanonischen Fix umsetzen, gezielt und mit Luna Medium prüfen und tatsächlichen Patch von beiden Reviewern abnehmen lassen.
3. [status: done] Nötigen Build lokal und auf GitHub ausliefern, Runner zum sicheren Reload informieren und Beobachtung desselben Laufs fortsetzen.
Evidence: Sol/Opus-Abnahme, fünf gezielte Luna-Entscheidungen mit Testgrenzen, 13 lokale Pakete und sieben Releases geprüft; Runner informiert: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-010 Temporäre Veröffentlichung während Managerübernahme klären

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0209]
Outcome: Die Selektor-Veröffentlichung vor TAKEOVER_COMPLETE ist unabhängig bewertet und ein nötiger allgemeiner Fix geprüft ausgeliefert.
Acceptance: Sol und Opus erreichen nach vollständigem Austausch Konsens und nehmen einen nötigen kurzen Patch ab; Eigentümerschaft und vollständige Reads bleiben erhalten; gezielte Luna-Proben, Build, lokale Updates, Runnerhinweis und nötige GitHub-Releases sind verifiziert, Grenzen benannt.
Instructions: Überwachung während der Fixphase pausiert. Keine EMPCO-Änderungen oder Tests; temporäre Ausgabe von Produktwirkung unterscheiden.
Steps:
1. [status: done] Tatsächliche Übernahmeaktionen und geladene Regeln von beiden bestehenden Reviewern beurteilen lassen; vollständige Ergebnisse zum Konsens austauschen.
2. [status: done] Nötigen kleinen kanonischen Fix umsetzen, gezielt mit Luna Medium prüfen und tatsächlichen Patch abnehmen lassen.
3. [status: done] Nötigen Build lokal und auf GitHub ausliefern, Runner zum sicheren Reload informieren und Beobachtung desselben Laufs fortsetzen.
Evidence: Aus b0a8b5e ausgeliefert: 13 lokale Pakete, sieben GitHub-Ziele samt Assets verifiziert; Reload zugestellt. [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-011 Build und veröffentlichten Export konsistent halten

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0209]
Outcome: Ein bestätigter Auslieferungsfehler ist korrigiert; Build, lokale Pakete und veröffentlichte Exporte stimmen überein.
Acceptance: Sol und Opus erreichen nach vollständigem Austausch Konsens über Ursache und kleinste allgemeine Sicherung; ein nötiger Patch ist abgenommen und gezielt geprüft. Lokale Anpassungen bleiben geschützt; verifizierter Build, lokale Updates, Runnerhinweis und GitHub-Releases sind vollständig abgeschlossen.
Instructions: Mit W-010s nötiger Auslieferung bündeln; Überwachung bleibt pausiert. Keine EMPCO-Änderungen oder Tests.
Steps:
1. [status: done] Tatsächliche ältere Build-/Exportabweichung unabhängig beurteilen lassen und kleinste allgemeine Korrektur vereinbaren.
2. [status: done] Nötigen Fix abnehmen und gezielt prüfen; nur betroffene veraltete Build-/Exportnachweise erneuern.
3. [status: done] Zusammen mit W-010 verifiziert ausliefern und Überwachung desselben Laufs fortsetzen.
Evidence: Aus b0a8b5e ausgeliefert: 13 lokale Pakete, sieben GitHub-Ziele samt Assets verifiziert; Reload zugestellt. [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-012 Wiederholten Python-Aufruffehler allgemein korrigieren

Status: done
Depends on: [W-008, W-011]
Blocked by: []
Decisions: [ADR-0209]
Outcome: Der erneut falsch gestartete Pythonhelper und vermeidbare Recovery-Verwaltung sind unabhängig bewertet; ein nötiger kleiner allgemeiner Fix ist geprüft ausgeliefert.
Acceptance: Sol und Opus tauschen vollständige Vorschläge und Patchreviews bis zum Konsens aus; nötiger Fix erhält vollständige Ausgabe, ehrliche Fehler, Rollen und Freigabegrenzen. Gezielte Checks und Luna-Medium-Verständnis, nötiger Build, lokale Updates, Runnerhinweis und GitHub-Releases sind verifiziert. Keine Wirkung ohne Nachweis behauptet.
Instructions: Überwachung während der Fixphase pausiert. Keine EMPCO-Änderungen oder Tests; reine Fixturebefunde getrennt halten.
Steps:
1. [status: done] Manager14s tatsächlichen WinError-193-Aufruf nach geladenem W-008-Text sowie Recovery-Aufwand von beiden bestehenden Reviewern beurteilen lassen; vollständige Ergebnisse zum Konsens austauschen.
2. [status: done] Nötigen kleinsten kanonischen Fix umsetzen, gezielt und mit Luna Medium prüfen; tatsächlichen Patch von beiden abnehmen lassen.
3. [status: done] Nötigen Build lokal und auf GitHub ausliefern, Runner zum sicheren Reload informieren und Beobachtung desselben Laufs fortsetzen.
Evidence: Sol/Opus-Konsens, Checks, Luna und Runtime-Matrix bestehen; 13 lokale Pakete, sieben Releases samt Assets geprüft, Reload zugestellt: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-013 Vollständige unveränderte Kontextabfragen wiederverwenden

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0209]
Outcome: Die unmittelbar doppelte erfolgreiche Kontextabfrage ist unabhängig bewertet; eine begründete allgemeine Verbesserung vermeidet Wiederholung bei erhaltenen Aktualitäts- und Reviewgrenzen.
Acceptance: Sol und Opus erreichen nach vollständigem Ergebnisaustausch Konsens. Ein nötiger kleiner Quellenfix ist von beiden abgenommen, gezielt und mit Luna Medium geprüft, gebaut, lokal installiert und auf allen geänderten Manifestzielen veröffentlicht und verifiziert; Runner informiert. Kein neuer Prüfrhythmus oder unbelegte Live-Wirkung. Bei begründetem Konsens ohne Quellenfix dessen Grenze festhalten und Beobachtung fortsetzen.
Instructions: Überwachung pausiert. Keine EMPCO-Änderungen oder Tests; bekannte unveränderte Befunde nicht neu beraten. W-002 nach Abschluss fortsetzen und Auditgrenzen erhalten.
Steps:
1. [status: done] Die identischen erfolgreichen Manager15-Aufrufe von den bestehenden Reviewern beurteilen lassen und vollständige Ergebnisse zum Konsens austauschen.
2. [status: done] Nötigen kleinsten kanonischen Ersatz umsetzen, gezielt und mit Luna Medium prüfen und den tatsächlichen Patch von beiden abnehmen lassen.
3. [status: done] Nötigen Build lokal und auf GitHub geprüft ausliefern, Runner zum sicheren Reload informieren und Beobachtung desselben Laufs fortsetzen.
Evidence: Beide Reviews, Checks und nötige Matrix bestanden; lokal und zwei Releases geprüft, Reload zugestellt: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-014 Runtime-Nachweise für geprüfte reine Instruktionen wiederverwenden

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0209]
Outcome: Das Runtime-Gate entspricht dem bestehenden Release-Test-Scope und erhält geschützte Abhängigkeiten sowie vollständige aktuelle Paketintegrität.
Acceptance: Beide Reviewer vereinbaren eine positive Einstufung mit geschütztem Standard, unveränderten Plattformnachweisen und gebundenem Scope; tatsächlicher Patch und gegenseitige Reviews bestanden. Gezielte Kontrasttests und frische Matrix bestehen; zusammen mit W-013 gebaut, lokal installiert und auf geänderten Manifestzielen verifiziert veröffentlicht, Runner informiert. Alte Evidenz erhält keinen unbelegten Wiederverwendungs-Pass.
Instructions: Nur geprüfte reine Instruktionen einstufen; zunächst operations.md. Überwachung bleibt bis zur gemeinsamen Auslieferung pausiert.
Steps:
1. [status: done] Vollständige Vorschläge austauschen und konservativen Daten- und Gate-Vertrag vereinbaren.
2. [status: done] Kanonischen Gate-Fix umsetzen, gezielt prüfen und tatsächlichen Patch von beiden Reviewern mit Ergebnisaustausch abnehmen lassen.
3. [status: done] Nötige frische Runtime-Matrix und gemeinsame Auslieferung mit W-013 verifizieren; danach Beobachtung desselben Laufs fortsetzen.
Evidence: Beide Reviews, Checks und nötige Matrix bestanden; lokal und zwei Releases geprüft, Reload zugestellt: [Auslieferung](../testing/0053-abschluss-auslieferung.md).

### W-015 Skill-Veröffentlichung ohne GitHub-Releases

Status: in_progress
Depends on: []
Blocked by: []
Decisions: [ADR-0210, ADR-0211]
Outcome: Skills werden ohne Releases veröffentlicht. Der Plan Viewer besitzt ein unabhängiges lokales Quellrepository und das GitHub-Repository scoville-plan-viewer mit geprüften Downloads.
Acceptance: Viewer-Quellhistorie, eigenständige Builds, Plan-Kompatibilität und Downloadprüfungen bleiben erhalten; keine zweite gepflegte Viewer-Kopie. GitHub-Skill, Workspace-Regeln und Buildprozess stimmen überein; Branch-, Paket- und Runtimeprüfungen erhalten. Beide Reviewer nehmen den tatsächlichen Patch nach Ergebnisaustausch ab; gezielte Checks und Luna-Verständnis bestehen. Lokale Quellen, generierte Distributionen und Installationen stimmen überein. Neues Viewer-Release verifiziert, danach zehn alte Skill-Releases entfernt; Tags, Sichtbarkeit, Einstellungen und fremde Produkt-Releases erhalten.
Instructions: EMPCO-Überwachung beendet. Keine EMPCO-Zugriffe. Nur benannte Skill-Repositories ändern; Produkt-Releases und Git-Historie erhalten.
Steps:
1. [status: done] Viewer-Historie nach projects/scoville-plan-viewer extrahieren; eigenständige Actions und Viewer-Gate, Releasepolitik und Skill-Publikationsgate umstellen; beide Reviewer beraten und Patch abnehmen lassen.
2. [status: in_progress] Gezielte Checks und Luna-Proben ausführen; vorhandene Viewer-Binaries mit identischen Anwendungsquellen und ursprünglichem Buildnachweis übernehmen, ohne nativen Neubuild. Erst nach geprüftem Release und Downloads generierte Skillquellen und Builds prüfen, lokal aktualisieren und geänderte Distributionen mit Downloadlinks pushen.
3. [status: todo] Nach verifiziertem Ersatz zehn alte Skill-Releases löschen, neues Viewer-Release, Downloadlinks und Remote-Bäume prüfen; Plan schließen.
Evidence: Beide Reviewer haben nach vollständigem gegenseitigem Patchreview Konsens; Checks und vier Luna-Erstentscheidungen bestanden. [Quellenabnahme und Auslieferungsstand](../testing/0053-viewer-trennung.md).
